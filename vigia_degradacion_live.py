#!/usr/bin/env python3
"""Vigía diario: degradación shadow→ejecutado en GBM_LATE_15M SOL/ETH BUY_YES
(las 2 únicas tuplas en pares_permitidos_live, dinero real).

Origen (12-Jul, petición Javi tras el hallazgo de fill-ability en las 8
candidatas): el IC "de papel" (shadow, todas las señales) no se traduce 1:1
al hit rate de las señales que de verdad se ejecutan — selección adversa de
contraparte (ver project_status_candidatas_12jul). Las 2 tuplas live YA
muestran esta misma degradación (shadow SOL 62.3%/ETH 59.4% hit → ejecutado
real 51.8%/46.3%) pero siguen rentables porque el precio de entrada moderado
compensa. Este vigía vigila si la ventana RECIENTE (últimos 30 trades
ejecutados) cruza a pnl/trade negativo — la señal de que la degradación se
acerca al punto de no retorno, antes de que duela varios días seguidos.

Corre 1 vez al día (cron). Log histórico en data/shadow/degradacion_live.csv
(para ver la tendencia día a día, no solo el snapshot actual). Alerta por
Telegram con histéresis por par: avisa al cruzar a negativo, no vuelve a
avisar hasta que se recupere por encima de +0.05€/trade (evita spam diario
si se queda pegado justo en el borde).

Read-only, no toca dinero ni config.
"""
import csv
import json
import statistics as st
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

RESULTS = REPO / "data/shadow/results.csv"
TRADES = REPO / "data/live/trades.csv"
CONFIG_LIVE = REPO / "data/live/config_live.json"
OUT = REPO / "data/shadow/degradacion_live.csv"
LATCH = REPO / "data/live/vigia_degradacion_live_latch.json"

VENTANA_RECIENTE = 30
UMBRAL_RECUPERACION = 0.05  # €/trade — por encima de esto se resetea el latch

# Fail-safe (13-Jul, propuesta #4 lista puntos ciegos): si config_live.json no
# se puede leer, monitorizar las tuplas conocidas de HOY en vez de vigilar la
# nada — mismo espíritu fail-safe que _es_par_live_protegido en shadow_predict.
_FALLBACK_TUPLAS = [("GBM_LATE_15M", "SOL", "15min", "BUY_YES"),
                    ("GBM_LATE_15M", "ETH", "15min", "BUY_YES")]

_CAMPOS = ["fecha", "par", "n_shadow", "ic_shadow", "n_ejecutado_total",
           "hit_total_pct", "pnl_trade_total", "var_total", "n_ult30", "hit_ult30_pct",
           "pnl_trade_ult30", "var_ult30"]

# 16-Jul (petición Javi, tras análisis de la racha real 09-16Jul): además de la
# media, trackear la VARIANZA de pnl/trade — una racha de días negativos puede
# caer dentro de la varianza normal (std~1.2-1.9€ ya medido) o ser una ruptura
# real; sin la serie temporal de varianza no se puede distinguir un caso del
# otro sesión a sesión. Ver varianza_evolutiva.py para la trayectoria completa
# on-demand (cada 10 N); esto es el snapshot diario para construir la serie.
CAND_CAMPOS = ["fecha", "par", "n_shadow", "ic_shadow", "var_shadow_total",
               "n_shadow_ult30", "mean_shadow_ult30", "var_shadow_ult30"]
OUT_CAND = REPO / "data/shadow/degradacion_candidatas.csv"
N_MIN_CANDIDATA = 30


def _tuplas_live() -> list:
    """Lee pares_permitidos_live dinámicamente en vez de tener SOL/ETH
    hardcodeado — si la whitelist cambia mañana, este vigía la sigue solo."""
    try:
        cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
        pares = cfg.get("pares_permitidos_live", [])
        tuplas = []
        for p in pares:
            partes = p.split("#")
            if len(partes) == 4:
                tuplas.append(tuple(partes))
        return tuplas or _FALLBACK_TUPLAS
    except Exception:
        return _FALLBACK_TUPLAS


def _shadow_ic(strategy: str, subtype: str, direccion: str):
    n, hits = 0, 0
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy") == strategy and r.get("subtype") == subtype
                    and r.get("decision") == direccion):
                n += 1
                hits += int(r.get("acierto") or 0)
    if n == 0:
        return 0, None
    ic = (hits + 1) / (n + 2) - 0.5
    return n, ic


def _tuplas_candidatas() -> list:
    try:
        cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
        pares = cfg.get("candidatos_evaluacion_live", [])
        tuplas = []
        for p in pares:
            partes = p.split("#")
            if len(partes) == 4:
                tuplas.append(tuple(partes))
        return tuplas
    except Exception:
        return []


def _pnls_shadow(strategy: str, subtype: str, direccion: str):
    pnls = []
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy") == strategy and r.get("subtype") == subtype
                    and r.get("decision") == direccion and r.get("pnl_neto") not in ("", None)):
                pnls.append((r.get("resolution_timestamp", ""), float(r["pnl_neto"])))
    pnls.sort(key=lambda x: x[0])
    return [p for _, p in pnls]


def _ejecutado_real(strategy: str, subtype: str, direccion: str):
    filas = []
    with open(TRADES, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy") == strategy and r.get("subtype") == subtype
                    and r.get("direction") == direccion and r.get("status") == "CLOSED"
                    and "maker_pilot=1" not in (r.get("notas") or "")):
                try:
                    filas.append((r.get("close_timestamp", ""), float(r.get("pnl_neto_eur") or 0),
                                  r.get("outcome_real") == "YES"))
                except ValueError:
                    continue
    filas.sort(key=lambda x: x[0])
    return filas


