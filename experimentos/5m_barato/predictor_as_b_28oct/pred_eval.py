#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pred_eval.py - evaluacion segun PREREG_PREDICTOR.md. IS 05-22 / OOS 23-26 (una mirada). PRED_SMOKE=1 -> prueba de humo."""
import os, sys, glob, json, gzip, csv, time, traceback
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier as HGB
from sklearn.metrics import roc_auc_score
BASE = '/root/polymarket-research/experimentos/5m_barato/predictor_as_b_28oct/'
UN = '/root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct/units/'
SMOKE = bool(os.environ.get('PRED_SMOKE'))
OOSD = {'2026-10-23', '2026-10-24', '2026-10-25', '2026-10-26'}
PES = (0.015, 0.046)
B_EV = 50 if SMOKE else 1000; B_AUC = 30 if SMOKE else 300; R_PL = 50 if SMOKE else 500; IT = 20 if SMOKE else 200
SEED = 2711; t00 = time.time()
G = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
def log(*a): print(*a, flush=True)

days = sorted(os.path.basename(p)[2:12] for p in glob.glob(BASE + 'out/p_2026-10-*.npz') if '.tmp' not in p)
if SMOKE: days = [d for d in days if d not in OOSD]   # humo: NUNCA toca los dias OOS
oos_days = {days[-1]} if SMOKE else set(OOSD)
log('dias', len(days), days[0], days[-1], '| OOS =', sorted(oos_days & set(days)), '| IS =', sorted(set(days) - oos_days), '| SMOKE' if SMOKE else '')
Lz = {k: [] for k in ('fm', 'ff', 'fk', 'sm', 'sf', 'sx', 'sk')}; dfy = []; dsy = []
for d in days:
    z = np.load(BASE + 'out/p_%s.npz' % d)
    for k in Lz: Lz[k].append(z[k])
    dfy += [d] * len(z['fm']); dsy += [d] * len(z['sm'])
    fn = [str(x) for x in z['fn']]; offs = [int(x) for x in z['offs']]
fm, ff, fk, sm_, sf, sx, sk = [np.concatenate(Lz[k]) for k in ('fm', 'ff', 'fk', 'sm', 'sf', 'sx', 'sk')]
dfy = np.array(dfy); dsy = np.array(dsy); NF = len(fn); NO = len(offs)
UNIT = {}
for d in days:
    with gzip.open(UN + 'u_%s.csv.gz' % d, 'rt') as f:
        for r in csv.DictReader(f):
            if r['P_t1'] in ('', 'None'): continue
            UNIT[(r['mercado'], r['lado'])] = (float(r['P_sh']), float(r['P_cost']))
nF0 = len(fm); sh = np.full(nF0, np.nan); co = np.full(nF0, np.nan); g = np.full(nF0, np.nan)
for i in range(nF0):
    u = UNIT.get((fk[i, 1], fk[i, 3]))
    if u: sh[i], co[i] = u
    w = G.get(str(fk[i, 1]))
    if w in ('YES', 'NO'): g[i] = 1.0 if w == fk[i, 3] else 0.0
tf_map = {fk[i, 0]: fm[i, 0] for i in range(nF0)}
V = (co > 0) & ~np.isnan(g)
log('fills', nF0, 'validos (coste>0 y desenlace)', int(V.sum()), 'sin desenlace', int((np.isnan(g)).sum()), 'snaps', len(sm_))
fm, ff, fk, dfy, sh, co, g = fm[V], ff[V], fk[V], dfy[V], sh[V], co[V], g[V]
pn = sh * g - co; cl = fm[:, 7].astype(np.int64); oo = np.array([d in oos_days for d in dfy]); iss = ~oo
win = g

def boot_ev(p, c, k, B):
    u, inv = np.unique(k, return_inverse=True)
    sp = np.bincount(inv, weights=p, minlength=len(u)); sc = np.bincount(inv, weights=c, minlength=len(u))
    rng = np.random.default_rng(SEED); out = np.empty(B)
    for b in range(B):
        ix = rng.integers(0, len(u), len(u)); out[b] = sp[ix].sum() / max(sc[ix].sum(), 1e-12)
    return np.percentile(out, [5, 95])

