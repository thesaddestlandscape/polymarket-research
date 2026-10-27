#!/usr/bin/env python3
"""v2 - re-entrena M14/M17/M16 (+ placebo de etiquetas permutadas) con split temporal estricto sobre FASE T; AUC estratificada, IC90 por dias, exceso dPnL. Solo lectura de datos; salidas en esta carpeta."""
import sys, os, numpy as np, pandas as pd, warnings, datetime as dt, pickle, time; warnings.filterwarnings('ignore')
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/dfuerte/scripts')
from sklearn.ensemble import HistGradientBoostingClassifier
R = '/root/polymarket-research-datalogs/regimen_5m'; HERE = os.path.dirname(os.path.abspath(__file__))
# lista de rasgos: leida de los pickles (columnas), NO de dfuerte_lib; familias definidas por orden de columnas del informe
import dfuerte_lib as DL   # solo para la lista de nombres de columnas por familia
F9 = ['rv_in','maxr_in','eff_in','zT','last','retr','imb_in','vol_in','hl_in']; F10 = ['rc12_all','rc36_all','rc36_coin','e12_all','e36_all','e36_coin']
F11 = ['basis','dbasis15','dbasis60','zbasis','pimb5','pimb15','pimb60','pvol15','lvr15','retgap15','fund','ofund','afund']
BASE = list(dict.fromkeys(sum(DL.FAM.values(), [])))
keep = ['coin','tmin','dia','T','con','q','pcon','y','win','R','rpre','o','s60'] + BASE + F9 + F10 + F11
day = lambda y, m, d: (dt.date(y, m, d) - dt.date(1970, 1, 1)).days
parts = []
for s in ('y2025','dic_ene','backfill','reciente'):
    u = pd.read_pickle(f'{R}/dfuerte/units_{s}_r3.pkl'); u = u[u['T'] == 180][[c for c in keep if c in u.columns]].copy(); u['src'] = s
    for c in BASE + F9 + F10 + F11: u[c] = u[c].astype('float32')
    parts.append(u)
U = pd.concat(parts, ignore_index=True); del parts
U['lpc'] = np.log(U.pcon / (1 - U.pcon)); U['qb'] = (U.pcon / .05).round().astype(int); U['e'] = U.win - U.q
U['mes'] = pd.to_datetime(U.dia * 86400, unit='s').dt.strftime('%Y-%m'); U.loc[(U.dia >= day(2025,12,17)) & (U.mes == '2025-12'), 'mes'] = '2025-12T'
U = U[((U.src != 'reciente') & (U.dia < day(2026,9,1))) | ((U.src == 'reciente') & (U.dia >= day(2026,9,24)))].reset_index(drop=True)
TEST_T = ['2025-12T','2026-01','2026-03','2026-04','2026-05','2026-06','2026-07','2026-08']
# comprobacion de no-solapamiento de fuentes
dup = U.duplicated(['coin','tmin']).sum(); print('unidades', len(U), 'duplicados coin,tmin:', dup)
MODELS = {'M14': BASE + F9 + F10, 'M17': BASE + F9 + F10 + F11, 'M16': F11, 'M10': BASE}
def gbm(): return HistGradientBoostingClassifier(max_depth=3, max_iter=150, learning_rate=.03, min_samples_leaf=500, l2_regularization=10, early_stopping=False, random_state=1)
def auc_strat(d, s):
    r = d.groupby('qb')[s].rank(); g = d.assign(r=r); n1 = g.groupby('qb').y.sum(); n = g.groupby('qb').y.size(); n0 = n - n1
    sr = g[g.y == 1].groupby('qb').r.sum(); Uu = (sr - n1 * (n1 + 1) / 2).reindex(n1.index).fillna(0); return float(Uu.sum() / (n1 * n0).sum())
