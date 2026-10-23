#!/usr/bin/env python3
"""e1_posthoc.py -- POST-HOC (no gate) sobre la regla NO elegida S1_x2_w2000 (Binance propio <=-2 bps en 2 s): volumen de controles,
EV de quitados/sustitutos, solape con R2 (bid15 mismo lado - obj <= 0,03 en el relleno) y senal en los rellenos REALES de B."""
import os, sys, math, numpy as np, pandas as pd
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(AQUI, '..', '..', 'salida', 'scripts'))
from msdata import Dia, SYM, DD as SDD
DD = os.path.join(AQUI, '..', 'datos'); DIAS = ['2026-10-17', '2026-10-18', '2026-10-19', '2026-10-20', '2026-10-21', '2026-10-22']
X = pd.concat([pd.read_csv(f'{DD}/e1_{d}.csv.gz') for d in DIAS], ignore_index=True)
X['coste'] = np.where(X.fill == 1, 5 * X.obj, 0.0); X['pnl'] = np.where(X.fill == 1, 5 * (X.gana - X.obj), 0.0)
B = X[X['var'] == 'BASE'].set_index('mid'); R = 'S1_x2_w2000'
X['per'] = np.where(X.dia <= '2026-10-19', 'DESC', 'TEST')
print('1) retencion de coste por control (DESC / TEST)')
for v in ['D100', 'INV', 'SH-60', 'SH+60', 'SH+240']:
    V = X[X['var'] == f'{R}|{v}']
    print(f'  {v:7s}', ' '.join(f"{p}: ret {V[V.per==p].coste.sum()/B[B.dia.isin(V[V.per==p].dia.unique())].coste.sum():.3f}" for p in ('DESC', 'TEST')))
V = X[X['var'] == f'{R}|D100'].set_index('mid'); b = B.loc[V.index]
rem = (b.fill == 1) & ((V.fill == 0) | (V.r != b.r)); sub = rem & (V.fill == 1)
print(f'2) quitados n={int(rem.sum())} EV {b.pnl[rem].sum()/b.coste[rem].sum():+.3f} acierto {b.gana[rem].mean():.3f} | retenidos EV {b.pnl[(b.fill==1)&~rem].sum()/b.coste[(b.fill==1)&~rem].sum():+.3f} '
      f'| sustitutos n={int(sub.sum())} EV {V.pnl[sub].sum()/V.coste[sub].sum():+.3f} acierto {V.gana[sub].mean():.3f}')
# 3) R2 en el relleno base
print('3) R2 (bid15 mismo lado - obj <= 0,03 en r-100 ms) x S1')
out = []
for d in DIAS:
    D = Dia(d); bb = B[(B.dia == d) & (B.fill == 1)]
    for mid, u in bb.iterrows():
        f15 = int(math.ceil(u.fin / 900.0) * 900); k = D.tok(u.act, '15min', f15, 'YES' if u.yes else 'NO')
        q = D.top(k, int(u.r) - 100) if k is not None else None
        out.append((mid, (q[0] - u.obj) if (q and q[0] == q[0] and q[0] > 0 and not (q[1] == q[1] and q[0] >= q[1])) else np.nan))
L = pd.Series(dict(out)); b2 = b[b.fill == 1].copy(); b2['lvl15'] = L.reindex(b2.index); b2['quit'] = rem.reindex(b2.index)
b2['dp'] = (V.pnl - b.pnl).reindex(b2.index)
for nm, m in (('R2 si', b2.lvl15 <= 0.03 + 1e-9), ('R2 no', b2.lvl15 > 0.03 + 1e-9), ('sin bid15', b2.lvl15.isna())):
    s = b2[m]
    print(f'  {nm:9s} rellenos {len(s):5d} EV base {s.pnl.sum()/s.coste.sum():+.3f} | S1 quita {s.quit.mean():.3f} dPnL {s.dp.sum():+.1f} ({s.dp.sum()/s.coste.sum():+.4f}/EUR) '
          f'| DESC {s[s.dia<="2026-10-19"].dp.sum():+.1f} TEST {s[s.dia>"2026-10-19"].dp.sum():+.1f}')
# 4) B real: print de relleno y senal S1 en [print-2068, print-100]
print('4) B real (unidades_b.csv): senal S1_x2_w2000 antes del print de relleno')
U = pd.read_csv(os.path.join(SDD, 'unidades_b.csv')); U = U[U.t_det.notna()]; rows = []
for d in sorted(U.dia.unique()):
    D = Dia(d)
    for u in U[U.dia == d].itertuples():
        fin5 = int(u.mercado.split('-')[-1]) + 300; lado = 'YES' if u.outcome == 'Up' else 'NO'
        own = D.tok(u.coin, '5min', fin5, lado); opp = D.tok(u.coin, '5min', fin5, 'NO' if lado == 'YES' else 'YES')
        td = int(u.t_det * 1000); pr = None
        for k, isown in ((own, True), (opp, False)):
            if k is None: continue
            r, v = D.trades(k, td - 5000, td)
            for rr, (p, sd, sz) in zip(r, v):
                if (isown and sd == 0 and p <= u.p_fill + 1e-6) or ((not isown) and sd == 1 and p >= 1 - u.p_fill - 1e-6):
                    pr = int(rr) if pr is None else min(pr, int(rr))
        if pr is None: rows.append(dict(gana=u.gana, coste=u.coste, pnl=u.payout - u.coste, coin=u.coin, dia=d, flag=np.nan)); continue
        sym = SYM[u.coin]; a, b_ = D.xs[sym], D.xs[sym + 1]; xr = D.xr[a:b_]; xv = D.xv[a:b_].astype(float); sg = 1 if lado == 'YES' else -1
        i0, i1 = np.searchsorted(xr, pr - 2068 - 2000), np.searchsorted(xr, pr - 100, 'right')
        rr = xr[i0:i1]; vv = xv[i0:i1]; flag = 0
        if len(rr) > 1:
            j = np.searchsorted(rr, rr - 2000, 'right') - 1; ok = (j >= 0) & (rr >= pr - 2068)
            ret = np.where(ok, (vv / vv[np.clip(j, 0, None)] - 1) * 1e4 * sg, 0); flag = int((ret <= -2).any())
        rows.append(dict(gana=u.gana, coste=u.coste, pnl=u.payout - u.coste, coin=u.coin, dia=d, flag=flag))
W = pd.DataFrame(rows)
print(f'  rellenos {len(W)}, con print {W.flag.notna().sum()} (missing {W.flag.isna().sum()})')
for f in (1, 0):
    s = W[W.flag == f]; print(f'  senal={f}: n {len(s)} acierto {s.gana.mean():.3f} EV {s.pnl.sum()/s.coste.sum():+.3f} PnL {s.pnl.sum():+.2f} por dia ' +
                             ' '.join(f'{d[5:]}:{s[s.dia==d].pnl.sum():+.1f}' for d in sorted(W.dia.unique())))
