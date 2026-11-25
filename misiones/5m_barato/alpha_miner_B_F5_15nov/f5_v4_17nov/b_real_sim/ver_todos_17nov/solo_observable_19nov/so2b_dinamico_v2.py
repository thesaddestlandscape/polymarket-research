#!/usr/bin/env python3
"""ADENDA_SO2_01: F5_t a real_tm3-150 ms en las ordenes rellenas. Solo lectura."""
import os, pickle, numpy as np, pandas as pd
import so1_traza_v2 as S
from so2_f5t_v2 import top, C0, C1, HERE
d = S.cargar_tomador(S.BASE); d['cost'] = d.real_q * d.L; d['pnl'] = d.real_q * (d.gana - d.L)
O = pd.read_pickle(HERE + 'so2_ordenes_v2.pkl')[['oid', 'NONE', 'traza', 'c1', 'terc']]
n_d = len(d); d = d.merge(O, on='oid', how='inner'); print('SO-2b: rellenos fuera por rem_estado != ok (no estan en O):', n_d - len(d)); out = []
for _, r in d.iterrows():
    m = S.TOKM.get(str(r.tok)); v = np.nan
    if m is not None and os.path.exists(S.MK + f'{m[0]}_{m[1]}.gz'):
        B = S.parse(S.MK + f'{m[0]}_{m[1]}.gz'); own = 'Y' if m[2] == 'YES' else 'N'; comp = 'N' if own == 'Y' else 'Y'
        t = int(r.real_tm3) - 150; tc = top(B[comp], t); to = top(B[own], t)
        if tc is not None and not (to is not None and to[0] + tc[0] >= 1000): v = float(np.log1p(tc[1]))
    out.append(v)
d['F5dyn'] = out
d['td'] = np.where(d.F5dyn.isna(), 'inval', np.where(d.F5dyn <= C0, 'bajo', np.where(d.F5dyn <= C1, 'medio', 'alto')))
d['grupo'] = np.where(d.NONE, 'NONE', np.where(d.c1 & d.traza, 'TRAZA_c1', np.where(d.c1, 'c1_otro', 'no_c1')))
g = d.groupby(['grupo', 'td']).agg(n=('oid', 'size'), cost=('cost', 'sum'), pnl=('pnl', 'sum')); g['EV'] = (g.pnl / g.cost).round(3); print(g)
print(pd.crosstab(d.grupo, d.td, normalize='index').round(3))
g2 = d[d.td != 'inval'].groupby('td').agg(n=('oid', 'size'), cost=('cost', 'sum'), pnl=('pnl', 'sum')); g2['EV'] = (g2.pnl / g2.cost).round(3); print('EV rellenos por tercil dinamico', g2)
d[['oid', 'grupo', 'td', 'F5dyn', 'cost', 'pnl', 'dia']].to_pickle(HERE + 'so2b_rellenos_v2.pkl')
