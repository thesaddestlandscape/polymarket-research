#!/usr/bin/env python3
"""e4_metricas.py: K1..K6 de PREREG_V2 sobre test_capa1.csv y test_capaG.csv (TEST 22-23). Salida datos/v2_metricas.json"""
import sys, json, numpy as np, pandas as pd
sys.path.insert(0, '.'); from v2lib import *
L = pd.read_csv(DL + 'v2/test_capa1.csv'); P = pd.read_csv(DL + 'v2/test_capaG.csv'); rng = np.random.default_rng(20261026); M = {}
n = len(L); kr = int(L.fill.sum()); lo, hi = wilson(kr, n); Po, Pr = L.v.mean(), L.fill.mean()
pj = L.groupby('puja').agg(v=('v', 'max')); real_pj = P.set_index('puja').real; pv = pj.v.reindex(real_pj.index)
tp = int(((L.v == 1) & (L.fill == 1)).sum()); fp = int(((L.v == 1) & (L.fill == 0)).sum()); fn = int(((L.v == 0) & (L.fill == 1)).sum())
M['capa1'] = dict(n_ordenes=n, rellenas_real=kr, P_orden_real=Pr, wilson=[lo, hi], P_orden_v=Po, rel_err=(Po - Pr) / Pr, P_puja_real=float(real_pj.mean()), P_puja_v=float(pv.mean()), recall=tp / (tp + fn), precision=tp / (tp + fp), tp=tp, fp=fp, fn=fn, auc_orden=auc(L.score, L.fill), n_pujas=len(real_pj))
M['capa1']['K1'] = bool((abs(M['capa1']['rel_err']) <= 0.30 or lo <= Po <= hi) and abs(M['capa1']['P_puja_v'] - M['capa1']['P_puja_real']) <= 0.10 and M['capa1']['recall'] >= 0.5 and M['capa1']['precision'] >= 0.5)
cl = P.slug.values; ucl = np.unique(cl); idx = {c: np.where(cl == c)[0] for c in ucl}
def boot(fn_, nb=2000):
    r = []
    for _ in range(nb):
        s = rng.choice(ucl, len(ucl)); ii = np.concatenate([idx[c] for c in s]); r.append(fn_(ii))
    return [float(x) for x in np.percentile(r, [5, 95])]
Pr_ = P.real.values
G = {}
for nm in ('G', 'PL+90', 'PL-90'):
    x = P['P_' + nm].values; G[nm] = dict(P_puja=float(x.mean()), P_orden=float(P['Po_' + nm].mean()), auc=auc(x, Pr_), dif=float(x.mean() - Pr_.mean()), ic90_dif_cierre=boot(lambda ii, x=x: x[ii].mean() - Pr_[ii].mean()))
G['por_dia'] = {d: dict(real=float(g.real.mean()), G=float(g.P_G.mean()), PLp=float(g['P_PL+90'].mean()), PLm=float(g['P_PL-90'].mean()), n_pujas=len(g)) for d, g in P.groupby('dia')}
# K2/K3/K4/K5
rel_o = (G['G']['P_orden'] - Pr) / Pr; ok_o = abs(rel_o) <= 0.30 or lo <= G['G']['P_orden'] <= hi
G['K2'] = bool(abs(G['G']['dif']) <= 0.10 and ok_o); G['K2_det'] = dict(rel_err_orden=rel_o, orden_ok=bool(ok_o))
G['K3'] = bool(G['G']['auc'] >= 0.65); apl = (G['PL+90']['auc'] + G['PL-90']['auc']) / 2; G['auc_placebo_medio'] = apl
G['K4'] = bool(apl <= 0.60 and G['G']['auc'] - apl >= 0.10)
G['K5'] = bool(all(abs(v['G'] - v['real']) <= 0.15 for v in G['por_dia'].values()) and G['G']['ic90_dif_cierre'][0] <= 0 <= G['G']['ic90_dif_cierre'][1])
# K6 EV ponderado por EUR (informativo)
ev_v = P.pnl_G.sum() / P.cost_G.sum() if P.cost_G.sum() > 0 else np.nan; rl = L[L.fill == 1]; ev_r = rl.pnl.sum() / rl.coste.sum()
ci_v = boot(lambda ii: P.pnl_G.values[ii].sum() / max(P.cost_G.values[ii].sum(), 1e-9)); lm = L.groupby('slug')[['pnl', 'coste']].sum()
rr = []
for _ in range(2000):
    s = rng.choice(lm.index.values, len(lm)); q = lm.loc[s]; rr.append(q.pnl.sum() / max(q.coste.sum(), 1e-9))
G['K6'] = dict(EV_virtual=float(ev_v), ic90_cierre_virtual=ci_v, EV_real=float(ev_r), ic90_cierre_real=[float(x) for x in np.percentile(rr, [5, 95])], ok=bool(abs(ev_v - ev_r) <= 0.15))
M['capaG'] = G
M['veredicto'] = 'CALIBRADA' if (M['capa1']['K1'] and G['K2'] and G['K3'] and G['K4'] and G['K5']) else ('PARCIAL' if M['capa1']['K1'] else 'NO_CALIBRADA')
json.dump(M, open('datos_v2_metricas.json', 'w'), indent=1, default=float); print(json.dumps(M, indent=1, default=float))
