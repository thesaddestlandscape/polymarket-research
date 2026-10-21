#!/usr/bin/env python3
"""concilia_escalado.py (H23 v3, tarea 1) -- concilia las cifras de STATUS (A +0,393 / ~0 sin 2 mejores 'con 5 acc') con v2 (A r0 +0,99 / +0,373 / r1500 +0,595)
re-dimensionando las filas del replay v2 (celda central: cola base, alta 79, cancel 60, stake 2 EUR) al TAMANO REAL del paquete (5 acc o ceil(1/p), tope 10)
y al UNIVERSO EJECUTABLE (p en [0,10;0,60], T>12 s). Escalado LINEAL del relleno (lleno_new = lleno*need_real/need_2EUR): aproximacion (exacta si el relleno fue completo);
la version exacta es la re-simulacion con sizing real (h23_sim_v3.py). Solo lectura. Uso: python3 -I concilia_escalado.py [dir_v2]"""
import glob, math, sys
import numpy as np, pandas as pd
O = sys.argv[1] if len(sys.argv) > 1 else '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/'
M = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'v2_BTC_20*.csv'))], ignore_index=True)
M['g'] = M.gana.map({True: 1.0, False: 0.0, 'True': 1.0, 'False': 0.0})
C = M[(M.cola == 'base') & (M.lat_post == 79) & (M.lat_cancel == 60) & (M.mult == 1.0) & (M.lleno > 0) & M.g.notna()].copy()
C['p0'] = C.coste / C.lleno
def real_need(p): return min(10.0, 5.0 if 5 * p >= 1 - 1e-9 else float(math.ceil(1 / p - 1e-9)))   # tamano H47: size_base 5, nocional>=1 -> ceil(1/p), tope 10
C['T_rel'] = C.cierre - C.t_rel / 1000.0
C['rebate_u'] = C.rebate / C.lleno
rng = np.random.default_rng(7)
def estat(f, lleno_col):
    if not len(f): return 'n=0'
    f = f.assign(L=f[lleno_col]); f['c'] = f.L * f.p0; f['pnl'] = f.L * f.g - f.c + f.rebate_u * f.L
    d = f.groupby('dia').agg(p=('pnl', 'sum'), c=('c', 'sum')); D = d.values
    b = [(lambda k: k[:, 0].sum() / k[:, 1].sum())(D[rng.integers(0, len(D), len(D))]) for _ in range(3000)]
    s2 = d.sort_values('p', ascending=False).iloc[2:]
    return 'n=%2d dias=%2d(+%d) PnL=%+7.2f coste=%6.2f EVpond=%+.3f EVunit=%+.3f IC90d=(%+.2f,%+.2f) sin2mejores=%+.3f (%d dias)' % (
        len(f), f.dia.nunique(), (d.p > 0).sum(), f.pnl.sum(), f.c.sum(), f.pnl.sum() / f.c.sum(), (f.pnl / f.c).mean(), np.percentile(b, 5), np.percentile(b, 95),
        (s2.p.sum() / s2.c.sum()) if len(s2) and s2.c.sum() > 0 else float('nan'), len(s2))
for brazo in ('A', 'B'):
    print(f'\n=== BRAZO {brazo}: celda central, BTC 06-18 Oct (13 dias, DESCUBRIMIENTO), 1 relleno por cierre ===')
    for var in ('r0', 'r150', 'r1500'):
        f = C[(C.brazo == brazo) & (C['var'] == var)].copy()
        f['L_2eur'] = f.lleno
        f['need_real'] = f.p0.map(real_need)
        f['L_real'] = f.need_real * np.minimum(1.0, f.lleno / f.need)       # misma FRACCION de relleno sobre un tamano real
        uni = f[(f.p0 >= 0.10 - 1e-9) & (f.p0 <= 0.60 + 1e-9) & (f.T_rel > 12)]
        print(f'{var:6s} 2 EUR  todo     : {estat(f, "L_2eur")}')
        print(f'{var:6s} 2 EUR  universo : {estat(uni, "L_2eur")}')
        print(f'{var:6s} real   todo     : {estat(f, "L_real")}')
        print(f'{var:6s} real   universo : {estat(uni, "L_real")}')
