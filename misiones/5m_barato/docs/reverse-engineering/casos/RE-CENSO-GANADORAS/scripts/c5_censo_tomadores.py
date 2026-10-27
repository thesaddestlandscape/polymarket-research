#!/usr/bin/env python3
"""E-RE-CG-01b: censo completo de TOMADORES 5m (f6 T parquet 05-23 Oct). Solo lectura."""
import glob, json, numpy as np, pandas as pd
from math import erf, sqrt
DL = '/root/polymarket-research-datalogs'
DES = {}
for f in (DL + '/maker_ms_desenlaces_cache.json', DL + '/mapa_escala/des.json', DL + '/desenlaces_por_market_id_cache.json'):
    for k, v in json.load(open(f)).items():
        if v in ('YES', 'NO'): DES.setdefault(str(k), v)
PB = [0, .05, .1, .2, .3, .5, .7, .9, .95, .99, 1.0001]; TB = [-1e9, 0, 10, 30, 60, 150, 300, 1e9]
Dw, Pc, cov = [], [], []
for f in sorted(glob.glob('/mnt/HC_Volume_106538179/agentes_datos/f6/T_2026-10-*.parquet')):
    dia = f[-18:-8]
    t = pd.read_parquet(f, columns=['ts', 'act', 'mkt', 'cierre', 'lado', 'buy', 'acc', 'usd', 'p', 'fee', 'w'])
    t['w'] = t.w.astype(str); des = t.mkt.astype(str).map(DES)
    cov.append((dia, t.usd.sum(), t.usd[des.notna()].sum())); t = t[des.notna()]; des = des[des.notna()]
    g = (des.values == t.lado.astype(str).values).astype(float)
    t['pnl'] = np.where(t.buy, t.acc * g - t.usd, t.usd - t.acc * g) - t.fee
    t['pb'] = np.digitize(t.p, PB) - 1; t['tb'] = np.digitize(t.cierre - t.ts, TB) - 1
    Dw.append(t.groupby('w')[['pnl', 'fee', 'usd']].sum().assign(n=t.groupby('w').size(), dia=dia).reset_index())
    Pc.append(t.groupby(['w', 'pb', 'tb', 'act'])[['pnl', 'fee', 'usd']].sum().reset_index())
cv = pd.DataFrame(cov, columns=['dia', 'usd', 'usd_cob']); print('cobertura desenlace (USD) por dia min %.4f total %.4f' % ((cv.usd_cob / cv.usd).min(), cv.usd_cob.sum() / cv.usd.sum()))
D = pd.concat(Dw); P = pd.concat(Pc).groupby(['w', 'pb', 'tb', 'act'])[['pnl', 'fee', 'usd']].sum().reset_index()
B = '0x659a40ff9920febc5a66836213040924343d297f'; D = D[D.w != B]
t = D.groupby('w').agg(net=('pnl', 'sum'), fee=('fee', 'sum'), usd=('usd', 'sum'), dias=('dia', 'nunique'), dpos=('pnl', lambda s: int((s > 0).sum())))
G = t[t.net > 0].sort_values('net', ascending=False)
print('TOMADORES %d | net>0 %d (%.1f%%) | net>1k$ %d | >10k$ %d | neto total %.0f | fees %.0f | gross (sin fee) %.0f' % (len(t), len(G), 100 * len(G) / len(t), (t.net > 1e3).sum(), (t.net > 1e4).sum(), t.net.sum(), t.fee.sum(), t.net.sum() + t.fee.sum()))
print('  beneficio ganadoras %.0f; top-1 %.1f%% top-10 %.1f%% top-100 %.1f%%' % (G.net.sum(), 100 * G.net.head(1).sum() / G.net.sum(), 100 * G.net.head(10).sum() / G.net.sum(), 100 * G.net.head(100).sum() / G.net.sum()))
dias = sorted(D.dia.unique()); SEL = [d for d in dias if d <= '2026-10-14']; TEST = [d for d in dias if d >= '2026-10-15']
def z(x):
    g = x.groupby('w').pnl; return pd.DataFrame({'net': g.sum(), 'z': g.mean() / (g.std(ddof=1) / np.sqrt(g.size())), 'nd': g.size(), 'usd': x.groupby('w').usd.sum()})
