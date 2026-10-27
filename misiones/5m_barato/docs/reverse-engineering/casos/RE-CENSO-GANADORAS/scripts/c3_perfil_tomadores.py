#!/usr/bin/env python3
"""c3 (descriptivo, POST-HOC sobre candidatas BH del proxy c0): perfil de las ordenes TOMADORAS de las candidatas (f6 T_D.parquet 05-23 Oct, 5m todas las monedas). Solo lectura."""
import glob, json, numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs'
DES = {}
for f in (DL + '/maker_ms_desenlaces_cache.json', DL + '/mapa_escala/des.json', DL + '/desenlaces_por_market_id_cache.json'):
    for k, v in json.load(open(f)).items():
        if v in ('YES', 'NO'): DES.setdefault(str(k), v)
c = pd.read_csv('c0_candidatas.csv', index_col=0)
W = set(c[c.tipo.isin(['tomador', 'hibrido'])].sort_values('net_total', ascending=False).head(12).index)
X = []
for f in sorted(glob.glob('/mnt/HC_Volume_106538179/agentes_datos/f6/T_2026-10-*.parquet')):
    t = pd.read_parquet(f, columns=['ts', 'act', 'mkt', 'cierre', 'lado', 'buy', 'acc', 'usd', 'p', 'fee', 'w'])
    t['w'] = t.w.astype(str); t = t[t.w.isin(W)]
    if len(t): X.append(t.assign(dia=f[-18:-8]))
X = pd.concat(X); X['T'] = X.cierre - X.ts
X['des'] = X.mkt.astype(str).map(DES); print('cobertura', X.des.notna().mean())
X = X[X.des.notna()]; g = (X.des == X.lado.astype(str)).astype(float)
X['pnl'] = np.where(X.buy, X.acc * g - X.usd, X.usd - X.acc * g) - X.fee
X['pb'] = pd.cut(X.p, [0, .05, .1, .2, .3, .5, .7, .9, .95, .99, 1.0]); X['tb'] = pd.cut(X['T'], [-1e9, 0, 5, 10, 30, 60, 150, 300, 1e9])
for w, q in X.groupby('w'):
    print('\n==', w, 'ordenes', len(q), 'usd %.0f pnl %.0f fee %.0f EV/€ %+.3f compra %.2f usd/orden %.1f dias %d' % (q.usd.sum(), q.pnl.sum(), q.fee.sum(), q.pnl.sum() / q.usd.sum(), q.buy.mean(), q.usd.mean(), q.dia.nunique()))
    for col in ('pb', 'tb', 'act'):
        s = q.groupby(col, observed=True).agg(usd=('usd', 'sum'), pnl=('pnl', 'sum'), n=('usd', 'size'))
        s = s[s.usd > 0.02 * q.usd.sum()]; s['ev'] = s.pnl / s.usd
        print('  ', col, '; '.join('%s: %.0f%% usd ev %+.3f n %d' % (i, 100 * r.usd / q.usd.sum(), r.ev, r.n) for i, r in s.iterrows()))
