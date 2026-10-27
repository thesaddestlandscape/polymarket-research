#!/usr/bin/env python3
"""e5_placebo_capa1.py: (post-hoc, descriptivo, NO es criterio del PREREG_V2) placebo de la Capa 1: prints desplazados +-90 s con las ventanas reales de TEST; y por-dia + cobertura de pujas."""
import sys, json, numpy as np, pandas as pd
sys.path.insert(0, '.'); from v2lib import *
S = json.load(open('datos_tune_sel.json')); E_, F_, G_ = int(S['sel']['e']), S['sel']['f'], S['sel']['g']
B = pd.read_parquet(DL + 'ordenes_b.parquet'); B = B[B.dia.isin(['2026-10-22', '2026-10-23'])].copy(); B['ti'] = B.t_ini * 1000; B['tf'] = B.t_fin * 1000
R = []
for dia in ('2026-10-22', '2026-10-23'):
    D = Dia(dia)
    for r in B[B.dia == dia].itertuples():
        row = dict(puja=r.puja, dia=dia, fill=r.fill, fp=r.fill_puja)
        for nm, sh in (('v', 0), ('pm', -90000), ('pp', 90000)):
            c = [(t - sh, sz, sw) for (t, sz, sw) in D.consumos(r.tok, r.precio, r.ti + sh, r.tf + E_ + sh)]; row[nm] = int(lleno(c, r.ti, r.tf, E_, F_, G_, r.size, 0.0) is not None)
        R.append(row)
R = pd.DataFrame(R)
for nm in ('v', 'pm', 'pp'):
    tp = ((R[nm] == 1) & (R.fill == 1)).sum(); print(nm, 'P_orden %.4f' % R[nm].mean(), 'recall %.3f' % (tp / R.fill.sum()), 'precision %.3f' % (tp / max(R[nm].sum(), 1)), 'P_puja %.3f' % R.groupby('puja')[nm].max().mean())
pjv = R.groupby('puja').agg(v=('v', 'max'), fp=('fp', 'max')); print('pujas v vs real: ambas', int(((pjv.v == 1) & (pjv.fp == 1)).sum()), 'solo v', int(((pjv.v == 1) & (pjv.fp == 0)).sum()), 'solo real', int(((pjv.v == 0) & (pjv.fp == 1)).sum()), 'ninguna', int(((pjv.v == 0) & (pjv.fp == 0)).sum()))
for d, g in R.groupby('dia'): print(d, 'ordenes', len(g), 'real', g.fill.sum(), 'v', g.v.sum(), 'P_orden real %.3f v %.3f' % (g.fill.mean(), g.v.mean()), 'pujas', g.puja.nunique())
