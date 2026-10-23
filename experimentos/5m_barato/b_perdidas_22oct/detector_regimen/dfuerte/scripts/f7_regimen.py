import numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
R = '/root/polymarket-research-datalogs/regimen_5m'; O = pd.read_pickle(f'{R}/dfuerte/oos_T180.pkl'); O['e'] = O.win - O.q
dr = {}
for s in ('y2025', 'dic_ene', 'backfill', 'reciente'):
    z = np.load(f'{R}/full_{s}.npz'); m0 = int(z['BTC_m0']); P = pd.Series(z['BTC_X'][:, 0], index=(m0 + np.arange(len(z['BTC_X']))) // 1440)
    g = P.groupby(level=0); d = (g.last() / g.first() - 1) * 100; dr.update(d.to_dict())
O['btcday'] = O.dia.map(dr); O['dir_day'] = np.where(O.btcday > 0.3, 'ALCISTA', np.where(O.btcday < -0.3, 'BAJISTA', 'LATERAL'))
O['pretrend'] = np.where(O.rpre > 0, 'rpre+', 'rpre-')
def ev(x): return x.e.sum() / x.q.sum() if len(x) > 30 else np.nan
for fase in ('T', 'R'):
    X = O[O.fase == fase].copy(); lo = X.s_M10.quantile(1 / 3); hi = X.s_M10.quantile(2 / 3); X['cls'] = np.where(X.s_M10 <= lo, 'BAD', np.where(X.s_M10 >= hi, 'GOOD', 'MID'))
    print(f'\n=== fase {fase}: EV/EUR por regimen del dia (BTC ex-post) x tendencia previa; CON/CONTRA global y dentro de la clase del detector (BAD=tercil inf de s_hat) ===')
    print('dir_dia  pretend  n   %BAD |  EV(CON) EV(CONTRA) Delta | BAD: EV(CON) EV(CONTRA) Delta | GOOD: EV(CON) EV(CONTRA) Delta | skip CON&s<=c0.25: dP exceso-aprox')
    for (d, p), g in X.groupby(['dir_day', 'pretrend']):
        a, b = g[g.con == 1], g[g.con == 0]; ba, bb = a[a.cls == 'BAD'], b[b.cls == 'BAD']; ga, gb = a[a.cls == 'GOOD'], b[b.cls == 'GOOD']
        print(f'{d:9s}{p:6s}{len(g):6d} {np.mean(g.cls=="BAD")*100:5.1f} | {ev(a):+.3f} {ev(b):+.3f} {ev(a)-ev(b):+.3f} | {ev(ba):+.3f} {ev(bb):+.3f} {ev(ba)-ev(bb):+.3f} | {ev(ga):+.3f} {ev(gb):+.3f} {ev(ga)-ev(gb):+.3f}')
    print('dias por regimen:', X.groupby('dir_day').dia.nunique().to_dict())
