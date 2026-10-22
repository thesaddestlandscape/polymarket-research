#!/usr/bin/env python3
"""fill_table.py -- tabla de RELLENOS de la politica base B-like (ETH k=2, SOL/XRP k=1 sobre la ultima operacion, repeg 5 s, T 295..65, cons)
con los rasgos del paso de relleno y de los pasos previos. Una fila por mercado rellenado. Salida: datos/ft_base.pkl"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from sa_sim import *
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = load(B + '/datos/sim')
R = run(D, delta=dB(D), mode='cons')
ix = np.flatnonzero(R.filled.values); k = R.k.values[ix]
FT = R.iloc[ix].copy().reset_index(drop=True)
for f in ['q', 'dp10', 'dp30', 'dp60', 'dopen', 'hi60', 'v30', 'sh30', 'flow60', 'z', 'ret10', 'sig', 'lastage', 'minpc']: FT[f] = D[f][ix, k]
FT['T'] = TKV[k]; FT['overshoot'] = FT.p - FT.minpc; FT['hora'] = pd.to_datetime(FT.fin - FT['T'], unit='s').dt.hour
# markout (precio del lado en pasos posteriores; NaN si no hay): q en k+1 (5 s), k+6 (30 s), k+24 (120 s)
for nm, s in (('mo5', 1), ('mo30', 6), ('mo120', 24)):
    kk = k + s; okk = kk < D['q'].shape[1]; v = np.full(len(ix), np.nan); v[okk] = D['q'][ix[okk], kk[okk]]; FT[nm] = (v - FT.p) / FT.p
FT['c'] = 5 * FT.p; FT['pn'] = 5 * (FT.win.astype(float) - FT.p)
FT['dpos'] = FT.dia
FT.to_pickle(B + '/datos/ft_base.pkl'); print(len(FT), FT.groupby('dia').size().to_dict())
q = R.quoted.sum(); print('quoted', q, 'fill', len(FT))
# AS: EV si fueramos rellenados SIEMPRE al precio de la 1a puja (sin selección)
Q = R[R.quoted]; print('win quoted', Q.win.mean(), 'pq', Q.pq.mean(), 'EV_allquoted', (Q.win.astype(float) - Q.pq).sum() / Q.pq.sum(), 'EV_filled', FT.pn.sum() / FT.c.sum())
