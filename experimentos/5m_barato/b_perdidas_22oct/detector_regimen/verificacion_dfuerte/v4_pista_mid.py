#!/usr/bin/env python3
"""v4 - pista 'mid5 a T=180 + desacuerdo': (a) calibracion del mid vs modelo, (b) mecanica: mid predicho por rasgos del propio movimiento (placebo mecanico), (c) placebos de desplazamiento, (d) EV al mid. Solo lectura."""
import numpy as np, pandas as pd, warnings, sys; warnings.filterwarnings('ignore')
from scipy.special import ndtr
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.linear_model import LogisticRegression
D = '/mnt/HC_Volume_106538179/agentes_datos/dfuerte'; R = '/root/polymarket-research-datalogs/regimen_5m'; rg = np.random.default_rng(5)
U = pd.read_pickle(f'{D}/techo_units.pkl')[['coin','tmin','dia','dstr','y','pcon','q','con','o','s60','lpc','s_M10','mid5_con_T','mid5_con_open','mid15_con_T','dis','win','spr5_open','mid15_con_open']].copy()
# ret180 y sT recomputados desde klines crudos (independientes)
z = np.load(f'{R}/full_reciente.npz'); ex = []
for c in U.coin.unique():
    m0 = int(z[c + '_m0']); lp = np.log(z[c + '_X'][:, 0]); g = U[U.coin == c]; io = g.tmin.values - m0
    R1 = np.full(len(lp), np.nan); R1[1:] = np.diff(lp); r2 = np.nan_to_num(R1) ** 2; cs = np.concatenate([[0], np.cumsum(r2)]); iT = io + 3
    sT = np.sqrt((cs[iT + 1] - cs[iT - 59]) / 60); ex.append(pd.DataFrame(dict(coin=c, tmin=g.tmin.values, retT=lp[iT] - lp[io], sT=sT)))
U = U.merge(pd.concat(ex), on=['coin','tmin']); U['zo'] = U.o * U.retT / (U.sT * np.sqrt(2)); U['qb'] = (U.pcon / .05).round().astype(int)
def auc_strat(d, s):
    g = d.assign(r=d.groupby('qb')[s].rank()); n1 = g.groupby('qb').y.sum(); n = g.groupby('qb').y.size(); n0 = n - n1
    sr = g[g.y == 1].groupby('qb').r.sum(); Uu = (sr - n1 * (n1 + 1) / 2).reindex(n1.index).fillna(0); return float(Uu.sum() / (n1 * n0).sum())
ds = sorted(U.dstr.unique()); test = ds[7:]; T = U.dropna(subset=['mid5_con_T']).reset_index(drop=True); A = T[T.dstr.isin(test)]
print(f'TEST {test[0]}..{test[-1]} ({len(test)} d) unidades con mid_T en test {len(A)} de {int(U.dstr.isin(test).sum())}; total dias {len(ds)} n={len(T)}')
T0=T
print('AUC_strat univariable: s_M10 %.3f | mid5_con_T %.3f | dis %.3f | |dis| %.3f | pcon (control, ~0.5) %.3f' % tuple(auc_strat(A, c) if c != 'adis' else auc_strat(A.assign(adis=A.dis.abs()), 'adis') for c in ['s_M10','mid5_con_T','dis','adis','pcon']))
# (a) calibracion: EV al mid y al modelo
print('(a) media y - pcon (EV al precio del modelo) %.4f | media y - mid (EV al mid) %.4f' % ((A.y - A.pcon).mean(), (A.y - A.mid5_con_T).mean()))
d = A.groupby('dstr').apply(lambda g: pd.Series(dict(a=(g.y - g.pcon).mean(), b=(g.y - g.mid5_con_T).mean())))
bs = [d.loc[rg.choice(d.index, len(d))].mean().values for _ in range(2000)]; print('    IC90 dias (modelo, mid):', np.percentile(np.array(bs), [5, 95], axis=0).round(4).tolist())
print('    Brier y~pcon %.4f | y~mid %.4f | y~0.5*(pcon+mid) %.4f' % (((A.y - A.pcon) ** 2).mean(), ((A.y - A.mid5_con_T) ** 2).mean(), ((A.y - .5 * (A.pcon + A.mid5_con_T)) ** 2).mean()))
# (b) mecanica: mid predicho por (lpc, zo, s60, sT, coin) con entrenamiento en dias previos; pista = residuo
T['mech'] = np.nan
for dd in ds:
    tr = T[T.dstr != dd]; te = T.dstr == dd
    cols = ['lpc','zo','s60','sT','retT']; m = HistGradientBoostingRegressor(max_depth=3, max_iter=150, learning_rate=.05).fit(tr[cols].values, tr.mid5_con_T.values); T.loc[te, 'mech'] = m.predict(T.loc[te, cols].values)
