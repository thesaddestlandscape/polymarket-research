#!/usr/bin/env python3
"""frente_posthoc.py -- POST-HOC DESCRIPTIVO (no decide nada; adenda declarada tras ver frente_salida.txt). Frente SIN TD, Lp=85, A+B,
unidad = primer print por mercado-lado. Cortes: tamano del primer print, tiempo hasta el relleno, T restante al relleno, tipo A/B."""
import sys, gzip, csv, random, collections
DF = sys.argv[1]; DIAS = ['2026-10-24', '2026-10-25', '2026-10-26']; U = {}
for d in DIAS:
    for r in csv.DictReader(gzip.open('%s/fr_%s.csv.gz' % (DF, d), 'rt')):
        if r['gana'] == '' or (r['ba85'] != '' and float(r['ba85']) <= float(r['bp']) + 1e-9): continue
        t0 = int(r['t0']); bp = float(r['bp']); pr = sorted((int(a), float(b), c) for a, b, c in (x.split(':') for x in r['prints'].split(';') if x)) if r['prints'] else []
        pr = [p for p in pr if p[0] >= t0 + 85]
        if not pr: continue
        tot = 0.0
        for p in pr:
            tot += p[1]
            if tot >= 5: break
        sh = min(5.0, tot); k = (r['mercado'], r['lado']); c = (pr[0][0], t0)
        if k not in U or c < U[k]['c']:
            U[k] = dict(c=c, dia=d, cie=r['cierre'], coin=r['coin'], pnl=sh * (int(r['gana']) - bp), cost=sh * bp, sz1=pr[0][1], ty=pr[0][2],
                        dt=(pr[0][0] - t0) / 1000, T=(int(r['cierre']) * 1000 - pr[0][0]) / 1000)
U = list(U.values())
def ic(L, R=1000):
    rnd = random.Random(2711); G = collections.defaultdict(lambda: [0.0, 0.0])
    for u in L: G[u['cie']][0] += u['pnl']; G[u['cie']][1] += u['cost']
    A = list(G.values()); res = sorted((lambda s: s[0] / s[1])([sum(x) for x in zip(*rnd.choices(A, k=len(A)))]) for _ in range(R))
    return res[int(.05 * R)], res[int(.95 * R)]
def lin(tag, L):
    if len(L) < 40: print('  %-28s n=%d (<40)' % (tag, len(L))); return
    c = sum(u['cost'] for u in L); lo, hi = ic(L)
    print('  %-28s n=%5d EVw=%+.3f IC90cierre=(%+.3f,%+.3f) dias=%s' % (tag, len(L), sum(u['pnl'] for u in L) / c, lo, hi,
          ' '.join('%+.2f' % (sum(u['pnl'] for u in L if u['dia'] == d) / max(1e-9, sum(u['cost'] for u in L if u['dia'] == d))) for d in DIAS)))
lin('TODO frente sin TD', U)
for nom, f, cortes in (('tam 1er print', 'sz1', (0, 5, 20, 100, 1e9)), ('dt relleno s', 'dt', (0, 1, 5, 20, 61)), ('T restante s', 'T', (0, 120, 180, 240, 301))):
    for lo_, hi_ in zip(cortes, cortes[1:]): lin('%s [%g,%g)' % (nom, lo_, hi_), [u for u in U if lo_ <= u[f] < hi_])
for ty in 'AB': lin('tipo 1er print %s' % ty, [u for u in U if u['ty'] == ty])
for lo_, hi_ in ((0, 5), (5, 1e9)): lin('BTC tam [%g,%g)' % (lo_, hi_), [u for u in U if u['coin'] == 'BTC' and lo_ <= u['sz1'] < hi_])
