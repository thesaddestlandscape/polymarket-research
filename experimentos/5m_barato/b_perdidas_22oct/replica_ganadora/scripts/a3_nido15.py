#!/usr/bin/env python3
"""a3 (H4 NIDO-15m): en 5m BTC que son último tramo de un 15m (cierre % 900 == 0), lado implicado s por TWAP60 oficial
(polybolt canal twap60 source=chainlink; ref15=twap(C-900), ref5=twap(C-300); ref15>ref5 => s=YES/Up; |gap|>=1 bp).
Cuota de $ de W en s vs población y EV población s vs no-s, DESC/OOS. Rellenos maker de compra p<0,40 (a1_*)."""
import sys, glob, csv
import numpy as np, pandas as pd
exec(open(__file__.replace("a3_nido15.py", "a2_ev.py")).read().split("print(f\"cobertura")[0])   # carga X y ev()
tw = {}
for d in sorted(set(pd.to_datetime(X.cierre - 900, unit="s").dt.strftime("%Y-%m-%d")) | set(X.dia)):
    try:
        for r in csv.DictReader(open(f"/root/polymarket-research/data/prices/polybolt_{d}.csv")):
            if r["asset"] == "BTC" and r["canal"] == "twap60" and r["source"] == "chainlink":
                tw[int(r["event_ts_ms"]) // 1000] = float(r["value"])
    except FileNotFoundError:
        print("falta polybolt", d)
L = X[X.cierre % 900 == 0].copy()
r15 = L.cierre.map(lambda c: tw.get(int(c) - 900)); r5 = L.cierre.map(lambda c: tw.get(int(c) - 300))
L["gap"] = (r15 - r5) / r5 * 1e4
print(f"últimos tramos: filas {len(L)}, con refs {L.gap.notna().mean():.3f}")
L = L[L.gap.abs() >= 1]
L["s"] = np.where(L.gap > 0, "YES", "NO"); L["ens"] = (L.lado == L.s)
for b in ["t<0.10", "b0.10-0.40"]:
    for per in ["DESC", "OOS"]:
        S = L[(L.b == b) & (L.per == per)]
        for w in (1, 0):
            g = S[S.esW == w]
            if not len(g): continue
            print(f"{b} {per} {'W' if w else 'P'} cuota$ en s={g.usd[g.ens].sum()/g.usd.sum():.2f} | s: {ev(g[g.ens])} | no-s: {ev(g[~g.ens])}")
