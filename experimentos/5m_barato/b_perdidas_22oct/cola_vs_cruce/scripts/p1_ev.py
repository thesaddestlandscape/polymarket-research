import os, sys, glob, pandas as pd, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from evlib import fila, boot
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
U = pd.concat([pd.read_csv(f, dtype={'mid': str}) for f in sorted(glob.glob(os.path.join(D, 'u_*.csv.gz')))])
U = U[U.gana.notna()].copy(); U['cierre'] = U.fin; U['p'] = U.pc
U['tramo'] = pd.cut(U.pc, [0.10, 0.15, 0.20, 0.25, 0.30]).astype(str)
K = sys.argv[1] if len(sys.argv) > 1 else 'cl_h1_0.005'
U['cl'] = U[K]; U['CR'] = np.where(U.cl == 'C3', 'COLA', 'CRUCE')
P = U[U.es_b == 0]; B = U[U.es_b == 1]
pd.set_option('display.width', 250)
def tabla(X, titulo):
    R = [fila(X, 'TODOS')] + [fila(X[X.cl == c], c) for c in ('C1', 'C2', 'C3')] + [fila(X[X.CR == c], c) for c in ('COLA', 'CRUCE')]
    print('==', titulo, K); print(pd.DataFrame(R).drop(columns=['por_dia']).to_string(index=False))
def dif(X, by=None):
    # diferencia COLA-CRUCE por dia, IC90 bootstrap por dia de la diferencia
    g = X.groupby(['dia', 'CR'])[['pnl', 'coste']].sum().unstack()
    e = (g['pnl'] / g['coste']); d = (e['COLA'] - e['CRUCE']).dropna()
    rng = np.random.default_rng(20261022); dd = g.index.values
    vals = []
    for _ in range(2000):
        s = rng.integers(0, len(dd), len(dd)); gg = g.iloc[s].sum()
        vals.append(gg[('pnl', 'COLA')] / gg[('coste', 'COLA')] - gg[('pnl', 'CRUCE')] / gg[('coste', 'CRUCE')])
    return d.round(3).tolist(), np.percentile(vals, [5, 95]).round(3)
tabla(P, 'POBLACION 17-22')
print('dif COLA-CRUCE pob por dia', dif(P))
for co in ('ETH', 'SOL', 'XRP'):
    X = P[P.act == co]; print(co, 'COLA', fila(X[X.CR == 'COLA'], '')['ev'], 'CRUCE', fila(X[X.CR == 'CRUCE'], '')['ev'], 'dif por dia/IC90', dif(X))
for tr in sorted(P.tramo.unique()):
    X = P[P.tramo == tr]; print(tr, 'COLA', fila(X[X.CR == 'COLA'], '')['ev'], 'CRUCE', fila(X[X.CR == 'CRUCE'], '')['ev'], 'n', (X.CR == 'COLA').sum(), (X.CR == 'CRUCE').sum(), 'dif IC90', dif(X)[1])
print('cuota COLA en coste pob', round(P[P.CR == 'COLA'].coste.sum() / P.coste.sum(), 3), 'hit COLA/CRUCE', round(P[P.CR=='COLA'].gana.mean(),3), round(P[P.CR=='CRUCE'].gana.mean(),3), 'p medio', round(P[P.CR=='COLA'].pc.mean(),3), round(P[P.CR=='CRUCE'].pc.mean(),3))
tabla(B, 'B REAL (unidad = primera 5 acc de la posicion)')
