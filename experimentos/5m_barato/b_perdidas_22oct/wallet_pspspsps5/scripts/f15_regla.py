#!/usr/bin/env python3
"""f15: busca la regla ex ante que separa los rellenos pasivos <0.10 de W de la poblacion. Rasgos con Binance (recepcion). Solo lectura.
Descubrimiento = dias <=12-Oct ; holdout = dias >=17-Oct (cierre). Unidad primaria = fill ponderado por $ (como W) y 1er fill por (mercado,lado)."""
import sys, glob, itertools
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from pathlib import Path
from analisis_maker_cancelacion_binance import desenlaces
O = Path("/root/polymarket-research-datalogs/wallet_pspspsps5")
_dt = {"mkt": "category", "act": "category", "lado": "category", "p": "float32", "acc": "float32", "pmax_prev": "float32", "d_bps": "float32", "mov10": "float32", "mov30": "float32", "z": "float32", "T": "float32"}
P = pd.concat([pd.read_csv(f, dtype=_dt, usecols=["ts", "p", "acc", "esW", "pmax_prev", "act", "mkt", "cierre", "lado", "T", "d_bps", "mov10", "mov30", "z"]) for f in sorted(glob.glob(str(O / "feat_2026-*.csv.gz")))], ignore_index=True)
P["mkt"] = P.mkt.astype(str).astype("category")
P["dia"] = pd.to_datetime(P.cierre, unit="s").dt.strftime("%Y-%m-%d")
des = desenlaces(set(P.mkt.astype(str))); P["des"] = P.mkt.astype(str).map(des).fillna(""); P = P[P.des != ""].copy()
P["win"] = (P.lado.astype(str) == P.des).astype("float32"); P["c"] = P.p * P.acc; P["pnl"] = P.acc * P.win - P.c; P = P.drop(columns=["des"])
sg = np.where(P.lado.astype(str) == "YES", 1.0, -1.0).astype("float32")
P["zs"] = P.z * sg; P["ds"] = P.d_bps * sg; P["m10s"] = P.mov10 * sg; P["m30s"] = P.mov30 * sg
P["dip"] = P.pmax_prev.fillna(0) - P.p
gs = P.groupby(["mkt", "lado", "ts"], observed=True); P["sw_n"] = gs.p.transform("nunique"); P["sw_acc"] = gs.acc.transform("sum")
P["swb"] = pd.cut(P.sw_n, [0, 1, 3, 7, 999], labels=["1", "2-3", "4-7", "8+"])
P = P[np.isfinite(P.zs) & np.isfinite(P.m10s)]
P["pb"] = pd.cut(P.p, [0, .03, .06, .10], right=False, labels=["a", "b", "c"]); P["tb"] = pd.cut(P["T"], [-99, 90, 180, 400], labels=["t1", "t2", "t3"])
P["per"] = np.where(P.dia <= "2026-10-12", "DESC", np.where(P.dia >= "2026-10-17", "HOLD", "x"))
rng = np.random.default_rng(9)
def bs(df, B=1500):
    g = df.groupby("dia")[["pnl", "c"]].sum().values; n = len(g)
    if n < 2: return (np.nan, np.nan)
    r = [g[i, 0].sum() / g[i, 1].sum() for i in (rng.integers(0, n, n) for _ in range(B))]
    return tuple(np.round(np.percentile(r, [5, 95]), 2))
def ev(s): return s.pnl.sum() / s.c.sum() if s.c.sum() > 0 else np.nan
def lin(nm, s):
    if len(s) < 30: print("  %-30s n=%d" % (nm, len(s))); return
    print("  %-30s fills %7d $%9.0f EV %+.3f %s hit/p %.2f dias %d" % (nm, len(s), s.c.sum(), ev(s), bs(s), s.win.mean() / s.p.mean(), s.dia.nunique()))
print("dias", sorted(P.dia.unique()), "fills", len(P), "W", int(P.esW.sum()), "fraccion con z finito")
zb = [-99, -3, -2, -1, 0, 1, 99]; P["zb"] = pd.cut(P.zs, zb)
Wd, Pp = P[P.esW], P[~P.esW]
print("\n== A. EV por rasgo del lado comprado: zs = z de Binance con el signo del lado (+ = el spot ya apoya ese lado) ==")
for per in ("DESC", "HOLD"):
    for nm, X in (("POBLACION", P[(~P.esW) & (P.per == per)]), ("W", P[P.esW & (P.per == per)])):
        print("--", per, nm)
        for b, s in X.groupby("zb", observed=True): lin("zs " + str(b), s)
