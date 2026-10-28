#!/usr/bin/env python3
"""r9a: E1 (red de sobre-disparo, puja profunda bb-4..-6) + E4 (estricto vs toque). Manda PREREG_R9.md (sha 9053254d)."""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
import time
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
R9 = E4 + 'formula_r9_28oct/'; coin = 'BTC'; Z = np.load(BASE + 'hz_%s.npz' % coin, allow_pickle=True)
days = list(Z['days']); nd = len(days); IS, OOS, DEV = part(days); OOS2 = OOS + DEV
di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; COLS = list(Z['cols']); F_ = Z['F'].astype(float); bb = F_[:, COLS.index('bb')]; trem = F_[:, COLS.index('trem')]
MS = (1, 2, 3, 4, 5, 6); LIV = (2000.0, 10000.0, 30000.0); NR = len(di)
TG = np.full((NR, 6), np.nan)
for mi, m in enumerate(MS):
    g = np.round(bb - m * 0.01, 2); ok = (g >= 0.09 - 1e-9) & (g <= 0.29 + 1e-9); TG[ok, mi] = g[ok]
CACHE = R9 + 'fills_r9_%s.npz' % coin
def sparse_min(a):
    T = [a]; k = 1
    while 2 * k <= len(a): p = T[-1]; T.append(np.minimum(p[:-k], p[k:])); k *= 2
    return T
def qmin(T, i0, i1):
    n = i1 - i0; out = np.full(len(i0), np.inf); ok = n > 0
    if not ok.any(): return out
    lv = np.zeros(len(i0), int); lv[ok] = np.floor(np.log2(n[ok])).astype(int)
    for L in np.unique(lv[ok]):
        s = ok & (lv == L); a = T[L]; out[s] = np.minimum(a[i0[s]], a[i1[s] - (1 << L)])
    return out
if not os.path.exists(CACHE):
    t0 = time.time(); MN = np.full((NR, 3), np.inf)
    for i, d in enumerate(days):
        D = Day(d, coin); rows = np.flatnonzero(di == i)
        for uu in np.unique(u[rows]):
            r = rows[u[rows] == uu]; st, se, sp, ss = D.stream(int(uu))
            if len(st) == 0: continue
            SP = sparse_min(sp.astype(float)); c0 = float(D.cie[int(uu)]) * 1000.0; a0 = t[r] + 73.0 + 26.0
            i0 = np.searchsorted(st, a0, 'left')
            for li, L in enumerate(LIV):
                i1 = np.searchsorted(st, np.minimum(a0 + L, c0), 'left'); MN[r, li] = qmin(SP, i0, np.maximum(i1, i0))
        print(d, '%.0f s' % (time.time() - t0), flush=True)
    np.savez_compressed(CACHE, MN=MN)
MN = np.load(CACHE)['MN']
STR = MN[:, :, None] < TG[:, None, :] - 1e-9; TOQ = MN[:, :, None] <= TG[:, None, :] + 1e-9  # [fila, vida, m]
v = np.isfinite(Z['tg'][:, 0]); P('== R9 E1/E4 [%s] filas %d; reproduccion R8 (m=1..3, vida 10 s, estricto) coincidencia fl: %s' % (coin, NR, ' '.join('%.4f' % (STR[np.isfinite(Z['tg'][:, k]), 1, k] == Z['fl'][np.isfinite(Z['tg'][:, k]), k]).mean() for k in range(3))))
isI = np.isin(di, IS); N = 10.0
def prep(A): return np.hstack([np.where(np.isnan(A), 0.0, A), np.isnan(A[:, [COLS.index(c) for c in ('cbb', 'bid15', 'comp_acc5')]]).astype(float)])
yy = Z['Y10'].astype(int); sc_ = StandardScaler().fit(prep(F_[isI])); lr = LogisticRegression(max_iter=300, C=0.3).fit(sc_.transform(prep(F_[isI])), yy[isI]); score = lr.decision_function(sc_.transform(prep(F_)))
import pickle, hashlib; pk = pickle.dumps((sc_, lr)); open(R9 + 'logit_hz_%s.pkl' % coin, 'wb').write(pk); P('  logit IS guardado sha256 %s' % hashlib.sha256(pk).hexdigest()[:16])
TR = (trem >= 15) & (trem < 120)
def select(cond, li, mi, mode):
    kept = np.zeros(NR, bool); fil = np.zeros(NR, bool); lk = None; nxt = -1e18
    fl_ = STR[:, li, mi]
    for i in np.flatnonzero(cond & np.isfinite(TG[:, mi])):
        k = (di[i], u[i])
        if k != lk: lk = k; nxt = -1e18
        if t[i] < nxt: continue
        kept[i] = True
        if fl_[i]: fil[i] = True
        if mode == 'REPEG': nxt = t[i] + (10000.0 if fl_[i] else 1.0)
        else: nxt = t[i] + LIV[li] + 300.0
    return kept, fil
