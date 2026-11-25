#!/usr/bin/env python3
"""RE-Q11 toxicidad (05-Nov, reverse-engineer). EXPLORATORIO, DEV, solo lectura, 0 ordenes. Lee el libro D del motor escalera_B (sin tocarlo)
y calcula para cada relleno G0 (A_all.pkl) y GEO6 (RC5d) bid/ask en t_arr, tf-300, tf+1 s, tf+10 s, tf+60 s (recortado a fin). Uso: python3 -I mk_markouts.py -> out/MK.pkl"""
import sys, os, json, gc, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; BC = H + '../barrido_corr/out/'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
PB = P2 + 'precursores_barrido/out/'
A = pd.read_pickle(BC + 'A_all.pkl')[['dia', 'k', 'L', 'tf', 'q', 't_dec', 'fin']].assign(src='G0')
R = pd.concat([pd.read_pickle(BC + f'RC5d_{d}.pkl') for d in sorted(A.dia.unique())])
R = R[R['var'] == 'GEO6'][['dia', 'k', 'L', 'tf', 'q', 'fin']].assign(src='GEO6', t_dec=np.nan)
X = pd.concat([A, R], ignore_index=True)
out = []
for d, g in X.groupby('dia'):
    tape = pd.read_pickle(PB + f'tape_{d}.pkl'); bad = {tuple(x) for x in json.load(open(PB + f'bad_{d}.json'))['bad']}
    E = G.DayEng(d, 'chain', tape, bad); D = E.D; del tape; gc.collect()
    def q4(k, t):
        a, b = D.qb[k], D.qb[k + 1]
        if b <= a: return [np.full(len(t), np.nan)] * 4
        j = np.searchsorted(D.qt[a:b], t, side='right') - 1; ok = j >= 0; jj = a + np.where(ok, j, 0)
        return [np.where(ok, v[jj], np.nan).astype(float) for v in (D.v0, D.v1, D.v2, D.v3)]
    for k, ix in g.groupby('k').indices.items():
        sub = g.iloc[ix]; tf = sub.tf.values.astype(np.int64); fin = int(sub.fin.values[0]) * 1000
        rec = {'idx': sub.index.values}
        for nm, tt in (('m300', tf - 300), ('p1', np.minimum(tf + 1000, fin)), ('p10', np.minimum(tf + 10000, fin)), ('p60', np.minimum(tf + 60000, fin)),
                       ('arr', np.where(np.isfinite(sub.t_dec.values), np.nan_to_num(sub.t_dec.values).astype(np.int64) + G.LAT_POST, tf - 300))):
            b, a_, bs, as_ = q4(int(k), tt); rec[nm + '_bid'] = b; rec[nm + '_ask'] = a_; rec[nm + '_bsz'] = bs
        out.append(pd.DataFrame(rec))
    print('ok', d, len(g), flush=True); del E, D; gc.collect()
M = pd.concat(out).set_index('idx').sort_index(); X = X.join(M)
X.to_pickle(H + 'out/MK.pkl'); print('FIN', X.shape)
