"""CONTRAPUNTO s4 (post-hoc, descriptivo): donde (T, banda, tamano del barrido del tomador) llegan los NUEVO/DES vs donde rellena B. ETH/SOL/XRP 20-23 Oct."""
import numpy as np, pandas as pd
U = pd.read_pickle("/mnt/HC_Volume_106538179/agentes_datos/contrapunto_informado/U.pkl")
U = U[U.cob & U.act.astype(str).isin(["ETH", "SOL", "XRP"]) & U.dia.astype(str).isin(["2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23"])].copy()
U["cl"] = U.cl.astype(str); U["Tb"] = pd.cut(U["T"], [-1e9, 60, 120, 180, 240, 1e9], labels=["<60", "60-120", "120-180", "180-240", ">240"])
U["bd"] = pd.cut(U.p, [0, .10, .15, .20, .25, .30]); U["nyb"] = U.cl.isin(["NUEVO", "DES"])
P = U[~U.isB]; B = U[U.isB]
for k in ("Tb", "bd"):
    t = P.groupby(k, observed=True).apply(lambda x: pd.Series({"cuotaNYD_pob": x.c[x.nyb].sum() / x.c.sum(), "EV_pob": x.pnl.sum() / x.c.sum(), "EV_NYD": x.pnl[x.nyb].sum() / max(x.c[x.nyb].sum(), 1e-9), "€pob": x.c.sum()}))
    t["cuota€B"] = B.groupby(k, observed=True).c.sum() / B.c.sum(); t["cuotaNYD_B"] = B.groupby(k, observed=True).apply(lambda x: x.c[x.nyb].sum() / x.c.sum())
    print(t.round(3).to_string(), "\n")
