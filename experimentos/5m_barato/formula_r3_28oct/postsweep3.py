#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contraste unico de PREREG_POSTSWEEP_R3.md sobre los datos de analysis3.py (22 dias). Post-hoc declarado."""
import sys, numpy as np
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct')
import analysis3 as A
y, dd, coin, fsz, fpx, bbl, oos = A.y, A.dd, A.coin, A.fsz, A.fpx, A.bbl, A.oos
ts = A.C('ts'); key = A.C('mkt').astype(np.int64) * 2 + A.C('yes').astype(np.int64)
ixf = np.nonzero(fsz > 0)[0]; ixf = ixf[np.argsort(ts[ixf], kind='stable')]
_, first = np.unique(key[ixf], return_index=True); ff = ixf[first]
x = bbl + 0.01; rho = 0.2 * 0.07 * x * (1 - x); pnl = y - x + rho; w = np.minimum(fsz, 5.0) / 5.0
fo = A.C('fo30_130'); fc = A.C('fc30_130')
fo_raw = np.sign(fo) * np.expm1(np.abs(fo)); fc_raw = np.sign(fc) * np.expm1(np.abs(fc))
rng = np.random.default_rng(2811)
def ev(sel): return float((w[sel] * pnl[sel]).sum() / w[sel].sum()) if sel.sum() and w[sel].sum() > 0 else float('nan')
def run(th, primary):
    S = (fo_raw <= -th) | (fc_raw <= -th)
    s = S[ff]; f = ff
    cov = s.mean(); d_all = ev(f[s]) - ev(f[~s])
    out = ['umbral %d acc%s: cobertura de S %.1f %% de los primeros rellenos (n=%d; S=%d) | EV/acc S %+.4f vs no-S %+.4f dEV %+.4f' % (th, ' [PRIMARIO]' if primary else '', 100 * cov, len(f), int(s.sum()), ev(f[s]), ev(f[~s]), d_all)]
    for lab, dm in (('22 dias', np.ones(len(f), bool)), ('IS 05-22', ~oos[f]), ('OOS 23-26', oos[f])):
        dl = []
        for d_ in np.unique(dd[f][dm]):
            sel = dm & (dd[f] == d_)
            if (s & sel).sum() >= 5 and (~s & sel).sum() >= 5: dl.append(ev(f[s & sel]) - ev(f[~s & sel]))
        mu, lo, hi = A.tint(dl); out.append('   %-9s dias=%2d dEV medio por dia %+.4f IC90t[%+.4f,%+.4f] (dias con dEV>0: %d)' % (lab, len(dl), mu, lo, hi, int(np.sum(np.array(dl) > 0))))
    strat = coin[f] * 1000 + np.rint(fpx[f] * 100).astype(np.int64)
    us, sid = np.unique(strat, return_inverse=True); kk = np.bincount(sid, weights=s.astype(float), minlength=len(us)).astype(np.int64)
    starts = np.concatenate([[0], np.cumsum(np.bincount(sid, minlength=len(us)))[:-1]]); sims = []
    for _ in range(500):
        order = np.lexsort((rng.random(len(sid)), sid)); rank = np.arange(len(sid)) - starts[sid[order]]
        ps = np.zeros(len(sid), bool); ps[order] = rank < kk[sid[order]]; sims.append(ev(f[ps]) - ev(f[~ps]))
    sims = np.array(sims); out.append('   placebo por precio de relleno: dEV medio %+.4f sd %.4f -> p(dEV_placebo >= observado)=%.3f' % (sims.mean(), sims.std(), (1 + (sims >= d_all).sum()) / 501.0))
    return out
L = ['POSTSWEEP (post-hoc declarado, contraste unico): primeros rellenos %d de %d filas con relleno' % (len(ff), int((fsz > 0).sum()))]
for th, pr in ((200, True), (100, False), (400, False)): L += run(th, pr)
print('\n'.join(L)); open(A.BASE + 'postsweep_salida.txt', 'w').write('\n'.join(L) + '\n')
