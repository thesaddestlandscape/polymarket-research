#!/usr/bin/env python3
"""s3_feats.py -- PREREG_W2 (sha 7b3c5e4c…). Indicadores causales (iguales a W1) para fills maker (rol M) BTC 5m 17-21 Oct.
Entradas: w2_btc/binance_btc.npz (s1), w2_btc/fills_btc_all.csv.gz (s2), sa_ms/btc_ms_D.npz. Salida w2_btc/feats_btc_M.csv.gz.
Pesado: >=09:00Z, nice/ionice, ulimit -v 3000000."""
import os, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); OUT = '/root/polymarket-research-datalogs/w2_btc'; BIG = 1 << 40
assert hashlib.sha256(open(os.path.join(AQ, '..', 'PREREG_W2.md'), 'rb').read()).hexdigest().startswith('7b3c5e4c')
B = np.load(os.path.join(OUT, 'binance_btc.npz')); RV = B['recv']; PX = B['px']; STALE = 120_000
def bn(t):
    j = np.searchsorted(RV, t, 'right') - 1; jc = np.clip(j, 0, None)
    ok = (j >= 0) & (t - RV[jc] <= STALE) & (t >= RV[0]) & (t <= RV[-1]); return np.where(ok, PX[jc], np.nan)
F = pd.read_csv(os.path.join(OUT, 'fills_btc_all.csv.gz'), dtype={'wallet': str}, usecols=['dia', 'ts', 'wallet', 'rol', 'mid', 'fin', 'lado_ef', 'px_ef', 'acc', 'des', 'T'])
F = F[(F.rol == 'M') & F.des.notna() & (F.px_ef >= 0.1) & (F.px_ef <= 0.9) & (F.acc > 0)].reset_index(drop=True)
print('fills M', len(F), 'wallets', F.wallet.nunique(), flush=True)
parts = {d: g for d, g in F.groupby('dia')}; del F; import gc; gc.collect(); DONE = []
def base(F):
    sg = np.where(F.lado_ef.values == 'YES', 1.0, -1.0); t0 = (F.ts.values * 1000).round().astype(np.int64) - 5000; fin = F.fin.values.astype(np.int64)
    P0 = bn(t0); op = (fin - 300) * 1000
    for nm, bk in (('r60', 60_000), ('r300', 300_000), ('r900', 900_000)): F[nm] = (P0 / bn(t0 - bk) - 1) * 1e4 * sg
    Po = bn(op); F['rop'] = (P0 / Po - 1) * 1e4 * sg; F['rpre'] = (Po / bn(op - 900_000) - 1) * 1e4 * sg
    for c in ['b15', 'mid5_t0', 'mid5_f', 'f60']: F[c] = np.nan
    return sg
for d in sorted(parts):
    F = parts.pop(d).reset_index(drop=True); sg = base(F); ix = F.index
    z = np.load(f'/root/polymarket-research-datalogs/sa_ms/btc_ms_{d}.npz'); D0 = int(z['t0']); tm = z['tmap']
    idx = {(str(m), int(pd.Timestamp(str(f)).timestamp()), str(l)): i for i, (a, m, mid, f, l) in enumerate(tm)}
    idm = {(str(m), str(mid), str(l)): i for i, (a, m, mid, f, l) in enumerate(tm)}
    key = z['q_k'].astype(np.int64) * BIG + z['q_t']
    o = np.argsort(key, kind='stable'); key = key[o]
    v0 = z['q_v0'][o]; v1 = z['q_v1'][o]; del o
    def top_mid(k, t):
        okk = k >= 0; kk = np.where(okk, k, 0); j = np.searchsorted(key, kk * BIG + t, 'right') - 1; jc = np.clip(j, 0, None)
        ok = okk & (j >= 0) & ((key[jc] // BIG) == kk); a = v0[jc]; b = v1[jc]
        good = ok & (a > 0) & (b > 0) & (b < 1.0001) & (a <= b + 1e-9); return np.where(good, (a + b) / 2, np.nan)
    tk = z['t_k'].astype(np.int64); tkey = tk * BIG + z['t_t']; o2 = np.argsort(tkey, kind='stable'); tkey = tkey[o2]
    sgt = np.where(np.char.startswith(tm[:, 4].astype(str), 'YES'), 1.0, -1.0); tkk = tk[o2]
    cs = np.concatenate([[0.0], np.cumsum(sgt[tkk] * (z['t_sd'][o2] * 2 - 1) * z['t_sz'][o2].astype(np.float64))]); del tk, o2
    G = F.loc[ix]; tr = (G.ts.values * 1000).round().astype(np.int64) - D0
    k15 = np.array([idx.get(('15min', int(((f + 899) // 900) * 900), l), -1) for f, l in zip(G.fin.values, G.lado_ef.values)])
    k5 = np.array([idx.get(('5min', int(f), l), -1) for f, l in zip(G.fin.values, G.lado_ef.values)])
    F.loc[ix, 'b15'] = top_mid(k15, tr - 5000) - 0.5; F.loc[ix, 'mid5_t0'] = top_mid(k5, tr - 5000); F.loc[ix, 'mid5_f'] = top_mid(k5, tr - 2500)
    kY = np.array([idx.get(('5min', int(f), 'YES'), -1) for f in G.fin.values]); kN = np.array([idx.get(('5min', int(f), 'NO'), -1) for f in G.fin.values])
    tot = np.zeros(len(G)); ok = (kY >= 0) & (kN >= 0)
    for kk in (kY, kN):
        k2 = np.where(kk >= 0, kk, 0); a = np.searchsorted(tkey, k2 * BIG + tr - 5000, 'right'); b = np.searchsorted(tkey, k2 * BIG + tr - 65000, 'right'); tot += np.where(kk >= 0, cs[a] - cs[b], 0.0)
    F.loc[ix, 'f60'] = np.where(ok, tot * sg[ix], np.nan)
    del key, v0, v1, tkey, cs; DONE.append(F); gc.collect(); print(d, len(G), flush=True)
F = pd.concat(DONE, ignore_index=True); F.to_csv(os.path.join(OUT, 'feats_btc_M.csv.gz'), index=False, compression='gzip')
print(F[['r60', 'r300', 'r900', 'rop', 'rpre', 'b15', 'mid5_t0', 'f60']].notna().mean().round(3).to_dict())
print(F.groupby('dia')[['r300', 'rpre', 'b15']].agg(lambda x: x.notna().mean()).round(3))
