import sys, os; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
OUT = BASE + 'ev_L_BTC.npz'; FS = 48847.0; N = 10.0
G = json.load(open(r4.I.CACHE)); days = days_incl(); IS, OOS, DEV = part(days); nd = len(days)
KEYS = ('di', 'p', 'y', 'dn', 'cum', 'X8', 'cls', 'src', 'k', 'trem', 'sp0', 'bs0', 'dbb1', 'dtc', 'cmin', 'ba215', 'bb300') + tuple('fA%d_%d' % (m, l) for m in (0, 1, 2) for l in (2, 10))
def build():
    A = {k: [] for k in KEYS}; aud = {k: [] for k in ('di', 'p', 'y', 'dn', 'c200', 't200', 'sz')}
    for di, d in enumerate(days):
        D = Day(d, 'BTC')
        for u in range(D.n):
            win = G.get(str(D.mks[u]))
            if win not in ('YES', 'NO') or D.qhi[u] <= D.qlo[u]: continue
            y = 1.0 if win == ('YES' if D.side[u] == 0 else 'NO') else 0.0
            st, se, sp, ss, so = stream_src(D, u)
            if len(st) == 0: continue
            cid, starts, ends = clusters(se); tot = np.bincount(cid, weights=ss, minlength=len(starts))
            cs = np.cumsum(ss); cum = cs - np.r_[0.0, cs][starts][cid]
            bnow, anow, snow = D.l1(u, st - 5.0); dn = np.where(np.isfinite(bnow), np.round((sp - bnow) / 0.01), np.nan)
            trem = D.cie[u] - st / 1000.0; z = (sp >= 0.09) & (sp <= 0.31) & (trem >= 5) & (trem <= 295)
            zz = z & np.isfinite(dn)
            if zz.any():
                aud['di'].append(np.full(int(zz.sum()), di)); aud['p'].append(sp[zz]); aud['y'].append(np.full(int(zz.sum()), y)); aud['dn'].append(dn[zz])
                aud['c200'].append(cum[zz] >= 200); aud['t200'].append(tot[cid][zz] >= 200); aud['sz'].append(ss[zz])
            for cls, cond in ((1, dn <= -3), (0, dn >= 0)):
                idx = np.flatnonzero(zz & cond & (cum >= 200))
                if len(idx) == 0: continue
                _, fi = np.unique(cid[idx], return_index=True); idx = idx[fi]
                for i in idx:
                    c0 = starts[cid[i]]; t = st[i]; cmin = float(sp[c0:i + 1].min())
                    b1 = D.l1(u, [t - 1005.0])[0][0]; a215 = D.l1(u, [t + 215.0])[1][0]; b300 = D.l1(u, [t + 300.0])[0][0]
                    A['di'].append(di); A['p'].append(sp[i]); A['y'].append(y); A['dn'].append(dn[i]); A['cum'].append(cum[i]); A['cls'].append(cls); A['src'].append(so[i])
                    A['X8'].append(cum[i] >= 800); A['k'].append(i - c0); A['trem'].append(trem[i]); A['sp0'].append((anow[i] - bnow[i]) / 0.01 if np.isfinite(anow[i]) else np.nan)
                    A['bs0'].append(np.log1p(snow[i]) if np.isfinite(snow[i]) else np.nan); A['dbb1'].append((bnow[i] - b1) / 0.01 if np.isfinite(b1) else np.nan)
                    A['dtc'].append(t - st[c0]); A['cmin'].append(cmin); A['ba215'].append(a215); A['bb300'].append(b300)
                    for m in (0, 1, 2):
                        for l in (2, 10):
                            A['fA%d_%d' % (m, l)].append(fillsrch(st, sp, t + 5.0 + 68.0, round(cmin - 0.01 * m, 2), life=1000.0 * l) >= 0)
        P('%s eventos %d' % (d, len(A['di'])))
    A = {k: np.asarray(v, float) for k, v in A.items()}; A.update({'a_' + k: np.concatenate(v).astype(float) for k, v in aud.items()})
    np.savez_compressed(OUT, **A); return A
