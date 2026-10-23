#!/usr/bin/env python3
"""e2_cola.py -- diagnostico (no gate): cola delante en el POST, real (ordenes_b.cola, libro de B al decidir) vs sim (nivel de libro5 en t_dec+0,085) para ordenes emparejadas (mismo slug, mismo precio, |dt_dec|<=1 s)."""
import os, sys, json, collections
sys.dont_write_bytecode = True
import e2_engine as E
import numpy as np, pandas as pd
S = E.S; D = E.D
O = pd.read_csv(os.path.join(D, 'e2_eval_base_ordenes.csv'), dtype={'mid': str}); R = pd.read_csv(os.path.join(D, 'cal_real_pujas.csv'), dtype={'mid': str}).set_index('mid')
RO = collections.defaultdict(list)
for x in json.load(open('/root/polymarket-research-datalogs/cola_posicion/ordenes_b.json')): RO[x['slug']].append(x)
rows = []; cache = {}
for mid, g in O.groupby('mid'):
    if mid not in R.index: continue
    r = R.loc[mid]; m = E.Mkt(r.act, mid, int(r.fin))
    if m.roto: continue
    for _, s in g.iterrows():
        for x in RO.get(r.slug, ()):
            if abs(x['precio'] - s.precio) < 1e-9 and abs(x['t_dec'] - s.t_dec) <= 1.0:
                rows.append(dict(act=r.act, real=x['cola'], sim=m.nivel(s.tok, round(s.precio * 1000), int((x['t_dec'] + 0.085) * 1000)), sim_en_t_sim=m.nivel(s.tok, round(s.precio * 1000), int(s.t_live * 1000)))); break
df = pd.DataFrame(rows); print('pares', len(df))
print('mediana real', df.real.median(), 'sim al t_dec real', df.sim.median(), 'sim al t_dec sim', df.sim_en_t_sim.median())
print('razon sim/real (t_dec real) p25/p50/p75', (df.sim / df.real.replace(0, np.nan)).quantile([.25, .5, .75]).round(2).to_dict())
print('dif sim-real (acc) p25/p50/p75', (df.sim - df.real).quantile([.25, .5, .75]).round(1).to_dict(), '| frac |dif|<=2:', ((df.sim - df.real).abs() <= 2).mean().round(3), '| cola real<=5:', (df.real <= 5).mean().round(3), 'sim<=5:', (df.sim <= 5).mean().round(3))
print(df.groupby('act').apply(lambda g: pd.Series(dict(n=len(g), real=g.real.median(), sim=g.sim.median()))))