def evs(m, B=None):
    B = B or B_EV
    if m.sum() < 5: return None
    p, c, k, dy = pn[m], co[m], cl[m], dfy[m]
    ev = p.sum() / c.sum(); lo, hi = boot_ev(p, c, k, B)
    ds = {d: (p[dy == d].sum(), c[dy == d].sum()) for d in np.unique(dy)}
    top = sorted(ds, key=lambda d: -ds[d][0])[:2]
    rp = sum(v[0] for d, v in ds.items() if d not in top); rc = sum(v[1] for d, v in ds.items() if d not in top)
    return dict(n=int(m.sum()), ev=ev, lo=lo, hi=hi, dpos=sum(1 for v in ds.values() if v[0] > 0), nd=len(ds),
                ev2=(rp / rc if rc > 0 else np.nan), co=c.sum())
def fs(r, pes=0.0):
    if r is None: return 'n<5'
    return 'n=%d EVw=%+.4f IC90c(%+.3f,%+.3f) dias+ %d/%d sin2mejores %+.4f coste %.0f' % (r['n'], r['ev'] - pes, r['lo'] - pes, r['hi'] - pes, r['dpos'], r['nd'], r['ev2'] - pes, r['co'])

def AUC(y, x):
    m = ~np.isnan(x)
    if m.sum() < 200 or len(np.unique(y[m])) < 2: return np.nan
    return roc_auc_score(y[m], x[m])

def boot_auc(y, p1, p0, k, B):
    u, inv = np.unique(k, return_inverse=True)
    order = np.argsort(inv, kind='stable'); st = np.searchsorted(inv[order], np.arange(len(u) + 1))
    rows = [order[st[i]:st[i + 1]] for i in range(len(u))]
    rng = np.random.default_rng(SEED); a1 = []; dd = []
    for _ in range(B):
        ix = np.concatenate([rows[i] for i in rng.integers(0, len(u), len(u))]); yy = y[ix]
        if yy.min() == yy.max(): continue
        x1 = roc_auc_score(yy, p1[ix]); x0 = roc_auc_score(yy, p0[ix]); a1.append(x1); dd.append(x1 - x0)
    return np.percentile(a1, [5, 95]), np.percentile(dd, [5, 95])

def sec(name, f):
    log('\n=====', name, '(t=%ds)' % (time.time() - t00))
    try: f()
    except Exception: log('ERROR en', name); traceback.print_exc(file=sys.stdout)

R = {}
def s_hold():
    log('HOLD IS ', fs(evs(iss))); log('HOLD OOS', fs(evs(oo)))
    log('referencia R1 alpha miner (SALIDA_DINAMICA): IS +0.0004 n=25427, OOS -0.0318 n=5711')
    sw = fm[:, 5]
    log('barrido (print estrictamente a traves del nivel): IS %.3f OOS %.3f de los rellenos' % (np.nanmean(sw[iss]), np.nanmean(sw[oo])))
    log('TECHO ORACULO (quitar barridos) IS ', fs(evs(iss & (sw == 0))), '\n                         OOS', fs(evs(oo & (sw == 0))))
    log('solo barridos                  IS ', fs(evs(iss & (sw == 1))), '\n                         OOS', fs(evs(oo & (sw == 1))))
sec('HOLD y techo oraculo', s_hold)

def s_uni():
    rows = []
    for j, name in enumerate(fn):
        if name == 'te_age': continue
        a = {o: (AUC(win[iss], ff[iss, oi, j]), AUC(win[oo], ff[oo, oi, j])) for oi, o in enumerate(offs) if o in (100, 300, 1000, 2000)}
        rows.append((name, a, 1.0 - np.isnan(ff[iss, 0, j]).mean()))
    rows = [r for r in rows if not np.isnan(r[1][100][0])]
    rows.sort(key=lambda r: -abs(r[1][100][0] - 0.5))
    log('AUC univariante de GANAR (>0,5: mayor valor -> mas gana). Orden por |AUC_IS@100ms-0,5|; cobertura no-NaN IS')
    log('%-14s %6s | IS@100  OOS@100 OOS@300 OOS@1000 OOS@2000' % ('rasgo', 'cobert'))
    for name, a, cv in rows[:16]:
        log('%-14s %6.2f | %.3f   %.3f   %.3f   %.3f    %.3f' % (name, cv, a[100][0], a[100][1], a[300][1], a[1000][1], a[2000][1]))
