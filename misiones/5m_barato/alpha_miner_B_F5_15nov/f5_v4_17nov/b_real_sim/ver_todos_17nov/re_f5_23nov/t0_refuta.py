#!/usr/bin/env python3
"""RE-F5-PUERTA0 paso 6 (exploratorio, dias ya vistos 05-14 Nov): F5 como filtro de ENTRADA por mercado-lado (tercil en la 1.a colocacion, t0).
Contrafactual exacto bajo supuesto: lados independientes (B coloca cada lado por separado) y no entrar = 0 ordenes en ese lado. Refutaciones: placebo dentro de dia x moneda, por moneda, por dia, reloj exchange, T de entrada, lado, quintiles."""
import glob, json, numpy as np, pandas as pd
rng = np.random.default_rng(20261123)
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob('../r1v2_eval/out_p0/p0_ordenes_2026-11-*.pkl'))], ignore_index=True)
POST = R[R.dia < '2026-11-05']; R = R[R.dia >= '2026-11-05']
def lados(Rv):
    Rv = Rv.sort_values('t_dec'); g = Rv.groupby(['dia', 'mid', 'lado'])
    S = g.agg(cost=('cost', 'sum'), pnl=('pnl', 'sum'), coin=('coin', 'first'), t0=('tercil', 'first'), t0ex=('tercil_ex', 'first'), f0=('f5t', 'first'),
              T0=('T_dec', 'first'), L0=('L', 'first'), nf=('q', lambda s: int((s > 0).any())), n_ord=('q', 'size')).reset_index()
    S['g'] = np.where(S.t0 == 'alto', 'alto', 'bm'); S['gex'] = np.where(S.t0ex == 'alto', 'alto', 'bm'); return S
def diff(S, col='g', a='bm', b='alto'):
    A = S[S[col] == a]; B = S[S[col] == b]
    return A.pnl.sum() / A.cost.sum() - B.pnl.sum() / B.cost.sum() if A.cost.sum() > 0 and B.cost.sum() > 0 else np.nan
def boot(S, col='g', a='bm', b='alto', K=2000):
    D = sorted(S.dia.unique()); idx = {d: S.index[S.dia == d] for d in D}; out = []
    for _ in range(K):
        ii = np.concatenate([idx[D[j]] for j in rng.integers(0, len(D), len(D))]); out.append(diff(S.loc[ii], col, a, b))
    out = np.array(out); out = out[np.isfinite(out)]
    if not len(out): return dict(diff=float('nan'), nota='sin coste en un grupo', n_alto=int((S[col] == b).sum()), n_alto_rell=int(S[(S[col] == b)].nf.sum()))
    per = [diff(S[S.dia == d], col, a, b) for d in D]
    return dict(diff=round(diff(S, col, a, b), 4), lo=round(np.percentile(out, 5), 4), hi=round(np.percentile(out, 95), 4), dias=len(D), dias_pos=int(np.nansum(np.array(per) > 0)), n_alto=int((S[col] == b).sum()), n_alto_rell=int(S[(S[col] == b)].nf.sum()))
def placebo(S, K=1000):
    """permuta t0 entre lados dentro de dia x moneda (conserva composicion y nº de alto por celda)"""
    obs = diff(S); v = []; grp = S.groupby(['dia', 'coin']).indices
    for _ in range(K):
        g = S.g.values.copy()
        for ix in grp.values(): g[ix] = rng.permutation(g[ix])
        v.append(diff(S.assign(g=g)))
    v = np.array(v); return dict(obs=round(obs, 4), p_una_cola=round(float((v >= obs).mean()), 4), placebo_media=round(float(v.mean()), 4))
res = {}
for b, Rv in R.groupby('bloq'):
    S = lados(Rv); r = dict(pooled=boot(S), placebo_dia_moneda=placebo(S), reloj_exchange=boot(S, 'gex'))
    r['por_moneda'] = {c: boot(S[S.coin == c]) for c in sorted(S.coin.unique())}
    r['por_mitad'] = {m: boot(S[(S.dia <= '2026-11-09') == (m == 'A')]) for m in 'AB'}
    r['por_dia'] = {d: round(diff(S[S.dia == d]), 3) for d in sorted(S.dia.unique())}
    S['T0b'] = pd.cut(S.T0, [-1e9, 150, 250, 1e9], labels=['<150', '150-250', '>250']).astype(str)
    r['por_T0'] = {k: boot(S[S.T0b == k]) for k in S.T0b.unique() if (S[S.T0b == k].g == 'alto').sum() >= 15}
    r['por_lado'] = {k: boot(S[S.lado == k]) for k in S.lado.unique()}
    r['frac_alto_moneda'] = S.groupby('coin').g.apply(lambda s: round((s == 'alto').mean(), 3)).to_dict()
    S['q5c'] = S.groupby('coin').f0.transform(lambda s: pd.qcut(s.rank(method='first'), 5, labels=False))  # quintiles DENTRO de moneda (recalibrado)
    t = S.groupby('q5c').agg(n=('pnl', 'size'), nf=('nf', 'sum'), cost=('cost', 'sum'), pnl=('pnl', 'sum')); t['EV'] = (t.pnl / t.cost).round(4); r['quintil_f0_dentro_moneda'] = t.round(2).reset_index().to_dict('records')
    r['q5c_0_vs_4'] = boot(S.assign(gq=S.q5c.astype(int)), 'gq', 0, 4)
    r['ev_por_t0'] = {k: dict(n=int(len(x)), nf=int(x.nf.sum()), cost=round(x.cost.sum(), 1), pnl=round(x.pnl.sum(), 2), EV=round(x.pnl.sum() / x.cost.sum(), 4)) for k, x in S.groupby('t0')}
    P0 = lados(POST[POST.bloq == b]); r['posthoc_03_04'] = dict(diff=round(diff(P0), 4), ev_por_t0={k: round(x.pnl.sum() / x.cost.sum(), 4) for k, x in P0.groupby('t0')})
    res[f'bloq{b}'] = r
json.dump(res, open('out/t0_refuta.json', 'w'), indent=1, default=str)
for b in res:
    print('=====', b)
    for k, v in res[b].items(): print(k, v)
