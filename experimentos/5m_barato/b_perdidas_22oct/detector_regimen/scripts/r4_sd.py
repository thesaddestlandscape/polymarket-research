#!/usr/bin/env python3
"""r4_sd.py - ENMIENDA 1 (sha 6d90c029...): S_D (2025, proxy) y combinado S_A+S_D para Delta e I_R. Bootstrap rapido por sumas diarias."""
import sys, os, numpy as np, pandas as pd, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); DAT = os.path.join(HERE, '..', 'datos')
assert hashlib.sha256(open(os.path.join(HERE, '..', 'PREREG_RTEND_enm1.md'), 'rb').read()).hexdigest().startswith('6d90c029')
sys.path.insert(0, HERE)
import r2_analisis as R2
RNG = np.random.default_rng(20261025); NB = 4000
def daily(U):
    g = U[U.cls != 'NEU'].groupby(['dia', 'R', 'cls']).agg(e=('e', 'sum'), q=('q', 'sum')).reset_index()
    days = sorted(U.dia.unique()); ix = {d: i for i, d in enumerate(days)}; M = {}
    for (R, c), x in g.groupby(['R', 'cls']):
        a = np.zeros((len(days), 2)); a[[ix[d] for d in x.dia]] = x[['e', 'q']].values; M[(R, c)] = a
    for c in ('CON', 'CONTRA'):                      # global
        a = np.zeros((len(days), 2))
        for R in ('TREND', 'MIXTO', 'REVERT', 'NA'): a += M.get((R, c), 0)
        M[('ALL', c)] = a
    return days, M
def ev(M, R, c, w): s = (M[(R, c)] * w[:, None]).sum(0); return s[0] / s[1]
def boot(U, label):
    days, M = daily(U); nd = len(days); w1 = np.ones(nd); out = {k: [] for k in ('D', 'DT', 'DR', 'I')}
    base = dict(D=ev(M, 'ALL', 'CON', w1) - ev(M, 'ALL', 'CONTRA', w1), DT=ev(M, 'TREND', 'CON', w1) - ev(M, 'TREND', 'CONTRA', w1), DR=ev(M, 'REVERT', 'CON', w1) - ev(M, 'REVERT', 'CONTRA', w1))
    base['I'] = base['DT'] - base['DR']
    for _ in range(NB):
        w = np.bincount(RNG.integers(0, nd, nd), minlength=nd).astype(float)
        d = ev(M, 'ALL', 'CON', w) - ev(M, 'ALL', 'CONTRA', w); dt = ev(M, 'TREND', 'CON', w) - ev(M, 'TREND', 'CONTRA', w); dr = ev(M, 'REVERT', 'CON', w) - ev(M, 'REVERT', 'CONTRA', w)
        out['D'].append(d); out['DT'].append(dt); out['DR'].append(dr); out['I'].append(dt - dr)
    s = f'{label}: dias {nd}  '
    for k in ('D', 'DT', 'DR', 'I'):
        a = np.array(out[k]); lo, hi = np.nanpercentile(a, [5, 95]); p2 = 2 * min((a <= 0).mean(), (a >= 0).mean())
        s += f'{k}={base[k]:+.4f} IC90({lo:+.4f},{hi:+.4f}) p2={p2:.3f} | '
    # X_otros vs Dp (POST-HOC, quita la mecanica)
    from scipy.stats import spearmanr
    dd = U.groupby('dia').apply(lambda g: pd.Series(dict(Dp=-g[g.cls == 'CON'].e.sum(), Xo=g[g.cls != 'CON'].e.sum(), X=g.e.sum())), include_groups=False)
    r1 = spearmanr(dd.Xo, dd.Dp); r2 = spearmanr(dd.X, dd.Dp)
    s += f'\n   Spearman(X_otros,Dp)={r1.statistic:+.3f} p={r1.pvalue:.4f}; Spearman(X_total,Dp)={r2.statistic:+.3f}; Dp>0 en {(dd.Dp>0).mean():.3f} dias; Dp medio dias Xo<mediana {dd.Dp[dd.Xo<dd.Xo.median()].mean():+.2f} vs >= {dd.Dp[dd.Xo>=dd.Xo.median()].mean():+.2f}'
    return s
if __name__ == '__main__':
    prim = ['ETH', 'SOL', 'XRP']; out = []
    A = pd.read_csv(os.path.join(DAT, 'panel_backfill.csv.gz')); Dd = pd.read_csv(os.path.join(DAT, 'panel_y2025.csv.gz')); B = pd.read_csv(os.path.join(DAT, 'panel_dic_ene.csv.gz'))
    UA = R2.prep(A, prim, 180, 'win_proxy'); UD = R2.prep(Dd, prim, 180, 'win_proxy'); UB = R2.prep(B, prim, 180, 'win_oficial'); UBp = R2.prep(B, prim, 180, 'win_proxy')
    UAD = pd.concat([UA, UD], ignore_index=True)
    for U, lab in ((UA, 'S_A (129 d)'), (UD, 'S_D (2025)'), (UAD, 'S_A+S_D'), (UB, 'S_B oficial'), (pd.concat([UA, UD, UBp], ignore_index=True), 'S_A+S_D+S_Bproxy')):
        out.append(boot(U, lab)); print(out[-1], flush=True)
    # sensibilidad BTC
    UDb = R2.prep(Dd, ['BTC'], 180, 'win_proxy'); out.append(boot(UDb, 'S_D BTC')); print(out[-1])
    # umbral relativo no hecho. Nota: Delta por clase R en S_D
    for c in ('TREND', 'MIXTO', 'REVERT'):
        s = UD[UD.R == c]; out.append(f'S_D R={c}: n {len(s)} Delta {R2.dstat(s):+.4f}'); print(out[-1])
    open(os.path.join(DAT, 'r4.txt'), 'w').write('\n'.join(out))
