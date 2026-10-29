#!/usr/bin/env python3
"""Robustez R10 (29-Oct): (1) HGB regularizado x 5 semillas + walk-forward dentro del IS; (2) importancias por permutacion + PDP del modelo congelado (solo lectura).
Solo se entrena con IS 06-15. OOS 16-27 solo se reporta. Salida: rep/salida_robustez.txt, rep/robustez_scores.npz"""
import sys, os; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
from r8lib import *
import pickle, hashlib
from sklearn.ensemble import HistGradientBoostingClassifier as H
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score, log_loss
R10 = BASE; N = 10.0
Z = np.load(R10 + 'hz_BTC.npz', allow_pickle=True); days = list(Z['days']); nd = len(days); IS, OOS, DEV = part(days); OO = OOS + DEV
di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; F_ = Z['F'].astype(float); COLS = list(Z['cols']); tg = Z['tg']; fl = Z['fl']; tf = Z['tf']; yy = Z['Y10'].astype(int)
trem = F_[:, COLS.index('trem')]; isI = np.isin(di, IS); isO = ~isI; v3 = np.isfinite(tg[:, 2])
L = []
def P(s): print(s, flush=True); L.append(s)
def dedupe(sel):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
def firstfill(f, key=None):
    key = u if key is None else key
    ii = np.flatnonzero(f); o = ii[np.argsort(tf[ii, 2], kind='stable')]
    k = np.stack([di[o], key[o]], 1); _, first = np.unique(k, axis=0, return_index=True); out = np.zeros(len(f), bool); out[o[first]] = True; return out
def stats(f, ds):
    num = np.where(f, N * (y - tg[:, 2]), 0.0); den = np.where(f, N * tg[:, 2], 0.0); dn = np.bincount(di, weights=num, minlength=nd); dd = np.bincount(di, weights=den, minlength=nd)
    sel = [i for i in ds if dd[i] > 0]
    if len(sel) < 2: return None
    ev = dn[sel] / dd[sel]; m, lo, hi = r4.tci(ev); fm = f & np.isin(di, ds)
    return dict(n=int(fm.sum()), nd=len(sel), evw=float(dn[sel].sum() / dd[sel].sum()), lo=lo, hi=hi, pos=int((ev > 0).sum()), s2=float(np.sort(ev)[:-2].mean()) if len(ev) > 3 else float('nan'), eurd=float(np.mean(dn[ds])))
def fmt(s): return '-' if s is None else 'EVw%+.3f [%+.2f,%+.2f] n%d d%d +%d sin2%+.2f %+.1fE/d' % (s['evw'], s['lo'], s['hi'], s['n'], s['nd'], s['pos'], s['s2'], s['eurd'])
def sel_eval(score, thr, ds, tb=None):
    f = fl[:, 2] & dedupe(v3 & (score <= thr) & (True if tb is None else ((trem >= tb[0]) & (trem < tb[1])))); f = firstfill(f); return stats(f, ds)
