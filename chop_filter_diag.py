#!/usr/bin/env python3
"""chop_filter_diag.py — ¿un filtro de "chop" (sin tendencia) plancha la varianza
de GBM_LATE_15M BUY_YES sin comerse el edge? (07-Jul, read-only, datos producción)

Hipótesis: en ventanas SIN conviction direccional (|drift_ventana_pct| bajo) el
resultado es ~coinflip → poco EV y mucha varianza. Skipearlas debería SUBIR el
pnl/trade Y BAJAR su desviación (free lunch), no solo reducir riesgo.

Mide, particionando GBM_LATE_15M BUY_YES por |drift_ventana_pct| (y por d_gbm,
sigma_h como control): n, hit, pnl medio, DESVIACIÓN del pnl (varianza) y ratio
media/desv (retorno ajustado a riesgo). Luego simula "skip si |drift|<X".

Nota: shadow (results.csv), no fill-ability. Es para decidir si vale prototipar
el filtro, no para cablearlo. n=882 resueltas.
"""
import csv
import json
import statistics

RESULTS = "/root/polymarket-research/data/shadow/results.csv"


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def load():
    out = []
    for r in csv.DictReader(open(RESULTS)):
        if r["strategy"] != "GBM_LATE_15M" or r["decision"] != "BUY_YES":
            continue
        if r["acierto"] not in ("1", "0"):
            continue
        try:
            fe = json.loads(r.get("features", "{}") or "{}")
        except (ValueError, TypeError):
            continue
        pnl = f(r["pnl_neto"])
        if pnl is None:
            continue
        out.append({
            "win": r["acierto"] == "1",
            "pnl": pnl,
            "drift": f(fe.get("drift_ventana_pct")),
            "d_gbm": f(fe.get("d_gbm")),
            "sigma": f(fe.get("sigma_h")),
            "py": f(fe.get("py_entrada")),
        })
    return out


def stats(g):
    n = len(g)
    if n == 0:
        return None
    pnls = [x["pnl"] for x in g]
    hit = sum(1 for x in g if x["win"]) / n
    media = statistics.mean(pnls)
    desv = statistics.pstdev(pnls) if n > 1 else 0.0
    sharpe = media / desv if desv else 0.0
    return {"n": n, "hit": hit, "media": media, "desv": desv, "sharpe": sharpe, "total": sum(pnls)}


def linea(lab, s):
    if not s:
        print(f"  {lab:<26} n=0")
        return
    print(f"  {lab:<26} n={s['n']:<4} hit={s['hit']:.0%} pnl/op={s['media']:+.3f} "
          f"desv={s['desv']:.2f} media/desv={s['sharpe']:+.3f} total={s['total']:+.1f}€")


def por_feature(data, key, cortes, unidad=""):
    print(f"\n== por |{key}|  (abs) ==")
    vals = [abs(x[key]) for x in data if x[key] is not None]
    if not vals:
        print("  (sin datos)")
        return
    lo, hi = cortes
    grupos = [
        (f"chop  |{key}|<{lo}", lambda v: v < lo),
        (f"medio {lo}-{hi}", lambda v: lo <= v < hi),
        (f"trend |{key}|>={hi}", lambda v: v >= hi),
    ]
    for lab, cond in grupos:
        g = [x for x in data if x[key] is not None and cond(abs(x[key]))]
        linea(lab, stats(g))


def main():
    data = load()
    print(f"GBM_LATE_15M BUY_YES resueltas: {len(data)}\n")
    print("== BASELINE (todo) ==")
    linea("todo", stats(data))

    # conviction direccional = |drift_ventana_pct|
    por_feature(data, "drift", (0.05, 0.15))
    por_feature(data, "d_gbm", (0.05, 0.15))
    por_feature(data, "sigma", (0.015, 0.030))

    # SIMULACIÓN del filtro: skip si |drift| < umbral → ¿sube pnl/op y baja desv?
    print("\n== SIMULACIÓN filtro 'skip si |drift_ventana_pct| < umbral' ==")
    base = stats(data)
    for u in (0.03, 0.05, 0.08, 0.12):
        keep = [x for x in data if x["drift"] is not None and abs(x["drift"]) >= u]
        s = stats(keep)
        if s:
            d_media = s["media"] - base["media"]
            d_desv = s["desv"] - base["desv"]
            print(f"  umbral {u}: quedan {s['n']}/{base['n']} "
                  f"({s['n']/base['n']:.0%}) | pnl/op {s['media']:+.3f} ({d_media:+.3f}) | "
                  f"desv {s['desv']:.2f} ({d_desv:+.2f}) | total {s['total']:+.1f}€")
    print("\n  → free lunch si al subir el umbral: pnl/op SUBE y desv BAJA a la vez.")
    print("  → si pnl/op baja al filtrar, el 'chop' también tenía edge (no filtrar; cf. anticoinflip).")


if __name__ == "__main__":
    main()
