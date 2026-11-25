#!/usr/bin/env python3
"""f4_techos.py (FN_132, 16-Nov) -- SOLO LECTURA, CPU ~s. TECHO en EV de la brecha (motor v4, v3d BASE, sin correccion de cancelacion) que cerraria VER cada tipo de FN:
EV_sim(+tipo) = (sum p_s + sum p_r[FN tipo]) / (sum c_s + sum c_r[FN tipo]); dEV vs EV_sim; fraccion = dEV / (EV_real - EV_sim). IC90 por cierre (cl = dia + t_ini//300000),
B = 10.000, semilla 20261116 (como QC2). Reproduccion previa: EV_sim -0,2217, EV_real -0,0615, gap 0,1602 (QC2_v2_sinpolvo.json, total.sin_correccion)."""
import os, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; L2 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'
REB = 0.2 * 0.07
def pnl_of(q, L, g): return q * (g - L) + q * REB * L * (1 - L)
R = pd.concat([pd.read_pickle(L2 + f'verif_real/out_v4/V3_2026-10-2{i}.pkl') for i in range(4)], ignore_index=True)
R['q_s'] = R.v3d_BASE_f_q.astype(float); R['q_r'] = R.real_q.astype(float)
R['q_s'] = R.q_s.where(R.q_s >= 1e-3, 0.0)
R['cl'] = R.dia + '_' + (R.t_ini // 300000).astype(str)
R['p_s'] = pnl_of(R.q_s, R.L, R.gana); R['c_s'] = R.q_s * R.L; R['p_r'] = pnl_of(R.q_r, R.L, R.gana); R['c_r'] = R.q_r * R.L
I = pd.read_pickle(H + 'inventario2.pkl')[['oid', 'estructura', 'cls']]; R = R.merge(I, on='oid', how='left')
fn = (R.q_s < 1e-3) & (R.q_r > 1e-9)
e_sim = R.p_s.sum() / R.c_s.sum(); e_real = R.p_r.sum() / R.c_r.sum(); gap = e_real - e_sim
rep = dict(ev_sim=round(e_sim, 4), ev_real=round(e_real, 4), gap=round(gap, 4), n_fn=int(fn.sum()), reproduce_QC2=bool(abs(e_sim + 0.2217) < 5e-5 and abs(e_real + 0.0615) < 5e-5 and int(fn.sum()) == 132))
grupos = {'SOLO': ['SOLO'], 'SOLO_ARRIBA': ['SOLO_ARRIBA'], 'MISMO_NIVEL': ['MISMO_NIVEL'], 'DEBAJO': ['DEBAJO'], 'multi(ARRIBA+MISMO+DEBAJO)': ['SOLO_ARRIBA', 'MISMO_NIVEL', 'DEBAJO'],
          'visibles_en_forward_sin_supuesto(MISMO+DEBAJO)': ['MISMO_NIVEL', 'DEBAJO'], 'todos_132': ['SOLO', 'SOLO_ARRIBA', 'MISMO_NIVEL', 'DEBAJO']}
cols = {'ps': R.p_s, 'cs': R.c_s, 'pr': R.p_r, 'cr': R.c_r}
for g, ests in grupos.items():
    m = fn & R.estructura.isin(ests); cols['p|' + g] = R.p_r.where(m, 0.0); cols['c|' + g] = R.c_r.where(m, 0.0)
M = pd.DataFrame(cols).groupby(R.cl.values).sum(); A = M.to_numpy(float); ix = {c: i for i, c in enumerate(M.columns)}; n = len(M)
rng = np.random.default_rng(20261116); S = np.vstack([rng.multinomial(n, np.full(n, 1.0 / n), size=1000) @ A for _ in range(10)])
es0 = S[:, ix['ps']] / S[:, ix['cs']]; er = S[:, ix['pr']] / S[:, ix['cr']]; gp = er - es0
out = dict(reproduccion=rep, n_cierres=n, techos={})
for g, ests in grupos.items():
    m = fn & R.estructura.isin(ests)
    e1 = (R.p_s.sum() + R.p_r[m].sum()) / (R.c_s.sum() + R.c_r[m].sum())
    eb = (S[:, ix['ps']] + S[:, ix['p|' + g]]) / (S[:, ix['cs']] + S[:, ix['c|' + g]]); de = eb - es0
    out['techos'][g] = dict(n=int(m.sum()), coste_real=round(float(R.c_r[m].sum()), 2), ev_real_tipo=round(float(R.p_r[m].sum() / R.c_r[m].sum()), 4),
                            ev_sim_con_tipo=round(float(e1), 4), dEV=round(float(e1 - e_sim), 4), dEV_ic90=[round(float(np.quantile(de, .05)), 4), round(float(np.quantile(de, .95)), 4)],
                            fraccion=round(float((e1 - e_sim) / gap), 3), p_dEV_le_0=round(float((de <= 0).mean()), 4))
json.dump(out, open(H + 'f4_techos.json', 'w'), indent=1); print(json.dumps(out, indent=1))
