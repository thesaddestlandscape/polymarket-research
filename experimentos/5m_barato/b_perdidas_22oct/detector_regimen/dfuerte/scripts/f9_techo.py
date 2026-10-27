#!/usr/bin/env python3
"""f9_techo.py - PREREG_DFUERTE_R3 sec.B: techo teorico con mid/desacuerdo del mercado (m5_registro 5-21 Oct). Semilla fija."""
import os, sys, subprocess, numpy as np, pandas as pd, warnings, io, datetime as dt
warnings.filterwarnings('ignore')
D = '/mnt/HC_Volume_106538179/agentes_datos/dfuerte'; R = '/root/polymarket-research-datalogs/regimen_5m/dfuerte'; RNG = np.random.default_rng(7)
days = [f'2026-10-{d:02d}' for d in range(5, 22)]; rows = []
for d in days:
    p = f'{D}/mid/{d}.csv.gz'
    if not os.path.exists(p): continue
    k = pd.read_csv(io.StringIO(subprocess.run(f"zcat /mnt/HC_Volume_106538179/m5_registro/m5_registro_{d}.csv.gz | awk -F, '$1==\"k\" && ($5==\"5min\"||$5==\"15min\"){{print $3\",\"$4\",\"$5\",\"$6\",\"$7\",\"$8}}'", shell=True, capture_output=True, text=True).stdout), names=['token', 'coin', 'tf', 'mid_', 'end', 'side'], dtype={'token': str})
    k['end_s'] = pd.to_datetime(k.end).astype('int64') // 10 ** 9 if False else pd.to_datetime(k.end, utc=True).map(lambda x: int(x.timestamp()))
    q = pd.read_csv(p, names=['t', 'token', 'bid', 'ask'], dtype={'token': str}); q['mid'] = (q.bid + q.ask) / 2; q = q[(q.bid > 0) & (q.ask > 0) & (q.ask >= q.bid)]
    q = q.merge(k[['token', 'coin', 'tf', 'end_s', 'side']], on='token'); q = q[q.side == 'YES'].sort_values('t'); q['day'] = d; rows.append(q)
