"""CONTRAPUNTO s1: clase ex ante del tomador (walk-forward D-7..D-1) + rellenos maker 17-23 Oct con clase y rasgos previos.
Solo lectura de agentes_datos/f6. Salida: VOL/agentes_datos/contrapunto_informado/U.pkl (rellenos) y cobertura."""
import json, numpy as np, pandas as pd
from pathlib import Path
F6 = Path("/mnt/HC_Volume_106538179/agentes_datos/f6"); OUT = Path("/mnt/HC_Volume_106538179/agentes_datos/contrapunto_informado")
DES = json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json"))
for f in ("/root/polymarket-research-datalogs/mapa_escala/des.json",
          "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/b_vs_poblacion/datos/des_gamma.json"):
    for k, v in json.load(open(f)).items(): DES.setdefault(k, v)
B = "0x659a40ff"
dia = lambda d: "2026-10-%02d" % d
HIST = range(10, 23); MEAS = range(17, 24)
def win_of(mkt, lado):
    o = pd.Series(mkt).astype(str).map(DES).values
    w = np.where(o == "YES", 1.0, np.where(o == "NO", 0.0, np.nan))
    return np.where(np.asarray(lado) == "YES", w, 1 - w)
# 1) estadistica diaria por tomador
daily = []
for d in HIST:
    x = pd.read_parquet(F6 / f"T_{dia(d)}.parquet", columns=["w", "buy", "acc", "usd", "fee", "mkt", "lado"])
    w = win_of(x.mkt.values, x.lado.astype(str).values); ok = ~np.isnan(w); w = np.nan_to_num(w)
    pnl = np.where(x.buy, x.acc * w - x.usd, x.usd - x.acc * w) - x.fee
    cost = np.where(x.buy, x.usd, x.acc - x.usd)
    g = pd.DataFrame({"w": x.w.astype(str).values, "pnl": np.where(ok, pnl, 0), "c": np.where(ok, cost, 0), "n": 1}).groupby("w").sum()
    g["d"] = d; daily.append(g.reset_index()); print("hist", d, len(x), "cob", round(ok.mean(), 4), flush=True)
daily = pd.concat(daily, ignore_index=True)
daily["pos"] = (daily.pnl > 0) & (daily.c > 0)
daily["neg"] = (daily.pnl < 0) & (daily.c > 0)
def clases(D):
    h = daily[(daily.d >= D - 7) & (daily.d <= D - 1)]
    g = h.groupby("w").agg(n=("n", "sum"), c=("c", "sum"), pnl=("pnl", "sum"), dd=("d", "nunique"), pos=("pos", "sum"), neg=("neg", "sum"))
    g["roi"] = g.pnl / g.c.where(g.c > 0)
    act = (g.n >= 30) & (g.c >= 200) & (g.dd >= 3)
    fpos = g.pos / g.dd; fneg = g.neg / g.dd
    cl = np.where(~act, "NUEVO", np.where((g.roi >= 0.02) & (fpos >= 0.6), "INF", np.where((g.roi <= -0.02) & (fneg >= 0.6), "DES", "MIX")))
    return pd.DataFrame({"cl": cl, "roi": g.roi.values, "hc": g.c.values}, index=g.index)
# 2) rellenos maker y flujo tomador por dia de medida
U = []
for D in MEAS:
    C = clases(D)
    T = pd.read_parquet(F6 / f"T_{dia(D)}.parquet", columns=["ts", "w", "usd", "mkt"])
    T["cl"] = T.w.astype(str).map(C.cl).fillna("NUEVO").values
    M = pd.read_parquet(F6 / f"M_{dia(D)}.parquet", columns=["ts", "tx", "act", "mkt", "cierre", "lado", "acc", "usd", "p", "maker", "taker"])
    M = M[(M.p >= 0.05) & (M.p <= 0.30)].copy()
    M["maker"] = M.maker.astype(str); M["taker"] = M.taker.astype(str)
    M["cl"] = M.taker.map(C.cl).fillna("NUEVO").values; M["tk_roi"] = M.taker.map(C.roi).values
    w = win_of(M.mkt.values, M.lado.astype(str).values); M["cob"] = ~np.isnan(w)
    M["pnl"] = M.acc * np.nan_to_num(w) - M.usd; M["c"] = M.usd
    # flujo previo en el mismo mercado por clase: ventanas [t-33,t-5) y [t-130,t-33)
    mk = T.mkt.astype(str).values; ts = T.ts.values
    o = np.lexsort((ts, mk)); mks = mk[o]; tss = ts[o]
    um = M.mkt.astype(str).values; tu = M.ts.values
    # vectorizado: clave combinada
    code, uniq = pd.factorize(np.concatenate([mks, um]))
    cT = code[:len(mks)].astype(np.float64); cU = code[len(mks):].astype(np.float64)
    key = cT * 1e10 + (tss - 1.7e9); ok_sorted = np.all(np.diff(key) >= 0)
    if not ok_sorted:
        o2 = np.argsort(key, kind="stable"); key = key[o2]; o = o[o2]
    pos = lambda off: np.searchsorted(key, cU * 1e10 + (tu - off - 1.7e9), "left")
    p5, p33, p130 = pos(5), pos(33), pos(130)
    usd_s = T.usd.values[o]; cl_s = T.cl.values[o]
    for nm, mask in (("all", np.ones(len(o), bool)), ("inf", cl_s == "INF"), ("des", cl_s == "DES"), ("new", cl_s == "NUEVO")):
        cs = np.concatenate([[0.0], np.cumsum(np.where(mask, usd_s, 0.0))])
        M[f"f33_{nm}"] = cs[p5] - cs[p33]; M[f"f130_{nm}"] = cs[p33] - cs[p130]
    M["dia"] = dia(D); M["T"] = M.ts - (M.cierre - 300)
    M["isB"] = M.maker.str.startswith(B)
    M["maker"] = M.maker.astype("category"); M["taker"] = M.taker.astype("category"); M["mkt"] = M.mkt.astype("category")
    U.append(M.drop(columns=["tx"])); print("meas", D, len(M), "B", int(M.isB.sum()), "cob€", round(M.c[M.cob].sum() / M.c.sum(), 4),
                         M.groupby("cl").c.sum().div(M.c.sum()).round(3).to_dict(), flush=True)
from pandas.api.types import union_categoricals
for c in ("maker", "taker", "mkt", "act", "lado"):
    uc = union_categoricals([u[c] for u in U]).categories
    for u in U: u[c] = pd.Categorical(u[c].astype(object), categories=uc)
U = pd.concat(U, ignore_index=True)
for c in ("cl", "dia"): U[c] = U[c].astype("category")
U.to_pickle(OUT / "U.pkl"); daily.to_pickle(OUT / "daily.pkl"); print("hecho", len(U))
