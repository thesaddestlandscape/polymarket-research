#!/usr/bin/env python3
"""e2_clases.py -- PREREG_E2 clases unificadas: valida el proxy L2 (C1/C2/C3 por prints) contra la clase on-chain cl_h1_0.005 en los rellenos REALES de B."""
import os, sys, bisect, collections
sys.dont_write_bytecode = True
import e2_engine as E
import numpy as np, pandas as pd
S = E.S; D = E.D
BC = pd.read_csv(os.path.join(D, '../../cola_vs_cruce/datos/b_clase.csv'), dtype={'mid': str}).drop_duplicates(['tx', 'c']); BC = BC[BC.es_b == 1].copy()
rows = []; miss = collections.Counter()
for _, r in BC.iterrows():
    fin = int(r.fin); path = S.SRC + f'mk/{r.act}_{r.mid}.gz'
    if not (S.FIN_MIN <= fin <= S.FIN_MAX) or not os.path.exists(path): miss['fuera_o_sin_fichero'] += 1; continue
    m = E.Mkt(r.act, r.mid, fin)
    if m.roto: miss['roto'] += 1; continue
    L = 'Y' if r.lado == 'YES' else 'N'; o = int(round(r.pc * 1000)); t = float(r.t_det) * 1000
    cand = [(rr, q, a) for (rr, q, a) in m.NT[L] if t - 3500 <= rr <= t + 300 and q <= o]
    if not cand: miss['sin_print'] += 1; continue
    eq = [c for c in cand if c[1] == o] or cand
    pr = min(eq, key=lambda c: abs(c[0] - t))
    rec = dict(cl=r['cl_h1_0.005'], q=pr[1], o=o, dt=(pr[0] - t) / 1000)
    for tau in (5, 25, 100):
        rec[f'p{tau}'] = E.clase_u(m.NT, L, pr[0], o, 'X' if pr[1] < o and False else 'P', tau1=tau)
    rows.append(rec)
df = pd.DataFrame(rows); print('rellenos reales localizados en L2', len(df), 'de', len(BC), dict(miss))
for tau in (5, 25, 100):
    c = f'p{tau}'; print(f'--- tau1={tau} ms: exactitud {(df[c]==df.cl).mean():.3f}'); print(pd.crosstab(df.cl, df[c]))
print('cuotas on-chain', df.cl.value_counts(normalize=True).round(3).to_dict(), '| proxy25', df.p25.value_counts(normalize=True).round(3).to_dict())
df.to_csv(os.path.join(D, 'e2_clases_validacion.csv'), index=False)
