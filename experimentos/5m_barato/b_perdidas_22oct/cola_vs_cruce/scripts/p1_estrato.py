import os, sys, glob, pandas as pd, numpy as np
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
U = pd.concat([pd.read_csv(f, dtype={'mid': str}) for f in sorted(glob.glob(os.path.join(D, 'up_*.csv.gz')))])
U = U[(U.gana.notna()) & (U.es_b == 0)].copy()
U['tr'] = pd.cut(U.pc, [0.10, 0.15, 0.20, 0.25, 0.30]).astype(str); U['tT'] = pd.cut(U['T'], [60, 120, 180, 240, 300]).astype(str)
for K in ('cl_h0_0.005', 'cl_h1_0.005', 'cl_h5_0.005'):
    U['CR'] = np.where(U[K] == 'C3', 'COLA', 'CRUCE')
    out = []
    for dia, X in list(U.groupby('dia')) + [('TODO', U)]:
        g = X.groupby(['act', 'tr', 'tT', 'CR'])[['pnl', 'coste']].sum().unstack()
        g = g.dropna(); w = g[('coste', 'COLA')] + g[('coste', 'CRUCE')]
        d = g[('pnl', 'COLA')] / g[('coste', 'COLA')] - g[('pnl', 'CRUCE')] / g[('coste', 'CRUCE')]
        out.append((dia, round((d * w).sum() / w.sum(), 3)))
    print(K, 'diferencia COLA-CRUCE estratificada (moneda x tramo pc x tramo T), por dia:', out)
