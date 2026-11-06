#!/usr/bin/env python3
"""Analisis toxicidad thru1 (DISENO_T.md sha 36e49c0c). EXPLORATORIO, dias quemados. Unidad: cierre (fin); IC bootstrap por cierre y por dia; EV ponderado por EUR."""
import glob, numpy as np, pandas as pd
O = '/root/polymarket-research/experimentos/5m_barato/q11/toxicidad_thru1/out/'
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(O + 'RT_*.pkl'))]); S = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(O + 'SEGT_*.pkl'))])
S['cost'] = S.q * S.L; S['pnl'] = S.q * (S.gana - S.L) + S.q * 0.2 * 0.07 * S.L * (1 - S.L)
DIAS = sorted(R.dia.unique()); OOS = [x for x in DIAS if x >= '2026-11-01']; FINS = np.array(sorted(S.fin.unique())); FD = S.groupby('fin').dia.first()
rng = np.random.default_rng(7); NB = 4000
def boot(v, qs=(5, 95, 1.25, 98.75)):
    v = np.asarray(v, float); n = len(v)
    if n < 2: return [np.nan] * len(qs) + [np.nan]
    m = v[rng.integers(0, n, (NB, n))].sum(1); return [np.percentile(m, q) for q in qs] + [float((m <= 0).mean())]
def per_fin(x, dias): return x[x.dia.isin(dias)].groupby('fin').pnl.sum().reindex([f for f in FINS if FD[f] in dias], fill_value=0.0)
def resumen(v, dias, base='G0'):
    x = R[(R['var'] == v) & R.dia.isin(dias)]; b = R[(R['var'] == base) & R.dia.isin(dias)]
    pd_ = x.groupby('dia').pnl.sum().reindex(dias, fill_value=0); cd = x.groupby('dia').cost.sum().reindex(dias, fill_value=0)
    top2 = pd_.sort_values().index[-2:]; s2 = (pd_.drop(top2).sum() / cd.drop(top2).sum()) if cd.drop(top2).sum() > 0 else np.nan
    dl = per_fin(x, dias) - per_fin(b, dias); dd = x.groupby('dia').pnl.sum().reindex(dias, fill_value=0) - b.groupby('dia').pnl.sum().reindex(dias, fill_value=0)
    bf = boot(dl.values); bd = boot(dd.values)
    return dict(n=len(x), eur=x.cost.sum(), pnl=x.pnl.sum(), ev=x.pnl.sum() / x.cost.sum() if x.cost.sum() > 0 else np.nan, sin2=s2, diasp=int((pd_ > 0).sum()),
                thru1=float((x.ftype == 'thru1').mean()), d=dl.sum(), ic=(bf[0], bf[1]), ic4=(bf[2], bf[3]), pb=bf[4], icd=(bd[0], bd[1]), ddp=int((dd > 0).sum()), nd=len(dias))
def fmt(v, r): return (f"{v:10s} n {r['n']:5d} EUR {r['eur']:7.1f} pnl {r['pnl']:+7.1f} EV {r['ev']:+.3f} sin2 {r['sin2']:+.3f} dias+ {r['diasp']}/{r['nd']} thru1 {r['thru1']:.2f} | dPnL {r['d']:+7.1f} "
                       f"IC90cie ({r['ic'][0]:+.1f},{r['ic'][1]:+.1f}) IC97.5cie ({r['ic4'][0]:+.1f},{r['ic4'][1]:+.1f}) IC90dia ({r['icd'][0]:+.1f},{r['icd'][1]:+.1f}) p(d<=0) {r['pb']:.3f} dias d>0 {r['ddp']}/{r['nd']}")
VAR = ['G0', 'GEO6', 'NJ3', 'NJ3A', 'CALM3', 'GEO6NJ3', 'CXB150', 'CXB300', 'CXB1000', 'CXB3000', 'CXJ150', 'CXJ1000']
for lab, dias in (('10 DIAS (quemados)', DIAS), ('OOS 01-04 Nov', OOS), ('TRAIN 26-31 Oct', [x for x in DIAS if x not in OOS])):
    print(f'\n== {lab}: {len(dias)} dias, cierres {sum(FD[f] in dias for f in FINS)}')
    RES = {v: resumen(v, dias) for v in VAR}
    for v in VAR: print(fmt(v, RES[v]))
    for fam, obs in (('PNJ3A_', 'NJ3A'), ('PCXB300_', 'CXB300')):
        pl = np.array([resumen(v, dias)['d'] for v in sorted(R['var'].unique()) if v.startswith(fam)]); o = RES[obs]['d']; mu = pl.mean()
        p_raw = (1 + (np.abs(pl) >= abs(o)).sum()) / (1 + len(pl)); p_cen = (1 + (np.abs(pl - mu) >= abs(o - mu)).sum()) / (1 + len(pl))
        print(f'  placebo {fam}: n {len(pl)} dPnL media {mu:+.1f} [{pl.min():+.1f},{pl.max():+.1f}] obs {obs} {o:+.1f} p_bilat(|.|) {p_raw:.3f} p_bilat(centrado) {p_cen:.3f}')
