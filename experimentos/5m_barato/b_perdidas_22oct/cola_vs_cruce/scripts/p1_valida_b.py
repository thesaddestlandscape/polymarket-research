import os, sys, glob, json, pandas as pd, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from evlib import fila
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
U = pd.concat([pd.read_csv(f, dtype={'mid': str}) for f in sorted(glob.glob(os.path.join(D, 'up_*.csv.gz')))])
B = U[U.es_b == 1].copy()
pos = pd.read_csv(os.path.join(D, '../../../contabilidad_wallet_dedicada/posiciones.csv')); pos = pos[pos.tanda_B.notna()]
print('posiciones B', len(pos), 'liquidadas', pos.estado.str.startswith('liquidada').sum(), 'unidades B clasificadas', len(B), 'con desenlace', B.gana.notna().sum())
# slug de B: coin-updown-5m-(fin-300)
B['mercado'] = B.act.str.lower() + '-updown-5m-' + (B.fin - 300).astype(int).astype(str); B['outcome'] = np.where(B.lado == 'YES', 'Up', 'Down')
falt = set(zip(pos.mercado, pos.outcome)) - set(zip(B.mercado, B.outcome)); print('posiciones sin clasificar', len(falt), sorted(falt)[:10])
ub = pd.read_csv(os.path.join(D, '../../salida/datos/unidades_b.csv'))
r3 = pd.read_csv(os.path.join(D, '../../r3_escalado/datos/b_real_r3.csv'))
X = B.merge(ub[['mercado', 'outcome', 'tras_cancel', 'n_tardios', 'espera_s', 't_det', 'n_rellenos']], on=['mercado', 'outcome'], how='left')
X = X.merge(r3[['mercado', 'print', 'V1_lt']], on='mercado', how='left')
X['ws'] = np.where(X['print'] != 1, 'sin_print', np.where(X.V1_lt > 0, 'cruce_ws', 'cola_ws'))
K = 'cl_h1_0.005'
print('\nconcordancia clase on-chain (H1) x clase WS r3:'); print(pd.crosstab(X[K], X.ws, margins=True))
print('\nH0 x WS'); print(pd.crosstab(X['cl_h0_0.005'], X.ws))
print('\nclase x tras_cancel'); print(pd.crosstab(X[K], X.tras_cancel.astype(str), margins=True))
print('\nclase x relleno tardio (n_tardios>0)'); print(pd.crosstab(X[K], (X.n_tardios > 0), margins=True))
X['lag_det'] = X.t_det - X.ts   # deteccion - hora de bloque
print('\ndeteccion - bloque (s) por clase'); print(X.groupby(K).lag_det.describe()[['count', '50%', '25%', '75%']])
print('\nespera_s (edad de la orden al relleno) por clase'); print(X.groupby(K).espera_s.describe()[['count', '50%', '25%', '75%']])
print('\nhit/EV por clase y tras_cancel')
X = X[X.gana.notna()]; X['cierre'] = X.fin; X['p'] = X.pc
R = []
for tc in (True, False):
    for c in ('C1', 'C2', 'C3'):
        g = X[(X.tras_cancel == tc) & (X[K] == c)]
        if len(g): R.append(fila(g, f'tras_cancel={tc} {c}'))
print(pd.DataFrame(R).drop(columns=['por_dia']).to_string(index=False))
X.to_csv(os.path.join(D, 'b_clase.csv'), index=False)
