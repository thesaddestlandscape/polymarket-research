#!/usr/bin/env python3
"""f12: fills pasivos de compra p<0.10 (5m, todas las monedas) poblacion sin W vs W, por precio x T x moneda; periodo DESC<=14 / HOLD>=15. EV makers sin fee ni rebate, ponderado por $; IC90 por dias."""
import sys, glob
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from pathlib import Path
from analisis_maker_cancelacion_binance import desenlaces
O = Path("/root/polymarket-research-datalogs/wallet_pspspsps5")
P = pd.concat([pd.read_csv(f, dtype={"mkt": str}) for f in sorted(glob.glob(str(O / "poblacion_2026-*.csv.gz")))], ignore_index=True)
P["dia"] = pd.to_datetime(P.cierre, unit="s").dt.strftime("%Y-%m-%d")
des = desenlaces(set(P.mkt)); P["des"] = P.mkt.map(des).fillna(""); P = P[P.des != ""]
P["win"] = (P.lado == P.des).astype(float); P["c"] = P.p * P.acc; P["pnl"] = P.acc * P.win - P.c
print("dias", sorted(P.dia.unique()), "fills", len(P), "W", int(P.esW.sum()))
rng = np.random.default_rng(3)
def bs(df, B=1500):
    g = df.groupby("dia")[["pnl", "c"]].sum().values; n = len(g)
    if n < 2: return "n/a"
    r = [g[i, 0].sum() / g[i, 1].sum() for i in (rng.integers(0, n, n) for _ in range(B))]
    return tuple(np.round(np.percentile(r, [5, 95]), 2))
def lin(nm, s):
    if len(s) < 30: print("  %-34s n=%d" % (nm, len(s))); return
    print("  %-34s fills %7d $%9.0f EV %+.3f %s hit(cuenta) %.2f%% p %.2f%% dias %d" % (nm, len(s), s.c.sum(), s.pnl.sum() / s.c.sum(), bs(s), 100 * s.win.mean(), 100 * s.p.mean(), s.dia.nunique()))
P["pb"] = pd.cut(P.p, [0, .03, .06, .10], right=False, labels=["<.03", ".03-.06", ".06-.10"]); P["tb"] = pd.cut(P["T"], [-99, 90, 180, 400], labels=["T<90", "T90-180", "T>=180"])
for per, f in (("DESC<=14", P.dia <= "2026-10-14"), ("HOLD>=15", P.dia >= "2026-10-15"), ("TODO", P.dia > "")):
    S = P[f]; print("\n##", per, "dias", S.dia.nunique())
    for nm, X in (("POBLACION sin W", S[~S.esW]), ("W", S[S.esW])):
        print(" ", nm); lin("todas <0.10", X)
        for b in X.pb.cat.categories: lin("precio " + b, X[X.pb == b])
        for b in X.tb.cat.categories: lin("tiempo " + b, X[X.tb == b])
        for a in ("BTC", "ETH", "SOL"): lin("moneda " + a, X[X.act == a])
# tamano: W compra mucho mas pequenio? y cuota de W en el $ pasivo <0.10
print("\nW cuota $ pasivo<0.10 (BTC/ETH/SOL): %.2f%%" % (100 * P[P.esW].c.sum() / P[P.act.isin(["BTC", "ETH", "SOL"])].c.sum()))
