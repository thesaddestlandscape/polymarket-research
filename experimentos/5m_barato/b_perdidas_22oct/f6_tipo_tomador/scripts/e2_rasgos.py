"""F6 e2: rasgos EX ANTE del tomador de cada unidad (tab.pkl 09-21 Oct) + composicion reciente del flujo del mercado. Solo historial anterior a ts-LAG.
Ventana historia = 96 h antes de (ts - 10 s). Sin ningun calculo de EV. Salida datos/units_clases.pkl"""
import sys, json
import numpy as np, pandas as pd
from pathlib import Path
from pandas.api.types import union_categoricals
VOL = Path("/mnt/HC_Volume_106538179"); F6 = VOL / "agentes_datos" / "f6"
OUT = Path("/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f6_tipo_tomador/datos")
LAG = 10.0; WIN = 96 * 3600.0; RES_LAG = 120.0
DES = json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json"))
dias = ["2026-10-%02d" % d for d in range(5, 24)]
cols = ["ts", "w", "buy", "p", "usd", "acc", "fee", "mkt", "cierre", "lado", "act"]
files = [F6 / f"T_{d}.parquet" for d in dias if (F6 / f"T_{d}.parquet").exists()]
allw = pd.Index([])
for f in files:
    allw = allw.union(pd.read_parquet(f, columns=["w"]).w.cat.categories)
wcat = allw; cid_ = {w: i for i, w in enumerate(wcat)}
L = {k: [] for k in ("wcode", "ts", "buy", "usd", "acc", "fee", "mk", "cierre", "ladoy", "mkt_s")}
for f in files:
    x = pd.read_parquet(f, columns=cols)
    cw = np.array([cid_[w] for w in x.w.cat.categories], dtype=np.int64)
    L["wcode"].append(cw[x.w.cat.codes.values]); L["ts"].append(x.ts.values.astype(np.float64)); L["buy"].append(x.buy.values)
    L["usd"].append(x.usd.values.astype(np.float64)); L["acc"].append(x.acc.values.astype(np.float64)); L["fee"].append(x.fee.values.astype(np.float64))
    L["mk"].append(x.mkt.astype(np.int64).values); L["cierre"].append(x.cierre.values.astype(np.int64)); L["ladoy"].append((x.lado.astype(str).values == "YES"))
    del x
A = {k: np.concatenate(v) for k, v in L.items() if k != "mkt_s"}; del L
wcode = A["wcode"]; ts = A["ts"]; buy = A["buy"]; usd = A["usd"]; acc = A["acc"]; fee = A["fee"]; mk = A["mk"]; cierre = A["cierre"]
print("taker rows", len(ts), "wallets", len(wcat), flush=True)
um, inv = np.unique(mk, return_inverse=True)
dm = np.array([DES.get(str(m), "") for m in um]); win_u = np.where(dm == "YES", 1.0, np.where(dm == "NO", 0.0, np.nan))
win = np.where(A["ladoy"], win_u[inv], 1.0 - win_u[inv]); cob = ~np.isnan(win); win = np.nan_to_num(win)
pnl = np.where(buy, acc * win - usd, usd - acc * win) - fee
cost = np.where(buy, usd, acc - usd)
print("cobertura desenlace taker rows", cob.mean(), flush=True)
# orden por (wallet, ts)
key = wcode * 10**10 + ts.astype(np.int64)
o = np.argsort(key, kind="stable"); ks = key[o]
csu = np.concatenate([[0.0], np.cumsum(usd[o])]); del key, o
def ventana(code, t):
    """n filas y usd del wallet en [t-WIN, t-LAG)"""
    hi = np.searchsorted(ks, code * 10**10 + np.floor(t - LAG).astype(np.int64), "left")
    lo = np.searchsorted(ks, code * 10**10 + np.floor(t - LAG - WIN).astype(np.int64), "left")
    return (hi - lo), (csu[hi] - csu[lo])
