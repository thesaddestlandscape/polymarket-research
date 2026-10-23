#!/usr/bin/env python3
"""an3.py -- placebo B real (descriptivo) para rpre/r900/r300 + sensibilidad t0. Salida ../datos/an3.txt"""
import os, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); DAT = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'PREREG.md'), 'rb').read()).hexdigest().startswith('303c2090')
rng = np.random.default_rng(7); out = []
def P(*a): out.append(' '.join(str(x) for x in a)); print(out[-1])
B = pd.read_csv(os.path.join(DAT, 'feats_b.csv.gz')); B = B[B.gana.notna()].copy()
B['strat'] = pd.factorize(B.dia + B.coin + B.outcome + (B.precio / 0.05).round().astype(int).astype(str))[0]
B = B.sort_values('strat').reset_index(drop=True); codes = B.strat.values
P(f'B: n {len(B)}, estratos {B.strat.nunique()} (media {len(B)/B.strat.nunique():.1f} por estrato)')
for c in ['rpre', 'r900', 'r300']:
    a = B[c].fillna(0).values > 0; b = B[c].fillna(0).values < 0
    st = lambda p, k: p[a].sum() / k[a].sum() - p[b].sum() / k[b].sum()
    obs = st(B.pnl.values, B.coste.values); v = []
    for _ in range(2000):
        i = np.lexsort((rng.random(len(B)), codes)); v.append(st(B.pnl.values[i], B.coste.values[i]))
    v = np.array(v); P(f'{c}: Delta B {obs:+.3f} (nCON {a.sum()}, nCONTRA {b.sum()}); placebo media {v.mean():+.3f} sd {v.std():.3f}; p (<=obs) {(v <= obs).mean():.3f}; p (>=obs) {(v >= obs).mean():.3f}')
open(os.path.join(DAT, 'an3.txt'), 'w').write('\n'.join(out) + '\n')
