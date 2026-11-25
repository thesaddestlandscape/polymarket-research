#!/usr/bin/env python3
"""SO-1a' (ADENDA_SO1_01, sha f664bfad...): REST por tamano EXACTO del remanente. Solo lectura, <200 MB."""
import os, pickle, json
import numpy as np, pandas as pd
import so1_traza as S

HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
SH = [-30000, -20000, -10000, 10000, 20000, 30000]


def match(ser, t0, t1, target):
    if ser is None or len(ser[0]) == 0 or not (target > 0): return False
    t, s = ser; prev = np.concatenate([[0.0], s[:-1]]); m = (t >= t0) & (t <= t1)
    dl = s[m] - prev[m]; tol = max(0.02 * target, 0.05)
    return bool(np.any(np.abs(dl - target) <= tol))


def main():
    d = pickle.load(open(S.BASE + 'tomador_202.pkl', 'rb'))
    d['cost'] = d.real_q * d.L; d['pnl'] = d.real_q * (d.gana - d.L)
    d['c1'] = d.causa.str.startswith('1_'); d['tp'] = d.causa == 'TP'
    d['rem_sh'] = d.tk_rem * d.tk_sz
    e1a = d[d.c1 & (d.tk_tipo == 'compra_comp') & (d.tk_rem > 0.01)]
    pool = e1a.rem_sh.values; rng = np.random.default_rng(20261119)
    cache = {}; rows = []
    for _, r in d.iterrows():
        m = S.TOKM.get(str(r.tok))
        if m is None: continue
        fn = S.MK + f'{m[0]}_{m[1]}.gz'
        if not os.path.exists(fn): continue
        if fn not in cache:
            if len(cache) > 8: cache.pop(next(iter(cache)))
            cache[fn] = S.parse(fn)
        B = cache[fn]; comp = 'N' if m[2] == 'YES' else 'Y'; t3 = int(r.real_tm3)
        ser = B[comp].get(int(round((1.0 - float(r.tk_eq)) * 100)) * 10)
        o = dict(oid=r.oid, c1=bool(r.c1), tp=bool(r.tp), comp=r.tk_tipo == 'compra_comp', rem=float(r.tk_rem) > 0.01,
                 en_L=bool(r.en_L), cost=float(r.cost), pnl=float(r.pnl), dia=r.dia, estructura=r.estructura)
        if o['rem']:
            tg = float(r.rem_sh); o['hit'] = match(ser, t3 - 50, t3 + 500, tg)
            o['pl'] = np.mean([match(ser, t3 + s - 50, t3 + s + 500, tg) for s in SH]); o['plmax_each'] = [match(ser, t3 + s - 50, t3 + s + 500, tg) for s in SH]
        else:
            tgs = rng.choice(pool, 20); o['hit'] = float(np.mean([match(ser, t3 - 50, t3 + 500, tg) for tg in tgs]))
            o['pl'] = float(np.mean([match(ser, t3 + s - 50, t3 + s + 500, tg) for s in SH for tg in tgs[:5]])); o['plmax_each'] = None
        rows.append(o)
    R = pd.DataFrame(rows); R.to_pickle(HERE + 'so1b_filas.pkl')
    def rep(g, lab):
        pm = np.array([x for x in g.plmax_each if x is not None]) if g.plmax_each.notna().any() else None
        plmax = pm.mean(0).max() if pm is not None and len(pm) else g.pl.mean()
        print(f"{lab:34s} n={len(g):3d} tasa={g.hit.astype(float).mean():.3f} placebo_medio={g.pl.mean():.3f} placebo_max={plmax:.3f}")
    rep(R[R.c1 & R.comp & R.rem], "E1a' clase1 comp rem>1%")
    rep(R[R.c1 & R.comp & R.rem & R.en_L], "  en_L")
    rep(R[R.c1 & R.comp & R.rem & ~R.en_L], "  mas_alla")
    rep(R[R.tp & R.comp & R.rem], "TP comp rem>1% (replica)")
    rep(R[R.c1 & R.comp & ~R.rem], "ctrl(i) clase1 rem<=1% (tg azar)")
    rep(R[R.tp & R.comp & ~R.rem], "ctrl(i) TP rem<=1% (tg azar)")
    g = R[R.c1 & R.comp & R.rem]
    for k, gg in g.groupby(g.hit.astype(bool)):
        print('  E1a hit=', k, 'n', len(gg), 'EV', round(gg.pnl.sum() / gg.cost.sum(), 3), 'por dia', gg.groupby('dia').size().to_dict())


if __name__ == '__main__':
    main()