# ROI previo (resolved): orden por (wallet, cierre), solo filas con desenlace, compras
m_r = cob & buy
kr = wcode[m_r] * 10**10 + cierre[m_r]; orr = np.argsort(kr, kind="stable"); krs = kr[orr]
cpn = np.concatenate([[0.0], np.cumsum(pnl[m_r][orr])]); ccs = np.concatenate([[0.0], np.cumsum(cost[m_r][orr])])
def roi(code, t):
    hi = np.searchsorted(krs, code * 10**10 + np.floor(t - RES_LAG).astype(np.int64), "left")
    lo = np.searchsorted(krs, code * 10**10 + np.floor(t - RES_LAG - WIN).astype(np.int64), "left")
    return cpn[hi] - cpn[lo], ccs[hi] - ccs[lo]
del kr, orr, pnl, cost, win, cob, inv, um, dm, win_u, A, m_r
import gc; gc.collect()
# dias distintos activos en la ventana: dia entero del timestamp (4 dias previos) via set (w,dia)
acc=fee=None
dayi = (ts // 86400).astype(np.int64)
wd = np.unique(wcode * 1000 + (dayi - dayi.min()))
wdset_sorted = wd
def ndias(code, t):
    d0 = (np.floor(t) // 86400).astype(np.int64) - dayi.min(); n = np.zeros(len(code), int)
    for k in range(0, 5):
        q = code * 1000 + (d0 - k)
        i = np.searchsorted(wdset_sorted, q); n += (i < len(wdset_sorted)) & (wdset_sorted[np.clip(i, 0, len(wdset_sorted) - 1)] == q)
    return n
# --- clase por fila de tomador (para composicion del flujo)
nrow, _ = ventana(wcode, ts)
T_n = nrow
# --- unidades
U = pd.read_pickle("/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl")
cid = {w: i for i, w in enumerate(wcat)}; ucode = U.taker.map(cid).fillna(-1).astype(np.int64).values
tu = U.ts.values.astype(np.float64)
known = ucode >= 0; n_u = np.zeros(len(U), int); usd_u = np.zeros(len(U)); nd_u = np.zeros(len(U), int); rp = np.zeros(len(U)); rc = np.zeros(len(U))
a, b = ventana(ucode[known], tu[known]); n_u[known] = a; usd_u[known] = b
nd_u[known] = ndias(ucode[known], tu[known])
a, b = roi(ucode[known], tu[known]); rp[known] = a; rc[known] = b
U["tk_n"] = n_u; U["tk_usd"] = usd_u; U["tk_ndias"] = nd_u; U["tk_ticket"] = np.where(n_u > 0, usd_u / np.maximum(n_u, 1), np.nan)
U["tk_roi_pnl"] = rp; U["tk_roi_cost"] = rc; U["tk_known"] = known
# --- composicion reciente del flujo del mercado: ventana [t-130, t-10) en el mismo mkt, por clase de cada fila
UM = U.mkt.astype(np.int64).values
km = mk * 10**10 + ts.astype(np.int64); om = np.argsort(km, kind="stable"); kms = km[om]
def comp(mask_rows):
    c = np.concatenate([[0.0], np.cumsum(np.where(mask_rows, usd, 0.0)[om])])
    hi = np.searchsorted(kms, UM * 10**10 + np.floor(tu - LAG).astype(np.int64), "left"); lo = np.searchsorted(kms, UM * 10**10 + np.floor(tu - 130).astype(np.int64), "left")
    return c[hi] - c[lo], (hi - lo)
U["fl_usd_all"], U["fl_n_all"] = comp(np.ones(len(ts), bool))
for nm, thr in (("rep200", 200), ("bot2000", 2000)):
    U["fl_usd_" + nm], _ = comp(T_n >= thr)
U.to_pickle(OUT / "units_clases.pkl")
print("hecho", len(U), flush=True)