print('\n== Descomposicion G0 por segmento (10 dias): segs, P(relleno), EV|relleno [IC90 cierre del pnl], EUR/seg, frac thru1')
S['bidLc'] = pd.cut(S.bidL, [-9, 0.02 - 1e-6, 0.04 - 1e-6, 0.06 - 1e-6, 0.08 - 1e-6, 9], labels=['<2c', '2-4c', '4-6c', '6-8c', '>=8c'])
S['Tc'] = pd.cut(S['T'], [0, 120, 200, 400], labels=['<120', '120-200', '>=200']); S['r3adv'] = np.where(S.r3.isna(), 'NaN', np.where(S.r3 <= -3, 'adv>=3', np.where(S.r3 >= 3, 'fav>=3', 'calma')))
S['fill'] = S.q > 1e-9
def dec(gr):
    for key, x in gr:
        f = x[x.fill]; bf = boot(f.groupby('fin').pnl.sum().values) if len(f) else [np.nan] * 5
        print(f'  {str(key):22s} segs {len(x):6d} P(rell) {x.fill.mean():.3f} rell {len(f):5d} EV|rell {f.pnl.sum() / max(f.cost.sum(), 1e-9):+.3f} pnl {f.pnl.sum():+7.1f} '
              f'IC90cie ({bf[0]:+.1f},{bf[1]:+.1f}) EUR/seg {x.pnl.sum() / len(x):+.4f} thru1 {(f.ftype == "thru1").mean() if len(f) else np.nan:.2f} EV|thru1 {f[f.ftype == "thru1"].pnl.sum() / max(f[f.ftype == "thru1"].cost.sum(), 1e-9):+.3f}')
for col in ('bidLc', 'Tc', 'r3adv', 'act', 'lado'): print(f' -- por {col}'); dec(S.groupby(col, observed=True))
print(' -- bidL x r3adv'); dec(S.groupby(['bidLc', 'r3adv'], observed=True))
print(' -- por tipo de relleno'); dec(S[S.fill].groupby('ftype'))
f = S[S.fill]; nn = f.r3.isna(); a = f[nn]; b = f[~nn]
ga = a.groupby('fin').pnl.sum(); gb = b.groupby('fin').pnl.sum()
print(f'\n== NaN r3 (rellenos G0): NaN n {len(a)} EV {a.pnl.sum() / max(a.cost.sum(), 1e-9):+.3f} | no NaN n {len(b)} EV {b.pnl.sum() / max(b.cost.sum(), 1e-9):+.3f}; dias con NaN: {a.dia.value_counts().to_dict()}')
if len(a) > 5:
    fins = np.array(sorted(set(ga.index) | set(gb.index))); A_ = ga.reindex(fins, fill_value=0).values; B_ = gb.reindex(fins, fill_value=0).values
    ca = a.groupby('fin').cost.sum().reindex(fins, fill_value=0).values; cb = b.groupby('fin').cost.sum().reindex(fins, fill_value=0).values
    ix = rng.integers(0, len(fins), (NB, len(fins))); dif = A_[ix].sum(1) / np.maximum(ca[ix].sum(1), 1e-9) - B_[ix].sum(1) / np.maximum(cb[ix].sum(1), 1e-9)
    print(f'   diferencia EV NaN - noNaN IC90 cierre ({np.percentile(dif, 5):+.3f},{np.percentile(dif, 95):+.3f})')
print('\n== Curva de latencia de cancelacion CXB_l (10 dias / OOS): ', {v: (round(resumen(v, DIAS)['d'], 1), round(resumen(v, OOS)['d'], 1)) for v in ['CXB150', 'CXB300', 'CXB1000', 'CXB3000']})
print('== cancelaciones por variante:', R[R['var'].isin(VAR)].groupby('var').canc.mean().round(3).to_dict())
