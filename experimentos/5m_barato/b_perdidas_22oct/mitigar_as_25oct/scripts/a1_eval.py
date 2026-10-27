#!/usr/bin/env python3
"""a1_eval.py -- PREREG_A1: walk-forward por dia, terciles del TRAIN, EXCESO vs placebo de misma fraccion de EUR, gate K=8."""
import os, sys, glob, hashlib, json, numpy as np, pandas as pd
from scipy import stats
AQ = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.join(AQ, '..')
assert hashlib.sha256(open(os.path.join(BASE, 'PREREG_A1.md'), 'rb').read()).hexdigest() == open(os.path.join(BASE, 'PREREG_A1.sha256')).read().split()[0]
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'
X = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(DL + 'r_2026-10-*.pkl'))], ignore_index=True)
X = X[X.dia >= '2026-10-06']
dias = sorted(X.dia.unique()); test = [d for d in dias if d >= '2026-10-09']
FE = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8']; K = len(FE)
out = {'n_rellenos': int(len(X)), 'dias': dias, 'coste_total': float(X.coste.sum()), 'EV_total': float(X.pnl.sum() / X.coste.sum()),
       'cobertura': {f: float(np.isfinite(X[f]).mean()) for f in FE}}
def terc(v, c): return np.where(v <= c[0], 0, np.where(v <= c[1], 1, 2))
def corre(f, suf='', inv=False):
    filas = []; clus = []; flags_c = []; flags_f = []
    for d in test:
        tr = X[(X.dia < d) & np.isfinite(X[f + suf])]; te = X[X.dia == d]
        c = np.quantile(tr[f + suf].values, [1/3, 2/3])
        if c[0] == c[1]: c = [c[0], np.nextafter(c[0], np.inf)] if (tr[f+suf] <= c[0]).mean() < 0.67 else [np.nextafter(c[0], -np.inf), c[0]]
        tt = terc(tr[f + suf].values, c); ev = [tr.pnl.values[tt == k].sum() / max(tr.coste.values[tt == k].sum(), 1e-9) for k in range(3)]
        sel = int(np.argmax(ev)) if inv else int(np.argmin(ev))
        v = te[f + suf].values; m = np.isfinite(v) & (terc(np.nan_to_num(v, nan=-9e18), c) == sel)
        fd = te.coste.values[m].sum() / te.coste.sum()
        exc = fd * te.pnl.sum() - te.pnl.values[m].sum()
        evr = te.pnl.values[~m].sum() / max(te.coste.values[~m].sum(), 1e-9); eva = te.pnl.sum() / te.coste.sum()
        filas.append(dict(dia=d, sel=sel, frac_eur=fd, exc=exc, ev_ret=evr, ev_all=eva, ev_flag=te.pnl.values[m].sum() / max(te.coste.values[m].sum(), 1e-9), n_flag=int(m.sum()), n=len(te)))
        g = pd.DataFrame({'fin': te.fin.values, 'e': fd * te.pnl.values - np.where(m, te.pnl.values, 0)}).groupby('fin').e.sum(); clus.append(g.values)
        if suf == '':
            vc = te[f + '_c'].values; bc = te['bid_c'].values; okc = np.isfinite(vc) & (bc > 0.10) & (bc <= 0.30)
            flags_c.append((terc(vc[okc], c) == sel).mean() if okc.sum() else np.nan); flags_f.append(m[np.isfinite(v)].mean())
    T = pd.DataFrame(filas); e = T.exc.values; n = len(e)
    t = e.mean() / (e.std(ddof=1) / np.sqrt(n)); p = 1 - stats.t.cdf(t, n - 1); h = stats.t.ppf(0.95, n - 1) * e.std(ddof=1) / np.sqrt(n)
    cl = np.concatenate(clus); rng = np.random.default_rng(20261025); bs = [cl[rng.integers(0, len(cl), len(cl))].sum() for _ in range(1000)]
    dd = T.ev_ret.values - T.ev_all.values; hd = stats.t.ppf(0.95, n - 1) * dd.std(ddof=1) / np.sqrt(n)
    r = dict(exc_total=float(e.sum()), ic90_dia=[float(e.mean() - h), float(e.mean() + h)], p=float(p), sin2=float(np.sort(e)[:-2].sum()),
             dias_pos=int((e > 0).sum()), n_dias=n, ic90_cierre=[float(np.quantile(bs, 0.05)), float(np.quantile(bs, 0.95))],
             frac_eur_media=float(T.frac_eur.mean()), ev_ret_menos_all=float(dd.mean()), ic90_dif=[float(dd.mean() - hd), float(dd.mean() + hd)],
             ev_flag_medio=float(T.ev_flag.mean()), ev_ret_medio=float(T.ev_ret.mean()), sel_moda=int(T.sel.mode()[0]), sel_estab=float((T.sel == T.sel.mode()[0]).mean()))
    if suf == '': r['tasa_disparo_control'] = float(np.nanmean(flags_c)); r['tasa_disparo_prerelleno'] = float(np.nanmean(flags_f))
    return r, T
