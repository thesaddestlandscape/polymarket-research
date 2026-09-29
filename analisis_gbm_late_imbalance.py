#!/usr/bin/env python3
"""analisis_gbm_late_imbalance.py -- lectura de gbm_late_imbalance_fase0.csv
(ronda2 #9, 29-Sep). EV al ask REAL (hold-to-resolution, fee 7 %) por tercil
de imbalance del libro del token comprado, desagregado por moneda x marco
(CLAUDE.md pt.17), primer disparo fillable (ratio>=5x) por (mercado,
estrategia). IC90 bootstrap por DIAS. Solo lectura.

Uso: python3 analisis_gbm_late_imbalance.py [--min-n 40]
Decidir con n>=40 por celda y >=10 dias; por debajo es exploratorio.
"""
import argparse
import csv
import random
import statistics as st
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
IN = REPO / "data" / "shadow" / "gbm_late_imbalance_fase0.csv"
RESULTS = REPO / "data" / "shadow" / "results.csv"
FEE = 0.07


def outcomes(market_ids):
    csv.field_size_limit(10 ** 9)
    out = {}
    with open(RESULTS, encoding="utf-8") as f:
        rd = csv.reader(f)
        h = next(rd)
        im, io = h.index("market_id"), h.index("outcome_real")
        for row in rd:
            if len(row) > io and row[im] in market_ids and row[io] in ("YES", "NO"):
                out[row[im]] = row[io]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-n", type=int, default=40)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(IN, encoding="utf-8")))
    rows.sort(key=lambda x: x["ts_deteccion_utc"])
    out = outcomes({x["market_id"] for x in rows})
    U = {}
    for x in rows:
        if x["market_id"] not in out or x["mejor_ask"] == "" or x["imbalance_top5"] in ("", "None"):
            continue
        if float(x["ratio_vs_stake"] or 0) < 5:
            continue
        p = float(x["mejor_ask"])
        if not 0.10 <= p <= 0.90:
            continue
        U.setdefault((x["market_id"], x["strategy"]), x)
    U = list(U.values())
    print(f"filas={len(rows)} con resultado y fillable={len(U)}")

    def win(x):
        return (x["decision"] == "BUY_YES") == (out[x["market_id"]] == "YES")

    def pnl(x):
        p = float(x["mejor_ask"])
        return ((1 - p) / p if win(x) else -1) - FEE * (1 - p)

    def ic(s):
        d = defaultdict(list)
        for x in s:
            d[x["ts_deteccion_utc"][:10]].append(pnl(x))
        g = list(d.values())
        random.seed(1)
        b = sorted(st.mean([v for k in random.choices(g, k=len(g)) for v in k]) for _ in range(2000))
        return b[100], b[1900], len(g)

    def rep(n, s):
        if len(s) < 15:
            print(f"{n:48s} n={len(s)} (<15)")
            return
        lo, hi, nd = ic(s)
        tag = "" if len(s) >= a.min_n and nd >= 10 else " [exploratorio]"
        print(f"{n:48s} n={len(s):4d} hit={sum(win(x) for x in s)/len(s):.3f} "
              f"ask={st.mean(float(x['mejor_ask']) for x in s):.3f} EV/EUR={st.mean(map(pnl, s)):+.3f} "
              f"IC90d[{lo:+.3f},{hi:+.3f}] dias={nd}{tag}")

    rep("TODAS", U)
    celdas = defaultdict(list)
    for x in U:
        celdas[(x["activo"], x["marco"])].append(x)
    for f in ("imbalance_top5", "imbalance_top10"):
        v = sorted(float(x[f]) for x in U if x[f] not in ("", "None"))
        if len(v) < 45:
            continue
        q = [v[len(v) // 3], v[2 * len(v) // 3]]
        print(f"-- {f} cortes globales {[round(z, 3) for z in q]}")
        for n, lo, hi in (("bajo", -9, q[0]), ("medio", q[0], q[1]), ("alto", q[1], 9)):
            rep(f"  {f} {n}", [x for x in U if lo <= float(x[f]) < hi])
            for k, s in sorted(celdas.items()):
                sub = [x for x in s if lo <= float(x[f]) < hi]
                if len(sub) >= 15:
                    rep(f"    {k[0]}#{k[1]} {f} {n}", sub)


if __name__ == "__main__":
    main()
