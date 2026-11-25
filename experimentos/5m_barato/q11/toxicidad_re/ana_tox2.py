#!/usr/bin/env python3
"""RE-Q11 toxicidad parte 2 (05-Nov, EXPLORATORIO, post hoc declarado sobre la parte 1): (a) geometria en el ARMADO (bid(t_arr)-L) en G0;
(b) PG_O50 vs G0 y GEO6 en los 7 dias OOS: quitados/anadidos, por lado/moneda/T/rel_arm; (c) sensibilidad tamano q:=min(q, sh_tx); (d) lado por dia."""
import os, glob, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
H = os.path.dirname(os.path.abspath(__file__)) + '/'; BC = H + '../barrido_corr/out/'
A = pd.read_pickle(H + 'out/TOX.pkl'); rng = np.random.default_rng(11)
def ev(x): c = x.cost.sum(); return x.pnl.sum() / c if c > 0 else np.nan
def dec(x):
    c = x.cost.sum(); return f"n {len(x)} pnl {x.pnl.sum():+.1f} ev {ev(x):+.3f} desc {(x.q*(x.m0-x.L)).sum()/c:+.3f} info {(x.q*(x.gana-x.m0)).sum()/c:+.3f} cierres {x.fin.nunique()} dias+ {int((x.groupby('dia').pnl.sum()>0).sum())}/{x.dia.nunique()}"
A['rel_arm'] = A.arr_bid - A.L
print('== (a) G0 por geometria en el ARMADO (bid en t_arr - L), descomposicion descuento/informacion (m0 = mid tf-300)')
A['ra'] = pd.cut(A.rel_arm, [-1, -0.005, 0.005, 0.035, 0.055, 1], labels=['encima', 'en_bid', '1-3c', '4-5c', '>=6c'])
for v, x in A.groupby('ra', observed=True): print(f'  arm {v}:', dec(x))
print('  arm NaN:', dec(A[A.rel_arm.isna()]) if A.rel_arm.isna().any() else 0)
print('  cruce arm x tf-300:'); print(pd.crosstab(A.ra, A.relb))
print('\n== (c) tamano: q:=min(q, sh_tx) (cota sup del tamano real si la cinta es la del tomador)')
B = A.copy(); B['q'] = np.minimum(B.q, B.sh_tx); B['cost'] = B.q * B.L; B['pnl'] = B.q * (B.gana - B.L) + B.q * 0.2 * 0.07 * B.L * (1 - B.L)
for nm, x, y in (('G0', A, B), ('arm<6c (quitados GEO6 aprox)', A[A.rel_arm < 0.055], B[B.rel_arm < 0.055]), ('arm>=6c', A[A.rel_arm >= 0.055], B[B.rel_arm >= 0.055])):
    print(f'  {nm}: EV {ev(x):+.3f} pnl {x.pnl.sum():+.1f} -> capado EV {ev(y):+.3f} pnl {y.pnl.sum():+.1f}')
print('\n== (d) lado por dia (pnl G0)'); print(A.pivot_table(index='lado', columns='dia', values='pnl', aggfunc='sum').round(1).to_string())
# (b) PG_O50
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(BC + 'RC5c_*.pkl'))], ignore_index=True)
R5d = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(BC + 'RC5d_*.pkl'))], ignore_index=True)
D7 = sorted(R.dia.unique()); print('\n== (b) dias OOS', D7)
key = lambda x: list(zip(x.k, x.L.round(2), x.tf))
G0 = A[A.dia.isin(D7)].copy(); G0['key'] = key(G0)
for v, src in (('PG_O50', R), ('PG_B50', R), ('GEO6', R5d), ('GEO6_T120', R5d), ('PGI_O50', R)):
    P = src[(src['var'] == v) & src.dia.isin(D7)].copy(); P['key'] = key(P); kp = set(P.key); k0 = set(G0.key)
    qu = G0[~G0.key.isin(kp)]; co = G0[G0.key.isin(kp)]; an = P[~P.key.isin(k0)]
    print(f'{v}: rellenos {len(P)} pnl {P.pnl.sum():+.1f} EV {ev(P):+.3f} | quitados {len(qu)} pnl {qu.pnl.sum():+.1f} EV {ev(qu):+.3f} | anadidos {len(an)} pnl {an.pnl.sum():+.1f} EV {ev(an):+.3f} | Delta {P.pnl.sum()-G0.pnl.sum():+.1f}')
    print('   quitados:', dec(qu)); print('   conservados:', dec(co))
    for col in ('lado', 'act'):
        print(f'   quitados por {col}:', {a: (len(x), round(x.pnl.sum(), 1)) for a, x in qu.groupby(col)}, '| conservados:', {a: (len(x), round(x.pnl.sum(), 1)) for a, x in co.groupby(col)})
    print('   quitados por arm:', {str(a): (len(x), round(x.pnl.sum(), 1)) for a, x in qu.groupby('ra', observed=True)}, '| T<150:', (len(qu[qu['T'] < 150]), round(qu[qu['T'] < 150].pnl.sum(), 1)))
# solapamiento PG_O50 vs GEO6 y PG_O50 menos GEO6
P1 = R[(R['var'] == 'PG_O50') & R.dia.isin(D7)].copy(); P1['key'] = key(P1); P2 = R5d[(R5d['var'] == 'GEO6') & R5d.dia.isin(D7)].copy(); P2['key'] = key(P2)
qO = set(G0.key) - set(P1.key); q6 = set(G0.key) - set(P2.key)
sol = G0[G0.key.isin(qO - q6)]; print('\n quitados por PG_O50 que GEO6 conserva:', dec(sol)); print('   por lado', {a: (len(x), round(x.pnl.sum(), 1)) for a, x in sol.groupby('lado')}, 'por T<150', (len(sol[sol['T'] < 150]), round(sol[sol['T'] < 150].pnl.sum(), 1)), 'por act', {a: (len(x), round(x.pnl.sum(), 1)) for a, x in sol.groupby('act')})
s2 = G0[G0.key.isin(q6 - qO)]; print(' quitados por GEO6 que PG_O50 conserva:', dec(s2))
# control de tendencia: si PG_O50 gana por lado, la ganancia debe concentrarse en dias en que NO pierde en G0
dd = sol.groupby('dia').pnl.sum().round(1).to_dict(); print(' pnl quitado solo-PG por dia:', dd)
print('FIN')
