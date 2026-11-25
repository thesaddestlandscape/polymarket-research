#!/usr/bin/env python3
"""FRENTE 2 sueltos, parte 2 (EXPLORATORIO, quemados): (a) aproximacion 'quitar rellenos' vs motor (GEO6 10 d = +140,0 EUR);
(b) reglas EVITAR nuevas (IW: Binance desde la apertura contra el lado; SPR: spread en la decision) INCREMENTALES a GEO6 y CXJ150-like
(brazos ya en el forward thru1), umbral elegido en TRAIN, placebo por permutacion del rasgo dentro de dia x moneda x L, e inversion;
(c) 'comprar mas' tras el relleno (inversion de la salida) al ask +1250 ms con fee tomador."""
import glob, numpy as np, pandas as pd
H = '/root/polymarket-research/experimentos/5m_barato/frente2_sueltos_10nov/'
A = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out/F_*.pkl'))], ignore_index=True)
TR = {'2026-10-26', '2026-10-27', '2026-10-28', '2026-10-29', '2026-10-30', '2026-10-31'}
A['per'] = np.where(A.dia.isin(TR), 'TRAIN', 'HOLD'); A['spread_dec'] = A.ask_dec - A.bid_dec
RNG = np.random.default_rng(7); out = []; P = out.append
D10 = A[A.dia <= '2026-11-04']
P(f'(a) 10 d, todos los rellenos G0 (n={len(D10)}, pnl {D10.pnl.sum():+.1f}); GEO6 por quitar rellenos: dPnL {-D10.pnl[(D10.bidL < 0.06 - 1e-6) | D10.bidL.isna()].sum():+.1f} (motor anaT: +140,0)')
P(f'    CXJ-like (ja3, sin la parte de cancelacion): dPnL {-D10.pnl[D10.ja3.fillna(False).astype(bool)].sum():+.1f} (motor NJ3A +2,5; CXJ150 +128,3 incluye cancelacion en vida)')
F = A[A.R0 >= 0].copy(); F['suelto'] = F.R0 == 0
def boot(df, col, B=2000):
    g = df.groupby('dia').agg(v=(col, 'sum'), c=('cost', 'sum')); ix = RNG.integers(0, len(g), (B, len(g)))
    r = g.v.values[ix].sum(1) / g.c.values[ix].sum(1); return np.percentile(r, [5, 95])
def sin2(df, col):
    g = df.groupby('dia').agg(v=(col, 'sum'), c=('cost', 'sum')).sort_values('v'); g = g.iloc[:-2]; return g.v.sum() / g.c.sum()
def av(nm, df, mask, perm_col=None, thr_fn=None, nperm=300):
    mask = np.asarray(mask, bool); d = np.where(mask, -df.pnl.values, 0.0); x = df.assign(d=d); lo, hi = boot(x, 'd'); g = x.groupby('dia').d.sum()
    kept = df[~mask]; s = f'{nm:44s} quita={mask.mean():.3f} dPnL={d.sum():+7.1f} (suelto {d[df.suelto.values].sum():+6.1f}) IC90d/EUR=({lo:+.3f},{hi:+.3f}) sin2={sin2(x, "d"):+.3f} dias+={int((g>0).sum())}/{len(g)} EV_rest={kept.pnl.sum()/kept.cost.sum():+.3f} EVsu_rest={kept.pnl[kept.suelto].sum()/kept.cost[kept.suelto].sum():+.3f}'
    if perm_col is not None and thr_fn is not None:   # placebo: permutar el rasgo dentro de dia x moneda x L (misma distribucion, sin asociacion)
        obs = d.sum(); null = []; grp = df.groupby(['dia', 'act', df.L.round(2)]).indices
        v = df[perm_col].values
        for _ in range(nperm):
            vp = v.copy()
            for idx in grp.values(): vp[idx] = v[RNG.permutation(idx)]
            null.append(-df.pnl.values[thr_fn(vp)].sum())
        null = np.array(null); s += f' | placebo media {null.mean():+.1f} p(>=obs) {(null >= obs).mean():.3f}'
    return s
for base_nm, base_mask in (('G0', np.zeros(len(F), bool)), ('GEO6', ((F.bidL < 0.06 - 1e-6) | F.bidL.isna()).values),
                           ('GEO6+ja3', (((F.bidL < 0.06 - 1e-6) | F.bidL.isna()) | F.ja3.fillna(False).astype(bool)).values)):
    P(f'== (b) base {base_nm}: reglas aplicadas sobre los rellenos que la base CONSERVA')
    for per in ('TRAIN', 'HOLD', 'TODO'):
        D_ = F[~base_mask] if per == 'TODO' else F[~base_mask & (F.per == per).values]
        P(f'-- {per} n={len(D_)} EV={D_.pnl.sum()/D_.cost.sum():+.3f} suelto={D_.pnl[D_.suelto].sum()/D_.cost[D_.suelto].sum():+.3f}')
        for th in (0, 2, 5, 10):
            m = (D_.bn_inwin <= -th).values
            P('  ' + av(f'IW{th}: no armar si Binance desde apertura <=-{th}bps', D_, m, 'bn_inwin', (lambda v, th=th: np.nan_to_num(v, nan=0.0) <= -th) if per != 'TODO' else None))
        P('  ' + av('IWinv5: no armar si Binance desde apertura >=+5', D_, (D_.bn_inwin >= 5).values))
        for s_ in (0.02, 0.03):
            m = (D_.spread_dec >= s_ - 1e-6).values
            P('  ' + av(f'SPR{int(s_*100)}: no armar si spread>={s_:.2f}', D_, m, 'spread_dec', (lambda v, s_=s_: np.nan_to_num(v, nan=0.0) >= s_ - 1e-6) if per != 'TODO' else None))
P('== correlaciones (todos): ' + ', '.join(f'{a}-{b} {F[a].corr(F[b], method="spearman"):+.2f}' for a, b in (('bn_inwin', 'bidL'), ('spread_dec', 'bidL'), ('bn_inwin', 'spread_dec'))))
# (c) comprar mas tras el relleno: q acciones al ask(+1250) con fee tomador; EV por EUR de la compra adicional
F['ask_p1250'] = F['ask_p1250'].astype(float); m = F.ask_p1250.notna() & (F.ask_p1250 > 0) & (F.ask_p1250 < 1)
F['c_add'] = np.where(m, F.q * F.ask_p1250, 0.0); F['p_add'] = np.where(m, F.q * (F.gana - F.ask_p1250 - 0.07 * F.ask_p1250 * (1 - F.ask_p1250)), 0.0)
for per in ('TRAIN', 'HOLD'):
    for nm, sub in (('suelto', F.suelto), ('rafaga', ~F.suelto)):
        D_ = F[sub & (F.per == per) & m]; g = D_.groupby('dia').agg(v=('p_add', 'sum'), c=('c_add', 'sum')); ix = RNG.integers(0, len(g), (2000, len(g)))
        lo, hi = np.percentile(g.v.values[ix].sum(1) / g.c.values[ix].sum(1), [5, 95])
        P(f'(c) comprar mas al ask+1250 {per} {nm}: n={len(D_)} ask medio={D_.ask_p1250.mean():.4f} acierto={D_.gana.mean():.4f} EV/EUR={D_.p_add.sum()/D_.c_add.sum():+.3f} IC90d=({lo:+.3f},{hi:+.3f}) dias+={int((g.v>0).sum())}/{len(g)}')
open(H + 'out/ana2.txt', 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
