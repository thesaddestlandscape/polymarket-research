#!/usr/bin/env python3
"""f10 - 24-Oct: (1) 15m CRUZADO con cotizaciones del m15_registro (hora de RECEPCION) alineado a cada ventana 5m; (2) pista del mid a T=180 s:
residuo mid-mecanico, desacuerdo mercado-modelo SIN mid (s_M10), placebo de permutacion dia x moneda x qb, multiplicidad, desagregado moneda x marco.
Entrada: techo_units.pkl (f9_techo_v2), mid15/<dia>.csv.gz. Solo lectura. Semilla fija."""
import numpy as np, pandas as pd, warnings, glob, sys; pd.options.future.infer_string = False; warnings.filterwarnings('ignore')
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.linear_model import LogisticRegression
D = '/mnt/HC_Volume_106538179/agentes_datos/dfuerte'; R = '/root/polymarket-research-datalogs/regimen_5m'; rg = np.random.default_rng(11)
U = pd.read_pickle(f'{D}/techo_units.pkl')
U = U[['coin','tmin','dia','dstr','y','pcon','q','con','o','s60','lpc','s_M10','mid5_con_T','mid5_con_open','spr5_open','win','to']].copy()
U['coin'] = U.coin.astype(object)
# --- 15m: cotizaciones por recepcion ---
parts = []
for f in sorted(glob.glob(f'{D}/mid15/2026-*.csv.gz')):
    q = pd.read_csv(f, names=['r','tok','bid','ask','coin','end'], dtype={'tok': str, 'bid': 'float32', 'ask': 'float32', 'r': 'float64'}); q = q.dropna(subset=['r']); q['r'] = q.r.astype('int64')
    q = q[(q.bid > 0) & (q.ask >= q.bid)]; q['sec'] = q.r // 1000; q = q.drop_duplicates(['tok','sec'], keep='last').drop(columns=['tok','sec'])
    q['mid'] = (q.bid + q.ask) / 2; q['kk'] = (pd.to_datetime(q.end).astype('datetime64[s]').astype('int64')); q['coin'] = q.coin.astype(object)
    parts.append(q[['r','coin','kk','mid','bid','ask']])
