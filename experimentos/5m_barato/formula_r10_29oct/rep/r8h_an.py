#!/usr/bin/env python3
"""r8h_an: Bloque 2 (hazard M1, politica de cotizar, salidas) / Bloque 5 (ETH). Uso: r8h_an.py BTC|ETH. Manda PREREG_FORMULA_R8.md."""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
from r8lib import *
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, brier_score_loss
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler
coin = sys.argv[1]; rng = np.random.default_rng(6282); Z = np.load(BASE + 'hz_%s.npz' % coin, allow_pickle=True)
days = list(Z['days']); nd = len(days); IS, OOS, DEV = part(days); OOS2 = OOS + DEV
F_ = Z['F'].astype(float); di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; fl = Z['fl']; tg = Z['tg']; xb = Z['xb']; COLS = list(Z['cols'])
isI = np.isin(di, IS); isO = np.isin(di, OOS2); N = 10.0; FS = 48847.0 if coin == 'BTC' else 1.0
P('== R8 Bloque 2/5 [%s]: filas %d (IS %d, OOS+DEV %d); tasa base Y10(>=800 acc en 10 s) IS %.4f OOS %.4f' % (coin, len(di), isI.sum(), isO.sum(), Z['Y10'][isI].mean(), Z['Y10'][isO].mean()))
def prep(A): return np.hstack([np.where(np.isnan(A), 0.0, A), np.isnan(A[:, [COLS.index(c) for c in ('cbb', 'bid15', 'comp_acc5')]]).astype(float)])
def boot(yt, sc, dv):
    ud = np.unique(dv); out = []
    for _ in range(150):
        pk = rng.choice(ud, len(ud)); ix = np.concatenate([np.flatnonzero(dv == x) for x in pk])
        if len(np.unique(yt[ix])) == 2: out.append(roc_auc_score(yt[ix], sc[ix]))
    return np.percentile(out, [5, 95])
def hgb(): return HistGradientBoostingClassifier(max_iter=200, learning_rate=0.07, max_depth=5, min_samples_leaf=100, random_state=1)
SC = {}
for lab in ('Y10', 'Y5', 'Y4'):
    yy = Z[lab].astype(int)
    if len(np.unique(yy[isI])) < 2 or yy[isI].sum() < 50: P('  %s: muestra insuficiente (positivos IS %d)' % (lab, yy[isI].sum())); continue
    idx = np.flatnonzero(isI); oof = np.zeros(len(idx))
    for a, b in GroupKFold(5).split(idx, groups=di[idx]): oof[b] = hgb().fit(F_[idx[a]], yy[idx[a]]).predict_proba(F_[idx[b]])[:, 1]
    m = hgb().fit(F_[isI], yy[isI]); pO = m.predict_proba(F_[isO])[:, 1]
    sc = StandardScaler().fit(prep(F_[isI])); lr = LogisticRegression(max_iter=300, C=0.3).fit(sc.transform(prep(F_[isI])), yy[isI]); pL = lr.predict_proba(sc.transform(prep(F_[isO])))[:, 1]
    lg = lambda p: np.log(np.clip(p, 1e-6, 1 - 1e-6) / (1 - np.clip(p, 1e-6, 1 - 1e-6))).reshape(-1, 1)
    pl = LogisticRegression().fit(lg(oof), yy[isI]); cal = lambda p: pl.predict_proba(lg(p))[:, 1]
    cO = cal(pO); cI = cal(oof); base = yy[isI].mean(); yo = yy[isO]
    null = []
    for _ in range(40):
        ps = pO.copy()
        for x in np.unique(di[isO]): ix = np.flatnonzero(di[isO] == x); ps[ix] = rng.permutation(pO[ix])
        null.append(roc_auc_score(yo, ps))
    P('  %s: AUC OOS HGB %.3f [%.3f,%.3f] logit %.3f | nulo permutado %.3f | OOF IS %.3f | Brier OOS %.5f vs constante %.5f (skill %+.3f) | n pos OOS %d' % (lab, roc_auc_score(yo, pO), *boot(yo, pO, di[isO]), roc_auc_score(yo, pL), np.mean(null), roc_auc_score(yy[isI], oof), brier_score_loss(yo, cO), brier_score_loss(yo, np.full(len(yo), base)), 1 - brier_score_loss(yo, cO) / brier_score_loss(yo, np.full(len(yo), base)), yo.sum()))
    if lab == 'Y10':
        SC['oof'] = cI; SC['O'] = cO; q = np.quantile(cO, np.linspace(0, 1, 11)); dec = np.clip(np.searchsorted(q[1:-1], cO, 'right'), 0, 9)
        P('   calibracion OOS por deciles (pred media / observada): ' + ' '.join('%.3f/%.3f' % (cO[dec == k].mean(), yo[dec == k].mean()) for k in range(10)))
        top = cO >= np.quantile(cO, 0.99); P('   top 1 %% OOS: tasa observada %.3f frente a base %.3f (lift %.1fx)' % (yo[top].mean(), yo.mean(), yo[top].mean() / max(yo.mean(), 1e-9)))
        fi = np.argsort(-np.abs(np.corrcoef(np.vstack([F_[isO].T, cO]).__array__() if False else np.nan_to_num(np.vstack([F_[isO].T, cO]))))[-1][:-1])[:6]; P('   rasgos con mayor |corr| con el hazard OOS: ' + ', '.join('%s %+.2f' % (COLS[k], np.corrcoef(np.nan_to_num(F_[isO][:, k]), cO)[0, 1]) for k in fi))
