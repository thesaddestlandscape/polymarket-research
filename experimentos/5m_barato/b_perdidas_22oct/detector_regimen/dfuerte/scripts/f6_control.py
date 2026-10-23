import sys, os, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
O = pd.read_pickle('/root/polymarket-research-datalogs/regimen_5m/dfuerte/oos_T180_ctrl.pkl')
def auc(df, s, w):
    d = df.assign(qb=(df.pcon / w).round().astype(int)); d['r'] = d.groupby('qb')[s].rank(); g = d.groupby('qb'); n1 = g.y.sum(); n = g.y.size(); n0 = n - n1
    sr = d[d.y == 1].groupby('qb').r.sum(); U = (sr - n1 * (n1 + 1) / 2).reindex(n1.index).fillna(0); return float(U.sum() / (n1 * n0).sum())
print('AUC estratificada por ancho de cubo de p_con (0.05 / 0.01 / 0.002) y SOLO dentro de moneda x cubo 0.01')
for ph in ('D', 'T', 'R'):
    X = O[O.fase == ph].reset_index(drop=True)
    for m in ('M10', 'M9', 'C0G', 'C7G', 'C8G', 'C0'):
        s = 's_' + m; X['cm'] = X.coin; r = [auc(X, s, w) for w in (0.05, 0.01, 0.002)]
        rc = np.mean([auc(g.reset_index(drop=True), s, 0.01) for c, g in X.groupby('coin')])
        # correlacion de s con pcon dentro de cubo 0.01
        X['b'] = (X.pcon / 0.01).round(); cc = X.groupby('b').apply(lambda g: g[s].corr(g.pcon) if len(g) > 50 else np.nan).mean()
        print(f'{ph} {m:4s} AUC {r[0]:.4f} {r[1]:.4f} {r[2]:.4f} | por moneda(0.01) {rc:.4f} | corr(s,pcon|cubo) {cc:+.3f}')
