#!/usr/bin/env python3
"""doble_conteo_v3.py -- MIDE el doble conteo de cola de engine.fill_segment BASE (hipotesis: print sellado en/tras la fila de libro descuenta la cola dos veces). TRAIN 26-Oct..09-Nov. Solo lectura.
Pares: (a) sello v2 causal [out_v2/RT_causal, == v2orig] vs v2dd (mismo sello viejo, dedupe): efecto del dedupe con los sellos VIEJOS; (b) v3orig vs v3dd: efecto con sellos v3 (sello correcto a ex(fila)-1 salvo ramas amb/nosig/guard).
Por variante (todas las no-placebo): rellenos solo-sin-dedupe (= candidatos a FANTASMA), solo-con-dedupe, cambios de q, pnl. Fantasma = relleno que desaparece al deduplicar."""
import sys, os, glob, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
DIAS = ['2026-10-26', '2026-10-27', '2026-10-28', '2026-10-29', '2026-10-30', '2026-10-31', '2026-11-01', '2026-11-02', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-07', '2026-11-08', '2026-11-09']
def load(tag, d):
    if tag == 'v2orig': r = pd.read_pickle(H + f'out_v2/RT_causal_{d}.pkl')
    else: r = pd.read_pickle(H + f'out_v3/RT_{tag}_{d}.pkl')
    return r[~r['var'].str.startswith('P')]
def cmp(a_tag, b_tag):
    out = {}
    for d in DIAS:
        try: a, b = load(a_tag, d), load(b_tag, d)
        except FileNotFoundError: continue
        m = a[['var', 'k', 'L', 'seg', 'q', 'pnl', 'cost' if 'cost' in a else 'q']].merge(b[['var', 'k', 'L', 'seg', 'q', 'pnl']], on=['var', 'k', 'L', 'seg'], how='outer', suffixes=('_a', '_b'), indicator=True)
        for v, g in m.groupby('var'):
            o = out.setdefault(v, dict(n_a=0, n_b=0, solo_a=0, solo_b=0, dq=0, pnl_a=0.0, pnl_b=0.0, pnl_solo_a=0.0, pnl_solo_b=0.0, dias=0))
            o['n_a'] += int((g._merge != 'right_only').sum()); o['n_b'] += int((g._merge != 'left_only').sum()); o['solo_a'] += int((g._merge == 'left_only').sum()); o['solo_b'] += int((g._merge == 'right_only').sum())
            both = g[g._merge == 'both']; o['dq'] += int((np.abs(both.q_a - both.q_b) > 1e-9).sum()); o['pnl_a'] += float(g.pnl_a.fillna(0).sum()); o['pnl_b'] += float(g.pnl_b.fillna(0).sum())
            o['pnl_solo_a'] += float(g[g._merge == 'left_only'].pnl_a.sum()); o['pnl_solo_b'] += float(g[g._merge == 'right_only'].pnl_b.sum()); o['dias'] += 1
    return out
R = {}
for a, b in (('v2orig', 'v2dd'), ('v3orig', 'v3dd'), ('v2orig', 'v3orig'), ('v2orig', 'v3dd')):
    R[f'{a}->{b}'] = cmp(a, b); print(f'=== {a} -> {b}')
    print(pd.DataFrame(R[f'{a}->{b}']).T.round(2).to_string())
json.dump(R, open(H + 'out_v3/doble_conteo_v3.json', 'w'), indent=1)
