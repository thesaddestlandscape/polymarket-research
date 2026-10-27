#!/usr/bin/env python3
"""t2_eval.py --tag test : criterios C1..C7 del PREREG_V3 sobre sim_<tag>_pujas.csv + Capa G de v2 (test_capaG.csv) + grupos de rellenos.
IC90 = bootstrap por CIERRE (cie, todas las monedas del mismo cierre juntas), 2000 reps, semilla 11. Salida eval_<tag>.json + stdout."""
import sys, json, argparse, numpy as np, pandas as pd
from v3lib import *
ap = argparse.ArgumentParser(); ap.add_argument('--tag', default='test'); ap.add_argument('--depurar-sin-g', action='store_true'); a = ap.parse_args()
P = pd.read_csv('sim_%s_pujas.csv' % a.tag)
G = pd.read_csv(DL + 'v2/test_capaG.csv')[['puja', 'P_G', 'P_PL+90']].rename(columns={'P_PL+90': 'P_G90'})
P = P.merge(G, on='puja', how='left')
if a.depurar_sin_g: P['P_G'] = P.P_M_PL90; P['P_G90'] = P.P_M_PL90   # SOLO depuracion del codigo en TUNE (G no existe en TUNE)
print('pujas', len(P), 'sin G', int(P.P_G.isna().sum()), 'rellenas real', int(P.real.sum()))
rng = np.random.default_rng(11); cl = P.cie.values; ucl = np.unique(cl); idx = {c: np.where(cl == c)[0] for c in ucl}
def boot(fn, R=2000):
    v = []
    for _ in range(R):
        ii = np.concatenate([idx[c] for c in rng.choice(ucl, len(ucl))]); s = P.iloc[ii]
        try: v.append(fn(s))
        except Exception: pass
    v = np.array([x for x in v if x == x]); return [float(np.percentile(v, 5)), float(np.percentile(v, 95))]
O = {'n_pujas': len(P), 'n_cierres': len(ucl), 'real': float(P.real.mean())}
for c in ('P_M', 'P_M_PL90', 'P_Mdet', 'P_G', 'P_G90'):
    O[c] = dict(media=float(P[c].mean()), sesgo=float(P[c].mean() - P.real.mean()), auc=auc(P[c], P.real))
O['C1_ic90_sesgo_M'] = boot(lambda s: s.P_M.mean() - s.real.mean())
O['C3_dauc_M_vs_PL90'] = O['P_M']['auc'] - O['P_M_PL90']['auc']; O['C3_ic90'] = boot(lambda s: auc(s.P_M, s.real) - auc(s.P_M_PL90, s.real))
O['C4_dauc_M_vs_G'] = O['P_M']['auc'] - O['P_G']['auc']; O['C4_ic90'] = boot(lambda s: auc(s.P_M, s.real) - auc(s.P_G, s.real))
O['C4_dabs_sesgo_ic90'] = boot(lambda s: abs(s.P_M.mean() - s.real.mean()) - abs(s.P_G.mean() - s.real.mean()))
O['brier'] = {c: float(((P[c] - P.real) ** 2).mean()) for c in ('P_M', 'P_M_PL90', 'P_G', 'P_G90')}
O['C2_auc_ic90'] = boot(lambda s: auc(s.P_M, s.real))
O['por_dia'] = {d: dict(n=len(g), real=float(g.real.mean()), P_M=float(g.P_M.mean()), P_G=float(g.P_G.mean()), auc_M=auc(g.P_M, g.real), auc_G=auc(g.P_G, g.real), auc_PL90=auc(g.P_M_PL90, g.real))
                for d, g in P.groupby('dia')}
v = P.dropna(subset=['vida1_Mdet'])
O['C6'] = dict(n=len(v), med_real=float(v.vida1_real.median()), med_Mdet=float(v.vida1_Mdet.median()), spearman=float(v.vida1_real.corr(v.vida1_Mdet, method='spearman')),
               nord_real=float(P.n_ord_real.mean()), nord_M=float(P.nord_M.mean()))
# C7 EV informativo: relleno esperado de M a su precio medio de relleno (5 acc) vs real on-chain
P['cost_M'] = P.P_M * 5 * P.pfill_M.fillna(0); P['pnl_M'] = P.P_M * 5 * (P.gana - P.pfill_M.fillna(0))
r = P.dropna(subset=['gana'])
O['C7'] = dict(ev_M=float(r.pnl_M.sum() / r.cost_M.sum()), ev_real=float(r.pnl_real.sum() / r.coste_real.sum()),
               ic90_M=boot(lambda s: s.dropna(subset=['gana']).pnl_M.sum() / s.dropna(subset=['gana']).cost_M.sum()),
               ic90_real=boot(lambda s: s.dropna(subset=['gana']).pnl_real.sum() / s.dropna(subset=['gana']).coste_real.sum()))
# veredicto
c1 = abs(O['P_M']['sesgo']) <= 0.10 and O['C1_ic90_sesgo_M'][0] <= 0 <= O['C1_ic90_sesgo_M'][1]
c2 = O['P_M']['auc'] >= 0.70
c3 = O['C3_dauc_M_vs_PL90'] >= 0.10 and O['C3_ic90'][0] > 0
c4 = O['C4_ic90'][0] > 0 and abs(O['P_M']['sesgo']) < abs(O['P_G']['sesgo'])
c5 = all(abs(x['P_M'] - x['real']) <= 0.15 for x in O['por_dia'].values())
c6 = O['C6']['spearman'] >= 0.4 and 0.5 <= O['C6']['med_Mdet'] / O['C6']['med_real'] <= 2
O['criterios'] = dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6)
O['veredicto'] = ('MEJORA_CALIBRADA' if all([c1, c2, c3, c4, c5, c6]) else 'MEJORA_PARCIAL' if (c2 and c3 and c4) else 'NO_MEJORA')
print(json.dumps(O, indent=1, default=float)); json.dump(O, open('eval_%s.json' % a.tag, 'w'), indent=1, default=float)
