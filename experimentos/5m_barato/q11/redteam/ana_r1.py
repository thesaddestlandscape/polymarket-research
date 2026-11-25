#!/usr/bin/env python3
"""Red-team R1: sensibilidad de dPnL al modelo de relleno + diagnostico de fechado. Uso: python3 -I ana_r1.py > out/ana_r1.log"""
import glob, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
OUT = '/root/polymarket-research/experimentos/5m_barato/q11/redteam/out/'; BC = OUT + '../../barrido_corr/out/'
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(OUT + 'RT_*.pkl'))], ignore_index=True)
DG = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(OUT + 'DG_*.pkl'))], ignore_index=True)
rng = np.random.default_rng(11)
D7 = sorted(R[R.pol == 'PG_O50'].dia.unique()); D10 = sorted(R.dia.unique())
def evw(x): c = x.cost.sum(); return x.pnl.sum() / c if c > 0 else np.nan
# reproduccion
c5c = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(BC + 'RC5c_*.pkl'))]); c5d = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(BC + 'RC5d_*.pkl'))])
for pol, ref in (('PG_O50', c5c[c5c['var'] == 'PG_O50']), ('G0', c5d[c5d['var'] == 'G0']), ('GEO6', c5d[c5d['var'] == 'GEO6'])):
    m = R[(R.pol == pol) & (R.fv == 'BASE')]
    print(f'reproduccion BASE {pol}: mio n {len(m)} pnl {m.pnl.sum():+.1f} | barrido_corr n {len(ref)} pnl {ref.pnl.sum():+.1f}')
def delta(a, b, days, by='fin', B=4000):
    x = R[(R.dia.isin(days))]; pa = x[x.pol == a[0]][x.fv == a[1]].groupby(by).pnl.sum(); pb = x[x.pol == b[0]][x.fv == b[1]].groupby(by).pnl.sum()
    if by == 'fin':
        allf = x.fin.unique(); pa = pa.reindex(allf).fillna(0); pb = pb.reindex(allf).fillna(0)
    else:
        pa = pa.reindex(days).fillna(0); pb = pb.reindex(days).fillna(0)
    dl = (pa - pb).values; i = rng.integers(0, len(dl), (B, len(dl))); s = dl[i].sum(1)
    return dl.sum(), np.quantile(s, [.05, .95]), dl
def sin2d(a, b, days):
    _, _, dl = delta(a, b, days, by='dia'); return np.sort(dl)[:-2].sum(), int((dl > 0).sum()), len(dl)
FV = ['BASE', 'STRICT', 'OPT', 'CROSS', 'THIN']
print('\n== Totales por politica y modelo de relleno (dias PG = %s)' % D7)
for days, lab in ((D7, '7d'), (D10, '10d')):
    for pol in ('G0', 'GEO6', 'PG_O50'):
        if pol == 'PG_O50' and lab == '10d': continue
        s = []
        for f in FV:
            x = R[(R.pol == pol) & (R.fv == f) & R.dia.isin(days)]; s.append(f'{f} n{len(x)} {x.pnl.sum():+.1f} EV{evw(x):+.3f}')
        print(f' {lab} {pol:6s} | ' + ' | '.join(s))
print('\n== dPnL pareado (IC90 bootstrap por cierre / por dia), sin 2 mejores dias, dias>0')
for days, pairs in ((D7, [('PG_O50', 'G0'), ('GEO6', 'G0'), ('PG_O50', 'GEO6')]), (D10, [('GEO6', 'G0')])):
    for a, b in pairs:
        for f in FV:
            t, ic, _ = delta((a, f), (b, f), days); _, icd, _ = delta((a, f), (b, f), days, by='dia'); s2, dp, nd = sin2d((a, f), (b, f), days)
            print(f' {len(days)}d {a}-{b} [{f:6s}] {t:+7.1f} IC90c ({ic[0]:+.1f},{ic[1]:+.1f}) IC90d ({icd[0]:+.1f},{icd[1]:+.1f}) sin2 {s2:+.1f} dias+ {dp}/{nd}')
