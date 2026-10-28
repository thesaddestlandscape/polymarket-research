#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""formula_r5_28oct/r5f.py - suite sobre rellenos de TODOS los makers (on-chain + registro). Manda PREREG_FORMULA_R5.md.
Uso: r5f.py suite [--days D,D,...] --tag T"""
import sys, os, json, math, time, traceback
import numpy as np
from scipy import stats
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r4_28oct')
import r4
BASE = '/root/polymarket-research/experimentos/5m_barato/formula_r5_28oct/'
COINS = r4.COINS; NC = r4.NC
LINES = []
FK = ('T', 'rhat', 'matched', 'coin', 'mk', 'tk', 'tkr', 'swid', 'p', 'sz', 'y', 'swsz', 'swT', 'trem')
IS_D = ['2026-10-%02d' % d for d in range(5, 16)]
OOS_D = ['2026-10-%02d' % d for d in range(16, 26)]
FRESH = ['2026-10-05', '2026-10-06', '2026-10-07', '2026-10-08', '2026-10-26', '2026-10-27']


def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); LINES.append(s)


def inclusion(days):
    conf = ['2026-10-%02d' % d for d in range(19, 26)]
    med = float(np.median([len(np.load(r4.OUT + 'd_%s.npz' % d)['T']) for d in conf]))
    inc = []
    for d in days:
        f = r4.OUT + 'd_%s.npz' % d
        if not os.path.exists(f): P('  %s NO CONSTRUIDO' % d); continue
        z = np.load(f); n = len(z['T']); yc = float(np.isfinite(z['y']).mean()); mc = float(z['matched'].mean())
        ok = (0.65 * med <= n <= 1.35 * med) and yc >= 0.99 and mc >= 0.35
        P('  %s n=%d (mediana ref %.0f) y_cov=%.4f casadas=%.3f -> %s' % (d, n, med, yc, mc, 'INCLUIDO' if ok else 'EXCLUIDO'))
        if ok: inc.append(d)
    return inc


def cl2(D, sm='ALL', gap=300.0):
    m = np.ones(len(D['pr_sz']), bool) if sm == 'ALL' else (D['pr_sd'] == 0)
    if not m.any(): return None
    ex = D['pr_ex'][m]; rec = D['pr_rec'][m]; tk = D['pr_tk'][m]; sd = D['pr_sd'][m]; sz = D['pr_sz'][m]; cn = D['pr_coin'][m]
    o = np.lexsort((ex, sd, tk)); ex, rec, tk, sd, sz, cn = ex[o], rec[o], tk[o], sd[o], sz[o], cn[o]
    new = np.ones(len(ex), bool); new[1:] = (tk[1:] != tk[:-1]) | (sd[1:] != sd[:-1]) | ((ex[1:] - ex[:-1]) > gap)
    cid = np.cumsum(new) - 1; K = int(cid[-1]) + 1
    size = np.bincount(cid, weights=sz, minlength=K); npr = np.bincount(cid, minlength=K).astype(float)
    crec = np.full(K, -np.inf); np.maximum.at(crec, cid, rec)
    cst = np.full(K, np.inf); np.minimum.at(cst, cid, ex); cen = np.full(K, -np.inf); np.maximum.at(cen, cid, ex)
    sell = np.bincount(cid, weights=sz * (sd == 0), minlength=K)
    ccoin = np.zeros(K, np.int8); ccoin[cid] = cn
    return dict(size=size, rec=crec, coin=ccoin, npr=npr, dur=cen - cst, fsell=sell / np.maximum(size, 1e-12))


def st_mask(c, th, rhat, coinq):
    if c is None: return np.zeros(len(rhat), bool)
    k = c['size'] >= th
    if not k.any(): return np.zeros(len(rhat), bool)
    return r4.eval_state(r4.prep_state(c['rec'][k], c['coin'][k], None), rhat, coinq)


def win_stat(t_ev, coin_ev, w_ev, tq, coin_q):
    out = np.zeros(len(tq))
    for c in np.unique(coin_ev):
        m = coin_ev == c; t = t_ev[m]; o = np.argsort(t, kind='stable'); t = t[o]
        cs = np.concatenate([[0.0], np.cumsum(w_ev[m][o])]) if w_ev is not None else np.arange(len(t) + 1, dtype=float)
        mq = np.nonzero(coin_q == c)[0]
        if len(mq) == 0: continue
        a = np.searchsorted(t, tq[mq] - 5000.0, 'right'); b = np.searchsorted(t, tq[mq] - 60000.0, 'right')
        out[mq] = cs[a] - cs[b]
    return out


def dev_day(S, num, den):
    if S.sum() == 0 or (~S).sum() == 0: return np.nan
    d1 = den[S].sum(); d0 = den[~S].sum()
    if d1 <= 0 or d0 <= 0: return np.nan
    return num[S].sum() / d1 - num[~S].sum() / d0


def holm(p):
    p = np.where(np.isfinite(p), p, 1.0); m = len(p); o = np.argsort(p); adj = np.empty(m); run = 0.0
    for r, i in enumerate(o): run = max(run, min(1.0, (m - r) * p[i])); adj[i] = run
    return adj


def mkboot(X, S, mask, B=1000, seed=7):
    rng = np.random.default_rng(seed)
    if mask.sum() == 0: return np.nan, (np.nan, np.nan), 0
    u, inv = np.unique(X['mk'][mask], return_inverse=True); K = len(u)
    n1 = np.bincount(inv, weights=(X['num'] * S)[mask], minlength=K); d1 = np.bincount(inv, weights=(X['den'] * S)[mask], minlength=K)
    n0 = np.bincount(inv, weights=(X['num'] * (~S))[mask], minlength=K); d0 = np.bincount(inv, weights=(X['den'] * (~S))[mask], minlength=K)
    est = n1.sum() / d1.sum() - n0.sum() / d0.sum() if d1.sum() > 0 and d0.sum() > 0 else np.nan
    out = np.empty(B)
    for b in range(B):
        ix = rng.integers(0, K, K); a1 = d1[ix].sum(); a0 = d0[ix].sum()
        out[b] = (n1[ix].sum() / a1 - n0[ix].sum() / a0) if a1 > 0 and a0 > 0 else np.nan
    return est, tuple(np.nanpercentile(out, [5, 95])), K


def summ(label, X, S, pop=None, dsel=None, show=True):
    nd = X['nd']; d = X['d']
    m = np.ones(len(d), bool) if pop is None else pop
    if dsel is not None: m = m & np.isin(d, dsel)
    e1, e0, dv, d1, d0 = r4.dday(S, X['num'], X['den'], d, nd, m)
    sel = np.arange(nd) if dsel is None else np.asarray(dsel, int)
    v = dv[sel]; v = v[np.isfinite(v)]
    mu, lo, hi = r4.tci(v)
    nS = int((S & m).sum()); nm = int(m.sum()); covn = nS / max(nm, 1)
    cove = float((X['den'] * (S & m)).sum() / max((X['den'] * m).sum(), 1e-12))
    n1 = (X['num'] * (S & m)).sum(); dd1 = (X['den'] * (S & m)).sum(); n0 = (X['num'] * ((~S) & m)).sum(); dd0 = (X['den'] * ((~S) & m)).sum()
    pooled = (n1 / dd1 - n0 / dd0) if dd1 > 0 and dd0 > 0 else np.nan
    ev1 = n1 / dd1 if dd1 > 0 else np.nan
    if len(v) > 1 and np.isfinite(mu):
        se = v.std(ddof=1) / math.sqrt(len(v)); tt = mu / se if se > 0 else 0.0; pv = float(1 - stats.t.cdf(tt, len(v) - 1)); sd = float(v.std(ddof=1))
    else: pv = np.nan; sd = np.nan
    r = dict(label=label, nS=nS, covn=covn, cove=cove, mu=mu, lo=lo, hi=hi, pos=int((v > 0).sum()), nv=len(v), pooled=pooled, ev1=ev1, p=pv, sd=sd)
    if show: P('%-42s nS=%7d cov %.3f/%.3f dEV/E dia %+.3f IC90[%+.3f,%+.3f] +%d/%d agreg %+.3f EV(S) %+.3f p=%.3f' % (label, nS, covn, cove, mu, lo, hi, r['pos'], r['nv'], pooled, ev1, pv))
    return r


def suite(days0, tag):
    P('== SUITE R5 (rellenos de TODOS los makers; EV/E ponderado por EUR, bruto de comision; reloj de recepcion) | inclusion mecanica = regla de ext_dias.py de R4')
    days = inclusion(days0); nd = len(days)
    P('dias incluidos (%d): %s' % (nd, ','.join(dd[-2:] for dd in days)))
    isn = [i for i, dd in enumerate(days) if dd in IS_D]
    isel = lambda names: [i for i, dd in enumerate(days) if dd in names]
    szc = {cc: [] for cc in range(NC)}
    for i in isn:
        c = cl2(r4.load_day(days[i]), 'ALL')
        for cc in range(NC): szc[cc].append(c['size'][c['coin'] == cc])
    szc = {cc: (np.concatenate(szc[cc]) if szc[cc] else np.zeros(0)) for cc in range(NC)}
    qstar = float((szc[0] < 800.0).mean()) if len(szc[0]) else 0.9
    theta = np.full(NC, np.inf)
    for cc in range(NC):
        if len(szc[cc]) >= 300: theta[cc] = float(np.quantile(szc[cc], qstar))
    P('umbral relativo por moneda (percentil de 800 acc en clusters BTC de los dias IS = %.4f): %s'
      % (qstar, ' '.join('%s=%s(n=%d)' % (COINS[cc], ('%.0f' % theta[cc]) if np.isfinite(theta[cc]) else 'NA', len(szc[cc])) for cc in range(NC))))
    SP = [(sm, th) for sm in ('ALL', 'SELL') for th in (100., 200., 400., 800., 1600., 3200.)]
    DEVm = np.full((len(SP), nd), np.nan); COVm = np.zeros((len(SP), nd))
    keys = ('d', 'coin', 'mk', 'p', 'sz', 'y', 'trem', 'S8', 'S8s', 'Sch2', 'Sch8', 'V', 'Vb', 'n2', 'Srel')
    A = {k: [] for k in keys}; CW = []
    for i, day in enumerate(days):
        D = r4.load_day(day); ok = np.isfinite(D['y']); F = {k: D[k][ok] for k in FK}
        num = F['sz'] * (F['y'] - F['p']); den = F['sz'] * F['p']
        cA = cl2(D, 'ALL'); cS = cl2(D, 'SELL')
        for k, (sm, th) in enumerate(SP):
            Sm = st_mask(cA if sm == 'ALL' else cS, th, F['rhat'], F['coin'])
            DEVm[k, i] = dev_day(Sm, num, den); COVm[k, i] = Sm.mean()
        S8 = st_mask(cA, 800.0, F['rhat'], F['coin']); S8s = st_mask(cS, 800.0, F['rhat'], F['coin'])
        Sch2 = r4.eval_state(r4.prep_state(*r4.events_chain(D, 200.0)), F['T'] * 1000.0, F['coin'])
        Sch8 = r4.eval_state(r4.prep_state(*r4.events_chain(D, 800.0)), F['T'] * 1000.0, F['coin'])
        V = win_stat(D['pr_rec'], D['pr_coin'], D['pr_sz'], F['rhat'], F['coin'])
        m0 = D['pr_coin'] == 0
        Vb = win_stat(D['pr_rec'][m0], np.zeros(int(m0.sum()), np.int8), D['pr_sz'][m0], F['rhat'], np.zeros(len(F['rhat']), np.int8))
        k2 = cA['size'] >= 200.0
        n2 = win_stat(cA['rec'][k2], cA['coin'][k2], None, F['rhat'], F['coin'])
        kr = cA['size'] >= theta[cA['coin']]
        Srel = r4.eval_state(r4.prep_state(cA['rec'][kr], cA['coin'][kr], None), F['rhat'], F['coin']) if kr.any() else np.zeros(len(den), bool)
        base = dict(d=np.full(len(den), i), coin=F['coin'], mk=F['mk'], p=F['p'], sz=F['sz'], y=F['y'], trem=F['trem'], S8=S8, S8s=S8s, Sch2=Sch2, Sch8=Sch8, V=V, Vb=Vb, n2=n2, Srel=Srel)
        for k in keys: A[k].append(base[k])
        K8 = np.nonzero(cA['size'] >= 800.0)[0]
        if len(K8):
            cwn = np.zeros(len(K8)); cwd = np.zeros(len(K8))
            for cc in np.unique(cA['coin'][K8]):
                mf = np.nonzero(F['coin'] == cc)[0]
                if len(mf) == 0: continue
                o = np.argsort(F['rhat'][mf], kind='stable'); tf = F['rhat'][mf][o]
                csn = np.concatenate([[0.0], np.cumsum(num[mf][o])]); csd = np.concatenate([[0.0], np.cumsum(den[mf][o])])
                kk = np.nonzero(cA['coin'][K8] == cc)[0]
                a = np.searchsorted(tf, cA['rec'][K8][kk] + 5000.0, 'left'); b = np.searchsorted(tf, cA['rec'][K8][kk] + 60000.0, 'left')
                cwn[kk] = csn[b] - csn[a]; cwd[kk] = csd[b] - csd[a]
            CW.append(np.column_stack([np.full(len(K8), i), cA['coin'][K8], cA['size'][K8], cA['npr'][K8], cA['fsell'][K8], cA['dur'][K8], cwn, cwd]))
    X = {k: np.concatenate(A[k]) for k in keys}
    X['nd'] = nd; X['num'] = X['sz'] * (X['y'] - X['p']); X['den'] = X['sz'] * X['p']; d = X['d']
    R4S = [dd for dd in days if '2026-10-09' <= dd <= '2026-10-25']

    def s1():
        P('\n-- 1. dEV/E diario de S800 (hueco 300 ms, ventana (5,60] s, recepcion): todas las monedas | BTC')
        e1, e0, dv, d1, d0 = r4.dday(X['S8'], X['num'], X['den'], d, nd)
        _, _, dvb, _, _ = r4.dday(X['S8'], X['num'], X['den'], d, nd, X['coin'] == 0)
        for i, day in enumerate(days):
            P('   %s %s todas %+.3f | BTC %+.3f | cobertura n %.3f' % (day, '(FRESCO)' if day in FRESH else '        ', dv[i], dvb[i], (X['S8'] & (d == i)).sum() / max(1, (d == i).sum())))
        for lab, names in (('R4 09-25', R4S), ('05-08 (nuevos m5_onchain)', [dd for dd in days if dd <= '2026-10-08']), ('05-25', [dd for dd in days if dd <= '2026-10-25']), ('todos incl. 26-27', days)):
            ix = isel(names)
            if ix: summ('S800 todas | ' + lab, X, X['S8'], None, ix); summ('S800 BTC   | ' + lab, X, X['S8'], X['coin'] == 0, ix)
    def s2():
        P('\n-- 2. SELECCION ANIDADA (walk-forward) de S entre %d especificaciones (modo ALL/SELL x umbral); >=8 dias de entrenamiento; cobertura pasada 5-60 %%' % len(SP))
        for name in ('naive_media', 'prudente_lo90', 'fijo_ALL800'):
            ser = []; picks = []; covs = []
            for j in range(8, nd):
                past = DEVm[:, :j]; covp = COVm[:, :j].mean(1); n_ = np.isfinite(past).sum(1)
                valid = (n_ >= 6) & (covp >= 0.05) & (covp <= 0.60)
                if name == 'fijo_ALL800': k = SP.index(('ALL', 800.0))
                else:
                    if not valid.any(): continue
                    mu_ = np.nanmean(past, 1); sd_ = np.nanstd(past, 1, ddof=1)
                    sc = mu_ if name == 'naive_media' else mu_ - stats.t.ppf(0.95, np.maximum(n_ - 1, 1)) * sd_ / np.sqrt(np.maximum(n_, 1))
                    k = int(np.argmax(np.where(valid, sc, -np.inf)))
                ser.append(DEVm[k, j]); picks.append(k); covs.append(COVm[k, j])
            v = np.array(ser, float); v = v[np.isfinite(v)]; mu, lo, hi = r4.tci(v)
            from collections import Counter
            P('   %-14s dEV/E dia medio %+.3f IC90[%+.3f,%+.3f] dias+ %d/%d | cobertura media elegida %.3f | elecciones %s'
              % (name, mu, lo, hi, int((v > 0).sum()), len(v), float(np.mean(covs)) if covs else float('nan'), {('%s%d' % (SP[k][0][:1], SP[k][1])): c for k, c in Counter(picks).most_common(4)}))
        mm = np.nanmean(DEVm, 1); kb = int(np.nanargmax(mm))
        P('   (referencia sesgada: mejor celda A POSTERIORI %s%d con media %+.3f sobre los %d dias; las medias de todas las celdas: %s)'
          % (SP[kb][0][:1], SP[kb][1], mm[kb], nd, ' '.join('%s%d:%+.3f' % (s[0][:1], s[1], m_) for s, m_ in zip(SP, mm))))
    def s3():
        P('\n-- 3. FAMILIA DE ESTADOS COMPLEMENTARIOS (16, prerregistrada, sin eleccion): dEV/E de cada estado vs el resto; Holm sobre los 16')
        edges = [1e-9, 200.0, 800.0, 3200.0, 12800.0]
        bV = np.digitize(X['V'], edges); bN = np.digitize(X['n2'], [1, 2, 4]); bB = np.digitize(X['Vb'], edges)
        nmV = ['V=0', 'V(0,200)', 'V[200,800)', 'V[800,3200)', 'V[3200,12800)', 'V>=12800']
        fs = [('flujo propio ' + nmV[k], bV == k, None) for k in range(6)]
        fs += [('barridos>=200 ' + nm, bN == k, None) for k, nm in enumerate(['n=0', 'n=1', 'n=2-3', 'n>=4'])]
        fs += [('BTC-lider ' + nmV[k] + ' (monedas no BTC)', bB == k, X['coin'] != 0) for k in range(6)]
        res = [summ(nm, X, S, pop, None, show=False) for nm, S, pop in fs]
        ph = holm(np.array([r['p'] for r in res]))
        for r, pa in zip(res, ph): P('   %-44s nS=%8d cov %.3f/%.3f dEV/E %+.3f IC90[%+.3f,%+.3f] +%d/%d p=%.3f pHolm=%.3f' % (r['label'], r['nS'], r['covn'], r['cove'], r['mu'], r['lo'], r['hi'], r['pos'], r['nv'], r['p'], pa))
        P('   cobertura acumulada (umbral de flujo propio, anidado):')
        for th in (200.0, 800.0, 3200.0, 12800.0): summ('   flujo propio >= %g acc' % th, X, X['V'] >= th)
    def s4():
        P('\n-- 4. RESTRICCION prerregistrada BTC y T_rem en [120,240) s: IC por dia y por MERCADO')
        popR = (X['coin'] == 0) & (X['trem'] >= 120.0) & (X['trem'] < 240.0)
        for lab, names in (('09-25 (donde se vio)', R4S), ('FRESCOS (05-08 y 26-27)', [dd for dd in days if dd in FRESH]), ('todos', days)):
            ix = isel(names)
            if not ix: continue
            summ('S800 BTC T120-240 | ' + lab, X, X['S8'], popR, ix)
            est, ci, K_ = mkboot(X, X['S8'], popR & np.isin(d, ix))
            P('       bootstrap por mercado (%d mercados): dEV %+.3f IC90 [%+.3f,%+.3f]' % (K_, est, ci[0], ci[1]))
        for lo_, hi_ in ((0, 60), (60, 120), (120, 180), (180, 240), (240, 301)): summ('S800 BTC T[%d,%d) | todos' % (lo_, hi_), X, X['S8'], (X['coin'] == 0) & (X['trem'] >= lo_) & (X['trem'] < hi_))
    def s5():
        P('\n-- 5. TAMANO del relleno (BTC; S800 vs no-S dentro de cada tramo de tamano)')
        for lo_, hi_ in ((0, 5), (5, 20), (20, 100), (100, 500), (500, 1e12)): summ('BTC sz[%g,%g)' % (lo_, hi_), X, X['S8'], (X['coin'] == 0) & (X['sz'] >= lo_) & (X['sz'] < hi_))
        for lo_, hi_ in ((0.09, 0.15), (0.15, 0.20), (0.20, 0.25), (0.25, 0.31)): summ('BTC precio[%.2f,%.2f)' % (lo_, hi_), X, X['S8'], (X['coin'] == 0) & (X['p'] >= lo_) & (X['p'] < hi_))
    def s6():
        P('\n-- 6. POR QUE S_reg REPLICA Y S_chain NO')
        for lab, m in (('reg y chain', X['S8'] & X['Sch2']), ('solo reg', X['S8'] & ~X['Sch2']), ('solo chain', ~X['S8'] & X['Sch2']), ('ninguno', ~X['S8'] & ~X['Sch2'])):
            P('   celda %-12s fills %.3f del total, EUR %.3f, EV/E %+.3f' % (lab, m.mean(), X['den'][m].sum() / X['den'].sum(), X['num'][m].sum() / max(X['den'][m].sum(), 1e-12)))
        for lab, S in (('S_reg800 ALL (registro, recepcion)', X['S8']), ('S_reg800 SOLO venta barata', X['S8s']), ('S_chain>=200 (tx,tomador,token; bloque)', X['Sch2']), ('S_chain>=800', X['Sch8'])): summ(lab, X, S)
        CWa = np.concatenate(CW); selB = CWa[:, 1] == 0
        P('   EV/E de fills fuera de S800 (referencia): %+.3f ; clusters>=800: %d (BTC %d)' % (X['num'][~X['S8']].sum() / X['den'][~X['S8']].sum(), len(CWa), int(selB.sum())))
        def ctab(name, x, edges):
            cells = []
            for lo_, hi_ in zip(edges[:-1], edges[1:]):
                k = selB & (x >= lo_) & (x < hi_)
                if k.sum() == 0: continue
                cells.append('[%g,%g): n=%d EV %+.3f (EUR %.0f)' % (lo_, hi_, int(k.sum()), CWa[k, 6].sum() / max(CWa[k, 7].sum(), 1e-12), CWa[k, 7].sum()))
            P('   EV de los fills en (5,60] s tras cada barrido BTC, por %s: ' % name + ' | '.join(cells))
        ctab('n de impresiones', CWa[:, 3], [1, 3, 11, 51, 1e9]); ctab('fraccion de venta barata', CWa[:, 4], [0, 0.2, 0.8, 1.01])
        ctab('duracion ms', CWa[:, 5], [0, 1000, 5000, 1e12]); ctab('tamano acc', CWa[:, 2], [800, 1600, 3200, 1e9])
    def s7():
        P('\n-- 7. POR MONEDA con umbral relativo fijado en IS (sin desenlaces); S_rel vs no-S dentro de la moneda')
        for cc in range(NC):
            if not np.isfinite(theta[cc]): continue
            pop = X['coin'] == cc
            if (X['Srel'] & pop).sum() == 0: continue
            r = summ('%s theta=%.0f | todos' % (COINS[cc], theta[cc]), X, X['Srel'], pop)
            summ('%s theta=%.0f | OOS 16-25' % (COINS[cc], theta[cc]), X, X['Srel'], pop, isel(OOS_D))
            est, ci, K_ = mkboot(X, X['Srel'], pop)
            nreq = (1.645 * r['sd'] / r['mu']) ** 2 if (r['mu'] and r['mu'] > 0 and np.isfinite(r['sd'])) else float('inf')
            P('       mercados %d | bootstrap por mercado dEV %+.3f IC90[%+.3f,%+.3f] | dias necesarios para t>1,645 con esta media/sd: %s (disponibles %d)' % (K_, est, ci[0], ci[1], ('%.0f' % nreq) if np.isfinite(nreq) else 'n/a (media<=0)', r['nv']))
    for nm, fn in (('s1', s1), ('s2', s2), ('s3', s3), ('s4', s4), ('s5', s5), ('s6', s6), ('s7', s7)):
        try: fn()
        except Exception: P('ERROR en %s: %s' % (nm, traceback.format_exc()[-1500:]))


if __name__ == '__main__':
    t0 = time.time(); a = sys.argv; tag = a[a.index('--tag') + 1] if '--tag' in a else 'x'
    try:
        days = a[a.index('--days') + 1].split(',') if '--days' in a else ['2026-10-%02d' % k for k in range(5, 28)]
        suite(days, tag)
    except Exception: P('ERROR', traceback.format_exc()[-3000:])
    P('fin suite %.0f s' % (time.time() - t0))
    open(BASE + 'salida_suite_%s.txt' % tag, 'w').write('\n'.join(LINES) + '\n')
