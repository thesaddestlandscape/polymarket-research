#!/usr/bin/env python3
"""e1d_r1_robustez.py -- control post hoc (NO prereg) de R1: ¿la vol baja es hueco del grabador Binance? Calcula por ventana la fraccion de puntos de 10 s
en [t0-900,t0] con ultimo aggTrade > 10 s (stale) y nº de aggTrades, y repite el walk-forward de R1 excluyendo ventanas con stale > 0,05. Salida datos/e1d_r1_robustez.txt"""
import os, gzip, glob, numpy as np, pandas as pd
OUT = '/root/polymarket-research-datalogs/e1_cancelacion_ms/'; D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
F = pd.read_csv(OUT + 'e1d_rellenos.csv.gz', dtype={'mid': str}); W = pd.read_csv(OUT + 'e1d_ventanas.csv.gz', dtype={'mid': str})
M = F.groupby(['coin', 'mid']).agg(pnl=('pnl', 'sum'), coste=('coste', 'sum')).reset_index(); W = W.merge(M, on=['coin', 'mid'], how='left').fillna({'pnl': 0, 'coste': 0})
X = {c: [] for c in ('ETH', 'SOL', 'XRP')}
for f in sorted(glob.glob(OUT + 'reg/2026-10-??.gz')):
    with gzip.open(f, 'rt') as fh:
        for ln in fh:
            if ln[0] == 'x':
                c = ln.split(',')
                try: X[c[2]].append(int(c[1]))
                except (ValueError, IndexError, KeyError): pass
X = {c: np.unique(np.array(v, np.int64)) for c, v in X.items()}
st = np.zeros(len(W)); nx = np.zeros(len(W))
for i, (c, fin) in enumerate(zip(W.coin.values, W.fin.values)):
    t0 = int((fin - 300) * 1000); g = np.arange(t0 - 900000, t0 + 1, 10000); a = X[c]
    j = np.searchsorted(a, g, 'right') - 1; age = np.where(j >= 0, g - a[np.maximum(j, 0)], 10**9); st[i] = (age > 10000).mean()
    nx[i] = np.searchsorted(a, t0, 'right') - np.searchsorted(a, t0 - 900000, 'right')
W['stale'] = st; W['nx'] = nx; out = []
def P(*a): out.append(' '.join(map(str, a))); print(*a)
P('stale>0,05:', round((W.stale > 0.05).mean(), 3), '| Spearman R1~stale', round(W[['R1', 'stale']].corr('spearman').iloc[0, 1], 3), '| R1~nx', round(W[['R1', 'nx']].corr('spearman').iloc[0, 1], 3))
W['t'] = pd.qcut(W.R1, 3, labels=['bajo', 'medio', 'alto']); P('stale medio por tercil R1:', W.groupby('t', observed=True).stale.mean().round(3).to_dict())
ev = lambda d: d.pnl.sum() / d.coste.sum()
for lab, Wx in (('TODAS', W), ('stale<=0,05', W[W.stale <= 0.05])):
    dias = sorted(Wx.dia.unique()); exc = []; dp = 0
    for i, d in enumerate(dias):
        if i < 3: continue
        tr = Wx[Wx.dia < d]; te = Wx[Wx.dia == d]; c1 = np.quantile(tr.R1.dropna(), 1 / 3); sk = (te.R1 <= c1) & te.R1.notna()
        exc.append(-te[sk].pnl.sum() + sk.sum() / len(te) * te.pnl.sum()); dp += -te[sk].pnl.sum()
    exc = np.array(exc); P(f'{lab}: ventanas {len(Wx)} | R1 walk-forward EXCESO {exc.sum():+.0f} dPnL {dp:+.0f} | dias >0 {(exc>0).sum()}/{len(exc)} | sin 2 mejores {np.sort(exc)[:-2].sum():+.0f}')
    for c, g in Wx.groupby('coin'):
        q = pd.qcut(g.R1, 3, labels=False, duplicates='drop'); P(f'   {c} EV por tercil propio de R1 (descriptivo): {[round(ev(g[q == k]), 3) for k in range(3)]}')
open(os.path.join(D, 'e1d_r1_robustez.txt'), 'w').write('\n'.join(out) + '\n')
