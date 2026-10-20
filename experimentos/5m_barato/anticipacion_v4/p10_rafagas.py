"""Rafagas (precio/tamano) y EV por T y banda de precio de R1/R2 con p1_fills (rival_D casado con WS)."""
import numpy as np, pandas as pd
A = pd.read_csv('/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/p1_fills.csv.gz', usecols=['dia','w','cierre','lado','p','acc','usd','fee','gana','ex','placebo','s5_ask','s5_bid','s5_asz','T_s','m15'])
A = A[(A.placebo == 0) & A.w.isin(['R1_9783', 'R2_e38c'])].sort_values('ex'); A['raf'] = A.ex // 60
G = A.groupby(['w', 'cierre', 'lado', 'raf']).agg(n=('p', 'size'), sh=('acc', 'sum'), usd=('usd', 'sum'), pmin=('p', 'min'), pmax=('p', 'max'), ndis=('p', 'nunique'), ask=('s5_ask', 'first'), asz=('s5_asz', 'first'), ex=('ex', 'first')).reset_index()
G['vwap'] = G.usd / G.sh
out = open('p10_out.txt', 'w')
def P(*a): print(*a); print(*a, file=out)
for w, g in G.groupby('w'):
    P(f'RAFAGAS {w}: n={len(g)} ordenes/rafaga P50/P90 {np.percentile(g.n,[50,90])} shares/rafaga P10/50/90 {np.percentile(g.sh,[10,50,90]).round(0)} niveles distintos P50/P90 {np.percentile(g.ndis,[50,90])}')
    P('   vwap-ask(ex-150) P10/50/90 (c):', (np.nanpercentile(g.vwap - g.ask, [10, 50, 90]) * 100).round(1), '| pmax-ask P50/P90 (c):', (np.nanpercentile(g.pmax - g.ask, [50, 90]) * 100).round(1), '| sh/tam. nivel1 P50:', np.nanmedian(g.sh / g.asz).round(2), '| rafagas con sh>nivel1:', np.nanmean(g.sh > g.asz).round(2), '| vwap<ask-1c:', np.nanmean(g.vwap < g.ask - 0.0099).round(2), '| pmax<=ask:', np.nanmean(g.pmax <= g.ask + 1e-9).round(2))
R = A.dropna(subset=['gana']).copy(); R['pnl'] = R.acc * (R.gana.astype(float) - R.p) - R.fee; R['c'] = R.usd + R.fee
rng = np.random.default_rng(2)
def ic(x):
    g = x.groupby('cierre')[['pnl', 'c']].sum().values
    if len(g) < 4: return (np.nan, np.nan)
    ix = rng.integers(0, len(g), (2000, len(g))); r = g[ix, 0].sum(1) / np.maximum(g[ix, 1].sum(1), 1e-9); return tuple(np.percentile(r, [5, 95]).round(2))
def tab(x, col, bins, nom):
    x = x.assign(b=pd.cut(x[col], bins)); 
    for b, g in x.groupby('b', observed=True):
        by = g.groupby('dia')[['pnl', 'c']].sum(); top = by.pnl.sort_values(ascending=False).index[:2]; y = g[~g.dia.isin(top)]
        P(f'  {nom} {str(b):14s} fills={len(g):5d} cierres={g.cierre.nunique():3d} coste={g.c.sum():8.0f} EV={g.pnl.sum()/g.c.sum():+.3f} IC90cierre={ic(g)} sin2mejores={(y.pnl.sum()/y.c.sum() if y.c.sum()>0 else np.nan):+.3f} dias+={(by.pnl>0).sum()}/{len(by)}')
for w in ['R1_9783', 'R2_e38c']:
    P('\n==', w); x = R[R.w == w]
    tab(x, 'p', [0, .15, .3, .5, .7, 1], 'precio'); tab(x, 'T_s', [0, 60, 120, 200, 300], 'T rest.')
