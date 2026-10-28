#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EXPLORATORIO post-hoc (NO prerregistrado): sensibilidad al ridge de M5 (info calibrada alcanzable) con las funciones de analysis3.py."""
import sys, numpy as np
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct')
import analysis3 as A
from scipy.special import expit
for nm, bl in (('M5', A.ALL), ('M1', ['B1'])):
    X, names = A.design(130, bl)
    Xt = X[A.isr]; mu = Xt.mean(0); sd = Xt.std(0); sd[sd < 1e-9] = 1.0; Xt -= mu; Xt /= sd
    Xe = X[A.oos]; Xe -= mu; Xe /= sd
    for lam in (1e-3, 1e-2, 1e-1, 1.0):
        b = A.fit(Xt, A.o[A.isr], A.y[A.isr], lam)
        zz = np.full(len(A.y), np.nan); zz[A.oos] = A.o[A.oos] + (Xe @ b[:-1].astype(np.float32)).astype(np.float64) + b[-1]
        A.report('%s ridge lam=%g OOS' % (nm, lam), zz, A.oos)
    del X, Xt, Xe
