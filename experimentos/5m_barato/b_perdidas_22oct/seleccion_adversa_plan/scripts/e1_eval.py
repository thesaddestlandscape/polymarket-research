#!/usr/bin/env python3
"""e1_eval.py -- evalua datos/e1_D.csv.gz segun PREREG_E1_CANCELAR_MS.md §4-5. Salida por stdout + datos/e1_resultados.json"""
import os, json, numpy as np, pandas as pd
DD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
DESC = ['2026-10-17', '2026-10-18', '2026-10-19']; TEST = ['2026-10-20', '2026-10-21', '2026-10-22']
X = pd.concat([pd.read_csv(f'{DD}/e1_{d}.csv.gz') for d in DESC + TEST], ignore_index=True)
X['coste'] = np.where(X.fill == 1, 5 * X.obj, 0.0); X['pnl'] = np.where(X.fill == 1, 5 * (X.gana - X.obj), 0.0)
B = X[X['var'] == 'BASE'].set_index('mid')
RULES = ['S1_x2_w500', 'S1_x2_w2000', 'S1_x4_w500', 'S1_x4_w2000', 'S2_w500', 'S2_w2000', 'S3_w2000']
SH = [f'SH{s:+d}' for s in (-240, -180, -120, -60, 60, 120, 180, 240)]
rng = np.random.default_rng(20261022)
def paired(var, dias):
    V = X[(X['var'] == var) & X.dia.isin(dias)].set_index('mid'); b = B.loc[V.index]
    dp = V.pnl - b.pnl
    rem = (b.fill == 1) & ((V.fill == 0) | (V.r != b.r))
    evit = -b.pnl[rem & (b.gana == 0)].sum(); sacr = b.pnl[rem & (b.gana == 1)].sum(); sust = V.pnl[rem & (V.fill == 1)].sum()
    return dict(dpnl=dp.sum(), dpe=dp.sum() / b.coste.sum(), ev_base=b.pnl.sum() / b.coste.sum(), ev_var=V.pnl.sum() / max(V.coste.sum(), 1e-9),
                ret=V.coste.sum() / b.coste.sum(), n_base=int(b.fill.sum()), n_var=int(V.fill.sum()), evit=evit, sacr=sacr, sust=sust,
                pnl_base=b.pnl.sum()), dp, b
def boot(dp, b, key):
    g = pd.DataFrame({'dp': dp.values, 'c': b.coste.values, 'k': b[key].values}).groupby('k').sum()
    a = g.dp.values; c = g.c.values; n = len(a); s = []
    for _ in range(2000):
        i = rng.integers(0, n, n); s.append(a[i].sum() / c[i].sum())
    return [float(np.percentile(s, 5)), float(np.percentile(s, 95))]
R = {}
for per, dias in (('DESC', DESC), ('TEST', TEST)):
    print(f'===== {per} {dias}')
    bb = B[B.dia.isin(dias)]
    print(f'BASE mercados {len(bb)} rellenos {int(bb.fill.sum())} ({bb.fill.mean():.3f}) acierto rellenos {bb[bb.fill==1].gana.mean():.3f} no rellenos {bb[bb.fill==0].gana.mean():.3f} '
          f'EV {bb.pnl.sum()/bb.coste.sum():+.4f} PnL {bb.pnl.sum():+.1f} coste {bb.coste.sum():.1f}')
    for r in RULES:
        res = {}
        for v in ('D100', 'D250', 'D0', 'INV') + tuple(SH):
            m, dp, b = paired(f'{r}|{v}', dias); res[v] = m
            if v == 'D100':
                m['ic_cierre'] = boot(dp, b, 'fin'); m['ic_dia'] = boot(dp, b, 'dia')
                m['por_dia'] = {d: float(dp[b.dia == d].sum()) for d in dias}
                m['por_moneda'] = {a: float(dp[b.act == a].sum()) for a in ('ETH', 'SOL', 'XRP')}
        sh = [res[s]['dpe'] for s in SH]; m = res['D100']
        print(f"{r:12s} dPnL {m['dpnl']:+7.1f} ({m['dpe']:+.4f}/EUR) IC90c {m['ic_cierre'][0]:+.4f},{m['ic_cierre'][1]:+.4f} dias {' '.join(f'{x:+.1f}' for x in m['por_dia'].values())} | "
              f"EV {m['ev_base']:+.4f}->{m['ev_var']:+.4f} ret {m['ret']:.2f} evit {m['evit']:.1f} sacr {m['sacr']:.1f} sust {m['sust']:+.1f} | "
              f"D250 {res['D250']['dpe']:+.4f} D0 {res['D0']['dpe']:+.4f} INV {res['INV']['dpe']:+.4f} placebo max {max(sh):+.4f} media {np.mean(sh):+.4f} | mon {' '.join(f'{k}{v:+.1f}' for k,v in m['por_moneda'].items())}")
        R[(per, r)] = res
    if per == 'DESC':
        obs = {r: R[(per, r)]['D100']['dpe'] for r in RULES}; best = max(obs, key=obs.get)
        mx = [max(R[(per, r)][s]['dpe'] for r in RULES) for s in SH]
        pfw = (1 + sum(x >= obs[best] for x in mx)) / (1 + len(SH))
        print(f'ELEGIDA en DESC: {best} ({obs[best]:+.4f}/EUR); p familiar (max-est. contra 8 desplazamientos) {pfw:.3f}')
m = R[('TEST', best)]; d = m['D100']
G = dict(G1=d['dpnl'] > 0 and d['ic_cierre'][0] > 0, G2=sum(v > 0 for v in d['por_dia'].values()) >= 2,
         G3=d['dpe'] > m['INV']['dpe'] and d['dpe'] > max(m[s]['dpe'] for s in SH), G4=d['ev_var'] > d['ev_base'], G5=m['D250']['dpnl'] > 0, G6=d['ret'] >= 0.5)
print('GATE TEST', best, G, '->', 'PROMISING' if all(G.values()) else 'REJECTED')
json.dump({f'{k[0]}|{k[1]}': v for k, v in R.items()} | {'elegida': best, 'gate': G}, open(f'{DD}/e1_resultados.json', 'w'), default=float, indent=1)
