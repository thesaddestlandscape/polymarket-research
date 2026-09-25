#!/usr/bin/env python3
"""vigia_precierre_naive_twap.py -- seguimiento DIARIO del PRECIERRE y del NAIVE en
modo TWAP (24-Sep, petición Javi: "vigila diariamente esto").

Para cada estrategia (RESOLUTION_SNIPER_PRECIERRE, RESOLUTION_SNIPER_NAIVE) y
marco (5min/15min), sobre los trades REALES desde el arranque de su modo TWAP
(data/live/precierre_twap_desde.txt / naive_twap_desde.txt):
  - n cerrados, acierto (esperado ~85 % precierre 5min en su banda con z>=1; 15min con evidencia más
    floja: n=84, +0,32 EUR/EUR, 7/10 días), PnL total y por trade, abiertos.
  - estado del kill-switch (latch).
  - embudo de decisiones de las últimas 24 h (gate_motivo del CSV del ejecutor).
  - alerta si el acierto real cae >10 pp por debajo del esperado con n>=20.
Cuando PolyBolt acumule >=7 días (data/prices/polybolt_*.csv), recuerda la
revalidación del offset (T-30/-45/-60) y de la banda por moneda con el TWAP
OFICIAL (analisis_precierre_twap_ventana_24sep.py).
Telegram SIEMPRE (resumen diario). Salida data/live/vigia_precierre_naive_twap.json.
"""
import csv
import glob
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
LIVE = REPO / "data" / "live"
TRADES = LIVE / "trades.csv"
DECISIONES = REPO / "data" / "shadow" / "resolution_sniper_precierre_executor_v2.csv"
OUT = LIVE / "vigia_precierre_naive_twap.json"
# 25-Sep (Javi "ok"): variantes de z/banda del PRECIERRE medidas HACIA ADELANTE sin arriesgar dinero.
# El barrido de 10 días (15-24 Sep) fue in-sample (z>=1 y banda [0,25-0,65) salieron de esos mismos
# días): 5min z>=1 5,6/día EV +1,02; z>=0,5 9,6/día +0,76; banda a 0,75 8,5/día +0,77; a 0,85
# 16/día +0,46; ancha 42,7/día +0,26. Aquí cada variante se evalúa sobre las decisiones REALES
# del ejecutor (ask y z de ese instante, profundidad >=5x stake) resueltas por gamma-api, desde
# FORWARD_DESDE. Se decide con n>=N_DECISION forward por variante y marco, nunca antes.
FORWARD_DESDE = "2026-09-25T00:00:00"
N_DECISION = 40
FEE = 0.07
MIN_RATIO = 5.0
VARIANTES = [  # (nombre, z_min, ask_lo, ask_hi)
    ("V0_actual z>=1 [0.25,0.65)", 1.0, 0.25, 0.65),
    ("V1 z>=0.5 [0.25,0.65)", 0.5, 0.25, 0.65),
    ("V2 z>=1 [0.25,0.75)", 1.0, 0.25, 0.75),
    ("V3 z>=1 [0.25,0.85)", 1.0, 0.25, 0.85),
    ("V4 z>=0.5 [0.25,0.75)", 0.5, 0.25, 0.75),
    ("V5 z>=1 [0.05,0.95)", 1.0, 0.05, 0.95),
]
OUTCOMES_CACHE = LIVE / "precierre_variantes_outcomes.json"

MODOS = {
    "RESOLUTION_SNIPER_PRECIERRE": (LIVE / "precierre_twap_desde.txt", LIVE / "precierre_twap_kill.json",
                                    # 24-Sep: 0.95 era el acierto GLOBAL a T-45s; en la banda operada
                                    # (ask [0.25,0.65), filtro z>=1) el backtest da z1-1.5 81%, z>=1.5 92-100%
                                    # (n=55, 10 días) -> ~0.85. Con 0.95 alertaría en falso.
                                    {"5min": 0.85, "15min": 0.85}),
    "RESOLUTION_SNIPER_NAIVE": (LIVE / "naive_twap_desde.txt", LIVE / "naive_twap_kill.json",
                                {"5min": 0.85}),
}


def _leer(p: Path, defecto=None):
    try:
        return p.read_text(encoding="utf-8").strip()
    except Exception:
        return defecto


