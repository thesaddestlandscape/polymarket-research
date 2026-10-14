#!/usr/bin/env python3
"""diag_v6_visible_anticipada.py -- DIAGNÓSTICO de V6_FOK_VUELO_BTC (Javi 14-Oct), FUERA del fichero congelado (el vigía V6
hashea su código): separa las ejecuciones "visibles" (en la decisión el ask del 5m ya estaba <= p*) de las "anticipadas"
(el ask bajó durante el vuelo), con las mismas cachés fok_vuelo_D_p250.csv.gz. No cambia la regla ni sus gates.
Uso: python3 diag_v6_visible_anticipada.py [--desde 2026-10-14] [--L 355]
"""
import argparse
import csv
import gzip
from collections import defaultdict
from pathlib import Path

D = Path("/root/polymarket-research-datalogs/m5barato_mision")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-14")
    ap.add_argument("--hasta", default="2099-12-31")
    ap.add_argument("--L", type=int, default=355)
    a = ap.parse_args()
    g = defaultdict(lambda: [0, 0.0, 0.0, 0])
    for f in sorted(D.glob("fok_vuelo_2026-*_p250.csv.gz")):
        dia = f.name[10:20]
        if not (a.desde <= dia <= a.hasta):
            continue
        with gzip.open(f, "rt") as fh:
            for r in csv.DictReader(fh):
                if r["moneda"] != "BTC" or int(r["L"]) != a.L or not r.get("pnl"):
                    continue
                k = "visible" if r["visible"] == "True" else "anticipada"
                x = g[k]
                x[0] += 1
                x[1] += float(r["pnl"])
                x[2] += float(r["coste"])
                x[3] += r["gana"] == "True"
    print(f"V6 BTC L{a.L} {a.desde}..: " + " | ".join(
        f"{k}: n {v[0]} PnL {v[1]:+.2f} € EV/€ {v[1] / v[2] if v[2] else float('nan'):+.3f} acierto {v[3] / v[0]:.0%}"
        for k, v in sorted(g.items())) if g else f"V6 BTC L{a.L} {a.desde}..: sin ejecuciones")


if __name__ == "__main__":
    main()