VAR = {
 'base d5/l100/i200': dict(max_iter=200, learning_rate=0.07, max_depth=5, min_samples_leaf=100),
 'reg1 d3/l300/i150': dict(max_iter=150, learning_rate=0.05, max_depth=3, min_samples_leaf=300, l2_regularization=5.0),
 'reg2 d3,8hojas/l800/i80': dict(max_iter=80, learning_rate=0.05, max_depth=3, max_leaf_nodes=8, min_samples_leaf=800, l2_regularization=20.0),
 'reg3 d2/l1000/i100': dict(max_iter=100, learning_rate=0.05, max_depth=2, min_samples_leaf=1000, l2_regularization=20.0),
}
SEEDS = [1, 2, 3, 4, 5]; idx = np.flatnonzero(isI)
# folds walk-forward dentro del IS (por indice de dia dentro de IS)
WF = [(IS[:4], IS[4:6]), (IS[:6], IS[6:8]), (IS[:8], IS[8:10])]
OUT = {}
for vn, kw in VAR.items():
    P('== variante %s (max_features=0.8 + semilla; base tambien)' % vn)
    oofs = []; prs = []; wfs = []
    for sd in SEEDS:
        mk = lambda: H(random_state=sd, max_features=0.8, **kw)
        oof = np.zeros(len(idx))
        for a, b in GroupKFold(5).split(idx, groups=di[idx]): oof[b] = mk().fit(F_[idx[a]], yy[idx[a]]).predict_proba(F_[idx[b]])[:, 1]
        m = mk().fit(F_[idx], yy[idx]); pO = m.predict_proba(F_[isO])[:, 1]
        sc = np.full(len(di), np.nan); sc[idx] = oof; sc[isO] = pO; thr = float(np.quantile(oof, 0.05)); oofs.append(oof); prs.append(pO)
        # walk-forward: entrena en tr, umbral = q05 de la prediccion del propio fold test (sin etiquetas)
        wf = np.full(len(di), np.nan); wthr = {}
        for tr, te in WF:
            itr = np.isin(di, tr); ite = np.isin(di, te); mm = mk().fit(F_[itr], yy[itr]); wf[ite] = mm.predict_proba(F_[ite])[:, 1]; wthr[tuple(te)] = float(np.quantile(wf[ite], 0.05))
        fw = np.zeros(len(di), bool)
        for tr, te in WF: ite = np.isin(di, te); fw |= v3 & ite & (wf <= wthr[tuple(te)])
        fwf = firstfill(fl[:, 2] & dedupe(fw)); wt = fwf & (trem >= 200) & (trem < 286)
        sA = sel_eval(sc, thr, OO); sT = sel_eval(sc, thr, OO, (200, 286)); sI = sel_eval(sc, thr, IS, (200, 286))
        auc = roc_auc_score(yy[isO], pO)
        P('  semilla %d thr %.4f AUC_OOS %.3f | IS(OOF) T200-286 %s | OOS16-27 todaT %s | OOS T200-286 %s | WF(6d, IS) todaT %s T200-286 %s' % (sd, thr, auc, fmt(sI), fmt(sA), fmt(sT), fmt(stats(fwf, WF[0][1] + WF[1][1] + WF[2][1])), fmt(stats(wt, WF[0][1] + WF[1][1] + WF[2][1]))))
        OUT.setdefault(vn, {})[sd] = (thr, sA, sT)
    # ensemble de las 5 semillas
    oofm = np.mean(oofs, 0); pOm = np.mean(prs, 0); sc = np.full(len(di), np.nan); sc[idx] = oofm; sc[isO] = pOm; thr = float(np.quantile(oofm, 0.05))
    P('  ENSEMBLE5 thr %.4f | IS T200-286 %s | OOS todaT %s | OOS T200-286 %s' % (thr, fmt(sel_eval(sc, thr, IS, (200, 286))), fmt(sel_eval(sc, thr, OO)), fmt(sel_eval(sc, thr, OO, (200, 286)))))
    ev = [OUT[vn][s][2]['evw'] if OUT[vn][s][2] else np.nan for s in SEEDS]; ea = [OUT[vn][s][1]['evw'] if OUT[vn][s][1] else np.nan for s in SEEDS]; th = [OUT[vn][s][0] for s in SEEDS]
    P('  DISPERSION 5 semillas: OOS T200-286 EVw media %+.3f sd %.3f rango [%+.3f,%+.3f] | OOS todaT media %+.3f sd %.3f [%+.3f,%+.3f] | thr q05 media %.4f sd %.4f' % (np.nanmean(ev), np.nanstd(ev), np.nanmin(ev), np.nanmax(ev), np.nanmean(ea), np.nanstd(ea), np.nanmin(ea), np.nanmax(ea), np.mean(th), np.std(th)))
    np.savez('/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep/robustez_scores_%s.npz' % vn.split()[0], sc=sc)
# ---------- (2) importancia + PDP del modelo congelado
pk = open(R10 + 'frozen_R10_hgb_BTC.pkl', 'rb').read(); P('== modelo congelado sha %s' % hashlib.sha256(pk).hexdigest()[:8]); M = pickle.loads(pk)['hgb']
rng = np.random.default_rng(11); io = np.flatnonzero(isO); io = io[rng.random(len(io)) < 0.5]
p0 = M.predict_proba(F_[io])[:, 1]; base_ll = log_loss(yy[io], p0); base_auc = roc_auc_score(yy[io], p0); q05b = np.quantile(p0, 0.05)
P('  OOS submuestra n%d logloss %.4f AUC %.3f' % (len(io), base_ll, base_auc))
imp = []
for j, c in enumerate(COLS):
    d_ll = []; d_sh = []
    for r in range(3):
        X = F_[io].copy(); X[:, j] = X[rng.permutation(len(io)), j]; p = M.predict_proba(X)[:, 1]; d_ll.append(log_loss(yy[io], p) - base_ll); d_sh.append(roc_auc_score(yy[io], p) - base_auc)
    imp.append((np.mean(d_ll), np.mean(d_sh), c))
imp.sort(reverse=True); P('  importancia por permutacion (OOS, sube logloss / baja AUC): ' + '; '.join('%s %+.4f/%+.3f' % (c, a, b) for a, b, c in imp[:12]))
top = [c for _, _, c in imp[:8]]; ii = np.flatnonzero(isI); ii = ii[rng.random(len(ii)) < 0.1]; ib = F_[ii]
for c in top:
    j = COLS.index(c); g = np.nanquantile(F_[isI, j], [0.05, 0.2, 0.35, 0.5, 0.65, 0.8, 0.95]); out = []
    for v in g: X = ib.copy(); X[:, j] = v; out.append(M.predict_proba(X)[:, 1].mean())
    P('  PDP %-7s grid %s -> p(Y10) %s' % (c, ' '.join('%.3g' % v for v in g), ' '.join('%.3f' % v for v in out)))
P('  p(Y10) base IS %.3f ; cortes quantiles IS q05 de p: %.4f' % (yy[isI].mean(), np.quantile(M.predict_proba(F_[ii])[:, 1], 0.05)))
open('/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep/salida_robustez.txt', 'w').write('\n'.join(L))
