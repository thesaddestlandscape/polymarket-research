#!/usr/bin/env python3
"""a1_post_sub.py -- POST HOC: F5_100 por subconjunto de nivel (relleno AL mejor bid vs POR DEBAJO, tipo B) y por dia de test."""
import glob, numpy as np, pandas as pd
from scipy import stats
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'
X = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(DL + 'r_2026-10-*.pkl'))], ignore_index=True)
dias = sorted(X.dia.unique()); test = [d for d in dias if d >= '2026-10-09']
def terc(v, c): return np.where(v <= c[0], 0, np.where(v <= c[1], 1, 2))
for nom, sub in [('al_mejor_bid', lambda t: (t.q - t.bid).abs() < 0.005), ('por_debajo_bid(B-like)', lambda t: (t.q < t.bid - 0.005))]:
    E = []; R = []
    for d in test:
        tr = X[(X.dia < d) & np.isfinite(X.F5)]; te = X[X.dia == d]; te = te[sub(te)]
        c = np.quantile(tr.F5.values, [1/3, 2/3]); tt = terc(tr.F5.values, c); ev = [tr.pnl.values[tt == k].sum() / tr.coste.values[tt == k].sum() for k in range(3)]; sel = int(np.argmin(ev))
        m = np.isfinite(te.F5.values) & (terc(np.nan_to_num(te.F5.values, nan=-9e18), c) == sel)
        E.append(te.coste.values[m].sum() / te.coste.sum() * te.pnl.sum() - te.pnl.values[m].sum()); R.append((te.pnl.values[m].sum(), te.coste.values[m].sum(), te.pnl.values[~m].sum(), te.coste.values[~m].sum()))
    e = np.array(E); n = len(e); h = stats.t.ppf(0.95, n - 1) * e.std(ddof=1) / np.sqrt(n); R = np.array(R).sum(0)
    print(nom, 'exc', round(e.sum()), 'IC90d', [round(e.mean() - h, 1), round(e.mean() + h, 1)], 'd+', int((e > 0).sum()), 'EV marcados', round(R[0] / R[1], 4), 'EV retenidos', round(R[2] / R[3], 4), 'coste test', round(R[1] + R[3]))
T = X[X.dia >= '2026-10-09']; print('coste diario medio población test', round(T.coste.sum() / len(test)), 'EV total test', round(T.pnl.sum() / T.coste.sum(), 4))
