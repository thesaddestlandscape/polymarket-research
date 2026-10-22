#!/usr/bin/env python3
"""r2_fwd_attach.py DIA -- une a datalogs/sa_r1/units_DIA.csv.gz los rasgos de libro WS: bid 15m del mismo lado/coin (b15), lvl15 = b15 - pc (pc = precio del relleno de la unidad),
vol30ws (acciones por WS en los 30 s previos a ts-4 s) y spread/tamano top del token 5m. Lee datalogs/sa_ms/ms_DIA.npz (ms_extract.py). Escribe units2_DIA.csv.gz. Solo medicion."""
import sys, os, numpy as np, pandas as pd
LAG = 4.0; DL = '/root/polymarket-research-datalogs/'
def main(d):
    TG = os.environ.get('SA_TAG', ''); P1 = DL + 'sa_r1/' + (TG + '/' if TG else ''); U = pd.read_csv(P1 + f'units_{d}.csv.gz'); z = np.load(DL + 'sa_ms/' + (TG + '_' if TG else '') + f'ms_{d}.npz', allow_pickle=True)
    toks = z['tokens']; meta = pd.DataFrame(z['tmap'], columns=['act', 'marco', 'mid', 'fin', 'lado']); meta['finE'] = pd.to_datetime(meta.fin, utc=True).map(lambda x: int(x.timestamp())); meta['mid'] = meta.mid.astype(np.int64)
    t0 = int(z['t0']); qk = z['q_k']; qt = z['q_t'] + t0; qv = [z['q_v%d' % j] for j in range(4)]; bounds = np.searchsorted(qk, np.arange(len(toks) + 1))
    t5 = {(r.mid, r.lado): i for i, r in enumerate(meta.itertuples()) if r.marco == '5min'}; t15 = {(r.act, r.finE, r.lado): i for i, r in enumerate(meta.itertuples()) if r.marco == '15min'}
    def at(i, t):
        a, b = bounds[i], bounds[i + 1]; j = np.searchsorted(qt[a:b], t, side='right') - 1
        return a + j if j >= 0 else -1
    n = len(U); c = {k: np.full(n, np.nan) for k in ['bb', 'ba', 'bs', 'b15', 'a15']}; tobs = U.ts.values - LAG
    for r in range(n):
        tm = tobs[r] * 1000; i5 = t5.get((int(U.mkt.iat[r]), U.lado_c.iat[r]))
        if i5 is not None:
            j = at(i5, tm)
            if j >= 0: c['bb'][r], c['ba'][r], c['bs'][r] = qv[0][j], qv[1][j], qv[2][j]
        i15 = t15.get((U.act.iat[r], int(np.ceil(U.fin.iat[r] / 900.0) * 900), U.lado_c.iat[r]))
        if i15 is not None:
            j = at(i15, tm)
            if j >= 0: c['b15'][r], c['a15'][r] = qv[0][j], qv[1][j]
    for k, v in c.items(): U[k] = v
    mk5 = {i: r.mid for i, r in enumerate(meta.itertuples()) if r.marco == '5min'}; tk = z['t_k']; tt = z['t_t'] + t0; sz = z['t_sz']
    mkt = np.array([mk5.get(k, -1) for k in tk]); o = np.lexsort((tt, mkt)); key = mkt[o].astype(np.float64) * 1e13 + tt[o]; cs = np.concatenate([[0], np.cumsum(sz[o])])
    kq = U.mkt.values.astype(np.float64) * 1e13; U['vol30ws'] = cs[np.searchsorted(key, kq + tobs * 1000, side='right')] - cs[np.searchsorted(key, kq + (tobs - 30) * 1000, side='right')]
    U['lvl15'] = U.b15 - U.pc; U['spread'] = U.ba - U.bb; U['A'] = U.lvl15 <= 0.03; U['R1ws'] = (U.vol30ws >= 26) & (U.hora >= 4)
    U.to_csv(P1 + f'units2_{d}.csv.gz', index=False)
    print(d, 'unidades', n, 'con bid15 %.3f' % U.b15.notna().mean(), 'A %.3f' % U.A.mean(), 'EV todas %.4f' % (U.p.sum() / U.c.sum()), 'EV A %.4f' % (U.p[U.A].sum() / U.c[U.A].sum()))
if __name__ == '__main__':
    for d in sys.argv[1:]: main(d)
