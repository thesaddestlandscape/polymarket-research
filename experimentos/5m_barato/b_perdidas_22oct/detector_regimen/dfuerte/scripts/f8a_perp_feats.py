#!/usr/bin/env python3
"""f8a - F11 (perps) por unidad (PREREG_DFUERTE_R3). units_<src>_w2.pkl -> units_<src>_r3.pkl"""
import sys, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
R = '/root/polymarket-research-datalogs/regimen_5m'; D = '/mnt/HC_Volume_106538179/agentes_datos/dfuerte'
F11 = ['basis', 'dbasis15', 'dbasis60', 'zbasis', 'pimb5', 'pimb15', 'pimb60', 'pvol15', 'lvr15', 'retgap15', 'fund', 'ofund', 'afund']
def csum(a): return np.concatenate([[0.0], np.cumsum(np.nan_to_num(a))])
def run(src):
    U = pd.read_pickle(f'{R}/dfuerte/units_{src}_w2.pkl'); zs = np.load(f'{R}/full_{src}.npz'); zp = np.load(f'{D}/perp_{src}.npz'); out = {c: np.full(len(U), np.nan) for c in F11}
    for coin, g in U.groupby('coin'):
        if coin + '_m0' not in zp.files: continue
        m0 = int(zs[coin + '_m0']); S = zs[coin + '_X']; n = len(S); mp = int(zp[coin + '_m0']); Xp = zp[coin + '_X']
        P = np.full((n, 4), np.nan); a = np.arange(n) + m0 - mp; ok = (a >= 0) & (a < len(Xp)); P[ok] = Xp[a[ok]]
        sc = S[:, 0]; pc = P[:, 0]; b = (pc / sc - 1) * 1e4; i = g.tmin.values - m0; o = g.o.values; s60 = g.s60.values
        cb = csum(b); cb2 = csum(b ** 2); cn = np.concatenate([[0], np.cumsum(np.isfinite(b))]).astype(float)
        n24 = cn[i + 1] - cn[i + 1 - 1440]; mu = (cb[i + 1] - cb[i + 1 - 1440]) / np.maximum(n24, 1); var = (cb2[i + 1] - cb2[i + 1 - 1440]) / np.maximum(n24, 1) - mu ** 2
        r = {}; r['basis'] = b[i]; r['dbasis15'] = b[i] - b[i - 15]; r['dbasis60'] = b[i] - b[i - 60]; r['zbasis'] = np.where(n24 > 1000, (b[i] - mu) / np.sqrt(np.maximum(var, 1e-9)), np.nan)
        cv, ct, cs = csum(P[:, 1]), csum(P[:, 2]), csum(S[:, 3]); w = lambda c, k: c[i + 1] - c[i + 1 - k]
        for k in (5, 15, 60): r['pimb%d' % k] = o * (2 * w(ct, k) - w(cv, k)) / np.maximum(w(cv, k), 1e-12)
        r['pvol15'] = w(cv, 15) / np.maximum(w(cv, 1440) / 96, 1e-12); r['lvr15'] = np.log(np.maximum(w(cs, 15), 1e-9) / np.maximum(w(cv, 15), 1e-9))
        r['retgap15'] = o * (np.log(pc[i] / pc[i - 15]) - np.log(sc[i] / sc[i - 15])) / s60
        f = zp['funding_' + coin]; j = np.searchsorted(f[:, 0], (g.tmin.values * 60000).astype(float), side='right') - 1
        rate = np.where(j >= 0, f[np.clip(j, 0, len(f) - 1), 1], np.nan) * 1e4; r['fund'] = rate; r['ofund'] = o * rate; r['afund'] = np.abs(rate)
        ii = g.index.values
        for c in F11: out[c][ii] = r[c]
    for c in F11: U[c] = out[c]
    U.to_pickle(f'{R}/dfuerte/units_{src}_r3.pkl'); print(src, len(U), U[F11].isna().mean().round(3).to_dict(), flush=True)
for s in sys.argv[1:]: run(s)
