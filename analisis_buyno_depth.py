#!/usr/bin/env python3
"""#2 buyno_depthfilter_sim — ¿existe un umbral de PROFUNDIDAD de libro donde
BUY_NO sea a la vez FILLABLE y RENTABLE?

Motivación: `veto_profundidad` en analisis_fills está congelado en 24/30 porque,
retirados los BUY_NO del live, no se generan muestras nuevas. Pero libro_snapshots
registra la profundidad (ratio_vs_stake) de CADA señal BUY_NO 24/7 (n=461) y
results.csv tiene el outcome shadow a precio de plan. Uniendo por market_id
medimos hit/PnL de BUY_NO en función de la profundidad — decisión con n>>30 HOY,
sin esperar a que el contador congelado crezca.

Read-only: no escribe en data/. Estimando = outcome a plan (lo que la señal
habría cobrado si se ejecutara a su precio de plan), que es exactamente la
pregunta fill-ability: entre los BUY_NO que PASAN un gate de profundidad, ¿cuánto
aciertan de verdad?
"""
import csv
import statistics
from collections import defaultdict
from pathlib import Path

DIR = Path(__file__).resolve().parent
SNAPS = DIR / "data/live/libro_snapshots.csv"
RESULTS = DIR / "data/shadow/results.csv"


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main() -> int:
    # 1) profundidad por market_id de las señales BUY_NO (mediana si hay reintentos)
    depth_por_mkt = defaultdict(list)
    for r in csv.DictReader(open(SNAPS, encoding="utf-8")):
        if r["direction"] != "BUY_NO":
            continue
        ratio = _f(r["ratio_vs_stake"])
        if ratio is not None:
            depth_por_mkt[r["market_id"]].append(ratio)
    depth = {m: statistics.median(v) for m, v in depth_por_mkt.items() if v}

    # 2) outcome shadow a plan por market_id (BUY_NO)
    outcome = {}
    for r in csv.DictReader(open(RESULTS, encoding="utf-8")):
        if r.get("decision") != "BUY_NO":
            continue
        pnl = _f(r.get("pnl_neto"))
        if pnl is None:
            continue
        hit = 1 if str(r.get("acierto")) in ("1", "True", "true") else 0
        outcome[r["market_id"]] = (hit, pnl)  # último gana si duplicado

    # 3) join
    joined = [(depth[m], *outcome[m]) for m in depth if m in outcome]
    print(f"BUY_NO con profundidad Y outcome: n={len(joined)} "
          f"(snapshots={len(depth)}, resueltos_BUY_NO={len(outcome)})\n")
    if len(joined) < 30:
        print("⚠️ join insuficiente — revisar clave market_id entre ficheros")
        return 1

    def stats(rs):
        if not rs:
            return "n=0"
        n = len(rs)
        hit = sum(h for _, h, _ in rs) / n
        pnl = sum(p for _, _, p in rs)
        return f"n={n:4d}  hit={hit*100:4.1f}%  pnl_tot={pnl:+8.2f}€  pnl_medio={pnl/n:+.3f}€"

    # 4) por bucket de profundidad (ratio libro / stake)
    print("Hit/PnL por PROFUNDIDAD de libro (ratio_vs_stake) — el eje fill-ability:")
    edges = [(0, 1), (1, 3), (3, 5), (5, 10), (10, 30), (30, 1e9)]
    for lo, hi in edges:
        b = [x for x in joined if lo <= x[0] < hi]
        etq = f"[{lo},{hi})" if hi < 1e9 else f"[{lo},inf)"
        print(f"  ratio {etq:12s} {stats(b)}")

    # 5) escenario gate: si SOLO tomamos BUY_NO con ratio>=X (los fillables)
    print("\nGate 'solo BUY_NO con ratio>=X' (lo que SÍ podrías ejecutar):")
    for x in [1, 3, 5, 10, 20]:
        keep = [t for t in joined if t[0] >= x]
        print(f"  ratio>={x:2d}: {stats(keep)}")

    # 6) veredicto direccional
    print("\nLectura: si el hit NO sube (o baja) con la profundidad, el edge de "
          "BUY_NO vive donde no puedes ejecutar (selección adversa estructural) "
          "-> archivar. Si sube monótono, hay umbral de reapertura gateado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
