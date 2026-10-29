#!/usr/bin/env python3
"""Auditoria QA hoja S3 (29-Oct, solo lectura de hz_BTC.npz, b_*.npz, k15, cache desenlaces, frozen sha 5e495915). Salida rep/salida_audit_s3.txt"""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
from r8lib import *
import pickle, hashlib
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import GroupKFold
R10 = BASE; N = 10.0; OUTF = R10 + 'rep/salida_audit_s3.txt'; L = []
def P(s): print(s, flush=True); L.append(s)
Z = np.load(R10 + 'hz_BTC.npz', allow_pickle=True); days = list(Z['days']); nd = len(days); IS, OOS, DEV = part(days); OO = OOS + DEV
di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; F_ = Z['F'].astype(float); COLS = list(Z['cols']); tg = Z['tg']; fl = Z['fl']; tf = Z['tf']; yy = Z['Y10'].astype(int)
col = lambda c: F_[:, COLS.index(c)]; trem = col('trem'); bb = col('bb'); cbb = col('cbb'); bid15 = col('bid15'); isI = np.isin(di, IS)
T = (trem >= 200) & (trem < 286); LEAF = T & (bid15 <= 0.51) & (cbb > 0.66) & (bb > 0.28)
G = json.load(open(r4.I.CACHE)); P('filas hz %d | T200-286 %d | LEAF %d' % (len(di), T.sum(), LEAF.sum()))
FEE = lambda p: 0.07 * p * (1 - p)
def daystat(pnl, cost, ds):
    dn = np.bincount(di, weights=pnl, minlength=nd); dd = np.bincount(di, weights=cost, minlength=nd); sel = [i for i in ds if dd[i] > 0]
    if len(sel) < 2: return '-'
    ev = dn[sel] / dd[sel]; m, lo, hi = r4.tci(ev); return 'EVw%+.3f [%+.2f,%+.2f] d%d +%d sin2%+.2f' % (dn[sel].sum() / dd[sel].sum(), lo, hi, len(sel), (ev > 0).sum(), np.sort(ev)[:-2].mean() if len(ev) > 3 else np.nan)
def first_per_tok(mask):
    ii = np.flatnonzero(mask); o = ii[np.lexsort((t[ii], u[ii], di[ii]))]; k = np.stack([di[o], u[o]], 1); _, f = np.unique(k, axis=0, return_index=True); out = np.zeros(len(mask), bool); out[o[f]] = True; return out
