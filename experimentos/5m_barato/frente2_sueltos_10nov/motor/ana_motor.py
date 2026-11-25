#!/usr/bin/env python3
"""Analisis del motor passT+IW (EXPLORATORIO, 12 dias quemados). Lee out/MI_*.pkl (passT_iw.py) y q11/toxicidad_thru1/out/RT_*.pkl (reproduccion).
TRAIN = 26-31 Oct (6 d), HOLD = 01-04 + 07-08 Nov (6 d). dPnL = sum pnl(var) - sum pnl(base) por cierre/dia; EV ponderado por EUR; IC90 bootstrap (4000) por dia y por cierre."""
import glob, json, numpy as np, pandas as pd
H = '/root/polymarket-research/experimentos/5m_barato/frente2_sueltos_10nov/motor/'
RTD = '/root/polymarket-research/experimentos/5m_barato/q11/toxicidad_thru1/out/'
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out/MI_*.pkl'))], ignore_index=True)
DIAS = sorted(R.dia.unique()); TR = [d for d in DIAS if d <= '2026-10-31']; HO = [d for d in DIAS if d > '2026-10-31']
rng = np.random.default_rng(20261110); NB = 4000; out = []; P = out.append
P(f'dias ({len(DIAS)}): TRAIN {TR} | HOLD {HO}')
def sel(v, dias): return R[(R['var'] == v) & R.dia.isin(dias)]
def perday(v, dias, col='pnl'): return sel(v, dias).groupby('dia')[col].sum().reindex(dias, fill_value=0.0)
def percie(v, dias): return sel(v, dias).groupby('fin').pnl.sum()
def boot(a): a = np.asarray(a, float); m = a[rng.integers(0, len(a), (NB, len(a)))].sum(1); return np.percentile(m, [5, 95])
def stat(v, dias):
    x = sel(v, dias); pd_ = perday(v, dias); cd = perday(v, dias, 'cost'); t2 = pd_.sort_values().index[-2:]
    s2 = pd_.drop(t2).sum() / cd.drop(t2).sum() if cd.drop(t2).sum() > 0 else np.nan
    return f'n={len(x):4d} EUR={x.cost.sum():7.1f} pnl={x.pnl.sum():+7.1f} EV/EUR={x.pnl.sum() / x.cost.sum():+.3f} sin2dias={s2:+.3f} dias+={int((pd_ > 0).sum())}/{len(dias)}'
def contrast(v, base, dias, plac=None):
    pv, pb = perday(v, dias), perday(base, dias); dd = pv - pb; fins = sorted(set(sel(v, dias).fin) | set(sel(base, dias).fin))
    dc = percie(v, dias).reindex(fins, fill_value=0.0) - percie(base, dias).reindex(fins, fill_value=0.0)
    ld, hd = boot(dd.values); lc, hc = boot(dc.values); t2 = dd.sort_values().index[-2:]
    s = f'  dPnL={dd.sum():+7.1f} (dias d>0 {int((dd > 0).sum())}/{len(dias)}; sin 2 mejores dias {dd.drop(t2).sum():+.1f}) IC90dia({ld:+.1f},{hd:+.1f}) IC90cierre({lc:+.1f},{hc:+.1f}) | quita {len(sel(base, dias)) - len(sel(v, dias))} de {len(sel(base, dias))} rellenos'
    if plac:
        pl = np.array([(perday(f'{plac}_{s_}', dias) - pb).sum() for s_ in range(1, 31)]); o = dd.sum()
        s += f'\n    placebo ({plac}, 30 mercados-pareja): media {pl.mean():+.1f} [{pl.min():+.1f},{pl.max():+.1f}] p(placebo>=obs)={(1 + (pl >= o).sum()) / 31:.3f}'
    return s
