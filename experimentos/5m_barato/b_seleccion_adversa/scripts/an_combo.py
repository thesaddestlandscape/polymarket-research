import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from sa_common import *
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = pd.read_pickle(B + '/datos/ms_units.pkl').rename(columns={'p': 'pn'}); U = U[U.has5].copy()
dn = U.dia.str[-2:].astype(int); U['per'] = np.where(dn <= 19, 'disc', 'hold')
A = U.lvl15 <= 0.03; R1a = U.vol30ws >= 26; R1b = U.hora >= 4; Dd = U.d_open >= 0.17; Cdev = U.cl_dev.abs() < 100
rules = {'todas': np.ones(len(U), bool), 'A lvl15<=0.03': A, 'A & R1a(ws)': A & R1a, 'A & R1b': A & R1b, 'A & R1': A & R1a & R1b, 'A & d_open>=0.17': A & Dd, 'A & R1 & d_open>=0.17': A & R1a & R1b & Dd,
         'd_open>=0.17 solo': Dd, 'R1 & d_open': R1a & R1b & Dd}
rows = []
for nm, m in rules.items():
    m = np.asarray(m)
    for per in ('disc', 'hold', 'todo'):
        s = U[m & ((U.per == per).values if per != 'todo' else True)]
        r = day_boot(s, 'pn', 'c', 'dia'); print('%-24s %-4s %s | retenido EUR %.2f | unid/dia %.0f' % (nm, per, fmt(r), s.c.sum() / U.c[(U.per == per).values if per != 'todo' else slice(None)].sum(), len(s) / s.dia.nunique()))
        rows.append(dict(regla=nm, per=per, **r))
pd.DataFrame(rows).to_csv(B + '/datos/combo_ms_units.csv', index=False)
s = U[np.asarray(A)]; print('A por dia:', {d: (round(g.pn.sum() / g.c.sum(), 3), len(g)) for d, g in s.groupby('dia')})
s = U[~np.asarray(A) & U.lvl15.notna().values]; print('no-A por dia:', {d: (round(g.pn.sum() / g.c.sum(), 3), len(g)) for d, g in s.groupby('dia')})
print('A por moneda:', {a: (round(g.pn.sum() / g.c.sum(), 3), len(g)) for a, g in U[np.asarray(A)].groupby('act')})
print('A por banda pc:', {str(b): (round(g.pn.sum() / g.c.sum(), 3), len(g)) for b, g in U[np.asarray(A)].groupby(pd.cut(U.pc[np.asarray(A)], [0.1, 0.15, 0.2, 0.25, 0.3]), observed=True)})
# umbral x continuo (sensibilidad)
for x in (-0.05, 0.0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12):
    s = U[(U.lvl15 <= x).values]; a = s[s.per == 'disc']; h = s[s.per == 'hold']
    print('lvl15<=%.2f n=%d EV disc %+.3f hold %+.3f' % (x, len(s), a.pn.sum() / a.c.sum(), h.pn.sum() / h.c.sum()))
