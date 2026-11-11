#!/usr/bin/env python3
"""prep_fills_v3.py TAG DIA [DIA...] -- como prep_fills_v2.py (no se edita) sobre out_v3/RT_<TAG>_<D>.pkl (TAG = <stamp><eng>, p.ej. v3dd). TODAS las variantes del RT se guardan en g0_all_<TAG>_<D>.pkl (CXB, GEO6...),
y G0 + segmentos en g0_fills_/g0_segs_ (misma estructura que v2). Idempotente. 0 ordenes."""
import sys, os, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OV = H + 'out_v3/'
SA2 = '/root/polymarket-research-datalogs/sa_ms2/'
tag = sys.argv[1]
for d in sys.argv[2:]:
    of = OV + f'g0_fills_{tag}_{d}.pkl'
    if os.path.exists(of): print('ya', tag, d); continue
    R = pd.read_pickle(OV + f'RT_{tag}_{d}.pkl'); s = pd.read_pickle(OV + f'SEGT_{tag}_{d}.pkl').copy(); r = R[R['var'] == 'G0'].copy()
    toks = list(np.load(SA2 + f'ms2_{d}.npz', allow_pickle=True)['tokens'])
    for x in (r, s, R): x['token'] = [toks[k] for k in x.k.values]; x['dia'] = d
    s.to_pickle(OV + f'g0_segs_{tag}_{d}.pkl'); R[~R['var'].str.startswith('P')].to_pickle(OV + f'g0_all_{tag}_{d}.pkl'); r.to_pickle(of + '.tmp'); os.replace(of + '.tmp', of)
    print('ok', tag, d, 'fills G0', len(r), 'segs', len(s), 'pnl', round(float(r.pnl.sum()), 2))
