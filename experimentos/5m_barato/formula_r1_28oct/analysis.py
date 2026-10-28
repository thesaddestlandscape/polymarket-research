#!/usr/bin/env python3
# FORMULA_R1_B analisis (prerregistrado en PREREG_FORMULA_R1.md). uso: analysis.py [--smoke]
import sys, glob, gzip, csv, math, traceback
import numpy as np
from statistics import NormalDist
np.seterr(all='ignore')
ND = NormalDist()
D0 = '/root/polymarket-research/experimentos/5m_barato/formula_r1_28oct/'
ESC = '/root/polymarket-research/experimentos/5m_barato/escalera_patas_28oct/out/e_%s.csv'
SMOKE = '--smoke' in sys.argv
OUTD = D0 + ('out_smoke/' if SMOKE else 'out/')
IS_ALL = ['2026-10-%02d' % d for d in range(5, 23)]
OOS_ALL = ['2026-10-%02d' % d for d in range(23, 27)]
KAP = [0.0, 0.005, 0.01, 0.02, 0.03, 0.05]
KIN = [0.0, 0.01, 0.02, 0.03, 0.05, 0.08]
B = 2000; NPL = 30 if SMOKE else 200
MINFIT = 20 if SMOKE else 200; MINSOLD = 3 if SMOKE else 100
rng = np.random.default_rng(2811)
STRC = ('dia', 'coin', 'mercado', 'lado', 'label', 'cls')
EDG = [0.10, 0.15, 0.20, 0.25, 0.30]
def fee(p): return 0.07 * p * (1 - p)
def sig(z): return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
def logit(p): p = np.clip(p, 1e-3, 1 - 1e-3); return np.log(p / (1 - p))
def ndtr(x): return 0.5 * (1.0 + np.vectorize(math.erf)(np.asarray(x, float) / math.sqrt(2.0)))
def ndtri(p):
    p = np.clip(p, 0.005, 0.995)
    return np.array([ND.inv_cdf(v) if v == v else np.nan for v in p])
def llv(y_, q_): q_ = np.clip(q_, 1e-6, 1 - 1e-6); return -(y_ * np.log(q_) + (1 - y_) * np.log(1 - q_))
def fit(X, y, off, lam=1e-3, it=40):
    k = X.shape[1]; b = np.zeros(k); P = lam * np.diag(np.r_[0.0, np.ones(k - 1)])
    for _ in range(it):
        p = sig(off + X @ b); W = p * (1 - p) + 1e-6
        g = X.T @ (y - p) - P @ b; H = (X * W[:, None]).T @ X + P
        try: d = np.linalg.solve(H, g)
        except Exception: break
        b = b + d
        if np.abs(d).max() < 1e-8: break
    p = sig(off + X @ b); W = p * (1 - p) + 1e-6
    H = (X * W[:, None]).T @ X + P
    return b, np.sqrt(np.abs(np.diag(np.linalg.pinv(H))))
def load():
    cols = {}
    for f in sorted(glob.glob(OUTD + 'f_*.csv.gz')):
        with gzip.open(f, 'rt') as fh: L = list(csv.DictReader(fh))
        if not L: continue
        for k in L[0].keys():
            if k in STRC: a = np.array([r[k] for r in L])
            else: a = np.array([float(r[k]) if r[k] not in ('', 'None', 'nan') else np.nan for r in L])
            cols.setdefault(k, []).append(a)
    return {k: np.concatenate(v) for k, v in cols.items()}