def main() -> int:
    from shadow_digest import enviar_telegram

    if not RESULTS.exists() or not TRADES.exists():
        return 0

    try:
        latch = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        latch = {}

    fecha = datetime.now(timezone.utc).date().isoformat()
    nuevo_archivo = not OUT.exists() or OUT.stat().st_size == 0
    avisos = []

    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=_CAMPOS)
        if nuevo_archivo:
            w.writeheader()

        for strategy, activo, duracion, direccion in _tuplas_live():
            subtype = f"{activo}#{duracion}"
            clave = f"{strategy}#{subtype}#{direccion}"
            n_shadow, ic_shadow = _shadow_ic(strategy, subtype, direccion)
            filas = _ejecutado_real(strategy, subtype, direccion)
            n_tot = len(filas)
            if n_tot == 0:
                continue
            hit_tot = sum(1 for _, _, ok in filas if ok) / n_tot * 100
            pnls_tot = [p for _, p, _ in filas]
            pnl_tot = sum(pnls_tot) / n_tot
            var_tot = st.variance(pnls_tot) if n_tot > 1 else None

            ult30 = filas[-VENTANA_RECIENTE:]
            n_ult = len(ult30)
            pnls_ult = [p for _, p, _ in ult30]
            hit_ult = sum(1 for _, _, ok in ult30 if ok) / n_ult * 100 if n_ult else None
            pnl_ult = sum(pnls_ult) / n_ult if n_ult else None
            var_ult = st.variance(pnls_ult) if n_ult > 1 else None

            print(f"[vigia_degradacion_live] {clave}: shadow n={n_shadow} ic={ic_shadow:+.3f} | "
                  f"ejecutado n={n_tot} hit={hit_tot:.1f}% pnl/trade={pnl_tot:+.3f} var={var_tot} | "
                  f"ult{n_ult} hit={hit_ult:.1f}% pnl/trade={pnl_ult:+.3f} var={var_ult}" if hit_ult is not None
                  else f"[vigia_degradacion_live] {clave}: sin datos suficientes")

            w.writerow({
                "fecha": fecha, "par": clave, "n_shadow": n_shadow,
                "ic_shadow": round(ic_shadow, 4) if ic_shadow is not None else "",
                "n_ejecutado_total": n_tot, "hit_total_pct": round(hit_tot, 1),
                "pnl_trade_total": round(pnl_tot, 4),
                "var_total": round(var_tot, 4) if var_tot is not None else "",
                "n_ult30": n_ult,
                "hit_ult30_pct": round(hit_ult, 1) if hit_ult is not None else "",
                "pnl_trade_ult30": round(pnl_ult, 4) if pnl_ult is not None else "",
                "var_ult30": round(var_ult, 4) if var_ult is not None else "",
            })

            if n_ult < 10 or pnl_ult is None:
                continue  # ventana reciente demasiado corta para fiarse

            ya_alertado = latch.get(clave, {}).get("negativo", False)
            if pnl_ult < 0 and not ya_alertado:
                avisos.append(
                    f"{clave}: últimos {n_ult} ejecutados hit={hit_ult:.1f}% "
                    f"pnl/trade={pnl_ult:+.3f}€ (shadow de papel: {n_shadow} señales, "
                    f"ic={ic_shadow:+.3f})"
                )
                latch.setdefault(clave, {})["negativo"] = True
            elif pnl_ult > UMBRAL_RECUPERACION and ya_alertado:
                latch.setdefault(clave, {})["negativo"] = False

    # 16-Jul: mismo snapshot diario pero para candidatas (shadow, results.csv,
    # n_shadow>=30) — no toca dinero, solo trackea si la varianza/media shadow
    # de las candidatas se está moviendo antes de que lleguen a tener n real.
    nuevo_cand = not OUT_CAND.exists() or OUT_CAND.stat().st_size == 0
    with open(OUT_CAND, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAND_CAMPOS)
        if nuevo_cand:
            w.writeheader()
        for strategy, activo, duracion, direccion in _tuplas_candidatas():
            subtype = f"{activo}#{duracion}"
            clave = f"{strategy}#{subtype}#{direccion}"
            pnls = _pnls_shadow(strategy, subtype, direccion)
            n_shadow = len(pnls)
            if n_shadow < N_MIN_CANDIDATA:
                continue
            ic_shadow = (sum(1 for p in pnls if p > 0) + 1) / (n_shadow + 2) - 0.5
            var_tot = st.variance(pnls)
            ult30 = pnls[-VENTANA_RECIENTE:]
            n_ult = len(ult30)
            mean_ult = sum(ult30) / n_ult
            var_ult = st.variance(ult30) if n_ult > 1 else None
            w.writerow({
                "fecha": fecha, "par": clave, "n_shadow": n_shadow,
                "ic_shadow": round(ic_shadow, 4), "var_shadow_total": round(var_tot, 4),
                "n_shadow_ult30": n_ult, "mean_shadow_ult30": round(mean_ult, 4),
                "var_shadow_ult30": round(var_ult, 4) if var_ult is not None else "",
            })

    if avisos:
        msg = (
            "⚠️ VIGÍA degradación live: pnl/trade RECIENTE cruzó a negativo\n"
            + "\n".join(f"  {a}" for a in avisos)
            + "\nMismo mecanismo que mató a las 8 candidatas (selección adversa "
              "de contraparte, ver project_status_candidatas_12jul) — puede ser "
              "el inicio de la misma degradación en dinero real. No se ha "
              "tocado nada, solo aviso."
        )
        ok = enviar_telegram(msg)
        print(f"[vigia_degradacion_live] aviso enviado (telegram={ok})")

    LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_degradacion_live] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
