import numpy as np, sys, glob
for f in sorted(glob.glob('cache/fuentes_2026-*.npz')):
    H = np.load(f)['H']; n0 = H[0, :, 0]; f0 = H[0, :, 1] / np.maximum(n0, 1); lo = (n0 >= 100) & (f0 >= .3); hi = (n0 >= 100) & (f0 <= .01); print(f[-14:-4], 'bins base lo', int(lo.sum()), 'hi', int(hi.sum()))
    for s, nm in ((1, 'q 5m fuera de banda'), (2, 'prints t 5m'), (3, 'q m15_registro (15m/60m)')):
        n = H[s, :, 0]; fr = H[s, :, 1] / np.maximum(n, 1); ok = n >= 30
        a = ok & lo; b = ok & hi; c = ok & (n0 >= 100); r = np.corrcoef(fr[c], f0[c])[0, 1] if c.sum() > 3 else np.nan
        print(f'  {nm:<26} filas {int(n.sum()):>9}; bins n>=30: en base-lo {int(a.sum())} frac d<30 media {fr[a].mean() if a.any() else float("nan"):.3f} (p10 {np.percentile(fr[a], 10) if a.any() else float("nan"):.3f}); en base-hi {int(b.sum())} media {fr[b].mean() if b.any() else float("nan"):.3f} (p90 {np.percentile(fr[b], 90) if b.any() else float("nan"):.3f}); corr con base {r:.2f}; bins con fuente n>=30 y base n<100: {int((ok & (n0 < 100)).sum())} de {int((n0 < 100).sum())}')
