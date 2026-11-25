#!/usr/bin/env python3
"""[v2, ADENDA_SO_A1c: lee so1*_v2] SO-2 (PREREG_SO2_19nov.md, sha 83f46a06...): tasa de clase 1 NONE por tercil F5_t en t_dec. Solo lectura, <300 MB."""
import os, pickle
import numpy as np, pandas as pd
import so1_traza_v2 as S

HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
C0, C1 = 3.526360511779785, 4.717426776885986


def top(sidebook, t):
    best = None
    for p, (tt, ss) in sidebook.items():
        i = np.searchsorted(tt, t, side='right') - 1
        if i >= 0 and ss[i] > 0 and (best is None or p > best[0]): best = (p, ss[i])
    return best


def main():
    O = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv',
                    usecols=['oid', 'tok', 'precio', 't_dec', 'dia', 'fill', 'coste', 'pnl'], dtype={'tok': str})
    a = pd.read_pickle(HERE + 'so1_filas_v2.pkl')[['oid', 'c1', 'tt', 'rem_estado']]
    b = pd.read_pickle(HERE + 'so1b_filas_v2.pkl')[['oid', 'hit']]
    k = a.merge(b, on='oid', how='left')
    k['traza'] = k.tt.fillna(False).astype(bool) | (k.hit.fillna(0).astype(float) >= 1)
    EXC = set(k.loc[k.rem_estado != 'ok', 'oid'])      # ADENDA_SO_A1c / review: sin resto fiable => fuera de O ANTES de terciles y tasas
    k['NONE'] = k.c1 & ~k.traza
    n0 = len(O); O = O[~O.oid.isin(EXC)].copy(); print(f'SO-2: oid con rem_estado != ok quitados de O: {n0 - len(O)} (de {n0}; {len(O)} restantes)')
    O = O.merge(k[['oid', 'c1', 'NONE', 'traza']], on='oid', how='left')
    for c in ['c1', 'NONE', 'traza']: O[c] = O[c].fillna(False).astype(bool)
    O['tok_s'] = O.tok.astype(str); O = O.sort_values('tok_s')
    cache = {}; f5 = []
    for _, r in O.iterrows():
        m = S.TOKM.get(r.tok_s); v = np.nan
        if m is not None:
            fn = S.MK + f'{m[0]}_{m[1]}.gz'
            if os.path.exists(fn):
                if fn not in cache:
                    cache.clear(); cache[fn] = S.parse(fn)
                B = cache[fn]; own = 'Y' if m[2] == 'YES' else 'N'; comp = 'N' if own == 'Y' else 'Y'
                t = int(r.t_dec * 1000); tc = top(B[comp], t); to = top(B[own], t)
                if tc is not None and not (to is not None and to[0] + tc[0] >= 1000): v = float(np.log1p(tc[1]))
        f5.append(v)
    O['F5t'] = f5
    O['terc'] = np.where(O.F5t.isna(), 'inval', np.where(O.F5t <= C0, 'bajo', np.where(O.F5t <= C1, 'medio', 'alto')))
    O.to_pickle(HERE + 'so2_ordenes_v2.pkl')
    V = O[O.terc != 'inval'].copy()
    print('ordenes', len(O), 'validas', len(V), 'por dia validas', V.groupby('dia').size().to_dict())
    g = O.groupby('terc').agg(n=('oid', 'size'), fills=('fill', 'sum'), c1=('c1', 'sum'), NONE=('NONE', 'sum'), traza=('traza', 'sum'),
                              coste=('coste', 'sum'), pnl=('pnl', 'sum'))
    g['r_NONE'] = (g.NONE / g.n).round(4); g['p_fill'] = (g.fills / g.n).round(4); g['EV_fills'] = (g.pnl / g.coste).round(3)
    print(g)
    V['bm'] = V.terc.isin(['bajo', 'medio'])
    def stat(lab):
        ra = V.NONE[lab == False].mean(); rb = V.NONE[lab].mean(); return ra - rb, ra, rb
    s0, ra, rb = stat(V.bm.values)
    rng = np.random.default_rng(20261119); cnt = 0; dias = V.dia.values; bm = V.bm.values.copy()
    idx = {d: np.where(dias == d)[0] for d in np.unique(dias)}
    for _ in range(2000):
        p = bm.copy()
        for d, ii in idx.items(): p[ii] = rng.permutation(bm[ii])
        if stat(p)[0] >= s0 - 1e-12: cnt += 1
    pval = (cnt + 1) / 2001
    print(f"r_alto={ra:.4f} r_bajo+medio={rb:.4f} ratio={rb / ra if ra > 0 else float('nan'):.3f} stat={s0:.4f} p={pval:.4f}")
    ver = 'ACEPTA' if (rb <= 0.5 * ra and pval < 0.10) else ('REFUTA' if rb >= ra else 'INCONCLUSO')
    print('veredicto SO-2:', ver)
    # descriptivo por dia
    print(V.groupby(['dia', 'bm']).agg(n=('oid', 'size'), NONE=('NONE', 'sum'), fills=('fill', 'sum'), pnl=('pnl', 'sum'), coste=('coste', 'sum')))


if __name__ == '__main__':
    main()
