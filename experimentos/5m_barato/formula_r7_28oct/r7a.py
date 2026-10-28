#!/usr/bin/env python3
"""formula_r7_28oct/r7a.py - bloques A (puja profunda armada), B (predictor), D (dosis-respuesta continua). Manda PREREG_FORMULA_R7.md."""
import sys, os, json, math, time, io, contextlib
import numpy as np
from scipy import stats
E4 = '/root/polymarket-research/experimentos/5m_barato/'
for d in ('formula_r6_28oct', 'formula_r5_28oct', 'formula_r4_28oct', 'formula_r3_28oct'): sys.path.insert(0, E4 + d)
import r4, r5f, r6a
from r6a import summ, F, P, signflip_max, load as load6
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
BASE = E4 + 'formula_r7_28oct/'; EXT = E4 + 'formula_r5_28oct/ext/'
rng = np.random.default_rng(6281)
XS = (100, 200, 400); MS = (3, 4); LATS = (68.0, 150.0, 300.0); LIFE = 10000.0; NACC = 10.0; DEC = 5.0; CLK = 26.0
FEATS = ['cum', 'npr', 'dur', 'rate', 'nlev', 'p_k', 'drop', 'spread', 'bs', 'cbb', 'dcbb', 'm15', 'trem', 'hour', 'adv', 'jd_since', 'ju_since']
def stream(u, comp, plo, phi, pt, pex, ppx, psz, psd):
    a, b = int(plo[u]), int(phi[u]); m = psd[a:b] == 0
    t = [pt[a:b][m]]; e = [pex[a:b][m]]; p = [np.round(ppx[a:b][m], 2)]; s = [psz[a:b][m]]; c = int(comp[u])
    if c >= 0:
        a2, b2 = int(plo[c]), int(phi[c]); m2 = psd[a2:b2] == 1
        t.append(pt[a2:b2][m2]); e.append(pex[a2:b2][m2]); p.append(np.round(1.0 - ppx[a2:b2][m2], 2)); s.append(psz[a2:b2][m2])
    t = np.concatenate(t); o = np.argsort(t, kind='stable')
    return t[o], np.concatenate(e)[o], np.concatenate(p)[o], np.concatenate(s)[o]
def lastq(qt_u, t): return int(np.searchsorted(qt_u, t, 'right')) - 1
def fillsrch(st, sp, ta, tgt, life=LIFE):
    i0 = int(np.searchsorted(st, ta + CLK, 'left')); i1 = int(np.searchsorted(st, ta + CLK + life, 'left'))
    if i1 <= i0: return -1
    hit = np.flatnonzero(sp[i0:i1] < tgt - 1e-9)
    return (i0 + int(hit[0])) if len(hit) else -1
