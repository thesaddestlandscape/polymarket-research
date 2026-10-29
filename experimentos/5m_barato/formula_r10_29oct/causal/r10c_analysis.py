#!/usr/bin/env python3
"""r10c_analysis (29-Oct): (B) reentreno causal de la misma familia HGB (IS 06-15, OOS 16-27) sobre hz causal; (C) ingenieria inversa: P(y) con L1 del complementario en t. Contabilidad 1 relleno por (dia,token); EV ponderado por EUR; IC90 por dias. Salida: salida_r10c_analysis.txt. Sin tocar originales ni el modelo sha 5e495915."""
import sys, subprocess; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupKFold
HERE = E4 + 'formula_r10_29oct/causal/'; N = 10.0; L = []
def P(s): print(s, flush=True); L.append(s)
Z = np.load(HERE + 'hz_BTC.npz', allow_pickle=True); days = list(Z['days']); nd = len(days); IS, OOS, DEV = part(days); OO = OOS + DEV
di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; F_ = Z['F'].astype(float); COLS = [str(c) for c in Z['cols']]; nc = int(Z['ncore']); tg = Z['tg']; fl = Z['fl']; tf = Z['tf']; yy = Z['Y10'].astype(int); a215 = Z['a215']
col = lambda c: F_[:, COLS.index(c)]; trem = col('trem'); bb = col('bb'); isI = np.isin(di, IS); isO = ~isI; FEE = lambda p: 0.07 * p * (1 - p)
P('hz causal: filas %d, dias %d (IS %d, OOS16-27 %d), columnas %d (nucleo %d). y medio %.4f' % (len(y), nd, len(IS), len(OO), len(COLS), nc, y.mean()))
r = subprocess.run([sys.executable, HERE + 'test_nan_predice_y.py', HERE + 'hz_BTC.npz', '--strat', 'bb', '--filas', '(trem>=15)&(trem<286)'], capture_output=True, text=True); P('== TEST NaN-predice-y sobre hz causal (todas las columnas, T15-286)')
P('\n'.join(x for x in r.stdout.splitlines() if ('FUGA' in x or 'RESULTADO' in x or 'filas' in x))); P('(salida completa en salida_test_nan_causal.txt)'); open(HERE + 'salida_test_nan_causal.txt', 'w').write(r.stdout)
def daystat(pnl, cost, ds):
    dn = np.bincount(di, weights=pnl, minlength=nd); dd = np.bincount(di, weights=cost, minlength=nd); sel = [i for i in ds if dd[i] > 0]
    nf = int(np.sum(cost > 0))
    if len(sel) < 2: return 'n%d (dias<2)' % nf
    ev = dn[sel] / dd[sel]; m, lo, hi = r4.tci(ev); return 'EVw%+.3f [%+.3f,%+.3f] +%d/%d sin2%+.3f n%d' % (dn[sel].sum() / dd[sel].sum(), lo, hi, (ev > 0).sum(), len(sel), np.sort(ev)[:-2].mean() if len(ev) > 3 else np.nan, nf)
def first_per_tok(mask, key=None):
    ii = np.flatnonzero(mask); k = t if key is None else key; o = ii[np.lexsort((k[ii], u[ii], di[ii]))]; kk = np.stack([di[o], u[o]], 1); _, f = np.unique(kk, axis=0, return_index=True); out = np.zeros(len(mask), bool); out[o[f]] = True; return out
def dedupe(sel):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
def mk(ff, m):  # relleno maker (m indice 0..2)
    return np.where(ff, N * (y - tg[:, m]), 0.0), np.where(ff, N * tg[:, m], 0.0)
def rep(nm, ff, m):
    p, c = mk(ff, m); return '%-46s IS %s || OOS %s' % (nm, daystat(p, c, IS), daystat(p, c, OO))