def RR(mi, fil, fl2=None): return dict(di=di, num=np.where(fil, N * (y - TG[:, mi]), 0.0), den=np.where(fil, N * TG[:, mi], 0.0))
def row(R, f, kept):
    o = []
    for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
        s = summ(R, f, ds, nd); nk = (kept & np.isin(di, ds)).sum(); nf = (f & np.isin(di, ds)).sum()
        o.append('%s %s' % (pn, ('%+.3f [%+.3f,%+.3f] +%d/%d sin2 %+.3f %.0fE/d rell %d/%d' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'], s['s2'], s['eurd'], nf, nk)) if s else '-'))
    return ' | '.join(o)
MODES = (('REPEG', 0), ('FIJA10', 1), ('FIJA30', 2)); pols = []; V = []
P('-- E1 familia 18 (m x modo x q), T_rem [15,120), logit Y10, relleno ESTRICTO')
for m in (4, 5, 6):
    mi = m - 1
    for mn, li in MODES:
        for qq in (0.90, 0.95):
            thr = np.quantile(score[isI], qq); kept, fil = select(TR & (score >= thr), li, mi, mn); R = RR(mi, fil); s = summ(R, fil, IS, nd)
            e, d_, _ = r6a.dayev(R, fil, nd); V.append([e[i] if d_[i] > 0 else 0.0 for i in IS]); pols.append((m, mn, li, qq, thr, kept, fil, R, s['lo'] if s else -9))
            P('  m=%d %-6s q=%.2f %s' % (m, mn, qq, row(R, fil, kept)))
obs, mx = signflip_max(np.array(V)); j = int(np.argmax([p[8] for p in pols])); m, mn, li, qq, thr, kept, fil, R, lo = pols[j]; mi = m - 1
P('-> elegida IS: m=%d %s q=%.2f (cota inf IS %+.3f) p max (18) %.3f' % (m, mn, qq, lo, (mx >= obs[j]).mean()))
rng = np.random.default_rng(9029); base = TR
fr = {pn: (TR & (score >= thr))[np.isin(di, ds)].sum() / max(1, TR[np.isin(di, ds)].sum()) for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV))}
frow = np.array([fr['IS'] if x in IS else (fr['OOS'] if x in OOS else fr['DEV']) for x in range(nd)])[di]
for nm, cm in (('SIEMPRE', TR), ('ALEATORIO', TR & (rng.random(NR) < frow)), ('INVERSION', TR & (score <= np.quantile(score[isI], 1 - qq))), ('ORACULO Y10', TR & yy.astype(bool))):
    k2, f2 = select(cm, li, mi, mn); P('   %-12s %s' % (nm, row(RR(mi, f2), f2, k2)))
for lab, lo_, hi_ in (('[.09,.15)', 0.09, 0.15), ('[.15,.22)', 0.15, 0.22), ('[.22,.29]', 0.22, 0.2901)):
    mk = fil & (TG[:, mi] >= lo_ - 1e-9) & (TG[:, mi] < hi_); P('   objetivo %s: %s' % (lab, row(R, mk, kept & (TG[:, mi] >= lo_ - 1e-9) & (TG[:, mi] < hi_))))
so = summ(R, fil, OOS, nd); P('   cuota OOS %.2f %% ; top dia OOS+DEV %.0f %% del pnl' % (100 * so['eurd'] / 48847.0 if so else 0, 100 * np.max(np.bincount(di[fil & np.isin(di, OOS2)], weights=R['num'][fil & np.isin(di, OOS2)], minlength=nd)) / max(1e-9, abs(R['num'][fil & np.isin(di, OOS2)].sum()))))
P('-- E1 secundario (NO gate): misma familia con relleno TOQUE (print <= tgt, sin cola) — solo OOS')
for (m_, mn_, li_, qq_, thr_, kp, fl0, R0, lo0) in pols:
    ftq = np.zeros(NR, bool); ftq[kp] = TOQ[kp, li_, m_ - 1]; s = summ(RR(m_ - 1, ftq), ftq, OOS, nd)
    P('  m=%d %-6s q=%.2f TOQUE OOS %s' % (m_, mn_, qq_, ('%+.3f [%+.3f,%+.3f] +%d/%d %.0fE/d' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'], s['eurd'])) if s else '-'))
P('-- E4 brecha: SIEMPRE vida 10 s (FIJA10), por m, todas las T_rem y T_rem<120; 22 dias (IS+OOS+DEV) y OOS')
ALL = list(range(nd))
for lab, base_ in (('todas T_rem', np.ones(NR, bool)), ('T_rem<120', TR)):
    for m_ in MS:
        k_, _ = select(base_, 1, m_ - 1, 'FIJA10'); fs = k_ & STR[:, 1, m_ - 1]; ft = k_ & TOQ[:, 1, m_ - 1]; fo = ft & ~fs; o = []
        for nm, f_ in (('estricto', fs), ('toque', ft), ('solo-toque', fo)):
            for pn, ds in (('22d', ALL), ('OOS', OOS)):
                s = summ(RR(m_ - 1, f_), f_, ds, nd); o.append('%s %s %s' % (nm, pn, ('%+.3f [%+.3f,%+.3f] n%d' % (s['pool'], s['lo'], s['hi'], (f_ & np.isin(di, ds)).sum())) if s else '-'))
        P('  %-11s m=%d %s' % (lab, m_, ' | '.join(o)))
open(R9 + 'salida_r9a_%s.txt' % coin, 'w').write('\n'.join(r6a.LINES))
