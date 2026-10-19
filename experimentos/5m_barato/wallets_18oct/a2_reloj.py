#!/usr/bin/env python3
"""a2_reloj.py DIA [fills.parquet tx.csv.gz out.parquet] -- reloj causal por orden TOMADORA de la celda H5M.
Hora del casado = fila t del registro ms (hora de EXCHANGE de Polymarket, c[1]) emparejada con el fill on-chain por (token, precio, tamaño) con la
hora de bloque DESPUES (bloque - casado en [0,3 ; 10] s); sin pareja -> se descarta (no se inventa). Binance: aggTrade (x), rejilla de 100 ms por hora de
EXCHANGE de Binance (c[1]) y por RECEPCION (c[7]). Salida por orden tomadora (tx): retornos de Binance con signo del lado apostado por el tomador
(+ = a favor del tomador) en lags relativos a la hora del casado, retorno desde la apertura del mercado (fin-300 s), etc."""
import sys, gzip
import numpy as np, pandas as pd
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib import *
d = sys.argv[1]
fp = sys.argv[2] if len(sys.argv) > 2 else CACHE + f"fills_{d}.parquet"
tp = sys.argv[3] if len(sys.argv) > 3 else CACHE + f"tx_{d}.csv.gz"
op = sys.argv[4] if len(sys.argv) > 4 else CACHE + f"reloj_{d}.parquet"
F = pd.read_parquet(fp); F = F[F.is_tk == 0]
X = en_celda(deriva(F)); X, cob = con_resultado(X)
X["p_tok"] = np.where(X.venta, (X.sh - X.coste_m) if False else np.nan, np.nan)
# precio del TOKEN: si el maker vende el token (side 1): recibe usdc=taker_amt por maker_amt acciones; si lo compra: paga maker_amt por taker_amt
usd = np.where(X.venta, X.taker_amt, X.maker_amt)
X["p_tok"] = usd / X.sh
X["sh4"] = (X.sh * 1e4).round().astype("int64"); X["p3"] = (X.p_tok * 1000).round().astype("int64")
toks = {t: i for i, t in enumerate(X.tok.unique())}
X["tid"] = X.tok.map(toks).astype("int32")
day0 = int(pd.Timestamp(d).timestamp()) - 3600
NB = (86400 + 7200) * 10
coins = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
GR = {c: {"T": np.full(NB, np.nan), "R": np.full(NB, np.nan)} for c in coins}
tt, tp_, tsz, ttx, trx = [], [], [], [], []
n_x = n_t = 0
with gzip.open(tp, "rt", errors="replace") as fh:
    for ln in fh:
        if ln[0] == "x":
            c = ln.split(",")
            try:
                co = c[2][:-4]; p = float(c[3]); T = int(c[1]) / 1000.0; R = int(c[7]) / 1000.0
            except (ValueError, IndexError):
                continue
            g = GR.get(co)
            if g is None: continue
            b = int((T - day0) * 10)
            if 0 <= b < NB: g["T"][b] = p
            b = int((R - day0) * 10)
            if 0 <= b < NB: g["R"][b] = p
            n_x += 1
        elif ln[0] == "t":
            c = ln.split(",")
            ti = toks.get(c[2])
            if ti is None: continue
            try:
                tt.append(int(c[1])); ttx.append(ti); tp_.append(round(float(c[3]) * 1000)); tsz.append(round(float(c[5]) * 1e4)); trx.append(int(c[6]))
            except (ValueError, IndexError):
                continue
            n_t += 1
print(d, "x", n_x, "t (tokens de la celda)", n_t, flush=True)
Tt = pd.DataFrame({"tex": np.array(tt) / 1000.0, "tid": np.array(ttx, dtype="int32"), "p3": np.array(tp_, dtype="int64"), "sh4": np.array(tsz, dtype="int64"), "trx": np.array(trx) / 1000.0})
del tt, ttx, tp_, tsz, trx
# relleno ffill de la rejilla (ultimo precio conocido) por moneda
for co in coins:
    for k in ("T", "R"):
        s = pd.Series(GR[co][k]).ffill().values; GR[co][k] = s
