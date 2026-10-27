#!/usr/bin/env python3
"""t4_sin_autoprint.py --dias ... --tag X : ATAQUE R1 (ADENDA_R1). Quita del feed de prints los AUTO-PRINTS de B (cada relleno on-chain
de B -> el print del token a su precio (SELL) o del complementario a 1-p (BUY) con el mismo tamano, recepcion en [ts_est-6 s, ts_est+1 s],
el mas cercano a ts_est-2,4 s) y repite M y M_PL90 (mismas latencias/semilla que t1). Salida sim_<tag>_pujas.csv."""
import json, argparse, numpy as np, pandas as pd
from v3lib import *
ap = argparse.ArgumentParser(); ap.add_argument('--dias', required=True); ap.add_argument('--tag', required=True); ap.add_argument('--rep', type=int, default=20); a = ap.parse_args()
V2 = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/calibracion_etiqueta/v2/'
S = json.load(open(V2 + 'datos_tune_sel.json'))['sel']; E, F, G = int(S['e']), S['f'], S['g']
LT = json.load(open('tune_latencias.json')); react = np.array(LT['react']); post = np.array(LT['post_half']); ase = np.array([x for x in LT['asentar'] if x <= 3000])
rng = np.random.default_rng(7)
def lat_rand(): return dict(react=lambda: float(rng.choice(react)), post_half=lambda: float(rng.choice(post)), asentar=lambda: float(rng.choice(ase)))
B = pd.read_parquet(DL + 'ordenes_b.parquet'); OC = pd.read_csv(DL + 'b_fills_onchain.csv'); OC['oid'] = OC.order_hash.str.lower()
B['oid_l'] = B.oid.str.lower(); OC = OC.merge(B[['oid_l', 'tok', 'precio', 'dia']], left_on='oid', right_on='oid_l', how='inner')
PJ = []; quitados = {}
for dia in a.dias.split(','):
    D = Dia(dia); n_q = 0; n_nf = 0
    for r in OC[OC.dia == dia].itertuples():
        hit = None; best = 1e18; tgt = r.ts_est * 1000 - 2400
        for tk, side, pr in ((r.tok, 0, r.precio), (D.comp.get(r.tok), 1, 1 - r.precio)):
            arr = D.tr.get(tk) if tk else None
            if arr is None: continue
            lo, hi = np.searchsorted(arr[:, 0], [r.ts_est * 1000 - 6000, r.ts_est * 1000 + 1000])
            for i in range(lo, hi):
                if arr[i, 2] == side and abs(arr[i, 1] - pr) < 1e-6 and abs(arr[i, 3] - r.taker_amt) < 1e-4 and not D.dup[tk][i]:
                    d = abs(arr[i, 0] - tgt)
                    if d < best: best = d; hit = (tk, i)
        if hit: D.dup[hit[0]][hit[1]] = True; n_q += 1      # marcado como dup = invisible para consumos()
        else: n_nf += 1
    quitados[dia] = dict(quitados=n_q, sin_casar=n_nf); print(dia, quitados[dia], flush=True)
    g = B[B.dia == dia]
    for puja, gp in g.groupby('puja'):
        gp = gp.sort_values('t_dec'); r0 = gp.iloc[0]; L = Libro(D, r0.tok, K[r0.coin])
        out = dict(puja=puja, dia=dia, cie=int(r0.cie), real=int(gp.fill_puja.max()))
        for nm, sh in (('M', 0), ('M_PL90', 90000)):
            out['P_' + nm] = float(np.mean([simular_puja(D, L, r0.tok, r0.t_dec * 1000, r0.cie * 1000, lat_rand(), E, F, G, shift=sh)['fill'] for _ in range(a.rep)]))
        PJ.append(out)
P = pd.DataFrame(PJ); P.to_csv('sim_%s_pujas.csv' % a.tag, index=False)
Gd = pd.read_csv(DL + 'v2/test_capaG.csv')[['puja', 'P_G']]; P = P.merge(Gd, on='puja', how='left')
res = dict(quitados=quitados, n=len(P), real=float(P.real.mean()), P_M=float(P.P_M.mean()), P_PL90=float(P.P_M_PL90.mean()),
           auc_M=auc(P.P_M, P.real), auc_PL90=auc(P.P_M_PL90, P.real), auc_G=auc(P.P_G, P.real) if P.P_G.notna().all() else None)
rb = np.random.default_rng(11); u = P.cie.unique(); v = []; w = []
for _ in range(2000):
    s = pd.concat([P[P.cie == c] for c in rb.choice(u, len(u))]); v.append(auc(s.P_M, s.real) - auc(s.P_M_PL90, s.real))
    if res['auc_G'] is not None: w.append(auc(s.P_M, s.real) - auc(s.P_G, s.real))
res['dauc_PL90_ic90'] = [float(np.percentile(v, 5)), float(np.percentile(v, 95))]
if w: res['dauc_G_ic90'] = [float(np.percentile(w, 5)), float(np.percentile(w, 95))]
print(json.dumps(res, indent=1)); json.dump(res, open('r1_%s.json' % a.tag, 'w'), indent=1)