def firstfill(f, m): return first_per_tok(f, tf[:, m])
hgb = lambda: HistGradientBoostingClassifier(max_iter=200, learning_rate=0.07, max_depth=5, min_samples_leaf=100, random_state=1)
lg = lambda p: np.log(np.clip(p, 1e-6, 1 - 1e-6) / (1 - np.clip(p, 1e-6, 1 - 1e-6))).reshape(-1, 1)
v3 = np.isfinite(tg[:, 2]); TB = (trem >= 200) & (trem < 286); idx = np.flatnonzero(isI)
P('\n== (B) REENTRENO CAUSAL (HGB d5/hoja100/200 it, 30 columnas nucleo, etiqueta Y10, Platt, umbral q05 del OOF IS, regla INVERSION m=3 vida 10 s relleno estricto, 1 relleno/(dia,token))')
Fc = F_[:, :nc]; oof = np.zeros(len(idx))
for a, b in GroupKFold(5).split(idx, groups=di[idx]): oof[b] = hgb().fit(Fc[idx[a]], yy[idx[a]]).predict_proba(Fc[idx[b]])[:, 1]
m_ = hgb().fit(Fc[idx], yy[idx]); pO = m_.predict_proba(Fc[isO])[:, 1]; pl = LogisticRegression().fit(lg(oof), yy[idx])
score = np.full(len(di), np.nan); score[idx] = pl.predict_proba(lg(oof))[:, 1]; score[isO] = pl.predict_proba(lg(pO))[:, 1]; thr = float(np.quantile(score[idx], 0.05))
P('AUC Y10: IS(OOF) %.3f | OOS %.3f; thr %.5f' % (roc_auc_score(yy[idx], oof), roc_auc_score(yy[isO], pO), thr))
sel = v3 & (score <= thr); ff = firstfill(fl[:, 2] & dedupe(sel), 2); P(rep('HGB-bajo causal (todas T)', ff, 2))
ff2 = firstfill(fl[:, 2] & dedupe(sel & TB), 2); P(rep('HGB-bajo causal T200-286', ff2, 2))
selh = v3 & (score >= float(np.quantile(score[idx], 0.95))); P(rep('HGB-ALTO q95 (cola contraria)', firstfill(fl[:, 2] & dedupe(selh), 2), 2))
fS = firstfill(fl[:, 2] & dedupe(v3), 2); P(rep('SIEMPRE (todas las filas validas)', fS, 2)); P(rep('SIEMPRE T200-286', firstfill(fl[:, 2] & dedupe(v3 & TB), 2), 2))
rng = np.random.default_rng(7); ev_r = []
for sd in range(20):
    fA = np.zeros(len(di), bool); pS = dedupe(v3)
    for ds, tag in ((IS, 'IS'), (OO, 'OO')):
        mp = np.isin(di, ds); fr = dedupe(sel)[mp].sum() / max(1, pS[mp].sum()); s_ = np.flatnonzero(pS & mp); fA[s_[rng.random(len(s_)) < fr]] = True
    p, c = mk(firstfill(fl[:, 2] & fA, 2), 2); dn = np.bincount(di, weights=p, minlength=nd); dd = np.bincount(di, weights=c, minlength=nd); ok = [i for i in OO if dd[i] > 0]; ev_r.append(dn[ok].sum() / dd[ok].sum())
P('ALEATORIO (misma fraccion, 20 semillas) OOS EVw media %+.3f [min %+.3f, max %+.3f]' % (np.mean(ev_r), np.min(ev_r), np.max(ev_r)))
sc_ = StandardScaler().fit(np.nan_to_num(Fc[idx])); lr = LogisticRegression(max_iter=300, C=0.3).fit(sc_.transform(np.nan_to_num(Fc[idx])), yy[idx]); sl = lr.decision_function(sc_.transform(np.nan_to_num(Fc))); thl = float(np.quantile(sl[idx], 0.05))
P(rep('logit-bajo causal (q05 IS)', firstfill(fl[:, 2] & dedupe(v3 & (sl <= thl)), 2), 2)); P(rep('logit-bajo causal T200-286', firstfill(fl[:, 2] & dedupe(v3 & (sl <= thl) & TB), 2), 2))
P('Nota: umbral/regla fijados con IS; OOS 16-27 solo reportado. Regla original (hazard bajo) fue descubierta mirando el OOS en R8/R9 (no limpia).')

P('\n== (C) INGENIERIA INVERSA: P(y) en t con L1 propio + L1 del complementario (todo <= t); modelos fijados con IS')
base = ['bb', 'spr', 'bs', 'trem']; cx = base + ['dbb1', 'dbb5', 'cbb', 'dcbb1', 'dcbb5', 'cba', 'cspr', 'cbs', 'dcba1', 'dcba5', 'sumb', 'suma']
def design(names):
    A = np.column_stack([col(c) for c in names]); fl_ = [np.isnan(col(c)).astype(float) for c in ('cbb', 'cba') if c in names]
    return np.column_stack([np.where(np.isnan(A), 0.0, A)] + fl_)