# --- emparejado fill <-> t
X = X.sort_values("ts").reset_index(drop=True)
X["ts_m"] = X.ts - 0.3
Tt = Tt.sort_values("tex").reset_index(drop=True)
def asof(L, R_, keys):
    L = L.sort_values("ts_m"); R_ = R_.sort_values("tex")
    return pd.merge_asof(L, R_, left_on="ts_m", right_on="tex", by=keys, direction="backward", tolerance=9.7)
M1 = asof(X[["tx", "li", "tid", "p3", "sh4", "ts_m", "ts"]], Tt[["tex", "tid", "p3", "sh4", "trx"]], ["tid", "p3", "sh4"])
# nivel (tx, token, precio): tamaño agregado
X["sh4_agg"] = X.groupby(["tx", "tid", "p3"]).sh4.transform("sum")
M2 = asof(X[["tx", "li", "tid", "p3", "ts_m"]].assign(sh4=X.sh4_agg), Tt[["tex", "tid", "p3", "sh4"]], ["tid", "p3", "sh4"])
M1 = M1.set_index(["tx", "li"]); M2 = M2.set_index(["tx", "li"])
X = X.set_index(["tx", "li"])
X["tex"] = M1.tex.reindex(X.index).values
X["via"] = np.where(X.tex.notna(), "fila", "")
sin = X.tex.isna()
X.loc[sin, "tex"] = M2.tex.reindex(X.index[sin]).values
X.loc[sin & X.tex.notna(), "via"] = "agregado"
X = X.reset_index()
print(d, "fills celda", len(X), "con casado (exch)", int(X.tex.notna().sum()), f"{X.tex.notna().mean():.1%}", "| via fila", int((X.via == "fila").sum()), "agregado", int((X.via == "agregado").sum()), flush=True)
X["dt_blk"] = X.ts - X.tex
print("bloque - casado (s):", X.dt_blk.describe(percentiles=[.05, .5, .95]).round(2).to_dict())
Xm = X[X.tex.notna()].copy()
# --- retornos de Binance a favor del tomador. Tomador apuesta al complemento de lado_c: si lado_c=='YES' (maker compra YES) -> tomador apuesta Down (-1) ; si 'NO' -> Up (+1)
Xm["sg"] = np.where(Xm.lado_c == "YES", -1.0, 1.0)
LAGS = [-30, -10, -5, -2, -1, -0.5, -0.25, -0.1, 0.1, 0.25, 0.5, 1, 2, 5, 10, 30]
def px(co_arr, key, t):
    out = np.full(len(t), np.nan)
    for co in coins:
        m = co_arr == co
        if not m.any(): continue
        b = np.floor((t[m] - day0) * 10).astype(np.int64)
        ok = (b >= 0) & (b < NB)
        v = np.full(m.sum(), np.nan); v[ok] = GR[co][key][b[ok]]
        out[m] = v
    return out
act = Xm.act.values
for key, nm in (("T", "ex"), ("R", "rx")):
    p0 = px(act, key, Xm.tex.values)
    for L in LAGS:
        pl = px(act, key, Xm.tex.values + L)
        Xm[f"r{nm}_{L:+g}"] = Xm.sg.values * (pl - p0) / p0 * 1e4 if L > 0 else Xm.sg.values * (p0 - pl) / pl * 1e4   # pre: retorno de (t+L) a t ; post: de t a t+L
    # apertura del mercado
    po = px(act, key, Xm.fin.values - 300.0)
    Xm[f"ropen_{nm}"] = Xm.sg.values * (p0 - po) / po * 1e4
    Xm[f"vol30_{nm}"] = np.nan
Xm.drop(columns=["tok", "sh4", "p3", "tid", "ts_m", "sh4_agg", "maker_amt", "taker_amt", "fee", "side", "is_tk"], errors="ignore").to_parquet(op)
print("->", op, len(Xm))