P('\n== 0. Reproduccion contra passT (RT_*.pkl): G0 y GEO6 identicos por dia (n, pnl)')
ok = True; tot = {'G0': [0, 0.0, 0.0], 'GEO6': [0, 0.0, 0.0]}
for d in DIAS:
    rt = pd.read_pickle(RTD + f'RT_{d}.pkl')
    for v in ('G0', 'GEO6'):
        a = rt[rt['var'] == v]; b = R[(R['var'] == v) & (R.dia == d)]; same = len(a) == len(b) and abs(a.pnl.sum() - b.pnl.sum()) < 1e-6 and abs(a.cost.sum() - b.cost.sum()) < 1e-6
        ok &= same
        if d <= '2026-11-04': tot[v][0] += len(b); tot[v][1] += b.pnl.sum(); tot[v][2] += b.cost.sum()
        if not same: P(f'  DIFERENCIA {d} {v}: RT n={len(a)} pnl={a.pnl.sum():.3f} | motor n={len(b)} pnl={b.pnl.sum():.3f}')
P(f'  G0 y GEO6 identicos a RT_*.pkl en los {len(DIAS)} dias: {ok}')
g0 = tot['G0']; ge = tot['GEO6']; P(f'  10 d (26-Oct..04-Nov): G0 n={g0[0]} pnl={g0[1]:+.1f} EV={g0[1] / g0[2]:+.3f} (esperado 2.938, -166,9, -0,076); GEO6 dPnL={ge[1] - g0[1]:+.1f} (esperado +140)')
P('\n== 1. Auditoria de causalidad (todas las evaluaciones de armado)')
A = [json.load(open(f))['aud'] for f in sorted(glob.glob(H + 'out/MI_*.json'))]; S = {k: sum(a[k] for a in A) for k in A[0]}
P(f"  IW (Binance recepcion): evaluaciones {S['n_el']}, con dato {S['n_iw']}, NaN->se arma {S['nan_iw']} ({S['nan_iw'] / S['n_el']:.4f}); tick usado > t_dec-300: {S['viol_iw']}")
P(f"  GEO6 (bid a t_dec-300): evaluaciones con cotizacion {S['n_b300']}; cotizacion usada > t_dec-300: {S['viol_b300']}")
P(f"  test de truncamiento (serie Binance cortada en t_dec-300): {S['trunc_n']} recomputos, distintos {S['trunc_bad']}")
P('  => rasgos con datos posteriores al armado: ' + str(S['viol_iw'] + S['viol_b300'] + S['trunc_bad']))
CT = [('IW5 vs G0', 'IW5', 'G0', 'PIW5'), ('GEO6 vs G0 (referencia)', 'GEO6', 'G0', None), ('GEO6^IW5 vs GEO6', 'GEO6IW5', 'GEO6', 'PGEO6IW5'), ('GEO6^IW5 vs G0', 'GEO6IW5', 'G0', None),
      ('IWINV5 vs G0 (control)', 'IWINV5', 'G0', None), ('GEO6^IWINV5 vs GEO6 (control)', 'GEO6IWINV5', 'GEO6', None)]
for lab, dias in (('TRAIN 26-31 Oct', TR), ('HOLD 01-08 Nov', HO), ('TODO 12 d', DIAS)):
    P(f'\n== {lab} ({len(dias)} dias)')
    for v in ('G0', 'GEO6', 'IW5', 'GEO6IW5', 'IWINV5', 'GEO6IWINV5'): P(f'  {v:11s} ' + stat(v, dias))
    for nm, v, b, pl in CT: P(f'-- {nm}\n' + contrast(v, b, dias, pl))
P('\n== dPnL por dia (GEO6^IW5 - GEO6 | IW5 - G0 | GEO6 - G0)')
for d in DIAS:
    P(f"  {d}  {(perday('GEO6IW5', [d]) - perday('GEO6', [d])).iloc[0]:+7.1f} | {(perday('IW5', [d]) - perday('G0', [d])).iloc[0]:+7.1f} | {(perday('GEO6', [d]) - perday('G0', [d])).iloc[0]:+7.1f}")
open(H + 'out/ana_motor.txt', 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