# ---------- (1) recalculo de rasgos a T+L y precios ejecutables
R = np.flatnonzero(T & (bb >= 0.20)); LAGS = (-3000, -2000, -1000, 0, 1000, 2000)
FT = {Lg: {k: np.full(len(di), np.nan) for k in ('bb', 'cbb', 'bid15')} for Lg in LAGS}
ask215 = np.full(len(di), np.nan); bbF = np.full(len(di), np.nan); yc = np.full(len(di), np.nan); pos = np.full(len(di), -1); bid15F = np.full(len(di), np.nan)
for d_i, d in enumerate(days):
    w = R[di[R] == d_i]
    if not len(w): continue
    D = Day(d, 'BTC'); f15 = BASE.replace('formula_r8_28oct', 'formula_r7_28oct') + 'k15/k_%s.npz' % d; kz = np.load(f15) if os.path.exists(f15) else None
    if kz is not None:
        kmap = {(int(kz['kside'][i]), int(kz['kstart'][i])): i for i in range(len(kz['kstart']))}; klo = np.searchsorted(kz['qk'], np.arange(len(kz['kstart'])), 'left'); khi = np.searchsorted(kz['qk'], np.arange(len(kz['kstart'])), 'right')
    for uu in np.unique(u[w]):
        rr = w[u[w] == uu]; tt = t[rr]; c = int(D.comp[uu]); c0 = float(D.cie[uu]) * 1000.0
        qq = bq = None
        if kz is not None:
            i = kmap.get((int(D.side[uu]), int((float(D.cie[uu]) - 300.0) // 900 * 900 + 900)))
            if i is not None and khi[i] > klo[i]: qq = kz['qt'][klo[i]:khi[i]]; bq = kz['qbb'][klo[i]:khi[i]]
        for Lg in LAGS:
            FT[Lg]['bb'][rr] = D.l1(uu, tt + Lg)[0]
            if c >= 0: FT[Lg]['cbb'][rr] = D.l1(c, tt + Lg)[0]
            if qq is not None: j = np.searchsorted(qq, tt + Lg, 'right') - 1; FT[Lg]['bid15'][rr] = np.where(j >= 0, bq[np.clip(j, 0, None)], np.nan)
        ask215[rr] = D.l1(uu, tt + 215.0)[1]; bbF[rr] = D.l1(uu, [c0 - 1500.0])[0][0]; pos[rr] = int(float(D.cie[uu]) % 900) // 300
        if c >= 0: win = G.get(str(D.mks[c])); yc[rr] = 1.0 if win == ('YES' if D.side[c] == 0 else 'NO') else 0.0
        if qq is not None and pos[rr[0]] == 0: j = np.searchsorted(qq, c0 - 1500.0, 'right') - 1; bid15F[rr] = bq[j] if j >= 0 else np.nan
    del D
for k, ref in (('bb', bb), ('cbb', cbb), ('bid15', bid15)):
    a = FT[0][k][R]; b = ref[R]; P('reproduccion L=0 %s: iguales %.4f (n %d, ambos nan %d)' % (k, np.mean(np.isclose(a, b, atol=1e-6) | (np.isnan(a) & np.isnan(b))), len(R), int((np.isnan(a) & np.isnan(b)).sum())))
lf = LEAF & np.isfinite(yc); P('ETIQUETAS en LEAF: y+y(compl)==1 %.4f n%d | libro final bb(u,c0-1,5s)>0,5 coincide con y %.4f n%d | fuera de LEAF (T200-286 bb>=0,20) coincide %.4f' % (np.mean(y[lf] + yc[lf] == 1), lf.sum(), np.mean((bbF[LEAF & np.isfinite(bbF)] > 0.5) == (y[LEAF & np.isfinite(bbF)] == 1)), (LEAF & np.isfinite(bbF)).sum(), np.mean((bbF[R][np.isfinite(bbF[R])] > 0.5) == (y[R][np.isfinite(bbF[R])] == 1))))
P('LEAF por posicion del 5m en el 15m (0 = ultimo 5m, cierra con el 15m): ' + ' | '.join('pos%d n%d y%.3f bb%.3f bid15 med %.2f' % (p_, (LEAF & (pos == p_)).sum(), y[LEAF & (pos == p_)].mean(), bb[LEAF & (pos == p_)].mean(), np.nanmedian(bid15[LEAF & (pos == p_)])) for p_ in (0, 1, 2) if (LEAF & (pos == p_)).sum()))
m0 = LEAF & (pos == 0) & np.isfinite(bid15F); P('  pos0: bid15 final del 15m (c0-1,5 s) >0,5 coincide con y del 5m %.3f n%d (5m y 15m del mismo lado cierran juntos)' % (np.mean((bid15F[m0] > 0.5) == (y[m0] == 1)), m0.sum()))
P('calibracion T200-286 (todas las filas hz, por bb): ' + ' | '.join('bb[%.2f,%.2f) y%.3f n%d' % (a, b_, y[T & (bb >= a) & (bb < b_)].mean(), (T & (bb >= a) & (bb < b_)).sum()) for a, b_ in ((.10, .16), (.16, .22), (.22, .28), (.28, .32), (.32, .36))))
B = T & (bb > 0.28)
P('bb in (0,28-0,35], T200-286, y por bid15: ' + ' | '.join('bid15[%.2f,%.2f) y%.3f n%d' % (a, b_, y[B & (bid15 >= a) & (bid15 < b_)].mean(), (B & (bid15 >= a) & (bid15 < b_)).sum()) for a, b_ in ((0, .2), (.2, .37), (.37, .51), (.51, .7), (.7, 1.01))) + ' | bid15 NaN y%.3f n%d' % (y[B & np.isnan(bid15)].mean(), (B & np.isnan(bid15)).sum()))
P('\n== (1) RASGOS RETRASADOS/ADELANTADOS: hoja con bb,cbb,bid15 tomados en T+L; regla ejecutable = hoja(L) y fila existente (bb actual en [0,10,0,35]); TOMADOR al ask de T+215 ms, fee 0,07p(1-p), 1 por (dia,token) la mas temprana')
for Lg in LAGS:
    f = FT[Lg]; with_ = np.errstate(invalid='ignore'); 
    with np.errstate(invalid='ignore'): lfL = T & (f['bid15'] <= 0.51) & (f['cbb'] > 0.66) & (f['bb'] > 0.28) & (f['bb'] <= 0.35) & np.isfinite(ask215)
    fs = first_per_tok(lfL); p = ask215; pnl = np.where(fs, N * (y - p - FEE(p)), 0.0); cost = np.where(fs, N * (p + FEE(p)), 0.0)
    P('  L=%+5d ms: filas %d tokens %d | y %.3f ask215 medio %.3f bb_actual %.3f | IS %s || OOS %s' % (Lg, lfL.sum(), fs.sum(), y[fs].mean(), np.nanmean(p[fs]), bb[fs].mean(), daystat(pnl, cost, IS), daystat(pnl, cost, OO)))
P('  (L<0 = informacion vieja; si la hoja fuese look-ahead de ms deberia desvanecerse con L=-1..-3 s)')
# ---------- (2) tomador y maker bb-1c estricto sobre la hoja original
P('\n== (2) REGLA EJECUTABLE sobre LEAF original')
for nm, msk in (('LEAF', LEAF), ('control T200-286 bb>0,28 bid15>0,51', T & (bb > 0.28) & (bid15 > 0.51)), ('control T200-286 bb>0,28 todo', T & (bb > 0.28))):
    fs = first_per_tok(msk & np.isfinite(ask215)); p = ask215; pnl = np.where(fs, N * (y - p - FEE(p)), 0.0); cost = np.where(fs, N * (p + FEE(p)), 0.0)
    P('  TOMADOR t0+215ms %-38s tokens %d y %.3f ask %.3f | IS %s || OOS %s' % (nm, fs.sum(), y[fs].mean(), np.nanmean(p[fs]), daystat(pnl, cost, IS), daystat(pnl, cost, OO)))
def dedupe(sel):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
def firstfill(f, m):
    ii = np.flatnonzero(f); o = ii[np.argsort(tf[ii, m], kind='stable')]; k = np.stack([di[o], u[o]], 1); _, first = np.unique(k, axis=0, return_index=True); out = np.zeros(len(f), bool); out[o[first]] = True; return out
P('  MAKER bb-m (relleno estricto: print < objetivo en 10 s tras alta 73+26 ms; sin rebate; 1 relleno por (dia,token)). Tasa de acierto con/sin relleno vs precio:')
for m in (0, 2):
    od = dedupe(LEAF & np.isfinite(tg[:, m])); ff = firstfill(od & fl[:, m], m); nf = od & ~fl[:, m]
    pnl = np.where(ff, N * (y - tg[:, m]), 0.0); cost = np.where(ff, N * tg[:, m], 0.0)
    for ds, nmds in ((IS, 'IS'), (OO, 'OOS')):
        z = np.isin(di, ds); P('   bb-%dc %s: ordenes %d | rellenadas(1/tok) %d y %.3f precio %.3f | NO rellenadas %d y %.3f precio %.3f (ask215 %.3f) | %s' % (m + 1, nmds, (od & z).sum(), (ff & z).sum(), y[ff & z].mean(), tg[ff & z, m].mean(), (nf & z).sum(), y[nf & z].mean(), tg[nf & z, m].mean(), np.nanmean(ask215[nf & z]), daystat(pnl, cost, ds)))
# ---------- (4) multiplicidad tabla fina
P('\n== (4) MULTIPLICIDAD tabla fina (72 celdas + uniones HGB T220-286/T200-286). Volteo de signos por DIAS (mismo signo para todas las celdas en cada permutacion, B=20000), estadistico t de EV diario; p max-T (FWER) y BH-FDR q<0,10 sobre p crudo.')
pk = open(R10 + 'frozen_R10_hgb_BTC.pkl', 'rb').read(); P('sha modelo %s' % hashlib.sha256(pk).hexdigest()[:8]); M = pickle.loads(pk); thr = M['thr']
lg = lambda p: np.log(np.clip(p, 1e-6, 1 - 1e-6) / (1 - np.clip(p, 1e-6, 1 - 1e-6))).reshape(-1, 1)
hgb = lambda: HistGradientBoostingClassifier(max_iter=200, learning_rate=0.07, max_depth=5, min_samples_leaf=100, random_state=1)
idx = np.flatnonzero(isI); oof = np.zeros(len(idx))
for a, b in GroupKFold(5).split(idx, groups=di[idx]): oof[b] = hgb().fit(F_[idx[a]], yy[idx[a]]).predict_proba(F_[idx[b]])[:, 1]
score = np.full(len(di), np.nan); score[idx] = M['platt'].predict_proba(lg(oof))[:, 1]; score[~isI] = M['platt'].predict_proba(lg(M['hgb'].predict_proba(F_[~isI])[:, 1]))[:, 1]
assert abs(float(np.quantile(score[isI], 0.05)) - thr) < 1e-4; low = score <= thr; v3 = np.isfinite(tg[:, 2])
def cellf(lo, hi, pl, ph, mod):
    sel = v3 & (trem >= lo) & (trem < hi) & (tg[:, 2] >= pl - 1e-9) & (tg[:, 2] < ph)
    if mod: sel = sel & low
    return firstfill(fl[:, 2] & dedupe(sel), 2)
def dayev(f):
    dn = np.bincount(di, weights=np.where(f, N * (y - tg[:, 2]), 0.0), minlength=nd); dd = np.bincount(di, weights=np.where(f, N * tg[:, 2], 0.0), minlength=nd)
    with np.errstate(invalid='ignore', divide='ignore'): return np.where(dd > 0, dn / dd, np.nan), dn, dd
CELLS = []
for pop in ('HGB', 'SIN'):
    for lo in range(120, 300, 20):
        for pl, ph in ((0.09, 0.2901), (0.09, 0.15), (0.15, 0.22), (0.22, 0.2901)): CELLS.append((pop, lo, lo + 20, pl, ph))
CELLS += [('HGB', 220, 286, 0.09, 0.2901), ('HGB', 200, 286, 0.09, 0.2901)]
EV = {}; EVS = {}
for cdef in CELLS:
    pop, lo, hi, pl, ph = cdef; EV[cdef] = dayev(cellf(lo, hi, pl, ph, pop == 'HGB'))
    if pop == 'HGB': EVS[cdef] = dayev(cellf(lo, hi, pl, ph, False))
rng = np.random.default_rng(2910); Bp = 20000
def family(vecs, ds, label):
    S = rng.choice([-1.0, 1.0], size=(Bp, len(ds))); tobs = []; tstar = []; keys = []
    for k, e in vecs.items():
        e = e[ds]; ok = np.isfinite(e)
        if ok.sum() < 4 or np.nanstd(e[ok]) == 0: continue
        x = e[ok]; n = len(x); t0_ = x.mean() / (x.std(ddof=1) / np.sqrt(n)); X = S[:, ok] * x; ts = X.mean(1) / (X.std(1, ddof=1) / np.sqrt(n)); keys.append(k); tobs.append(t0_); tstar.append(ts)
    tobs = np.array(tobs); tstar = np.array(tstar); mx = np.nanmax(tstar, 0)
    praw = (1 + (tstar >= tobs[:, None]).sum(1)) / (Bp + 1); padj = (1 + (mx[None, :] >= tobs[:, None]).sum(1)) / (Bp + 1)
    o = np.argsort(praw); m_ = len(praw); bh = np.zeros(m_, bool); thr_ = [praw[o[i]] <= 0.10 * (i + 1) / m_ for i in range(m_)]
    kmax = max([i for i in range(m_) if thr_[i]], default=-1); bh[o[:kmax + 1]] = True
    P('-- %s: %d tests; sobreviven max-T p<0,05: %d; BH-FDR q<0,10: %d' % (label, m_, (padj < 0.05).sum(), bh.sum()))
    for i in np.argsort(-tobs)[:12]:
        k = keys[i]; P('   %s T%d-%d p[%.2f,%.2f) t%+.2f p_crudo %.4f p_maxT %.4f BH %s' % (k[0], k[1], k[2], k[3], k[4], tobs[i], praw[i], padj[i], 'SI' if bh[i] else 'no'))
    return dict(zip(keys, zip(praw, padj, bh)))
fO = family({k: v[0] for k, v in EV.items()}, OO, 'EV>0 OOS 16-27 (12 d), 74 tests')
fI = family({k: v[0] for k, v in EV.items()}, IS, 'EV>0 IS 06-15 (10 d), 74 tests')
fD = family({k: EV[k][0] - EVS[k][0] for k in EVS}, OO, 'dEV HGB - SIN misma celda OOS 16-27, 38 tests')
P('Celdas pedidas (OOS EV>0 / OOS dEV vs SIN): ')
for k in (('HGB', 220, 240, .09, .2901), ('HGB', 240, 260, .09, .2901), ('HGB', 280, 300, .09, .2901), ('HGB', 220, 286, .09, .2901), ('HGB', 200, 286, .09, .2901)):
    a = fO.get(k); b = fD.get(k); P('   %s T%d-%d: EV p_crudo %s p_maxT %s BH %s | dEV p_crudo %s p_maxT %s BH %s' % (k[0], k[1], k[2], *(('%.4f' % a[0], '%.4f' % a[1], a[2]) if a else ('-',) * 3), *(('%.4f' % b[0], '%.4f' % b[1], b[2]) if b else ('-',) * 3)))
open(OUTF, 'w').write('\n'.join(L))