def day_events(day, di, G):
    z = np.load(EXT + 'b_%s.npz' % day); Z = {k: z[k] for k in z.files}
    cie = Z['tok_cie']; side = Z['tok_side']; comp = Z['tok_comp']; mks = Z['tok_mk']; n = len(cie)
    qt, qtok, qbb, qba, qbs = Z['qt'], Z['qtok'], Z['qbb'], Z['qba'], Z['qbs']
    pt, ptok, pex, ppx, psz, psd = Z['pt'], Z['ptok'], Z['pex'], Z['ppx'], Z['psz'], Z['psd']
    ids = np.arange(n); qlo = np.searchsorted(qtok, ids, 'left'); qhi = np.searchsorted(qtok, ids, 'right'); plo = np.searchsorted(ptok, ids, 'left'); phi = np.searchsorted(ptok, ids, 'right')
    jd = np.sort(Z['jd']); ju = np.sort(Z['ju'])
    kz = np.load(BASE + 'k15/k_%s.npz' % day) if os.path.exists(BASE + 'k15/k_%s.npz' % day) else None
    if kz is not None:
        kst = kz['kstart']; ksd = kz['kside']; kqk = kz['qk']; kqt = kz['qt']; kbb = kz['qbb']; kmap = {(int(ksd[i]), int(kst[i])): i for i in range(len(kst))}
        klo = np.searchsorted(kqk, np.arange(len(kst)), 'left'); khi = np.searchsorted(kqk, np.arange(len(kst)), 'right')
    def bid15(u, t):
        if kz is None: return np.nan
        s5 = float(cie[u]) - 300.0; i = kmap.get((int(side[u]), int(s5 // 900 * 900)))
        if i is None or khi[i] <= klo[i]: return np.nan
        j = int(np.searchsorted(kqt[klo[i]:khi[i]], t, 'right')) - 1
        return float(kbb[klo[i] + j]) if j >= 0 else np.nan
    def q1(u, t):
        a, b = int(qlo[u]), int(qhi[u])
        if b <= a: return None
        j = int(np.searchsorted(qt[a:b], t, 'right')) - 1
        return None if j < 0 else (float(qbb[a + j]), float(qba[a + j]), float(qbs[a + j]))
    E = {}  # clave (X,m) -> lista de filas
    PL = {m: [] for m in MS}; nev100 = 0; toks = []
    clu = {}
    for u in range(n):
        win = G.get(str(mks[u]))
        if win not in ('YES', 'NO') or qhi[u] <= qlo[u]: continue
        y = 1.0 if win == ('YES' if side[u] == 0 else 'NO') else 0.0
        st, se, sp, ss = stream(u, comp, plo, phi, pt, pex, ppx, psz, psd)
        if len(st) == 0: toks.append((u, y, None)); continue
        newc = np.r_[True, np.diff(se) > 300.0]; cid = np.cumsum(newc) - 1; K = int(cid[-1]) + 1
        starts = np.flatnonzero(newc); ends = np.r_[starts[1:], len(st)]
        tot = np.bincount(cid, weights=ss, minlength=K); cend = np.array([st[e - 1] for e in ends])
        clu[u] = (st, cend[tot >= 100])
        toks.append((u, y, st))
        adv = jd if side[u] == 0 else ju
        for ci in range(K):
            s0, e0 = starts[ci], ends[ci]
            if not (0.10 <= sp[s0] <= 0.35): continue
            cum = np.cumsum(ss[s0:e0]); dur = se[s0:e0] - se[s0]
            for X in XS:
                k = int(np.searchsorted(cum, X, 'left'))
                if k >= len(cum) or dur[k] > 2000.0: continue
                kk = s0 + k; tk = float(st[kk]); pk = float(sp[kk]); td = tk + DEC; r = q1(u, td)
                if r is None: continue
                bb, ba, bs = r; c = int(comp[u]); cb = q1(c, td) if c >= 0 else None; cb1 = q1(c, td - 1000.0) if c >= 0 else None
                b15 = bid15(u, td); prs = sp[s0:kk + 1]
                dl = td - jd[np.searchsorted(jd, td, 'right') - 1] if len(jd) and np.searchsorted(jd, td, 'right') > 0 else 60000.0
                ul = td - ju[np.searchsorted(ju, td, 'right') - 1] if len(ju) and np.searchsorted(ju, td, 'right') > 0 else 60000.0
                ad = dl if side[u] == 0 else ul
                f = [cum[k], k + 1, dur[k], cum[k] / max(dur[k], 50.0) * 1000.0, len(np.unique(prs)), pk, (sp[s0] - pk) / 0.01, ba - bb, bs, (cb[0] if cb else np.nan), ((cb[0] - cb1[0]) if (cb and cb1) else np.nan), b15,
                     float(cie[u]) - td / 1000.0, ((td / 1000.0) % 86400) // 3600, min(ad, 60000.0), min(dl, 60000.0), min(ul, 60000.0)]
                for m in MS:
                    tgt = round(min(bb, pk) - m * 0.01, 2)
                    if not (0.09 - 1e-9 <= tgt <= 0.29 + 1e-9): continue
                    row = dict(di=di, u=u, y=y, tgt=tgt, f=f, tk=tk, s0=s0, kk=kk)
                    for L in LATS:
                        ta = td + L; j = fillsrch(st, sp, ta, tgt)
                        row['j%d' % L] = j; row['tf%d' % L] = float(st[j]) if j >= 0 else np.nan
                    # rasgos tardios (cancelacion): ultima info con >=100 ms antes de tf
                    j = row['j68']
                    if j >= 0:
                        tc = float(st[j]) - 130.0; row['cancelable'] = tc >= td + 68.0
                        if row['cancelable']:
                            l = int(np.searchsorted(st, tc, 'right')) - 1; l = max(l, kk)
                            cs = float(ss[s0:l + 1].sum()); pl = float(sp[l])
                            row['late'] = [cs, l - s0 + 1, (pl - tgt) / 0.01, (tc - float(st[l])), (sp[s0] - pl) / 0.01]
                    E.setdefault((X, m), []).append(row)
                    if X == 100 and m == 3: nev100 += 1
    # placebo (cotizar siempre a esa profundidad en instantes aleatorios sin barrido >=100 en los 60 s previos)
    ok = [t for t in toks if q1(t[0], float(cie[t[0]]) * 1000.0 - 100000.0) is not None]
    for m in MS:
        got = 0; tries = 0; want = 3 * nev100
        while got < want and tries < want * 30 and ok:
            tries += 1; u, y, st = ok[rng.integers(len(ok))]; t = (float(cie[u]) - rng.uniform(10.0, 290.0)) * 1000.0; r = q1(u, t)
            if r is None or not (0.12 <= r[0] <= 0.38): continue
            if u in clu:
                ce = clu[u][1]; i = np.searchsorted(ce, t, 'right') - 1
                if i >= 0 and t - ce[i] < 60000.0: continue
            tgt = round(r[0] - m * 0.01, 2)
            if not (0.09 - 1e-9 <= tgt <= 0.29 + 1e-9): continue
            st2, se2, sp2, ss2 = stream(u, comp, plo, phi, pt, pex, ppx, psz, psd)
            j = fillsrch(st2, sp2, t + DEC + 68.0, tgt) if len(st2) else -1
            PL[m].append(dict(di=di, y=y, tgt=tgt, j68=j)); got += 1
    return E, PL
def tab(rows, key='j68', mask=None):
    di = np.array([r['di'] for r in rows]); y = np.array([r['y'] for r in rows]); tg = np.array([r['tgt'] for r in rows]); fl = np.array([r[key] >= 0 for r in rows])
    return di, y, tg, fl
def evR(di, y, tg, fl):
    return dict(di=di, num=np.where(fl, NACC * (y - tg), 0.0), den=np.where(fl, NACC * tg, 0.0))
def block(rows, key, ds, nd, extra=None):
    di, y, tg, fl = tab(rows, key); R = evR(di, y, tg, fl); m = fl & np.isin(di, ds) if extra is None else fl & np.isin(di, ds) & extra
    s = summ(R, m, ds, nd); nev = int(np.isin(di, ds).sum()); nfl = int((fl & np.isin(di, ds)).sum())
    return s, nev, nfl
def main():
    t0 = time.time(); G = json.load(open(r4.I.CACHE)); days0 = sorted(f[2:12] for f in os.listdir(E4 + 'formula_r6_28oct/fills') if f.startswith('f_'))
    with contextlib.redirect_stdout(io.StringIO()): days = r5f.inclusion(days0)
    nd = len(days); dd = lambda lo, hi: [i for i, d in enumerate(days) if lo <= int(d[-2:]) <= hi]
    IS, OOS, DEV = dd(6, 15), dd(16, 25), dd(26, 27); OOS2 = dd(16, 27)
    ALL = {}; PLA = {m: [] for m in MS}
    for di, d in enumerate(days):
        E, PL = day_events(d, di, G)
        for k, v in E.items(): ALL.setdefault(k, []).extend(v)
        for m in MS: PLA[m].extend(PL[m])
        print(d, {k: len(v) for k, v in E.items() if k[1] == 3}, '%.0f s' % (time.time() - t0), flush=True)
    P('== R7 A: puja profunda armada (N=10 acc, vida 10 s, relleno estricto por travesia, latencia GTC 68 ms; EUR flujo S800-BTC 48.847/d)')
    FS = 48847.0; V = []; labs = []
    for X in XS:
        for m in MS:
            rows = ALL.get((X, m), [])
            di, y, tg, fl = tab(rows); R = evR(di, y, tg, fl); e, d_, _ = r6a.dayev(R, fl, nd); V.append([e[i] if d_[i] > 0 else np.nan for i in IS]); labs.append((X, m))
    lo = np.array([r4.tci(np.array(v)[np.isfinite(v)])[1] if np.isfinite(v).sum() > 2 else -9 for v in V]); j = int(np.argmax(lo)); obs, nm = signflip_max(np.array(V)); pj = (nm >= obs[j]).mean()
    P('  variantes (X,m): IS cota inf IC90: ' + ' '.join('%s:%+.3f' % (str(l), x) for l, x in zip(labs, lo)) + ' | elegida %s, p max-stat %.3f' % (str(labs[j]), pj))
    for (X, m) in labs:
        rows = ALL.get((X, m), [])
        for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
            s, nev, nfl = block(rows, 'j68', ds, nd)
            P('  X=%d m=%d %-3s eventos/d %.0f relleno %.1f %% | %s | cuota %.2f %%' % (X, m, pn, nev / len(ds), 100 * nfl / max(1, nev), F(s), 100 * (s['eurd'] / FS if s else 0)))
    X, m = labs[j]; rows = ALL[(X, m)]
    P('  -- elegida %s: latencia (OOS 16-25)' % str(labs[j]))
    for L in LATS:
        s, nev, nfl = block(rows, 'j%d' % L, OOS, nd); P('     GTC %d ms: relleno %.1f %% | %s' % (L, 100 * nfl / max(1, nev), F(s)))
    for m2 in MS:
        for pn, ds in (('IS', IS), ('OOS', OOS)):
            s, nev, nfl = block(PLA[m2], 'j68', ds, nd); P('  PLACEBO cotizar siempre m=%d %s: relleno %.1f %% | %s' % (m2, pn, 100 * nfl / max(1, nev), F(s)))
    di, y, tg, fl = tab(rows); m15 = np.array([r['f'][11] for r in rows]); mg = m15 - tg
    for lab, ex in (('margen15<=0', mg <= 0), ('0<margen15<=0,10', (mg > 0) & (mg <= 0.10)), ('margen15>0,10', mg > 0.10), ('sin 15m', np.isnan(mg))):
        for pn, ds in (('IS', IS), ('OOS', OOS2)):
            s, nev, nfl = block(rows, 'j68', ds, nd, ex); P('  covariable 15m %-18s %-3s: eventos %d rellenos %d | %s' % (lab, pn, int((np.isin(di, ds) & ex).sum()), nfl, F(s)))
    # ---- B
    P('\n== R7 B: predictor (X=100, m=3, todos los eventos armados; entrenado IS 06-15, AUC en OOS 16-27)')
    rows = ALL[(100, 3)]; Xf = np.array([r['f'] for r in rows], float); di, y, tg, fl = tab(rows); isI = np.isin(di, IS); isO = np.isin(di, OOS2)
    def prep(A): 
        B = np.where(np.isnan(A), 0.0, A); return np.hstack([B, np.isnan(A).astype(float)[:, [FEATS.index('cbb'), FEATS.index('dcbb'), FEATS.index('m15')]]])
    def boot_auc(yt, sc, dayv):
        ud = np.unique(dayv); out = []
        for _ in range(200):
            pick = rng.choice(ud, len(ud)); idx = np.concatenate([np.flatnonzero(dayv == dd_) for dd_ in pick])
            if len(np.unique(yt[idx])) == 2: out.append(roc_auc_score(yt[idx], sc[idx]))
        return np.percentile(out, [5, 95])
    for nm_, tgtv, sel in (('Y1 continua (relleno)', fl.astype(int), np.ones(len(rows), bool)), ('Y2 gana|relleno', y.astype(int), fl)):
        tr = isI & sel; te = isO & sel
        if tr.sum() < 100 or te.sum() < 100 or len(np.unique(tgtv[tr])) < 2: P('  %s: muestra insuficiente (%d/%d)' % (nm_, tr.sum(), te.sum())); continue
        sc = StandardScaler().fit(prep(Xf[tr])); lr = LogisticRegression(max_iter=500, C=0.3).fit(sc.transform(prep(Xf[tr])), tgtv[tr]); p1 = lr.predict_proba(sc.transform(prep(Xf[te])))[:, 1]
        hg = HistGradientBoostingClassifier(max_iter=150, learning_rate=0.08, max_depth=4, random_state=1).fit(Xf[tr], tgtv[tr]); p2 = hg.predict_proba(Xf[te])[:, 1]
        pr = np.array([rng.permutation(p2[di[te] == dd_]) for dd_ in []], object) if False else None
        null = []
        for _ in range(100):
            ps = p2.copy()
            for dd_ in np.unique(di[te]): ix = np.flatnonzero(di[te] == dd_); ps[ix] = rng.permutation(p2[ix])
            null.append(roc_auc_score(tgtv[te], ps))
        P('  %s: n_IS=%d n_OOS=%d base %.3f | AUC logit %.3f HGB %.3f IC90 dias HGB [%.3f,%.3f] | nulo permutado %.3f' % (nm_, tr.sum(), te.sum(), tgtv[te].mean(), roc_auc_score(tgtv[te], p1), roc_auc_score(tgtv[te], p2), *boot_auc(tgtv[te], p2, di[te]), np.mean(null)))
        if nm_.startswith('Y2'):
            # filtro: umbral elegido con predicciones fuera-de-muestra por dia en IS
            from sklearn.model_selection import GroupKFold
            idx = np.flatnonzero(tr); oof = np.zeros(len(idx))
            for a, b in GroupKFold(5).split(idx, groups=di[idx]):
                h = HistGradientBoostingClassifier(max_iter=150, learning_rate=0.08, max_depth=4, random_state=1).fit(Xf[idx[a]], tgtv[idx[a]]); oof[b] = h.predict_proba(Xf[idx[b]])[:, 1]
            pnl_i = NACC * (y[idx] - tg[idx]); best = None
            for q in np.linspace(0.0, 0.6, 13):
                th = np.quantile(oof, q); keep = oof >= th; v = pnl_i[keep].sum()
                if keep.mean() >= 0.4 and (best is None or v > best[1]): best = (th, v, q)
            th = best[0]; keep = p2 >= th; pn = NACC * (y[te] - tg[te]); cs = NACC * tg[te]
            P('  filtro P(gana|relleno)>=%.3f (cuantil IS %.2f, conserva %.0f %% en OOS): EV/E %+.3f frente a sin filtro %+.3f; pnl total %+.1f vs %+.1f EUR (n=%d rellenos OOS)' % (th, best[2], 100 * keep.mean(), pn[keep].sum() / cs[keep].sum(), pn.sum() / cs.sum(), pn[keep].sum(), pn.sum(), te.sum()))
            keep_d = np.array([ (pn[(di[te] == dd_) & keep].sum() / max(1e-9, cs[(di[te] == dd_) & keep].sum())) for dd_ in np.unique(di[te])]); P('     por dias: %s' % F(summ(dict(di=di[te], num=np.where(keep, pn, 0.0), den=np.where(keep, cs, 0.0)), keep, list(np.unique(di[te])), nd)))
            # cancelacion tardia
            canc = np.array([bool(r.get('cancelable', False)) and r['j68'] >= 0 for r in rows])
            Lf = np.array([r['late'] if canc[i] else [np.nan] * 5 for i, r in enumerate(rows)], float); XL = np.hstack([Xf, Lf])
            trc = isI & canc; tec = isO & canc
            if trc.sum() > 100 and tec.sum() > 100 and len(np.unique(y[trc])) == 2:
                h = HistGradientBoostingClassifier(max_iter=150, learning_rate=0.08, max_depth=4, random_state=1).fit(XL[trc], y[trc].astype(int)); pc = h.predict_proba(XL[tec])[:, 1]
                idc = np.flatnonzero(trc); oofc = np.zeros(len(idc))
                for a, b in GroupKFold(5).split(idc, groups=di[idc]):
                    hh = HistGradientBoostingClassifier(max_iter=150, learning_rate=0.08, max_depth=4, random_state=1).fit(XL[idc[a]], y[idc[a]].astype(int)); oofc[b] = hh.predict_proba(XL[idc[b]])[:, 1]
                pnl_c = NACC * (y[idc] - tg[idc]); bb_ = (None, -1e18)
                for q in np.linspace(0.0, 0.5, 11):
                    th2 = np.quantile(oofc, q); v = pnl_c[oofc >= th2].sum()
                    if v > bb_[1]: bb_ = (th2, v)
                pnt = NACC * (y[tec] - tg[tec]); kc = pc >= bb_[0]; orac = -pnt[pnt < 0].sum(); ahorro = pnt[kc].sum() - pnt.sum()
                P('  CANCELACION TARDIA (rasgos hasta fill-130 ms; cancelables %d de %d rellenos OOS): AUC y|relleno %.3f | ahorro OOS %+.1f EUR (pnl %+.1f -> %+.1f) frente a cota oraculo %.1f EUR (%.0f %% de la cota); base sin cancelar EV/E %+.3f' % (tec.sum(), (isO & (fl)).sum(), roc_auc_score(y[tec].astype(int), pc) if len(np.unique(y[tec])) == 2 else float('nan'), ahorro, pnt.sum(), pnt[kc].sum(), orac, 100 * ahorro / max(1e-9, orac), pnt.sum() / (NACC * tg[tec]).sum()))
    # ---- D dosis-respuesta continua con rellenos reales (R6)
    P('\n== R7 D: dosis-respuesta continua (rellenos de todos los makers, BTC, estado S800)')
    R = load6(days, 0); S = np.isfinite(R['dA']); r_i = (R['y'] - R['p']) / R['p']; w = R['den']
    xs = np.log(np.where(S, R['sA'], 800.0) / 800.0); inw = (R['swsz'] >= 200).astype(float)
    def wls(m):
        Xm = np.vstack([np.ones(m.sum()), xs[m], inw[m]]).T; W = w[m]; b = np.linalg.solve((Xm * W[:, None]).T @ Xm, (Xm * W[:, None]).T @ r_i[m]); return b
    for nm_, ds in (('IS 06-15', IS), ('OOS 16-25', OOS), ('DEV 26-27', DEV)):
        m = S & np.isin(R['di'], ds); b = wls(m)
        bs = []
        for _ in range(200):
            pick = rng.choice(ds, len(ds)); mm = np.concatenate([np.flatnonzero(S & (R['di'] == dd_)) for dd_ in pick]); Xm = np.vstack([np.ones(len(mm)), xs[mm], inw[mm]]).T; W = w[mm]
            try: bs.append(np.linalg.solve((Xm * W[:, None]).T @ Xm, (Xm * W[:, None]).T @ r_i[mm])[1])
            except Exception: pass
        P('  WLS EV/E ~ a + b*log(tam barrido/800) + c*dentro_barrido, %s: a %+.3f b %+.3f IC90 dias [%+.3f,%+.3f] c %+.3f (n=%d)' % (nm_, b[0], b[1], *np.percentile(bs, [5, 95]), b[2], m.sum()))
        if nm_.startswith('IS'): bIS = b
    m = S & np.isin(R['di'], OOS2); pred = bIS[0] + bIS[1] * xs[m] + bIS[2] * inw[m]; ss_res = (w[m] * (r_i[m] - pred) ** 2).sum(); ss_tot = (w[m] * (r_i[m] - np.average(r_i[m], weights=w[m])) ** 2).sum(); ss_c = (w[m] * (r_i[m] - np.average(r_i[S & np.isin(R['di'], IS)], weights=w[S & np.isin(R['di'], IS)])) ** 2).sum()
    P('  R2 OOS ponderado vs media IS: %.4f (modelo) ; (R2 frente a media OOS %.4f)' % (1 - ss_res / ss_c, 1 - ss_res / ss_tot))
    edges = [800, 1000, 1400, 2000, 3000, 5000, 1e9]
    for ctx, cm in (('dentro de barrido', R['swsz'] >= 200), ('post-barrido', R['swsz'] < 200)):
        for k in range(len(edges) - 1):
            mk_ = S & cm & (R['sA'] >= edges[k]) & (R['sA'] < edges[k + 1]); o = []
            for pn, ds in (('IS', IS), ('OOS', OOS2)):
                s = summ(R, mk_, ds, nd); o.append('%s %s' % (pn, ('EVw %+.3f [%+.3f,%+.3f] +%d/%d %.0fEUR/d' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'], s['eurd'])) if s else '-'))
            P('  %-18s tam [%d,%s): %s' % (ctx, edges[k], ('%d' % edges[k + 1]) if edges[k + 1] < 1e8 else 'inf', ' | '.join(o)))
    open(BASE + 'salida_r7a.txt', 'w').write('\n'.join(r6a.LINES)); print('fin %.0f s' % (time.time() - t0))
if __name__ == "__main__": main()
