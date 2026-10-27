#!/usr/bin/env python3
"""congelar.py -- entrena y CONGELA M1F (desplegable con sa_r1/units2 + bookTicker + ventanas_bookticker) y M2 (FULL de build_units)
con TODOS los rellenos de poblacion 09-20 Oct de q_techo/tab.pkl (21-Oct excluido: truncado). Corte = cuantil 90 % del EUR del EV predicho
en TRAIN (top 10 %). Escribe pickles + JSON con sha256 en /mnt/HC_Volume_106538179/agentes_datos/detector_ex_ante/."""
import pandas as pd, numpy as np, pickle, json, hashlib, os, sklearn
from sklearn.ensemble import HistGradientBoostingClassifier
OUT = '/mnt/HC_Volume_106538179/agentes_datos/detector_ex_ante/'; os.makedirs(OUT, exist_ok=True)
T = pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl')
T = T[T.dia <= '2026-10-20'].copy()
T['y'] = T.gana_f.astype(float); T['coin'] = T.act.map({'ETH': 0, 'SOL': 1, 'XRP': 2}); T['lado'] = (T.lado_c == 'YES').astype(int)
T['depth_ticks'] = (T.bb - T.pc) / 0.01; T['gap15'] = T.b15 - T.bb
M1F = ['pc','T','coin','hora','lado','vol30','bb','ba','bs','spread','depth_ticks','b15','a15','lvl15','gap15','vol30ws','r60f','rpre_s','CON']
FWD = ['pc','T','coin','hora','lado','vol30','bb','ba','bs','as_','spread','depth_ticks','b15','a15','lvl15','gap15','d15_30','dbb30','vol30ws','r60f','rpre_s','CON','imb','qage','q15age']
M2 = FWD + ['gap_last','dp5','dp30','dp60','hi60','rng60','d_open','vol_all','flow60','fv_gap','z','sig_bps_s','b10']
meta = {'congelado_utc': pd.Timestamp.utcnow().isoformat(), 'train': '2026-10-09..2026-10-20', 'n_train': int(len(T)), 'sklearn': sklearn.__version__, 'modelos': {}}
for nm, f in (('M1F', M1F), ('M2', M2)):
    m = HistGradientBoostingClassifier(max_depth=3, max_iter=200, learning_rate=0.05, min_samples_leaf=300, l2_regularization=1.0, random_state=0).fit(T[f], T.y)
    ev = m.predict_proba(T[f])[:, 1] / T.pc.values - 1; o = np.argsort(ev); cw = np.cumsum(T.c.values[o]) / T.c.sum(); cut = float(ev[o][np.searchsorted(cw, 0.90)])
    pk = OUT + 'modelo_%s.pkl' % nm; pickle.dump({'modelo': m, 'feats': f, 'corte_ev': cut}, open(pk, 'wb'))
    meta['modelos'][nm] = {'pickle': pk, 'sha256': hashlib.sha256(open(pk, 'rb').read()).hexdigest(), 'feats': f, 'corte_ev': cut,
                           'f_train_top': float(T.c.values[ev >= cut].sum() / T.c.sum())}
json.dump(meta, open(OUT + 'MODELO_CONGELADO.json', 'w'), indent=1)
print(json.dumps(meta, indent=1)[:1500])
