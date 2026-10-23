"""Fidelidad del simulador E1Q frente a B REAL en los mismos mercados (MEDIR 20-22 Oct): tasa de relleno por puja, acuerdo puja a puja,
mezcla de clases (sim X1/X2/X3 vs on-chain C1/C2/C3) y EV de los rellenos. Descriptivo."""
import json, os, sys, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from evlib import fila
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
X = pd.read_csv(os.path.join(D, 'e1q_MEDIR.csv.gz'), dtype={'mid': str}); X = X[X.alloc == 'prop']
T = pd.concat([pd.read_csv(os.path.join(D, f'tok_2026-10-{d}.csv'), dtype={'mid': str}) for d in (20, 21, 22)]).drop_duplicates(['act', 'mid'])
mid = {(r.act, int(r.fin)): r.mid for r in T.itertuples()}
pj = {}
for l in open('/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'):
    try: d = json.loads(l)
    except Exception: continue
    if d.get('real') and d.get('tipo') == 'puja_fin':
        coin, _, _, st = d['slug'].split('-'); m = mid.get((coin.upper(), int(st) + 300))
        if m: pj[m] = dict(real_fill=int(bool(d.get('rellenos'))), real_lado='Y' if d['lado'] == 'YES' else 'N', fin_puja=d.get('fin_puja'))
R = pd.DataFrame.from_dict(pj, orient='index'); R.index.name = 'mid'
bc = pd.read_csv(os.path.join(D, 'b_clase.csv'), dtype={'mid': str}).drop_duplicates('mid').set_index('mid')
print('pujas B real con mercado en el simulador:', len(R.index.intersection(X.mid.unique())), 'de', len(R))
out = []
for v in X['var'].unique():
    V = X[X['var'] == v].set_index('mid'); J = R.join(V[['fill', 'lado', 'clase', 'p', 'acc', 'gana']], how='inner')
    J = J[J.lado == J.real_lado]
    a = (J.fill == J.real_fill)
    out.append(dict(var=v, n=len(J), tasa_sim=round(J.fill.mean(), 3), tasa_real=round(J.real_fill.mean(), 3),
                    acuerdo=round(a.mean(), 3), p_sim_dado_real=round(J[J.real_fill == 1].fill.mean(), 3), p_real_dado_sim=round(J[J.fill == 1].real_fill.mean(), 3)))
print(pd.DataFrame(out).to_string(index=False))
print('\nmezcla on-chain de B real (C1/C2/C3, coste):', (bc.groupby('cl_h1_0.005').coste.sum() / bc.coste.sum()).round(3).to_dict())
for v in ('BASE', 'BREAL', 'B_FIEL', 'BF_RAPIDO'):
    V = X[(X['var'] == v) & (X.fill == 1)].copy(); V['coste'] = V.acc * V.p; V['pnl'] = V.acc * V.gana - V.coste; V['cierre'] = V.fin
    print(v, 'mezcla sim', (V.groupby('clase').coste.sum() / V.coste.sum()).round(3).to_dict(), 'EV', round(V.pnl.sum() / V.coste.sum(), 3), 'n', len(V))
