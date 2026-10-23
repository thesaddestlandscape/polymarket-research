#!/usr/bin/env python3
"""p2_eval.py FASE -- PREREG_P2: EV por variante (rellenos del simulador E1Q), diferencia pareada vs BASE con IC90 por dia y por cierre,
control de igual volumen (quitar al azar rellenos de BASE por dia hasta el EUR de la variante), mezcla X1/X2/X3, sin 2 mejores dias."""
import os, sys, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from evlib import fila
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
F = sys.argv[1]; SUF = sys.argv[2] if len(sys.argv) > 2 else ''; BV = sys.argv[3] if len(sys.argv) > 3 else 'BASE'
X = pd.read_csv(os.path.join(D, f'e1q_{F}{SUF}.csv.gz'), dtype={'mid': str})
X['coste'] = X.acc * X.p.fillna(0); X['pnl'] = X.acc * X.gana - X.coste; X['cierre'] = X.fin
rng = np.random.default_rng(20261022)
P = X[X.alloc == 'prop']; B = P[P['var'] == BV].set_index('mid')
print(F, 'mercados', B.shape[0], 'dias', sorted(P.dia.unique()))
R = []
for v in P['var'].unique():
    V = P[P['var'] == v]; Vf = V[V.fill == 1]; f = fila(Vf.assign(p=Vf.p), v)
    f['tasa_relleno'] = round(V.fill.mean(), 3); f['ret_coste'] = round(Vf.coste.sum() / B[B.fill == 1].coste.sum(), 3)
    mix = Vf.groupby('clase').coste.sum() / Vf.coste.sum(); f.update({f'cuota_{c}': round(mix.get(c, 0), 3) for c in ('X1', 'X2', 'X3')})
    # diferencia pareada por mercado: EV_var - EV_base, IC por dia y por cierre
    V2 = V.set_index('mid')[['pnl', 'coste']].join(B[['pnl', 'coste', 'dia', 'cierre']], rsuffix='_b')
    def dif(idx):
        s = V2.loc[idx]; return s.pnl.sum() / max(s.coste.sum(), 1e-9) - s.pnl_b.sum() / max(s.coste_b.sum(), 1e-9)
    f['dif'] = round(dif(V2.index), 4)
    for g in ('dia', 'cierre'):
        grupos = [V2.index[V2[g] == u] for u in V2[g].unique()]; vals = []
        for _ in range(1000):
            s = rng.integers(0, len(grupos), len(grupos)); vals.append(dif(np.concatenate([grupos[i] for i in s])))
        f[f'dif_ic_{g}'] = f'({np.percentile(vals,5):+.3f},{np.percentile(vals,95):+.3f})'
    f['dif_por_dia'] = [round(dif(V2.index[V2.dia == u]), 3) for u in sorted(V2.dia.unique())]
    # placebo de igual volumen: por dia, subconjunto aleatorio de rellenos BASE con el mismo EUR que la variante
    Bf = B[B.fill == 1]; obj = Vf.groupby('dia').coste.sum(); evs = []
    for _ in range(2000):
        pn = cs = 0.0
        for d, g in Bf.groupby('dia'):
            o = obj.get(d, 0.0); idx = rng.permutation(len(g)); c = g.coste.values[idx].cumsum(); m = c <= o + 1e-9
            pn += g.pnl.values[idx][m].sum(); cs += g.coste.values[idx][m].sum()
        evs.append(pn / max(cs, 1e-9))
    f['placebo_ev_med'] = round(float(np.mean(evs)), 3); f['p_placebo'] = round(float(np.mean(np.array(evs) >= f['ev'])), 3)
    R.append(f)
T = pd.DataFrame(R).drop(columns=['p_med']); pd.set_option('display.width', 300); pd.set_option('display.max_columns', 40)
print(T.to_string(index=False))
print(f'\n{BV} por clase (prop):'); Bf = P[(P['var'] == BV) & (P.fill == 1)]
print(pd.DataFrame([fila(Bf[Bf.clase == c], c) for c in ('X1', 'X2', 'X3')]).to_string(index=False))
print('\nBASE sensibilidad de la cola (lo/hi):')
for a in ('lo', 'hi'):
    Q = X[(X['var'] == 'BASE') & (X.alloc == a) & (X.fill == 1)]; print(a, fila(Q, a)['ev'], 'n', len(Q), (Q.groupby('clase').coste.sum() / Q.coste.sum()).round(3).to_dict())
for co in ('ETH', 'SOL', 'XRP'):
    s = []
    for v in P['var'].unique():
        Q = P[(P['var'] == v) & (P.fill == 1) & (P.act == co)]; s.append(f"{v} {fila(Q, v)['ev']:+.3f}(n{len(Q)})")
    print(co, ' | '.join(s))
T.to_csv(os.path.join(D, f'p2_eval_{F}{SUF}_{BV}.csv'), index=False)
