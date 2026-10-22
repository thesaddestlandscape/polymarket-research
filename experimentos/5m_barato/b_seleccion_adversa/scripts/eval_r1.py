"""eval_r1.py -- regla R1 (candidata congelada): NO pujar 00-03:59 UTC y NO pujar con <26 acciones casadas en el mercado en los 30 s previos.
Evalua en (i) poblacion (unidades, A 09-13 / B 14-17 / C 18-21) y (ii) simulador de cinta con contrafactico (re-simulacion con puerta)."""
import sys, os, glob, json; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from sa_common import *; from sa_sim import *
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(B + '/datos/units/units_*.pkl'))], ignore_index=True).rename(columns={'p': 'pn'})
dn = U.dia.str[-2:].astype(int)
U['per'] = np.where(dn <= 13, 'A', np.where(dn <= 17, 'B', 'C'))
U['R1'] = (U.hora >= 4) & (U.vol30 >= 26)
print('== POBLACION (unidades 5 acc, 09-21 Oct, ETH/SOL/XRP, pc 0,10-0,30, T 60-300)')
rows = []
for per in ('A', 'B', 'C', 'ABC'):
    S = U if per == 'ABC' else U[U.per == per]
    for nm, m in (('todas', np.ones(len(S), bool)), ('R1 pujar', S.R1.values), ('R1 descartar', ~S.R1.values)):
        r = day_boot(S[m], 'pn', 'c', 'dia'); print(per, nm, fmt(r)); rows.append(dict(per=per, grupo=nm, **r))
pd.DataFrame(rows).to_csv(B + '/datos/r1_poblacion.csv', index=False)
print('retenido € C:', U[(U.per == 'C') & U.R1].c.sum() / U[U.per == 'C'].c.sum())
for nm, m in (('solo hora', U.hora >= 4), ('solo vol30', U.vol30 >= 26)):
    print('componente', nm, 'C pujar:', fmt(day_boot(U[(U.per == 'C') & m], 'pn', 'c', 'dia')), '| B:', fmt(day_boot(U[(U.per == 'B') & m], 'pn', 'c', 'dia')))
print('== SIMULADOR (cinta, B-like, contrafactico)')
D = load(B + '/datos/sim')
hour = ((D['fin'][:, None] - TKV[None, :]) // 3600 % 24).astype(int)
gate = (D['sh30'] >= 26) & (hour >= 4)
dd = D['dia']; dnn = np.array([int(x[-2:]) for x in dd])
for per, m in (('A', dnn <= 13), ('B', (dnn >= 14) & (dnn <= 17)), ('C', dnn >= 18), ('ABC', dnn > 0)):
    Ds = sub(D, m); g = gate[m]
    R0 = run(Ds, delta=dB(Ds)); R1 = run(Ds, delta=dB(Ds), gate=g)
    a0, a1 = adv(R0), adv(R1); q0 = R0[R0.quoted]; q1 = R1[R1.quoted]
    allq1 = (q1.win.astype(float) - q1.pq).sum() / q1.pq.sum()
    print(per, 'BASE', fmt(evtab(R0)), '| fr %.2f' % a0['fr'], '\n   R1  ', fmt(evtab(R1)), '| fr %.2f' % a1['fr'], '| EV_todas_cotizadas(sin seleccion) %+.3f' % allq1, '| PnL base %.1f R1 %.1f' % (evtab(R0)['ev'] * evtab(R0)['eur'], evtab(R1)['ev'] * evtab(R1)['eur']))