Q = pd.concat(rows, ignore_index=True); print('cotizaciones YES', len(Q), Q.day.nunique(), 'dias', flush=True)
U = pd.read_pickle(f'{R}/oos_T180.pkl'); U = U[(U.fase == 'R')].copy(); U['dstr'] = pd.to_datetime(U.dia * 86400, unit='s').dt.strftime('%Y-%m-%d'); U = U[U.dstr.isin(days) & U.coin.isin(['BTC', 'ETH', 'SOL', 'XRP'])].reset_index(drop=True)
U['to'] = U.tmin * 60
# implementacion directa por moneda: 5m (token con end-300 == to) y 15m (end-900 <= to < end)
def feat(U, Q):
    res = {k: np.full(len(U), np.nan) for k in ['mid5_open', 'spr5_open', 'mid15_open', 'mid5_T', 'mid15_T']}
    for coin in ['BTC', 'ETH', 'SOL', 'XRP']:
        qc = Q[Q.coin == coin]; idx = U.index[U.coin == coin]
        for tf, nm in (('5min', '5'), ('15min', '15')):
            qt = qc[qc.tf == tf]
            for name, off, lo in (('open', 1, 31), ('T', 180, 61)):
                a = pd.DataFrame({'i': idx, 'tq': (U.loc[idx, 'to'].values + off) * 1000})
                if tf == '5min': a['kk'] = U.loc[idx, 'to'].values; qq = qt.assign(kk=qt.end_s - 300)
                else:   # 15m: fin del bloque de 15 que contiene to
                    a['kk'] = (U.loc[idx, 'to'].values // 900 + 1) * 900; qq = qt.assign(kk=qt.end_s)
                m = pd.merge_asof(a.sort_values('tq'), qq[['kk', 't', 'mid', 'bid', 'ask']].sort_values('t'), left_on='tq', right_on='t', by='kk', direction='backward', tolerance=lo * 1000)
                if name == 'open' and tf == '5min': res['spr5_open'][m.i.values] = (m.ask - m.bid).values
                res[f'mid{nm}_' + name][m.i.values] = m.mid.values
    return pd.DataFrame(res, index=U.index)
F = feat(U, Q); U = pd.concat([U, F], axis=1)
for a, b in (('mid5_open', 'mid5_con_open'), ('mid15_open', 'mid15_con_open'), ('mid5_T', 'mid5_con_T'), ('mid15_T', 'mid15_con_T')): U[b] = np.where(U.o > 0, U[a], 1 - U[a])
U['gap15_5'] = U.mid15_con_open - U.mid5_con_open; U['dis'] = U.mid5_con_T - U.pcon; U['adis'] = U.dis.abs()
print('unidades', len(U), 'cobertura mid5_open', U.mid5_con_open.notna().mean().round(3), 'mid15_open', U.mid15_con_open.notna().mean().round(3), 'mid5_T', U.mid5_con_T.notna().mean().round(3), flush=True)
U.to_pickle(f'{D}/techo_units.pkl')
# --- fidelidad de prices-history (hist_reciente.jsonl) frente al registro y orientacion Up=YES ---
import json
H = [json.loads(l) for l in open(f'{D}/hist_reciente.jsonl')]; rec = []
for h in H:
    if 'pts' not in h or not h['pts']: continue
    to = h['tmin'] * 60; p = [x for x in h['pts'] if x[0] <= to]; pT = [x for x in h['pts'] if x[0] <= to + 180]
    rec.append((h['coin'], h['tmin'], p[-1][1] if p else np.nan, pT[-1][1] if pT else np.nan))
Hh = pd.DataFrame(rec, columns=['coin', 'tmin', 'h_open', 'h_T']).merge(U[['coin', 'tmin', 'mid5_open', 'mid5_T']], on=['coin', 'tmin'])
print('fidelidad prices-history vs registro (n=%d): corr apertura %.3f, |dif| mediana apertura %.4f, corr T %.3f, |dif| mediana T %.4f' % (len(Hh), Hh.h_open.corr(Hh.mid5_open), (Hh.h_open - Hh.mid5_open).abs().median(), Hh.h_T.corr(Hh.mid5_T), (Hh.h_T - Hh.mid5_T).abs().median()), flush=True)
# --- techo: apilar s_M10 + F12, walk-forward por dias ---
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
U['lpc'] = np.log(U.pcon / (1 - U.pcon)); U['qb'] = (U.pcon / 0.05).round().astype(int)
SETS = {'base': ['s_M10'], 'open': ['s_M10', 'mid5_con_open', 'spr5_open', 'mid15_con_open', 'gap15_5'], 'open+T': ['s_M10', 'mid5_con_open', 'spr5_open', 'mid15_con_open', 'gap15_5', 'mid5_con_T', 'mid15_con_T', 'dis', 'adis']}
def auc(df, s):
    d = df.assign(r=df.groupby('qb')[s].rank()); g = d.groupby('qb'); n1 = g.y.sum(); n = g.y.size(); n0 = n - n1; sr = d[d.y == 1].groupby('qb').r.sum(); Uu = (sr - n1 * (n1 + 1) / 2).reindex(n1.index).fillna(0); return float(Uu.sum() / (n1 * n0).sum())
ds = sorted(U.dstr.unique()); test = ds[7:]; res = {}
for lr in ('LOG', 'GBM'):
    for sn, cols in SETS.items():
        sc = pd.Series(np.nan, index=U.index)
        for d in test:
            tr = U[U.dstr < d]; te = U[U.dstr == d]
            m = make_pipeline(SimpleImputer(strategy='median'), StandardScaler(), LogisticRegression(C=1.0, max_iter=400)) if lr == 'LOG' else HistGradientBoostingClassifier(max_depth=2, max_iter=100, learning_rate=0.05, min_samples_leaf=100, l2_regularization=10, early_stopping=False, random_state=1)
            m.fit(tr[cols].values.astype(float), tr.y.values); sc[te.index] = m.predict_proba(te[cols].values.astype(float))[:, 1] - te.pcon.values
        U[f's_{lr}_{sn}'] = sc
T = U[U.dstr.isin(test)].reset_index(drop=True); print(f'\nTEST dias {test[0]}..{test[-1]} ({len(test)} d), unidades {len(T)}; AUC_strat del s_M10 ya existente (sin reentrenar): {auc(T, "s_M10"):.4f}')
def dboot(a, b, nb=1000):
    dd = sorted(T.dstr.unique()); g = {d: T[T.dstr == d].index.values for d in dd}; v = []
    for _ in range(nb):
        ch = RNG.choice(dd, len(dd)); ix = np.concatenate([g[d] for d in ch]); X = T.loc[ix].reset_index(drop=True); v.append(auc(X, b) - auc(X, a))
    return np.percentile(v, [5, 95])
for lr in ('LOG', 'GBM'):
    b0 = auc(T, f's_{lr}_base'); print(f'{lr} base [lpc,s_M10]: AUC {b0:.4f}')
    for sn in ('open', 'open+T'):
        a = auc(T, f's_{lr}_{sn}'); ci = dboot(f's_{lr}_base', f's_{lr}_{sn}'); print(f'{lr} +{sn}: AUC {a:.4f}  ganancia {a-b0:+.4f} IC90 dias ({ci[0]:+.4f},{ci[1]:+.4f})')
print('AUC univariable (estratificada) de las nuevas senales en TEST: ' + ', '.join(f'{c} {auc(T.assign(z=T[c].fillna(T[c].median())), "z"):.3f}' for c in ['mid5_con_open', 'mid15_con_open', 'gap15_5', 'spr5_open', 'mid5_con_T', 'dis', 'adis']))
