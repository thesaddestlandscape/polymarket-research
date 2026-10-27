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
P = pd.concat([pd.read_csv(f, dtype=_dt, usecols=["li", "ts", "p", "acc", "esW", "pmax_prev", "act", "mkt", "cierre", "lado", "T", "d_bps", "mov10", "mov30", "z"]) for f in sorted(glob.glob(str(O / "feat_2026-*.csv.gz")))], ignore_index=True)
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

print("dias", sorted(P.dia.unique()), "fills", len(P), "W", int(P.esW.sum()))
P = P.sort_values(["mkt", "lado", "ts", "p", "li"])
g = P.groupby(["mkt", "lado", "ts", "p"], observed=True, sort=False)
P["ahead"] = g.acc.cumsum() - P.acc            # acciones rellenadas ANTES en ese nivel y bloque (cola consumida por delante)
P["lvl_acc"] = g.acc.transform("sum"); P["rank"] = g.cumcount()
P["ab"] = pd.cut(P.ahead, [-1, 0.001, 20, 100, 1e9], labels=["0 (primero)", "0-20", "20-100", ">100"])
P["lb"] = pd.cut(P.lvl_acc, [0, 20, 100, 400, 1e9], labels=["<=20", "20-100", "100-400", ">400"])
Wd, Pp = P[P.esW], P[~P.esW]
for per in ("DESC", "HOLD"):
    for nm, X in (("POBLACION", Pp[Pp.per == per]), ("W", Wd[Wd.per == per])):
        print("--", per, nm, "(% de $ por acciones por delante en la cola)", (X.groupby("ab", observed=True).c.sum() / X.c.sum() * 100).round(1).to_dict())
        for b, s in X.groupby("ab", observed=True): lin("delante " + str(b), s)
        for b, s in X.groupby("lb", observed=True): lin("volumen del nivel en el bloque " + str(b), s)
print("\n== emparejado por (moneda, precio, tiempo, cola-por-delante) ==")
cells = ["act", "pb", "tb", "ab"]
for per in ("DESC", "HOLD"):
    w = Wd[Wd.per == per]; p = Pp[Pp.per == per]
    wc = w.groupby(cells, observed=True).c.sum(); wc = wc / wc.sum()
    pe = p.groupby(cells, observed=True).apply(lambda s: pd.Series({"pnl": s.pnl.sum(), "c": s.c.sum()})); pe["ev"] = pe.pnl / pe.c
    j = pd.concat([wc.rename("w"), pe.ev], axis=1, join="inner"); print(per, "EV pop emparejada %+.3f | EV W %+.3f | brecha %+.3f" % ((j.w * j.ev).sum() / j.w.sum(), ev(w), ev(w) - (j.w * j.ev).sum() / j.w.sum()))
