#!/usr/bin/env python3
"""c12_fill_vs_a0.py -- PREREG_COLA (sha a72007c5...). Sobre TODAS las ordenes de B del ledger (snapshot): P(relleno) y tasa de relleno por segundo en riesgo segun la cola delante al
postear (A0 = cola del ledger, nivel_precio), estratificada por moneda, con censura por la vida de la orden (fin = fuera_libro/cancelacion o relleno). Descriptivo (bootstrap por dia).
Salida datos/fill_vs_a0.txt"""
import os, json, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_posicion/'
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_COLA.md'), 'rb').read()).hexdigest().startswith('a72007c5deecc5e7')
iso = lambda s: pd.Timestamp(s).timestamp()
rows = []
for o in json.load(open(DL + 'ordenes_b.json')):
    t0 = o.get('t_post_gemelo') or o.get('t_ret')
    if t0 is None: continue
    lect = [l for l in o.get('lect', []) if (l.get('acc') or l.get('f') or 0) > 0]
    fill = bool(lect or o.get('pf') or o.get('tardio'))
    if fill:
        t1 = min([p['t_det'] for p in o.get('pf', [])] + [iso(l['ts']) for l in lect] + ([iso(o['tardio']['ts'])] if o.get('tardio') else []))
    elif o.get('t_fuera'): t1 = iso(o['t_fuera'])
    else: continue
    if t1 - t0 <= 0 or t1 - t0 > 400: continue
    rows.append(dict(oid=o['oid'], coin=o['coin'], k=o.get('k'), pc=o['precio'], A0=o['cola'], T=o['T'], fill=int(fill), vida=t1 - t0, dia=o['ts_post'][:10], size=o['size']))
X = pd.DataFrame(rows); X['bin'] = pd.cut(X.A0, [-1, 0.5, 10, 30, 80, 1e9], labels=['0', '(0,10]', '(10,30]', '(30,80]', '>80'])
rng = np.random.default_rng(20261022); out = []
def P(*a): out.append(' '.join(str(x) for x in a))
P(f'Ordenes B con vida medible: {len(X)} (rellenos {int(X.fill.sum())}, canceladas {int((1-X.fill).sum())}); vida mediana {X.vida.median():.2f} s; dias {X.dia.nunique()}')
def tasa(d): return d.fill.sum() / d.vida.sum() * 100
def ic(d):
    g = [x.index.values for _, x in d.groupby('dia')]; v = []
    for _ in range(1000):
        s = d.loc[np.concatenate([g[i] for i in rng.integers(0, len(g), len(g))])]; v.append(tasa(s))
    return np.percentile(v, [5, 95])
def tabla(d, nom):
    P(f'\n{nom}')
    for b, s in d.groupby('bin', observed=True):
        a, b2 = ic(s) if s.dia.nunique() > 1 else (np.nan, np.nan)
        P(f'   A0 {str(b):9s} n={len(s):4d} rellenos={int(s.fill.sum()):3d}  P(relleno)={s.fill.mean():.3f}  vida media {s.vida.mean():.2f}s  tasa/100 s en riesgo {tasa(s):.2f} (IC90 por dia {a:.2f},{b2:.2f})')
tabla(X, 'TODAS')
for c, s in X.groupby('coin'): tabla(s, f'MONEDA {c}')
P(f'\nCorrelacion Spearman A0 vs P(relleno) por orden: {X[["A0","fill"]].corr(method="spearman").iloc[0,1]:+.3f}; A0 vs vida (todas): {X[["A0","vida"]].corr(method="spearman").iloc[0,1]:+.3f}')
open(os.path.join(D, 'fill_vs_a0.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
