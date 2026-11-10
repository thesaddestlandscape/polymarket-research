#!/usr/bin/env python3
"""Paso 1 (solo lectura): tabla de ordenes G0 del motor passT (RT_/SEGT_, sin tocar) + token_id por dia (ms_<D>.npz 'tokens').
Salida: out/g0_fills.pkl (fills G0 con token), out/g0_segs.pkl (todos los segmentos colocados). Uso: python3 -I prep_fills.py"""
import numpy as np, pandas as pd, os
H = os.path.dirname(os.path.abspath(__file__)) + '/'
Q = H + '../q11/toxicidad_thru1/out/'; M = H + 'passT_copia/out/'
DL = '/root/polymarket-research-datalogs/sa_ms/'
DIAS = ['2026-10-26','2026-10-27','2026-10-28','2026-10-29','2026-10-30','2026-10-31','2026-11-01','2026-11-02','2026-11-03','2026-11-04','2026-11-05','2026-11-06','2026-11-07','2026-11-08','2026-11-09']
F = []; S = []
for d in DIAS:
    p = (M if os.path.exists(M + f'RT_{d}.pkl') else Q)
    r = pd.read_pickle(p + f'RT_{d}.pkl'); r = r[r['var'] == 'G0'].copy()
    s = pd.read_pickle(p + f'SEGT_{d}.pkl').copy()
    toks = list(np.load(DL + f'ms_{d}.npz', allow_pickle=True)['tokens'])
    for x in (r, s): x['token'] = [toks[k] for k in x.k.values]; x['dia'] = d
    F.append(r); S.append(s)
F = pd.concat(F, ignore_index=True); S = pd.concat(S, ignore_index=True)
F.to_pickle(H + 'out/g0_fills.pkl'); S.to_pickle(H + 'out/g0_segs.pkl')
print(F.groupby('dia').agg(n=('pnl', 'size'), pnl=('pnl', 'sum'), cost=('cost', 'sum')).round(1).to_string())
