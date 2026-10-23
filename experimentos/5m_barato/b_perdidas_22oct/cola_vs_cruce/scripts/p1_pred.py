import os, sys, glob, pandas as pd, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from evlib import fila
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
U = pd.concat([pd.read_csv(f, dtype={'mid': str}) for f in sorted(glob.glob(os.path.join(D, 'up_*.csv.gz')))])
U = U[U.gana.notna()].copy(); U['cierre'] = U.fin; U['p'] = U.pc
K = 'cl_h1_0.005'; U['C2'] = (U[K] == 'C2').astype(int); U['CR'] = (U[K] != 'C3').astype(int)
U['per'] = np.where(U.dia <= '2026-10-19', 'A17-19', 'B20-22')
P = U[U.es_b == 0]
def auc(y, x):
    m = np.isfinite(x); y = y[m]; x = x[m]
    if y.sum() == 0 or y.sum() == len(y): return np.nan
    r = pd.Series(x).rank().values; n1 = y.sum(); n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)
print('AUC (prediccion de C2 / de CRUCE) por periodo; >0,5 = valor alto -> mas C2')
for f in ('dist', 'vol30', 'lvl15', 'db30', 'bs6', 'T', 'pc', 'edad6'):
    s = []
    for per in ('A17-19', 'B20-22'):
        X = P[P.per == per]; s.append(f"{per} C2 {auc(X.C2.values, X[f].values.astype(float)):.3f} CR {auc(X.CR.values, X[f].values.astype(float)):.3f}")
    print(f'{f:6s}', ' | '.join(s))
P = P.copy(); P['dist_b'] = pd.cut(P.dist, [-1, -0.005, 0.005, 0.015, 0.025, 1], labels=['mejora(<0)', 'top(0)', '1tick', '2ticks', '>=3ticks'])
print('\nPOR DISTANCIA AL TOP (bid en ts-6 s menos pc)')
R = []
for per in ('A17-19', 'B20-22', 'TODO'):
    X = P if per == 'TODO' else P[P.per == per]
    for b, g in X.groupby('dist_b', observed=True):
        f = fila(g, f'{per} {b}'); f['cuota_C2'] = round(g.C2.mean(), 3); f['cuota_CR'] = round(g.CR.mean(), 3); f['cuota_coste'] = round(g.coste.sum() / X.coste.sum(), 3); R.append(f)
print(pd.DataFrame(R).drop(columns=['por_dia', 'p_med']).to_string(index=False))
