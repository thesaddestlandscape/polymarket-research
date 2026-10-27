#!/usr/bin/env python3
"""a1_post_eval.py -- POST HOC descriptivo: perfil de latencia de F5/F2, exceso estratificado por moneda x bucket 0,05 de q y x dia de semana, por moneda."""
import glob, numpy as np, pandas as pd, json
from scipy import stats
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'
X = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(DL + 'r_2026-10-*.pkl'))], ignore_index=True)
L = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(DL + 'l_2026-10-*.pkl'))], ignore_index=True)
X = pd.concat([X, L.drop(columns=[c for c in L.columns if c in X.columns])], axis=1)
X['qb'] = (np.floor((X.q - 1e-9) / 0.05) * 0.05).round(2); X['est'] = X.coin + '_' + X.qb.astype(str)
dias = sorted(X.dia.unique()); test = [d for d in dias if d >= '2026-10-09']
def terc(v, c): return np.where(v <= c[0], 0, np.where(v <= c[1], 1, 2))
def wf(col, strat=None, sub=None, inv=False):
    E = []
    for d in test:
        tr = X[(X.dia < d) & np.isfinite(X[col])]; te = X[X.dia == d]
        if sub is not None: te = te[sub(te)]
        c = np.quantile(tr[col].values, [1/3, 2/3]); tt = terc(tr[col].values, c)
        ev = [tr.pnl.values[tt == k].sum() / tr.coste.values[tt == k].sum() for k in range(3)]; sel = int(np.argmax(ev) if inv else np.argmin(ev))
        v = te[col].values; m = np.isfinite(v) & (terc(np.nan_to_num(v, nan=-9e18), c) == sel)
        if strat is None:
            E.append(te.coste.values[m].sum() / te.coste.sum() * te.pnl.sum() - te.pnl.values[m].sum())
        else:
            g = pd.DataFrame({'s': te[strat].values, 'p': te.pnl.values, 'c': te.coste.values, 'm': m})
            a = g.groupby('s').apply(lambda h: h.c[h.m].sum() / h.c.sum() * h.p.sum() - h.p[h.m].sum(), include_groups=False)
            E.append(a.sum())
    e = np.array(E); n = len(e); h = stats.t.ppf(0.95, n - 1) * e.std(ddof=1) / np.sqrt(n)
    return f"{e.sum():8.0f} IC90d [{e.mean()-h:7.1f},{e.mean()+h:7.1f}] d+ {(e>0).sum():2d}/{n} sin2 {np.sort(e)[:-2].sum():7.0f}"
print('== perfil de latencia (walk-forward igual que prereg; antelación respecto a la RECEPCIÓN del print)')
for lag in [100, 150, 200, 250, 400, 700, 1000, 2000, 5000]:
    print(f'F5 lag {lag:5d}', wf(f'F5_{lag}'), '| F2', wf(f'F2_{lag}'))
print('== F5 lag 100 estratificado por moneda x bucket q 0,05 (placebo dentro del estrato):', wf('F5_100', strat='est'))
print('== F5 lag 250 estratificado:', wf('F5_250', strat='est'))
print('== F5 lag 1000 estratificado:', wf('F5_1000', strat='est'))
for c in ['ETH', 'SOL', 'XRP']:
    print('== moneda', c, 'F5_100', wf('F5_100', sub=lambda t, c=c: t.coin == c), '| F5_250', wf('F5_250', sub=lambda t, c=c: t.coin == c))
# ¿el tamaño del ask cambia en los últimos ms? (mecánica)
d = (X.F5_100 - X.F5_1000); print('== Δlog1p(ta) 1000→100 ms: media', round(float(np.nanmean(d)), 3), 'p10/p50/p90', np.nanpercentile(d, [10, 50, 90]).round(3))
d2 = (X.ask_100 - X.ask_1000).round(3); print('== Δask 1000→100 ms (fracción): baja', round(float((d2 < 0).mean()), 3), 'igual', round(float((d2 == 0).mean()), 3), 'sube', round(float((d2 > 0).mean()), 3))
print('== Δask 250→100 ms: baja', round(float(((X.ask_100 - X.ask_250).round(3) < 0).mean()), 3), 'ask(100)==q(+0..)?', round(float(((X.ask_100 - X.q).round(3) <= 0.01).mean()), 3))
# EV por tercil de F5_100 en todo el periodo (descriptivo)
c = np.nanquantile(X.F5_100, [1/3, 2/3]); t = terc(np.nan_to_num(X.F5_100.values, nan=-9e18), c)
for k in range(3):
    m = (t == k) & np.isfinite(X.F5_100.values); print('tercil', k, 'cortes', c.round(2), 'n', int(m.sum()), 'EV€', round(X.pnl[m].sum() / X.coste[m].sum(), 4), 'hit-q', round(float((X.gana[m] - X.q[m]).mean()), 4), 'acc medio', round(float(X.acc[m].mean()), 1))
