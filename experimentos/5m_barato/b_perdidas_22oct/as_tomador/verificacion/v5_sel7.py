#!/usr/bin/env python3
"""v5_sel7.py -- sensibilidad: SEL ampliada a 05-11 Oct (7 dias, el diseno original antes de la 'desviacion declarada'), mismos umbrales; test = UT (12-21) de v2.
POST-HOC (extra, no cuenta para decidir)."""
import sys, json, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/verificacion')
import vlib
from vlib import *
rng = np.random.default_rng(99)
S = pd.read_pickle(V + 'sets_codes.pkl'); vlib._codes.update(S['codes'])
UT = pd.read_pickle(V + 'UT.pkl')
usc = vlib._codes.get(US, -9)
acc = []
for d in ['2026-10-%02d' % x for x in range(5, 12)]:
    try: X, ok = load_day(d)
    except FileNotFoundError: print('falta', d); continue
    X = X[ok]; res = X.gana.values >= 0; cob = res.mean(); X = X[res & (X.mk.values != usc) & (X.tk.values != usc)]
    pm = pnl_m(X); fee = FEE * X.sh.values * X.pc.values * (1 - X.pc.values)
    acc.append(pd.DataFrame({'dia': d, 'tk': X.tk.values, 'pn': -pm - fee, 'c': X.sh.values * (1 - X.pc.values), 'pc': X.pc.values})); print(d, len(X), 'cob', round(float(cob), 4), flush=True)
A = pd.concat(acc)
g = A.groupby('tk').agg(n=('pn', 'size'), pnl=('pn', 'sum'), cost=('c', 'sum')); gd = A.groupby(['tk', 'dia']).agg(n=('pn', 'size'), pnl=('pn', 'sum')).reset_index(); gd = gd[gd.n >= 10]
g['dpos'] = gd[gd.pnl > 0].groupby('tk').size().reindex(g.index).fillna(0); g['dval'] = gd.groupby('tk').size().reindex(g.index).fillna(0); g['roi'] = g.pnl / g.cost
pnl = UT.p.values; c = UT.c.values; tkv = UT.tk.values; cl = pd.factorize(UT.cierre)[0]; ncl = cl.max() + 1
def exc(f): return pnl[~f].sum() / c[~f].sum() - pnl.sum() / c.sum()
def boot(f):
    Pt = np.bincount(cl, pnl, ncl); Ct = np.bincount(cl, c, ncl); Pr = np.bincount(cl, pnl * ~f, ncl); Cr = np.bincount(cl, c * ~f, ncl)
    w = rng.multinomial(ncl, np.ones(ncl) / ncl, size=2000).astype(float); e = (w @ Pr) / (w @ Cr) - (w @ Pt) / (w @ Ct); return [round(float(x), 4) for x in np.percentile(e, [5, 95])]
pool = g[(g.n >= 100) & (g.cost >= 200)].index.values; pool = np.array(sorted(set(pool) & set(np.unique(tkv))))
for nm, ok in (('7d: >=2 dias+ (regla prereg literal)', (g.n >= 100) & (g.cost >= 200) & (g.roi >= .02) & (g.dpos >= 2)),
               ('7d: >=4/7 dias+', (g.n >= 100) & (g.cost >= 200) & (g.roi >= .02) & (g.dpos >= 4)),
               ('7d: sin condicion de dias', (g.n >= 100) & (g.cost >= 200) & (g.roi >= .02))):
    st = set(g[ok].index); f = np.isin(tkv, list(st)); k = len(st & set(np.unique(tkv)))
    ex = np.array([exc(np.isin(tkv, rng.choice(pool, k, replace=False))) for _ in range(2000)]) if k else np.array([0.])
    print(nm, '| takers', len(st), 'en test', k, '| unidades', int(f.sum()), 'frac_eur', round(float(c[f].sum() / c.sum()), 4), '| EXCESO', round(float(exc(f)), 4), 'IC90 cierre', boot(f) if f.any() else None,
          '| EV_IN', round(float(pnl[f].sum() / c[f].sum()), 4) if f.any() else None, '| placebo(pool activo) media', round(float(ex.mean()), 4), 'p95', round(float(np.percentile(ex, 95)), 4), 'p_emp', round(float((1 + (ex >= exc(f)).sum()) / (len(ex) + 1)), 3))