if not os.path.exists(OUT): build()
Z = np.load(OUT); A = {k: Z[k] for k in Z.files}
def row(R, m):
    o = []
    for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
        s = summ(R, m, ds, nd); o.append('%s %s' % (pn, ('%+.3f [%+.3f,%+.3f] +%d/%d sin2 %+.3f %.0fE/d n=%d' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'], s['s2'], s['eurd'], s['nf'])) if s else '-'))
    return ' | '.join(o)
# Auditoria causal vs total
P('== R8-L1 auditoria: EV/E del comprador del print, clase D_now, dentro de barrido >=200 TOTAL (Bloque 1, look-ahead) vs ACUMULADO (causal)')
Ra = dict(di=A['a_di'].astype(int), num=A['a_sz'] * (A['a_y'] - A['a_p']), den=A['a_sz'] * A['a_p']); dn = A['a_dn']
for nm, ctx in (('TOTAL', A['a_t200'] > 0), ('ACUMULADO', A['a_c200'] > 0), ('total pero aun no acumulado', (A['a_t200'] > 0) & (A['a_c200'] == 0))):
    for lb, cm in (('-3..-4', (dn <= -3) & (dn >= -4)), ('<=-5', dn <= -5), ('0', dn == 0)):
        P('  %-28s %-7s %s' % (nm, lb, row(Ra, ctx & cm)))
di = A['di'].astype(int); p = A['p']; y = A['y']; dnE = A['dn']; cls = A['cls']; X8 = A['X8'] > 0
bk = np.where(p < 0.15, 0, np.where(p < 0.22, 1, 2))
def RB(mask, net=True):
    ba = A['ba215']; ok = mask & np.isfinite(ba) & (ba > 0) & (ba < 1)
    bv = np.where(ok, ba, 0.5); fee = 0.07 * bv * (1 - bv) if net else 0.0
    return dict(di=di, num=np.where(ok, N * (y - bv - fee), 0.0), den=np.where(ok, N * bv, 0.0)), ok
def pol_B(X, cl, L, pl=False):
    base = (cls == (0 if pl else 1)) & (X8 if X == 800 else True)
    if not pl: base &= ((dnE <= -3) & (dnE >= -4)) if cl == '-3..-4' else (dnE <= -3)
    lim = {'0.45': 0.45 + 0 * p, 'p+2': p + 0.02, 'p+4': p + 0.04}[L]
    return base & (A['ba215'] <= lim + 1e-9)
def RA(mask, m, l):
    f = mask & (A['fA%d_%d' % (m, l)] > 0); tg = np.round(A['cmin'] - 0.01 * m, 2)
    return dict(di=di, num=np.where(f, N * (y - tg), 0.0), den=np.where(f, N * tg, 0.0)), f
def pol_A(X, pl=False):
    base = (cls == (0 if pl else 1)) & (X8 if X == 800 else True)
    return base if pl else base & (dnE <= -3)
def dayv(R, m, ds):
    e, d, n = r6a.dayev(R, m, nd); return np.array([n[i] / d[i] if d[i] > 0 else 0.0 for i in ds])
def fam(name, specs):
    P('== %s (EV/E por EUR, IC90 por dias, IS/OOS/DEV)' % name); best = None; V = []
    for lab, R, m in specs:
        s = summ(R, m, IS, nd); V.append(dayv(R, m, IS))
        P('  %-26s %s' % (lab, row(R, m)))
        if s and (best is None or s['lo'] > best[0]): best = (s['lo'], lab, R, m)
    obs, mx = signflip_max(np.array(V)); pmax = [(mx >= o).mean() for o in obs]
    P('  p max-estadistico IS (K=5000): ' + ' '.join('%.3f' % x for x in pmax))
    return best, dict(zip([s[0] for s in specs], pmax))
specsB = []
for X in (200, 800):
    for cl in ('-3..-4', '<=-3'):
        for L in ('0.45', 'p+2', 'p+4'):
            m = pol_B(X, cl, L); R, ok = RB(m); specsB.append(('B X%d %s L=%s' % (X, cl, L), R, ok))
bB, pB = fam('R8-L1 (b) TOMADOR al ask L1 t+215 ms, NETO comision', specsB)
specsA = []
for X in (200, 800):
    for mm in (0, 1, 2):
        for l in (2, 10):
            R, f = RA(pol_A(X), mm, l); specsA.append(('A X%d m=%d vida %ds' % (X, mm, l), R, f))
bA, pA = fam('R8-L1 (a) MAKER reactiva a bb_corr = min cluster - m, alta +73 ms, relleno estricto', specsA)
P('== Elegidas en IS: (b) %s p_max %.3f | (a) %s p_max %.3f' % (bB[1], pB[bB[1]], bA[1], pA[bA[1]]))
for nmF, b in (('b', bB), ('a', bA)):
    lab, R, m = b[1], b[2], b[3]
    P(' [%s] %s' % (nmF, lab)); P('   todo   %s' % row(R, m))
    for k, kl in enumerate(('[.09,.15)', '[.15,.22)', '[.22,.31]')): P('   %-9s %s' % (kl, row(R, m & (bk == k))))
    so = summ(R, m, OOS, nd)
    if so: P('   cuota OOS %.2f %% del flujo S800 (%.0f EUR/d)' % (100 * so['eurd'] / FS, so['eurd']))
    X = 800 if 'X800' in lab else 200
    if nmF == 'b':
        mm = pol_B(X, None, lab.split('L=')[1], pl=True); Rp, okp = RB(mm); P('   PLACEBO coherente D_now>=0: %s' % row(Rp, okp))
        Rg, okg = RB(m, net=False); P('   (bruto de comision: %s)' % row(Rg, okg))
        bam = A['ba215'] - p; okb = m; P('   ask(t+215)-p en ticks: mediana %.1f p90 %.1f; %% eventos con ask finito %.1f' % (np.nanmedian(bam[okb]) / 0.01, np.nanpercentile(bam[okb], 90) / 0.01, 100 * okb.sum() / max(1, ((cls == 1) & (dnE <= -3)).sum())))
    else:
        mm_, ll_ = int(lab.split('m=')[1][0]), int(lab.split('vida ')[1].split('s')[0])
        Rp, fp = RA(pol_A(X, pl=True), mm_, ll_); P('   PLACEBO coherente D_now>=0: %s' % row(Rp, fp))
        P('   tasa de relleno %.1f %%' % (100 * m.sum() / max(1, pol_A(X).sum())))
# (c) clasificador del retraso
P('== R8-L1 (c) clasificador Lr = bb(t+300) > p entre eventos deep X200')
ev = (cls == 1) & (dnE <= -3); Lr = (A['bb300'] > p + 1e-9)
P('  tasa Lr IS %.3f OOS %.3f (n deep IS %d OOS %d)' % (Lr[ev & np.isin(di, IS)].mean(), Lr[ev & np.isin(di, OOS)].mean(), (ev & np.isin(di, IS)).sum(), (ev & np.isin(di, OOS)).sum()))
for nmF, b in (('b', bB), ('a', bA)):
    for lv in (True, False): P('  oraculo [%s] Lr=%s: %s' % (nmF, lv, row(b[2], b[3] & (Lr == lv))))
Xf = np.c_[np.clip(dnE, -10, 0), p, np.log(A['cum']), np.log1p(A['k']), A['src'], np.clip(A['sp0'], 0, 20), A['bs0'], A['trem'], np.clip(A['dbb1'], -10, 10), np.log1p(A['dtc'])]
Xf = np.where(np.isfinite(Xf), Xf, np.nanmedian(Xf[ev], 0)); trI = ev & np.isin(di, IS)
mu, sd = Xf[trI].mean(0), Xf[trI].std(0) + 1e-9; Xs = (Xf - mu) / sd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
lr = LogisticRegression(C=1.0, max_iter=2000).fit(Xs[trI], Lr[trI]); sc = lr.decision_function(Xs)
au = []
for i in OOS:
    mm = ev & (di == i)
    if mm.sum() > 10 and 0 < Lr[mm].mean() < 1: au.append(roc_auc_score(Lr[mm], sc[mm]))
m_, lo_, hi_ = r4.tci(au); P('  AUC OOS por dias %.3f [%.3f,%.3f] (%d dias); coef: %s' % (m_, lo_, hi_, len(au), ' '.join('%s%+.2f' % (n, c) for n, c in zip(('dn', 'p', 'lcum', 'k', 'src', 'spr', 'lbs', 'trem', 'dbb1', 'ldtc'), lr.coef_[0]))))
thr = np.median(sc[trI])
for nmF, b in (('b', bB), ('a', bA)): P('  politica (c) [%s] score>=mediana IS: %s' % (nmF, row(b[2], b[3] & (sc >= thr))))
open(BASE + 'salida_r8L.txt', 'w').write('\n'.join(r6a.LINES))