sec('Univariante (rasgos y lead)', s_uni)

def _ok(j):
    if fn[j] == 'te_age': return False
    a = ff[:, 0, j]; a = a[~np.isnan(a)]; b = sf[::10, j]; b = b[~np.isnan(b)]
    return len(np.unique(a)) >= 2 and len(np.unique(b)) >= 2
okc = {j for j in range(NF) if _ok(j)}
log('rasgos sin variacion (excluidos del modelo):', [fn[j] for j in range(NF) if j not in okc])
def fc(names): return [fn.index(k) for k in names if fn.index(k) in okc]
ST = fc(['T', 'coin', 'side', 'hour', 'lvl'])
FAM = {'PM_propio': ST + fc(['bb', 'ba', 'bs', 'as', 'spr', 'mid', 'dist', 'st_age', 'dbb300', 'dba300', 'dmid300', 'dbb1000', 'dba1000', 'dmid1000', 'nupd1000', 'nbbchg1000', 'nbachg1000', 'das1000', 'dbs1000', 'bb_age', 'ba_age', 'te_age']),
       'espejo_comp': ST + fc(['cbb', 'cba', 'cbs', 'cas', 'gap_bb', 'gap_ba', 'dcmid300', 'dcmid1000', 'cst_age']),
       'prints': ST + fc(['npr1000', 'bear1000', 'bull1000', 'imb1000', 'lastpr_age']),
       'Binance': ST + fc(['r300', 'r1000', 'r3000', 'rabs1000', 'bn_n1000', 'bn_imb1000', 'bn_age', 'v60'])}
ALL = [j for j in range(NF) if j in okc]; OFF_TR = [i for i, o in enumerate(offs) if o <= 1100]
def mkm(): return HGB(max_depth=3, learning_rate=0.05, max_iter=IT, l2_regularization=1.0, min_samples_leaf=300, random_state=SEED, early_stopping=False)
def train(cols, idx):
    X = ff[idx][:, OFF_TR, :][:, :, cols].reshape(-1, len(cols)); y = np.repeat(win[idx], len(OFF_TR))
    return mkm().fit(X, y)
def pred(m, cols, idx):
    return m.predict_proba(ff[idx][:, :, cols].reshape(-1, len(cols)))[:, 1].reshape(len(idx), NO)
idx_is = np.where(iss)[0]; idx_oo = np.where(oo)[0]
M = {}
def s_q1():
    mo1 = train(ALL, idx_is); mo0 = train(ST, idx_is)
    P1 = pred(mo1, ALL, idx_oo); P0 = pred(mo0, ST, idx_oo); M['P1'] = P1; M['P0'] = P0; M['mo1'] = mo1; M['mo0'] = mo0
    y = win[idx_oo]; k = cl[idx_oo]
    log('Q1: AUC OOS (gana) M1 (todos los rasgos) vs M0 (T, moneda, lado, hora, nivel); n_OOS=%d, ganadores=%d' % (len(y), int(y.sum())))
    for oi, o in enumerate(offs):
        if o not in (100, 200, 300, 600, 1000, 2000): continue
        a1 = roc_auc_score(y, P1[:, oi]); a0 = roc_auc_score(y, P0[:, oi])
        (l1, h1), (ld, hd) = boot_auc(y, P1[:, oi], P0[:, oi], k, B_AUC)
        log('  L=%4d ms  AUC M1 %.3f IC90(%.3f,%.3f)  M0 %.3f  dAUC %+.3f IC90(%+.3f,%+.3f)' % (o, a1, l1, h1, a0, a1 - a0, ld, hd))
    log('Q1 por familia de rasgos (AUC OOS; M0 estatico como referencia)')
    for nm, cols in FAM.items():
        mf = train(cols, idx_is); Pf = pred(mf, cols, idx_oo)
        log('  %-12s ' % nm + ' '.join('L=%d: %.3f' % (o, roc_auc_score(y, Pf[:, oi])) for oi, o in enumerate(offs) if o in (100, 300, 1000)),
            '| M0:', ' '.join('L=%d: %.3f' % (o, roc_auc_score(y, P0[:, oi])) for oi, o in enumerate(offs) if o in (100, 300, 1000)))
