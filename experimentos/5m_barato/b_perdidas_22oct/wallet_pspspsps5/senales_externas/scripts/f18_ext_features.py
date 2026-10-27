#!/usr/bin/env python3
"""f18: senales externas por fill (poblacion+W, <0.10). Todo con marcas de RECEPCION. t0 = ts-3 s (como f13).
Chainlink (RTDS, timestamp_utc de recepcion): d_cl, z_cl (sigma propia 1 s), ref_cl = media por ws_timestamp en [open-62, open-3] (aprox. regla oficial).
Cross-asset: z_cl de BTC/ETH/SOL en el mismo cierre y t0. Basis = d_cl - d_bn (bps). Imbalance Binance bookticker (bid_qty-ask_qty)/(sum).
Markouts (SOLO descriptivos, usan el futuro del fill): fwd5/fwd30 = movimiento Binance y Chainlink de t0 a ts+5/ts+30 (bps).
Salida ext_D.csv.gz en datalogs/wallet_pspspsps5/senales_externas."""
import sys, gzip
import numpy as np, pandas as pd
from pathlib import Path
DL = Path("/root/polymarket-research-datalogs"); O = DL / "wallet_pspspsps5"; X = O / "senales_externas"; PR = Path("/root/polymarket-research/data/prices")
def cl(d):
    for f in (PR / f"chainlink_{d}.csv.gz", PR / f"chainlink_{d}.csv"):
        if f.exists():
            x = pd.read_csv(f, usecols=["timestamp_utc", "asset", "price_usd", "ws_timestamp_ms", "source"])
            x = x[x.source == "chainlink"]
            x["tr"] = (pd.to_datetime(x.timestamp_utc, utc=True, format="ISO8601") - pd.Timestamp("1970-01-01", tz="UTC")).dt.total_seconds()
            x["tw"] = pd.to_numeric(x.ws_timestamp_ms, errors="coerce") / 1000.0
            x = x.dropna(subset=["tr", "tw", "price_usd"])
            return x[["asset", "price_usd", "tr", "tw"]]
    return None
def bt(d):
    f = DL / f"binance_bookticker_{d}.csv"
    if not f.exists(): return None
    x = pd.read_csv(f, usecols=["ts_recepcion_ms", "activo", "mid", "bid_qty", "ask_qty"]).dropna(); x = x[x.mid > 0]; x["t"] = x.ts_recepcion_ms / 1000.0; return x
def prep_asset(C, a):
    s = C[C.asset == a].sort_values("tr")
    s = s[s.price_usd > 0]
    tr = s.tr.values; pr = s.price_usd.values.astype(float); tw = s.tw.values
    grid = np.arange(np.ceil(tr[0]), tr[-1], 1.0); pg = pr[np.clip(np.searchsorted(tr, grid, side="right") - 1, 0, len(pr) - 1)]
    sg = np.diff(np.log(pg)); sg = sg[np.isfinite(sg)]
    o = np.argsort(tw, kind="stable"); twc = tw[o]; prw = pr[o]
    return dict(tr=tr, pr=pr, tw=twc, prw=prw, cs=np.concatenate([[0], np.cumsum(prw)]), sig=np.std(sg))
def at(A, x): return A["pr"][np.clip(np.searchsorted(A["tr"], x, side="right") - 1, 0, len(A["pr"]) - 1)]
def ref(A, a0, a1):
    i0 = np.searchsorted(A["tw"], a0); i1 = np.searchsorted(A["tw"], a1, side="right"); n = i1 - i0
    return np.where(n > 0, (A["cs"][i1] - A["cs"][i0]) / np.maximum(n, 1), np.nan)
