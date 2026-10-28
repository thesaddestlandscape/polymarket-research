#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""formula_r3_28oct/analysis3.py - manda PREREG_FORMULA_R3.md (hashes en HASHES_R3.txt). Frontera de informacion de la compuerta eps de B.
Uso: analysis3.py   |   analysis3.py --smoke DIA   (solo prueba de codigo con out_smoke/, particion por mercado; NO decide nada)"""
import sys, os, json, math, time, traceback
import numpy as np
from scipy.optimize import minimize
from scipy.special import expit, ndtri
from scipy import stats
from statistics import NormalDist

BASE = '/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct/'
CACHE = '/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'
A2, A3, LAM, B_BOOT, B_PERM = 0.026, 0.085, 1e-4, 2000, 200
NIS = 18
SMOKE = '--smoke' in sys.argv
DAYS = ['2026-10-%02d' % d for d in range(5, 27)]
if SMOKE: DAYS = [sys.argv[sys.argv.index('--smoke') + 1]]
OUT = BASE + ('out_smoke/' if SMOKE else 'out/')
COINS = ('BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB')
LINES = []
rng = np.random.default_rng(2811)
ND = NormalDist()


def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); LINES.append(s)


def safe(fn, *a, **k):
    try: return fn(*a, **k)
    except Exception:
        P('ERROR en', getattr(fn, '__name__', str(fn)), traceback.format_exc()[-1200:]); return None


def load():
    cols = None; parts = []; di = []; miss = []
    for i, d in enumerate(DAYS):
        p = OUT + 'f_%s.npz' % d
        if not os.path.exists(p): miss.append(d); continue
        z = np.load(p, allow_pickle=True)
        nm = [str(x) for x in z['names']]
        if cols is None: cols = nm
        assert nm == cols
        parts.append(z['X']); di.append(np.full(len(z['X']), i, np.int32))
    X = np.concatenate(parts); dayv = np.concatenate(di)
    return {n: X[:, j] for j, n in enumerate(cols)}, dayv, miss


t00 = time.time()
D, dayv, miss = load()
G = json.load(open(CACHE))
mk0 = D['mkt'].astype(np.int64)
uq, inv = np.unique(mk0, return_inverse=True)
yy = np.array([{'YES': 1, 'NO': 0}.get(G.get(str(int(k))), -1) for k in uq], dtype=np.int8)
yv = yy[inv]
idx = np.nonzero(yv >= 0)[0]


def C(n): return D[n][idx].astype(np.float64)


y = np.where(C('yes') > 0.5, yv[idx], 1 - yv[idx]).astype(np.float64)
dd0 = dayv[idx].astype(np.int64)
if SMOKE:
    mkv = C('mkt').astype(np.int64)
    isr = (mkv % 7) != 0; grp = mkv % 6; dd = mkv % 22
else:
    isr = dd0 < NIS; grp = dd0 // 3; dd = dd0
oos = ~isr
ND_ = int(dd.max()) + 1
m = C('m130'); lm = np.log(m / (1.0 - m)); o = lm
T = C('T'); bbl = C('bbl'); coin = C('coin').astype(np.int64); fsz = C('fsz'); fpx = C('fpx')
kap = np.exp(-0.5 * ndtri(m) ** 2) / math.sqrt(2 * math.pi) / (m * (1.0 - m)); sc = kap / np.sqrt(np.maximum(T, 1.0))


def ll(z, yy_): return np.logaddexp(0.0, z) - yy_ * z


LL0 = ll(o, y)


def tint(v, conf=0.90):
    v = np.asarray(v, float); n = len(v)
    if n == 0: return (np.nan, np.nan, np.nan)
    mu = float(v.mean())
    if n < 2: return (mu, np.nan, np.nan)
    se = float(v.std(ddof=1)) / math.sqrt(n); t = float(stats.t.ppf(0.5 + conf / 2.0, n - 1))
    return (mu, mu - t * se, mu + t * se)


def bootci(v, B=B_BOOT):
    v = np.asarray(v, float); n = len(v)
    if n < 2: return (np.nan, np.nan)
    ix = rng.integers(0, n, (B, n)); mm = v[ix].mean(1)
    return (float(np.percentile(mm, 5)), float(np.percentile(mm, 95)))


def dayvals(x, mask):
    s = np.bincount(dd[mask], weights=x[mask], minlength=ND_); c = np.bincount(dd[mask], minlength=ND_)
    k = c > 0
    return s[k] / c[k], np.nonzero(k)[0]


def report(name, z, mask):
    d = ll(z, y) - LL0
    v, days = dayvals(d, mask)
    mu, lo, hi = tint(v); bl, bh = bootci(v)
    eps = expit(z) - m; em = eps[mask]
    sig = float(em.std()) * 100.0
    pred = float(np.mean(em ** 2 / (2.0 * m[mask] * (1.0 - m[mask]))))
    num = np.bincount(dd[mask], weights=em * (y[mask] - m[mask]), minlength=ND_)
    den = np.bincount(dd[mask], weights=em * em, minlength=ND_)
    k = den > 0
    slope = float(num.sum() / den.sum()) if den.sum() > 0 else float('nan')
    sl = tint(num[k] / den[k]) if k.sum() > 1 else (np.nan, np.nan, np.nan)
    P('%-20s n=%8d dias=%2d | dLL=%+.3e IC90t[%+.2e,%+.2e] boot[%+.2e,%+.2e] | sigma_eps=%.2f pp  dLL_pred=%.2e | pend.calib=%.2f IC90[%.2f,%.2f]'
      % (name, int(mask.sum()), len(v), mu, lo, hi, bl, bh, sig, pred, slope, sl[1], sl[2]))
    return dict(mu=mu, lo=lo, hi=hi, sig=sig, slope=slope, pred=pred, vals=v)


def fit(X, off, yy_, lam=LAM):
    n, p = X.shape

    def fg(b):
        w = b[:-1].astype(np.float32)
        z = off + (X @ w).astype(np.float64) + b[-1]
        r = expit(z) - yy_
        L = float(np.mean(np.logaddexp(0.0, z) - yy_ * z)) + lam * float(b[:-1] @ b[:-1])
        g = np.empty_like(b)
        g[:-1] = (X.T @ r.astype(np.float32)).astype(np.float64) / n + 2.0 * lam * b[:-1]
        g[-1] = float(r.mean())
        return L, g
    res = minimize(fg, np.zeros(p + 1), jac=True, method='L-BFGS-B', options={'maxiter': 150, 'ftol': 1e-13, 'gtol': 1e-8})
    return res.x


def fitpred(X, tr, te):
    Xt = X[tr]; mu = Xt.mean(0); sd = Xt.std(0); sd[sd < 1e-9] = 1.0
    Xt -= mu; Xt /= sd
    b = fit(Xt, o[tr], y[tr]); del Xt
    Xe = X[te]; Xe -= mu; Xe /= sd
    z = o[te] + (Xe @ b[:-1].astype(np.float32)).astype(np.float64) + b[-1]
    return z, b


BOOK = ('dq', 'lbs', 'las')


def design(L, blocks, nobook=False):
    g = lambda n: C('%s_%d' % (n, L))
    cols = []; names = []

    def add(n, v): cols.append(v); names.append(n)
    tt = T / 300.0
    if 'B1' in blocks:
        for n in ('dq', 'dc0', 'hasfv', 'lmd', 'spr', 'lbs', 'las'):
            if nobook and n in BOOK: continue
            add(n, g(n))
        add('T', tt); add('T2', tt * tt); add('lm', lm)
        for k, th in enumerate((0.15, 0.20, 0.25)): add('b%d' % k, (bbl >= th - 1e-6).astype(np.float64))
        for k in range(1, 6): add('c%d' % k, (coin == k).astype(np.float64))
    if 'B2' in blocks:
        for n in ('bn02', 'bn1', 'bn5'):
            v = g(n); add(n, v); add(n + 'k', v * sc)
    if 'B3' in blocks:
        for n in ('fo1', 'fo5', 'fo30', 'fc1', 'fc5', 'fc30', 'cnt5', 'imp', 'tsl'): add(n, g(n))
    if 'B4' in blocks:
        for n in ('bl', 'bd1', 'bd5', 'bbn1', 'bbn5'): add(n, g(n))
    if 'B5' in blocks:
        for n in ('dfv1', 'dfv5', 'dfv30', 'dm1', 'dm5', 'dm30'): add(n, g(n))
    return np.column_stack(cols).astype(np.float32), names


ALL = ['B1', 'B2', 'B3', 'B4', 'B5']
R = {}; Z = {}


def bound(s, c):
    a = c / s; pz = 1.0 - ND.cdf(a)
    return s * ND.pdf(a) / pz, pz


def datos():
    P('== DATOS: dias cargados %d de %d (faltan %s) | filas %d -> con desenlace %d (cobertura %.2f %%) | IS %d OOS %d | %s'
      % (len(set(dayv.tolist())), len(DAYS), miss, len(dayv), len(idx), 100.0 * len(idx) / max(1, len(dayv)), int(isr.sum()), int(oos.sum()), 'SMOKE (no decide)' if SMOKE else 'completo'))
    P('   por moneda', {COINS[k]: int((coin == k).sum()) for k in range(6)}, '| hasfv_130 %.3f | filas con relleno a 2 s %d (%.2f %%) | y media %.3f | 1/(2m(1-m)) medio %.3f'
      % (float(C('hasfv_130').mean()), int((fsz > 0).sum()), 100.0 * float((fsz > 0).mean()), float(y.mean()), float(np.mean(1.0 / (2 * m * (1 - m))))))


def modelos():
    z0 = o + A2 * C('dc0_130') + A3 * C('dq_130')
    Z['M0'] = z0
    R['M0_oos'] = report('M0 R2-fijo OOS', z0, oos); report('M0 R2-fijo IS', z0, isr)
    BL = {'M1': ['B1'], 'M2': ['B1', 'B2'], 'M3': ['B1', 'B2', 'B3'], 'M4': ['B1', 'B2', 'B3', 'B4'], 'M5': ALL}
    for nm, bl in BL.items():
        t0 = time.time()
        X, names = design(130, bl)
        z = np.full(len(y), np.nan)
        if nm in ('M1', 'M5'):
            for f in range(6):
                te = isr & (grp == f); tr = isr & (grp != f)
                if te.sum() == 0 or tr.sum() == 0: continue
                z[te], _ = fitpred(X, tr, te)
        z[oos], b = fitpred(X, isr, oos)
        Z[nm] = z
        R[nm + '_oos'] = report(nm + ' OOS', z, oos)
        if nm in ('M1', 'M5'): R[nm + '_cv'] = report(nm + ' IS-CV', z, isr)
        if nm == 'M5':
            top = np.argsort(-np.abs(b[:-1]))[:12]
            P('   M5 coef estandarizados (top12 por |b|):', ', '.join('%s=%+.4f' % (names[i], b[i]) for i in top))
        P('   [%s] p=%d  %.0fs' % (nm, X.shape[1], time.time() - t0))
        del X


def variantes():
    for nm, bl in (('M1nb', ['B1']), ('M5nb', ALL)):
        X, _ = design(130, bl, nobook=True); z = np.full(len(y), np.nan); z[oos], _ = fitpred(X, isr, oos)
        R[nm + '_oos'] = report(nm + ' (sin libro) OOS', z, oos); del X
    for L in (60, 30):
        for nm, bl in (('M1', ['B1']), ('M5', ALL)):
            X, _ = design(L, bl); z = np.full(len(y), np.nan); z[oos], _ = fitpred(X, isr, oos)
            R['%s_L%d' % (nm, L)] = report('%s LR=%d OOS' % (nm, L), z, oos); del X


def extras():
    z = Z['M5']; d = ll(z, y) - LL0
    for k in range(6):
        mk_ = oos & (coin == k)
        if mk_.sum() < 200: continue
        v, _ = dayvals(d, mk_); mu, lo, hi = tint(v)
        P('   M5 OOS moneda %-4s n=%7d dLL=%+.2e IC90t[%+.2e,%+.2e] sigma_eps=%.2f pp' % (COINS[k], int(mk_.sum()), mu, lo, hi, float((expit(z[mk_]) - m[mk_]).std()) * 100))
    for nm_, mask in (('IS-CV', isr), ('OOS', oos)):
        v, _ = dayvals(d, mask); vs = np.sort(v)
        if len(vs) > 3: P('   M5 %s sin los 2 mejores dias: dLL=%+.2e (con todos %+.2e; mejores dias %+.2e %+.2e)' % (nm_, float(vs[2:].mean()), float(v.mean()), float(vs[0]), float(vs[1])))
    oi = np.nonzero(oos)[0]
    key = ((dd[oi] * 10 + coin[oi]) * 20 + (T[oi] // 30).astype(np.int64)) * 100 + (m[oi] // 0.02).astype(np.int64)
    _, sid = np.unique(key, return_inverse=True)
    adj = (z - o)[oi]; oo = o[oi]; yo = y[oi]; l0 = LL0[oi]
    base = np.argsort(sid, kind='stable')
    obs = float((ll(oo + adj, yo) - l0).mean())
    pv = []
    for _ in range(B_PERM):
        order = np.lexsort((rng.random(len(oi)), sid))
        ap = np.empty_like(adj); ap[base] = adj[order]
        pv.append(float((ll(oo + ap, yo) - l0).mean()))
    pv = np.array(pv)
    P('   placebo permutacion (estratos dia x moneda x T30 x m0,02; %d perm.): dLL observado(filas) %+.3e | placebo media %+.3e sd %.2e | p=%.3f' % (B_PERM, obs, pv.mean(), pv.std(), (1 + (pv <= obs).sum()) / (B_PERM + 1.0)))


def proxy():
    ixf = np.nonzero(fsz > 0)[0]
    ts = C('ts'); key = C('mkt').astype(np.int64) * 2 + C('yes').astype(np.int64)
    ixf = ixf[np.argsort(ts[ixf], kind='stable')]
    _, first = np.unique(key[ixf], return_index=True)
    ff = ixf[first]
    x = bbl + 0.01; rho = 0.2 * 0.07 * x * (1.0 - x); pnl = y - x + rho; w = np.minimum(fsz, 5.0) / 5.0
    ev_all = float((w[ff] * pnl[ff]).sum() / w[ff].sum())
    P('== PROXY ESTATICO DE GP (primer relleno por mercado-token con puja a bb+0,01, cola 0; informativo, no decide): filas relleno %d, primeros rellenos %d (OOS %d), EV/acc sin compuerta %+.4f (peso por tamano/5)'
      % (int((fsz > 0).sum()), len(ff), int(oos[ff].sum()), ev_all))
    for nm in ('M1', 'M5'):
        eps = expit(Z[nm]) - m
        if np.isnan(eps[ff]).any(): P('   %s: eps con NaN en rellenos, se omite' % nm); continue
        P('   %s: E[eps|primer relleno]=%+.2f pp frente a E[eps|todas las filas]=%+.2f pp (fuera de muestra: OOF en IS, final en OOS)' % (nm, float(eps[ff].mean()) * 100, float(eps[~np.isnan(eps)].mean()) * 100))
        for c in (0.0, 0.005, 0.01, 0.02):
            pas = eps[ff] >= c
            if pas.sum() < 5: P('   %s c=%+.1f pp: pasan %d rellenos (insuficiente)' % (nm, c * 100, int(pas.sum()))); continue
            wf = w[ff]; pf = pnl[ff]
            evp = float((wf[pas] * pf[pas]).sum() / wf[pas].sum()); dev = evp - ev_all
            res = []
            for lab, dmask in (('22d', np.ones(len(ff), bool)), ('OOS', oos[ff])):
                dl = []
                for d_ in np.unique(dd[ff][dmask]):
                    sel = dmask & (dd[ff] == d_)
                    if (pas & sel).sum() == 0 or sel.sum() == 0: continue
                    dl.append(float((wf[pas & sel] * pf[pas & sel]).sum() / wf[pas & sel].sum() - (wf[sel] * pf[sel]).sum() / wf[sel].sum()))
                mu, lo, hi = tint(dl); res.append('%s dias=%d dEV=%+.4f IC90[%+.4f,%+.4f]' % (lab, len(dl), mu, lo, hi))
            strat = coin[ff] * 1000 + np.rint(fpx[ff] * 100).astype(np.int64)
            us, sidf = np.unique(strat, return_inverse=True)
            kk = np.bincount(sidf, weights=pas.astype(float), minlength=len(us)).astype(np.int64)
            starts = np.concatenate([[0], np.cumsum(np.bincount(sidf, minlength=len(us)))[:-1]])
            sims = []
            for _ in range(500):
                order = np.lexsort((rng.random(len(sidf)), sidf))
                rank = np.arange(len(sidf)) - starts[sidf[order]]
                ps = np.zeros(len(sidf), bool); ps[order] = rank < kk[sidf[order]]
                sims.append(float((wf[ps] * pf[ps]).sum() / wf[ps].sum() - ev_all))
            sims = np.array(sims)
            P('   %s c=%+.1f pp: pasan %d (%.1f %% del peso) | EV/acc paso %+.4f dEV(agregado) %+.4f | %s | placebo por precio de relleno: media %+.4f p=%.3f'
              % (nm, c * 100, int(pas.sum()), 100.0 * float(wf[pas].sum() / wf.sum()), evp, dev, ' ; '.join(res), float(sims.mean()), (1 + (sims >= dev).sum()) / 501.0))


def veredicto():
    r5 = R.get('M5_oos'); r1 = R.get('M1_oos')
    if r5 is None: P('VEREDICTO_R3: SIN_DATOS'); return
    exito = (r5['sig'] >= 2.6) and (r5['mu'] <= -2e-3) and (r5['hi'] < 0) and (r5['slope'] >= 0.7)
    parcial = (r5['sig'] >= 1.5) and (r5['hi'] < 0)
    P('VEREDICTO_R3: %s | M5 OOS sigma_eps=%.2f pp (umbral 2,6), dLL=%+.2e (umbral -2,0e-3) IC90t sup=%+.2e, pend.calib=%.2f (umbral 0,7)%s'
      % ('EXITO' if exito else ('PARCIAL' if parcial else 'FALLO'), r5['sig'], r5['mu'], r5['hi'], r5['slope'], ' [SMOKE]' if SMOKE else ''))
    P('== COTA ANALITICA con la sigma_eps alcanzada (E[eps|eps>=c], gaussiana; pass = fraccion de tiempo que se cotiza)')
    for lab, r in (('M0 R2 fijo', R.get('M0_oos')), ('M1 OOS', r1), ('M5 OOS', r5)):
        if r is None: continue
        s = r['sig']
        P('   %-10s sigma=%.2f pp: ' % (lab, s) + ' | '.join('c=%+.1f pp -> %+.2f pp (pasa %.0f %%)' % ((c,) + (bound(s, c)[0], 100 * bound(s, c)[1])) for c in (0.0, 0.5, 1.0)))
    a = R.get('M5nb_oos')
    if a is not None:
        sb = math.sqrt(max(r5['sig'] ** 2 - a['sig'] ** 2, 0.0)); rest = a['sig']; smax = math.sqrt(rest ** 2 + (2.0 * sb) ** 2)
        P('REGLA_L2: sigma(M5)=%.2f, sigma(M5 sin libro)=%.2f -> contribucion del libro L1 %.2f pp en cuadratura; cota generosa de L2 (x2 en la parte de libro) sigma_max=%.2f pp (minimo matematico 2,1) -> %s'
          % (r5['sig'], rest, sb, smax, 'L2_JUSTIFICADO (solo si ademas PARCIAL/EXITO)' if smax >= 2.1 else 'L2_NO_JUSTIFICADO -> cerrar familia pasiva L1/L2 si no hay EXITO'))


if __name__ == '__main__':
    P('analysis3 %s  dias=%s' % ('SMOKE' if SMOKE else 'COMPLETO', DAYS[0] + '..' + DAYS[-1]))
    for fn in (datos, modelos, variantes, extras, proxy, veredicto): safe(fn)
    P('fin %.0f s' % (time.time() - t00))
    open(BASE + ('analysis_salida_smoke.txt' if SMOKE else 'analysis_salida.txt'), 'w').write('\n'.join(LINES) + '\n')
