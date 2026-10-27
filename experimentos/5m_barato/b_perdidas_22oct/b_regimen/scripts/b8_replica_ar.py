#!/usr/bin/env python3
"""b8_replica_ar.py -- ADENDA 4: replica larga de R_AR0 sobre proxies (precio de modelo)."""
import sys, os, numpy as np, pandas as pd
DET = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen'
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
rng = np.random.default_rng(20261028)
def prep(path, wcol):
    D = pd.read_csv(path, usecols=['coin', 'tmin', 'T', 'q', 'lado_up', 'rpre', 'dia', wcol]); U = D[D.coin.isin(['ETH', 'SOL', 'XRP']) & (D['T'] == 180) & D[wcol].notna()].copy()
    U['sd'] = np.where(U.lado_up, 1.0, -1.0); U['cls'] = np.where(U.rpre.abs() < 7.7, 'NEU', np.where(np.sign(U.rpre) == U.sd, 'CON', 'CONTRA')); U['e'] = U[wcol] - U.q
    U = U.sort_values('tmin').reset_index(drop=True); t = U.tmin.values; ce = np.concatenate([[0], np.cumsum(U.e.values)]); cq = np.concatenate([[0], np.cumsum(U.q.values)])
    hi = np.searchsorted(t, t - 5, 'right'); lo = np.searchsorted(t, t - 120, 'left'); n = hi - lo
    U['AR'] = np.where(n >= 20, (ce[hi] - ce[lo]) / np.maximum(cq[hi] - cq[lo], 1e-9), np.nan); U['nAR'] = n; return U
def delta_by(U, mask_fn, nb=3000):
    V = U[U.cls.isin(['CON', 'CONTRA']) & U.AR.notna()]; days = sorted(V.dia.unique()); ix = {d: i for i, d in enumerate(days)}; k = len(days)
    M = np.zeros((k, 2, 2, 2))   # dia, grupo(bajo/alto), clase(CON/CONTRA), (e,q)
    g = mask_fn(V.AR.values)
    for (d, gg, cl), r in V.assign(g=g).groupby(['dia', 'g', 'cls']).agg(e=('e', 'sum'), q=('q', 'sum')).iterrows(): M[ix[d], int(gg), 0 if cl == 'CON' else 1] = (r.e, r.q)
    def st(w):
        s = (M * w[:, None, None, None]).sum(0); ev = s[..., 0] / np.maximum(s[..., 1], 1e-9); D = ev[:, 0] - ev[:, 1]; return D[1] - D[0], D[0], D[1]   # (Delta alto - Delta bajo), Delta_bajo, Delta_alto
    base = st(np.ones(k)); bs = np.array([st(np.bincount(rng.integers(0, k, k), minlength=k).astype(float)) for _ in range(nb)])
    lo, hi = np.nanpercentile(bs[:, 0], [5, 95]); return base, (lo, hi), k, int(((V.AR.values <= 0)).sum())
for nom, (f, w) in {'2025 (349 d, proxy)': ('panel_y2025', 'win_proxy'), 'backfill (129 d, proxy)': ('panel_backfill', 'win_proxy'), 'dic_ene (40 d, oficial)': ('panel_dic_ene', 'win_oficial'), 'bookTicker (29 d, proxy)': ('panel_bookticker', 'win_proxy')}.items():
    U = prep(f'{DET}/datos/{f}.csv.gz', w)
    for cut_nom, fn in (('AR<=0', lambda a: (a > 0).astype(int)), ('AR<=-0,10', lambda a: (a > -0.10).astype(int))):
        (d, dlo, dhi), ic, k, nlow = delta_by(U, fn)
        P(f'{nom} {cut_nom}: dias {k} | Delta(AR bajo) {dlo:+.3f}  Delta(AR alto) {dhi:+.3f}  diferencia (alto-bajo) {d:+.3f} IC90 dias [{ic[0]:+.3f},{ic[1]:+.3f}]   [diferencia>0 => penalizacion mayor cuando AR bajo]')
    P(f'    cobertura AR: {float(U.AR.notna().mean()):.3f}, n medio ventana {float(U.nAR.mean()):.1f}')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos', 'b8_resultados.txt'), 'w').write('\n'.join(OUT))