def feats(R):
    ok = lambda b, a: (b == b) & (a == a) & (a >= b)
    mA = np.where(ok(R['A_b'], R['A_a']), 0.5 * (R['A_b'] + R['A_a']), np.nan)
    mB = np.where(ok(R['B_b'], R['B_a']), 0.5 * (R['B_b'] + R['B_a']), np.nan)
    mC = np.where(ok(R['C_b'], R['C_a']) & (R['C_age'] <= 15000), 0.5 * (R['C_b'] + R['C_a']), np.nan)
    mC0 = np.where(ok(R['C0_b'], R['C0_a']) & (R['C0_age'] <= 30000), 0.5 * (R['C0_b'] + R['C0_a']), np.nan)
    lA = logit(mA); dP = logit(1 - mB) - lA
    zC = ndtri(mC); zC0 = ndtri(mC0)
    tau = np.maximum(R['tau'], 1.0)
    w = (np.sqrt(tau + R['extra']) * zC - np.where(R['jw'] >= 2, np.sqrt(300.0 + R['extra']) * zC0, 0.0)) / np.sqrt(tau)
    dC = np.clip(logit(ndtr(np.clip(w, -6, 6))) - lA, -7, 7)
    sgn = np.where(R['lado'] == 'YES', 1.0, -1.0)
    zB = np.clip(sgn * np.log(R['S_now'] / R['refB']) / (R['sig60'] * np.sqrt(np.maximum(tau - 12.0, 3.0))), -6, 6)
    dQ = np.clip((R['A_bs'] - R['A_as']) / (R['A_bs'] + R['A_as']), -1, 1)
    return dict(mA=mA, lA=lA, dP=dP, dQ=dQ, dC=dC, zB=zB)
