#!/usr/bin/env python3
"""t0_tune_latencias.py: SOLO TUNE (20-21 Oct). Fidelidad de la regla mecanica sobre las ordenes reales de B y distribuciones de
latencia (react = intencion_cancel - primer cambio de objetivo en el libro q grabado; post_half = t_ini - t_dec; asentar = siguiente t_dec
- intencion_cancel en la misma puja). Salida: tune_latencias.json + t0_salida.txt."""
import json, numpy as np, pandas as pd
from v3lib import *
B = pd.read_parquet(DL + 'ordenes_b.parquet'); B = B[B.dia.isin(['2026-10-20', '2026-10-21'])].copy()
R = []
for dia in ('2026-10-20', '2026-10-21'):
    D = Dia(dia); g = B[B.dia == dia]; Ls = {}
    for r in g.itertuples():
        L = Ls.setdefault(r.tok, Libro(D, r.tok, K[r.coin]))
        td = r.t_dec * 1000; cie = r.cie * 1000
        p0, v0 = L.obj_at(td)
        tch = L.primer_cambio(td, r.precio, cie - 60000)
        R.append(dict(oid=r.oid, puja=r.puja, dia=dia, coin=r.coin, n_orden=r.n_orden, precio=r.precio, obj_dec=p0, val_dec=v0, td=td,
                      ti=r.t_ini * 1000, tci=(r.t_cancel_int * 1000 if r.t_cancel_int == r.t_cancel_int else np.nan), tch=(tch if tch is not None else np.nan),
                      tfin=r.t_fin * 1000, cie=cie, fill=r.fill))
R = pd.DataFrame(R).sort_values(['puja', 'td'])
R['obj_ok'] = (np.abs(R.obj_dec - R.precio) < 1e-9)
R['react'] = R.tci - R.tch
R['post_half'] = R.ti - R.td
R['next_td'] = R.groupby('puja').td.shift(-1); R['asentar'] = R.next_td - R.tci
out = {}
print('ordenes TUNE', len(R), 'objetivo(libro q en t_dec)==precio:', round(R.obj_ok.mean(), 3))
x = R[R.fill == 0]
print('no rellenas con cancel', x.tci.notna().sum(), 'con cambio predicho', x.tch.notna().sum())
for nm, s in [('react_todas', R.react), ('react_norell', x.react)]:
    s = s.dropna(); print(nm, len(s), 'pct 5/25/50/75/95', np.percentile(s, [5, 25, 50, 75, 95]).round(0), '|react|<=300ms', round((s.abs() <= 300).mean(), 3), '<-300', round((s < -300).mean(), 3), '>1000', round((s > 1000).mean(), 3))
s = R.post_half.dropna(); print('post_half', np.percentile(s, [5, 50, 95]).round(0))
s = R.asentar.dropna(); print('asentar', len(s), np.percentile(s, [5, 25, 50, 75, 95]).round(0))
# motivo de fin aproximado de las no predichas
y = x[x.tci.notna()]
print('no rellenas: cancel real sin cambio predicho antes del T-60:', int(y.tch.isna().sum()), '; cancel real cerca de T-60 (cie-tci<62s):', int(((y.cie - y.tci) < 62000).sum()))
R.to_parquet('t0_tune_ordenes.parquet')
sel = lambda s: [float(v) for v in s.dropna().values]
json.dump(dict(react=sel(x.react[(x.react > -300) & (x.react < 3000)]), post_half=sel(R.post_half), asentar=sel(R.asentar[(R.asentar > 0) & (R.asentar < 30000)])), open('tune_latencias.json', 'w'))
