#!/usr/bin/env python3
"""segfav_posthoc.py -- ADENDA POST-HOC DECLARADA (tras ver segfav_salida.txt). Descriptivo, no gate.
Separa los prints S por p_print vs askpre (ask de F antes del print): p<askpre (levanta una cotizacion MEJORADA, p.ej. puja
del barato a bb+0,01 por el espejo), p==askpre, p>askpre (barre). EV del tomador a su precio y nuestro EV al ask L=250."""
import sys, gzip, csv, glob, collections, numpy as np
FEE = 0.07; G = collections.defaultdict(lambda: {'t': [], 'n': []})
for fn in sorted(glob.glob(sys.argv[1] + '/sf_*.csv.gz')):
    for r in csv.DictReader(gzip.open(fn, 'rt')):
        if r['tipo'] != 'S' or r['gana'] == '' or r['askpre'] == '': continue
        p, ap = float(r['p_print']), float(r['askpre']); g = int(r['gana'])
        k = ('p<ask' if p < ap - 1e-9 else ('p=ask' if abs(p - ap) <= 1e-9 else 'p>ask'), 'T<180' if float(r['T_s']) < 180 else 'T>=180')
        G[k]['t'].append((5 * g - 5 * p - 5 * FEE * p * (1 - p), 5 * p + 5 * FEE * p * (1 - p), r['dia'] == '2026-10-26'))
        a, s, age = r['askF250'], r['asF250'], r['ageF250']
        if a and s and age and float(s) >= 5 and float(age) <= 30000 and 0 < float(a) < 1:
            a = float(a); G[k]['n'].append((5 * g - 5 * a - 5 * FEE * a * (1 - a), 5 * a + 5 * FEE * a * (1 - a), r['dia'] == '2026-10-26'))
def ev(v, oos=None):
    v = [x for x in v if oos is None or x[2] == oos]
    return (len(v), sum(x[0] for x in v) / sum(x[1] for x in v)) if v else (0, float('nan'))
for k in sorted(G):
    t, n = G[k]['t'], G[k]['n']
    print('%-16s tomador@print n=%5d EVw=%+.4f (OOS26 %+.4f) | nosotros@ask250 n=%5d EVw=%+.4f (OOS26 %+.4f)' % (str(k), *ev(t), ev(t, True)[1], *ev(n), ev(n, True)[1]))