def pct(a): return np.percentile(a, [5, 95])
def main():
    R = load(); n = len(R['p0']); present = sorted(set(R['dia']))
    ISd = [d for d in IS_ALL if d in present]; OOd = [d for d in OOS_ALL if d in present]
    print('FILAS', n, 'DIAS IS', len(ISd), 'OOS', len(OOd), flush=True)
    umap = {}
    uid = np.array([umap.setdefault(k, len(umap)) for k in zip(R['dia'], R['mercado'], R['lado'])])
    order = np.lexsort((-R['tau'], uid)); R = {k: v[order] for k, v in R.items()}; uid = uid[order]; nU = len(umap)
    F = feats(R); m0 = R['label'] == 'n0'
    U = {}
    for k in ('p0', 'sh', 'cost', 'win'):
        U[k] = np.full(nU, np.nan); U[k][uid[m0]] = R[k][m0]
    udia = np.empty(nU, dtype=object); ucoin = np.empty(nU, dtype=object)
    udia[uid[m0]] = R['dia'][m0]; ucoin[uid[m0]] = R['coin'][m0]
    sh, cost, p0, win = U['sh'], U['cost'], U['p0'], U['win']
    reb = 0.2 * sh * fee(p0); hold = sh * win - cost + reb
    days = ISd + OOd; dmap = {d: i for i, d in enumerate(days)}; nd = len(days)
    dayid = np.array([dmap[d] for d in udia]); isi = np.array([dmap[d] for d in ISd]); ooi = np.array([dmap[d] for d in OOd])
    costd = np.bincount(dayid, weights=cost, minlength=nd); holdd = np.bincount(dayid, weights=hold, minlength=nd)
    rday = dayid[uid]; cls = R['cls']; lab = R['label']; y = R['win']
    print('UNIDADES', nU, 'IS', int(np.isin(dayid, isi).sum()), 'OOS', int(np.isin(dayid, ooi).sum()), 'coste/dia IS %.1f OOS %.1f EUR' % (costd[isi].mean() if len(isi) else 0, costd[ooi].mean() if len(ooi) else 0))
    print('HOLD EVw IS %.4f OOS %.4f' % (holdd[isi].sum() / costd[isi].sum() if len(isi) else float('nan'), holdd[ooi].sum() / costd[ooi].sum() if len(ooi) else float('nan')))
    X = np.column_stack([np.ones(n)] + [np.where(np.isfinite(F[k]), F[k], 0.0) for k in ('dC', 'dQ', 'zB')])
    off = F['lA']; valid = np.isfinite(off); QM = sig(off)
    XB = np.full(n, np.nan); Q0 = np.full(n, np.nan); COEF = {}
    for cl in ('N', 'E', 'L'):
        mcl = (cls == cl) & valid; trm = (mcl & (lab == 'n0')) if cl == 'N' else mcl
        ISm = trm & np.isin(rday, isi)
        if ISm.sum() < MINFIT: continue
        b, se = fit(X[ISm], y[ISm], off[ISm]); b0, _ = fit(X[ISm][:, :1], y[ISm], off[ISm]); COEF[cl] = (b, se, int(ISm.sum()))
        for d in isi:
            tr = ISm & (rday != d); te = mcl & (rday == d)
            if len(isi) >= 3 and tr.sum() >= MINFIT:
                bb, _ = fit(X[tr], y[tr], off[tr]); bz, _ = fit(X[tr][:, :1], y[tr], off[tr])
                XB[te] = X[te] @ bb; Q0[te] = sig(off[te] + bz[0])
            else:
                XB[te] = X[te] @ b; Q0[te] = sig(off[te] + b0[0])
        te = mcl & np.isin(rday, ooi); XB[te] = X[te] @ b; Q0[te] = sig(off[te] + b0[0])
    QH = sig(off + XB); QINV = sig(off - XB)
    print('\n== COBERTURA de terminos (fraccion finita) por clase ==')
    VAL = (np.isfinite(R['X_b']) & (R['X_age'] <= 2000) & (R['X_bs'] >= R['sh'] - 1e-9) & (R['sh'] * R['X_b'] >= 1.0 - 1e-9) & (R['X_b'] >= 0.01 - 1e-9))
    for cl in ('N', 'E', 'L'):
        m = cls == cl
        print(cl, 'filas', int(m.sum()), 'mA %.3f dC %.3f dQ %.3f zB %.3f ejecutable(VAL) %.3f' % (*[np.isfinite(F[k][m]).mean() for k in ('mA', 'dC', 'dQ', 'zB')], VAL[m].mean()), '| paridad dP: filas con |dP|>0.02 = %.4f (libros espejo => ~0)' % np.nanmean(np.abs(F['dP'][m]) > 0.02))
    print('\n== COEFICIENTES (ajuste en todo IS; SE del modelo, anticonservador) ==')
    for cl, (b, se, nn) in COEF.items():
        print(cl, 'n', nn, 'a0 %.3f(%.3f) a2_dC %.3f(%.3f) a3_dQ %.3f(%.3f) a4_zB %.3f(%.3f)' % (b[0], se[0], b[1], se[1], b[2], se[2], b[3], se[3]))
    print('\n== CONTENIDO INFORMATIVO: logloss medio mid-solo / a0 / completo; delta(completo-a0) e IC90 por dias ==')
    for cl in ('N', 'E', 'L'):
        for nm, dd in (('IS cross-fit', isi), ('OOS', ooi)):
            if len(dd) == 0: continue
            m = (cls == cl) & valid & np.isfinite(XB) & np.isin(rday, dd) & ((lab == 'n0') if cl == 'N' else True)
            if m.sum() < 30: continue
            dl = llv(y[m], QH[m]) - llv(y[m], Q0[m])
            num = np.bincount(rday[m], weights=dl, minlength=nd)[dd]; den = np.bincount(rday[m], minlength=nd)[dd].astype(float)
            bi = rng.integers(0, len(dd), size=(B, len(dd))); bs = num[bi].sum(1) / np.maximum(den[bi].sum(1), 1)
            print(cl, nm, 'n', int(m.sum()), 'LL mid %.4f a0 %.4f full %.4f' % (llv(y[m], QM[m]).mean(), llv(y[m], Q0[m]).mean(), llv(y[m], QH[m]).mean()), 'dLL(full-a0) %.5f IC90 [%.5f, %.5f]' % (num.sum() / den.sum(), *pct(bs)))
    print('\n== SELECCION ADVERSA MEDIDA: win - mid por instante (filas con mid) ==')
    for L_ in ('n1', 'n0', 'e1', 'e2', 'e3', 'e4', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6'):
        out = [L_]
        for nm, dd in (('IS', isi), ('OOS', ooi)):
            m = (lab == L_) & valid & np.isin(rday, dd)
            if m.sum() == 0: out.append(nm + ' n=0'); continue
            out.append(nm + ' n=%d win=%.3f mid=%.3f win-mid=%+.4f' % (m.sum(), y[m].mean(), F['mA'][m].mean(), (y[m] - F['mA'][m]).mean()))
        print(' | '.join(out))
    print('\n== TERMINOS UNO A UNO: dLogLoss(a0+termino menos a0) en IS cross-fit y OOS con IC90 por dias; coeficiente IS | OOS ==')
    for cl in ('N', 'E', 'L'):
        trm0 = (cls == cl) & valid & ((lab == 'n0') if cl == 'N' else True)
        for j, tn in ((1, 'dC'), (2, 'dQ'), (3, 'zB')):
            Xt = X[:, [0, j]]; ISm = trm0 & np.isin(rday, isi); OOm = trm0 & np.isin(rday, ooi)
            if ISm.sum() < MINFIT or OOm.sum() < 30: continue
            bI, _ = fit(Xt[ISm], y[ISm], off[ISm]); b0I, _ = fit(Xt[ISm][:, :1], y[ISm], off[ISm]); bO_, _ = fit(Xt[OOm], y[OOm], off[OOm])
            line = [cl + ' ' + tn + ' coef IS %+.3f | OOS %+.3f' % (bI[1], bO_[1])]
            for nm, dd in (('IS', isi), ('OOS', ooi)):
                dl = np.full(n, np.nan)
                for d in dd:
                    te = trm0 & (rday == d)
                    if nm == 'IS' and len(isi) >= 3:
                        tr = ISm & (rday != d)
                        if tr.sum() < MINFIT: continue
                        bb, _ = fit(Xt[tr], y[tr], off[tr]); bz, _ = fit(Xt[tr][:, :1], y[tr], off[tr])
                    else: bb, bz = bI, b0I
                    dl[te] = llv(y[te], sig(off[te] + Xt[te] @ bb)) - llv(y[te], sig(off[te] + bz[0]))
                m = np.isfinite(dl)
                if m.sum() < 30: continue
                num = np.bincount(rday[m], weights=dl[m], minlength=nd)[dd]; den = np.bincount(rday[m], minlength=nd)[dd].astype(float)
                bi = rng.integers(0, len(dd), size=(B, len(dd))); bs = num[bi].sum(1) / np.maximum(den[bi].sum(1), 1)
                line.append('%s n=%d dLL=%+.5f IC90 [%+.5f, %+.5f]' % (nm, m.sum(), num.sum() / den.sum(), *pct(bs)))
            print(' | '.join(line))
    VAL_nomin = (np.isfinite(R['X_b']) & (R['X_age'] <= 2000) & (R['X_bs'] >= R['sh'] - 1e-9) & (R['X_b'] >= 0.01 - 1e-9))
    S = R['X_b'] - fee(R['X_b']); rsh = R['sh']; rcost = R['cost']; rreb = 0.2 * rsh * fee(R['p0'])
    print('\n== COSTE DE SALIR POR INSTANTE (vender todo al bid de t_d+250 ms; solo filas ejecutables) ==')
    for L_ in ('e1', 'e2', 'e3', 'e4', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6'):
        out = [L_]
        for nm, dd in (('IS', isi), ('OOS', ooi)):
            m = (lab == L_) & VAL & np.isin(rday, dd)
            if m.sum() == 0: out.append(nm + ' n=0'); continue
            ps = rsh[m] * S[m] - rcost[m] + rreb[m]; ph = rsh[m] * y[m] - rcost[m] + rreb[m]
            out.append(nm + ' n=%d win=%.3f mid=%.3f S=%.3f EVw_vender=%.3f EVw_mantener=%.3f' % (m.sum(), y[m].mean(), F['mA'][m].mean(), S[m].mean(), ps.sum() / rcost[m].sum(), ph.sum() / rcost[m].sum()))
        print(' | '.join(out))
    def exit_policy(qh, classes, kap):
        cond = VAL & np.isin(cls, classes) & np.isfinite(qh) & ((S - qh) >= kap - 1e-12)
        idx = np.nonzero(cond)[0]; pnl = hold.copy(); sold = np.zeros(nU, bool)
        if len(idx):
            uu, first = np.unique(uid[idx], return_index=True); ri = idx[first]
            pnl[uu] = sh[uu] * S[ri] - cost[uu] + reb[uu]; sold[uu] = True
        return pnl, sold
    def dday(pnl_alt): return np.bincount(dayid, weights=pnl_alt - hold, minlength=nd)
    def best2out(dp, dd):
        if len(dd) <= 2: return float('nan')
        keep = dd[np.sort(np.argsort(-dp[dd])[2:])]; return dp[keep].sum() / costd[keep].sum()
    def boot(dp, dd):
        bi = rng.integers(0, len(dd), size=(B, len(dd))); ix = dd[bi]; return dp[ix].sum(1) / costd[ix].sum(1)
    # ---------------- VENDER ----------------
    try:
        print('\n== VENDER: 18 variantes (clase x kappa); IS con q^ cross-fit; OOS con ajuste en todo IS ==')
        VARS = [(nm, cs, k) for nm, cs in (('E', ['E']), ('L', ['L']), ('EL', ['E', 'L'])) for k in KAP]
        res = {}
        for nm, cs, k in VARS:
            pnl, sold = exit_policy(QH, cs, k); res[(nm, k)] = (dday(pnl), sold)
        keys = list(res.keys()); idxIS = isi[rng.integers(0, len(isi), size=(B, len(isi)))]
        D_is = np.array([res[k][0][isi].sum() / costd[isi].sum() for k in keys])
        Dboot = np.array([res[k][0][idxIS].sum(1) / costd[idxIS].sum(1) for k in keys]); s_v = Dboot.std(1) + 1e-12
        Tobs = (D_is / s_v).max(); Tb = ((Dboot - D_is[:, None]) / s_v[:, None]).max(0); p_ms = (1 + (Tb >= Tobs).sum()) / (1 + B)
        nsIS = {k: int(res[k][1][np.isin(dayid, isi)].sum()) for k in keys}; nsOO = {k: int(res[k][1][np.isin(dayid, ooi)].sum()) for k in keys}
        for i, k in enumerate(keys):
            dO = res[k][0][ooi].sum() / costd[ooi].sum() if len(ooi) else float('nan')
            print('%-3s kappa=%.3f  IS Delta %+.5f (vendidas %d)  OOS Delta %+.5f (vendidas %d)' % (k[0], k[1], D_is[i], nsIS[k], dO, nsOO[k]))
        cand = [i for i, k in enumerate(keys) if nsIS[k] >= MINSOLD]
        iv = max(cand, key=lambda i: D_is[i]) if cand else int(np.argmax(D_is)); vk = keys[iv]; cs = dict((a, b) for a, b, c in VARS)[vk[0]]
        print('VARIANTE IS-ELEGIDA', vk, 'p max-stat IS = %.4f (18 variantes)' % p_ms)
        dp = res[vk][0]; lo, hi = pct(Dboot[iv])
        print('IS  Delta %+.5f IC90 dias [%+.5f, %+.5f] sin 2 mejores dias %+.5f  EVw regla %.4f (HOLD %.4f)' % (D_is[iv], lo, hi, best2out(dp, isi), (holdd[isi].sum() + dp[isi].sum()) / costd[isi].sum(), holdd[isi].sum() / costd[isi].sum()))
        pnl_v, sold_v = exit_policy(QH, cs, vk[1])
        if len(ooi):
            dO = dp[ooi].sum() / costd[ooi].sum(); bO = boot(dp, ooi); lo, hi = pct(bO)
            print('OOS Delta %+.5f IC90 dias [%+.5f, %+.5f] sin 2 mejores dias %+.5f  EVw regla %.4f (HOLD %.4f)  vendidas %d de %d  Delta por dia %s' % (dO, lo, hi, best2out(dp, ooi), (holdd[ooi].sum() + dp[ooi].sum()) / costd[ooi].sum(), holdd[ooi].sum() / costd[ooi].sum(), nsOO[vk], int(np.isin(dayid, ooi).sum()), np.round(dp[ooi] / costd[ooi], 4)))
            print('OOS Delta EUR/dia %.3f (IC90 dias [%.3f, %.3f]) => EUR/ano a volumen simulado %.0f' % (dp[ooi].mean(), *pct(dp[ooi][rng.integers(0, len(ooi), size=(B, len(ooi)))].mean(1)), dp[ooi].mean() * 365))
            VAL_save = VAL; VAL = VAL_nomin; pnl2, sold2 = exit_policy(QH, cs, vk[1]); VAL = VAL_save; d2 = dday(pnl2)
            print('SENSIBILIDAD sin minimo 1 USD: IS Delta %+.5f (vendidas %d) OOS Delta %+.5f (vendidas %d)' % (d2[isi].sum() / costd[isi].sum(), int(sold2[np.isin(dayid, isi)].sum()), d2[ooi].sum() / costd[ooi].sum(), int(sold2[np.isin(dayid, ooi)].sum())))
            # placebo e inversion
            oo_rows = np.isin(rday, ooi) & valid; ridx = np.nonzero(oo_rows)[0]
            strat = np.array(['%s|%s|%d' % (c_, k_, int(m_ * 10)) for c_, k_, m_ in zip(R['coin'][ridx], cls[ridx], F['mA'][ridx])])
            _, inv = np.unique(strat, return_inverse=True); groups = [ridx[inv == g] for g in range(inv.max() + 1)]
            def perm_q():
                Xp = X.copy()
                for g in groups:
                    if len(g) > 1: Xp[g, 1:] = X[g[rng.permutation(len(g))], 1:]
                QP = QH.copy()
                for cl_, (b_, _, _) in COEF.items():
                    mm = oo_rows & (cls == cl_); QP[mm] = sig(off[mm] + Xp[mm] @ b_)
                return QP
            Dp = []
            for _ in range(NPL):
                pnl_p, _s = exit_policy(perm_q(), cs, vk[1]); Dp.append((dday(pnl_p)[ooi]).sum() / costd[ooi].sum())
            Dp = np.array(Dp); print('PLACEBO OOS (cov. permutadas): media %+.5f p95 %+.5f  p(>=obs) = %.3f' % (Dp.mean(), np.percentile(Dp, 95), (1 + (Dp >= dO).sum()) / (1 + NPL)))
            pnl_i, sold_i = exit_policy(QINV, cs, vk[1]); di = dday(pnl_i)
            print('INVERSION: OOS Delta %+.5f (vendidas %d)  IS Delta %+.5f (vendidas %d)' % (di[ooi].sum() / costd[ooi].sum(), int(sold_i[np.isin(dayid, ooi)].sum()), di[isi].sum() / costd[isi].sum(), int(sold_i[np.isin(dayid, isi)].sum())))
            print('\n-- por moneda x bucket de p0 (regla elegida): n unidades / vendidas / Delta EUR  [IS | OOS] --')
            bk = np.digitize(p0, EDG)
            for c_ in sorted(set(ucoin)):
                for b_ in range(len(EDG) + 1):
                    cells = []
                    for dd in (isi, ooi):
                        m = (ucoin == c_) & (bk == b_) & np.isin(dayid, dd); cells.append((int(m.sum()), int((sold_v & m).sum()), float((pnl_v - hold)[m].sum())))
                    if cells[0][0] + cells[1][0] >= 30: print(c_, 'bucket', b_, 'IS n=%d v=%d D=%+.2f | OOS n=%d v=%d D=%+.2f' % (*cells[0], *cells[1]))
            nco = sum(1 for c_ in set(ucoin) if (pnl_v - hold)[(ucoin == c_) & np.isin(dayid, ooi)].sum() > 0)
            print('monedas con Delta OOS>0:', nco, 'de', len(set(ucoin)))
            crit = dict(i=(D_is[iv] > 0 and lo_is_pos(Dboot[iv]) and p_ms < 0.05), ii=(dO > 0 and pct(bO)[0] > 0 and best2out(dp, ooi) > 0 and (holdd[ooi].sum() + dp[ooi].sum()) > 0), iii=((1 + (Dp >= dO).sum()) / (1 + NPL) < 0.05 and di[ooi].sum() < 0), iv=nco >= 3, v=nsOO[vk] >= 150)
            print('CRITERIOS VENDER:', crit)
    except Exception:
        traceback.print_exc()
    # ---------------- CANCELAR ----------------
    try:
        print('\n== CANCELAR (reserva de compra): cancelar si q^_N + rebate - p0 < kappa_in ==')
        def entry_keep(qh, lab_, kin):
            r_ = np.nonzero((lab == lab_) & np.isfinite(qh))[0]; sc = qh[r_] + 0.2 * fee(R['p0'][r_]) - R['p0'][r_]
            keep = np.ones(nU, bool); keep[uid[r_[sc < kin - 1e-12]]] = False; return keep
        def entry_dd(keep): return np.bincount(dayid, weights=np.where(keep, 0.0, -hold), minlength=nd)
        resE = {}
        for lb_ in ('n0', 'n1'):
            for k in KIN: kp = entry_keep(QH, lb_, k); resE[(lb_, k)] = (entry_dd(kp), kp)
        keysE = [k for k in resE if k[0] == 'n0']; idxIS = isi[rng.integers(0, len(isi), size=(B, len(isi)))]
        D_is = np.array([resE[k][0][isi].sum() / costd[isi].sum() for k in keysE]); Dboot = np.array([resE[k][0][idxIS].sum(1) / costd[idxIS].sum(1) for k in keysE]); s_v = Dboot.std(1) + 1e-12
        Tobs = (D_is / s_v).max(); Tb = ((Dboot - D_is[:, None]) / s_v[:, None]).max(0); p_ms = (1 + (Tb >= Tobs).sum()) / (1 + B)
        for lb_ in ('n0', 'n1'):
            for k in KIN:
                dpE, kp = resE[(lb_, k)]; dI = dpE[isi].sum() / costd[isi].sum(); dO = dpE[ooi].sum() / costd[ooi].sum() if len(ooi) else float('nan')
                cI = int((~kp)[np.isin(dayid, isi)].sum()); cO = int((~kp)[np.isin(dayid, ooi)].sum())
                print('%s kappa_in=%.2f  IS Delta_EUR/EUR %+.5f (canceladas %d)  OOS %+.5f (canceladas %d)' % (lb_, k, dI, cI, dO, cO))
        cand = [i for i, k in enumerate(keysE) if int((~resE[k][1])[np.isin(dayid, isi)].sum()) >= MINSOLD]
        iv = max(cand, key=lambda i: D_is[i]) if cand else int(np.argmax(D_is)); vk = keysE[iv]; dpE, kp = resE[vk]
        print('VARIANTE IS-ELEGIDA', vk, 'p max-stat IS = %.4f (6 variantes)' % p_ms, 'IS Delta %+.5f IC90 [%+.5f, %+.5f] sin 2 mejores %+.5f' % (D_is[iv], *pct(Dboot[iv]), best2out(dpE, isi)))
        if len(ooi):
            dO = dpE[ooi].sum() / costd[ooi].sum(); bO = boot(dpE, ooi); mO = np.isin(dayid, ooi)
            print('OOS Delta %+.5f IC90 dias [%+.5f, %+.5f] sin 2 mejores %+.5f; canceladas %d de %d (%.1f%%); EVw retenidas %.4f vs HOLD %.4f; EUR totales OOS %+.2f en %d dias' % (dO, *pct(bO), best2out(dpE, ooi), int((~kp)[mO].sum()), int(mO.sum()), 100 * (~kp)[mO].mean(), hold[kp & mO].sum() / cost[kp & mO].sum(), hold[mO].sum() / cost[mO].sum(), dpE[ooi].sum(), len(ooi)))
            oo_rows = np.isin(rday, ooi) & valid; ridx = np.nonzero(oo_rows)[0]
            strat = np.array(['%s|%s|%d' % (c_, k_, int(m_ * 10)) for c_, k_, m_ in zip(R['coin'][ridx], cls[ridx], F['mA'][ridx])])
            _, inv = np.unique(strat, return_inverse=True); groups = [ridx[inv == g] for g in range(inv.max() + 1)]
            keepm = kp & mO
            num_k = np.bincount(dayid[keepm], weights=hold[keepm], minlength=nd)[ooi]; den_k = np.bincount(dayid[keepm], weights=cost[keepm], minlength=nd)[ooi]
            bi = rng.integers(0, len(ooi), size=(B, len(ooi))); bk_ = num_k[bi].sum(1) / np.maximum(den_k[bi].sum(1), 1e-9)
            print('EVw retenidas OOS %.4f IC90 dias [%.4f, %.4f]' % (num_k.sum() / max(den_k.sum(), 1e-9), *pct(bk_)))
            Dp = []
            for _ in range(NPL):
                Xp = X.copy()
                for g in groups:
                    if len(g) > 1: Xp[g, 1:] = X[g[rng.permutation(len(g))], 1:]
                QP = QH.copy(); mm = oo_rows & (cls == 'N')
                if 'N' in COEF: QP[mm] = sig(off[mm] + Xp[mm] @ COEF['N'][0])
                kpp = entry_keep(QP, vk[0], vk[1]); Dp.append(entry_dd(kpp)[ooi].sum() / costd[ooi].sum())
            Dp = np.array(Dp); kpi = entry_keep(QINV, vk[0], vk[1]); di = entry_dd(kpi)
            print('PLACEBO OOS: media %+.5f p95 %+.5f p(>=obs) = %.3f ; INVERSION OOS Delta %+.5f (canceladas %d)' % (Dp.mean(), np.percentile(Dp, 95), (1 + (Dp >= dO).sum()) / (1 + NPL), di[ooi].sum() / costd[ooi].sum(), int((~kpi)[mO].sum())))
            pp = (1 + (Dp >= dO).sum()) / (1 + NPL)
            print('CRITERIOS CANCELAR:', dict(i=bool(D_is[iv] > 0 and pct(Dboot[iv])[0] > 0 and p_ms < 0.05), ii=bool(dO > 0 and pct(bO)[0] > 0 and best2out(dpE, ooi) > 0 and num_k.sum() / max(den_k.sum(), 1e-9) > 0 and pct(bk_)[0] > 0), iii=bool(pp < 0.05 and di[ooi].sum() < 0), v=bool(int((~kp)[mO].sum()) >= 150)))
    except Exception:
        traceback.print_exc()
    # ---------------- ESCALERA ----------------
    try:
        print('\n== ESCALERA FIJA (escalera_patas_28oct, terminal H, mismas unidades) ==')
        LAD = {}
        for d in days:
            try:
                with open(ESC % d) as fh:
                    for r in csv.DictReader(fh):
                        if r['kind'] == 'real': LAD[(d, r['mercado'], r['lado'])] = r
            except FileNotFoundError: pass
        for nm_, col in (('HOLD', 'pnl_base_H'), ('+10c', 'pnl_s1_H'), ('+20c', 'pnl_s3_H'), ('+45c', 'pnl_s5_H')):
            out = [nm_]
            for dd in (ISd, OOd):
                num = den = 0.0; cnt = 0
                for (d, mm, ll_), r in LAD.items():
                    if d in dd and r[col] != '': num += float(r[col]); den += float(r['cost']); cnt += 1
                out.append('n=%d EVw=%.4f' % (cnt, num / den if den else float('nan')))
            print(' | '.join(out))
    except Exception:
        traceback.print_exc()
def lo_is_pos(b): return pct(b)[0] > 0
if __name__ == '__main__':
    main()
