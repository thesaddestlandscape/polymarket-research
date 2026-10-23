#!/usr/bin/env python3
"""r2_analisis.py - PREREG_RTEND H1/H2 (+H3 proxy) sobre S_A (backfill) y S_B (dic_ene). Semilla fija. Salida datos/r2.txt"""
import sys, os, numpy as np, pandas as pd, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); DAT = os.path.join(HERE, '..', 'datos')
assert hashlib.sha256(open(os.path.join(HERE, '..', 'PREREG_RTEND.md'), 'rb').read()).hexdigest().startswith('0cbe5e44')
RNG = np.random.default_rng(20261023); NB = 2000; NP = 1000; THR = 7.7
FAM = {'R': ('TREND', 'REVERT'), 'D': ('TENDENCIA', 'RANGO'), 'COH': ('COH4', 'NOCOH')}
def prep(U, coins, T, wcol):
    U = U[U.coin.isin(coins) & (U['T'] == T)].copy(); U = U[U[wcol].notna()]
    U['sd'] = np.where(U.lado_up, 1.0, -1.0); big = U.rpre.abs() >= THR
    U['cls'] = np.where(~big, 'NEU', np.where(np.sign(U.rpre) == U.sd, 'CON', 'CONTRA'))
    U['e'] = U[wcol] - U.q; U['COHc'] = np.where(U.COH.isna(), 'NA', np.where(U.COH >= 4, 'COH4', 'NOCOH'))
    U['qb'] = (U.q * 20).astype(int); return U
def dstat(U):  # Delta = EV(CON)-EV(CONTRA)
    a = U[U.cls == 'CON']; b = U[U.cls == 'CONTRA']
    if len(a) < 20 or len(b) < 20: return np.nan
    return a.e.sum() / a.q.sum() - b.e.sum() / b.q.sum()
def day_boot(U, fn, nb=NB):
    days = U.dia.unique(); g = {d: x for d, x in U.groupby('dia')}; out = np.empty(nb)
    for i in range(nb):
        ch = RNG.choice(days, len(days)); out[i] = fn(pd.concat([g[d] for d in ch], ignore_index=True))
    return out
def placebo_delta(U, np_=NP):
    V = U[U.cls != 'NEU'].reset_index(drop=True); lab = (V.cls == 'CON').values; strat = (V.dia.astype(str) + V.coin + V.qb.astype(str)).astype('category').cat.codes.values
    e = V.e.values; q = V.q.values; ob = lab.copy(); out = np.empty(np_); idx_sorted = np.argsort(strat, kind='stable')
    for i in range(np_):
        key = RNG.random(len(V)); order = np.lexsort((key, strat)); lp = np.empty(len(V), bool); lp[idx_sorted] = lab[order]
        a = lp; out[i] = e[a].sum() / q[a].sum() - e[~a].sum() / q[~a].sum()
    return out
def line(name, v, bs): 
    lo, hi = np.nanpercentile(bs, [5, 95]); return f'{name}: {v:+.4f}  IC90 dias ({lo:+.4f},{hi:+.4f})'
