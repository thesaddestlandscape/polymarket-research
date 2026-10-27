#!/usr/bin/env python3
"""E-RE-CG-04: persistencia de makers en el rango de B (0,05-0,40) y en favoritos (>=0,70/>=0,90). Solo lectura de U_D.parquet."""
import glob, sys
import numpy as np, pandas as pd
from math import erf, sqrt
from archivo_volumen import VOL  # noqa
IN = VOL / 'agentes_datos' / 're_censo'
B = '0x659a40ff9920febc5a66836213040924343d297f'
CONOC = ('0x21f4', '0xe290', '0x86b1', '0x0ab0', '0xf074', '0xb0f85baa', '0x32ed2e54')
def _lee(f):
    u = pd.read_parquet(f, columns=['w', 'rol', 'act', 'mkt', 'lado', 'b05', 'pnl', 'reb', 'c', 'acc', 'n', 'Tc', 'cob', 'dia'])
    u = u[(u.rol == 'M') & u.cob]
    for col in ('w', 'act', 'mkt', 'lado', 'dia', 'rol'): u[col] = u[col].astype(str)
    return u
U = pd.concat([_lee(f) for f in sorted(glob.glob(str(IN / 'U_*.parquet')))], ignore_index=True)
for col in ('w', 'act', 'mkt', 'lado', 'dia'): U[col] = U[col].astype('category')
U = U[U.w != B]
U['pc'] = U.b05 * 0.05
UNIV = {'R-B': (U.rol == 'M') & (U.pc >= 0.05) & (U.pc < 0.40) & U.act.isin(['ETH', 'SOL', 'XRP']),
        'R-B6': (U.rol == 'M') & (U.pc >= 0.05) & (U.pc < 0.40),
        'R-F70': (U.rol == 'M') & (U.pc >= 0.70), 'R-F90': (U.rol == 'M') & (U.pc >= 0.90)}
VENT = {'A7': (['2026-10-%02d' % d for d in range(8, 15)], ['2026-10-%02d' % d for d in range(15, 26)]),
        'A10': (['2026-10-%02d' % d for d in range(5, 15)], ['2026-10-%02d' % d for d in range(15, 26)]),
        'A14': (['2026-10-%02d' % d for d in range(5, 19)], ['2026-10-%02d' % d for d in range(19, 26)])}
rng = np.random.default_rng(20261026)
def zt(x, reb):
    v = x.pnl + (x.reb if reb else 0)
    g = x.assign(v=v).groupby(['w', 'dia']).agg(v=('v', 'sum'), c=('c', 'sum')).reset_index().groupby('w')
    m = g.v.mean(); s = g.v.std(ddof=1); n = g.size()
    return pd.DataFrame({'net': g.v.sum(), 'c': g.c.sum(), 'z': m / (s / np.sqrt(n)), 'nd': n})
def ic_dias(x, reb):
    g = x.assign(v=x.pnl + (x.reb if reb else 0)).groupby('dia')[['v', 'c']].sum().values
    if len(g) < 3: return np.nan, np.nan
    idx = rng.integers(0, len(g), (2000, len(g))); s = g[idx].sum(axis=1); r = s[:, 0] / s[:, 1]
    return np.percentile(r, 5), np.percentile(r, 95)
