#!/usr/bin/env python3
"""p1_pop.py DIA... -- PREREG_P1 (sha 0552983b...): clase C1/C2/C3 de cada relleno maker on-chain (ETH/SOL/XRP 5m) y unidades
primeras-5 acc por (maker, mercado, lado c). Salida datos/u_D.csv.gz (unidades, incluida B con es_b=1) y datos/fb_D.csv (rellenos de B)."""
import sys, os, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos')
PR = os.path.join(AQ, '..', 'prereg', 'PREREG_P1_CLASIFICACION.md')
assert hashlib.sha256(open(PR, 'rb').read()).hexdigest().startswith('0552983b7e6ead68'), 'prereg cambiado'
EX = '0xe111180000d2663c0091e4f400237545b87b996b'; US = '0x659a40ff9920febc5a66836213040924343d297f'
HS = (0, 1, 2, 5); THS = (0.005, 0.015)
def dia(d):
    T = pd.read_csv(os.path.join(D, f'tok_{d}.csv'), dtype={'mid': str, 'token': str})
    comp = {}
    for mid, g in T.groupby('mid'):
        if len(g) == 2: a, b = g.tok_i.values; comp[a] = b; comp[b] = a
    F = pd.read_csv(os.path.join(D, f'oc_{d}.csv.gz'), dtype={'tx': str, 'maker': str, 'taker': str})
    F = F[F.taker != EX].copy()
    F = F[F.tok_i.isin(comp.keys())]
    buy = F.side.values == 0
    F['sh'] = np.where(buy, F.ta, F.ma); usd = np.where(buy, F.ma, F.ta)
    F = F[F.sh > 0].copy(); buy = F.side.values == 0; usd = np.where(buy, F.ma, F.ta)
    pr = usd / F.sh.values
    F['c'] = np.where(buy, F.tok_i.values, F.tok_i.map(comp).values).astype(int)
    F['pc'] = np.where(buy, pr, 1 - pr)
    ti = T.set_index('tok_i')
    F['act'] = F.c.map(ti.act); F['mid'] = F.c.map(ti.mid); F['fin'] = F.c.map(ti.fin); F['lado'] = F.c.map(ti.lado); F['des'] = F.c.map(ti.des)
    F = F.sort_values(['c', 'bloque', 'li']).reset_index(drop=True)
    F['txi'] = pd.factorize(F.tx)[0]
    n = len(F); res = {f'deep_tx_{t}': np.zeros(n, bool) for t in THS}
    for t in THS:
        for h in HS: res[f'deep_post_h{h}_{t}'] = np.zeros(n, bool)
    cs = F.c.values; bl = F.bloque.values.astype(np.int64); li = F.li.values.astype(np.int64); tx = F.txi.values; pc = F.pc.values
    st = np.r_[0, np.flatnonzero(np.diff(cs)) + 1, n]
    for a, b in zip(st[:-1], st[1:]):
        B = bl[a:b]; L = li[a:b]; X = tx[a:b]; P = pc[a:b]
        # min pc por tx dentro del grupo
        mn_tx = pd.Series(P).groupby(X).transform('min').values
        for t in THS: res[f'deep_tx_{t}'][a:b] = mn_tx < P - t
        # posterior: para cada i, min pc entre filas con (B==Bi & L>Li & X!=Xi) o (Bi<B<=Bi+h)
        m = b - a
        if m == 1: continue
        # suffix min por orden (B,L) ya ordenado; ventana por bloque via searchsorted
        sufmin = np.minimum.accumulate(P[::-1])[::-1]   # min de P[j:] (orden bloque,li)
        for h in HS:
            hi = np.searchsorted(B, B + h, 'right')        # filas con bloque <= Bi+h
            # min sobre j en (i, hi) excluyendo misma tx: aproximamos con min de rango y luego corregimos misma tx
            out = np.full(m, np.inf)
            for i in range(m):
                j0 = i + 1; j1 = hi[i]
                if j1 > j0:
                    seg = P[j0:j1]; sx = X[j0:j1]; ok = sx != X[i]
                    if ok.any(): out[i] = seg[ok].min()
            for t in THS: res[f'deep_post_h{h}_{t}'][a:b] = out < P - t
    for k, v in res.items(): F[k] = v
    for t in THS:
        for h in HS:
            F[f'cl_h{h}_{t}'] = np.where(F[f'deep_tx_{t}'], 'C1', np.where(F[f'deep_post_h{h}_{t}'], 'C2', 'C3'))
    F['T'] = F.fin - F.ts
    # rellenos de B
    Bf = F[F.maker == US].copy(); Bf.to_csv(os.path.join(D, f'fb_{d}.csv'), index=False)
    # unidades primeras 5 acc
    F = F.sort_values(['maker', 'c', 'bloque', 'li']).reset_index(drop=True)
    F['cum'] = F.groupby(['maker', 'c']).sh.cumsum(); prev = F.cum - F.sh
    F['use'] = np.clip(5 - prev, 0, None).clip(upper=F.sh); F = F[F.use > 0].copy()
    F['coste'] = F.use * F.pc; F['gana'] = (F.des == F.lado).astype(float); F.loc[F.des.isna(), 'gana'] = np.nan
    F['pnl'] = F.use * F.gana - F.coste
    g = F.groupby(['maker', 'c'], sort=False)
    U = g.first()[['act', 'mid', 'fin', 'lado', 'des', 'pc', 'T', 'bloque', 'ts', 'tx'] + [c for c in F.columns if c.startswith('cl_')]].copy()
    U['coste'] = g.coste.sum(); U['pnl'] = g.pnl.sum(min_count=1); U['acc'] = g.use.sum(); U['gana'] = g.gana.first()
    U = U.reset_index(); U['es_b'] = (U.maker == US).astype(int)
    U = U[(U.pc > 0.10 + 1e-9) & (U.pc <= 0.30 + 1e-9) & (U['T'] > 60) & (U['T'] <= 300)]
    U['dia'] = d
    U.to_csv(os.path.join(D, f'u_{d}.csv.gz'), index=False)
    print(d, 'rellenos', n, 'unidades banda', len(U), 'B', int(U.es_b.sum()), 'sin desenlace', int(U.gana.isna().sum()),
          U.groupby('cl_h1_0.005').coste.sum().round(0).to_dict(), flush=True)
for d in sys.argv[1:]: dia(d)
