#!/usr/bin/env python3
"""describe.py b|pop DIAS -- que pasa tras el relleno: senales por tau en perdedoras vs ganadoras, AUC por dia, y calibracion
acierto real vs bid del momento (la salida solo gana si el bid sobrevalora la probabilidad tras la senal)."""
import sys, os, numpy as np, pandas as pd
DD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
def auc(x, y):
    m = ~np.isnan(x); x, y = x[m], y[m]
    if y.sum() == 0 or y.sum() == len(y): return np.nan
    r = pd.Series(x).rank().values; n1 = y.sum(); n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)
modo = sys.argv[1]; dias = sys.argv[2].split(',')
L = pd.concat([pd.read_csv(os.path.join(DD, f'largo_{modo}_{d}.csv')) for d in dias], ignore_index=True)
L['imb'] = np.where((L.fav + L.con) > 0, (L.fav - L.con) / (L.fav + L.con).clip(lower=1e-9), np.nan)
L['bsh'] = L.bsz / (L.bsz + L.asz)
L['bidrel'] = L.bid / L.p_fill
pd.set_option('display.width', 250)
for tau, g in L.groupby('tau'):
    print(f'\n--- tau={tau}s  n={len(g)} (ganadoras {g.gana.sum()})')
    for c in ('dbid', 'bnret', 'd15', 'imb', 'bsh', 'bid'):
        x = g[c].values.astype(float); y = g.gana.values
        aucs = [auc(h[c].values.astype(float), h.gana.values) for _, h in g.groupby('dia')]
        print(f'  {c:6s} perd media {np.nanmean(x[y==0]):+.4f} med {np.nanmedian(x[y==0]):+.4f} | gan media {np.nanmean(x[y==1]):+.4f} med {np.nanmedian(x[y==1]):+.4f} '
              f'| AUC(gana) {auc(x, y):.3f} por dia {" ".join(f"{a:.2f}" for a in aucs)} | n_na {np.isnan(x).sum()}')
    # calibracion: acierto vs bid de salida, por cuantiles del cambio de bid
    a = g[g.aplic == 1]
    if len(a):
        a = a.assign(q=pd.qcut(a.dbid.rank(method='first'), 4, labels=False))
        t = a.groupby('q').agg(n=('gana', 'size'), dbid_med=('dbid', 'median'), acierto=('gana', 'mean'), bid_exec=('bid_exec', 'mean'), p_fill=('p_fill', 'mean'),
                               salida_eur=('salida', 'sum'), payout_eur=('payout', 'sum'), coste=('coste', 'sum'))
        t['salida_menos_hold'] = t.salida_eur - t.payout_eur
        print('  por cuartil de dbid (cambio del bid propio vs precio de relleno):'); print(t.round(3).to_string())
