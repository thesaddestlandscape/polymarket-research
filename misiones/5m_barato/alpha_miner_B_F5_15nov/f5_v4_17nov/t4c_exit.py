"""t4c_exit.py -- variante con confirmacion de SALIDA Y s (la salida deja de ser inmediata; coste: Y s mas de exposicion) y entrada X s. python3 -I t4c_exit.py W,C,rho,nmin. Causal (solo crudo hasta t)."""
import sys, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as SC, t4b_eval as T
def estado_xy(crudo, X, Y):
    """entra tras X crudos True seguidos; sale tras Y crudos False seguidos (Y=1: inmediata)."""
    n = len(crudo); st = np.zeros(n, bool); s = False; a = b = 0
    for i, c in enumerate(crudo):
        a = a + 1 if c else 0; b = 0 if c else b + 1
        if not s and a >= X: s = True
        elif s and b >= Y: s = False
        st[i] = s
    return st
W, C, rho, nmin = [float(x) for x in sys.argv[1].split(',')]; p = SC.ParamsDetector(int(W), int(C), rho, int(nmin), 1)
DAYS = [T.Dia(d) for d in T.DIAS]; dev = [D for D in DAYS if D.d <= T.CORTE]; ho = [D for D in DAYS if D.d > T.CORTE]; cr = {D.d: SC.lo_crudo(D.S, p) for D in DAYS}; L = [f'# T4c salida confirmada Y (entrada X) en {p!r}']
for X, Y in ((1, 1), (1, 2), (1, 3), (1, 5), (1, 10), (3, 5), (5, 10)):
    row = []
    for nm, g in (('DEV', dev), ('HO', ho)):
        sts = [estado_xy(cr[D.d], X, Y) for D in g]; A = T.agrega([T.metricas_dia(D, s) for D, s in zip(g, sts)]); can = np.mean([(np.diff(s.astype(int)) == -1).sum() for s in sts])
        row.append(f"{nm} score {A['lo_en_hi'] + A['nolo_en_lo']} lo_en_hi {A['lo_en_hi']} nolo_en_lo {A['nolo_en_lo']} cancel/dia {can:.1f} lohi p50/p90 {T.pq(A['lohi'], 50)}/{T.pq(A['lohi'], 90)} miss {A['lohi_miss']}")
    L.append(f'X={X} Y={Y}: ' + ' | '.join(row))
open(HERE + '/T4c_exit.txt', 'w').write('\n'.join(L) + '\n'); print('\n'.join(L))