res = {}
for f in FE:
    r, T = corre(f); ri, _ = corre(f, inv=True); r2, _ = corre(f, '_250')
    r['inv_exc_total'] = ri['exc_total']; r['tau250_exc_total'] = r2['exc_total']; r['tau250_ic90_dia'] = r2['ic90_dia']
    r['por_dia'] = T.round(4).to_dict('records'); res[f] = r
ps = np.array([res[f]['p'] for f in FE]); o = np.argsort(ps); q = np.empty(K); q[o] = np.minimum.accumulate((ps[o] * K / np.arange(1, K + 1))[::-1])[::-1]
for k, f in enumerate(FE):
    r = res[f]; r['q_BH'] = float(min(q[k], 1))
    r['gate'] = {'1_ic_dia': r['ic90_dia'][0] > 0 and r['exc_total'] > 0, '2_bonf_bh': r['p'] < 0.05 / K and r['q_BH'] < 0.10, '3_sin2': r['sin2'] > 0,
                 '4_inv': r['inv_exc_total'] < 0, '5_dias': r['dias_pos'] >= 10, '6_cierre': r['ic90_cierre'][0] > 0, '7_ret': r['ic90_dif'][0] > 0}
    r['PASA'] = all(r['gate'].values())
out['rasgos'] = res
# por moneda (descriptivo, regla de todo el pool)
json.dump(out, open(os.path.join(BASE, 'datos', 'a1_resultados.json'), 'w'), indent=1, default=float)
print('n', len(X), 'EV total', round(out['EV_total'], 4), 'coste', round(out['coste_total']), 'cobertura', {k: round(v, 3) for k, v in out['cobertura'].items()})
for f in FE:
    r = res[f]
    print(f, 'PASA' if r['PASA'] else 'no', 'exc', round(r['exc_total']), 'IC90d', [round(x, 1) for x in r['ic90_dia']], 'p', round(r['p'], 4), 'qBH', round(r['q_BH'], 3),
          'sin2', round(r['sin2']), 'd+', r['dias_pos'], 'IC90c', [round(x) for x in r['ic90_cierre']], 'inv', round(r['inv_exc_total']), 'frac', round(r['frac_eur_media'], 2),
          'EVret-all', round(r['ev_ret_menos_all'], 4), [round(x, 4) for x in r['ic90_dif']], 'EVflag', round(r['ev_flag_medio'], 3), 'EVret', round(r['ev_ret_medio'], 3),
          'sel', r['sel_moda'], round(r['sel_estab'], 2), 'disp_ctrl/pre', round(r['tasa_disparo_control'], 3), round(r['tasa_disparo_prerelleno'], 3),
          'tau250', round(r['tau250_exc_total']), [round(x, 1) for x in r['tau250_ic90_dia']], 'gate', ''.join('1' if v else '0' for v in r['gate'].values()))