print('\n== Rellenos que CROSS anade/adelanta frente a BASE (mismo (k,L)): ')
for pol in ('G0', 'GEO6', 'PG_O50'):
    days = D7 if pol == 'PG_O50' else D10
    b = R[(R.pol == pol) & (R.fv == 'BASE') & R.dia.isin(days)].groupby(['dia', 'k', 'L']).agg(qb=('q', 'sum'), tb=('tf', 'min'))
    c = R[(R.pol == pol) & (R.fv == 'CROSS') & R.dia.isin(days)].groupby(['dia', 'k', 'L']).agg(qc=('q', 'sum'), tc=('tf', 'min'), gana=('gana', 'first'), fin=('fin', 'first'))
    j = c.join(b, how='outer'); j[['qb', 'qc']] = j[['qb', 'qc']].fillna(0)
    j = j.reset_index(); j['L'] = j.L.astype(float)
    nuevos = j[(j.qb == 0) & (j.qc > 0)]; adel = j[(j.qb > 0) & (j.qc > 0) & (j.tc < j.tb)]; igual = j[(j.qb > 0) & (j.qc > 0) & (j.tc >= j.tb)]; perd = j[(j.qb > 0) & (j.qc == 0)]
    def e(z, q):
        if len(z) == 0: return 'n0'
        cost = (z[q] * z.L).sum(); pnl = (z[q] * (z.gana - z.L)).sum(); return f'n{len(z)} pnl{pnl:+.1f} EV{pnl / cost:+.3f}'
    print(f' {pol}: (k,L) nuevos solo-CROSS {e(nuevos, "qc")} | adelantados {e(adel, "qb")} (mediana adelanto {np.median((adel.tb - adel.tc) / 1000) if len(adel) else np.nan:.1f} s) | igual {e(igual, "qb")}')
print('\n== Fechado de los rellenos BASE (DG): bid ya por debajo de L antes del relleno, y cruce posible antes')
for pol in ('G0', 'GEO6', 'PG_O50'):
    x = DG[DG.pol == pol]; arm_enc = (x.bid_arr < x.L - 1e-6); bel = x.t_below >= 0
    gap = (x.tf - x.t_below)[bel] / 1000.0; cr = x.t_cross >= 0
    print(f' {pol}: n {len(x)} | armada ya por encima del bid {arm_enc.mean():.3f} | bid<L antes del relleno {bel.mean():.3f} (desde que cae: mediana {gap.median():.1f} s, p75 {gap.quantile(.75):.1f}, p90 {gap.quantile(.9):.1f}) | cruce posible antes del relleno {cr.mean():.3f}'
          f' | mediana adelanto si cruce {((x.tf - x.t_cross)[cr] / 1000).median():.1f} s | mid tf-300 menos mid t*-300 (cruce) mediana {(x.m_tf300 - x.m_tc300)[cr].median():+.3f}')
print('\n== Descomposicion descuento/informacion con fecha BASE vs fecha temprana (t*=cruce si lo hay) en rellenos BASE')
for pol in ('G0', 'GEO6', 'PG_O50'):
    x = DG[DG.pol == pol].copy(); x['m_alt'] = np.where(x.t_cross >= 0, x.m_tc300, x.m_tf300); ok = x.m_tf300.notna() & x.m_alt.notna()
    x = x[ok]; c = x.L.sum()
    print(f' {pol}: n {len(x)} | fecha BASE desc {(x.m_tf300 - x.L).sum() / c:+.3f} info {(x.gana - x.m_tf300).sum() / c:+.3f} | fecha temprana desc {(x.m_alt - x.L).sum() / c:+.3f} info {(x.gana - x.m_alt).sum() / c:+.3f} (por accion, sin q)')
print('FIN')