Q = pd.concat(parts, ignore_index=True).sort_values('r'); print('cotizaciones 15m YES (recepcion)', len(Q), 'dias', len(parts), 'monedas', sorted(Q.coin.unique()), flush=True)
for name, off, lo in (('open', 1, 31), ('T', 180, 61)):
    a = pd.DataFrame({'i': U.index, 'tq': (U.to.values + off) * 1000, 'kk': (U.to.values // 900 + 1) * 900, 'coin': U.coin.values}).sort_values('tq')
    m = pd.merge_asof(a, Q[['r','coin','kk','mid']].rename(columns={'r': 'rq'}), left_on='tq', right_on='rq', by=['coin','kk'], direction='backward', tolerance=lo * 1000)
    U.loc[m.i.values, 'mid15_' + name] = m.mid.values
for n in ('open', 'T'): U[f'mid15_con_{n}'] = np.where(U.o > 0, U['mid15_' + n], 1 - U['mid15_' + n])
U['slot15'] = (U.to // 300) % 3; U['dis15'] = U.mid15_con_T - U.pcon; U['gap15_5'] = U.mid15_con_open - U.mid5_con_open; U['gapT'] = U.mid15_con_T - U.mid5_con_T; U['dis'] = U.mid5_con_T - U.pcon
print('cobertura mid15_open %.3f mid15_T %.3f (n unidades %d)' % (U.mid15_con_open.notna().mean(), U.mid15_con_T.notna().mean(), len(U)), flush=True)
# --- movimiento propio de la ventana desde klines crudos ---
z = np.load(f'{R}/full_reciente.npz'); ex = []
for c in U.coin.unique():
    m0 = int(z[c + '_m0']); lp = np.log(z[c + '_X'][:, 0]); g = U[U.coin == c]; io = g.tmin.values - m0
    R1 = np.full(len(lp), np.nan); R1[1:] = np.diff(lp); cs = np.concatenate([[0], np.cumsum(np.nan_to_num(R1) ** 2)]); iT = io + 3
    ex.append(pd.DataFrame(dict(coin=c, tmin=g.tmin.values, retT=lp[iT] - lp[io], sT=np.sqrt((cs[iT + 1] - cs[iT - 59]) / 60))))
U = U.merge(pd.concat(ex), on=['coin','tmin']); U['zo'] = U.o * U.retT / (U.sT * np.sqrt(2)); U['qb'] = (U.pcon / .05).round().astype(int)
U['p_model'] = U.s_M10 + U.pcon          # P(y) del modelo M10 (NO usa mid)
U['dis_M10'] = U.mid5_con_T - U.p_model; U['dis15_M10'] = U.mid15_con_T - U.p_model; U['adis_M10'] = U.dis_M10.abs()
def auc_strat(d, s):
    g = d.assign(r=d.groupby('qb')[s].rank()); n1 = g.groupby('qb').y.sum(); n = g.groupby('qb').y.size(); n0 = n - n1
    sr = g[g.y == 1].groupby('qb').r.sum(); Uu = (sr - n1 * (n1 + 1) / 2).reindex(n1.index).fillna(0); return float(Uu.sum() / (n1 * n0).sum())
ds = sorted(U.dstr.unique()); test = ds[7:]
# --- mid mecanico (CV por dias) y residuos ---
T = U.reset_index(drop=True)
for col, nm in (('mid5_con_T', '5'), ('mid15_con_T', '15')):
    T['mech' + nm] = np.nan; ok = T[col].notna()
    for dd in ds:
        tr = T[ok & (T.dstr != dd)]; te = ok & (T.dstr == dd)
        if te.sum() == 0: continue
        cols = ['lpc','zo','s60','sT','retT'] + (['slot15'] if nm == '15' else []); m = HistGradientBoostingRegressor(max_depth=3, max_iter=150, learning_rate=.05).fit(tr[cols].values, tr[col].values); T.loc[te, 'mech' + nm] = m.predict(T.loc[te, cols].values)
    T['resid' + nm] = T[col] - T['mech' + nm]
A = T[T.dstr.isin(test)]
print('\n== (1) 15m cruzado: descriptivo (test %s..%s, %d d, unidades %d; con mid15_T %d) ==' % (test[0], test[-1], len(test), len(A), A.mid15_con_T.notna().sum()))
print('corr(mid15_con_T, zo) %.3f | corr(mid5_con_T, zo) %.3f | corr(mid15_con_open, zo) %.3f | R2 mid15 por (lpc,zo,vol,slot) %.3f' % (A.mid15_con_T.corr(A.zo), A.mid5_con_T.corr(A.zo), A.mid15_con_open.corr(A.zo), 1 - ((A.mid15_con_T - A.mech15) ** 2).sum() / ((A.mid15_con_T - A.mid15_con_T.mean()) ** 2).sum()))
uni = ['s_M10','pcon','mid15_con_open','gap15_5','mid15_con_T','dis15','gapT','mech15','resid15','resid5','dis_M10','dis15_M10','adis_M10','dis']
res = {}
for c in uni:
    d = A.dropna(subset=[c]); res[c] = (auc_strat(d, c), len(d))
print('AUC_strat univariable (inversion = 1-AUC): ' + ' | '.join(f'{c} {a:.3f} (n={n})' for c, (a, n) in res.items()))
# --- apilado walk-forward por dias ---
def shuf(col):
    g = T.groupby(['dstr','coin','qb']).ngroup().values; o_ = np.lexsort((rg.random(len(T)), g)); ix = np.argsort(g, kind='stable'); s = np.empty(len(T)); s[ix] = T[col].values[o_]; return s
for c in ('mid5_con_T', 'mid15_con_T', 'mid15_con_open'): T[c + '_shuf'] = shuf(c)
T['dis15_shuf'] = T.mid15_con_T_shuf - T.pcon; T['dis_shuf'] = T.mid5_con_T_shuf - T.pcon
B = ['lpc','s_M10']
SETS = {'base': B, '+15m_open': B + ['mid15_con_open','gap15_5'], '+15m_T': B + ['mid15_con_T','dis15'], '+15m_open+T': B + ['mid15_con_open','gap15_5','mid15_con_T','dis15'],
        '+5m_T': B + ['mid5_con_T','dis'], '+5m+15m_T': B + ['mid5_con_T','dis','mid15_con_T','dis15','gapT'], '+resid5': B + ['resid5'], '+resid15': B + ['resid15'], '+resid5+15': B + ['resid5','resid15'],
        '+dis_M10 (5m)': B + ['dis_M10'], '+dis_M10 (5m+15m)': B + ['dis_M10','dis15_M10'],
        'PLACEBO 15m_T shuf': B + ['mid15_con_T_shuf','dis15_shuf'], 'PLACEBO 5m_T shuf': B + ['mid5_con_T_shuf','dis_shuf']}
def walk(cols, TT, nested=False):
    cols = [c for c in cols if TT[c].notna().mean() > 0.2]; sc = pd.Series(np.nan, index=TT.index)
    for dd in test:
        tr = TT[TT.dstr < dd]; te = TT[TT.dstr == dd]
        if len(te) == 0: continue
        X = tr[cols].fillna(tr[cols].median()).fillna(0).values; mu, sd = X.mean(0), X.std(0) + 1e-9; m = LogisticRegression(C=1.0, max_iter=500).fit((X - mu) / sd, tr.y.values)
        sc[te.index] = m.predict_proba((te[cols].fillna(tr[cols].median()).fillna(0).values - mu) / sd)[:, 1]
    return sc
for nm, cols in SETS.items(): T['sc_' + nm] = walk(cols, T)
S = T.dropna(subset=['sc_base']).reset_index(drop=True)
ix = {k: g.index.values for k, g in S.groupby('dstr')}; dd_ = list(ix)
def dboot(b, nb=600):
    out = []
    for _ in range(nb):
        x = S.loc[np.concatenate([ix[k] for k in rg.choice(dd_, len(dd_))])].reset_index(drop=True); out.append(auc_strat(x, b) - auc_strat(x, 'sc_base'))
    return np.percentile(out, [5, 95])
b0 = auc_strat(S, 'sc_base'); print(f'\n== apilado logistico walk-forward (entrena con dias previos; test {test[0]}..{test[-1]}, n={len(S)}, {len(dd_)} d) base [lpc,s_M10] AUC {b0:.4f}; inversion base {auc_strat(S.assign(sc_base=-S.sc_base), "sc_base"):.4f} ==')
gain = {}
for nm in list(SETS)[1:]:
    g_ = auc_strat(S, 'sc_' + nm) - b0; ci = dboot('sc_' + nm); gain[nm] = g_; print('  %-22s AUC %.4f ganancia %+.4f IC90 dias (%+.4f,%+.4f)' % (nm, auc_strat(S, 'sc_' + nm), g_, ci[0], ci[1]), flush=True)
# --- permutacion (placebo propio) para las especificaciones no-placebo: null de la ganancia con mid permutado dia x moneda x qb ---
NP = 150; K = 0
print('\n== permutacion dia x moneda x qb (%d perms) del bloque mid; p una cola de la ganancia ==' % NP)
tests = {'+15m_T': (['mid15_con_T','dis15'], lambda X: (X.mid15_con_T, X.mid15_con_T - X.pcon)), '+5m+15m_T': (None, None)}
nulls = {k: [] for k in ('+15m_T', '+5m_T', '+5m+15m_T')}
for p in range(NP):
    P = T.copy(); P['m5'] = shuf('mid5_con_T'); P['m15'] = shuf('mid15_con_T'); P['d5'] = P.m5 - P.pcon; P['d15'] = P.m15 - P.pcon; P['gT'] = P.m15 - P.m5
    for nm, cols in (('+15m_T', ['m15','d15']), ('+5m_T', ['m5','d5']), ('+5m+15m_T', ['m5','d5','m15','d15','gT'])):
        sc = walk(B + cols, P); P['sc_x'] = sc; SS = P.dropna(subset=['sc_x']).reset_index(drop=True); SS['sc_b'] = S.sc_base.values[:len(SS)] if len(SS) == len(S) else np.nan
        nulls[nm].append(auc_strat(SS, 'sc_x') - b0)
    if p % 50 == 49: print('  perm', p + 1, flush=True)
for nm, v in nulls.items():
    v = np.array(v); print('  %-12s ganancia real %+.4f | null media %+.4f sd %.4f | p(null >= real) = %.3f (Bonferroni x%d specs = %.2f)' % (nm, gain[nm], v.mean(), v.std(), (1 + (v >= gain[nm]).sum()) / (NP + 1), len(SETS) - 1, min(1, (1 + (v >= gain[nm]).sum()) / (NP + 1) * (len(SETS) - 1))))
# --- desagregado moneda x marco ---
print('\n== desagregado moneda x marco (ganancia AUC_strat sobre base; test; IC90 por dias) ==')
for nm in ('+5m_T', '+15m_T', '+5m+15m_T', '+resid5', '+resid15'):
    row = []
    for c in sorted(S.coin.unique()):
        d = S[S.coin == c].reset_index(drop=True)
        if len(d) < 150: continue
        g_ = auc_strat(d, 'sc_' + nm) - auc_strat(d, 'sc_base'); dk = d.dstr.unique(); ii = {k: x.index.values for k, x in d.groupby('dstr')}; v = []
        for _ in range(300):
            x = d.loc[np.concatenate([ii[k] for k in rg.choice(dk, len(dk))])].reset_index(drop=True); v.append(auc_strat(x, 'sc_' + nm) - auc_strat(x, 'sc_base'))
        row.append('%s n=%d %+.3f (%+.3f,%+.3f)' % (c, len(d), g_, *np.percentile(v, [5, 95])))
    print('  %-10s ' % nm + ' | '.join(row))
T.to_pickle(f'{D}/pista_T.pkl')
