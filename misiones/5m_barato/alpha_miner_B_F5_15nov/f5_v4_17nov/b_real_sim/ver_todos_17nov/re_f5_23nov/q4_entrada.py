#!/usr/bin/env python3
"""Exploratorio (dias vistos): filtro de ENTRADA 'no entrar en el lado si F5 de la 1.a colocacion >= p80 de su moneda'. Cortes p80 por moneda con lados 03-14 Nov (a congelar para >=18-Nov).
Evalua 05-14 (y 03-04 aparte): diff EV(q0-3) - EV(q4), dPnL, IC90 dias, placebo permutando la etiqueta dentro de dia x moneda (K=2000, numpy)."""
import glob, json, numpy as np, pandas as pd
rng = np.random.default_rng(20261124)
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob('../r1v2_eval/out_p0/p0_ordenes_2026-11-*.pkl'))], ignore_index=True)
def lados(Rv):
    return Rv.sort_values('t_dec').groupby(['dia', 'mid', 'lado']).agg(cost=('cost', 'sum'), pnl=('pnl', 'sum'), coin=('coin', 'first'), f0=('f5t', 'first')).reset_index()
cortes = {c: float(np.quantile(x.f0, 0.8)) for c, x in lados(R[R.bloq == 0]).groupby('coin')}
res = dict(cortes_p80_por_moneda_03_14=cortes)
for b in (0, 1):
    for tramo, sel in (('C_05_14', R.dia >= '2026-11-05'), ('posthoc_03_04', R.dia < '2026-11-05')):
        S = lados(R[(R.bloq == b) & sel]); S['alto'] = S.f0 >= S.coin.map(cortes)
        D = sorted(S.dia.unique()); di = S.dia.map({d: i for i, d in enumerate(D)}).values
        def stats(a):
            M = np.zeros((len(D), 4)); np.add.at(M, (di, np.where(a, 2, 0)), S.pnl.values); np.add.at(M, (di, np.where(a, 3, 1)), S.cost.values); return M
        def dif(M): s = M.sum(0); return s[0]/s[1] - s[2]/s[3] if s[1] > 0 and s[3] > 0 else np.nan
        M = stats(S.alto.values); obs = dif(M)
        bs = np.array([dif(M[rng.integers(0, len(D), len(D))]) for _ in range(2000)]); bs = bs[np.isfinite(bs)]
        grp = list(S.groupby(['dia', 'coin']).indices.values()); pl = []
        for _ in range(2000):
            a = S.alto.values.copy()
            for ix in grp: a[ix] = rng.permutation(a[ix])
            pl.append(dif(stats(a)))
        pl = np.array(pl); per = [dif(M[[i]]) for i in range(len(D))]
        res[f'bloq{b}_{tramo}'] = dict(n_lados=len(S), n_q4=int(S.alto.sum()), diff=round(obs, 4), ic90=[round(np.percentile(bs, 5), 4), round(np.percentile(bs, 95), 4)] if len(bs) else None,
            dias_pos=f'{int(np.nansum(np.array(per) > 0))}/{len(D)}', placebo_p=round(float((pl >= obs).mean()), 4), pnl_sin_filtro=round(S.pnl.sum(), 2), pnl_con_filtro=round(S[~S.alto].pnl.sum(), 2),
            ev_q4=round(S[S.alto].pnl.sum()/S[S.alto].cost.sum(), 4), ev_resto=round(S[~S.alto].pnl.sum()/S[~S.alto].cost.sum(), 4),
            por_moneda={c: dict(n_q4=int(x.alto.sum()), ev_q4=round(x[x.alto].pnl.sum()/max(x[x.alto].cost.sum(), 1e-9), 3), ev_resto=round(x[~x.alto].pnl.sum()/x[~x.alto].cost.sum(), 3)) for c, x in S.groupby('coin')},
            sin_2_mejores_dias=round(dif(np.delete(M, np.argsort(M[:, 0] + M[:, 2])[-2:], axis=0)), 4))
json.dump(res, open('out/q4_entrada.json', 'w'), indent=1); print(json.dumps(res, indent=0))
