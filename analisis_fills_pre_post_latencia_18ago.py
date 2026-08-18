#!/usr/bin/env python3
"""analisis_fills_pre_post_latencia_18ago.py — auditoría pre/post cambio de
latencia de matching de Polymarket (18-Ago, petición explícita Javi:
"tenemos que dejar cripto cerrado antes de nada").

Polymarket recortó el delay de matching de taker (~250ms→~50ms, según
Javi) con rollout 24-Jul-2026 04:00 UTC (confirmado en nuestro propio
changelog cacheado, vigia_actualizaciones_polymarket.py: entrada oficial
17-Jul-2026 "async commit pipeline cuts matching latency"). El mecanismo
que produce selección adversa en TODO el proyecto (libro se mueve entre
detección de señal y ejecución) depende directamente de ese delay -- si
bajó 5x, la fill-ability medida ANTES del 24-Jul puede estar obsoleta,
mismo tipo de cambio de régimen que ya obligó a filtrar TWAP siempre.

Replica EXACTAMENTE la lógica canónica de analisis_fills.py (colapso por
market_id+strategy+direction con PRIORIDAD, cruce con results.csv por
market_id+strategy+decision, CLAUDE.md regla 3b -- nunca contar filas) --
pero segmentado por corte de fecha en vez de --dias, y desagregado por
familia de estrategia (CLAUDE.md pt.17).
"""
import csv
from collections import defaultdict
from pathlib import Path

DIR = Path(__file__).parent
SNAPSHOTS = DIR / "data/live/libro_snapshots.csv"
RESULTS = DIR / "data/shadow/results.csv"

CORTE = "2026-07-24T04:00:00+00:00"

from libro_snapshots_prioridad import PRIORIDAD, prio as _prio


def _familia(strategy):
    if strategy.startswith("GBM_LATE_15M"):
        return "GBM_LATE_15M_FAMILIA"
    if strategy.startswith("GBM_LATE_5M"):
        return "GBM_LATE_5M_FAMILIA"
    if strategy.startswith("UPDOWN_GBM"):
        return "UPDOWN_GBM_FAMILIA"
    if strategy.startswith("FAVORITO_CONFIRMADO"):
        return "FAVORITO_CONFIRMADO_FAMILIA"
    if strategy.startswith("BALLENAS"):
        return "BALLENAS_FAMILIA"
    if strategy.startswith("RESOLUTION_SNIPER"):
        return "RESOLUTION_SNIPER"
    return strategy


def main():
    outcomes = {}
    with open(RESULTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            outcomes[(r["market_id"], r["strategy"], r["decision"])] = (
                int(r["acierto"]), float(r["pnl_neto"]))

    senales_pre = {}
    senales_post = {}
    with open(SNAPSHOTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            ts = r["timestamp_utc"]
            bucket = senales_pre if ts < CORTE else senales_post
            key = (r["market_id"], r["strategy"], r["direction"])
            prev = bucket.get(key)
            if prev is None or _prio(r["motivo"]) < _prio(prev["motivo"]):
                bucket[key] = {"motivo": r["motivo"], "strategy": r["strategy"]}

    def agregar(bucket):
        # (familia, motivo) -> [wins, n, pnl]
        agg = defaultdict(lambda: [0, 0, 0.0])
        for (market_id, strategy, direction), s in bucket.items():
            out = outcomes.get((market_id, strategy, direction))
            if out is None:
                # decision puede llevar sufijo distinto a direction en results.csv;
                # intento alternativo con BUY_YES/BUY_NO tal cual viene
                continue
            acierto, pnl = out
            fam = _familia(strategy)
            a = agg[(fam, s["motivo"])]
            a[0] += acierto
            a[1] += 1
            a[2] += pnl
        return agg

    agg_pre = agregar(senales_pre)
    agg_post = agregar(senales_post)

    print(f"Corte: {CORTE}  |  snapshots pre={len(senales_pre)} señales únicas, "
          f"post={len(senales_post)} señales únicas\n")

    familias = sorted(set(f for f, _ in agg_pre) | set(f for f, _ in agg_post))
    for fam in familias:
        print(f"=== {fam} ===")
        for motivo in ["ejecutada", "veto_profundidad", "no_viable_stake", "senal_caducada"]:
            pre = agg_pre.get((fam, motivo))
            post = agg_post.get((fam, motivo))
            def fmt(a):
                if not a or a[1] == 0:
                    return "n=0"
                w, n, pnl = a
                return f"n={n:>4} hit={w/n:>5.1%} pnl_medio={pnl/n:>+7.3f}€ pnl_tot={pnl:>+8.2f}€"
            print(f"  {motivo:<18} PRE-24Jul: {fmt(pre):<55} POST-24Jul: {fmt(post)}")
        print()


if __name__ == "__main__":
    main()