def _resolver_outcomes(mids: list) -> dict:
    """market_id -> nombre del outcome ganador ("Up"/"Down"), solo mercados ya cerrados (gamma-api).
    Cachea solo los resueltos; los pendientes se reintentan al día siguiente. Fail-soft: sin red
    devuelve lo cacheado."""
    import time
    try:
        cache = json.loads(OUTCOMES_CACHE.read_text(encoding="utf-8"))
    except Exception:
        cache = {}
    pend = [m for m in mids if m not in cache]
    try:
        import requests
        for i in range(0, len(pend), 20):
            lote = pend[i:i + 20]
            try:
                r = requests.get("https://gamma-api.polymarket.com/markets",
                                 params=[("id", m) for m in lote] + [("closed", "true")], timeout=20)
                for m in r.json():
                    outs = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
                    pr = [float(x) for x in (json.loads(m["outcomePrices"]) if isinstance(m["outcomePrices"], str)
                                             else m["outcomePrices"])]
                    if max(pr) >= 0.99:
                        cache[str(m["id"])] = outs[pr.index(max(pr))]
            except Exception:
                continue
            time.sleep(0.2)
        OUTCOMES_CACHE.write_text(json.dumps(cache), encoding="utf-8")
    except Exception:
        pass
    return cache


def _variantes_forward() -> tuple[dict, list]:
    """Evalúa VARIANTES sobre las decisiones reales del PRECIERRE desde FORWARD_DESDE. Devuelve
    (json_por_variante, líneas_para_telegram). Una fila por (market_id, activo); ask y z son los del
    instante de decisión; solo cuentan filas con profundidad >= MIN_RATIO x stake."""
    filas = {}
    try:
        for r in csv.DictReader(open(DECISIONES, encoding="utf-8")):
            if (r.get("estrategia") != "RESOLUTION_SNIPER_PRECIERRE" or r.get("dry_run") != "False"
                    or r.get("marco") not in ("5min", "15min")
                    or (r.get("timestamp_utc") or "") < FORWARD_DESDE):
                continue
            try:
                ask, z, ratio = float(r["ask_implicita"]), float(r["z_twap"]), float(r["ratio_vs_stake"])
            except (KeyError, TypeError, ValueError):
                continue   # sin ask / z / profundidad: no ejecutable, no cuenta
            if ratio < MIN_RATIO or r.get("direccion_implicita") not in ("Up", "Down"):
                continue
            filas[(r["market_id"], r["activo"])] = (r["marco"], r["activo"], r["timestamp_utc"][:10],
                                                     r["direccion_implicita"], ask, z, r["market_id"])
    except OSError:
        return {}, ["variantes: sin CSV de decisiones"]
    ganador = _resolver_outcomes(sorted({f[6] for f in filas.values()}))
    out, lineas = {}, []
    dias_fwd = len({f[2] for f in filas.values()}) or 1
    for marco in ("5min", "15min"):
        lineas.append(f"· variantes forward {marco} (desde {FORWARD_DESDE[:10]}, {dias_fwd} día(s) con datos):")
        for nombre, zmin, lo, hi in VARIANTES:
            evs, aciertos, dias, por_act = [], 0, set(), defaultdict(list)
            for m, act, dia, dr, ask, z, mid in filas.values():
                if m != marco or z < zmin or not (lo <= ask < hi) or mid not in ganador:
                    continue
                ac = ganador[mid] == dr
                ev = ((1 - ask) / ask - FEE * (1 - ask)) if ac else -1.0
                evs.append(ev); aciertos += ac; dias.add(dia); por_act[act].append(ev)
            n = len(evs)
            out[f"{marco}|{nombre}"] = {
                "n": n, "dias": len(dias), "acierto": round(aciertos / n, 3) if n else None,
                "ev_por_eur": round(sum(evs) / n, 3) if n else None,
                "por_activo": {a: {"n": len(v), "ev_por_eur": round(sum(v) / len(v), 3)} for a, v in sorted(por_act.items())}}
            marca = f"✅ n>={N_DECISION}: decidir" if n >= N_DECISION else f"acumulando ({n}/{N_DECISION})"
            lineas.append(f"   {nombre}: n={n} acierto={'-' if not n else f'{aciertos/n:.0%}'} "
                          f"EV/€={'-' if not n else f'{sum(evs)/n:+.2f}'} {marca}")
    return out, lineas


MULTIOFFSET = Path("/root/polymarket-research-datalogs/precierre_multioffset_fase0.csv")
MO_DESDE = "2026-09-25T09:00:00"
MO_BANDA = (0.25, 0.85)


