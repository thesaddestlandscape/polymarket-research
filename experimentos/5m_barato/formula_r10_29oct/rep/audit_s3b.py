#!/usr/bin/env python3
"""Auditoria QA hoja S3, parte b (29-Oct): rasgos del complementario recalculados CAUSALMENTE (L1 a T+L, sin depender de que el complementario imprima en el resto de la ventana) + k15 con ruta correcta. Solo lectura. Salida rep/salida_audit_s3b.txt"""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
from r8lib import *
import pickle, hashlib
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import GroupKFold
R10 = BASE; N = 10.0; OUTF = R10 + 'rep/salida_audit_s3b.txt'; L = []; K15 = E4 + 'formula_r7_28oct/k15/k_%s.npz'
def P(s): print(s, flush=True); L.append(s)
Z = np.load(R10 + 'hz_BTC.npz', allow_pickle=True); days = list(Z['days']); nd = len(days); IS, OOS, DEV = part(days); OO = OOS + DEV
di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; F_ = Z['F'].astype(float); COLS = list(Z['cols']); tg = Z['tg']; fl = Z['fl']; tf = Z['tf']; yy = Z['Y10'].astype(int)
col = lambda c: F_[:, COLS.index(c)]; trem = col('trem'); bb = col('bb'); cbb = col('cbb'); bid15 = col('bid15'); isI = np.isin(di, IS)
T = (trem >= 200) & (trem < 286); LEAF = T & (bid15 <= 0.51) & (cbb > 0.66) & (bb > 0.28); FEE = lambda p: 0.07 * p * (1 - p)
def daystat(pnl, cost, ds):
    dn = np.bincount(di, weights=pnl, minlength=nd); dd = np.bincount(di, weights=cost, minlength=nd); sel = [i for i in ds if dd[i] > 0]
    if len(sel) < 2: return '-'
    ev = dn[sel] / dd[sel]; m, lo, hi = r4.tci(ev); return 'EVw%+.3f [%+.2f,%+.2f] d%d +%d sin2%+.2f' % (dn[sel].sum() / dd[sel].sum(), lo, hi, len(sel), (ev > 0).sum(), np.sort(ev)[:-2].mean() if len(ev) > 3 else np.nan)
def first_per_tok(mask):
    ii = np.flatnonzero(mask); o = ii[np.lexsort((t[ii], u[ii], di[ii]))]; k = np.stack([di[o], u[o]], 1); _, f = np.unique(k, axis=0, return_index=True); out = np.zeros(len(mask), bool); out[o[f]] = True; return out
def dedupe(sel):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
def firstfill(f, m):
    ii = np.flatnonzero(f); o = ii[np.argsort(tf[ii, m], kind='stable')]; k = np.stack([di[o], u[o]], 1); _, first = np.unique(k, axis=0, return_index=True); out = np.zeros(len(f), bool); out[o[first]] = True; return out
B = T & (bb > 0.28)
P('== FUGA por ausencia: en hz, cbb/dcbb1/dcbb5/comp_acc5 = NaN cuando el complementario NO tiene prints en TODA la ventana (r10_build.py:23-24,50-55; D.stream sin corte temporal).')
for nm in ('cbb', 'comp_acc5'):
    v = col(nm); P('  T200-286 bb>0,28: %s NaN %.1f%% y|NaN %.4f n%d | y|finito %.3f n%d' % (nm, 100 * np.isnan(v[B]).mean(), y[B & np.isnan(v)].mean(), (B & np.isnan(v)).sum(), y[B & np.isfinite(v)].mean(), (B & np.isfinite(v)).sum()))
