#!/usr/bin/env python3
"""f23: ¿el tamano del fill de W (acciones) lleva informacion? Solo filas de W con rasgos Binance."""
import glob, numpy as np, pandas as pd
from scipy.stats import spearmanr
O = "/root/polymarket-research-datalogs/wallet_pspspsps5/"
parts = []
for f in sorted(glob.glob(O + "feat_2026-*.csv.gz")):
    for x in pd.read_csv(f, usecols=["ts", "p", "acc", "esW", "pmax_prev", "act", "mkt", "cierre", "lado", "T", "d_bps", "mov10", "z"], chunksize=300000, dtype={"mkt": str}):
        x = x[x.esW]
        if len(x): parts.append(x)
W = pd.concat(parts, ignore_index=True)
import sys; sys.path.insert(0, "/root/polymarket-research")
from analisis_maker_cancelacion_binance import desenlaces
des = desenlaces(set(W.mkt)); W["win"] = (W.lado == W.mkt.map(des)).astype(float)
W["dia"] = pd.to_datetime(W.cierre, unit="s").dt.strftime("%Y-%m-%d"); sg = np.where(W.lado == "YES", 1.0, -1.0)
W["zs"] = W.z * sg; W["m10s"] = W.mov10 * sg; W["c"] = W.p * W.acc; W["pnl"] = W.acc * W.win - W.c; W["dip"] = W.pmax_prev.fillna(0) - W.p
W = W[np.isfinite(W.zs)]; Wc = W[W.p < .10]
print("W fills <0.10 con rasgos:", len(Wc))
for v in ("zs", "m10s", "T", "p", "dip"):
    r = spearmanr(Wc[v], Wc.acc); print("  spearman(acc, %s) = %+.3f (p=%.1e)" % (v, r.statistic, r.pvalue))
r = spearmanr(Wc.acc, Wc.win); print("  spearman(acc, win) = %+.3f (p=%.1e)" % (r.statistic, r.pvalue))
Wc = Wc.assign(ab=pd.cut(Wc.acc, [0, 20.01, 200.01, 1e9], labels=["<=20", "20-200", ">200"]), zb=pd.cut(Wc.zs, [-99, -2, -1, 0, 99], labels=["<-2", "-2..-1", "-1..0", ">0"]), pb=pd.cut(Wc.p, [0, .03, .06, .10], right=False, labels=["<.03", ".03-.06", ".06-.10"]))
def row(s): return "n %5d $%7.0f EV %+.3f hit/p %.2f" % (len(s), s.c.sum(), s.pnl.sum() / s.c.sum() if s.c.sum() else np.nan, s.win.mean() / s.p.mean() if len(s) else np.nan)
print("\nEV por tamano x zs (fills <0.10 de W):")
for a, g in Wc.groupby("ab", observed=True):
    for z, h in g.groupby("zb", observed=True): print("  acc %-7s zs %-7s %s" % (a, z, row(h)))
print("\nEV por tamano x precio:")
for a, g in Wc.groupby("ab", observed=True):
    for z, h in g.groupby("pb", observed=True): print("  acc %-7s p %-8s %s" % (a, z, row(h)))
print("\nEV por tamano x tiempo (T<90 / >=90):")
for a, g in Wc.groupby("ab", observed=True):
    for nm, h in (("T<90", g[g["T"] < 90]), ("T>=90", g[g["T"] >= 90])): print("  acc %-7s %-6s %s" % (a, nm, row(h)))
print("\nEV por tamano x moneda:")
for a, g in Wc.groupby("ab", observed=True):
    for z, h in g.groupby("act", observed=True): print("  acc %-7s %-4s %s" % (a, z, row(h)))
print("\nmitades por dias (acc 20-200):", {k: row(g) for k, g in Wc[Wc.ab == "20-200"].assign(per=np.where(Wc.dia <= "2026-10-12", "05-12", "13-24")).groupby("per")})
# probabilidad de que un fill de 20-200 sea parte de una orden mayor (misma tx)
