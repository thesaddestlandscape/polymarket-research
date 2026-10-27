#!/usr/bin/env python3
"""v4_desenlaces.py -- cobertura y validez del desenlace (DES de gamma) frente a (a) precierre_desenlaces_cache (por slug, otra tuberia) y (b) precio on-chain de los ultimos 30 s."""
import sys, json, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/verificacion')
import vlib
from vlib import *
PRE = json.load(open('/root/polymarket-research-datalogs/precierre_desenlaces_cache.json'))
tot = dict(mk=0, des=0, pre=0, comp=0, disc=0, ch=0, chcomp=0, chdisc=0); falt = []
for d in ['2026-10-%02d' % x for x in range(9, 22)]:
    X, ok = load_day(d); X = X[ok]
    X['pyes'] = np.where(X.yes, X.pc, 1 - X.pc)
    M = X.groupby('mid').agg(fin=('fin', 'first'), coin=('coin', 'first'), n=('sh', 'size'), vol=('coste_m', 'sum')).reset_index()
    M['des'] = M.mid.astype(str).map(DES)
    M['slug'] = M.coin.str.lower() + '-updown-5m-' + (M.fin - 300).astype(str)
    M['pre'] = M.slug.map(PRE).map({'Up': 'YES', 'Down': 'NO'})
    # on-chain: precio YES medio de fills con ts en [fin-30, fin+3]
    L = X[(X.ts >= X.fin - 30) & (X.ts <= X.fin + 3)].groupby('mid').pyes.agg(['mean', 'size'])
    M = M.merge(L, left_on='mid', right_index=True, how='left')
    M['ch'] = np.where(M['mean'] > .9, 'YES', np.where(M['mean'] < .1, 'NO', None))
    c1 = M.des.notna() & M.pre.notna(); c2 = M.des.notna() & M.ch.notna() & (M['size'] >= 3)
    r = dict(dia=d, mercados=len(M), con_des=int(M.des.notna().sum()), con_pre=int(M.pre.notna().sum()), comp_pre=int(c1.sum()), disc_pre=int((M.des[c1] != M.pre[c1]).sum()),
             comp_chain=int(c2.sum()), disc_chain=int((M.des[c2] != M.ch[c2]).sum()), sin_des=int(M.des.isna().sum()), vol_sin_des=float(M.vol[M.des.isna()].sum() / M.vol.sum()))
    print(r, flush=True)
    for k, v in (('mk', r['mercados']), ('des', r['con_des']), ('pre', r['con_pre']), ('comp', r['comp_pre']), ('disc', r['disc_pre']), ('chcomp', r['comp_chain']), ('chdisc', r['disc_chain'])): tot[k] += v
    falt.append(M[M.des.isna()][['mid', 'coin', 'fin']].assign(dia=d))
print('TOTAL', tot)
F = pd.concat(falt); print('mercados sin desenlace por moneda:', F.coin.value_counts().to_dict(), '| muestra', F.head(5).to_dict('records'))
