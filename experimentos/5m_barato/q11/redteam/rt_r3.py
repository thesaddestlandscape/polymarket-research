#!/usr/bin/env python3
"""Red-team R3 (DISENO_RT.md): multiplicidad (max-t por cierre sobre la familia de politicas candidatas probadas en los mismos 7 dias), regimen por lado,
reposicion, potencia del criterio «supera a GEO6». Solo pkl existentes. Uso: python3 -I rt_r3.py > out/rt_r3.log"""
import glob, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
BC = '/root/polymarket-research/experimentos/5m_barato/q11/barrido_corr/out/'; OUT = '/root/polymarket-research/experimentos/5m_barato/q11/redteam/out/'
rng = np.random.default_rng(5)
D7 = ['2026-10-29', '2026-10-30', '2026-10-31', '2026-11-01', '2026-11-02', '2026-11-03', '2026-11-04']
allR = []
for p in ('RC3', 'RC5', 'RC5b', 'RC5c', 'RC5d'):
    x = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(BC + p + '_*.pkl'))]); x = x[x.dia.isin(D7)]; x['src'] = p; allR.append(x)
R = pd.concat(allR, ignore_index=True)
g0 = R[(R['var'] == 'G0') & (R.src == 'RC5d')]
cand = sorted({v for v in R['var'].unique() if not (v.startswith('PGP') or v.startswith('PLA') or v.startswith('PGI') or v.startswith('INV') or v == 'G0')})
fins = np.unique(R.fin.values)
M = {}
for v in cand:
    x = R[R['var'] == v]; x = x[x.src == x.src.iloc[0]]
    M[v] = x.groupby('fin').pnl.sum().reindex(fins).fillna(0).values - g0.groupby('fin').pnl.sum().reindex(fins).fillna(0).values
V = list(M); A = np.vstack([M[v] for v in V]); n = A.shape[1]
obs = A.sum(1); se = A.std(1, ddof=1) * np.sqrt(n); tobs = obs / se
B = 5000; mx = np.empty(B)
for b in range(B):
    i = rng.integers(0, n, n); s = A[:, i].sum(1); seb = A[:, i].std(1, ddof=1) * np.sqrt(n); mx[b] = np.max((s - obs) / seb)
print(f'== Familia de politicas candidatas en los mismos 7 dias OOS (sin placebos/inversiones): {len(V)}: {V}')
for v, o, t in sorted(zip(V, obs, tobs), key=lambda z: -z[2]):
    print(f'  {v:10s} dPnL vs G0 {o:+7.1f} t {t:+.2f} p_max-t {float(np.mean(mx >= t)):.4f}')
# regimen por lado
X = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(OUT + 'RT_*.pkl'))]); X = X[X.fv == 'BASE']
print('\n== Regimen: pnl por dia y lado (BASE); dPnL PG_O50-G0 y GEO6-G0 por lado')
t = X.groupby(['dia', 'pol', 'lado']).pnl.sum().unstack(['pol', 'lado']).round(1)
print(t.to_string())
for lado in ('YES', 'NO'):
    a = t.get(('PG_O50', lado)); b = t.get(('G0', lado)); c = t.get(('GEO6', lado))
    dd = (a - b).dropna(); de = (c - b)
    print(f' lado {lado}: dPG-G0 total {dd.sum():+.1f} dias+ {(dd > 0).sum()}/{len(dd)} | dGEO6-G0 total {de.sum():+.1f} dias+ {(de > 0).sum()}/{len(de)}')
gN = t[('G0', 'NO')]; dN = (t[('PG_O50', 'NO')] - gN).dropna()
print(' dias con G0 lado NO >= 0:', gN[gN >= 0].index.tolist(), '| dPG-G0 lado NO en esos dias:', dN.reindex(gN[gN >= 0].index).round(1).tolist())
# tasa de victoria por lado del universo (tokens con relleno G0 o no): aproximacion con tokens rellenados por G0 BASE
w = X[X.pol == 'G0'].drop_duplicates(['dia', 'k']).groupby(['dia', 'lado']).gana.mean().unstack().round(3); print(' P(gana) de los tokens rellenados por G0, por dia y lado:\n' + w.to_string())
# reposicion: rellenos por segmento
print('\n== Reposicion: rellenos por numero de segmento (seg=0 primera colocacion)')
for pol in ('G0', 'GEO6', 'PG_O50'):
    x = X[X.pol == pol]
    print(f' {pol}: ' + ' | '.join(f'seg{s if s < 3 else "3+"} n{len(z)} pnl{z.pnl.sum():+.1f} EV{z.pnl.sum() / z.cost.sum():+.3f}' for s, z in x.groupby(np.minimum(x.seg, 3))))
# doble conteo: ambos lados del mismo mercado rellenados
print('\n== Ambos lados del mismo mercado rellenados (pares) y concentracion por cierre')
for pol in ('G0', 'GEO6', 'PG_O50'):
    x = X[X.pol == pol]; s = x.groupby('fin').pnl.sum(); top = s.abs().sort_values(ascending=False)
    pares = x.groupby(['fin', 'act']).lado.nunique(); 
    print(f' {pol}: cierres {s.size} | mercados con ambos lados {int((pares == 2).sum())}/{pares.size} | pnl sin el mejor cierre {s.sum() - s.max():+.1f} (total {s.sum():+.1f}) | top5 cierres {s.nlargest(5).round(1).tolist()}')
# potencia del criterio supera a GEO6
a = X[X.pol == 'PG_O50'].groupby('dia').pnl.sum().reindex(D7).fillna(0); b = X[X.pol == 'GEO6'].groupby('dia').pnl.sum().reindex(D7).fillna(0)
dd = a - b; m, sd = dd.mean(), dd.std(ddof=1)
print(f'\n== PG_O50-GEO6 por dia (BASE): media {m:+.1f} EUR/dia, sd {sd:.1f}; dias para IC90 por dia > 0 si la media se mantiene: {(1.645 * sd / m) ** 2 if m > 0 else np.inf:.1f}; si se retiene el 28 %: {(1.645 * sd / (0.28 * m)) ** 2 if m > 0 else np.inf:.0f}')
# concentracion de dPnL por cierre (BASE y CROSS)
Y = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(OUT + 'RT_*.pkl'))])
print('\n== dPnL sin los 5 cierres que mas aportan a la diferencia')
for fv in ('BASE', 'CROSS'):
    for a, b, days in (('PG_O50', 'G0', D7), ('GEO6', 'G0', D7), ('PG_O50', 'GEO6', D7)):
        y = Y[(Y.fv == fv) & Y.dia.isin(days)]; fs = np.unique(y.fin.values)
        dl = y[y.pol == a].groupby('fin').pnl.sum().reindex(fs).fillna(0) - y[y.pol == b].groupby('fin').pnl.sum().reindex(fs).fillna(0)
        print(f' [{fv}] {a}-{b}: total {dl.sum():+.1f} | sin top5 cierres {dl.sum() - dl.nlargest(5).sum():+.1f} | sin top10 {dl.sum() - dl.nlargest(10).sum():+.1f} | cierres con dif!=0 {(dl != 0).sum()}')
print('FIN')