for un, mk in UNIV.items():
    X = U[mk].copy(); X['w'] = X.w.astype(str); dias = sorted(X.dia.unique())
    pool = X.groupby('dia').c.sum().mean(); evp = X.pnl.sum() / X.c.sum(); evr = (X.pnl.sum() + X.reb.sum()) / X.c.sum()
    tw = X.groupby('w').c.sum(); ww = X.groupby('w').pnl.sum()
    print('\n######## %s: pool %.0f €/dia (coste maker), %d wallets, EV poblacion %+.4f (+reb %+.4f), unidades %d, dias %d' % (un, pool, len(tw), evp, evr, len(X), len(dias)))
    print('  wallets net>0 en todo el periodo: %d (con >=5 dias %d); top-10 net %s' % ((ww > 0).sum(), ((ww > 0) & (X.groupby('w').dia.nunique() >= 5)).sum(), ', '.join('%s %+.0f' % (w[:10], v) for w, v in ww.sort_values(ascending=False).head(10).items())))
    for vn, (A, Tt) in VENT.items():
        for reb in (False, True):
            S = zt(X[X.dia.isin(A)], reb); T = zt(X[X.dia.isin(Tt)], reb)
            ros = S[(S.net > 0) & (S.z >= 2) & (S.nd >= 4)].index; inv = S[(S.net < 0) & (S.z <= -2) & (S.nd >= 4)].index
            if len(ros) == 0:
                print('  %s reb=%d roster vacio (A activas %d)' % (vn, reb, len(S))); continue
            Tm = T.reindex(S.index); v = Tm.loc[ros].net.fillna(0)
            dec = pd.qcut(S.c.rank(method='first'), 10, labels=False); rd = dec.loc[ros].value_counts(); pn, pp = [], []
            for _ in range(1000):
                pick = np.concatenate([rng.choice(dec.index[dec == k], size=c, replace=False) for k, c in rd.items()]); y = Tm.loc[pick].net.fillna(0); pn.append(y.sum()); pp.append((y > 0).mean())
            pn, pp = np.array(pn), np.array(pp); vi = Tm.loc[inv].net.fillna(0)
            evT = Tm.loc[ros].net.sum() / Tm.loc[ros].c.sum() if Tm.loc[ros].c.sum() > 0 else np.nan
            c = T.loc[T.index.intersection(ros)]; c = c[c.nd >= 3].copy()
            c['p'] = [1 - .5 * (1 + erf(zz / sqrt(2))) if np.isfinite(zz) else 1 for zz in c.z]; c = c.sort_values('p'); m = len(c)
            k = max([i for i, pv in enumerate(c.p.values, 1) if pv <= .1 * i / m], default=0)
            ok = v.sum() > np.percentile(pn, 95) and (v > 0).mean() > np.percentile(pp, 95) and vi.sum() < pn.mean()
            print('  %s reb=%d roster %d | TEST net %+.0f (EV %+.4f) frac+ %.3f | placebo net p50 %+.0f p95 %+.0f frac p95 %.3f | INVERSION n %d net %+.0f | BH %d/%d | %s' % (
                vn, reb, len(ros), v.sum(), evT, (v > 0).mean(), np.median(pn), np.percentile(pn, 95), np.percentile(pp, 95), len(inv), vi.sum(), k, m, 'PERSISTE' if ok else 'no persiste'))
            if not reb and len(c):
                best = c.index[0]; xb = X[X.dia.isin(Tt) & (X.w == best)]; lo, hi = ic_dias(xb, False)
                print('     mejor candidata %s: z TEST %.2f net TEST %+.0f coste TEST %.0f EV %+.4f IC90 dias (%+.4f,%+.4f) dias %d' % (best, c.z.iloc[0], c.net.iloc[0], c.c.iloc[0], c.net.iloc[0] / c.c.iloc[0], lo, hi, int(c.nd.iloc[0])))
    # perfil de las 15 mayores por net del periodo con >=8 dias + conocidas
    g = X.groupby('w'); P = pd.DataFrame({'net': g.pnl.sum(), 'reb': g.reb.sum(), 'c': g.c.sum(), 'dias': g.dia.nunique(), 'unid': g.size(),
                                          'T_med': g.Tc.sum() / g.c.sum(), 'acc_fill': g.acc.sum() / g.n.sum(), 'pc_med': (X.pc * X.c).groupby(X.w).sum() / g.c.sum()})
    P['EV'] = P.net / P.c; P['reb_frac_net'] = P.reb / (P.net + P.reb)
    dpos = X.groupby(['w', 'dia']).pnl.sum().gt(0).groupby(level=0).mean(); P['dias_pos'] = dpos
    mon = X.groupby(['w', 'act']).c.sum().unstack(fill_value=0); P['moneda_top'] = mon.idxmax(axis=1)
    lados = X.groupby(['w', 'mkt']).lado.nunique().gt(1).groupby(level=0).mean(); P['frac_mkt_2lados'] = lados
    sel = P[(P.dias >= 8)].sort_values('net', ascending=False).head(12)
    con = P[[any(i.startswith(cc) for cc in CONOC) for i in P.index]]
    print('  perfil top-12 (>=8 dias) y conocidas:')
    print(pd.concat([sel, con[~con.index.isin(sel.index)]]).round(3).to_string())
