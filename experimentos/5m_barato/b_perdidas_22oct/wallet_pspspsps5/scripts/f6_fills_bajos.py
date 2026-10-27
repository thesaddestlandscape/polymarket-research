#!/usr/bin/env python3
"""f6: fills <0.10 de pspspsps5: puros vs escalera, hit por conteo, rebate maker estimado, holdout, bootstrap por dia."""
import numpy as np, pandas as pd
O = "/root/polymarket-research-datalogs/wallet_pspspsps5/"
R = pd.read_csv(O + "fills.csv.gz", dtype={"mkt": str}); rng = np.random.default_rng(11)
R["c"] = R.usdc + R.fee
R["reb"] = 0.2 * 0.07 * R.p * (1 - R.p) * R.acc          # rebate maker estimado (20 % de la comision del tomador), NO observado on-chain
g = R.groupby(["mkt", "lado"])
R["pmax_u"] = g.p.transform("max"); R["pmin_u"] = g.p.transform("min"); R["nf_u"] = g.p.transform("size")
R["pu"] = g.usdc.transform("sum") / g.acc.transform("sum")
def bs(df, B=3000):
    d = df.groupby("dia_cierre")[["pnl", "c"]].sum().values; n = len(d)
    r = [d[i, 0].sum() / d[i, 1].sum() for i in (rng.integers(0, n, n) for _ in range(B))]
    return np.round(np.percentile(r, [5, 95]), 3)
def lin(nm, s):
    if not len(s): print(nm, "vacio"); return
    print("%-34s fills %6d unid %5d coste %8.0f pnl %7.0f EV %+.3f IC90dias %s | hit(cuenta) %.2f%% vs p(cuenta) %.2f%% | EV con rebate %+.3f | sin 2 mejores dias PnL %.0f" % (
        nm, len(s), s.groupby(["mkt", "lado"]).ngroups, s.c.sum(), s.pnl.sum(), s.pnl.sum() / s.c.sum(), bs(s), 100 * s.win.mean(), 100 * s.p.mean(), (s.pnl.sum() + s.reb.sum()) / s.c.sum(), s.groupby("dia_cierre").pnl.sum().sort_values().iloc[:-2].sum()))
L = R[R.p < .10]
lin("fills<0.10 TODOS", L)
lin("  pura (unidad entera <0.10)", L[L.pmax_u < .10])
lin("  escalera (unidad con fills>=0.10)", L[L.pmax_u >= .10])
lin("  escalera, 1er fill bajo (nf=1)", L[(L.pmax_u >= .10) & (L.nf_u == 1)])
lin("  escalera nf>=2", L[(L.pmax_u >= .10) & (L.nf_u >= 2)])
for a in ("BTC", "ETH", "SOL"):
    lin("  %s todos" % a, L[L.act == a]); lin("  %s escalera" % a, L[(L.act == a) & (L.pmax_u >= .10)])
for nm, s in (("DESC 05-14", L[L.dia_cierre <= "2026-10-14"]), ("HOLD 15-24", L[L.dia_cierre >= "2026-10-15"])):
    lin("  " + nm + " todos", s); lin("  " + nm + " escalera", s[s.pmax_u >= .10]); lin("  " + nm + " pura", s[s.pmax_u < .10])
print()
for lo, hi in ((0, .02), (.02, .05), (.05, .10)):
    lin("  fills [%.2f,%.2f) escalera" % (lo, hi), L[(L.p >= lo) & (L.p < hi) & (L.pmax_u >= .10)])
    lin("  fills [%.2f,%.2f) pura" % (lo, hi), L[(L.p >= lo) & (L.p < hi) & (L.pmax_u < .10)])
print("\n== escalera: forma tipica (unidades con algun fill<0.10 y fills>=0.10) ==")
U = R.groupby(["mkt", "lado"]).agg(pmin=("p", "min"), pmax=("p", "max"), n=("p", "size"), c=("c", "sum"), pnl=("pnl", "sum"), win=("win", "first"), T1=("T", "max"), Tl=("T", "min")).reset_index()
E_ = U[(U.pmin < .10) & (U.pmax >= .10)]
print("unidades escalera", len(E_), "coste %.0f pnl %.0f EV %+.3f hit %.1f%% ; pmax mediana %.2f ; n fills mediana %d ; T primer fill mediana %.0f s" % (E_.c.sum(), E_.pnl.sum(), E_.pnl.sum() / E_.c.sum(), 100 * E_.win.mean(), E_.pmax.median(), E_.n.median(), E_.T1.median()))
print("EV de ESTAS unidades enteras (todos sus fills)  - incluye fills altos")
# unidades escalera por precio max
for lo, hi in ((.10, .30), (.30, .60), (.60, 1.01)):
    s = E_[(E_.pmax >= lo) & (E_.pmax < hi)]; print("  pmax [%.2f,%.2f): unid %d coste %.0f pnl %.0f EV %+.3f hit %.1f%%" % (lo, hi, len(s), s.c.sum(), s.pnl.sum(), s.pnl.sum() / max(s.c.sum(), 1e-9), 100 * s.win.mean()))
# tamano de fill vs precio
print("\n$ medio por fill: <0.10 %.2f ; 0.10-0.40 %.2f ; 0.40-0.60 %.2f ; >=0.60 %.2f" % tuple(R[(R.p >= lo) & (R.p < hi)].usdc.mean() for lo, hi in ((0, .1), (.1, .4), (.4, .6), (.6, 1.01))))
# rebate total estimado
print("rebate maker estimado total $%.0f sobre coste $%.0f (%.2f%%) ; PnL+rebate %.0f" % (R.reb.sum(), R.c.sum(), 100 * R.reb.sum() / R.c.sum(), R.pnl.sum() + R.reb.sum()))
# >=0.90 fills (carry de casi seguro)
H = R[R.p >= .90]; lin("fills >=0.90", H); lin("fills 0.80-0.90", R[(R.p >= .8) & (R.p < .9)])
# sin escalera total
print("\nPnL por clase de fill: <0.10 puro %.0f ; <0.10 escalera %.0f ; 0.10-0.40 %.0f ; 0.40-0.90 %.0f ; >=0.90 %.0f" % (L[L.pmax_u < .1].pnl.sum(), L[L.pmax_u >= .1].pnl.sum(), R[(R.p >= .1) & (R.p < .4)].pnl.sum(), R[(R.p >= .4) & (R.p < .9)].pnl.sum(), H.pnl.sum()))
