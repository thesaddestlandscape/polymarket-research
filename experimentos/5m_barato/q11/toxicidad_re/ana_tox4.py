#!/usr/bin/env python3
"""RE-Q11 parte 4 (05-Nov, DESCRIPTIVO, dias GASTADOS, NO cuenta para ningun prereg): (a) P-C en G0: descomposicion descuento/informacion y markouts (AS vs direccion);
(b) dosis-respuesta del re-armado tras salto en dec2 (T1_r0 / T1 r1000 / T1_r2000, G0, PLA_T1) para dimensionar la variante T1 calma 3 s; (c) PG_O50 Delta por dia y por lado en dias con NO>=0."""
import os, glob, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
H = os.path.dirname(os.path.abspath(__file__)) + '/'; BC = H + '../barrido_corr/out/'
DEC = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/out/'
A = pd.read_pickle(H + 'out/TOX.pkl'); rng = np.random.default_rng(5)
def ev(x): c = x.cost.sum(); return x.pnl.sum() / c if c > 0 else np.nan
def dec(x):
    c = x.cost.sum(); r = f"n {len(x)} pnl {x.pnl.sum():+.1f} ev {ev(x):+.3f} desc {(x.q*(x.m0-x.L)).sum()/c:+.3f} info {(x.q*(x.gana-x.m0)).sum()/c:+.3f}"
    for h in ('p1', 'p10', 'p60'):
        m = (x[h + '_bid'] + x[h + '_ask']) / 2; o = m.notna(); r += f" mk_{h} {(x.q[o]*(m[o]-x.m0[o])).sum()/x.cost[o].sum():+.3f}"
    return r + f" cierres {x.fin.nunique()} dias+ {int((x.groupby('dia').pnl.sum()>0).sum())}/{x.dia.nunique()}"
N = A[A.lado == 'NO'].copy(); r1 = -N.x_cl_rpre1h; r4 = -N.x_cl_rpre5h   # deshacer el signo por lado (NO: ss=-1) -> rasgo crudo del prereg
ok = r1.notna() & r4.notna(); Hs = ok & (r1 > 0) & (r4 < 0); Cs = ok & ~Hs
print('== (a) P-C en G0 (lado NO, dias gastados): sin rasgo', int((~ok).sum()))
print('  H (r1>0, r4<0):', dec(N[Hs])); print('  C:', dec(N[Cs]))
print('  H por arm>=6c:', {a: dec(x) for a, x in N[Hs].groupby(N[Hs].arr_bid - N[Hs].L >= 0.055)})
X = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(DEC + 'dec2_2026-1*.pkl')) if f[-14:-4] <= '2026-11-04'])
print('\n== (b) dec2 dias', sorted(X.dia.unique()))
for v in ('G0', 'T1_r0', 'T1', 'T1_r2000', 'T1_c300', 'T1_c1000', 'PLA_T1'):
    x = X[X['var'] == v]; z = x[x.lagj <= 3000]; dd = x.groupby('dia').pnl.sum(); s2 = dd.sort_values(ascending=False).iloc[2:].sum() / x[x.dia.isin(dd.sort_values(ascending=False).index[2:])].cost.sum()
    print(f'  {v:9s} n {len(x):5d} pnl {x.pnl.sum():+7.1f} EV {ev(x):+.3f} sin2mej {s2:+.3f} | lagj<=3s n {len(z)} EV {ev(z):+.3f} pnl {z.pnl.sum():+.1f} | lagj<=1s n {(x.lagj<=1000).sum()}')
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(BC + 'RC5c_*.pkl'))], ignore_index=True)
P = R[R['var'] == 'PG_O50']; G = R[R['var'] == 'G0']
t = pd.DataFrame({'PG': P.groupby(['dia', 'lado']).pnl.sum(), 'G0': G.groupby(['dia', 'lado']).pnl.sum()}).fillna(0); t['D'] = t.PG - t.G0
print('\n== (c) PG_O50 vs G0 por dia x lado (pnl)'); print(t.round(1).unstack('lado').to_string())
