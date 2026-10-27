#!/usr/bin/env python3
"""a1_post_lags.py -- POST HOC (no preregistrado, declarado en INFORME): F5/F2 a varias antelaciones (perfil de latencia).
Misma lectura que a1_rasgos.py. Salida DL/mitigar_as_25oct/l_D.pkl."""
import os, numpy as np, pandas as pd, importlib.util
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'; E1 = '/root/polymarket-research-datalogs/e1_cancelacion_ms/'
SH = np.int64(1) << np.int64(41); LAGS = [100, 150, 200, 250, 400, 700, 1000, 2000, 5000]
tk = pd.read_csv(DL + 'tokens.csv', header=None, names=['tok', 'id', 'coin', 'mid', 'fin', 'lado'], dtype={'tok': str, 'mid': str})
TID = {(m, l): i for m, l, i in zip(tk.mid, tk.lado, tk.id)}
def leeq(D, keep):
    out = []
    for ch in pd.read_csv(DL + f'q_{D}.gz', header=None, names=['id', 'r', 'b', 'a', 'tb', 'ta'], chunksize=2_000_000,
                          dtype={'id': np.int64, 'r': np.int64, 'b': np.float32, 'a': np.float32, 'tb': np.float32, 'ta': np.float32}, on_bad_lines='skip'):
        out.append(ch[ch.id.isin(keep)].dropna())
    return pd.concat(out, ignore_index=True)
dias = [f'2026-10-{d:02d}' for d in range(6, 24)]
for j, D in enumerate(dias):
    out = DL + f'l_{D}.pkl'
    if os.path.exists(out): continue
    F = pd.read_pickle(DL + f'r_{D}.pkl'); keep = set(F.tid.unique().tolist())
    Q = leeq(D, keep)
    if j > 0:
        P = leeq(dias[j-1], keep); t0 = pd.Timestamp(D).timestamp() * 1000 - 120000; Q = pd.concat([P[P.r >= t0], Q]); del P
    K = Q.id.values * SH + Q.r.values; o = np.lexsort((Q.ta.values, Q.tb.values, Q.a.values, Q.b.values, K)); K = K[o]
    R = Q.r.values[o]; B = Q.b.values[o]; A = Q.a.values[o]; TB = Q.tb.values[o]; TA = Q.ta.values[o]; del Q
    ids = F.tid.values.astype(np.int64); res = {}
    for L in LAGS:
        t = F.r.values - L; k = ids * SH + t; i = np.searchsorted(K, k, 'right') - 1; ok = i >= 0; i = np.maximum(i, 0)
        ok &= ((K[i] // SH) == ids) & ((t - R[i]) <= 30000) & (B[i] < A[i])
        res[f'F5_{L}'] = np.where(ok, np.log1p(TA[i]), np.nan); res[f'F2_{L}'] = np.where(ok, TB[i] / np.maximum(TB[i] + TA[i], 1e-9), np.nan)
        res[f'mid_{L}'] = np.where(ok, (B[i] + A[i]) / 2, np.nan); res[f'ask_{L}'] = np.where(ok, A[i], np.nan)
    G = pd.DataFrame(res, index=F.index); G['dia'] = F.dia.values; G.to_pickle(out); print(D, len(G), flush=True)
