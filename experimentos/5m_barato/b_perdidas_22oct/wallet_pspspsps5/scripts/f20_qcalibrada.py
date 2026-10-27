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

from sklearn.linear_model import LogisticRegression
print("dias", sorted(P.dia.unique()), "fills", len(P), "W", int(P.esW.sum()))
P["u"] = P.mkt.astype(str) + P.lado.astype(str)
from scipy.stats import norm
P["phi"] = norm.cdf(P.zs.astype(float))
def X_(D):
    lp = np.log(D.p / (1 - D.p))
    return np.column_stack([lp, D.zs.clip(-4, 4), D.zs.clip(-4, 4) ** 2, D["T"] / 100.0, D.m10s.clip(-10, 10), D.dip.clip(0, 1), (D.act == "BTC"), (D.act == "ETH")]).astype(float)
P = P.drop(columns=[c for c in ("d_bps","mov10","mov30","z","pmax_prev","cierre","des") if c in P.columns])
tr = P[(~P.esW) & (P.per == "DESC")].sort_values("ts").groupby("u", observed=True).head(1)
m = LogisticRegression(C=1.0, max_iter=500).fit(X_(tr), tr.win.values)
names = ["logit(p)", "zs", "zs^2", "T/100", "m10s", "dip", "BTC", "ETH"]
print("\n== H-A. Modelo de q calibrada (logit) ajustado SOLO con la poblacion ex-W de DESC, 1er fill por unidad, n=%d ==" % len(tr))
print(dict(zip(names, np.round(m.coef_[0], 3))), "intercepto %.3f" % m.intercept_[0])
print("Phi(zs) crudo vs acierto real en DESC (1er fill): medio Phi %.3f, precio medio %.3f, acierto %.3f" % (tr.phi.mean(), tr.p.mean(), tr.win.mean()))
for per in ("DESC", "HOLD"):
    S = P.loc[P.per == per, ["p","acc","c","pnl","win","zs","m10s","dip","T","act","dia","esW"]].copy(); S["q"] = m.predict_proba(X_(S))[:, 1]; S["r"] = S.q / S.p
    Pp, Wd = S[~S.esW], S[S.esW]
    print("\n-- %s: q^/p medio  poblacion %.3f  W %.3f | q^ medio pob %.4f W %.4f | acierto pob %.4f W %.4f | precio pob %.4f W %.4f" % (per, Pp.r.mean(), Wd.r.mean(), Pp.q.mean(), Wd.q.mean(), Pp.win.mean(), Wd.win.mean(), Pp.p.mean(), Wd.p.mean()))
    qs = np.array(Pp.r.quantile([0, .5, .8, .9, .95, 1.0]).values); qs[0] -= 1e-9; qs[-1] += 1e-9
    for lo, hi in zip(qs[:-1], qs[1:]):
        a, b = Pp[(Pp.r > lo) & (Pp.r <= hi)], Wd[(Wd.r > lo) & (Wd.r <= hi)]
        lin("pob q^/p (%.2f,%.2f]" % (lo, hi), a); lin("  W  q^/p (%.2f,%.2f]" % (lo, hi), b)
    dq = pd.qcut(Pp.q, 5, duplicates="drop", labels=False); print("  calibracion por quintil de q^ (pob): ", [(round(Pp.q[dq == k].mean(), 3), round(Pp.win[dq == k].mean(), 3)) for k in sorted(dq.unique())])
    # regla: elegir fills de la poblacion con q^/p>=tau (tau fijado en DESC como p90 de r) y medir EV
    if per == "DESC": tau = Pp.r.quantile(.9)
    print("  regla r>=tau(%.2f): poblacion" % tau, end=" "); lin("", Pp[Pp.r >= tau]); print("                      W", end=" "); lin("", Wd[Wd.r >= tau])
    print("  W fuera de la regla:", end=" "); lin("", Wd[Wd.r < tau])
