#!/usr/bin/env python3
"""concat_v2.py MODO DIA [DIA...] -> out_v2/g0_fills_<modo>_ALL.pkl y g0_segs_<modo>_ALL.pkl (concatenacion de los por-dia de prep_fills_v2.py; falla si falta alguno)."""
import sys, os, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OV = H + 'out_v2/'; modo = sys.argv[1]; dias = sys.argv[2:]
F = pd.concat([pd.read_pickle(OV + f'g0_fills_{modo}_{d}.pkl') for d in dias], ignore_index=True); S = pd.concat([pd.read_pickle(OV + f'g0_segs_{modo}_{d}.pkl') for d in dias], ignore_index=True)
F.to_pickle(OV + f'g0_fills_{modo}_ALL.pkl'); S.to_pickle(OV + f'g0_segs_{modo}_ALL.pkl'); print('ok', modo, len(dias), 'dias', len(F), 'fills', len(S), 'segs')
