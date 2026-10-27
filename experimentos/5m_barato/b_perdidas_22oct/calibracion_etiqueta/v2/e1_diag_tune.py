#!/usr/bin/env python3
"""e1_diag_tune.py: DIAGNOSTICO SOLO TUNE (20-21 Oct). Para las ordenes reales de B: posicion del consumo mas cercano respecto a la ventana, rellenas vs no."""
import sys, numpy as np, pandas as pd
sys.path.insert(0, '.'); from v2lib import *
B = pd.read_parquet(DL + 'ordenes_b.parquet'); out = []
for dia in sys.argv[1:]:
    assert dia in ('2026-10-20', '2026-10-21'), 'diagnostico solo TUNE'
    D = Dia(dia); g = B[B.dia == dia]
    for r in g.itertuples():
        ti, tf = r.t_ini * 1000, r.t_fin * 1000
        c = D.consumos(r.tok, r.precio, ti - 5000, tf + 5000)
        # consumo mas cercano a la ventana (distancia con signo: <0 antes de ti, 0 dentro, >0 despues de tf)
        dd = [(t - ti) if t < ti else (0 if t <= tf else t - tf) for t, sz, sw in c]
        k = int(np.argmin(np.abs(dd))) if dd else -1
        out.append(dict(oid=r.oid, dia=dia, fill=r.fill, s=r.size, vida=(tf - ti) / 1000, n_cons5=len(c), dmin=dd[k] if dd else np.nan, szmin=c[k][1] if dd else np.nan,
                        cons_in=sum(sz for t, sz, sw in c if ti <= t <= tf), nt_in=sum(1 for t, sz, sw in c if ti <= t <= tf), tsest=r.t_fin))
    print(dia, 'listo', flush=True)
X = pd.DataFrame(out); X.to_parquet(DL + 'v2/diag_tune.parquet')
for fl, g in X.groupby('fill'):
    print('fill', fl, 'n', len(g), 'con consumo dentro', (g.nt_in > 0).mean().round(3), 'con consumo (+-5s)', (g.n_cons5 > 0).mean().round(3))
    d = g.dmin.dropna(); print('  dmin ms percentiles 5/25/50/75/95', np.percentile(d, [5, 25, 50, 75, 95]).round(0), ' frac dentro', (d == 0).mean().round(3), ' antes', (d < 0).mean().round(3), ' despues', (d > 0).mean().round(3))
f = X[X.fill == 1]; print('rellenas: dist de dmin cuando fuera:', np.histogram(f.dmin[f.dmin != 0].dropna(), bins=[-5000, -2000, -1000, -500, -250, -100, 0, 100, 250, 500, 1000, 2000, 5000])[0])