v = col('cbb'); A = np.isfinite(bb) & T; P('  todo T200-286 por banda bb: ' + ' | '.join('bb[%.2f,%.2f) NaN %.0f%% y|NaN %.3f y|fin %.3f' % (a, b_, 100 * np.isnan(v[A & (bb >= a) & (bb < b_)]).mean(), y[A & (bb >= a) & (bb < b_) & np.isnan(v)].mean(), y[A & (bb >= a) & (bb < b_) & np.isfinite(v)].mean()) for a, b_ in ((.10, .16), (.16, .22), (.22, .28), (.28, .36))))
R = np.flatnonzero(T & (bb >= 0.20)); LAGS = (-3000, -2000, -1000, 0, 1000)
FT = {Lg: {k: np.full(len(di), np.nan) for k in ('bb', 'cbb', 'bid15')} for Lg in LAGS}; ask215 = np.full(len(di), np.nan); npre = np.full(len(di), -1.0); ntot = np.full(len(di), -1.0)
for d_i, d in enumerate(days):
    w = R[di[R] == d_i]
    if not len(w): continue
    D = Day(d, 'BTC'); kz = np.load(K15 % d) if os.path.exists(K15 % d) else None
    if kz is not None: kmap = {(int(kz['kside'][i]), int(kz['kstart'][i])): i for i in range(len(kz['kstart']))}; klo = np.searchsorted(kz['qk'], np.arange(len(kz['kstart'])), 'left'); khi = np.searchsorted(kz['qk'], np.arange(len(kz['kstart'])), 'right')
    for uu in np.unique(u[w]):
        rr = w[u[w] == uu]; tt = t[rr]; c = int(D.comp[uu]); qq = None
        if kz is not None:
            i = kmap.get((int(D.side[uu]), int((float(D.cie[uu]) - 300.0) // 900 * 900 + 900)))
            if i is not None and khi[i] > klo[i]: qq = kz['qt'][klo[i]:khi[i]]; bq = kz['qbb'][klo[i]:khi[i]]
        for Lg in LAGS:
            FT[Lg]['bb'][rr] = D.l1(uu, tt + Lg)[0]
            if c >= 0: FT[Lg]['cbb'][rr] = D.l1(c, tt + Lg)[0]
            if qq is not None: j = np.searchsorted(qq, tt + Lg, 'right') - 1; FT[Lg]['bid15'][rr] = np.where(j >= 0, bq[np.clip(j, 0, None)], np.nan)
        ask215[rr] = D.l1(uu, tt + 215.0)[1]
        if c >= 0: sc = D.stream(c)[0]; ntot[rr] = len(sc); npre[rr] = np.searchsorted(sc, tt, 'right')
    del D
for k, ref in (('bb', bb), ('bid15', bid15)):
    a = FT[0][k][R]; P('reproduccion L=0 %s: iguales %.4f n%d' % (k, np.mean(np.isclose(a, ref[R], atol=1e-6) | (np.isnan(a) & np.isnan(ref[R]))), len(R)))
fin = np.isfinite(cbb[R]); P('reproduccion L=0 cbb donde hz finito: iguales %.4f n%d | hz NaN y L1 causal existe: %d' % (np.mean(np.isclose(FT[0]['cbb'][R][fin], cbb[R][fin], atol=1e-6)), fin.sum(), int((~fin & np.isfinite(FT[0]['cbb'][R])).sum())))
m = np.isnan(cbb) & (ntot >= 0); P('  hz cbb NaN <=> stream(comp) vacio en toda la ventana: %.4f (n%d); filas hz-finitas con 0 prints del comp ANTES de t: %d de %d, y=%.3f' % (np.mean(ntot[m] == 0), m.sum(), int((np.isfinite(cbb) & (npre == 0)).sum()), int((np.isfinite(cbb) & (npre >= 0)).sum()), y[np.isfinite(cbb) & (npre == 0)].mean()))
P('\n== (1) HOJA con rasgos CAUSALES en T+L (cbb = L1 del complementario, no NaN por futuro), regla ejecutable = hoja(L) & fila existente; TOMADOR ask T+215 ms, fee 0,07p(1-p), 1 por (dia,token)')
for Lg in LAGS:
    f = FT[Lg]
    with np.errstate(invalid='ignore'): lfL = T & (f['bid15'] <= 0.51) & (f['cbb'] > 0.66) & (f['bb'] > 0.28) & (f['bb'] <= 0.35) & np.isfinite(ask215)
    fs = first_per_tok(lfL); p = ask215; pnl = np.where(fs, N * (y - p - FEE(p)), 0.0); cost = np.where(fs, N * (p + FEE(p)), 0.0)
    P('  L=%+5d ms: filas %d tokens %d | y %.3f ask215 %.3f | IS %s || OOS %s' % (Lg, lfL.sum(), fs.sum(), y[fs].mean(), np.nanmean(p[fs]), daystat(pnl, cost, IS), daystat(pnl, cost, OO)))
with np.errstate(invalid='ignore'): CL = T & (FT[0]['bid15'] <= 0.51) & (FT[0]['cbb'] > 0.66) & (FT[0]['bb'] > 0.28)
P('  hoja causal L=0: %d filas vs hoja hz %d; y causal %.3f vs hz %.3f' % (CL.sum(), LEAF.sum(), y[CL].mean(), y[LEAF].mean()))
with np.errstate(invalid='ignore'): CLp = CL & (npre > 0)
P('  hoja causal & comp con >=1 print ANTES de t (indicador causal): filas %d y %.3f' % (CLp.sum(), y[CLp].mean()))
P('\n== (2) MAKER bb-m sobre hoja CAUSAL (relleno estricto print<objetivo, 10 s; sin rebate; 1 relleno/(dia,token))')
for mm in (0, 2):
    od = dedupe(CL & np.isfinite(tg[:, mm])); ff = firstfill(od & fl[:, mm], mm); nf = od & ~fl[:, mm]; pnl = np.where(ff, N * (y - tg[:, mm]), 0.0); cost = np.where(ff, N * tg[:, mm], 0.0)
    for ds, nmd in ((IS, 'IS'), (OO, 'OOS')):
        z = np.isin(di, ds); P('   bb-%dc %s: ordenes %d | rellenos %d y %.3f precio %.3f | no rellenadas %d y %.3f | %s' % (mm + 1, nmd, (od & z).sum(), (ff & z).sum(), y[ff & z].mean(), tg[ff & z, mm].mean(), (nf & z).sum(), y[nf & z].mean(), daystat(pnl, cost, ds)))
fs = first_per_tok(CL & np.isfinite(ask215)); p = ask215; P('   TOMADOR hoja causal L=0: IS %s || OOS %s' % (daystat(np.where(fs, N * (y - p - FEE(p)), 0.0), np.where(fs, N * (p + FEE(p)), 0.0), IS), daystat(np.where(fs, N * (y - p - FEE(p)), 0.0), np.where(fs, N * (p + FEE(p)), 0.0), OO)))
P('\n== (3) contaminacion del HGB congelado (sha 5e495915) por la ausencia de cbb/comp_acc5')
pk = open(R10 + 'frozen_R10_hgb_BTC.pkl', 'rb').read(); M = pickle.loads(pk); thr = M['thr']; P('sha %s' % hashlib.sha256(pk).hexdigest()[:8])
lg = lambda p: np.log(np.clip(p, 1e-6, 1 - 1e-6) / (1 - np.clip(p, 1e-6, 1 - 1e-6))).reshape(-1, 1)
hgb = lambda: HistGradientBoostingClassifier(max_iter=200, learning_rate=0.07, max_depth=5, min_samples_leaf=100, random_state=1)
idx = np.flatnonzero(isI); oof = np.zeros(len(idx))
for a, b in GroupKFold(5).split(idx, groups=di[idx]): oof[b] = hgb().fit(F_[idx[a]], yy[idx[a]]).predict_proba(F_[idx[b]])[:, 1]
score = np.full(len(di), np.nan); score[idx] = M['platt'].predict_proba(lg(oof))[:, 1]; score[~isI] = M['platt'].predict_proba(lg(M['hgb'].predict_proba(F_[~isI])[:, 1]))[:, 1]
low = score <= thr; v3 = np.isfinite(tg[:, 2]); TB = (trem >= 200) & (trem < 286)
for nm, sel in (('HGB-bajo todas T', v3 & low), ('HGB-bajo T200-286', v3 & low & TB), ('SIEMPRE T200-286', v3 & TB)):
    ff = firstfill(fl[:, 2] & dedupe(sel), 2); nn = np.isnan(cbb)
    P('  %-18s rellenos %d: cbb NaN %.1f%% (y %.3f) | cbb finito (y %.3f) | precio %.3f' % (nm, ff.sum(), 100 * nn[ff].mean(), y[ff & nn].mean() if (ff & nn).sum() else np.nan, y[ff & ~nn].mean(), tg[ff, 2].mean()))
    for ds, nmd in ((IS, 'IS'), (OO, 'OOS')): P('     %s todas %s | solo cbb NaN %s | solo cbb finito %s' % (nmd, daystat(np.where(ff, N * (y - tg[:, 2]), 0), np.where(ff, N * tg[:, 2], 0), ds), daystat(np.where(ff & nn, N * (y - tg[:, 2]), 0), np.where(ff & nn, N * tg[:, 2], 0), ds), daystat(np.where(ff & ~nn, N * (y - tg[:, 2]), 0), np.where(ff & ~nn, N * tg[:, 2], 0), ds)))
F2 = F_.copy()
for nm in ('cbb', 'dcbb1', 'dcbb5', 'comp_acc5'): F2[:, COLS.index(nm)] = np.nan
s2 = np.full(len(di), np.nan); s2[idx] = M['platt'].predict_proba(lg(M['hgb'].predict_proba(F2[idx])[:, 1]))[:, 1]; s2[~isI] = M['platt'].predict_proba(lg(M['hgb'].predict_proba(F2[~isI])[:, 1]))[:, 1]
for nm, sel in (('HGB congelado con cbb/dcbb/comp_acc5 = NaN para todos (sin fuga), umbral original', v3 & (s2 <= thr)), ('idem T200-286', v3 & (s2 <= thr) & TB)):
    ff = firstfill(fl[:, 2] & dedupe(sel), 2); P('  %s: rellenos %d | IS %s || OOS %s' % (nm, ff.sum(), daystat(np.where(ff, N * (y - tg[:, 2]), 0), np.where(ff, N * tg[:, 2], 0), IS), daystat(np.where(ff, N * (y - tg[:, 2]), 0), np.where(ff, N * tg[:, 2], 0), OO)))
open(OUTF, 'w').write('\n'.join(L))

keep = [i for i, c in enumerate(COLS) if c not in ('cbb', 'dcbb1', 'dcbb5', 'comp_acc5')]; Fk = F_[:, keep]; oof2 = np.zeros(len(idx))
for a, b in GroupKFold(5).split(idx, groups=di[idx]): oof2[b] = hgb().fit(Fk[idx[a]], yy[idx[a]]).predict_proba(Fk[idx[b]])[:, 1]
m2 = hgb().fit(Fk[idx], yy[idx]); s3 = np.full(len(di), np.nan); s3[idx] = oof2; s3[~isI] = m2.predict_proba(Fk[~isI])[:, 1]; th3 = float(np.quantile(oof2, 0.05))
for nm, sel in (('HGB REENTRENADO en IS SIN las 4 columnas con fuga, q05 OOF', v3 & (s3 <= th3)), ('idem T200-286', v3 & (s3 <= th3) & TB)):
    ff = firstfill(fl[:, 2] & dedupe(sel), 2); P('  %s: rellenos %d | IS(OOF) %s || OOS %s' % (nm, ff.sum(), daystat(np.where(ff, N * (y - tg[:, 2]), 0), np.where(ff, N * tg[:, 2], 0), IS), daystat(np.where(ff, N * (y - tg[:, 2]), 0), np.where(ff, N * tg[:, 2], 0), OO)))
open(OUTF, 'w').write('\n'.join(L))
