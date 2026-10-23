#!/usr/bin/env python3
"""cal_diag.py -- diagnostico (descriptivo, fuera de los criterios) de los desacuerdos del B_FIEL nominal en EVAL: n de ordenes por puja, tipo de relleno, T, moneda."""
import os
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos')
import numpy as np, pandas as pd
S = pd.read_csv(os.path.join(D, 'cal_sim.csv'), dtype={'mid': str}); R = pd.read_csv(os.path.join(D, 'cal_real_pujas.csv'), dtype={'mid': str})
s = S[(S.lat_can == 280) & (S.alloc == 'prop')]
J = R[R.dia.isin(['2026-10-21', '2026-10-22'])].merge(s, on='mid', suffixes=('', '_s')); J = J[J.lado_sim == J.real_lado].copy()
J['cat'] = np.select([(J.fill == 1) & (J.rf_a == 1), (J.fill == 1) & (J.rf_a == 0), (J.fill == 0) & (J.rf_a == 1)], ['ambos', 'solo_sim', 'solo_real'], 'ninguno')
J['T_sim'] = J.fin - J.r / 1000.0
print(J.groupby('cat').agg(n=('mid', 'size'), n_ord_real=('n_ord', 'mean'), npost_sim=('npost', 'mean'), T_sim=('T_sim', 'median'), acc_sim=('acc', 'mean')).round(2))
print('\nn ordenes por puja: real vs sim (todas las pujas EVAL): real media %.2f mediana %.1f | sim media %.2f mediana %.1f | Spearman %.3f' % (
    J.n_ord.mean(), J.n_ord.median(), J.npost.mean(), J.npost.median(), J[['n_ord', 'npost']].corr(method='spearman').iloc[0, 1]))
print('tipo de relleno sim (ambos / solo_sim):'); print(pd.crosstab(J.cat, J.tipo.fillna('-')).to_string())
print('\nfin_puja real por categoria:'); print(pd.crosstab(J.cat, J.fin_puja.fillna('-')).to_string())
print('\nacuerdo por tramo de n_ord real (1, 2-3, 4+):')
J['tr'] = pd.cut(J.n_ord, [0, 1, 3, 1000], labels=['1', '2-3', '4+'])
print(J.groupby('tr', observed=True).apply(lambda g: pd.Series(dict(n=len(g), acuerdo=(g.fill == g.rf_a).mean(), tasa_sim=g.fill.mean(), tasa_real=g.rf_a.mean()))).round(3).to_string())
