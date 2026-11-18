#!/usr/bin/env python3
"""v8_hazard.py -- POST HOC DESCRIPTIVO (no prerregistrado): ¿la demanda tomadora AJENA reciente (calldata, tx sin filas nuestras, eq<=L, en [t_arr-30 s, t_arr))
anticipa los rellenos que ningun print hace visibles? Compara P(relleno real) y P(relleno 'invisible' = FN de DEMr_COLA_C150) con/sin esa demanda. Solo calculo."""
import glob, os, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; FLOOR = 1e-3
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out/V5_DEM_*_2026-10-2?.pkl'))], ignore_index=True)
EV = {d: pd.read_pickle(H + f'out/DEMEV_{d}.pkl') for d in R.dia.unique()}
f = []
for r in R.itertuples():
    e = EV[r.dia]; e = e[(e.k == r.k) & (e.dec == 'ok') & (e.f_own <= 0) & (e.t >= r.t_arr - 30000) & (e.t < r.t_arr)] if r.k == r.k else e.iloc[0:0]
    f.append(dict(n_dem=len(e), n_dem_L=int((e['eq'] <= r.L + 0.0049).sum())))
R = pd.concat([R, pd.DataFrame(f)], axis=1); R['dem'] = R.n_dem_L > 0
R['inv'] = (R.real_fill == 1) & (R.DEMr_COLA_C150_f_q < FLOOR)
out = {}
for k, g in R.groupby('dem'):
    out[str(k)] = dict(n=len(g), real=int(g.real_fill.sum()), p_real=round(g.real_fill.mean(), 4), inv=int(g.inv.sum()), p_inv=round(g.inv.mean(), 4), dias=g.groupby('dia').real_fill.mean().round(3).to_dict())
json.dump(out, open(H + 'v8_hazard.json', 'w'), indent=1); print(json.dumps(out, indent=1))
