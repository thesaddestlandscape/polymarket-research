"""s6: clase ex ante (hist 17-23 incl.) y rellenos maker del 24-Oct con la MISMA logica que contrapunto s1 (copiada, parametros D=24).
Salida agentes_datos/b_sin_flujo/U24.pkl ; cobertura de desenlace reportada."""
import json, numpy as np, pandas as pd
from pathlib import Path
F6 = Path("/mnt/HC_Volume_106538179/agentes_datos/f6"); NEW = Path("/mnt/HC_Volume_106538179/agentes_datos/b_sin_flujo")
CP = Path("/mnt/HC_Volume_106538179/agentes_datos/contrapunto_informado")
DES = json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json"))
for f in ("/root/polymarket-research-datalogs/mapa_escala/des.json",
          "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/b_vs_poblacion/datos/des_gamma.json"):
    for k, v in json.load(open(f)).items(): DES.setdefault(k, v)
extra = Path("/mnt/HC_Volume_106538179/agentes_datos/b_sin_flujo/des_24.json")
if extra.exists():
    for k, v in json.load(open(extra)).items(): DES.setdefault(k, v)
B = "0x659a40ff"
def win_of(mkt, lado):
    o = pd.Series(mkt).astype(str).map(DES).values
    w = np.where(o == "YES", 1.0, np.where(o == "NO", 0.0, np.nan))
    return np.where(np.asarray(lado) == "YES", w, 1 - w)
daily = pd.read_pickle(CP / "daily.pkl")
def day_stats(d, path):
    x = pd.read_parquet(path, columns=["w", "buy", "acc", "usd", "fee", "mkt", "lado"])
    w = win_of(x.mkt.values, x.lado.astype(str).values); ok = ~np.isnan(w); w = np.nan_to_num(w)
    pnl = np.where(x.buy, x.acc * w - x.usd, x.usd - x.acc * w) - x.fee
    cost = np.where(x.buy, x.usd, x.acc - x.usd)
    g = pd.DataFrame({"w": x.w.astype(str).values, "pnl": np.where(ok, pnl, 0), "c": np.where(ok, cost, 0), "n": 1}).groupby("w").sum()
    g["d"] = d; print("hist", d, len(x), "cob", round(ok.mean(), 4)); return g.reset_index()
if 23 not in set(daily.d): 
    g = day_stats(23, F6 / "T_2026-10-23.parquet"); daily = pd.concat([daily, g], ignore_index=True)
daily["pos"] = (daily.pnl > 0) & (daily.c > 0); daily["neg"] = (daily.pnl < 0) & (daily.c > 0)
def clases(D):
    h = daily[(daily.d >= D - 7) & (daily.d <= D - 1)]
    g = h.groupby("w").agg(n=("n", "sum"), c=("c", "sum"), pnl=("pnl", "sum"), dd=("d", "nunique"), pos=("pos", "sum"), neg=("neg", "sum"))
    g["roi"] = g.pnl / g.c.where(g.c > 0)
    act = (g.n >= 30) & (g.c >= 200) & (g.dd >= 3); fpos = g.pos / g.dd; fneg = g.neg / g.dd
    cl = np.where(~act, "NUEVO", np.where((g.roi >= 0.02) & (fpos >= 0.6), "INF", np.where((g.roi <= -0.02) & (fneg >= 0.6), "DES", "MIX")))
    return pd.DataFrame({"cl": cl, "roi": g.roi.values, "hc": g.c.values}, index=g.index)
D = 24; C = clases(D)
T = pd.read_parquet(NEW / "T_2026-10-24.parquet", columns=["ts", "w", "usd", "mkt"])
T["cl"] = T.w.astype(str).map(C.cl).fillna("NUEVO").values
M = pd.read_parquet(NEW / "M_2026-10-24.parquet", columns=["ts", "tx", "act", "mkt", "cierre", "lado", "acc", "usd", "p", "maker", "taker"])
M = M[(M.p >= 0.05) & (M.p <= 0.30)].copy(); M["maker"] = M.maker.astype(str); M["taker"] = M.taker.astype(str)
M["cl"] = M.taker.map(C.cl).fillna("NUEVO").values; M["tk_roi"] = M.taker.map(C.roi).values
w = win_of(M.mkt.values, M.lado.astype(str).values); M["cob"] = ~np.isnan(w)
M["pnl"] = M.acc * np.nan_to_num(w) - M.usd; M["c"] = M.usd
M["dia"] = "2026-10-24"; M["T"] = M.ts - (M.cierre - 300); M["isB"] = M.maker.str.startswith(B)
print("n", len(M), "cob€", round(M.c[M.cob].sum() / M.c.sum(), 4), "cob mercados", round(M.drop_duplicates("mkt").cob.mean(), 4))
print("cuota € por clase", M.groupby("cl").c.sum().div(M.c.sum()).round(3).to_dict())
M.drop(columns=["tx"]).to_pickle(NEW / "U24.pkl")
M[~M.cob].drop_duplicates("mkt")[["mkt","act","cierre"]].to_csv(NEW / "sin_des_24.csv", index=False)
