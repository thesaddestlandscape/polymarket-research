#!/usr/bin/env python3
"""t1_sim.py --dias D1,D2 --tag X [--rep 20] [--seed 7] : replay mecanico M de cada puja real de B (inicio = t_dec de su 1a orden real,
mismo token) con latencias muestreadas de tune_latencias.json (solo TUNE) y regla de relleno de la Capa 1 (e,g,f de datos_tune_sel.json).
Variantes: M (prints reales), M_PL90 (prints +90 s, mismo libro), Mdet (latencias = medianas TUNE). Salida sim_<tag>_pujas.csv,
sim_<tag>_ordenes.csv (ordenes de la variante Mdet con su vida, para comparar con la real)."""
import sys, json, argparse, numpy as np, pandas as pd
from v3lib import *
ap = argparse.ArgumentParser(); ap.add_argument('--dias', required=True); ap.add_argument('--tag', required=True)
ap.add_argument('--rep', type=int, default=20); ap.add_argument('--seed', type=int, default=7); a = ap.parse_args()
V2 = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/calibracion_etiqueta/v2/'
S = json.load(open(V2 + 'datos_tune_sel.json'))['sel']; E, F, G = int(S['e']), S['f'], S['g']
LT = json.load(open('tune_latencias.json'))
react = np.array(LT['react']); post = np.array(LT['post_half']); ase = np.array([x for x in LT['asentar'] if x <= 3000])
rng = np.random.default_rng(a.seed)
def lat_rand(): return dict(react=lambda: float(rng.choice(react)), post_half=lambda: float(rng.choice(post)), asentar=lambda: float(rng.choice(ase)))
med = dict(react=lambda: float(np.median(react)), post_half=lambda: float(np.median(post)), asentar=lambda: float(np.median(ase)))
dias = a.dias.split(',')
B = pd.read_parquet(DL + 'ordenes_b.parquet'); B = B[B.dia.isin(dias)].copy()
PJ = []; OR = []
for dia in dias:
    D = Dia(dia); g = B[B.dia == dia]
    for puja, gp in g.groupby('puja'):
        gp = gp.sort_values('t_dec'); r0 = gp.iloc[0]; tk = r0.tok; L = Libro(D, tk, K[r0.coin]); td0 = r0.t_dec * 1000; cie = r0.cie * 1000
        out = dict(puja=puja, dia=dia, slug=r0.slug, coin=r0.coin, cie=int(r0.cie), real=int(gp.fill_puja.max()), real_oc=int(gp.fill.max()),
                   gana=float(r0.gana_lado) if r0.gana_lado == r0.gana_lado else np.nan, n_ord_real=len(gp),
                   vida1_real=(r0.t_fin - r0.t_ini) * 1000, coste_real=gp.coste.sum(), pnl_real=gp.pnl.sum())
        for nm, sh in (('M', 0), ('M_PL90', 90000)):
            fl = []; no = []; ps = []
            for _ in range(a.rep):
                s = simular_puja(D, L, tk, td0, cie, lat_rand(), E, F, G, shift=sh)
                fl.append(s['fill']); no.append(s['n_ord'])
                if s['fill']: ps.append(s['ordenes'][-1][3])
            out['P_' + nm] = float(np.mean(fl)); out['nord_' + nm] = float(np.mean(no)); out['pfill_' + nm] = float(np.mean(ps)) if ps else np.nan
        s = simular_puja(D, L, tk, td0, cie, med, E, F, G)
        out['P_Mdet'] = int(s['fill']); out['nord_Mdet'] = s['n_ord']
        out['vida1_Mdet'] = (s['ordenes'][0][2] + 30 - s['ordenes'][0][1]) if s['ordenes'] else np.nan
        out['p1_Mdet'] = s['ordenes'][0][3] if s['ordenes'] else np.nan; out['p1_real'] = r0.precio
        PJ.append(out)
        for j, o in enumerate(s['ordenes']): OR.append(dict(puja=puja, dia=dia, j=j, td=o[0], ti=o[1], tc=o[2], p=o[3], fill=o[4] is not None))
    print(dia, 'listo', flush=True)
PJ = pd.DataFrame(PJ); PJ.to_csv('sim_%s_pujas.csv' % a.tag, index=False); pd.DataFrame(OR).to_csv('sim_%s_ordenes.csv' % a.tag, index=False)
print(PJ[['real', 'P_M', 'P_M_PL90', 'P_Mdet', 'n_ord_real', 'nord_M', 'nord_Mdet']].mean().round(3).to_dict())
for c in ('P_M', 'P_M_PL90', 'P_Mdet'): print('AUC', c, round(auc(PJ[c], PJ.real), 3))
v = PJ.dropna(subset=['vida1_Mdet']); print('vida 1a orden ms mediana real/Mdet', round(v.vida1_real.median()), round(v.vida1_Mdet.median()), 'Spearman', round(v.vida1_real.corr(v.vida1_Mdet, method='spearman'), 3), 'n', len(v))