res = []; t0 = time.time(); cuts = {}
for mes in TEST_T:
    te = U[U.mes == mes].copy(); st = te.dia.min(); tr = U[U.dia < st - 1]
    assert tr.dia.max() < te.dia.min() - 1 and not (tr.tmin.max() >= te.tmin.min())   # split temporal estricto
    for nm, cols in MODELS.items():
        X = tr[['lpc'] + cols].values.astype(float); m = gbm().fit(X, tr.y.values)
        te['s_' + nm] = m.predict_proba(te[['lpc'] + cols].values.astype(float))[:, 1] - te.pcon.values
        if nm == 'M17': cuts[mes] = float(np.quantile(m.predict_proba(tr[tr.con == 1][['lpc'] + cols].values.astype(float))[:, 1] - tr[tr.con == 1].pcon.values, .5))
        if nm in ('M17',):   # PLACEBO: etiquetas permutadas dentro de dia x moneda x qb en entrenamiento
            rg = np.random.default_rng(11); g = tr.groupby(['dia','coin','qb']).ngroup().values; yp = tr.y.values.copy()
            o_ = np.lexsort((rg.random(len(tr)), g)); ix = np.argsort(g, kind='stable'); yp2 = np.empty_like(yp); yp2[ix] = yp[o_]
            mp = gbm().fit(X, yp2); te['s_M17perm'] = mp.predict_proba(te[['lpc'] + cols].values.astype(float))[:, 1] - te.pcon.values
    res.append(te); print(mes, 'train', len(tr), 'test', len(te), 'seg', round(time.time() - t0), flush=True)
O = pd.concat(res, ignore_index=True); O.drop(columns=BASE + F9 + F10 + F11).to_pickle(f'{HERE}/oos_verif.pkl'); pickle.dump(cuts, open(f'{HERE}/cuts.pkl', 'wb'))
print('FASE T n', len(O), 'dias', O.dia.nunique())
rg = np.random.default_rng(3)
def boot(d, fa, fb=None, nb=300):
    days = d.dia.unique(); idx = {k: g.index.values for k, g in d.groupby('dia')}; v = []
    for _ in range(nb):
        ch = rg.choice(days, len(days)); x = d.loc[np.concatenate([idx[k] for k in ch])].reset_index(drop=True); v.append(auc_strat(x, fa) - (auc_strat(x, fb) if fb else 0))
    return np.percentile(v, [5, 95])
O['inv_M17'] = -O.s_M17
for s in ['s_M10','s_M14','s_M17','s_M16','s_M17perm','inv_M17']:
    a = auc_strat(O, s); ci = boot(O, s); print(f'AUC_strat {s}: {a:.4f} IC90 dias ({ci[0]:.4f},{ci[1]:.4f})', flush=True)
ci = boot(O, 's_M17', 's_M14'); print('M17-M14: %+.4f IC90 dias (%+.4f,%+.4f)' % (auc_strat(O, 's_M17') - auc_strat(O, 's_M14'), *ci))
# placebo: score permutado dentro de dia x moneda x qb
g = O.groupby(['dia','coin','qb']).ngroup().values; o_ = np.lexsort((rg.random(len(O)), g)); ix = np.argsort(g, kind='stable'); sp = np.empty(len(O)); sp[ix] = O.s_M17.values[o_]
print('AUC placebo (score M17 permutado dia x moneda x qb): %.4f' % auc_strat(O.assign(sp=sp), 'sp'))
print('AUC por mes M17:', {m: round(auc_strat(d.reset_index(drop=True), 's_M17'), 3) for m, d in O.groupby('mes')})
print('AUC por mes M14:', {m: round(auc_strat(d.reset_index(drop=True), 's_M14'), 3) for m, d in O.groupby('mes')})
print('AUC pooled SIN estratificar M17 (informativo): ', end=''); from sklearn.metrics import roc_auc_score; print(round(roc_auc_score(O.y, O.s_M17), 4), ' qb fino 0.02:', end=' '); O2 = O.assign(qb=(O.pcon / .02).round().astype(int)); print(round(auc_strat(O2, 's_M17'), 4))
O['hasperp'] = O.coin.isin(['BTC','ETH','SOL','XRP']) & O.src.isin(['y2025','dic_ene','reciente']) ; 
cov = O.groupby('src').apply(lambda d: d.coin.isin(['BTC','ETH','SOL','XRP']).mean()); print('cobertura monedas con perps por src (FASE T):', cov.round(3).to_dict(), ' cuota por moneda:', O.coin.value_counts(normalize=True).round(3).to_dict())
for sub, nm in ((O[O.coin.isin(['BTC','ETH','SOL','XRP'])], 'monedas con perps'),):
    sub = sub.reset_index(drop=True); print(f'  {nm} n={len(sub)}: M14 {auc_strat(sub,"s_M14"):.4f} M17 {auc_strat(sub,"s_M17"):.4f} M16 {auc_strat(sub,"s_M16"):.4f}')