A = T[T.dstr.isin(test)]
print('(b) R2 del mid explicado por (lpc, z, vol) fuera de muestra: %.3f ; corr(mid, mech) %.3f' % (1 - ((A.mid5_con_T - A.mech) ** 2).sum() / ((A.mid5_con_T - A.mid5_con_T.mean()) ** 2).sum(), A.mid5_con_T.corr(A.mech)))
T['resid'] = T.mid5_con_T - T.mech; T['dis_mech'] = T.mech - T.pcon; A = T[T.dstr.isin(test)]
print('    AUC_strat: mid %.3f | mech (mid predicho solo con el movimiento) %.3f | residuo mid-mech %.3f | dis %.3f | dis_mech %.3f' % tuple(auc_strat(A, c) for c in ['mid5_con_T','mech','resid','dis','dis_mech']))
# apilado walk-forward por dias: base [lpc,s_M10] vs +mid/+mech/+residuo/+placebos
T['mid_lag'] = np.nan; T['mid_shuf'] = T.mid5_con_T.values
g = T.groupby(['dstr','coin','qb']).ngroup().values; o_ = np.lexsort((rg.random(len(T)), g)); ix = np.argsort(g, kind='stable'); sp = np.empty(len(T)); sp[ix] = T.mid5_con_T.values[o_]; T['mid_shuf'] = sp
# placebo desplazado: mid de la ventana anterior de la misma moneda (5 min antes), misma orientacion que o actual
Tm = U.set_index(['coin','tmin']).mid5_con_T; o_prev = U.set_index(['coin','tmin']).o
prev = [Tm.get((c, t - 5), np.nan) for c, t in zip(T.coin, T.tmin)]; oprev = [o_prev.get((c, t - 5), np.nan) for c, t in zip(T.coin, T.tmin)]
T['mid_prev'] = np.where(np.array(oprev) == T.o.values, prev, 1 - np.array(prev))
T['adis']=T.dis.abs(); T['gap15_5']=T.mid15_con_open-T.mid5_con_open; T['adis_mech']=T.dis_mech.abs()
SETS = {'base': ['lpc','s_M10'], '+mid': ['lpc','s_M10','mid5_con_T'], '+mech': ['lpc','s_M10','mech'], '+resid': ['lpc','s_M10','resid'], '+mid_shuf(placebo)': ['lpc','s_M10','mid_shuf'], '+mid_prev(placebo)': ['lpc','s_M10','mid_prev'], 'SPEC_PREREG open+T': ['s_M10','mid5_con_open','spr5_open','mid15_con_open','gap15_5','mid5_con_T','dis','adis'], 'SPEC solo T (mid,dis,adis)': ['s_M10','mid5_con_T','dis','adis'], 'SPEC mecanica (mech,dis_mech,adis_mech)': ['s_M10','mech','dis_mech','adis_mech'], 'SPEC solo apertura': ['s_M10','mid5_con_open','spr5_open','mid15_con_open','gap15_5']}
for nm, cols in SETS.items():
    sc = pd.Series(np.nan, index=T.index)
    cols=[c for c in cols if T[c].notna().mean()>0.2]
    for dd in test:
        tr = T[T.dstr < dd]; te = T[T.dstr == dd]
        X = tr[cols].fillna(tr[cols].median()).fillna(0).values; sd=X.std(0)+1e-9; m = LogisticRegression(C=1.0, max_iter=500).fit((X - X.mean(0)) / sd, tr.y.values)
        Xt = te[cols].fillna(tr[cols].median()).fillna(0).values; sc[te.index] = m.predict_proba((Xt - X.mean(0)) / sd)[:, 1]
    T['sc_' + nm] = sc
S = T.dropna(subset=['sc_base']).reset_index(drop=True); print(f'(c) apilado logistico walk-forward, entrena con dias previos 5-11 Oct en adelante (dias {test[0]}..{test[-1]}, n={len(S)}): ' + ' | '.join(f'{nm} {auc_strat(S, "sc_" + nm):.4f}' for nm in SETS))
def dboot(a, b, nb=500):
    dd = S.dstr.unique(); ix = {k: g.index.values for k, g in S.groupby('dstr')}; v = []
    for _ in range(nb):
        ch = rg.choice(dd, len(dd)); x = S.loc[np.concatenate([ix[k] for k in ch])].reset_index(drop=True); v.append(auc_strat(x, b) - auc_strat(x, a))
    return np.percentile(v, [5, 95])
for nm in list(SETS)[1:]: print('    ganancia %-20s %+.4f IC90 dias (%+.4f,%+.4f)' % (nm, auc_strat(S, 'sc_' + nm) - auc_strat(S, 'sc_base'), *dboot('sc_base', 'sc_' + nm)))
# (d) correlacion con el movimiento propio de la ventana: dis frente a zo
print('(d) corr(dis, zo) %.3f ; corr(mid5_con_T, zo) %.3f ; corr(mid5_con_open, zo) %.3f' % (A.dis.corr(A.zo), A.mid5_con_T.corr(A.zo), A.mid5_con_open.corr(A.zo)))

T=A.copy(); T['dt']=pd.qcut(T.dis,3,labels=['dis bajo','dis medio','dis alto']); 
print('(e) EV al mid por tercil de desacuerdo (y - mid; sin comision ni spread):'); print(T.groupby('dt').apply(lambda g: pd.Series(dict(n=len(g), ev_mid=(g.y-g.mid5_con_T).mean(), ev_modelo=(g.y-g.pcon).mean(), con=g.con.mean()))).round(4).to_string())
