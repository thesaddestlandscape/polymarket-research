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
OUT = REPO / "data/shadow/degradacion_live.csv"
LATCH = REPO / "data/live/vigia_degradacion_live_latch.json"

PARES = ["SOL", "ETH"]
ESTRATEGIA = "GBM_LATE_15M"
DIRECCION = "BUY_YES"
VENTANA_RECIENTE = 30
UMBRAL_RECUPERACION = 0.05  # €/trade — por encima de esto se resetea el latch

_CAMPOS = ["fecha", "par", "n_shadow", "ic_shadow", "n_ejecutado_total",
           "hit_total_pct", "pnl_trade_total", "n_ult30", "hit_ult30_pct",
           "pnl_trade_ult30"]


def _shadow_ic(par: str):
    n, hits = 0, 0
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy") == ESTRATEGIA and r.get("subtype") == f"{par}#15min"
                    and r.get("decision") == DIRECCION):
                n += 1
                hits += int(r.get("acierto") or 0)
    if n == 0:
        return 0, None
    ic = (hits + 1) / (n + 2) - 0.5
    return n, ic


def _ejecutado_real(par: str):
    filas = []
    with open(TRADES, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy") == ESTRATEGIA and r.get("subtype") == f"{par}#15min"
                    and r.get("direction") == DIRECCION and r.get("status") == "CLOSED"
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

        for par in PARES:
            n_shadow, ic_shadow = _shadow_ic(par)
            filas = _ejecutado_real(par)
            n_tot = len(filas)
            if n_tot == 0:
                continue
            hit_tot = sum(1 for _, _, ok in filas if ok) / n_tot * 100
            pnl_tot = sum(p for _, p, _ in filas) / n_tot

            ult30 = filas[-VENTANA_RECIENTE:]
            n_ult = len(ult30)
            hit_ult = sum(1 for _, _, ok in ult30 if ok) / n_ult * 100 if n_ult else None
            pnl_ult = sum(p for _, p, _ in ult30) / n_ult if n_ult else None

            print(f"[vigia_degradacion_live] {par}: shadow n={n_shadow} ic={ic_shadow:+.3f} | "
                  f"ejecutado n={n_tot} hit={hit_tot:.1f}% pnl/trade={pnl_tot:+.3f} | "
                  f"ult{n_ult} hit={hit_ult:.1f}% pnl/trade={pnl_ult:+.3f}" if hit_ult is not None
                  else f"[vigia_degradacion_live] {par}: sin datos suficientes")

            w.writerow({
                "fecha": fecha, "par": par, "n_shadow": n_shadow,
                "ic_shadow": round(ic_shadow, 4) if ic_shadow is not None else "",
                "n_ejecutado_total": n_tot, "hit_total_pct": round(hit_tot, 1),
                "pnl_trade_total": round(pnl_tot, 4),
                "n_ult30": n_ult,
                "hit_ult30_pct": round(hit_ult, 1) if hit_ult is not None else "",
                "pnl_trade_ult30": round(pnl_ult, 4) if pnl_ult is not None else "",
            })

            if n_ult < 10 or pnl_ult is None:
                continue  # ventana reciente demasiado corta para fiarse

            ya_alertado = latch.get(par, {}).get("negativo", False)
            if pnl_ult < 0 and not ya_alertado:
                avisos.append(
                    f"{par}: últimos {n_ult} ejecutados hit={hit_ult:.1f}% "
                    f"pnl/trade={pnl_ult:+.3f}€ (shadow de papel: {n_shadow} señales, "
                    f"ic={ic_shadow:+.3f})"
                )
                latch.setdefault(par, {})["negativo"] = True
            elif pnl_ult > UMBRAL_RECUPERACION and ya_alertado:
                latch.setdefault(par, {})["negativo"] = False

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
