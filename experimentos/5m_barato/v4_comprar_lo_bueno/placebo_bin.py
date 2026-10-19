#!/usr/bin/env python3
"""Placebo del precursor Binance: P(movimiento orientado >=1 bp que empieza >=255 ms antes del instante) en instantes aleatorios del mismo
día y moneda (ventana viva 5m: C-300+2 s .. C-10 s) frente a los instantes de los triggers V4. Reloj E de Binance (identificación, no decisión)."""
import json, sys, random, bisect, collections
from datetime import datetime, timezone
S = sys.argv[1]
O = json.load(open(f'{S}/cron2_out.json'))
SIM = {'BTC': 'BTCUSDT', 'ETH': 'ETHUSDT', 'SOL': 'SOLUSDT', 'XRP': 'XRPUSDT', 'DOGE': 'DOGEUSDT', 'BNB': 'BNBUSDT'}
rng = random.Random(11)
from array import array
X = {}
def xs(dia, mon):
    k = (dia, mon)
    if k not in X:
        X.clear()
        v = []
        pat = ',' + SIM[mon] + ','
        for ln in open(f'{S}/x_{dia}.txt'):
            if pat not in ln: continue
            c = ln.split(',')
            try: v.append((int(c[6]), float(c[3])))
            except Exception: pass
        v.sort()
        X[k] = (v, array('q', [a for a, _ in v]))
    return X[k]
def stat(dia, mon, T, sgn, win=3000, thr=1.0, need=255):
    v, e = xs(dia, mon)
    j = bisect.bisect_right(e, T - win) - 1
    if j < 0: return None
    base = v[j][1]
    i0 = bisect.bisect_left(e, T - win); i1 = bisect.bisect_right(e, T + 300)
    for k in range(i0, i1):
        if sgn * (v[k][1] / base - 1) * 1e4 >= thr:
            return v[k][0] - T          # <0: antelación
    return 'none'
def summarize(vals, need=255):
    vals = [x for x in vals if x is not None]
    n = len(vals)
    ant = sum(1 for x in vals if x != 'none' and x < 0)
    lead = sum(1 for x in vals if x != 'none' and x <= -need)
    return n, ant, lead
ev_vals, pl_vals = [], []
byday_pl = collections.defaultdict(list)
for r in sorted(O, key=lambda r: (r['dia'], r['moneda'])):
    dia, mon = r['dia'], r['moneda']; sgn = 1 if r['lado'] == 'Up' else -1
    T = r['t_trig_ex']
    ev_vals.append(stat(dia, mon, T, sgn))
    # placebo: 300 instantes en la ventana viva de mercados cuyo cierre esté en el mismo día (se generan por cierre aleatorio de la jornada)
    d0 = int(datetime.fromisoformat(dia + 'T00:00:00+00:00').timestamp())
    for _ in range(300):
        cie = d0 + 900 * rng.randint(1, 95)
        t = (cie - 300) * 1000 + rng.randint(2000, 290000)
        pl_vals.append(stat(dia, mon, t, sgn))
for nom, vals in (('eventos V4 (58)', ev_vals), ('placebo (mismo día/moneda/orientación)', pl_vals)):
    n, ant, lead = summarize(vals)
    print(f'{nom}: n={n} movimiento >=1bp orientado que empieza antes del instante: {ant} ({ant/n:.3f}); con antelación >=255 ms: {lead} ({lead/n:.3f})')
# por moneda BTC
for nom, mon in (('BTC', 'BTC'),):
    pass
# IC bootstrap eventos
def ci(vals, need=255, n=3000):
    vals = [x for x in vals if x is not None]; res = []
    for _ in range(n):
        s = [rng.choice(vals) for _ in vals]; res.append(sum(1 for x in s if x != 'none' and x <= -need) / len(s))
    res.sort(); return round(res[int(.05 * n)], 3), round(res[int(.95 * n)], 3)
print('IC90 eventos (>=255 ms antelación):', ci(ev_vals))
