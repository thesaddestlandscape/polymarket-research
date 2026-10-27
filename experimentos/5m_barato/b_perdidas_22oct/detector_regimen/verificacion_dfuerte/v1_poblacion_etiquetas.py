#!/usr/bin/env python3
"""v1 - verificacion independiente: reconstruye poblacion y etiquetas de las unidades desde klines crudos (full_*.npz) sin importar dfuerte_lib. Solo lectura."""
import numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
from scipy.special import ndtr
R = '/root/polymarket-research-datalogs/regimen_5m'
def rms(lp, i, w):
    R1 = np.full(len(lp), np.nan); R1[1:] = lp[1:] - lp[:-1]; ok = np.isfinite(R1); r0 = np.where(ok, R1, 0.0)
    cq = np.concatenate([[0], np.cumsum(r0 ** 2)]); cn = np.concatenate([[0], np.cumsum(ok)])
    lo = i - w + 1; g = lo >= 1; lo2 = np.where(g, lo, 1); c = cn[i + 1] - cn[lo2]
    v = np.sqrt(np.where(c > 0, (cq[i + 1] - cq[lo2]) / np.maximum(c, 1), np.nan)); v[(~g) | (c < 0.8 * w)] = np.nan; return v
tot = {}
for src in ('y2025', 'dic_ene', 'backfill', 'reciente'):
    z = np.load(f'{R}/full_{src}.npz'); U = pd.read_pickle(f'{R}/dfuerte/units_{src}_r3.pkl'); U = U[U['T'] == 180]
    lo_t, hi_t = U.tmin.min(), U.tmin.max(); mine = []
    for c in sorted({k[:-3] for k in z.files if k.endswith('_m0')}):
        m0 = int(z[c + '_m0']); X = z[c + '_X']; lp = np.log(X[:, 0]); tm = np.arange((lo_t + 4) // 5 * 5, hi_t + 1, 5); io = tm - m0
        io = io[(io >= 1500) & (io + 5 < len(lp))]; tm = io + m0
        rpre = (lp[io] - lp[io - 15]) * 1e4; ret = lp[io + 3] - lp[io]; sT = rms(lp, io + 3, 60); fin = lp[io + 5] - lp[io]
        q = ndtr(-np.abs(ret) / (sT * np.sqrt(2.0))); up = ret < 0
        win = np.where(up, fin >= 0, fin < 0).astype(float); win[~np.isfinite(fin) | ~np.isfinite(ret)] = np.nan
        m = (q >= .1) & (q < .3) & np.isfinite(win) & np.isfinite(rpre) & (ret != 0) & (np.abs(rpre) >= 7.7)
        d = pd.DataFrame(dict(coin=c, tmin=tm[m], q2=q[m], win2=win[m], con2=(np.sign(rpre[m]) == np.where(up[m], 1, -1)).astype(int), rpre2=rpre[m])); mine.append(d)
    M = pd.concat(mine); J = U[['coin', 'tmin', 'q', 'win', 'con', 'rpre', 'dia']].merge(M, on=['coin', 'tmin'], how='outer', indicator=True)
    both = J[J._merge == 'both']
    print(f'{src}: guardadas {len(U)} mias {len(M)} | solo guardadas {int((J._merge=="left_only").sum())} solo mias {int((J._merge=="right_only").sum())} | '
          f'max|dq| {np.abs(both.q-both.q2).max():.2e} win distinto {int((both.win!=both.win2).sum())} con distinto {int((both.con!=both.con2).sum())} max|drpre| {np.abs(both.rpre-both.rpre2).max():.2e}', flush=True)
    for k, v in J[J._merge != 'both'].groupby('_merge').dia.agg(['count', 'min', 'max']).iterrows(): print('   ', k, dict(v))
    tot[src] = len(U)
print(tot)
