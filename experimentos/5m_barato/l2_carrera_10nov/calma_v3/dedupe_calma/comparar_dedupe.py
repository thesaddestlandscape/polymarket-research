#!/usr/bin/env python3
"""comparar_dedupe.py DIR D1 D2 ... [--ref DIR_REF] -- compara dec2v3dd0_<D>.pkl (sin dedupe) vs dec2v3dd1_<D>.pkl (con dedupe) de esc_dec2_v3_dedupe.py. Por variante: filas (rellenos), q, EUR=sum(pnl) y coste; rellenos AFECTADOS =
filas que no coinciden en (q, tf) tras alinear por (var, mkt, L, orden dentro del grupo) + filas que solo estan en un lado; dEUR_vs_G0 (sum pnl variante - sum pnl G0) con y sin dedupe. Con --ref DIR_REF tambien compara dd0 contra el dec2v3 ya
calculado (motor legacy original): debe ser identico (valida que DayEngV3 legacy reproduce el original)."""
import sys, os, json
import pandas as pd
a = sys.argv[1:]; ref = None
if '--ref' in a: i = a.index('--ref'); ref = a[i + 1].rstrip('/') + '/'; a = a[:i] + a[i + 2:]
D = a[0].rstrip('/') + '/'; dias = a[1:]


def carga(p):
    x = pd.read_pickle(p).sort_values(['var', 'mkt', 'L', 'tf'], kind='stable').reset_index(drop=True); x['ord'] = x.groupby(['var', 'mkt', 'L']).cumcount(); return x


def comp(x, y):
    m = x.merge(y, on=['var', 'mkt', 'L', 'ord'], how='outer', suffixes=('_a', '_b'), indicator=True); solo_a = int((m._merge == 'left_only').sum()); solo_b = int((m._merge == 'right_only').sum()); both = m[m._merge == 'both']
    cambiados = int(((both.q_a - both.q_b).abs() > 1e-9).sum() + (both.tf_a != both.tf_b).sum() - (((both.q_a - both.q_b).abs() > 1e-9) & (both.tf_a != both.tf_b)).sum()); return solo_a, solo_b, cambiados


res = {}; tot = {}
for d in dias:
    a0 = carga(D + f'dec2v3dd0_{d}.pkl'); a1 = carga(D + f'dec2v3dd1_{d}.pkl'); sa, sb, ch = comp(a0, a1); r = dict(filas_sin_dedupe=len(a0), filas_con_dedupe=len(a1), solo_sin=sa, solo_con=sb, cambiados=ch, rellenos_afectados=sa + sb + ch)
    if ref: r0 = carga(ref + f'dec2v3_{d}.pkl'); r['dd0_vs_dec2v3_original'] = dict(zip(('solo_orig', 'solo_dd0', 'cambiados'), comp(r0, a0))); r['dd0_vs_original_filas'] = (len(r0), len(a0))
    pv = {}
    for nom, x in (('sin', a0), ('con', a1)): pv[nom] = {v: dict(n=len(g), pnl=float(g.pnl.sum()), cost=float(g.cost.sum())) for v, g in x.groupby('var')}
    r['por_var'] = pv; res[d] = r
    for nom in ('sin', 'con'):
        for v, z in pv[nom].items():
            t = tot.setdefault(nom, {}).setdefault(v, dict(n=0, pnl=0.0, cost=0.0)); t['n'] += z['n']; t['pnl'] += z['pnl']; t['cost'] += z['cost']
out = dict(dias=dias, por_dia={d: {k: v for k, v in r.items() if k != 'por_var'} for d, r in res.items()}, total={})
afect = sum(r['rellenos_afectados'] for r in res.values()); out['rellenos_afectados_total'] = afect; out['filas_total_sin_dedupe'] = sum(r['filas_sin_dedupe'] for r in res.values())
for v in tot['sin']:
    s, c = tot['sin'][v], tot['con'][v]; g0s, g0c = tot['sin']['G0'], tot['con']['G0']
    out['total'][v] = dict(filas_sin=s['n'], filas_con=c['n'], pnl_sin=round(s['pnl'], 2), pnl_con=round(c['pnl'], 2), dEUR_vs_G0_sin=round(s['pnl'] - g0s['pnl'], 2), dEUR_vs_G0_con=round(c['pnl'] - g0c['pnl'], 2), delta_dEUR=round((c['pnl'] - g0c['pnl']) - (s['pnl'] - g0s['pnl']), 2),
                           EV_sin=round(s['pnl'] / s['cost'], 4) if s['cost'] else None, EV_con=round(c['pnl'] / c['cost'], 4) if c['cost'] else None)
print(json.dumps(out, indent=1))
