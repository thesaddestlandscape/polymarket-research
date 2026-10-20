"""Dinamica de las rafagas de R1/R2: EV por indice de rafaga y por direccion del precio respecto a la rafaga previa de la misma unidad; bolsillo T>200 por precio. Ponderado por EUR."""
import numpy as np, pandas as pd
A = pd.read_csv('/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/p1_fills.csv.gz', usecols=['dia','w','cierre','lado','p','acc','usd','fee','gana','ex','placebo','T_s','s5_ask','m15'])
A = A[(A.placebo == 0) & A.w.isin(['R1_9783', 'R2_e38c'])].dropna(subset=['gana']).sort_values('ex'); A['raf'] = A.ex // 60
G = A.groupby(['w', 'dia', 'cierre', 'lado', 'raf']).agg(sh=('acc', 'sum'), usd=('usd', 'sum'), fee=('fee', 'sum'), gana=('gana', 'first'), ex=('ex', 'first'), T=('T_s', 'first'), m=('m15', 'first')).reset_index().sort_values('ex')
G['p'] = G.usd / G.sh; G['k'] = G.groupby(['w', 'cierre', 'lado']).cumcount(); G['dp'] = G.groupby(['w', 'cierre', 'lado']).p.diff()
G['dt'] = G.groupby(['w', 'cierre', 'lado']).ex.diff() / 1000
G['pnl'] = G.sh * G.gana.astype(float) - G.usd - G.fee; G['c'] = G.usd + G.fee
G['inv'] = G.groupby(['w', 'cierre', 'lado']).sh.cumsum() - G.sh      # acciones ya compradas antes
rng = np.random.default_rng(4)
def ic(x):
    g = x.groupby('cierre')[['pnl', 'c']].sum().values
    if len(g) < 4: return (np.nan, np.nan)
    ix = rng.integers(0, len(g), (2000, len(g))); r = g[ix, 0].sum(1) / np.maximum(g[ix, 1].sum(1), 1e-9); return tuple(np.percentile(r, [5, 95]).round(2))
def row(x, nom):
    if len(x) < 5 or x.c.sum() <= 0: print(f'  {nom:34s} n={len(x)}'); return
    by = x.groupby('dia')[['pnl', 'c']].sum(); top = by.pnl.sort_values(ascending=False).index[:2]; y = x[~x.dia.isin(top)]
    print(f'  {nom:34s} rafagas={len(x):5d} cierres={x.cierre.nunique():3d} coste={x.c.sum():8.0f} EV={x.pnl.sum()/x.c.sum():+.3f} IC90cierre={ic(x)} sin2mejores={(y.pnl.sum()/y.c.sum() if y.c.sum()>0 else np.nan):+.3f} dias+={(by.pnl>0).sum()}/{len(by)}')
for w in ['R1_9783', 'R2_e38c']:
    g = G[G.w == w]; print('\n==', w)
    for nom, x in (('k=0 (1a rafaga)', g[g.k == 0]), ('k=1', g[g.k == 1]), ('k=2-4', g[(g.k >= 2) & (g.k <= 4)]), ('k>=5', g[g.k >= 5])): row(x, nom)
    s = g[g.k >= 1]
    for nom, x in (('k>=1 precio SUBE >=1c vs previa', s[s.dp >= 0.0099]), ('k>=1 precio igual (|dp|<1c)', s[s.dp.abs() < 0.0099]), ('k>=1 precio BAJA >=1c', s[s.dp <= -0.0099])): row(x, nom)
    for nom, x in (('k>=1 dt<1 s', s[s.dt < 1]), ('k>=1 dt 1-10 s', s[(s.dt >= 1) & (s.dt < 10)]), ('k>=1 dt>=10 s', s[s.dt >= 10])): row(x, nom)
    e = g[g['T'] > 200]
    for lo, hi in ((0, .3), (.3, .5), (.5, .7), (.7, 1.01)): row(e[(e.p > lo) & (e.p <= hi)], f'T>200 precio ({lo},{hi}]')
    row(g[(g['T'] > 200) & (g.k == 0)], 'T>200 y 1a rafaga')
