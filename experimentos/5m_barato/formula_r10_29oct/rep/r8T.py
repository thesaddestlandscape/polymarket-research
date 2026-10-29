import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
from r8lib import *
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
coin = sys.argv[1] if len(sys.argv) > 1 else 'BTC'; rng = np.random.default_rng(6290); Z = np.load(BASE + 'hz_%s.npz' % coin, allow_pickle=True)
days = list(Z['days']); nd = len(days); IS, OOS, DEV = part(days); OOS2 = OOS + DEV
F_ = Z['F'].astype(float); di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; fl = Z['fl']; tg = Z['tg']; tf = Z['tf']; COLS = list(Z['cols'])
isI = np.isin(di, IS); N = 10.0; FS = 48847.0 if coin == 'BTC' else 1.0
def prep(A): return np.hstack([np.where(np.isnan(A), 0.0, A), np.isnan(A[:, [COLS.index(c) for c in ('cbb', 'bid15', 'comp_acc5')]]).astype(float)])
yy = Z['Y10'].astype(int); sc_ = StandardScaler().fit(prep(F_[isI])); lr = LogisticRegression(max_iter=300, C=0.3).fit(sc_.transform(prep(F_[isI])), yy[isI])
score = lr.decision_function(sc_.transform(prep(F_))); q05, q95 = np.quantile(score[isI], [0.05, 0.95])
P('== R8-TREM [%s] logit Y10 AUC OOS %.3f; filas %d' % (coin, roc_auc_score(yy[np.isin(di, OOS)], score[np.isin(di, OOS)]), len(di)))
trem = F_[:, COLS.index('trem')]
def dedupe(sel):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
def RR(mi, kept):
    f = fl[:, mi] & kept; return dict(di=di, num=np.where(f, N * (y - tg[:, mi]), 0.0), den=np.where(f, N * tg[:, mi], 0.0)), f
def row(R, m, kept):
    o = []
    for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
        s = summ(R, m, ds, nd); nk = (kept & np.isin(di, ds)).sum()
        o.append('%s %s' % (pn, ('%+.3f [%+.3f,%+.3f] +%d/%d sin2 %+.3f %.0fE/d fill %.0f%%' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'], s['s2'], s['eurd'], 100 * s['nf'] / max(1, nk))) if s else '-'))
    return ' | '.join(o)
BANDS = [(15, 60), (60, 120), (120, 200), (200, 286)]; HZ = {'bajo': score <= q05, 'medio': (score > q05) & (score < q95), 'alto': score >= q95, 'todos': np.ones(len(di), bool)}
pols = []; V = []; P('-- familia 48 (T_rem x hazard x m), vida 10 s, relleno estricto')
for b in BANDS:
    inb = (trem >= b[0]) & (trem < b[1])
    for hn, hm in HZ.items():
        for mi in range(3):
            sel = inb & hm & np.isfinite(tg[:, mi]); kept = dedupe(sel); R, f = RR(mi, kept); s = summ(R, f, IS, nd)
            e, d_, _ = r6a.dayev(R, f, nd); V.append([e[i] if d_[i] > 0 else 0.0 for i in IS]); pols.append((b, hn, mi, kept, R, f, s['lo'] if s else -9))
            P('  T%3d-%3d %-5s m=%d %s' % (b[0], b[1], hn, mi + 1, row(R, f, kept)))
obs, mx = signflip_max(np.array(V)); j = int(np.argmax([p[6] for p in pols])); b, hn, mi, kept, R, f, lo = pols[j]
P('-> elegida IS: T%d-%d %s m=%d (cota inf %+.3f) p max %.3f' % (b[0], b[1], hn, mi + 1, lo, (mx >= obs[j]).mean()))
inb = (trem >= b[0]) & (trem < b[1]); base = inb & np.isfinite(tg[:, mi]); frac = (kept.sum() / max(1, dedupe(base).sum()))
ka = dedupe(base & (rng.random(len(di)) < kept.sum() / max(1, base.sum()) * 1.0)); Ra, fa = RR(mi, ka); P('   ALEATORIO misma banda: %s' % row(Ra, fa, ka))
for k, (lo_, hi_) in enumerate(((0.09, 0.15), (0.15, 0.22), (0.22, 0.2901))):
    mk = f & (tg[:, mi] >= lo_ - 1e-9) & (tg[:, mi] < hi_); P('   objetivo [%.2f,%.2f): %s' % (lo_, hi_, row(R, mk, kept & (tg[:, mi] >= lo_ - 1e-9) & (tg[:, mi] < hi_))))
so = summ(R, f, OOS, nd); P('   cuota OOS %.2f %%' % (100 * so['eurd'] / FS if so else 0))
P('-- auditoria INVERSION (hazard bajo <= q05, m=3, todas las T_rem)')
kI = dedupe(HZ['bajo'] & np.isfinite(tg[:, 2])); RI, fI = RR(2, kI); P('  reproduccion logit: %s' % row(RI, fI, kI))
for nm, c in (('trem', 'trem'), ('spr', 'spr'), ('acc60', 'acc60'), ('bb', 'bb'), ('tsl200', 'tsl200')):
    x = F_[:, COLS.index(c)]; P('  %-6s mediana bajo-relleno %.3f | bajo-todo %.3f | SIEMPRE-relleno %.3f' % (nm, np.nanmedian(x[fI]), np.nanmedian(x[kI]), np.nanmedian(x[fl[:, 2] & np.isfinite(tg[:, 2])])))
ttf = (tf[:, 2] - t) if tf.ndim == 2 else None
if ttf is not None: P('  ms hasta relleno (bajo) p10/p50/p90: %s' % ' '.join('%.0f' % v for v in np.nanpercentile(ttf[fI], [10, 50, 90])))
md = np.unique(np.c_[di[fI], u[fI]], axis=0); P('  rellenos %d en %d (dia,token) distintos; top dia aporta %.0f %% del pnl OOS+DEV' % (fI.sum(), len(md), 100 * np.max(np.bincount(di[fI & np.isin(di, OOS2)], weights=RI['num'][fI & np.isin(di, OOS2)], minlength=nd)) / max(1e-9, RI['num'][fI & np.isin(di, OOS2)].sum())))
for b in BANDS:
    m_ = fI & (trem >= b[0]) & (trem < b[1]); P('  bajo m=3 T%3d-%3d: %s' % (b[0], b[1], row(RI, m_, kI & (trem >= b[0]) & (trem < b[1]))))
open(BASE + 'salida_r8T_%s.txt' % coin, 'w').write('\n'.join(r6a.LINES))
