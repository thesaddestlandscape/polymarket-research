#!/usr/bin/env python3
"""h23_pareado_v2.py -- lectura pareada del replay v2 (solo lee v2_*_D.csv). Celda central (cola base, alta 79, cancel 60, stake 2 EUR).
Diferencial por dia (rep - r1500) con IC90 por DIAS (bootstrap de dias, 3000, semilla 7), sin 2 mejores dias, rellenos 'recuperados' (solo con re-puja corta),
tasa de rellenos/dia con IC Poisson 90 % y dias hasta n=40. Uso: python3 -I h23_pareado_v2.py [COIN=BTC]"""
import glob, sys
import numpy as np, pandas as pd
from scipy.stats import chi2
O = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/'
coin = sys.argv[1] if len(sys.argv) > 1 else 'BTC'
M = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + f'v2_{coin}_20*.csv'))], ignore_index=True)
M['g'] = M.gana.map({True: 1.0, False: 0.0, 'True': 1.0, 'False': 0.0}); M['pnl'] = M.lleno * M.g - M.coste + M.rebate
C = M[(M.cola == 'base') & (M.lat_post == 79) & (M.lat_cancel == 60) & (M.mult == 1.0) & (M.lleno > 0)]
dias = sorted(M.dia.unique()); nd = len(dias); rng = np.random.default_rng(7)
def serie(b, v): return C[(C.brazo == b) & (C['var'] == v)].groupby('dia').pnl.sum().reindex(dias).fillna(0.0)
def poisson_ci(n, T, a=0.10):
    lo = chi2.ppf(a / 2, 2 * n) / 2 if n > 0 else 0.0; hi = chi2.ppf(1 - a / 2, 2 * n + 2) / 2
    return lo / T, hi / T
print(f'{coin}: {nd} dias {dias[0]}..{dias[-1]} (descubrimiento, ya vistos por H23 v1)')
for b in ('A', 'B'):
    for rep in ('r0', 'r50', 'r150', 'r500'):
        d = (serie(b, rep) - serie(b, 'r1500')).values
        bs = [d[rng.integers(0, nd, nd)].sum() for _ in range(3000)]
        d2 = np.sort(d)[:-2].sum()
        a = C[(C.brazo == b) & (C['var'] == rep)].set_index('cierre'); z = C[(C.brazo == b) & (C['var'] == 'r1500')].set_index('cierre')
        ex = a.loc[a.index.difference(z.index)]; co = a.loc[a.index.intersection(z.index)]
        print(f'{b} {rep:5s} vs r1500: dPnL total={d.sum():+.2f} EUR (dias+ {int((d>0).sum())}/{nd}, dias- {int((d<0).sum())}) IC90 dias de la suma=({np.percentile(bs,5):+.1f},{np.percentile(bs,95):+.1f}) '
              f'sin 2 mejores dias={d2:+.2f} | rellenos recuperados n={len(ex)} (dias {ex.dia.nunique()}) PnL={ex.pnl.sum():+.2f} coste={ex.coste.sum():.2f} EVpond={ex.pnl.sum()/max(ex.coste.sum(),1e-9):+.2f} acierto={ex.g.mean() if len(ex) else float("nan"):.2f} | comunes n={len(co)} dPnL en comunes={(co.pnl - z.loc[co.index].pnl).sum():+.2f}')
print('\nTasa de rellenos (celda central) e intervalo Poisson 90 %; dias hasta n=40 (central, IC):')
for b in ('A', 'B'):
    for rep in ('r0', 'r150', 'r1500'):
        n = len(C[(C.brazo == b) & (C['var'] == rep)]); lo, hi = poisson_ci(n, nd); r = n / nd
        print(f'{b} {rep:5s} n={n} -> {r:.2f}/dia (IC90 {lo:.2f}-{hi:.2f}) -> n=40 en {40/r:.0f} dias (IC {40/hi:.0f}-{40/max(lo,1e-9):.0f})')
