#!/usr/bin/env python3
"""r10_train (copia de r9c.py solo E2/BTC con hz_BTC corregido; mismo protocolo IS 06-15/OOS 16-25/DEV 26-27). r9c: E2 (INVERSION HGB BTC: reproduccion, refutacion, congelacion) + E5 (ETH T120-200 hazard bajo m=3: congelacion). Manda PREREG_R9.md (+A1)."""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
import pickle, hashlib
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GroupKFold
R9 = E4 + 'formula_r10_29oct/'; N = 10.0
def hgb(): return HistGradientBoostingClassifier(max_iter=200, learning_rate=0.07, max_depth=5, min_samples_leaf=100, random_state=1)
def load(coin):
    Z = np.load(R9 + 'hz_%s.npz' % coin, allow_pickle=True); days = list(Z['days']); return Z, days, len(days), part(days)
def dedupe(sel, di, u, t):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
def line(R, f, ds, nd):
    s = summ(R, f, ds, nd)
    return ('%+.3f [%+.3f,%+.3f] +%d/%d sin2 %+.3f %.0fE/d n%d' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'], s['s2'], s['eurd'], s['nf'])) if s else '-'
def three(R, f, P3, nd): return ' | '.join('%s %s' % (pn, line(R, f, ds, nd)) for pn, ds in zip(('IS', 'OOS', 'DEV'), P3))
# ---------------- E2 BTC
Z, days, nd, (IS, OOS, DEV) = load('BTC'); di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; F_ = Z['F'].astype(float); COLS = list(Z['cols']); tg = Z['tg']; fl = Z['fl']
isI = np.isin(di, IS); isO = ~isI; yy = Z['Y10'].astype(int); idx = np.flatnonzero(isI); oof = np.zeros(len(idx))
for a, b in GroupKFold(5).split(idx, groups=di[idx]): oof[b] = hgb().fit(F_[idx[a]], yy[idx[a]]).predict_proba(F_[idx[b]])[:, 1]
m = hgb().fit(F_[isI], yy[isI]); pO = m.predict_proba(F_[isO])[:, 1]
lg = lambda p: np.log(np.clip(p, 1e-6, 1 - 1e-6) / (1 - np.clip(p, 1e-6, 1 - 1e-6))).reshape(-1, 1)
pl = LogisticRegression().fit(lg(oof), yy[isI]); score = np.full(len(di), np.nan); score[idx] = pl.predict_proba(lg(oof))[:, 1]; score[isO] = pl.predict_proba(lg(pO))[:, 1]
thr = float(np.quantile(score[isI], 0.05)); pk = pickle.dumps(dict(hgb=m, platt=pl, thr=thr, regla='INVERSION: score<=thr, m=3 (bb-0,03), vida 10 s, relleno estricto, una orden/10,3 s por token, filas 2 s T_rem 15-285, bb 0,10-0,35'))
open(R9 + 'frozen_R10_hgb_BTC.pkl', 'wb').write(pk); P('== R9 E2 BTC: modelo congelado frozen_R10_hgb_BTC.pkl sha256 %s thr %.6f' % (hashlib.sha256(pk).hexdigest(), thr))
v3 = np.isfinite(tg[:, 2]); kI = dedupe(v3 & (score <= thr), di, u, t); fI = fl[:, 2] & kI
R = dict(di=di, num=np.where(fI, N * (y - tg[:, 2]), 0.0), den=np.where(fI, N * tg[:, 2], 0.0)); P('  (i) reproduccion INVERSION: %s' % three(R, fI, (IS, OOS, DEV), nd))
e, d_, n_ = r6a.dayev(R, fI, nd); ok = [i for i in range(nd) if d_[i] > 0]; o2 = sorted(ok, key=lambda i: -n_[i])[:2]; rest = [i for i in ok if i not in o2]
P('  (ii) dias con relleno %d; 2 mejores dias (%s) aportan %.0f %% del pnl; EV pooled sin ellos %+.3f; EV por dia: %s' % (len(ok), ','.join(days[i][-2:] for i in o2), 100 * n_[o2].sum() / max(1e-9, n_[ok].sum()), n_[rest].sum() / d_[rest].sum(), ' '.join('%s:%+.2f' % (days[i][-2:], e[i]) for i in ok)))
mk = np.unique(np.c_[di[fI], u[fI]], axis=0); P('  (iii) rellenos %d en %d (dia,token) distintos; ordenes %d' % (fI.sum(), len(mk), kI.sum()))
fS = fl[:, 2] & dedupe(v3, di, u, t)
P('  (iv) perfil mediana [bajo-relleno | SIEMPRE-relleno]: ' + '; '.join('%s %.3g|%.3g' % (c, np.nanmedian(F_[fI, COLS.index(c)]), np.nanmedian(F_[fS, COLS.index(c)])) for c in COLS))
P('      y medio bajo-relleno %.3f (precio %.3f) | SIEMPRE-relleno %.3f (precio %.3f)' % (y[fI].mean(), tg[fI, 2].mean(), y[fS].mean(), tg[fS, 2].mean()))
# (v) origen del print que rellena + coherencia del libro
ORG = np.full(len(di), -1); COH = np.full(len(di), np.nan); COH2 = np.full(len(di), np.nan)
for i_ in sorted(set(di[fI].tolist())):
    D = Day(days[i_], 'BTC'); rr = np.flatnonzero(fI & (di == i_))
    for r in rr:
        st, se, sp, ss, so = stream_src(D, int(u[r])); j = fillsrch(st, sp, t[r] + 73.0, tg[r, 2])
        if j >= 0: ORG[r] = so[j]
        c = int(D.comp[int(u[r])])
        if c >= 0:
            cb, ca, _ = D.l1(c, [t[r]]); COH[r] = F_[r, COLS.index('bb')] + cb[0]; COH2[r] = F_[r, COLS.index('bb')] - (1 - ca[0])
for nm, mm in (('propio', ORG == 0), ('complementario', ORG == 1)):
    f2 = fI & mm; R2 = dict(di=di, num=np.where(f2, N * (y - tg[:, 2]), 0.0), den=np.where(f2, N * tg[:, 2], 0.0)); P('  (v) origen %-14s n %d: %s' % (nm, f2.sum(), three(R2, f2, (IS, OOS, DEV), nd)))
inc = fI & (COH > 1.005); P('      libros con bb+bb_comp>1 (cruzados) %d de %d; bb−(1−ask_comp)>0,02: %d; EV de los cruzados %s' % (inc.sum(), fI.sum(), (fI & (COH2 > 0.02)).sum(), line(dict(di=di, num=np.where(inc, N * (y - tg[:, 2]), 0.0), den=np.where(inc, N * tg[:, 2], 0.0)), inc, list(range(nd)), nd)))
trem = F_[:, COLS.index('trem')]
for lo_, hi_ in ((15, 60), (60, 120), (120, 200), (200, 286)):
    f2 = fI & (trem >= lo_) & (trem < hi_); P('  (vi) T_rem %3d-%3d: %s' % (lo_, hi_, three(R, f2, (IS, OOS, DEV), nd)))
for lo_, hi_ in ((0.09, 0.15), (0.15, 0.22), (0.22, 0.2901)):
    f2 = fI & (tg[:, 2] >= lo_ - 1e-9) & (tg[:, 2] < hi_); P('  (vi) precio [%.2f,%.2f): %s' % (lo_, hi_, three(R, f2, (IS, OOS, DEV), nd)))

# ---- comparadores (PREREG_R10): SIEMPRE ya = fS; ALEATORIO misma fraccion por particion; ALTO = cola contraria (score >= q95 IS)
rng = np.random.default_rng(7); pS = dedupe(v3, di, u, t); fA = np.zeros(len(di), bool)
for ds in (IS, OOS, DEV):
    mp = np.isin(di, ds); fr = kI[mp].sum() / max(1, pS[mp].sum()); sel_ = np.flatnonzero(pS & mp); fA[sel_[rng.random(len(sel_)) < fr]] = True
fAl = fl[:, 2] & fA; hi = dedupe(v3 & (score >= float(np.quantile(score[isI], 0.95))), di, u, t); fH = fl[:, 2] & hi
for nm, ff in (('SIEMPRE', fS), ('ALEATORIO', fAl), ('ALTO q95', fH)):
    R3 = dict(di=di, num=np.where(ff, N * (y - tg[:, 2]), 0.0), den=np.where(ff, N * tg[:, 2], 0.0)); P('  comparador %-10s %s' % (nm, three(R3, ff, (IS, OOS, DEV), nd)))
P('  cobertura bid15 (no NaN) en filas: %.3f ; mediana bid15 %.3f ; corr(bid15,bb) %.3f' % (np.mean(np.isfinite(F_[:, COLS.index('bid15')])), np.nanmedian(F_[:, COLS.index('bid15')]), np.corrcoef(*[x[np.isfinite(F_[:, COLS.index('bid15')])] for x in (F_[:, COLS.index('bid15')], F_[:, COLS.index('bb')])])[0, 1]))
open(R9 + 'salida_r10_train.txt', 'w').write('\n'.join(r6a.LINES))
