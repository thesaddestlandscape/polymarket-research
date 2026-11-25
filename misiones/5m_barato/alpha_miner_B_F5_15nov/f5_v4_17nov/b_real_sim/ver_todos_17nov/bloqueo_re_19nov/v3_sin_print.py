"""v3_sin_print.py -- V3: por que 29 casos de u1b A1 no tienen print ancla. Solo lectura, no EV. Descriptivo (sin criterio de aceptacion)."""
import sys, os, gzip, numpy as np, pandas as pd
sys.path.insert(0, '../solo_observable_19nov'); import so1_traza as S
A = pd.read_csv('../cierre_limites_19nov/out/u1b_prereg_bloqueo_A1.csv'); A = A[A.src == 'sin_print']
d = pd.read_pickle(S.BASE + 'tomador_202.pkl').set_index('oid')
rows = []; cache = {}
for oid, pos in zip(A.oid, A.pos):
    r = d.loc[oid]; m = S.TOKM.get(str(r.tok)); fn = S.MK + f'{m[0]}_{m[1]}.gz'
    if fn not in cache:
        T = {'Y': [], 'N': []}; tmin = tmax = None
        with gzip.open(fn, 'rt', errors='replace') as f:
            for ln in f:
                c = ln.rstrip('\n').split(',')
                if len(c) < 3: continue
                try: t = int(c[2])
                except ValueError: continue
                tmin = t if tmin is None else min(tmin, t); tmax = t if tmax is None else max(tmax, t)
                if c[1] == 'T' and c[0] in T and len(c) >= 6:
                    try: T[c[0]].append((t, c[3], float(c[4]), float(c[5])))
                    except ValueError: pass
        if len(cache) > 4: cache.pop(next(iter(cache)))
        cache[fn] = (T, tmin, tmax)
    T, tmin, tmax = cache[fn]; t3 = int(r.real_tm3); own = 'Y' if m[2] == 'YES' else 'N'; comp = 'N' if own == 'Y' else 'Y'
    cov = tmin is not None and tmin <= t3 - 5000 and tmax >= t3 + 5000
    near = [(abs(x[0] - t3), sd, x) for sd in ('Y', 'N') for x in T[sd] if abs(x[0] - t3) <= 5000]
    near.sort(key=lambda z: z[0])
    n15 = [z for z in near if -100 <= z[2][0] - t3 <= 1500]
    best = near[0] if near else None
    rows.append(dict(oid=oid[:12], pos=pos, cobertura_mk=cov, T_en_5s=len(near), T_en_ventana=len(n15), L=r.L, eq=r.tk_eq,
                     T_mas_cercano_dt=(best[2][0] - t3) if best else None, T_lado=('own' if best and best[1] == own else 'comp') if best else None,
                     T_precio=best[2][2] if best else None, T_side=best[2][1] if best else None, T_sz=best[2][3] if best else None, real_q=r.real_q, dia=r.dia))
X = pd.DataFrame(rows); X.to_csv('out/v3_sin_print.csv', index=False)
print(X.to_string(index=False))
print('resumen: sin cobertura mk', int((~X.cobertura_mk).sum()), '| con cobertura y 0 T en +-5 s', int((X.cobertura_mk & (X.T_en_5s == 0)).sum()),
      '| T en ventana pero a otro precio', int((X.T_en_ventana > 0).sum()), '| T solo fuera de ventana (<=5 s)', int(((X.T_en_ventana == 0) & (X.T_en_5s > 0)).sum()))
