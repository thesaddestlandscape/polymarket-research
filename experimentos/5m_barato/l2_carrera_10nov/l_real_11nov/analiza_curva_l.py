#!/usr/bin/env python3
"""analiza_curva_l.py STAMP [STAMP2 ...] -- curva EV(l) de CXB-true con motor v3 (out_l/CXL_<STAMP>_<D>.pkl de passT_cxb_l.py), TRAIN 26-Oct..09-Nov (15 dias; HOLD NO se lee). Solo lectura, 0 ordenes.
Metricas como analiza_cxb_v3.py (mismas definiciones): EV ponderado por EUR = sum pnl / sum coste (rebate 0,2 de la comision, igual que el motor), IC90 bootstrap por DIAS y por CIERRE (cluster `fin`), sin 2 mejores dias, dias+,
incremental vs GEO1 (misma colocacion, sin cancelar), por moneda y por L (descriptivo). Dosis-respuesta: se ajusta la pendiente de EV en l (OLS sobre l = 35..150 de las 7 variantes fijas) con bootstrap por dias.
Variante EMP = l muestreado del pool empirico de anclas propias (anclas_l_real.json) + PROC=3 ms (no medido). Sin multiplicidad corregida (declarado: K=8 variantes de l, EXPLORATORY)."""
import sys, os, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
DIAS = ['2026-10-26', '2026-10-27', '2026-10-28', '2026-10-29', '2026-10-30', '2026-10-31', '2026-11-01', '2026-11-02', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-07', '2026-11-08', '2026-11-09']
LS = [35, 45, 60, 80, 100, 120, 150]; VARS = [f'CXB{l}' for l in LS] + ['CXBEMP']; B = 20000; rng = np.random.default_rng(20261111)


def run(stamp):
    X = [pd.read_pickle(H + f'out_l/CXL_{stamp}_{d}.pkl') for d in DIAS if os.path.exists(H + f'out_l/CXL_{stamp}_{d}.pkl')]
    dias = [d for d in DIAS if os.path.exists(H + f'out_l/CXL_{stamp}_{d}.pkl')]; nd = len(dias)
    A = pd.concat([x['A'] for x in X], ignore_index=True); R = pd.concat([x['R'] for x in X], ignore_index=True); assert A.dia.max() <= '2026-11-09'
    def day(v, c, by=None):
        a = A[A['var'] == v] if by is None else A[(A['var'] == v) & by(A)]
        return a.groupby('dia')[c].sum().reindex(dias).fillna(0).values
    def st(v, by=None):
        num, den = day(v, 'pnl', by), day(v, 'cost', by); ev = num.sum() / den.sum() if den.sum() > 0 else np.nan
        ix = rng.integers(0, nd, (B, nd)); bs = num[ix].sum(1) / np.maximum(den[ix].sum(1), 1e-9); o = np.argsort(-num)[2:]
        rv = R[R['var'] == v] if by is None else None
        icc = (np.nan, np.nan)
        if rv is not None and len(rv):
            cl = rv.groupby('fin')[['pnl', 'cost']].sum().values; ixc = rng.integers(0, len(cl), (4000, len(cl))); bc = cl[:, 0][ixc].sum(1) / np.maximum(cl[:, 1][ixc].sum(1), 1e-9); icc = (np.quantile(bc, .05), np.quantile(bc, .95))
        return dict(var=v, fills=int(day(v, 'n_fill', by).sum()), canc=int(day(v, 'n_canc', by).sum()), cost=round(float(den.sum()), 1), pnl=round(float(num.sum()), 1), ev=round(float(ev), 4),
                    ic90_dias=(round(float(np.quantile(bs, .05)), 3), round(float(np.quantile(bs, .95)), 3)), ic90_cierre=(round(float(icc[0]), 3), round(float(icc[1]), 3)),
                    ev_sin2=round(float(num[o].sum() / den[o].sum()), 4) if den[o].sum() > 0 else np.nan, dias_pos=f'{int((num > 0).sum())}/{nd}', pnl_dia=num)
    rows = {v: st(v) for v in ['G0', 'GEO1'] + VARS}
    print(f'\n=== STAMP {stamp}: TRAIN {dias[0]}..{dias[-1]} ({nd} dias)')
    print(pd.DataFrame([{k: v for k, v in r.items() if k != 'pnl_dia'} for r in rows.values()]).to_string(index=False))
    inc = []
    for v in VARS:
        d = rows[v]['pnl_dia'] - rows['GEO1']['pnl_dia']; ix = rng.integers(0, nd, (B, nd)); bs = d[ix].mean(1)
        inc.append(dict(var=v, dpnl_total=round(float(d.sum()), 1), ic90_dias_por_dia=(round(float(np.quantile(bs, .05)), 2), round(float(np.quantile(bs, .95)), 2)), dias_pos=f'{int((d > 0).sum())}/{nd}'))
    print('--- incremental vs GEO1 (pnl evitado/ganado por la regla, misma colocacion)'); print(pd.DataFrame(inc).to_string(index=False))
    # dosis-respuesta: pendiente EV por +40 ms (OLS sobre las 7 l fijas, bootstrap por dias de la razon de sumas)
    xs = np.array(LS, float); ix = rng.integers(0, nd, (4000, nd)); sl = []
    nums = np.stack([rows[f'CXB{l}']['pnl_dia'] for l in LS]); dens = np.stack([day(f'CXB{l}', 'cost') for l in LS])
    for b in ix:
        evb = nums[:, b].sum(1) / np.maximum(dens[:, b].sum(1), 1e-9); sl.append(np.polyfit(xs, evb, 1)[0] * 40)
    evs = np.array([rows[f'CXB{l}']['ev'] for l in LS]); print(f'--- pendiente EV por +40 ms: {np.polyfit(xs, evs, 1)[0] * 40:.4f}  IC90 dias ({np.quantile(sl, .05):.4f}, {np.quantile(sl, .95):.4f})')
    print('--- por moneda (fills, coste, pnl, EV)')
    for v in ['G0', 'GEO1', 'CXB35', 'CXB45', 'CXB60', 'CXB100', 'CXB150', 'CXBEMP']:
        out = {}
        for c in ['ETH', 'SOL', 'XRP']:
            a = A[(A['var'] == v) & (A.act == c)]; out[c] = (int(a.n_fill.sum()), round(float(a.cost.sum()), 0), round(float(a.pnl.sum()), 1), round(float(a.pnl.sum() / max(a.cost.sum(), 1e-9)), 3))
        print(v, out)
    print('--- por L (fills, pnl, EV)')
    for v in ['GEO1', 'CXB35', 'CXB60', 'CXB100', 'CXBEMP']:
        a = A[A['var'] == v].groupby('L').agg(n=('n_fill', 'sum'), cost=('cost', 'sum'), pnl=('pnl', 'sum')); print(v, {str(L): (int(r.n), round(float(r.pnl), 1), round(float(r.pnl / max(r.cost, 1e-9)), 3)) for L, r in a.iterrows()})
    print('ramas del sello (suma de dias):', {k: int(sum(x['ramas'].get(k, 0) for x in X)) for k in ('sig', 'amb', 'nosig', 'guard', 'sinev')}, 'dhi por dia:', [x.get('dhi') for x in X])
    json.dump(dict(stamp=stamp, dias=dias, variantes={v: {k: x for k, x in r.items() if k != 'pnl_dia'} for v, r in rows.items()}, incremental=inc), open(H + f'out_l/curva_{stamp}.json', 'w'), indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))


if __name__ == '__main__':
    for s in sys.argv[1:]: run(s)
