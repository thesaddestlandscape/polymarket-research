#!/usr/bin/env python3
"""f2_walkforward.py - walk-forward por MESES de los K=11 modelos + controles (PREREG_DFUERTE sha 5efad7c6...). Semilla fija.
Salida: datalogs/regimen_5m/dfuerte/oos.pkl (unidades fuera de muestra con s_hat por modelo), frozen_models.pkl (entrenados hasta 2026-08-17)."""
import sys, os, hashlib, pickle, numpy as np, pandas as pd, warnings, time, datetime as dt
warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
assert hashlib.sha256(open(os.path.join(HERE, '..', 'PREREG_DFUERTE.md'), 'rb').read()).hexdigest().startswith('5efad7c6')
import dfuerte_lib as DL
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
OUT = '/root/polymarket-research-datalogs/regimen_5m/dfuerte'; TSEL = int(os.environ.get('TSEL', '180'))
day = lambda y, m, d: (dt.date(y, m, d) - dt.date(1970, 1, 1)).days
U = pd.concat([pd.read_pickle(f'{OUT}/units_{s}' + ('_w2' if os.environ.get('WAVE2') else '') + '.pkl').assign(src=s) for s in ('y2025', 'dic_ene', 'backfill', 'reciente')], ignore_index=True)
U = U[U['T'] == TSEL].reset_index(drop=True)
_F9 = ['rv_in', 'maxr_in', 'eff_in', 'zT', 'last', 'retr', 'imb_in', 'vol_in', 'hl_in']; _F10 = ['rc12_all', 'rc36_all', 'rc36_coin', 'e12_all', 'e36_all', 'e36_coin']
_keep = ['coin', 'tmin', 'dia', 'src', 'T', 'con', 'q', 'pcon', 'y', 'win', 'R', 'rpre', 'o', 's60', 'win_oficial'] + DL.FEATS + [c for c in _F9 + _F10 if c in U.columns]
U = U[list(dict.fromkeys(_keep))]
for _c in DL.FEATS + [c for c in _F9 + _F10 if c in U.columns]: U[_c] = U[_c].astype('float32')
W2 = bool(os.environ.get('WAVE2')); TAG = ('_abl' if os.environ.get('CTRLG2') else '') + ('_ctrl' if os.environ.get('CTRLG') else '') + ('_w2' if W2 else '') + ('_synth' if os.environ.get('SYNTH') else '')
if os.environ.get('SYNTH'):
    U['win'] = (np.random.default_rng(5).random(len(U)) < U.q).astype(float); U['y'] = np.where(U.con == 1, U.win, 1 - U.win)
U['lpc'] = np.log(U.pcon / (1 - U.pcon)); U['e'] = U.win - U.q
d2 = pd.to_datetime(U.dia * 86400, unit='s'); U['mes'] = d2.dt.strftime('%Y-%m')
U.loc[(U.dia >= day(2025, 12, 17)) & (U.mes == '2025-12'), 'mes'] = '2025-12T'
U.loc[U.src == 'reciente', 'mes'] = 'REC'; U = U[(U.src != 'reciente') | (U.dia >= day(2026, 9, 24))].reset_index(drop=True)
U = U[(U.src == 'reciente') | (U.dia < day(2026, 9, 1))]
MODELS = {f'M{i+1}': ('LOG', [f]) for i, f in enumerate(['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'])}
MODELS['M9'] = ('LOG', list(DL.FAM)); MODELS['M10'] = ('GBM', list(DL.FAM)); MODELS['M11'] = ('LOGCON', list(DL.FAM))
CTRL = {'C0': ('LOG', ['COIN'])}
if os.environ.get('CTRLG2'): MODELS = {f'G{i}': ('GBM', [f'F{i}']) for i in range(1, 7)}; MODELS['GnoF8'] = ('GBM', [f for f in DL.FAM if f != 'F8']); MODELS['GnoF7'] = ('GBM', [f for f in DL.FAM if f != 'F7']); MODELS['GnoF78'] = ('GBM', [f for f in DL.FAM if f not in ('F7', 'F8')]); CTRL = {}
if os.environ.get('CTRLG'): MODELS = {'M10': ('GBM', list(DL.FAM)), 'M9': ('LOG', list(DL.FAM))}; CTRL = {'C0G': ('GBM', ['COIN']), 'C7G': ('GBM', ['F7']), 'C8G': ('GBM', ['F8']), 'C0': ('LOG', ['COIN'])}
F9 = ['rv_in', 'maxr_in', 'eff_in', 'zT', 'last', 'retr', 'imb_in', 'vol_in', 'hl_in']; F10 = ['rc12_all', 'rc36_all', 'rc36_coin', 'e12_all', 'e36_all', 'e36_coin']
FAMX = {**DL.FAM, 'F9': F9, 'F10': F10}
if os.environ.get('WAVE2'): MODELS = {'M12': ('LOG', ['F9']), 'M13': ('LOG', list(FAMX)), 'M14': ('GBM', list(FAMX))}
def cols(fams):
    out = ['lpc']
    for f in fams: out += ['c_' + c for c in DL.ALLC] if f == 'COIN' else FAMX[f]
    return list(dict.fromkeys(out))
