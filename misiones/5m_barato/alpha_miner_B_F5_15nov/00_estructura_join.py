#!/usr/bin/env python3
"""Paso 0 (SOLO estructura/cobertura del join, sin EV por tercil): fills reales de B (e02real_fills.json) <-> tokens.csv <-> poblacion r_D/l_D (F5 a r-100 ms)."""
import json, glob, sys
import numpy as np, pandas as pd
RE = '/root/polymarket-research/misiones/5m_barato/docs/reverse-engineering/casos/RE-AS-B/'
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'
fills = pd.DataFrame(json.load(open(RE + 'e02real_fills.json')))
cruce = json.load(open(RE + 'e02real_cruce.json'))
fills['t_fill'] = [ (c.get('TOBp') or {}).get('t_fill') for c in cruce ]
fills['huella_acc'] = [h['acc_t'] for h in fills.huella]
fills['huella_tok'] = [h['tok_t'] for h in fills.huella]
fills['huella_side'] = [h['side_t'] for h in fills.huella]
print('fills', len(fills), 'con t_fill', fills.t_fill.notna().sum(), 'dias', fills.fecha.str[:10].value_counts().sort_index().to_dict())
tk = pd.read_csv(DL + 'tokens.csv', header=None, names=['token', 'tid', 'coin', 'mid', 'cierre', 'lado'], dtype={'token': str})
print('tokens', len(tk), tk.cierre.min(), tk.cierre.max())
fills = fills.merge(tk[['token', 'tid', 'mid', 'lado']], left_on='tok_x', right_on='token', how='left')
print('fills con tid', fills.tid.notna().sum())
res = []
for d in sorted(fills.fecha.str[:10].unique()):
    r = pd.read_pickle(DL + f'r_{d}.pkl'); f = fills[fills.fecha.str[:10] == d]
    ok = 0; multi = 0; none = 0
    for i, x in f.iterrows():
        c = r[(r.tid == x.tid) & (np.abs(r.q - x.precio) < 1e-6)]
        if pd.notna(x.t_fill): c2 = c[np.abs(c.r - x.t_fill) <= 2000]
        else: c2 = c.iloc[0:0]
        if len(c2) == 1: ok += 1
        elif len(c2) > 1: multi += 1
        else: none += 1
    print(d, 'fills', len(f), 'match unico', ok, 'multiples', multi, 'ninguno', none, 'r filas', len(r))
