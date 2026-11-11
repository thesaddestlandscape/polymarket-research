#!/usr/bin/env python3
"""analiza_cxb_v3.py [TAG=v3dd] -- evaluacion de la familia CXB-true / F5 con MOTOR v3 (out_v3/CX_<TAG>_<D>.pkl de passT_cxb_v3.py), TRAIN 26-Oct..09-Nov (15 dias, HOLD NO se lee). Solo lectura, 0 ordenes.
Metricas por variante: n colocaciones/rellenos/cancelaciones, coste, pnl (rb 0,2), EV ponderado por EUR (sum pnl / sum coste), IC90 bootstrap por DIAS (razon de sumas), IC90 por CIERRE (cluster `fin`), sin 2 mejores dias, dias+, por moneda y por nivel L.
Incremental vs control con MISMA colocacion (CXB*, TOP60, CXB60r -> GEO1; F5A_CXB* -> GEO1_F5A; F5A/F5B -> G0): delta pnl diario, IC90 por dias.
Placebo de igual cobertura: S semillas por variante (cancelacion en instante uniforme del segmento / mascara F5 rodada). p por variante = (1+#{EV_placebo >= EV_obs})/(1+S);
MULTIPLICIDAD: max-statistic sobre las K variantes probadas (z de cada variante vs su distribucion placebo; p_familia = (1+#{max_v z_vs >= max_v z_v})/(1+S)); IC por dias tambien con Bonferroni (quantil 0,05/K)."""
import sys, os, json, glob, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; TAG = sys.argv[1] if len(sys.argv) > 1 else 'v3dd'
DIAS = ['2026-10-26', '2026-10-27', '2026-10-28', '2026-10-29', '2026-10-30', '2026-10-31', '2026-11-01', '2026-11-02', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-07', '2026-11-08', '2026-11-09']
TESTED = ['CXB60', 'CXB100', 'CXB150', 'TOP60', 'CXB60r', 'F5A', 'F5B', 'F5A_CXB60', 'F5A_CXB100', 'F5A_CXB150']; K = len(TESTED)
CTRL = {'CXB60': 'GEO1', 'CXB100': 'GEO1', 'CXB150': 'GEO1', 'TOP60': 'GEO1', 'CXB60r': 'GEO1', 'F5A': 'G0', 'F5B': 'G0', 'F5A_CXB60': 'GEO1_F5A', 'F5A_CXB100': 'GEO1_F5A', 'F5A_CXB150': 'GEO1_F5A'}
B = 20000; SEED = 20261111
fs = [H + f'out_v3/CX_{TAG}_{d}.pkl' for d in DIAS]; miss = [f for f in fs if not os.path.exists(f)]
if miss: print('FALTAN dias:', [os.path.basename(f) for f in miss]); DIAS = [d for d, f in zip(DIAS, fs) if os.path.exists(f)]
X = [pd.read_pickle(H + f'out_v3/CX_{TAG}_{d}.pkl') for d in DIAS]; A = pd.concat([x['A'] for x in X], ignore_index=True); R = pd.concat([x['R'] for x in X], ignore_index=True)
assert A.dia.max() <= '2026-11-09', 'HOLD'
nd = len(DIAS); rng = np.random.default_rng(SEED)
def day(v, col):
    return A[A['var'] == v].groupby('dia')[col].sum().reindex(DIAS).fillna(0).values
def stats(v):
    num, den = day(v, 'pnl'), day(v, 'cost'); ev = num.sum() / den.sum() if den.sum() > 0 else np.nan
    ix = rng.integers(0, nd, (B, nd)); bs = num[ix].sum(1) / np.maximum(den[ix].sum(1), 1e-9)
    o = np.argsort(-num)[2:]; s2 = num[o].sum() / den[o].sum() if den[o].sum() > 0 else np.nan
    rv = R[R['var'] == v]
    if len(rv):
        cl = rv.groupby('fin')[['pnl', 'cost']].sum().values; ixc = rng.integers(0, len(cl), (4000, len(cl))); bc = cl[:, 0][ixc].sum(1) / np.maximum(cl[:, 1][ixc].sum(1), 1e-9); icc = (np.quantile(bc, .05), np.quantile(bc, .95), len(cl))
    else: icc = (np.nan, np.nan, 0)
    return dict(var=v, n_seg=int(day(v, 'n_seg').sum()), n_canc=int(day(v, 'n_canc').sum()), n_fill=int(day(v, 'n_fill').sum()), cost=round(float(den.sum()), 1), pnl=round(float(num.sum()), 1), ev=round(float(ev), 4),
                ic90_dias=(round(float(np.quantile(bs, .05)), 3), round(float(np.quantile(bs, .95)), 3)), ic_bonf_dias_lo=round(float(np.quantile(bs, .05 / K)), 3), ic90_cierre=(round(float(icc[0]), 3), round(float(icc[1]), 3)), n_cierres=int(icc[2]),
                ev_sin2=round(float(s2), 4), dias_pos=f'{int((num > 0).sum())}/{nd}', pnl_dia=num)
rows = {v: stats(v) for v in ['G0', 'GEO1', 'GEO1_F5A'] + TESTED}
def tb(rs): return pd.DataFrame([{k: v for k, v in r.items() if k != 'pnl_dia'} for r in rs]).to_string(index=False)
print('=== TRAIN', DIAS[0], DIAS[-1], nd, 'dias; variantes probadas K =', K, '(+3 controles)'); print(tb(rows.values()))
# ---- incremental vs control (misma colocacion): delta pnl diario
inc = []
for v in TESTED:
    c = CTRL[v]; d = rows[v]['pnl_dia'] - rows[c]['pnl_dia']; ix = rng.integers(0, nd, (B, nd)); bs = d[ix].mean(1)
    cc = day(c, 'cost').sum(); cv = day(v, 'cost').sum()
    inc.append(dict(var=v, ctrl=c, dpnl_total=round(float(d.sum()), 1), dpnl_dia=round(float(d.mean()), 2), ic90_dias=(round(float(np.quantile(bs, .05)), 2), round(float(np.quantile(bs, .95)), 2)), ic_bonf_lo=round(float(np.quantile(bs, .05 / K)), 2), dias_pos=f'{int((d > 0).sum())}/{nd}',
                    dEV=round(rows[v]['ev'] - rows[c]['ev'], 4), frac_coste_quitado=round(1 - cv / cc, 3)))
print('\n=== INCREMENTAL vs control con la misma colocacion (delta pnl = pnl_variante - pnl_control; >0 = la regla ayuda)'); print(pd.DataFrame(inc).to_string(index=False))
# ---- placebo + max-statistic
S_ = sorted({int(v.rsplit('_', 1)[1]) for v in A['var'].unique() if v.startswith('P_')}); ns = len(S_)
zs = {}; pl = []; PE = {}
for v in TESTED:
    ev_p = np.array([(lambda n, d_: n.sum() / d_.sum() if d_.sum() > 0 else np.nan)(day(f'P_{v}_{s}', 'pnl'), day(f'P_{v}_{s}', 'cost')) for s in S_]); PE[v] = ev_p
    m, sd = np.nanmean(ev_p), np.nanstd(ev_p, ddof=1); zobs = (rows[v]['ev'] - m) / sd if sd > 0 else np.nan; zs[v] = zobs
    pl.append(dict(var=v, ev_obs=rows[v]['ev'], ev_placebo_media=round(float(m), 4), ev_placebo_p5_p95=(round(float(np.nanpercentile(ev_p, 5)), 3), round(float(np.nanpercentile(ev_p, 95)), 3)), exceso=round(float(rows[v]['ev'] - m), 4), z=round(float(zobs), 2),
                   p_placebo=round(float((1 + np.nansum(ev_p >= rows[v]['ev'])) / (1 + ns)), 4), n_seg_placebo=int(np.mean([day(f'P_{v}_{s}', 'n_seg').sum() for s in S_])), n_canc_obs_vs_placebo=(rows[v]['n_canc'], int(np.mean([day(f'P_{v}_{s}', 'n_canc').sum() for s in S_])))))
Mobs = np.nanmax(list(zs.values()))
Ms = np.array([np.nanmax([(PE[v][i] - np.nanmean(PE[v])) / np.nanstd(PE[v], ddof=1) for v in TESTED]) for i in range(ns)])
p_fam = float((1 + (Ms >= Mobs).sum()) / (1 + ns))
print(f'\n=== PLACEBO de igual cobertura (S={ns} semillas) y MAX-STATISTIC sobre K={K}'); print(pd.DataFrame(pl).to_string(index=False)); print(f'max z observado {Mobs:.2f}; p familia (max-stat) = {p_fam:.4f} (resolucion minima {1/(1+ns):.3f})')
# ---- por moneda y nivel L (descriptivo) para cada variante probada + G0
def split(v, by):
    g = A[A['var'] == v].groupby(by).agg(n=('n_fill', 'sum'), cost=('cost', 'sum'), pnl=('pnl', 'sum')); g['ev'] = (g.pnl / g.cost).round(3); return g
print('\n=== POR MONEDA (n rellenos, coste, pnl, EV)')
for v in ['G0', 'GEO1'] + TESTED: print(v, {c: (int(r.n), round(float(r.cost), 0), round(float(r.pnl), 1), round(float(r.ev), 3)) for c, r in split(v, 'act').iterrows()})
print('\n=== POR NIVEL L')
for v in ['G0', 'GEO1'] + TESTED: print(v, {str(L): (int(r.n), round(float(r.pnl), 1), round(float(r.ev), 3)) for L, r in split(v, 'L').iterrows()})
# ---- gradiente F5 sobre los rellenos G0 (F5 en el instante de decision, RX): EV por tercil con los cortes congelados
C0, C1 = 3.526360511779785, 4.717426776885986
g0 = R[R['var'] == 'G0'].copy(); g0['ter'] = np.where(~np.isfinite(g0.f5_dec), 'sin', np.where(g0.f5_dec <= C0, 'bajo', np.where(g0.f5_dec <= C1, 'medio', 'alto')))
print('\n=== GRADIENTE F5(t_dec) en rellenos G0 v3 (n, coste, pnl, EV, EV sin 2 mejores dias, dias+)')
for t, g in g0.groupby('ter'):
    dd = g.groupby('dia')[['pnl', 'cost']].sum().reindex(DIAS).fillna(0); o = np.argsort(-dd.pnl.values)[2:]
    print(t, len(g), round(float(g.cost.sum()), 0), round(float(g.pnl.sum()), 1), round(float(g.pnl.sum() / g.cost.sum()), 3), round(float(dd.pnl.values[o].sum() / max(dd.cost.values[o].sum(), 1e-9)), 3), f'{int((dd.pnl.values > 0).sum())}/{nd}')
json.dump(dict(tag=TAG, dias=DIAS, K=K, variantes={v: {k: x for k, x in r.items() if k != 'pnl_dia'} for v, r in rows.items()}, incremental=inc, placebo=pl, p_familia=p_fam, max_z=float(Mobs)), open(H + f'out_v3/analiza_cxb_{TAG}.json', 'w'), indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
