#!/usr/bin/env python3
"""test_motor_repro.py DIA -- (pesado) eng_v5.build(DIA) debe reproducir q y tf de los segmentos G0 seg==0 de L2/out_v4/SEGT_v3dd_<DIA>.pkl (t_arr = t_dec + 68, fin = t_arr + vida_ms, rem 5, cola BASE)."""
import sys, os, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import eng_v5 as EV
d = sys.argv[1]; E, info = EV.build(d); S = pd.read_pickle(EV.L2 + f'out_v4/SEGT_v3dd_{d}.pkl'); S = S[S.seg == 0]
S = pd.concat([S[S.q >= 1e-3], S[S.q < 1e-3].sample(min(400, int((S.q < 1e-3).sum())), random_state=1)]); bad = 0; n = 0
for r in S.itertuples():
    t_arr = int(r.t_dec) + 68; q, tf, _ = E.run_segment(int(r.k), float(r.L), t_arr, t_arr + int(r.vida_ms), 5.0, 'BASE'); n += 1
    if abs(q - r.q) > 1e-6 or (q >= 1e-3 and int(tf) != int(r.tf)): bad += 1
print('segmentos', n, 'rellenos referencia', int((S.q >= 1e-3).sum()), 'discrepancias', bad); assert bad == 0
