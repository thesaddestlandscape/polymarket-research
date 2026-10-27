#!/usr/bin/env python3
"""t3_grupos.py --dias ... --tag X : clasifica cada ORDEN real rellena on-chain en SIN_PRINT / CARRERA / DENTRO (definicion PREREG_V3) con
la ventana REAL y la regla de consumo (cualquier tamano); a nivel puja, grupo de su 1a orden rellena. Recall de M y de su placebo por grupo
(sim_<tag>_pujas.csv) y EV/EUR por grupo con IC90 bootstrap por cierre. Salida grupos_<tag>.json."""
import json, argparse, numpy as np, pandas as pd
from v3lib import *
ap = argparse.ArgumentParser(); ap.add_argument('--dias', required=True); ap.add_argument('--tag', required=True); a = ap.parse_args()
B = pd.read_parquet(DL + 'ordenes_b.parquet'); B = B[B.dia.isin(a.dias.split(',')) & (B.fill == 1)].copy(); rows = []
for dia, g in B.groupby('dia'):
    D = Dia(dia)
    for r in g.itertuples():
        ti, tf = r.t_ini * 1000, r.t_fin * 1000; tci = r.t_cancel_int * 1000 if r.t_cancel_int == r.t_cancel_int else None
        c = D.consumos(r.tok, r.precio, ti, tf + 250)
        tp = c[0][0] if c else None
        grp = 'SIN_PRINT' if tp is None else ('CARRERA' if (tci is not None and tp > tci) else 'DENTRO')
        rows.append(dict(oid=r.oid, puja=r.puja, dia=dia, cie=r.cie, t_dec=r.t_dec, grupo=grp, coste=r.coste, pnl=r.pnl))
O = pd.DataFrame(rows); print(O.groupby(['dia', 'grupo']).size().unstack(fill_value=0))
rng = np.random.default_rng(13); res = {'n_ordenes': O.grupo.value_counts().to_dict()}
for gname, g in O.groupby('grupo'):
    u = g.cie.unique(); v = []
    for _ in range(2000):
        s = pd.concat([g[g.cie == c] for c in rng.choice(u, len(u))]); v.append(s.pnl.sum() / s.coste.sum())
    res['EV_' + gname] = dict(n=len(g), ev=float(g.pnl.sum() / g.coste.sum()), ic90=[float(np.percentile(v, 5)), float(np.percentile(v, 95))], n_cierres=len(u))
try:
    P = pd.read_csv('sim_%s_pujas.csv' % a.tag); f1 = O.sort_values('t_dec').groupby('puja').grupo.first().rename('grupo')
    P = P.merge(f1, left_on='puja', right_index=True, how='left')
    res['recall_por_grupo'] = {k: dict(n=len(g), P_M=float(g.P_M.mean()), P_M_PL90=float(g.P_M_PL90.mean())) for k, g in P[P.real_oc == 1].groupby('grupo')}
    res['no_rellenas'] = dict(n=int((P.real == 0).sum()), P_M=float(P[P.real == 0].P_M.mean()), P_M_PL90=float(P[P.real == 0].P_M_PL90.mean()))
except FileNotFoundError: pass
print(json.dumps(res, indent=1)); json.dump(res, open('grupos_%s.json' % a.tag, 'w'), indent=1)
