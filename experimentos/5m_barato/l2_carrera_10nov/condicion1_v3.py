#!/usr/bin/env python3
"""condicion1_v3.py DIA [DIA...] -- aceptacion (n L2-valido, EV) y dtf de G0 con sello v3 frente a original (passT_copia/out, legacy) y causal v2 (out_v2). Sin cambiar reglas ni umbrales. 0 ordenes.
Referencia de aceptacion §4 (original, 03-07 Nov): n=1350 L2-valido, EV rb0,2 = -0,2447. Salida out_v3/condicion1_v3_<dias>.json"""
import sys, os, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; V2 = H + 'out_v2/'; V3 = H + 'out_v3/'; M = H + 'passT_copia/out/'; Q = H + '../q11/toxicidad_thru1/out/'
dias = sys.argv[1:]; R = dict(dias=dias, tags={}, pares={})
def pct(x):
    x = np.asarray(x, float)
    if len(x) == 0: return dict(n=0)
    p = np.percentile(x, [1, 5, 50, 95, 99]); return dict(n=int(len(x)), p1=float(p[0]), p5=float(p[1]), p50=float(p[2]), p95=float(p[3]), p99=float(p[4]), abs_le_50=round(float((np.abs(x) <= 50).mean()), 4), igual=round(float((x == 0).mean()), 4))
def resumen(F, T, tfcol='tf'):
    m = F.merge(T[['k', 'L', 'tf', 'bad']], left_on=['k', 'L', tfcol], right_on=['k', 'L', 'tf'], how='left', suffixes=('', '_t'), validate='1:1'); v = m[m.bad.isna()]
    return dict(fills=int(len(F)), pnl=float(F.pnl.sum()), cost=float(F.cost.sum()), n_l2valido=int(len(v)), pnl_l2valido=float(v.pnl.sum()), cost_l2valido=float(v.cost.sum()), bad=m.bad.fillna('ok').value_counts().to_dict())
acc = {}
for d in dias:
    G = {}
    for tag, dirp in (('v3dd', V3), ('v3orig', V3), ('v2dd', V3)):
        f, t = dirp + f'g0_fills_{tag}_{d}.pkl', dirp + f'trg_{tag}_{d}.pkl'
        if os.path.exists(f) and os.path.exists(t):
            F = pd.read_pickle(f); F['cost'] = F.q * F.L; F['tf_orig'] = F.tf; G[tag] = F; r = resumen(F, pd.read_pickle(t), 'tf_orig'); R['tags'].setdefault(tag, {})[d] = r
    f, t = V2 + f'g0_fills_causal_{d}.pkl', V2 + f'trg_causal_{d}.pkl'
    if os.path.exists(f) and os.path.exists(t):
        F = pd.read_pickle(f); F['cost'] = F.q * F.L; G['causal_v2'] = F; R['tags'].setdefault('causal_v2', {})[d] = resumen(F, pd.read_pickle(t))
    p = M if os.path.exists(M + f'RT_{d}.pkl') else Q
    r = pd.read_pickle(p + f'RT_{d}.pkl'); r = r[r['var'] == 'G0'].copy(); r['cost'] = r.q * r.L; G['original'] = r; R['tags'].setdefault('original', {})[d] = resumen(r, pd.read_pickle(H + f'out/trg_{d}.pkl'))
    if 'v3dd' in G:
        for ref in ('original', 'causal_v2'):
            a, b = G[ref], G['v3dd']; m = a.merge(b, on=['k', 'L', 'seg'], how='outer', suffixes=('_ref', '_new'), indicator=True); both = m[m._merge == 'both']
            R['pares'][f'v3dd_vs_{ref}_{d}'] = dict(n_ref=int(len(a)), n_new=int(len(b)), solo_ref=int((m._merge == 'left_only').sum()), solo_new=int((m._merge == 'right_only').sum()), en_ambos=int(len(both)), dtf_ms=pct((both.tf_new - both.tf_ref).values),
                                                    pnl_solo_ref=float(m[m._merge == 'left_only'].pnl_ref.sum()), pnl_solo_new=float(m[m._merge == 'right_only'].pnl_new.sum()))
def tot(tag):
    x = R['tags'][tag]; n = sum(v['n_l2valido'] for v in x.values()); p = sum(v['pnl_l2valido'] for v in x.values()); c = sum(v['cost_l2valido'] for v in x.values())
    return dict(n_l2valido=n, pnl=round(p, 2), ev_l2valido=round(p / c, 4) if c else None, fills=sum(v['fills'] for v in x.values()), ev_todos=round(sum(v['pnl'] for v in x.values()) / sum(v['cost'] for v in x.values()), 4))
R['aceptacion_total'] = {t: tot(t) for t in R['tags']}; R['esperado_original'] = dict(n=1350, ev=-0.2447)
json.dump(R, open(V3 + 'condicion1_v3_' + '_'.join(dias) + '.json', 'w'), indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
print(json.dumps(R['aceptacion_total'], indent=1)); print({k: v for k, v in R['pares'].items() if 'original' in k})
