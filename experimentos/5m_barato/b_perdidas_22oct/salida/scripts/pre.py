#!/usr/bin/env python3
"""pre.py b|pop DIAS -- veto PRE-relleno (cancelar antes de que nos rellenen): senales en [t_rel-10 s, t_rel-0,3 s].
Ganancia del veto = -sum(pnl hold) de las vetadas, / coste total. Placebo: veto barajado dentro de dia. Solo unidades rellenadas
(no modela el contrafactico de pujas no rellenadas ni la re-puja)."""
import sys, os, numpy as np, pandas as pd
DD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
modo = sys.argv[1]; dias = sys.argv[2].split(',')
L = pd.concat([pd.read_csv(os.path.join(DD, f'largo_{modo}_{d}.csv')) for d in dias], ignore_index=True)
U = L[L.tau == 5].reset_index(drop=True); U['pnl'] = U.payout - U.coste
tot = U.pre_fav + U.pre_con; U['pre_imb'] = np.where(tot > 0, (U.pre_fav - U.pre_con) / tot.clip(lower=1e-9), 0)
R = {'P1_bid-0.01': U.pre_dbid <= -0.01 + 1e-9, 'P1_bid-0.02': U.pre_dbid <= -0.02 + 1e-9, 'P2_bn-3': U.pre_bn <= -3, 'P2_bn-6': U.pre_bn <= -6,
     'P3_15-0.01': U.pre_d15 <= -0.01 + 1e-9, 'P3_15-0.02': U.pre_d15 <= -0.02 + 1e-9, 'P4_flujo': (U.pre_imb <= -0.5) & (tot >= 10)}
INV = {'P1_bid-0.01': U.pre_dbid >= 0.01 - 1e-9, 'P1_bid-0.02': U.pre_dbid >= 0.02 - 1e-9, 'P2_bn-3': U.pre_bn >= 3, 'P2_bn-6': U.pre_bn >= 6,
       'P3_15-0.01': U.pre_d15 >= 0.01 - 1e-9, 'P3_15-0.02': U.pre_d15 >= 0.02 - 1e-9, 'P4_flujo': (U.pre_imb >= 0.5) & (tot >= 10)}
c = U.coste.sum(); rng = np.random.default_rng(3); print(f'{modo} {dias} unidades {len(U)} coste {c:.0f} EV hold {U.pnl.sum()/c:+.4f}')
for k, m in R.items():
    m = m.fillna(False).values; g = -U.pnl.values[m].sum()
    pl = []
    for _ in range(1000):
        s = 0
        for dd, h in U.groupby('dia'):
            i = h.index.values; kk = m[i].sum()
            if kk: s += -h.pnl.values[rng.choice(len(i), kk, replace=False)].sum()
        pl.append(s)
    pl = np.array(pl); gd = {dd: -h.pnl.values[m[h.index.values]].sum() / h.coste.sum() for dd, h in U.groupby('dia')}
    print(f'  {k:12s} vetadas {m.sum():5d} (gan {U.gana.values[m].sum()}) ganancia {g/c:+.4f}/EUR ({g:+.1f}) placebo {pl.mean()/c:+.4f} p {np.mean(pl >= g):.3f} '
          f'inversion {-U.pnl.values[INV[k].fillna(False).values].sum()/c:+.4f} | por dia ' + ' '.join(f'{v:+.3f}' for v in gd.values()))
