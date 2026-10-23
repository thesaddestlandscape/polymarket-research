#!/usr/bin/env python3
"""f5_wave2_feats.py - anade F9 (en ventana) y F10 (memoria de residuos) a units_<src>.pkl -> units_<src>_w2.pkl (PREREG_DFUERTE_W2)."""
import sys, os, numpy as np, pandas as pd, warnings
warnings.filterwarnings('ignore')
OUT = '/root/polymarket-research-datalogs/regimen_5m'; F9 = ['rv_in', 'maxr_in', 'eff_in', 'zT', 'last', 'retr', 'imb_in', 'vol_in', 'hl_in']
F10 = ['rc12_all', 'rc36_all', 'rc36_coin', 'e12_all', 'e36_all', 'e36_coin']
def run(src):
    U = pd.read_pickle(f'{OUT}/dfuerte/units_{src}.pkl'); U = U[U['T'] == 180].reset_index(drop=True); z = np.load(f'{OUT}/full_{src}.npz'); f = {c: np.full(len(U), np.nan) for c in F9}
    for coin, g in U.groupby('coin'):
        m0 = int(z[coin + '_m0']); X = z[coin + '_X']; io = g.tmin.values - m0; o = g.o.values; s60 = g.s60.values; lp = np.log(X[:, 0]); R = np.diff(lp, prepend=np.nan)
        idx = io[:, None] + np.arange(1, 4)[None, :]; r = R[idx]; ret = lp[io + 3] - lp[io]
        k = np.arange(0, 4)[None, :]; path = o[:, None] * (lp[io[:, None] + k] - lp[io][:, None]); ext = np.nanmax(path, 1)
        vol = X[idx, 3]; tbv = X[idx, 4]; v24 = np.array([np.nansum(X[i - 1439:i + 1, 3]) for i in io]); sv = vol.sum(1)
        v = dict(rv_in=np.sqrt((r ** 2).mean(1)) / s60, maxr_in=np.abs(r).max(1) / s60, eff_in=np.abs(ret) / np.abs(r).sum(1), zT=np.clip(o * ret / (s60 * np.sqrt(3)), -8, 8), last=o * r[:, -1] / s60,
                 retr=(ext - o * ret) / s60, imb_in=o * (2 * tbv.sum(1) - sv) / sv, vol_in=sv / (v24 / 480), hl_in=np.log(X[idx, 1].max(1) / X[idx, 2].min(1)) / s60)
        ii = g.index.values
        for c in F9: f[c][ii] = v[c]
    for c in F9: U[c] = f[c]
    U['rcon'] = U.y - U.pcon; U['slot'] = U.tmin // 5; lo, hi = U.slot.min() - 40, U.slot.max() + 1; n = hi - lo + 1
    def trail(df, col, w):   # media de col en los slots [s-w, s-1]
        s = np.zeros(n); c = np.zeros(n); np.add.at(s, df.slot.values - lo, df[col].values); np.add.at(c, df.slot.values - lo, 1)
        cs = np.concatenate([[0], np.cumsum(s)]); cc = np.concatenate([[0], np.cumsum(c)]); i = U.slot.values - lo
        S = cs[i] - cs[i - w]; C = cc[i] - cc[i - w]; return np.where(C >= 10, S / np.maximum(C, 1), np.nan)
    U['rc12_all'] = trail(U, 'rcon', 12); U['rc36_all'] = trail(U, 'rcon', 36); U['e12_all'] = trail(U, 'e_', 12) if False else np.nan
    U['e_'] = U.win - U.q; U['e12_all'] = trail(U, 'e_', 12); U['e36_all'] = trail(U, 'e_', 36); U['rc36_coin'] = np.nan; U['e36_coin'] = np.nan
    for coin, g in U.groupby('coin'):
        sub = U[U.coin == coin]; i = sub.index.values
        for col, nm in (('rcon', 'rc36_coin'), ('e_', 'e36_coin')):
            s = np.zeros(n); c = np.zeros(n); np.add.at(s, sub.slot.values - lo, sub[col].values); np.add.at(c, sub.slot.values - lo, 1)
            cs = np.concatenate([[0], np.cumsum(s)]); cc = np.concatenate([[0], np.cumsum(c)]); j = sub.slot.values - lo; S = cs[j] - cs[j - 36]; C = cc[j] - cc[j - 36]
            U.loc[i, nm] = np.where(C >= 10, S / np.maximum(C, 1), np.nan)
    U.drop(columns=['e_', 'rcon', 'slot']).to_pickle(f'{OUT}/dfuerte/units_{src}_w2.pkl'); print(src, len(U), U[F9 + F10].isna().mean().round(3).to_dict())
for s in sys.argv[1:]: run(s)
