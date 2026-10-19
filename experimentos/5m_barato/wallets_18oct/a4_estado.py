#!/usr/bin/env python3
"""a4_estado.py DIA -- features de ESTADO (observables antes de la decision, sin el casado) para TODOS los fills maker de la celda H5M:
retorno de Binance desde la apertura del mercado (fin-300 s) hasta tau = ts_bloque - 2,5 s (reloj de RECEPCION de Binance), signado hacia lado_c
(+ = el lado que compra el maker va por delante), sigma del dia por moneda (retornos de 10 s), z_rem = ropen/(sigma*sqrt(T)), P_fair = Phi(z_rem).
Salida: estado_D.parquet con una fila por fill de la celda. NO usa el resultado (pnl) para las features. Solo lectura."""
import sys, gzip, math
import numpy as np, pandas as pd
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib import *
d = sys.argv[1]
fp = sys.argv[2] if len(sys.argv) > 2 else CACHE + f"fills_{d}.parquet"
tp = sys.argv[3] if len(sys.argv) > 3 else CACHE + f"tx_{d}.csv.gz"
op = sys.argv[4] if len(sys.argv) > 4 else CACHE + f"estado_{d}.parquet"
F = pd.read_parquet(fp); F = F[F.is_tk == 0]
X = en_celda(deriva(F)); X, cob = con_resultado(X)
day0 = int(pd.Timestamp(d).timestamp()) - 3600
NB = (86400 + 7200) * 10
coins = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
GR = {c: np.full(NB, np.nan) for c in coins}
with gzip.open(tp, "rt", errors="replace") as fh:
    for ln in fh:
        if ln[0] != "x": continue
        c = ln.split(",")
        try:
            co = c[2][:-4]; p = float(c[3]); R = int(c[7]) / 1000.0
        except (ValueError, IndexError):
            continue
        g = GR.get(co)
        if g is None: continue
        b = int((R - day0) * 10)
        if 0 <= b < NB: g[b] = p
SIG = {}
for co in coins:
    s = pd.Series(GR[co]).ffill().values; GR[co] = s
    r = np.diff(np.log(s[~np.isnan(s)][::100]))   # pasos de 10 s
    SIG[co] = float(np.nanstd(r[np.abs(r) < 0.01]) / math.sqrt(10)) * 1e4   # bps por sqrt(s)
print(d, "sigma bps/sqrt(s)", {k: round(v, 3) for k, v in SIG.items()}, flush=True)
tau = X.ts.values - 2.5
act = X.act.values
pt = np.full(len(X), np.nan); po = np.full(len(X), np.nan)
for co in coins:
    m = act == co
    if not m.any(): continue
    bt = np.floor((tau[m] - day0) * 10).astype(np.int64); bo = np.floor((X.fin.values[m] - 300.0 - day0) * 10).astype(np.int64)
    ok = (bt >= 0) & (bt < NB) & (bo >= 0) & (bo < NB)
    a = np.full(m.sum(), np.nan); b = np.full(m.sum(), np.nan)
    a[ok] = GR[co][bt[ok]]; b[ok] = GR[co][bo[ok]]
    pt[m] = a; po[m] = b
sg = np.where(X.lado_c.values == "YES", 1.0, -1.0)         # + = Binance sube a favor del lado que compra el maker (YES = Up)
X["ropen"] = sg * (pt - po) / po * 1e4
sig = X.act.map(SIG).values
Trem = np.maximum(X.fin.values - tau, 1.0)
X["z_rem"] = X.ropen.values / (sig * np.sqrt(Trem))
from math import erf
X["p_fair"] = 0.5 * (1 + np.vectorize(lambda z: erf(z / math.sqrt(2)) if np.isfinite(z) else np.nan)(X.z_rem.values))
X["dia"] = d
keep = ["dia", "tx", "li", "maker", "taker", "act", "mkt", "fin", "ts", "T", "lado_c", "pc", "sh", "coste_m", "pnl_m", "coste_t", "pnl_t", "venta", "ropen", "z_rem", "p_fair"]
X[keep].to_parquet(op)
print(d, "filas", len(X), "con estado", int(X.z_rem.notna().sum()), "->", op)
