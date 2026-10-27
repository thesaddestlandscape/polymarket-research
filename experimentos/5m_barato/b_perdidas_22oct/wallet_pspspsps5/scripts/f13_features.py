#!/usr/bin/env python3
"""f13: rasgos ex ante (Binance bookTicker, marca de RECEPCION) para cada relleno pasivo <0.10 de la poblacion (f7), incl. W.
d_bps = (mid_t - ref)/ref*1e4 con ref = media del mid en [cierre-300-62, cierre-300-3] (aprox. del TWAP60 de apertura; NO es el oficial),
z = ln(S/ref)/(sigma_s*sqrt(T)), sigma_s = std de retornos a 1 s del dia por moneda. mov10/mov30 = bps del mid en los 10/30 s previos al fill.
Salida feat_D.csv.gz (solo columnas necesarias)."""
import sys
import numpy as np, pandas as pd
from pathlib import Path
O = Path("/root/polymarket-research-datalogs/wallet_pspspsps5"); BT = Path("/root/polymarket-research-datalogs")
def bt(d):
    f = BT / f"binance_bookticker_{d}.csv"
    if not f.exists(): return None
    x = pd.read_csv(f, usecols=["ts_recepcion_ms", "activo", "mid"]); x = x.dropna(); x = x[x.mid > 0]; x["t"] = x.ts_recepcion_ms / 1000.0
    return x
for d in sys.argv[1:]:
    out = O / f"feat_{d}.csv.gz"
    if out.exists(): continue
    P = pd.read_csv(O / f"poblacion_{d}.csv.gz", dtype={"mkt": str})
    dprev = (pd.Timestamp(d) - pd.Timedelta(days=1)).strftime("%Y-%m-%d"); dnext = (pd.Timestamp(d) + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    B = pd.concat([x for x in (bt(dprev), bt(d), bt(dnext)) if x is not None], ignore_index=True)
    res = []
    for a, g in P.groupby("act"):
        s = B[B.activo == a].sort_values("t"); t = s.t.values; m = s.mid.values.astype(float)
        if len(t) < 1000 or not np.isfinite(t).all(): continue
        grid = np.arange(np.ceil(t[0]), t[-1], 1.0); mg = m[np.clip(np.searchsorted(t, grid, side="right") - 1, 0, len(m) - 1)]
        sg = np.diff(np.log(mg)); sg = sg[np.isfinite(sg)]; sig = np.std(sg) if len(sg) else np.nan
        def mid_at(x): return m[np.clip(np.searchsorted(t, x, side="right") - 1, 0, len(m) - 1)]
        def mean_win(a0, a1):
            c = np.concatenate([[0], np.cumsum(m)]); i0 = np.searchsorted(t, a0); i1 = np.searchsorted(t, a1, side="right")
            n = np.maximum(i1 - i0, 1); return (c[i1] - c[i0]) / n, (i1 - i0)
        ts = g.ts.values; ap = g.cierre.values - 300.0
        ref, nref = mean_win(ap - 62, ap - 3); ref = np.where(nref > 0, ref, np.nan)
        S = mid_at(ts - 0.0)                       # fill block-time est. (ya con retraso); se anade rasgo a ts-3 s
        S3 = mid_at(ts - 3.0); S10 = mid_at(ts - 10.0); S30 = mid_at(ts - 30.0); S60 = mid_at(ts - 60.0)
        Tt = np.maximum(g["T"].values, 1.0)
        g = g.assign(d_bps=(S3 - ref) / ref * 1e4, mov10=(S3 - S10) / S10 * 1e4, mov30=(S3 - S30) / S30 * 1e4, mov60=(S3 - S60) / S60 * 1e4,
                     z=np.log(S3 / ref) / (sig * np.sqrt(Tt)), sig_bps_s=sig * 1e4, nref=nref)
        res.append(g)
    R = pd.concat(res, ignore_index=True)
    R.drop(columns=["pasivo_compra"]).to_csv(out, index=False, compression="gzip")
    print(d, len(R), flush=True)