def fit(kind, fams, tr):
    X = tr[cols(fams)].values.astype(float)
    if kind == 'GBM':
        m = HistGradientBoostingClassifier(max_depth=3, max_iter=150, learning_rate=0.03, min_samples_leaf=500, l2_regularization=10, early_stopping=False, random_state=1); y = tr.y.values
    else:
        m = make_pipeline(SimpleImputer(strategy='median'), StandardScaler(), LogisticRegression(C=0.02, max_iter=400)); y = tr.y.values
        if kind == 'LOGCON': y = tr.win.values
    if kind == 'LOGCON': tr = tr[tr.con == 1]; X = tr[cols(fams)].values.astype(float); y = tr.win.values
    m.fit(X, y); return m
QS = [0.10, 0.25, 0.50, 0.75, 0.90]
def cutoffs(m, fams, tr, nm, te):
    sc = score(m, fams, tr[tr.con == 1])
    for q in QS: te['c_%s_q%d' % (nm, round(q * 100))] = float(np.quantile(sc, q))
def score(m, fams, te): return m.predict_proba(te[cols(fams)].values.astype(float))[:, 1] - te.pcon.values
months = sorted(U.mes.unique(), key=lambda s: (s == 'REC', s.replace('T', 'z')))
starts = {m: U[U.mes == m].dia.min() for m in months}
TEST_D = [m for m in months if '2025-04' <= m <= '2025-12']; TEST_T = ['2025-12T', '2026-01', '2026-03', '2026-04', '2026-05', '2026-06', '2026-07', '2026-08']
if os.environ.get('SMOKE'): TEST_D = TEST_D[:2]; TEST_T = TEST_T[:1]
res = []; t0 = time.time(); ALL = {**MODELS, **CTRL}
for mes in TEST_D + TEST_T:
    te = U[U.mes == mes].copy(); tr = U[(U.dia < starts[mes] - 1) & (U.src != 'reciente')]
    if tr.mes.nunique() < 3 or len(te) == 0: print('salta', mes, len(tr), len(te)); continue
    for nm, (kind, fams) in ALL.items():
        mm = fit(kind, fams, tr); te['s_' + nm] = score(mm, fams, te); cutoffs(mm, fams, tr, nm, te)
    te['fase'] = 'D' if mes in TEST_D else 'T'; res.append(te); print(mes, 'train', len(tr), 'test', len(te), 'seg', round(time.time() - t0), flush=True)
# modelo congelado (entrenado hasta 2026-08-17) y evaluacion RECIENTE
tr = U[(U.dia <= day(2026, 8, 17)) & (U.src != 'reciente')]; te = U[U.mes == 'REC'].copy(); frozen = {}
for nm, (kind, fams) in ALL.items():
    m = fit(kind, fams, tr); te['s_' + nm] = score(m, fams, te); cutoffs(m, fams, tr, nm, te); frozen[nm] = (kind, fams, m, {c[len('c_' + nm) + 1:]: float(te[c].iloc[0]) for c in te.columns if c.startswith('c_' + nm + '_q')})
te['fase'] = 'R'; res.append(te); print('REC train', len(tr), 'test', len(te), 'seg', round(time.time() - t0), flush=True)
O = pd.concat(res, ignore_index=True); O.to_pickle(f'{OUT}/oos_T{TSEL}{TAG}.pkl')
pickle.dump(frozen, open(f'{OUT}/frozen_models_T{TSEL}{TAG}.pkl', 'wb')); print('OOS', len(O), O.fase.value_counts().to_dict())