print("\n== A2. por tamano de barrido (niveles distintos <0.10 golpeados en el mismo bloque, mismo mercado+lado) ==")
for per in ("DESC", "HOLD"):
    for nm, X in (("POBLACION", P[(~P.esW) & (P.per == per)]), ("W", P[P.esW & (P.per == per)])):
        print("--", per, nm)
        for b, s_ in X.groupby("swb", observed=True): lin("barrido " + str(b), s_)
print("\n== B. distribucion de fills por zs: W vs poblacion (% de $) ==")
for nm, X in (("POB", Pp), ("W", Wd)):
    print(nm, (X.groupby("zb", observed=True).c.sum() / X.c.sum() * 100).round(1).to_dict())
for v in ("m10s", "ds", "dip", "T"):
    print(v, "mediana POB %.2f W %.2f | p25-p75 POB (%.2f,%.2f) W (%.2f,%.2f)" % (Pp[v].median(), Wd[v].median(), Pp[v].quantile(.25), Pp[v].quantile(.75), Wd[v].quantile(.25), Wd[v].quantile(.75)))
# C. emparejado: reponderar poblacion a la mezcla de W en (act, pb, tb) y comparar EV
cells = ["act", "pb", "tb"]
def matched(per):
    w = Wd[Wd.per == per]; p = Pp[Pp.per == per]
    wc = w.groupby(cells, observed=True).c.sum(); wc = wc / wc.sum()
    pe = p.groupby(cells, observed=True).apply(lambda s: pd.Series({"pnl": s.pnl.sum(), "c": s.c.sum()}))
    pe["ev"] = pe.pnl / pe.c; j = pd.concat([wc.rename("w"), pe.ev], axis=1, join="inner")
    return (j.w * j.ev).sum() / j.w.sum(), ev(w), w.c.sum()
print("\n== C. EV emparejado por (moneda, precio, tiempo) ==")
for per in ("DESC", "HOLD"):
    m, e, c = matched(per); print(per, "EV poblacion emparejada %+.3f | EV W %+.3f | brecha %+.3f ($W %.0f)" % (m, e, e - m, c))
# D. regla minima: reglas candidatas K declarado
RUL = []
for zt in (-1.0, 0.0):                       # el spot no apoya el lado (zs < zt)
    RUL.append(("zs<%.0f" % zt, lambda X, zt=zt: X.zs < zt))
for mt in (-1.0, 0.0, 1.0):                  # el spot en 10 s se mueve CONTRA el lado
    RUL.append(("m10s<%.0f" % mt, lambda X, mt=mt: X.m10s < mt))
for dt_ in (0.2, 0.4):
    RUL.append(("dip>=%.1f" % dt_, lambda X, dt_=dt_: X.dip >= dt_))
for tt in (120, 180):
    RUL.append(("T<%d" % tt, lambda X, tt=tt: X["T"] < tt))
RUL.append(("zs<0 & dip>=0.2", lambda X: (X.zs < 0) & (X.dip >= .2)))
RUL.append(("zs<-1 & T<180", lambda X: (X.zs < -1) & (X["T"] < 180)))
RUL.append(("m10s<0 & zs<0", lambda X: (X.m10s < 0) & (X.zs < 0)))
print("\n== D. reglas candidatas (K=%d) sobre POBLACION ex-W ; elegir en DESC, confirmar en HOLD ; alfa Bonferroni %.4f ==" % (len(RUL), 0.05 / len(RUL)))
rows = []
for nm, f in RUL:
    d_ = Pp[(Pp.per == "DESC")]; h_ = Pp[(Pp.per == "HOLD")]
    sd, sh = d_[f(d_)], h_[f(h_)]; wd, wh = Wd[(Wd.per == "DESC")], Wd[(Wd.per == "HOLD")]
    rows.append((nm, ev(sd), ev(sh), len(sh), sh.win.mean() / sh.p.mean(), f(Wd).mean(), ev(Wd[f(Wd)]), ev(Wd[~f(Wd)])))
print(pd.DataFrame(rows, columns=["regla", "EV_pop_DESC", "EV_pop_HOLD", "n_HOLD", "hit/p_HOLD", "W_frac_$", "EV_W_dentro", "EV_W_fuera"]).round(3).to_string(index=False))

