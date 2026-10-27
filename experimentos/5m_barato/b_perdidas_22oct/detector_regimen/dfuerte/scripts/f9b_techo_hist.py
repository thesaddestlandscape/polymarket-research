#!/usr/bin/env python3
"""f9b - techo con mid reconstruido (CLOB prices-history, PROXY ~60 s) en ventanas-unidad de S_A (FASE T, oos de M10). mid_open = ultimo punto <= t_o; mid_T = ultimo punto <= t_o+180 s."""
import json, glob, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
D = '/mnt/HC_Volume_106538179/agentes_datos/dfuerte'; R = '/root/polymarket-research-datalogs/regimen_5m/dfuerte'; RNG = np.random.default_rng(9)
rec = []
for l in open(f'{D}/hist_backfill.jsonl'):
    h = json.loads(l)
    if 'pts' not in h or not h['pts']: continue
    to = h['tmin'] * 60; p = [x for x in h['pts'] if x[0] <= to]; pT = [x for x in h['pts'] if x[0] <= to + 180]; pl = [x for x in h['pts'] if to - 180 <= x[0] <= to]
    rec.append((h['coin'], h['tmin'], p[-1][1] if p else np.nan, to - p[-1][0] if p else np.nan, pT[-1][1] if pT else np.nan, pl[0][1] if pl else np.nan))
H = pd.DataFrame(rec, columns=['coin', 'tmin', 'h_open', 'age_open', 'h_T', 'h_m3']).drop_duplicates(['coin', 'tmin'])
O = pd.read_pickle(f'{R}/oos_T180.pkl'); O = O[O.fase == 'T'].merge(H, on=['coin', 'tmin']); O = O[O.src == 'backfill'].reset_index(drop=True)
O['dstr'] = pd.to_datetime(O.dia * 86400, unit='s').dt.strftime('%Y-%m-%d')
O['mid_con_open'] = np.where(O.o > 0, O.h_open, 1 - O.h_open); O['mid_con_T'] = np.where(O.o > 0, O.h_T, 1 - O.h_T); O['dis'] = O.mid_con_T - O.pcon; O['adis'] = O.dis.abs(); O['dmid'] = O.mid_con_T - O.mid_con_open
O['lpc'] = np.log(O.pcon / (1 - O.pcon)); O['qb'] = (O.pcon / 0.05).round().astype(int)
print('unidades con mid reconstruido', len(O), 'dias', O.dstr.nunique(), O.dstr.min(), O.dstr.max(), 'edad mediana del punto de apertura (s)', O.age_open.median())
SETS = {'base': ['s_M10'], 'open': ['s_M10', 'mid_con_open'], 'open+T': ['s_M10', 'mid_con_open', 'mid_con_T', 'dis', 'adis', 'dmid']}
def auc(df, s):
    d = df.assign(r=df.groupby('qb')[s].rank()); g = d.groupby('qb'); n1 = g.y.sum(); n = g.y.size(); n0 = n - n1; sr = d[d.y == 1].groupby('qb').r.sum(); u = (sr - n1 * (n1 + 1) / 2).reindex(n1.index).fillna(0); return float(u.sum() / (n1 * n0).sum())
ds = sorted(O.dstr.unique()); k0 = max(7, len(ds) // 3); test = ds[k0:]
for lr in ('LOG', 'GBM'):
    for sn, cols in SETS.items():
        sc = pd.Series(np.nan, index=O.index)
        for d in test:
            tr = O[O.dstr < d]; te = O[O.dstr == d]
            m = make_pipeline(SimpleImputer(strategy='median'), StandardScaler(), LogisticRegression(C=1.0, max_iter=400)) if lr == 'LOG' else HistGradientBoostingClassifier(max_depth=2, max_iter=100, learning_rate=0.05, min_samples_leaf=100, l2_regularization=10, early_stopping=False, random_state=1)
            m.fit(tr[cols].values.astype(float), tr.y.values); sc[te.index] = m.predict_proba(te[cols].values.astype(float))[:, 1] - te.pcon.values
        O[f's_{lr}_{sn}'] = sc
T = O[O.dstr.isin(test)].reset_index(drop=True); print(f'TEST {test[0]}..{test[-1]} ({len(test)} d, {len(T)} unidades); AUC s_M10 sin reentrenar {auc(T, "s_M10"):.4f}')
dd = sorted(T.dstr.unique()); g = {d: T[T.dstr == d].index.values for d in dd}
def dboot(a, b, nb=500):
    v = []
    for _ in range(nb):
        ix = np.concatenate([g[d] for d in RNG.choice(dd, len(dd))]); X = T.loc[ix].reset_index(drop=True); v.append(auc(X, b) - auc(X, a))
    return np.percentile(v, [5, 95])
for lr in ('LOG', 'GBM'):
    b0 = auc(T, f's_{lr}_base'); print(f'{lr} base: AUC {b0:.4f}')
    for sn in ('open', 'open+T'):
        a = auc(T, f's_{lr}_{sn}'); ci = dboot(f's_{lr}_base', f's_{lr}_{sn}'); print(f'{lr} +{sn}: AUC {a:.4f} ganancia {a-b0:+.4f} IC90 dias ({ci[0]:+.4f},{ci[1]:+.4f})')
print('univariable: ' + ', '.join(f'{c} {auc(T.assign(z=T[c].fillna(T[c].median())), "z"):.3f}' for c in ['mid_con_open', 'mid_con_T', 'dis', 'adis', 'dmid']))
