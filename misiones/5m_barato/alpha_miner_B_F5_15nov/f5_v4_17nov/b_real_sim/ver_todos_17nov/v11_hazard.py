#!/usr/bin/env python3
"""v11_hazard.py (18-Nov) -- paso 2b del PREREG_VER_TODOS_v2_18nov (sha b3374be3...): hazard de llegada de tomadores por intervalos de 250 ms, logistica L2 C=1, leave-one-day-out.
Entrada out_v2/HZ_<tag>_<d>.pkl (rasgos solo <= t) + out_v2/<tag>_<d>.pkl (real_q, clasificacion COLAv). Solo calculo. -> v11_hazard.json"""
import glob, json, os, hashlib, numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import roc_auc_score
H = os.path.dirname(os.path.abspath(__file__)) + '/'; TAG = 'V2_r3_call00a35_intc33_v3d'; FLOOR = 1e-3
assert hashlib.sha256(open(H + 'PREREG_VER_TODOS_v2_18nov.md', 'rb').read()).hexdigest().startswith('b3374be38c2f12ce')
B = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + f'out_v2/HZ_{TAG}_2026-10-2?.pkl'))], ignore_index=True)
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + f'out_v2/{TAG}_2026-10-2?.pkl'))], ignore_index=True)
for c in ('eth', 'sol', 'xrp'): B[f'c_{c}'] = (B.coin == c).astype(int)
F = ['dist', 'spread', 'lbsz', 'lcola', 'Tc', 'yes', 'r1', 'r5', 'r30', 'a5', 'c_eth', 'c_sol']
assert not B[F].isna().any().any(), 'NaN en rasgos'
DIAS = sorted(B.dia.unique()); B['p'] = np.nan; out = dict(n_bins=len(B), n_pos=int(B.y.sum()), por_dia={})
for d in DIAS:
    tr = B.dia != d; te = ~tr
    if B.y[tr].sum() < 5 or B.y[te].sum() == 0: continue
    m = make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=2000)).fit(B.loc[tr, F], B.y[tr])
    p = m.predict_proba(B.loc[te, F])[:, 1]; B.loc[te, 'p'] = p; y = B.y[te].values; b0 = B.y[tr].mean()
    bs = float(np.mean((p - y) ** 2)); bs0 = float(np.mean((b0 - y) ** 2))
    out['por_dia'][d] = dict(bins=int(te.sum()), pos=int(y.sum()), brier=round(bs, 6), brier_base=round(bs0, 6), skill=round(1 - bs / bs0, 4), auc=round(float(roc_auc_score(y, p)), 3),
                             coef=dict(zip(F, np.round(m[-1].coef_[0], 3).tolist())))
V = B[B.p.notna()].copy(); V['dec'] = pd.qcut(V.p.rank(method='first'), 10, labels=False)
out['fiabilidad_decil'] = V.groupby('dec').agg(p_media=('p', 'mean'), y_media=('y', 'mean'), n=('y', 'size')).round(5).to_dict('index')
out['auc_total'] = round(float(roc_auc_score(V.y, V.p)), 3)
# separacion perdedores/ganadores en el intervalo del relleno
P = V[V.y == 1].merge(R[['oid', 'real_q', 'COLAv_f_q']], on='oid', how='left'); P['pierde'] = (P.gana.astype(float) == 0).astype(int)
out['sep_perd_gan'] = dict(n=len(P), perd=int(P.pierde.sum()), auc_p_predice_perder=round(float(roc_auc_score(P.pierde, P.p)), 3) if P.pierde.nunique() == 2 else None,
                           por_dia={d: (round(float(roc_auc_score(g.pierde, g.p)), 3) if g.pierde.nunique() == 2 else None, len(g)) for d, g in P.groupby('dia')})
P['ter'] = pd.qcut(P.p.rank(method='first'), 3, labels=['bajo', 'medio', 'alto'])
def evg(g):
    c = (g.real_q * g.L).sum(); return dict(n=len(g), ev_eur=round(float((g.real_q * (g.gana.astype(float) - g.L)).sum() / c), 4) if c > 0 else None, ev_unit=round(float(((g.gana.astype(float) - g.L) / g.L).mean()), 4))
out['EV_rellenos_por_tercil'] = {str(k): evg(g) for k, g in P.groupby('ter', observed=True)}
# visibles (TP de COLAv) frente a no identificables (FN de COLAv): hazard predicha en su intervalo de relleno
P['vis'] = (P.COLAv_f_q.fillna(0) >= FLOOR) & (P.COLAv_f_q.fillna(0) >= 0.5 * P.real_q)
out['hazard_vis_vs_noident'] = dict(vis=dict(n=int(P.vis.sum()), p_med=float(P.p[P.vis].median())), noident=dict(n=int((~P.vis).sum()), p_med=float(P.p[~P.vis].median())),
                                    auc_p_predice_noident=round(float(roc_auc_score(~P.vis, P.p)), 3) if P.vis.nunique() == 2 else None)
# nivel orden: P(relleno antes de te) = 1 - prod(1-p) (ventana endogena: solo descriptivo)
Oo = V.groupby('oid').agg(p_o=('p', lambda s: 1 - np.prod(1 - s.values)), y_o=('y', 'max'), dia=('dia', 'first')).reset_index()
out['orden'] = dict(n=len(Oo), auc=round(float(roc_auc_score(Oo.y_o, Oo.p_o)), 3), brier=round(float(np.mean((Oo.p_o - Oo.y_o) ** 2)), 5), brier_base=round(float(np.mean((Oo.y_o.mean() - Oo.y_o) ** 2)), 5))
ok = [x for x in out['por_dia'].values()]
out['UTIL'] = bool(sum(x['skill'] > 0 for x in ok) >= 3 and out['auc_total'] >= 0.60)
sp = out['sep_perd_gan']; dd = [v[0] for v in sp['por_dia'].values() if v[0] is not None]
out['SEPARA_AS'] = bool(sp['auc_p_predice_perder'] is not None and sp['auc_p_predice_perder'] >= 0.60 and sum(x > 0.5 for x in dd) >= 3)
json.dump(out, open(H + 'v11_hazard.json', 'w'), indent=1, default=str); print(json.dumps(out, indent=1, default=str)[:6000])