sec('Q1 AUC y lead', s_q1)

def s_q2():
    days_is = sorted(set(dfy[iss])); nfold = min(3, len(days_is))
    Pis = np.zeros((len(idx_is), NO)); fold = np.array([days_is.index(d) % nfold for d in dfy[idx_is]])
    for kf in range(nfold):
        tr = idx_is[fold != kf]; te = fold == kf
        if len(tr) < 100 or te.sum() == 0: continue
        Pis[te] = pred(train(ALL, tr), ALL, idx_is[te])
    lv = fn.index('lvl')
    def evsc(P, idx):
        l = ff[idx][:, :, lv].copy(); bp = fm[idx, 1][:, None]; l = np.where(np.isnan(l), bp, l); return P / np.maximum(l, 0.01) - 1.0
    Sis = evsc(Pis, idx_is); Soo = evsc(M['P1'], idx_oo)
    rng = np.random.default_rng(SEED)
    for Lc in (100, 250):
        cols = [i for i, o in enumerate(offs) if Lc <= o <= Lc + 1000]
        si = Sis[:, cols].min(1); so = Soo[:, cols].min(1); best = None
        log('\n-- Lc=%d ms (offsets %s) --' % (Lc, [offs[i] for i in cols]))
        for q in (0.1, 0.2, 0.3, 0.5):
            thr = np.quantile(si, q); fi = np.zeros(len(pn), bool); fo = np.zeros(len(pn), bool)
            fi[idx_is[si <= thr]] = True; fo[idx_oo[so <= thr]] = True
            ri = evs(iss & ~fi); ro = evs(oo & ~fo); fli = evs(iss & fi); flo = evs(oo & fo)
            cf = co[iss & ~fi].sum() / co[iss].sum()
            if cf >= 0.4 and ri is not None and (best is None or ri['ev'] > best[1]): best = (q, ri['ev'])
            log(' q=%.1f theta=%+.3f marcados IS %.2f OOS %.2f' % (q, thr, (fi & iss).sum() / iss.sum(), (fo & oo).sum() / oo.sum()))
            log('   IS(OOF) retenidos', fs(ri)); log('   IS(OOF) marcados  ', fs(fli))
            log('   OOS retenidos     ', fs(ro), '| pes(-%.3f):' % PES[1], '%+.4f IC90c(%+.3f,%+.3f)' % (ro['ev'] - PES[1], ro['lo'] - PES[1], ro['hi'] - PES[1]) if ro else '')
            log('   OOS marcados (inversion)', fs(flo))
            if ro is not None:
                m = oo; pl = []
                for _ in range(R_PL):
                    rm = (rng.random(len(pn)) < (fo & oo).sum() / oo.sum()) & oo
                    c_ = co[oo & ~rm].sum()
                    if c_ > 0: pl.append(pn[oo & ~rm].sum() / c_)
                pl = np.array(pl); log('   placebo OOS: mediana %+.4f p95 %+.4f; P(placebo>=obs)=%.3f' % (np.median(pl), np.percentile(pl, 95), (pl >= ro['ev']).mean()))
        log(' q primario (IS, retenidos>=40%% del coste): %s' % (best,))
sec('Q2 politica no pujar/cancelar', s_q2)

