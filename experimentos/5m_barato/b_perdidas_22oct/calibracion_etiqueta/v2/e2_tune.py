#!/usr/bin/env python3
"""e2_tune.py: SELECCION SOLO EN TUNE (20-21 Oct) de (e,f,g) de la Capa 1 + plantillas de puja + rho_off (PREREG_V2). Salida datos/tune_sel.json"""
import sys, json, itertools, numpy as np, pandas as pd
sys.path.insert(0, '.'); from v2lib import *
B = pd.read_parquet(DL + 'ordenes_b.parquet'); B = B[B.dia.isin(['2026-10-20', '2026-10-21'])].copy()
B['ti'] = B.t_ini * 1000; B['tf'] = B.t_fin * 1000; B['Qv'] = B.cola.fillna(0.0)
# cache de consumos (hasta tf+1000)
C = {}
for dia in ('2026-10-20', '2026-10-21'):
    D = Dia(dia)
    for r in B[B.dia == dia].itertuples(): C[r.oid] = D.consumos(r.tok, r.precio, r.ti, r.tf + 1000)
EV = (0, 100, 250, 500, 1000); FV = (0.0, 0.25, 0.5, 1.0); GV = (1.0, 0.5); res = []
for e, f, g in itertools.product(EV, FV, GV):
    fl = np.array([lleno(C[r.oid], r.ti, r.tf, e, f, g, r.size, r.Qv) is not None for r in B.itertuples()]).astype(int)
    y = B.fill.values; tp = int(((fl == 1) & (y == 1)).sum()); fp = int(((fl == 1) & (y == 0)).sum()); fn = int(((fl == 0) & (y == 1)).sum())
    pv = pd.Series(fl, index=B.index).groupby(B.puja).max(); pr = B.groupby('puja').fill_puja.max()
    Po, Pr = fl.mean(), y.mean(); Pp, Ppr = pv.mean(), pr.mean()
    prec = tp / max(tp + fp, 1); rec = tp / max(tp + fn, 1)
    err = abs(math.log(max(Po, 1e-9) / Pr)) + abs(math.log(max(Pp, 1e-9) / Ppr))
    res.append(dict(e=e, f=f, g=g, P_orden=Po, P_orden_real=Pr, P_puja=Pp, P_puja_real=Ppr, recall=rec, precision=prec, err=err))
R = pd.DataFrame(res); R.to_csv(DL + 'v2/tune_grid.csv', index=False)
ok = R[R.precision >= 0.80].copy(); ok['rp'] = ok.recall * ok.precision
best = ok.sort_values(['err', 'rp', 'e'], ascending=[True, False, True]).iloc[0].to_dict()
print(R.round(3).sort_values('err').head(8).to_string()); print('SELECCION', best)
# rho_off en TUNE: mediana cola/bs por off_c
rho = {}
for off in (0, 1, 2):
    g_ = B[(B.off_c == off) & (B.bs > 0) & B.cola.notna()]; rho[off] = float(np.median(g_.cola / g_.bs)) if len(g_) >= 20 else (1.0 if off == 0 else None)
# plantillas: por puja, (offset ms, vida ms, off_c)
T = []
for k, g_ in B.sort_values('ti').groupby('puja'):
    g_ = g_[g_.off_c.notna()]
    if len(g_) == 0: continue
    t0 = g_.ti.min(); T.append([(float(r.ti - t0), float(r.tf - r.ti), int(r.off_c)) for r in g_.itertuples()])
json.dump(dict(sel=best, rho=rho, plantillas=T, n_pujas_tune=int(B.puja.nunique()), n_ordenes_tune=len(B)), open('datos_tune_sel.json', 'w'))
print('rho', rho, 'plantillas', len(T))
