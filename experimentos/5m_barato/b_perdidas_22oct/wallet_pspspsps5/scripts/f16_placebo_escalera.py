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

print("dias", sorted(P.dia.unique()), "fills", len(P), "W", int(P.esW.sum()))
P["u"] = P.mkt.astype(str) + P.lado.astype(str)
Wd, Pp = P[P.esW], P[~P.esW]
# 1. NULL: W (fills <0.10) vs submuestras de unidades de la poblacion, estratificadas por moneda, mismo n de unidades por periodo y moneda
print("\n== 1. PLACEBO: EV de W frente a muestras aleatorias de unidades (mercado+lado) de la poblacion con la misma mezcla de monedas ==")
for per in ("DESC", "HOLD", "TODO"):
    sel = (P.per != "x") if per == "TODO" else (P.per == per)
    w = Wd[sel[Wd.index]]; p = Pp[sel[Pp.index]]
    uw = w.groupby("u").act.first().value_counts().to_dict()
    ug = p.groupby("u", observed=True).agg(pnl=("pnl", "sum"), c=("c", "sum"), act=("act", "first")).reset_index()
    ew = w.pnl.sum() / w.c.sum(); null = []
    byact = {a: x for a, x in ug.groupby("act", observed=True)}
    for _ in range(1500):
        s = pd.concat([byact[a].sample(n, random_state=int(rng.integers(1e9))) for a, n in uw.items() if a in byact]); null.append(s.pnl.sum() / s.c.sum())
    null = np.array(null); print("%s: W EV %+.3f (unid %d) | nulo media %+.3f sd %.3f | z %.1f | p(nulo>=W) %.4f" % (per, ew, sum(uw.values()), null.mean(), null.std(), (ew - null.mean()) / null.std(), (null >= ew).mean()))
# 2. escalera ingenua OPTIMISTA: bid de 10 acc en cada tick 0.01..0.09, fill a nivel L la primera vez que hay una operacion pasiva a precio <= L en esa unidad
print("\n== 2. ESCALERA INGENUA (optimista: sin cola) sobre unidades de la poblacion: relleno en L cuando algun relleno <=L toca el nivel; 10 acc por nivel ==")
rows = []
for L in np.round(np.arange(.01, .10, .01), 2):
    s = P[P.p <= L + 1e-6].sort_values("ts").groupby("u", observed=True).head(1)
    s = s.assign(Lc=L * 10.0, Lp=10.0 * (s.win - L), esW_=s.esW)
    rows.append(s[["u", "dia", "per", "act", "win", "zs", "m10s", "T", "Lc", "Lp"]].assign(L=L))
LL = pd.concat(rows, ignore_index=True)
def ev2(s): return s.Lp.sum() / s.Lc.sum() if len(s) else np.nan
def bs2(s, B=1000):
    g = s.groupby("dia")[["Lp", "Lc"]].sum().values; n = len(g)
    if n < 2: return (np.nan, np.nan)
    r = [g[i, 0].sum() / g[i, 1].sum() for i in (rng.integers(0, n, n) for _ in range(B))]
    return tuple(np.round(np.percentile(r, [5, 95]), 2))
for per in ("DESC", "HOLD"):
    S = LL[LL.per == per]
    print("--", per, "todas las posiciones tocadas: n %d EV %+.3f %s" % (len(S), ev2(S), bs2(S)))
    for nm, m in (("T<=180", S["T"] <= 180), ("T<=120", S["T"] <= 120), ("zs>-1 (spot no contra el lado)", S.zs > -1), ("zs>-1 & T<=180", (S.zs > -1) & (S["T"] <= 180)), ("m10s>=0 (spot no se va contra el lado)", S.m10s >= 0)):
        X = S[m]; print("   %-38s n %6d EV %+.3f %s" % (nm, len(X), ev2(X), bs2(X)))
    for L in (.02, .05, .09):
        X = S[np.isclose(S.L, L)]; print("   nivel %.2f: n %d EV %+.3f" % (L, len(X), ev2(X)))
