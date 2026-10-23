#!/usr/bin/env python3
"""p1_pre.py -- rasgos PREVIOS al relleno (registro ms por RECEPCION, salida/datos/ms_D.npz) para cada unidad u_D:
top bid/ask del token c en ts-6 s y ts-30 s (ts = bloque estimado; el casado es ~bloque-2,4 s +-1,5 s), tamano del top bid,
dist = bid_top(ts-6) - pc (0 = la orden estaba en el top; >0 por debajo), vol30 (acc casadas en ambos tokens del 5m en [ts-36, ts-6]),
cambio del bid en 30 s, bid15 mismo lado (lvl15 = bid15 - pc) en ts-6. Salida datos/up_D.csv.gz."""
import sys, os, math, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos')
sys.path.insert(0, os.path.join(AQ, '../../salida/scripts')); from msdata import Dia
for d in sys.argv[1:]:
    M = Dia(d); U = pd.read_csv(os.path.join(D, f'u_{d}.csv.gz'), dtype={'mid': str})
    tk = {str(t): i for i, t in enumerate(M.tokens)}
    T = pd.read_csv(os.path.join(D, f'tok_{d}.csv'), dtype={'token': str, 'mid': str}).set_index('tok_i')
    rows = []
    for u in U.itertuples():
        k = tk.get(T.token.get(u.c)); r = {}
        if k is not None:
            t6 = int((u.ts - 6) * 1000); t30 = int((u.ts - 30) * 1000)
            q6 = M.top(k, t6); q30 = M.top(k, t30)
            if q6 is not None and q6[0] == q6[0]:
                r.update(b6=q6[0], a6=q6[1], bs6=q6[2], dist=round(q6[0] - u.pc, 3), edad6=(t6 - q6[4]) / 1000)
            if q30 is not None and q30[0] == q30[0]: r['db30'] = (q6[0] - q30[0]) if q6 is not None else np.nan
            opp = M.tok(u.act, '5min', int(u.fin), 'NO' if u.lado == 'YES' else 'YES')
            tot = 0.0
            for kk in (k, opp):
                if kk is None: continue
                rr, vv = M.trades(kk, int((u.ts - 36) * 1000), t6); tot += float(vv[:, 2].sum()) if len(vv) else 0.0
            r['vol30'] = tot
            k15 = M.tok(u.act, '15min', int(math.ceil(u.fin / 900.0) * 900), u.lado)
            if k15 is not None:
                q = M.top(k15, t6)
                if q is not None and q[0] == q[0] and q[0] > 0 and not (q[1] == q[1] and q[0] >= q[1] - 1e-9): r['lvl15'] = round(q[0] - u.pc, 3)
        rows.append(r)
    X = pd.concat([U.reset_index(drop=True), pd.DataFrame(rows)], axis=1)
    X.to_csv(os.path.join(D, f'up_{d}.csv.gz'), index=False); print(d, len(X), 'con top', int(X.dist.notna().sum()), flush=True)
