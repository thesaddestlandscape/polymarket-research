#!/usr/bin/env python3
"""a1_rasgos.py -- PREREG_A1 (sha en PREREG_A1.sha256). Rasgos L1 dinamicos (<=2 s antes del print, por RECEPCION) para los rellenos
de E1D (e1d_dia_D.pkl) y para un instante de CONTROL por relleno. Salida DL/mitigar_as_25oct/r_D.pkl. Reanudable por dia."""
import os, sys, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.join(AQ, '..')
assert hashlib.sha256(open(os.path.join(BASE, 'PREREG_A1.md'), 'rb').read()).hexdigest() == open(os.path.join(BASE, 'PREREG_A1.sha256')).read().split()[0]
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'; E1 = '/root/polymarket-research-datalogs/e1_cancelacion_ms/'
SH = np.int64(1) << np.int64(41)
tk = pd.read_csv(DL + 'tokens.csv', header=None, names=['tok', 'id', 'coin', 'mid', 'fin', 'lado'], dtype={'tok': str, 'mid': str})
TID = {(m, l): i for m, l, i in zip(tk.mid, tk.lado, tk.id)}
def leeq(D, keep):   # 25-Oct: lectura por trozos filtrando a los tokens con rellenos ese dia (MemoryError con el dia entero)
    out = []
    for ch in pd.read_csv(DL + f'q_{D}.gz', header=None, names=['id', 'r', 'b', 'a', 'tb', 'ta'], chunksize=2_000_000,
                          dtype={'id': np.int64, 'r': np.int64, 'b': np.float32, 'a': np.float32, 'tb': np.float32, 'ta': np.float32}, on_bad_lines='skip'):
        out.append(ch[ch.id.isin(keep)].dropna())
    return pd.concat(out, ignore_index=True)
def estado(K, R, B, A, TB, TA, LC, ids, t):
    k = ids * SH + t; i = np.searchsorted(K, k, 'right') - 1; ok = (i >= 0); i = np.maximum(i, 0)
    ok &= ((K[i] // SH) == ids) & ((t - R[i]) <= 30000)
    return i, ok
dias = [f'2026-10-{d:02d}' for d in range(6, 24)]
for j, D in enumerate(dias):
    out = DL + f'r_{D}.pkl'
    if os.path.exists(out) or not os.path.exists(DL + f'q_{D}.gz'): continue
    F, _ = pd.read_pickle(E1 + f'e1d_dia_{D}.pkl')
    F = F.copy(); F['tid'] = [TID.get((m, l), -1) for m, l in zip(F.mid, F.lado_m)]
    keep = set(F.tid.unique().tolist())
    Q = leeq(D, keep)
    if j > 0 and os.path.exists(DL + f'q_{dias[j-1]}.gz'):
        P = leeq(dias[j-1], keep); t0 = pd.Timestamp(D).timestamp() * 1000 - 120000; Q = pd.concat([P[P.r >= t0], Q]); del P
    K = Q.id.values * SH + Q.r.values; o = np.lexsort((Q.ta.values, Q.tb.values, Q.a.values, Q.b.values, K)); K = K[o]
    R = Q.r.values[o]; B = Q.b.values[o]; A = Q.a.values[o]; TB = Q.tb.values[o]; TA = Q.ta.values[o]; IDs = Q.id.values[o]; del Q
    u = np.ones(len(K), bool); u[1:] = (K[1:] != K[:-1]) | (B[1:] != B[:-1]) | (A[1:] != A[:-1]) | (TB[1:] != TB[:-1]) | (TA[1:] != TA[:-1])   # duplicados exactos (tramos solapados)
    K, R, B, A, TB, TA, IDs = K[u], R[u], B[u], A[u], TB[u], TA[u], IDs[u]
    chg = np.ones(len(K), bool); chg[1:] = (IDs[1:] != IDs[:-1]) | (B[1:] != B[:-1]) | (A[1:] != A[:-1])
    LC = np.maximum.accumulate(np.where(chg, K, 0)) - IDs * SH          # recepcion del ultimo cambio de top en el token
    ids = F.tid.values.astype(np.int64); rng = np.random.default_rng(int(D.replace('-', '')))
    rc = F.r.values - rng.integers(5000, 30001, len(F))
    res = {}
    for tag, base, lag in (('', F.r.values, 100), ('_250', F.r.values, 250), ('_c', rc, 100)):
        tau = base - lag
        i1, ok1 = estado(K, R, B, A, TB, TA, LC, ids, tau); i0, ok0 = estado(K, R, B, A, TB, TA, LC, ids, tau - 2000)
        ok1 &= (ids >= 0) & (B[i1] < A[i1]); ok0 &= ok1
        mid1 = (B[i1] + A[i1]) / 2; mid0 = (B[i0] + A[i0]) / 2
        pos0 = np.searchsorted(K, ids * SH + (tau - 2000), 'right')
        res['F1' + tag] = np.where(ok1, A[i1] - B[i1], np.nan)
        res['F2' + tag] = np.where(ok1, TB[i1] / np.maximum(TB[i1] + TA[i1], 1e-9), np.nan)
        res['F3' + tag] = np.where(ok0, np.log1p(TB[i1]) - np.log1p(TB[i0]), np.nan)
        res['F4' + tag] = np.where(ok0, mid1 - mid0, np.nan)
        res['F5' + tag] = np.where(ok1, np.log1p(TA[i1]), np.nan)
        res['F6' + tag] = np.where(ok1, (i1 + 1 - pos0).astype(float), np.nan)
        res['F7' + tag] = np.where(ok1, (tau - LC[i1]).astype(float), np.nan)
        res['F8' + tag] = F.fin.values - base / 1000.0
        res['bid' + tag] = np.where(ok1, B[i1], np.nan)
    for k, v in res.items(): F[k] = v
    F.to_pickle(out)
    print(D, 'rellenos', len(F), 'sin_token', int((ids < 0).sum()), 'F1 valido', round(float(np.isfinite(F.F1).mean()), 3), 'F3 valido', round(float(np.isfinite(F.F3).mean()), 3), flush=True)