def run(U, label, coins, T, wcol, out):
    P = lambda s: out.append(s); print(s := f'\n=== {label} | monedas {coins} | T={T} | desenlace {wcol} ===', flush=True); P(s)
    D = prep(U, coins, T, wcol); nd = D.dia.nunique(); P(f'unidades {len(D)} dias {nd}  CON {int((D.cls=="CON").sum())} CONTRA {int((D.cls=="CONTRA").sum())} NEUTRO {int((D.cls=="NEU").sum())}; EV/EUR todas {D.e.sum()/D.q.sum():+.4f}; acierto {D[wcol].mean():.4f} vs q medio {D.q.mean():.4f}')
    d0 = dstat(D); bs = day_boot(D, dstat); pl = placebo_delta(D)
    P(line('H1 Delta=EV(CON)-EV(CONTRA)', d0, bs)); P(f'   placebo (perm CON/CONTRA en dia x moneda x q): p una cola (Delta<=obs) = {(pl<=d0).mean():.4f}; SE_dias={np.nanstd(bs):.4f}; MDE(1,64 SE)={1.64*np.nanstd(bs):.4f}')
    for k in ('CON', 'CONTRA'):
        s = D[D.cls == k]; P(f'   EV {k}: {s.e.sum()/s.q.sum():+.4f} (n {len(s)}, coste {s.q.sum():.0f}, acierto {s[wcol].mean():.3f} vs q {s.q.mean():.3f})')
    res = {}
    for fam, (A, B) in FAM.items():
        col = {'R': 'R', 'D': 'D', 'COH': 'COHc'}[fam]
        sub = D[D[col].isin([A, B])]
        fn = lambda u, A=A, B=B, col=col: dstat(u[u[col] == A]) - dstat(u[u[col] == B])
        iv = fn(sub); bsi = day_boot(sub, fn)
        p2 = 2 * min((bsi <= 0).mean(), (bsi >= 0).mean()) if np.isfinite(bsi).all() else np.nan
        dA = dstat(sub[sub[col] == A]); dB = dstat(sub[sub[col] == B]); nA = int((sub[col] == A).sum()); nB = int((sub[col] == B).sum())
        P(f'H2 {fam}: Delta({A})={dA:+.4f} (n {nA}), Delta({B})={dB:+.4f} (n {nB}); I={iv:+.4f}  IC90 ({np.nanpercentile(bsi,5):+.4f},{np.nanpercentile(bsi,95):+.4f})  p2 dias={p2:.4f}  p_Bonf(x3)={min(1,3*p2):.4f}')
        res[fam] = dict(I=iv, p2=p2, dA=dA, dB=dB)
    # Delta por clase R completa
    for c in ('TREND', 'MIXTO', 'REVERT'):
        s = D[D.R == c]; P(f'   R={c}: n {len(s)}  Delta {dstat(s):+.4f}  EV todo {s.e.sum()/max(s.q.sum(),1e-9):+.4f}')
    # dia-nivel: Dp por dia, X por dia
    day = D.groupby('dia').apply(lambda g: pd.Series(dict(X=g.e.sum(), Dp=-g[g.cls == 'CON'].e.sum(), Con=g[g.cls == 'CON'].e.sum(), nCon=(g.cls == 'CON').sum(), ER=g.ER_dia_prev.mean())), include_groups=False)
    day['Xprev'] = day.X.shift(1)
    from scipy.stats import spearmanr
    P(f'dia-nivel (n dias {len(day)}): Dp=-Sum e CON; X=Sum e todas las unidades del dia. Dp>0 en {(day.Dp>0).mean():.3f} de los dias; PnL skip-CON total {day.Dp.sum():+.1f} acc-EUR; sin 2 mejores dias {day.Dp.sort_values().iloc[:-2].sum():+.1f}')
    for a, b in (('X', 'Dp'), ('ER', 'Dp'), ('ER', 'X'), ('Xprev', 'X'), ('Xprev', 'Dp')):
        t = day[[a, b]].dropna(); r = spearmanr(t[a], t[b]); P(f'   Spearman({a},{b}) = {r.statistic:+.3f} p={r.pvalue:.4f} n_dias {len(t)}')
    # dias malos/buenos segun X (ex-post) : Dp
    mal = day[day.X < day.X.median()]; bue = day[day.X >= day.X.median()]
    P(f'   Dp en dias X<mediana (malos): media {mal.Dp.mean():+.2f} n {len(mal)}; en dias X>=mediana (buenos): {bue.Dp.mean():+.2f} n {len(bue)}')
    day.to_csv(os.path.join(DAT, f'dia_{label.split()[0]}_{wcol}_{T}.csv')); return D, res
if __name__ == '__main__':
    out = []; A = pd.read_csv(os.path.join(DAT, 'panel_backfill.csv.gz')); B = pd.read_csv(os.path.join(DAT, 'panel_dic_ene.csv.gz')); C = pd.read_csv(os.path.join(DAT, 'panel_bookticker.csv.gz'))
    prim = ['ETH', 'SOL', 'XRP']
    run(A, 'S_A backfill', prim, 180, 'win_proxy', out)
    run(B, 'S_B dic_ene', prim, 180, 'win_oficial', out)
    run(B, 'S_Bproxy dic_ene', prim, 180, 'win_proxy', out)
    run(C, 'S_Cprox bookticker(28d)', prim, 180, 'win_proxy', out)
    for T in (120,): run(A, 'sensA backfill', prim, T, 'win_proxy', out); run(B, 'sensB dic_ene', prim, T, 'win_oficial', out)
    run(A, 'replica backfill BTC/BNB/DOGE', ['BTC', 'BNB', 'DOGE'], 180, 'win_proxy', out)
    run(B, 'replica dic_ene BTC', ['BTC'], 180, 'win_oficial', out)
    open(os.path.join(DAT, 'r2.txt'), 'w').write('\n'.join(out))
