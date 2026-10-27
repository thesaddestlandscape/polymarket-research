#!/usr/bin/env python3
"""v3 - alineacion temporal perps vs spot (correlacion cruzada de retornos 1m por retardo) + comprobacion funding."""
import numpy as np
R = '/root/polymarket-research-datalogs/regimen_5m'; D = '/mnt/HC_Volume_106538179/agentes_datos/dfuerte'
for src in ('reciente', 'y2025'):
    zs = np.load(f'{R}/full_{src}.npz'); zp = np.load(f'{D}/perp_{src}.npz')
    for c in ('BTC', 'ETH', 'XRP'):
        ms, Xs = int(zs[c + '_m0']), zs[c + '_X']; mp, Xp = int(zp[c + '_m0']), zp[c + '_X']
        lo = max(ms, mp); hi = min(ms + len(Xs), mp + len(Xp)); a = np.log(Xs[lo - ms:hi - ms, 0]); b = np.log(Xp[lo - mp:hi - mp, 0])
        ra = np.diff(a); rb = np.diff(b); out = {}
        for k in (-2, -1, 0, 1, 2):   # corr(spot[t], perp[t+k])
            x = ra[max(0, -k):len(ra) - max(0, k)]; y = rb[max(0, k):len(rb) - max(0, -k)]; ok = np.isfinite(x) & np.isfinite(y); out[k] = round(float(np.corrcoef(x[ok], y[ok])[0, 1]), 3)
        f = zp['funding_' + c]; print(src, c, 'lag-corr spot[t] vs perp[t+k]:', out, '| m0 spot', ms, 'perp', mp, '| funding n', len(f), 'ultimo', int(f[-1, 0]), 'residuo ms mod 8h mediano', int(np.median(f[:, 0] % 28800000)))