if 'oof' not in SC: P('  hazard no entrenable'); sys.exit()
score = np.full(len(di), np.nan); score[np.flatnonzero(isI)] = SC['oof']; score[np.flatnonzero(isO)] = SC['O']
def dedupe(sel):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
def ev(mi, kept, ds):
    f = fl[:, mi] & kept; R = dict(di=di, num=np.where(f, N * (y - tg[:, mi]), 0.0), den=np.where(f, N * tg[:, mi], 0.0)); s = summ(R, f, ds, nd)
    return s, int((kept & np.isin(di, ds)).sum()), int((f & np.isin(di, ds)).sum()), R, f
def line(s, no, nf, ds): return ('ord/d %.0f fill %.1f %% | %s | cuota %.2f %%' % (no / len(ds), 100 * nf / max(1, no), F(s), 100 * (s['eurd'] / FS if s else 0))) if True else ''
valid = [np.isfinite(tg[:, mi]) for mi in range(3)]
P('\n-- Politicas hazard (cotizar a bb − m ticks si hazard >= umbral IS; N=10 acc; vida 10 s; llegada 73 ms; relleno estricto; 1 orden viva por token)')
pols = []; Vd = []
for qi, qq in enumerate((0.99, 0.98, 0.95)):
    thr = np.quantile(SC['oof'], qq)
    for mi in range(3):
        sel = (score >= thr) & valid[mi]; kept = dedupe(sel); s, no, nf, R, f = ev(mi, kept, IS); e, d_, _ = r6a.dayev(R, f, nd)
        Vd.append([e[i] if d_[i] > 0 else np.nan for i in IS]); pols.append((qq, mi + 1, thr, kept))
lo = np.array([r4.tci(np.array(v)[np.isfinite(v)])[1] if np.isfinite(v).sum() > 2 else -9 for v in Vd]); j = int(np.argmax(lo)); obs, nm = signflip_max(np.array(Vd)); pj = (nm >= obs[j]).mean()
for (qq, m, thr, kept), l_ in zip(pols, lo):
    for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
        s, no, nf, R, f = ev(m - 1, kept, ds); P('  q=%.2f m=%d %-3s %s' % (qq, m, pn, line(s, no, nf, ds)))
qq, m, thr, kept = pols[j]; mi = m - 1; P('  -> elegida (IS cota inf IC90 %+.3f): q=%.2f m=%d; p max-stat (9 politicas) %.3f' % (lo[j], qq, m, pj))
P('-- comparadores de la elegida (misma m; IS / OOS / DEV)')
sel0 = (score >= thr) & valid[mi]; fr = {pn: sel0[np.isin(di, ds)].sum() / max(1, valid[mi][np.isin(di, ds)].sum()) for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV))}
frow = np.array([fr['IS'] if x in IS else (fr['OOS'] if x in OOS else fr['DEV']) for x in range(nd)])[di]
comps = {'SIEMPRE': valid[mi], 'ALEATORIO': valid[mi] & (rng.random(len(di)) < frow), 'INVERSION (hazard bajo)': valid[mi] & (score <= np.quantile(score[isI], 1 - qq)), 'ORACULO (barrido real <=10 s)': valid[mi] & Z['Y10'].astype(bool)}
for nm_, cm in comps.items():
    kk = dedupe(cm)
    for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
        s, no, nf, R, f = ev(mi, kk, ds); P('  %-30s %-3s %s' % (nm_, pn, line(s, no, nf, ds)))
P('-- desagregado de la elegida en OOS+DEV por bucket de precio del objetivo')
for lb, lo_, hi_ in (('[.09,.15)', 0.09, 0.15), ('[.15,.22)', 0.15, 0.22), ('[.22,.29]', 0.22, 0.2901)):
    mk_ = kept & (tg[:, mi] >= lo_ - 1e-9) & (tg[:, mi] < hi_); s, no, nf, R, f = ev(mi, mk_, OOS2); P('  objetivo %s: %s' % (lb, line(s, no, nf, OOS2)))
P('-- salidas tras el relleno (OOS+DEV): mantener frente a vender al bid L1 a tf+215 ms+Δ (comision tomadora 0,07 p(1-p)); cota oraculo = max(mantener, vender)')
s, no, nf, R, f = ev(mi, kept, OOS2); ff = f & np.isin(di, OOS2); hold = N * (y - tg[:, mi]); cost = N * tg[:, mi]
P('  mantener: EV/E %+.3f pnl %+.1f EUR (n=%d)' % (hold[ff].sum() / cost[ff].sum(), hold[ff].sum(), ff.sum()))
for k, dl in enumerate((0, 1, 3)):
    b = xb[:, mi, k]; okx = ff & np.isfinite(b); ex = N * ((b - tg[:, mi]) - 0.07 * b * (1 - b)); pol = np.where(okx, ex, hold)
    orc = np.where(okx, np.maximum(ex, hold), hold)
    P('  vender Δ=%ds: con bid disponible %.0f %%; EV/E vender-siempre %+.3f (pnl %+.1f) | cota oraculo pnl %+.1f (ahorro maximo %+.1f EUR)' % (dl, 100 * okx.sum() / max(1, ff.sum()), pol[ff].sum() / cost[ff].sum(), pol[ff].sum(), orc[ff].sum(), orc[ff].sum() - hold[ff].sum()))
open(BASE + 'salida_r8h_%s.txt' % coin, 'w').write('\n'.join(r6a.LINES))