S = z(D[D.dia.isin(SEL)]); T = z(D[D.dia.isin(TEST)])
ros = S[(S.net > 0) & (S.z >= 2) & (S.nd >= 4)].index; Tm = T.reindex(S.index); v = Tm.loc[ros].net.fillna(0)
dec = pd.qcut(S.usd.rank(method='first'), 10, labels=False); rd = dec.loc[ros].value_counts(); rng = np.random.default_rng(20261026); pn, pp = [], []
for _ in range(1000):
    pick = np.concatenate([rng.choice(dec.index[dec == k], size=c, replace=False) for k, c in rd.items()]); x = Tm.loc[pick].net.fillna(0); pn.append(x.sum()); pp.append((x > 0).mean())
pn, pp = np.array(pn), np.array(pp)
print('Q2 roster SEL n=%d de %d | TEST net %.0f frac>0 %.3f | placebo net media %.0f p95 %.0f frac media %.3f p95 %.3f | p_net %.4f p_frac %.4f' % (len(ros), len(S), v.sum(), (v > 0).mean(), pn.mean(), np.percentile(pn, 95), pp.mean(), np.percentile(pp, 95), (pn >= v.sum()).mean(), (pp >= (v > 0).mean()).mean()))
c = T.loc[T.index.intersection(ros)]; c = c[c.nd >= 4].copy(); c['p'] = [1 - .5 * (1 + erf(zz / sqrt(2))) if np.isfinite(zz) else 1 for zz in c.z]
c = c.sort_values('p'); m = len(c); k = max([i for i, pv in enumerate(c.p.values, 1) if pv <= .1 * i / m], default=0); bh = c.head(k).index
print('  BH q=0,10 TEST: %d de %d; net TEST de BH %.0f $ (%d dias TEST) ; net total periodo de BH %.0f $' % (k, m, c.head(k).net.sum(), len(TEST), t.loc[bh].net.sum()))
PBL = ['<.05', '.05-.10', '.10-.20', '.20-.30', '.30-.50', '.50-.70', '.70-.90', '.90-.95', '.95-.99', '>.99']; TBL = ['post', '0-10', '10-30', '30-60', '60-150', '150-300', '>300']
P['grp'] = np.where(P.w.isin(bh), 'BH', 'resto')
q = P.groupby(['grp', 'pb', 'tb'])[['pnl', 'usd']].sum().reset_index()
tot = q.groupby('grp').usd.sum()
print('\nmecanismo: celdas (banda x T) con >=2%% del volumen de cada grupo; EV/€ neto de fee')
for grp in ('BH', 'resto'):
    s = q[q.grp == grp].copy(); s['share'] = s.usd / tot[grp]; s['ev'] = s.pnl / s.usd; s = s[s.share >= .02].sort_values('share', ascending=False)
    print(' ', grp, 'usd %.0f EV %+.4f' % (tot[grp], q[q.grp == grp].pnl.sum() / tot[grp]))
    for _, r in s.iterrows(): print('     %-8s T %-8s %5.1f%% ev %+.4f' % (PBL[int(r.pb)], TBL[int(r.tb)], 100 * r.share, r.ev))
o = t.loc[bh].sort_values('net', ascending=False).head(25); mon = P[P.w.isin(o.index)].groupby(['w', 'act']).usd.sum().unstack(fill_value=0)
o['BTC_frac'] = (mon.get('BTC', 0) / mon.sum(axis=1)).reindex(o.index)
o.to_csv('c5_tomadores_BH.csv'); print('\ntop 25 BH tomadores'); print(o.round(1).to_string())
