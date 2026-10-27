#!/usr/bin/env python3
"""E-RE-CG-00 proxy: censo 5m PARES desde quien_gana_agg (solo lectura)."""
import glob, numpy as np, pandas as pd
from math import erf, sqrt
F = sorted(glob.glob('/root/polymarket-research-datalogs/m5barato_mision/quien_gana_agg_2026-10-*.csv'))
D = pd.concat([pd.read_csv(f, usecols=['wallet', 'pnl5_M', 'pnl5_T', 'fee5', 'vol5', 'volT5']).assign(dia=f[-14:-4]) for f in F])
D = D[D.vol5 > 0]; D['net'] = D.pnl5_M + D.pnl5_T
B = '0x659a40ff9920febc5a66836213040924343d297f'; D = D[D.wallet != B]
dias = sorted(D.dia.unique()); print('dias', len(dias), dias[0], dias[-1])
print('por dia: suma net (todas) / fees / makers / tomadores (netos de fee)')
g = D.groupby('dia')[['net', 'fee5', 'pnl5_M', 'pnl5_T', 'vol5']].sum(); print(g.round(0).to_string())
t = D.groupby('wallet').agg(net=('net', 'sum'), M=('pnl5_M', 'sum'), T=('pnl5_T', 'sum'), fee=('fee5', 'sum'), vol=('vol5', 'sum'), volT=('volT5', 'sum'),
                            dias=('dia', 'nunique'), dpos=('net', lambda s: int((s > 0).sum())))
t['tipo'] = np.where(t.volT / t.vol <= 0.2, 'maker', np.where(t.volT / t.vol >= 0.8, 'tomador', 'hibrido'))
G = t[t.net > 0].sort_values('net', ascending=False)
print('\nwallets %d | net>0 %d (%.1f %%) | net>1000$ %d | net>10000$ %d' % (len(t), len(G), 100 * len(G) / len(t), (t.net > 1000).sum(), (t.net > 10000).sum()))
for nd in (5, 10):
    m = t.dias >= nd; print('  >=%d dias: %d; net>0 %d; net>0 y dias+>=70%% %d' % (nd, m.sum(), (m & (t.net > 0)).sum(), (m & (t.net > 0) & (t.dpos >= .7 * t.dias)).sum()))
print('  beneficio ganadoras %.0f | perdidas perdedoras %.0f | neto %.0f | fees %.0f (rebate pool 20%% = %.0f)' % (G.net.sum(), t[t.net < 0].net.sum(), t.net.sum(), t.fee.sum(), .2 * t.fee.sum()))
for k in (1, 10, 100, 1000): print('  top-%d = %.1f %% del beneficio ganador' % (k, 100 * G.net.head(k).sum() / G.net.sum()))
print(t.groupby('tipo').agg(n=('net', 'size'), gan=('net', lambda s: int((s > 0).sum())), net=('net', 'sum'), M=('M', 'sum'), T=('T', 'sum'), fee=('fee', 'sum'), vol=('vol', 'sum')).round(0).to_string())
SEL = [d for d in dias if d <= '2026-10-14']; TEST = [d for d in dias if d >= '2026-10-15']
def z(x):
    g = x.groupby('wallet').net; return pd.DataFrame({'net': g.sum(), 'z': g.mean() / (g.std(ddof=1) / np.sqrt(g.size())), 'nd': g.size(), 'vol': x.groupby('wallet').vol5.sum()})
S = z(D[D.dia.isin(SEL)]); T = z(D[D.dia.isin(TEST)])
ros = S[(S.net > 0) & (S.z >= 2) & (S.nd >= 4)].index
Tm = T.reindex(S.index); v = Tm.loc[ros].net.fillna(0)
dec = pd.qcut(S.vol.rank(method='first'), 10, labels=False); rd = dec.loc[ros].value_counts()
rng = np.random.default_rng(20261026); pn, pp = [], []
for _ in range(1000):
    pick = np.concatenate([rng.choice(dec.index[dec == k], size=c, replace=False) for k, c in rd.items()])
    x = Tm.loc[pick].net.fillna(0); pn.append(x.sum()); pp.append((x > 0).mean())
pn, pp = np.array(pn), np.array(pp)
print('\nQ2 roster SEL n=%d (de %d) | TEST net %.0f frac>0 %.3f activas %.3f | placebo net media %.0f p95 %.0f frac media %.3f p95 %.3f | p_net %.4f p_frac %.4f' % (
    len(ros), len(S), v.sum(), (v > 0).mean(), Tm.loc[ros].net.notna().mean(), pn.mean(), np.percentile(pn, 95), pp.mean(), np.percentile(pp, 95), (pn >= v.sum()).mean(), (pp >= (v > 0).mean()).mean()))
c = T.loc[T.index.intersection(ros)]; c = c[c.nd >= 4].copy()
c['p'] = [1 - 0.5 * (1 + erf(zz / sqrt(2))) if np.isfinite(zz) else 1 for zz in c.z]
c = c.sort_values('p'); m = len(c); k = max([i for i, pv in enumerate(c.p.values, 1) if pv <= .1 * i / m], default=0)
print('  BH q=0,10 en TEST: %d de %d' % (k, m))
top = c.head(k).join(t[['tipo', 'M', 'T', 'fee', 'vol', 'dias', 'dpos', 'net']], rsuffix='_total')
print(top.round(1).head(40).to_string())
# perdedoras persistentes (quien paga)
rl = S[(S.net < 0) & (S.z <= -2) & (S.nd >= 4)].index; vl = Tm.loc[rl].net.fillna(0)
print('\nperdedoras SEL z<=-2: n=%d | TEST net %.0f frac<0 %.3f' % (len(rl), vl.sum(), (vl < 0).mean()))
top.to_csv('/root/polymarket-research/misiones/5m_barato/docs/reverse-engineering/casos/RE-CENSO-GANADORAS/c0_candidatas.csv')