mods = {}
for nm, names in (('BASE(bb,spr,bs,trem)', base), ('CX logit', cx)):
    X = design(names); s_ = StandardScaler().fit(X[isI]); m = LogisticRegression(max_iter=500, C=1.0).fit(s_.transform(X[isI]), y[isI]); mods[nm] = m.predict_proba(s_.transform(X))[:, 1]
X = design(cx); mh = HistGradientBoostingClassifier(max_iter=100, learning_rate=0.05, max_depth=3, min_samples_leaf=300, random_state=1).fit(X[isI], y[isI]); mods['CX hgb d3'] = mh.predict_proba(X)[:, 1]
ask = a215; okA = np.isfinite(ask) & (ask > 0.02) & (ask < 0.98)
for nm, ph in mods.items():
    brO = np.mean((ph[isO] - y[isO]) ** 2); brM = np.mean((bb[isO] + 0.005 - y[isO]) ** 2); P('%-22s Brier OOS %.4f (mid-bb %.4f) | corr(ph, y) IS %.3f OOS %.3f | AUC OOS %.3f' % (nm, brO, brM, np.corrcoef(ph[isI], y[isI])[0, 1], np.corrcoef(ph[isO], y[isO])[0, 1], roc_auc_score(y[isO], ph[isO])))
MARG = (0.05, 0.10, 0.15)
def tomador(ph, mg, perm=None):
    sel = okA & (ph - ask - FEE(ask) >= mg); ff = first_per_tok(sel); p = np.where(ff, N * (y - ask - FEE(ask)), 0.0); c = np.where(ff, N * (ask + FEE(ask)), 0.0); return ff, p, c
P('-- TOMADOR al ask real a t+215 ms (fee 0,07p(1-p)); entra la 1a fila del token con ph - ask - fee >= margen; 1 por (dia,token)')
for nm, ph in mods.items():
    for mg in MARG:
        ff, p, c = tomador(ph, mg); P('%-22s margen %.2f: IS %s || OOS %s' % (nm, mg, daystat(p, c, IS), daystat(p, c, OO)))
P('-- MAKER bb-m con relleno estricto (sin rebate); entra si ph - tg >= margen (precio objetivo), 1 relleno/(dia,token)')
for nm in ('CX logit', 'CX hgb d3'):
    ph = mods[nm]
    for mm in (0, 2):
        for mg in (0.05, 0.10):
            s_ = np.isfinite(tg[:, mm]) & (ph - tg[:, mm] >= mg); ffm = firstfill(fl[:, mm] & dedupe(s_), mm); P(rep('%s bb-%dc margen %.2f' % (nm, mm + 1, mg), ffm, mm))
P('-- PLACEBO tomador (CX logit): ph permutado dentro de cada dia (400 perms), estadistico = max sobre margenes de EVw OOS 16-27; p = frac(perm >= real)')
ph = mods['CX logit']; real = []
def evw(ph_, mg):
    ff, p, c = tomador(ph_, mg); dn = np.bincount(di, weights=p, minlength=nd); dd = np.bincount(di, weights=c, minlength=nd); ok = [i for i in OO if dd[i] > 0]
    return dn[ok].sum() / dd[ok].sum() if ok and dd[ok].sum() > 0 else -9.0
real = max(evw(ph, mg) for mg in MARG); pm = []; rng = np.random.default_rng(11); byday = [np.flatnonzero(di == d) for d in range(nd)]
for k in range(400):
    pp = ph.copy()
    for ii in byday: pp[ii] = ph[ii][rng.permutation(len(ii))]
    pm.append(max(evw(pp, mg) for mg in MARG))
pm = np.array(pm); P('real max EVw %+.3f | placebo media %+.3f p95 %+.3f max %+.3f | p = %.3f' % (real, pm.mean(), np.quantile(pm, .95), pm.max(), (pm >= real).mean()))
open(HERE + 'salida_r10c_analysis.txt', 'w').write('\n'.join(L))