def _multioffset_forward() -> tuple[dict, list]:
    """EV al ASK REAL por instante de disparo del precierre (observador precierre_multioffset_fase0,
    25-Sep): mismas decisiones que el ejecutor a cada offset T-120..T-10 s (z verificado idéntico al
    ejecutor a T-45: 18/18 misma dirección, dif. de z 0,0). Solo cuentan lecturas con ask en la banda
    [0,25-0,85), z>=umbral y profundidad >=5x stake. 'Primer disparo' = el offset más temprano que
    cumple por (mercado, moneda): lo que ganaría un ejecutor multi-instante. Backtest previo (in-sample,
    ask <=10 s): 5min primer disparo 339/día EV +0,089 (10/10 días). Decidir con n>=40 y >=3 días."""
    try:
        filas = [r for r in csv.DictReader(open(MULTIOFFSET, encoding="utf-8")) if r["ts_utc"] >= MO_DESDE]
    except OSError:
        return {}, ["multi-offset: sin CSV todavía"]
    datos = []
    for r in filas:
        try:
            ask, z, ratio, off = float(r["ask"]), float(r["z"]), float(r["ratio_vs_stake"]), int(float(r["offset_s"]))
        except (TypeError, ValueError):
            continue
        if r["error"] or ratio < MIN_RATIO or r["direccion"] not in ("Up", "Down") or not (0.05 <= ask < 0.95):
            continue
        datos.append({"m": r["marco"], "act": r["activo"], "mid": r["market_id"], "off": off, "z": z, "ask": ask,
                      "dir": r["direccion"], "dia": r["ts_utc"][:10]})
    if not filas:
        return {}, ["multi-offset: sin filas"]
    t0, t1 = filas[0]["ts_utc"], filas[-1]["ts_utc"]
    dias = max(1.0, (datetime.fromisoformat(t1) - datetime.fromisoformat(t0)).total_seconds() / 86400)
    gan = _resolver_outcomes(sorted({d["mid"] for d in datos}))
    out, lineas = {}, [f"· multi-offset forward ({t0[:16]}→{t1[:16]}, {dias:.1f} días, {len(filas)} lecturas, banda "
                       f"[{MO_BANDA[0]},{MO_BANDA[1]}), profundidad>=5x):"]

    def stats(rows):
        v = [((1 - d["ask"]) / d["ask"] - FEE * (1 - d["ask"])) if gan[d["mid"]] == d["dir"] else -1.0
             for d in rows if d["mid"] in gan]
        return (len(v), round(sum(v) / len(v), 3), round(sum(gan[d["mid"]] == d["dir"] for d in rows if d["mid"] in gan) / len(v), 2)) if v else None

    for marco in ("5m", "15m"):
        for zmin in (1.0, 0.5):
            base = [d for d in datos if d["m"] == marco and d["z"] >= zmin and MO_BANDA[0] <= d["ask"] < MO_BANDA[1]]
            porof = {}
            for off in (-120, -90, -60, -45, -30, -20, -10):
                st = stats([d for d in base if d["off"] == off])
                porof[off] = st
            primero = {}
            for d in sorted(base, key=lambda x: x["off"]):
                primero.setdefault((d["mid"], d["act"]), d)
            sp = stats(list(primero.values()))
            out[f"{marco}|z>={zmin}"] = {"por_offset": {str(o): x for o, x in porof.items()}, "primer_disparo": sp,
                                          "n_lecturas_cumplen": len(base)}
            fila = " ".join(f"T{o}:{x[0]}/{x[1]:+.2f}" for o, x in porof.items() if x)
            lineas.append(f"   {marco} z>={zmin}: [n/EV€ por offset] {fila or '-'}")
            if sp:
                marca = "✅ n>=40" if sp[0] >= 40 and dias >= 3 else "acumulando"
                lineas.append(f"      primer disparo: n={sp[0]} ({sp[0]/dias:.0f}/día) acierto={sp[2]:.0%} EV/€={sp[1]:+.2f} {marca}")
    return out, lineas


