#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EXPLORATORIO post-hoc (NO prerregistrado, configuracion unica fijada aqui antes de ver resultados): comprobacion NO LINEAL de M5.
Regresion por gradiente (HistGradientBoostingRegressor) de (y - m130) sobre los rasgos de M5; eps^ = prediccion; q^ = clip(m130 + eps^).
Estima directamente E[y|x] - m = eps. Mismos IS/OOS y misma metrica que analysis3.py."""
import sys, time, numpy as np
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct')
import analysis3 as A
from sklearn.ensemble import HistGradientBoostingRegressor
X, names = A.design(130, A.ALL)
t = (A.y - A.m).astype(np.float64)
def mk(): return HistGradientBoostingRegressor(loss='squared_error', learning_rate=0.03, max_iter=150, max_depth=3, min_samples_leaf=500,
                                                  l2_regularization=10.0, early_stopping=False, random_state=2811)
def toz(eps): q = np.clip(A.m[:len(eps)] if False else eps, -1, 1); return q
z = np.full(len(A.y), np.nan); t0 = time.time()
def put(te, e):
    q = np.clip(A.m[te] + e, 0.001, 0.999); z[te] = np.log(q / (1 - q))
for f in range(6):
    te = A.isr & (A.grp == f); tr = A.isr & (A.grp != f)
    if te.sum() == 0: continue
    g = mk().fit(X[tr], t[tr]); put(te, g.predict(X[te]))
g = mk().fit(X[A.isr], t[A.isr]); put(A.oos, g.predict(X[A.oos]))
print('GBM no lineal: 7 ajustes en %.0f s' % (time.time() - t0))
A.report('GBM M5 IS-CV', z, A.isr)
A.report('GBM M5 OOS', z, A.oos)
for s in (0.5,):
    zs = np.full(len(A.y), np.nan); e = (1 / (1 + np.exp(-z)) - A.m)
    for msk in (A.isr, A.oos):
        q = np.clip(A.m[msk] + s * e[msk], 0.001, 0.999); zs[msk] = np.log(q / (1 - q))
    A.report('GBM M5 x%.1f IS-CV' % s, zs, A.isr); A.report('GBM M5 x%.1f OOS' % s, zs, A.oos)
