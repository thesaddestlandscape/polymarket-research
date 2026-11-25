#!/usr/bin/env python3
"""f5_metricas.py (FN_132, 16-Nov) -- SOLO LECTURA, CPU ~s. Metricas de las variantes de verif_fn.py (fn_16nov/out/V3_<D>.pkl) contra las 3.796 ordenes reales de B 20-23 Oct:
(1) reproduccion: v3d de verif_fn == v3d_BASE de l2_carrera_10nov/verif_real/out_v4 (q y tf, orden a orden); (2) por variante: rellenos sim, TP, FP, FN, EV_sim, dEV vs v3d,
fraccion de la brecha (EV_real - EV_sim_v3d), IC90 por cierre (B=10.000, semilla 20261116), y que FN de cada tipo (inventario) pasa a TP; FP nuevos."""
import os, glob, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; L2 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'
REB = 0.2 * 0.07
def pnl_of(q, L, g): return q * (g - L) + q * REB * L * (1 - L)
V = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out/V3_*.pkl'))], ignore_index=True)
R4 = pd.concat([pd.read_pickle(L2 + f'verif_real/out_v4/V3_2026-10-2{i}.pkl') for i in range(4)], ignore_index=True)[['oid', 'v3d_BASE_f_q', 'v3d_BASE_f_tf']].rename(columns={'v3d_BASE_f_q': 'q4', 'v3d_BASE_f_tf': 'tf4'})
V = V.merge(R4, on='oid', how='left')
rep = dict(dias=sorted(V.dia.unique().tolist()), n=len(V), q_igual=int((np.abs(V.v3d_BASE_f_q - V.q4) <= 1e-12).sum()), tf_igual=int((V.v3d_BASE_f_tf == V.tf4).sum()))
rep['EXACTA'] = bool(rep['q_igual'] == len(V) and rep['tf_igual'] == len(V))
I = pd.read_pickle(H + 'inventario2.pkl')[['oid', 'estructura']]; V = V.merge(I, on='oid', how='left')
V['cl'] = V.dia + '_' + (V.t_ini // 300000).astype(str); V['q_r'] = V.real_q.astype(float); real = V.q_r > 1e-9
V['p_r'] = pnl_of(V.q_r, V.L, V.gana); V['c_r'] = V.q_r * V.L
tags = [c[:-9] for c in V.columns if c.endswith('_BASE_f_q')]
cols = {'pr': V.p_r, 'cr': V.c_r}
for t in tags:
    q = V[t + '_BASE_f_q'].where(V[t + '_BASE_f_q'] >= 1e-3, 0.0); V[t + '_q'] = q; cols['p|' + t] = pnl_of(q, V.L, V.gana); cols['c|' + t] = q * V.L
M = pd.DataFrame(cols).groupby(V.cl.values).sum(); A = M.to_numpy(float); ix = {c: i for i, c in enumerate(M.columns)}; n = len(M)
rng = np.random.default_rng(20261116); S = np.vstack([rng.multinomial(n, np.full(n, 1.0 / n), size=1000) @ A for _ in range(10)])
e0b = S[:, ix['p|v3d']] / S[:, ix['c|v3d']]; erb = S[:, ix['pr']] / S[:, ix['cr']]
e_real = V.p_r.sum() / V.c_r.sum(); e0 = cols['p|v3d'].sum() / cols['c|v3d'].sum(); gap = e_real - e0
out = dict(reproduccion=rep, ev_real=round(e_real, 4), ev_sim_v3d=round(e0, 4), gap=round(gap, 4), n_cierres=n, variantes={})
for t in tags:
    q = V[t + '_q']; sim = q > 0; tp = sim & real; fp = sim & ~real
    e = cols['p|' + t].sum() / cols['c|' + t].sum(); eb = S[:, ix['p|' + t]] / S[:, ix['c|' + t]]; de = eb - e0b
    sim0 = V['v3d_q'] > 0
    out['variantes'][t] = dict(fills_sim=int(sim.sum()), tp=int(tp.sum()), fp=int(fp.sum()), fn=int((real & ~sim).sum()), ev_sim=round(float(e), 4), dEV=round(float(e - e0), 4),
                               dEV_ic90=[round(float(np.quantile(de, .05)), 4), round(float(np.quantile(de, .95)), 4)], p_dEV_le_0=round(float((de <= 0).mean()), 4),
                               fraccion=round(float((e - e0) / gap), 3), fn_rescatados_por_tipo=V[real & ~sim0 & sim].estructura.value_counts().to_dict(),
                               tp_perdidos=int((real & sim0 & ~sim).sum()), fp_nuevos=int((~real & ~sim0 & sim).sum()), fp_quitados=int((~real & sim0 & ~sim).sum()),
                               pnl_fp_nuevos=round(float(cols['p|' + t][(~real & ~sim0 & sim).values].sum()), 3))
json.dump(out, open(H + 'f5_metricas.json', 'w'), indent=1); print(json.dumps(out, indent=1))