for d in sys.argv[1:]:
    out = X / f"ext_{d}.csv.gz"
    if out.exists(): continue
    P = pd.read_csv(O / f"feat_{d}.csv.gz", dtype={"mkt": str})
    prev = (pd.Timestamp(d) - pd.Timedelta(days=1)).strftime("%Y-%m-%d"); nxt = (pd.Timestamp(d) + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    C = pd.concat([x for x in (cl(prev), cl(d), cl(nxt)) if x is not None], ignore_index=True)
    B = pd.concat([x for x in (bt(prev), bt(d), bt(nxt)) if x is not None], ignore_index=True)
    CA = {a: prep_asset(C, a) for a in C.asset.unique()}
    t0 = P.ts.values - 3.0; cie = P.cierre.values.astype(float); op = cie - 300.0; Tt = np.maximum(P["T"].values, 1.0)
    def zc(a, t0_, cie_, op_, T_):
        if a not in CA: return np.full(len(t0_), np.nan), np.full(len(t0_), np.nan)
        A = CA[a]; r = ref(A, op_ - 62, op_ - 3); S = at(A, t0_)
        dd = (S - r) / r * 1e4
        return dd, np.log(S / r) / (A["sig"] * np.sqrt(T_))
    P["d_cl"] = np.nan; P["z_cl"] = np.nan; P["fwd5_cl"] = np.nan; P["fwd30_cl"] = np.nan; P["mov10_cl"] = np.nan; P["mov30_cl"] = np.nan
    P["imb"] = np.nan; P["fwd5_bn"] = np.nan; P["fwd30_bn"] = np.nan; P["lag_cl"] = np.nan
    for a, g in P.groupby("act"):
        ix = g.index.values
        if a in CA:
            A = CA[a]; dd, zz = zc(a, t0[ix], cie[ix], op[ix], Tt[ix]); P.loc[ix, "d_cl"] = dd; P.loc[ix, "z_cl"] = zz
            S0 = at(A, t0[ix]); ts_ = P.ts.values[ix]
            P.loc[ix, "fwd5_cl"] = (at(A, ts_ + 5) - S0) / S0 * 1e4; P.loc[ix, "fwd30_cl"] = (at(A, ts_ + 30) - S0) / S0 * 1e4
            P.loc[ix, "mov10_cl"] = (S0 - at(A, t0[ix] - 10)) / S0 * 1e4; P.loc[ix, "mov30_cl"] = (S0 - at(A, t0[ix] - 30)) / S0 * 1e4
            P.loc[ix, "lag_cl"] = t0[ix] - A["tr"][np.clip(np.searchsorted(A["tr"], t0[ix], side="right") - 1, 0, len(A["tr"]) - 1)]
        s = B[B.activo == a].sort_values("t")
        if len(s) > 1000:
            t = s.t.values; m = s.mid.values.astype(float); bq = s.bid_qty.values.astype(float); aq = s.ask_qty.values.astype(float)
            j = np.clip(np.searchsorted(t, t0[ix], side="right") - 1, 0, len(t) - 1)
            P.loc[ix, "imb"] = (bq[j] - aq[j]) / np.maximum(bq[j] + aq[j], 1e-12)
            ts_ = P.ts.values[ix]; S0 = m[j]
            for h, nm in ((5, "fwd5_bn"), (30, "fwd30_bn")):
                jj = np.clip(np.searchsorted(t, ts_ + h, side="right") - 1, 0, len(t) - 1); P.loc[ix, nm] = (m[jj] - S0) / S0 * 1e4
    for a in ("BTC", "ETH", "SOL"):
        dd, zz = zc(a, t0, cie, op, Tt); P["z_" + a] = zz
    P["basis"] = P.d_cl - P.d_bps
    cols = ["ts", "li", "p", "acc", "esW", "act", "mkt", "cierre", "lado", "T", "pmax_prev", "d_bps", "z", "mov10", "mov30", "d_cl", "z_cl", "mov10_cl", "mov30_cl", "lag_cl", "basis", "imb", "z_BTC", "z_ETH", "z_SOL", "fwd5_cl", "fwd30_cl", "fwd5_bn", "fwd30_bn"]
    P[cols].to_csv(out, index=False, compression="gzip"); print(d, len(P), P.z_cl.notna().mean(), flush=True)