def main() -> int:
    ahora = datetime.now(timezone.utc)
    informe, lineas, alertas = {}, [], []
    filas = list(csv.DictReader(open(TRADES, encoding="utf-8")))
    for est, (p_desde, p_kill, esperado) in MODOS.items():
        desde = _leer(p_desde)
        kill = _leer(p_kill)
        info = {"desde": desde, "kill": json.loads(kill) if kill else {"matado": False}, "marcos": {}}
        for marco in ("5min", "15min"):
            ts = [r for r in filas if r.get("strategy") == est and desde and (r.get("timestamp_utc") or "") >= desde
                  and (r.get("subtype") or "").endswith(marco)]
            cerr = [r for r in ts if r.get("status") == "CLOSED"]
            pnls = []
            for r in cerr:
                try:
                    pnls.append(float(r["pnl_neto_eur"]))
                except (KeyError, ValueError):
                    pass
            n = len(pnls)
            hit = sum(p > 0 for p in pnls) / n if n else None
            d = {"n_cerrados": n, "acierto": round(hit, 3) if hit is not None else None,
                 "pnl_total": round(sum(pnls), 2), "pnl_trade": round(sum(pnls) / n, 3) if n else None,
                 "abiertos": sum(1 for r in ts if r.get("status") in ("OPEN", "ERROR")),
                 "esperado": esperado.get(marco)}
            info["marcos"][marco] = d
            if esperado.get(marco) and n >= 20 and hit is not None and hit < esperado[marco] - 0.10:
                alertas.append(f"⚠️ {est} {marco}: acierto real {hit:.0%} (n={n}) vs esperado {esperado[marco]:.0%}")
            if n or d["abiertos"]:
                lineas.append(f"{est.replace('RESOLUTION_SNIPER_', '')} {marco}: n={n} acierto="
                              f"{'-' if hit is None else f'{hit:.0%}'} pnl={sum(pnls):+.2f}€ "
                              f"({'-' if not n else f'{sum(pnls)/n:+.3f}'}/tr) abiertos={d['abiertos']}")
            # 24-Sep (sustituye a vigia_resolution_sniper_naive_degradacion.py, que medía el
            # naive VIEJO post-cierre): desglose por moneda (CLAUDE.md pt.17), misma alerta.
            por_activo = defaultdict(list)
            for r in cerr:
                try:
                    por_activo[(r.get("subtype") or "?").split("#")[0]].append(float(r["pnl_neto_eur"]))
                except (KeyError, ValueError):
                    pass
            d["por_activo"] = {}
            for act, ps in sorted(por_activo.items()):
                h = sum(p > 0 for p in ps) / len(ps)
                d["por_activo"][act] = {"n": len(ps), "acierto": round(h, 3), "pnl_total": round(sum(ps), 2)}
                if esperado.get(marco) and len(ps) >= 20 and h < esperado[marco] - 0.10:
                    alertas.append(f"⚠️ {est} {act}#{marco}: acierto real {h:.0%} (n={len(ps)}) "
                                   f"vs esperado {esperado[marco]:.0%}")
            if por_activo:
                lineas.append("   " + " | ".join(f"{a} n={v['n']} {v['acierto']:.0%} {v['pnl_total']:+.2f}€"
                                              for a, v in d["por_activo"].items()))
        if info["kill"].get("matado"):
            alertas.append(f"🛑 {est} kill-switch ACTIVO: {info['kill'].get('motivo')}")
        informe[est] = info
    # embudo de decisiones 24 h
    lim = (ahora - timedelta(hours=24)).isoformat()
    embudo = defaultdict(Counter)
    try:
        for r in csv.DictReader(open(DECISIONES, encoding="utf-8")):
            if (r.get("timestamp_utc") or "") >= lim:
                mot = (r.get("gate_motivo") or "").split("=")[0].split(":")[0]
                embudo[f"{r.get('estrategia')}|{r.get('marco')}"][mot] += 1
    except OSError:
        pass
    informe["embudo_24h"] = {k: dict(v.most_common(8)) for k, v in embudo.items()}
    dias_pb = len(glob.glob(str(REPO / "data/prices/polybolt_*.csv*")))
    informe["dias_polybolt"] = dias_pb
    if dias_pb >= 7:
        alertas.append(f"📅 PolyBolt ya tiene {dias_pb} días: toca revalidar offset (T-30/-45/-60) y banda por moneda "
                       f"con el TWAP oficial (analisis_precierre_twap_ventana_24sep.py)")
    try:
        informe["variantes_forward"], lineas_var = _variantes_forward()
    except Exception as e:   # el resumen diario nunca debe caerse por esta sección
        informe["variantes_forward"], lineas_var = {}, [f"variantes forward: error {type(e).__name__}: {e}"]
    try:
        informe["multioffset_forward"], lineas_mo = _multioffset_forward()
    except Exception as e:
        informe["multioffset_forward"], lineas_mo = {}, [f"multi-offset: error {type(e).__name__}: {e}"]
    informe["actualizado_utc"] = ahora.isoformat(timespec="seconds")
    OUT.write_text(json.dumps(informe, indent=1, ensure_ascii=False), encoding="utf-8")
    msg = ["📊 PRECIERRE/NAIVE modo TWAP -- resumen diario"] + (lineas or ["sin trades reales todavía"])
    for k, v in informe["embudo_24h"].items():
        msg.append(f"· 24h {k}: " + ", ".join(f"{m}={c}" for m, c in list(v.items())[:5]))
    msg += lineas_var
    msg += lineas_mo
    msg += alertas
    print("\n".join(msg))
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram("\n".join(msg))
    except Exception as e:
        print(f"(Telegram falló: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
