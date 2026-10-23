import csv, os, sys, pandas as pd, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from evlib import fila
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
t = pd.read_csv(os.path.join(D, 'b_tx.csv')); t = t[t.clase_tx != 'missing']
pos = pd.read_csv(os.path.join(D, '../../../contabilidad_wallet_dedicada/posiciones.csv'))
pos = pos[pos.tanda_B.notna()]
est = {(r.mercado, r.outcome): r.estado for r in pos.itertuples()}
t['estado'] = [est.get((a, b)) for a, b in zip(t.mercado, t.outcome)]
print(t.estado.value_counts(dropna=False).to_dict())
t = t[t.estado.isin(['liquidada_ganada', 'liquidada_perdida'])].copy()
t['gana'] = (t.estado == 'liquidada_ganada').astype(int); t['coste'] = t.acc * t.p; t['pnl'] = t.acc * t.gana - t.coste
t['dia'] = t.fecha.str[:10]; t['cierre'] = t.mercado.str.split('-').str[-1]; t['coin'] = t.mercado.str.split('-').str[0]
t.to_csv(os.path.join(D, 'b_tx_ev.csv'), index=False)
R = [fila(t, 'TODOS')] + [fila(t[t.clase_tx == c], c) for c in ('TX_STOP', 'TX_DEEP')]
for co in ('eth', 'sol', 'xrp'):
    for c in ('TX_STOP', 'TX_DEEP'): R.append(fila(t[(t.coin == co) & (t.clase_tx == c)], f'{co} {c}'))
print(pd.DataFrame(R).to_string())
