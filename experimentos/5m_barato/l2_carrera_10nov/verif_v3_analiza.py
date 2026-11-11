"""verif_v3_analiza.py -- recall/precision de v2o/v3o/v3d frente a las ordenes REALES de B (20-23 Oct, ledger). Solo lectura. Wilson 90 % sobre ordenes."""
import glob, numpy as np, pandas as pd
H = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/verif_real/'
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out_v3/V3_*.pkl'))], ignore_index=True); R = R[R['cov'] == 'ok'].copy()
V = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out/V_*.pkl'))], ignore_index=True)
m = R.merge(V[['oid', 'BASE_f_q', 'OPT_f_q']], on='oid', how='left')
print('REGRESION v2o vs V_ original: BASE iguales', bool(np.allclose(m.v2o_BASE_f_q, m.BASE_f_q)), 'OPT iguales', bool(np.allclose(m.v2o_OPT_f_q, m.OPT_f_q)), 'n', len(m))
def wil(k, n, z=1.645):
    if n == 0: return (np.nan, np.nan)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)); return round((c - h) / d, 3), round((c + h) / d, 3)
def conf(df, col):
    s = df[col] > 1e-9; r = df.real_fill == 1; tp = int((s & r).sum()); sim = int(s.sum()); re = int(r.sum())
    return dict(n=len(df), real=re, sim=sim, tp=tp, prec=round(tp / max(sim, 1), 3), prec_ic90=wil(tp, sim), rec=round(tp / max(re, 1), 3), rec_ic90=wil(tp, re))
def pnl(q, L, g): return q * (g - L) + q * 0.2 * 0.07 * L * (1 - L)
rows = []
for var in ('BASE', 'OPT'):
    for tag in ('v2o', 'v3o', 'v3d'):
        rows.append(dict(var=var, tag=tag, **conf(R, f'{tag}_{var}_f_q')))
print(pd.DataFrame(rows).to_string(index=False))
print('--- por moneda (BASE)')
for tag in ('v2o', 'v3o', 'v3d'):
    for c, g in R.groupby('coin'): print(tag, c, conf(g, f'{tag}_BASE_f_q'))
print('--- por dia (BASE)')
for tag in ('v2o', 'v3d'):
    for d, g in R.groupby('dia'): print(tag, d, conf(g, f'{tag}_BASE_f_q'))
print('--- vida>=1,5 s (BASE)')
R['vida'] = (R.t_fuera - R.t_ini) / 1000
for tag in ('v2o', 'v3d'): print(tag, conf(R[R.vida >= 1.5], f'{tag}_BASE_f_q'))
# cambios fila a fila v2o -> v3
for a, b in (('v2o', 'v3o'), ('v3o', 'v3d')):
    x = R[f'{a}_BASE_f_q'] > 1e-9; y = R[f'{b}_BASE_f_q'] > 1e-9
    print(f'{a}->{b}: solo {a} {int((x & ~y).sum())}, solo {b} {int((~x & y).sum())}, ambos {int((x & y).sum())}; de los solo-{a}: reales {int(((x & ~y) & (R.real_fill == 1)).sum())}; de los solo-{b}: reales {int(((~x & y) & (R.real_fill == 1)).sum())}')
# EV real vs simulado
for tag in ('v2o', 'v3d'):
    q = R[f'{tag}_BASE_f_q']; ps = pnl(q, R.L, R.gana); cs = q * R.L; pr = pnl(R.real_q, R.L, R.gana); cr = R.real_q * R.L
    print(tag, 'EV sim', round(float(ps.sum() / cs.sum()), 3), 'pnl', round(float(ps.sum()), 2), 'coste', round(float(cs.sum()), 2), '| real EV', round(float(pr.sum() / cr.sum()), 3), 'pnl', round(float(pr.sum()), 2), 'coste', round(float(cr.sum()), 2))
# sello del relleno propio: donde cae tm v2 vs v3 respecto a la firma
O = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out_v3/own_*.pkl'))], ignore_index=True)
print('propios: ramas', O.rama.value_counts(dropna=False).to_dict(), 'tm3-tm2 (ms) p5/p50/p95', np.nanpercentile((O.tm3 - O.tm2).astype(float), [5, 50, 95]).round(0).tolist())
