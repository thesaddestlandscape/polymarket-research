#!/usr/bin/env python3
"""prep_fills_v2.py MODO DIA [DIA...] -- como prep_fills.py (no se edita) pero sobre out_v2/RT_<modo>_<D>.pkl / SEGT_<modo>_<D>.pkl (passT_v2) y tokens de sa_ms2. Solo G0.
Salida: out_v2/g0_fills_<modo>_<D>.pkl, out_v2/g0_segs_<modo>_<D>.pkl. Idempotente (no sobrescribe). Lectura/escritura local, 0 ordenes."""
import sys, os, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OV = H + 'out_v2/'
SA2 = '/root/polymarket-research-datalogs/sa_ms2/'
modo = sys.argv[1]
for d in sys.argv[2:]:
    of = OV + f'g0_fills_{modo}_{d}.pkl'
    if os.path.exists(of): print('ya', modo, d); continue
    r = pd.read_pickle(OV + f'RT_{modo}_{d}.pkl'); r = r[r['var'] == 'G0'].copy(); s = pd.read_pickle(OV + f'SEGT_{modo}_{d}.pkl').copy()
    toks = list(np.load(SA2 + f'ms2_{d}.npz', allow_pickle=True)['tokens'])
    for x in (r, s): x['token'] = [toks[k] for k in x.k.values]; x['dia'] = d
    s.to_pickle(OV + f'g0_segs_{modo}_{d}.pkl'); r.to_pickle(of + '.tmp'); os.replace(of + '.tmp', of)
    print('ok', modo, d, 'fills G0', len(r), 'segs', len(s), 'pnl', round(float(r.pnl.sum()), 2))
