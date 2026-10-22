"""model_units.py -- UN solo modelo multi-rasgo, ajustado UNA vez en descubrimiento (09-15 Oct) y evaluado UNA vez en holdout (16-21):
regresion logistica de 'gana' con rasgos previos al relleno; EV previsto = phat/pc - 1 (en mercado) ; regla: pujar solo si EV previsto >= umbral
(umbral fijado en descubrimiento: percentil 50 o 75 del EV previsto). Congela coeficientes. Sale JSON + resumen."""
import sys, os, glob, json, hashlib; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from sa_common import *
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(B + '/datos/units/units_*.pkl'))], ignore_index=True)
U['win'] = (U.p > 0).astype(int); U = U.rename(columns={'p': 'pn'})
F = ['gap_last', 'dp5', 'dp30', 'dp60', 'hi60', 'rng60', 'd_open', 'vol30', 'vol_all', 'flow60', 'fv_gap', 'sig_bps_s', 'b10', 'T', 'pc']
X = U[F].astype(float).copy()
for k in ('vol30', 'vol_all'): X[k] = np.log1p(X[k])
for a in ('SOL', 'XRP'): X['is_' + a] = (U.act == a).astype(float)
dis = U.dia.isin(['2026-10-%02d' % d for d in range(9, 16)]).values
med = X[dis].median(); X = X.fillna(med); mu = X[dis].mean(); sd = X[dis].std().replace(0, 1); Z = (X - mu) / sd
m = LogisticRegression(C=0.3, max_iter=500).fit(Z[dis], U.win[dis])
ph = m.predict_proba(Z)[:, 1]; U['evp'] = ph / U.pc - 1
print('coef', {k: round(float(v),3) for k,v in zip(Z.columns, m.coef_[0])})
from sklearn.metrics import roc_auc_score
print('AUC win (disc/hold)', round(roc_auc_score(U.win[dis], ph[dis]),3), round(roc_auc_score(U.win[~dis], ph[~dis]),3))
res = {}
for q in (0.0, 0.5, 0.75, 0.9):
    thr = np.quantile(U.evp[dis], q) if q > 0 else -9
    for nm, msk in (('disc', dis), ('hold', ~dis)):
        s = U[msk & (U.evp >= thr)]; r = day_boot(s, 'pn', 'c'); res[f'q{q}_{nm}'] = r
        print(f'umbral q{q} ({thr:+.3f}) {nm}:', fmt(r))
    s = U[(~dis) & (U.evp < thr)]; 
    if len(s) and q > 0: print('   descartadas hold:', fmt(day_boot(s, 'pn', 'c')))
json.dump({'rasgos': list(Z.columns), 'mu': mu.to_dict(), 'sd': sd.to_dict(), 'med': med.to_dict(), 'coef': dict(zip(Z.columns, m.coef_[0].tolist())), 'intercept': float(m.intercept_[0]),
           'umbrales_evp': {str(q): float(np.quantile(U.evp[dis], q)) for q in (0.5, 0.75, 0.9)}}, open(B + '/datos/modelo_units_logit.json', 'w'), indent=1)