def s_q2b():
    isS = np.array([d not in oos_days for d in dsy]); ooS = ~isS
    gu = np.array([(1.0 if G.get(str(m)) == s_ else 0.0) if G.get(str(m)) in ('YES', 'NO') else np.nan for m, s_ in zip(sk[:, 1], sk[:, 3])])
    tfs = np.array([tf_map.get(t, np.inf) for t in sk[:, 0]]); lead = tfs - sm_[:, 0]; Ts = sm_[:, 2] - sm_[:, 0] / 1000.0
    keep = (Ts >= 63) & ~np.isnan(gu)
    cba = sf[:, fn.index('cba')]; cx = sx[:, 1]
    ycx = ((cx - cba) >= 0.02) & ~np.isnan(cx) & ~np.isnan(cba)
    def yadv(L, H): return (lead > L) & (lead <= L + H) & (gu == 0)
    ysw = (lead > 100) & (lead <= 2100)
    log('snaps total %d, usables (T>=63, desenlace) %d; IS %d OOS %d; P(barrido 100-2100ms) %.4f; P(barrido adverso) %.4f; P(ask comp +2c en 250ms) %.4f' % (
        len(sm_), keep.sum(), (keep & isS).sum(), (keep & ooS).sum(), ysw[keep].mean(), yadv(100, 2000)[keep].mean(), ycx[keep].mean()))
    rng = np.random.default_rng(SEED); ii = np.where(keep & isS)[0]
    ii = rng.choice(ii, min(len(ii), 100000 if SMOKE else 300000), replace=False); oi_ = np.where(keep & ooS)[0]
    stc = fc(['T', 'coin', 'side', 'hour', 'lvl'])
    def fitauc(y, nm):
        m1 = mkm().fit(sf[ii][:, ALL], y[ii]); m0 = mkm().fit(sf[ii][:, stc], y[ii])
        p1 = m1.predict_proba(sf[oi_][:, ALL])[:, 1]; p0 = m0.predict_proba(sf[oi_][:, stc])[:, 1]; yy = y[oi_]
        if yy.min() == yy.max(): log(nm, 'OOS sin positivos'); return m1, None, None
        (l1, h1), (ld, hd) = boot_auc(yy.astype(int), p1, p0, sm_[oi_, 2].astype(np.int64), max(10, B_AUC // 10))
        log('%s: AUC OOS M1 %.3f IC90(%.3f,%.3f) M0 %.3f dAUC %+.3f IC90(%+.3f,%+.3f) positivos OOS=%d' % (nm, roc_auc_score(yy, p1), l1, h1, roc_auc_score(yy, p0), roc_auc_score(yy, p1) - roc_auc_score(yy, p0), ld, hd, int(yy.sum())))
        return m1, p1, p0
    ya = yadv(100, 2000); m2, p2, _ = fitauc(ya, 'M2 barrido ADVERSO en (100,2100] ms')
    fitauc(ycx, 'M3 ask complementario +2c a +250 ms')
    if p2 is not None:
        yy = ya[oi_]
        for L in (100, 250, 500, 1000, 2000):
            y2 = yadv(L, 1000)[oi_]
            if y2.min() != y2.max(): log('   lead: AUC de M2 contra barrido adverso en (%d,%d] ms: %.3f (positivos %d)' % (L, L + 1000, roc_auc_score(y2, p2), int(y2.sum())))
        pis = m2.predict_proba(sf[ii][:, ALL])[:, 1]
        for q in (0.01, 0.03, 0.10):
            thr = np.quantile(pis, 1 - q); fl = np.zeros(len(sm_), bool); fl[oi_[p2 >= thr]] = True
            def ev_first(mask):
                seen = set(); P_ = []; C_ = []; K_ = []
                for i in np.where(mask)[0][np.argsort(sm_[mask][:, 0])]:
                    t_ = sk[i, 0]
                    if t_ in seen or np.isnan(cx[i]) or np.isnan(sx[i, 3]) or sx[i, 3] < 5 or cx[i] <= 0: continue
                    seen.add(t_); p = cx[i]; P_.append((1.0 - gu[i]) - p - 0.07 * p * (1 - p)); C_.append(p); K_.append(int(sm_[i, 2]))
                if len(P_) < 5: return None
                P_ = np.array(P_); C_ = np.array(C_); lo, hi = boot_ev(P_, C_, np.array(K_), B_EV)
                return 'n=%d EVw=%+.4f IC90c(%+.3f,%+.3f)' % (len(P_), P_.sum() / C_.sum(), lo, hi)
            log(' q=%.2f theta=%.4f marcados OOS %.3f | comprar complementario (taker, ask+250ms, fee) marcados: %s | incondicional: %s' % (
                q, thr, fl[oi_].mean(), ev_first(fl & keep & ooS), ev_first(keep & ooS)))
sec('Q1b/Q2b snapshots: barrido, ask y complementario', s_q2b)
log('\nFIN t=%ds' % (time.time() - t00))
