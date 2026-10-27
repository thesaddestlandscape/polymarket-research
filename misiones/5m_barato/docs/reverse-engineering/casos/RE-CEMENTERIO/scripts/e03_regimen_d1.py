#!/usr/bin/env python3
"""E-RE-CM-03: persistencia diaria del EV maker barato de la poblacion (H50). Solo lectura."""
import csv, gzip, json, random, collections, glob
DL = '/root/polymarket-research-datalogs/mapa_escala'
des = json.load(open(DL + '/des.json'))
D = collections.defaultdict(lambda: collections.defaultdict(lambda: [0.0, 0.0]))
for f in sorted(glob.glob(DL + '/cells_2026-10-*.csv.gz')):
    for r in csv.DictReader(gzip.open(f, 'rt')):
        if r['marco'] != '5min' or r['tb'] not in ('1', '2') or r['banda'] not in ('1', '2', '3'):
            continue
        g = des.get(r['mid'])
        if g is None:
            continue
        grp = 'BTC' if r['coin'] == 'BTC' else ('ALT3' if r['coin'] in ('ETH', 'SOL', 'XRP') else None)
        if not grp:
            continue
        c = float(r['coste']); x = D[grp][r['dia']]; x[0] += c; x[1] += float(r['acc']) * (g == r['lc']) - c
def pear(a, b):
    n = len(a); ma = sum(a) / n; mb = sum(b) / n
    sa = sum((x - ma) ** 2 for x in a) ** .5; sb = sum((y - mb) ** 2 for y in b) ** .5
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sa * sb)
random.seed(20261026)
for grp in ('BTC', 'ALT3'):
    dias = sorted(D[grp]); ev = [D[grp][d][1] / D[grp][d][0] for d in dias]
    r = pear(ev[:-1], ev[1:]); cnt = 0
    for _ in range(5000):
        e = ev[:]; random.shuffle(e)
        if pear(e[:-1], e[1:]) >= r: cnt += 1
    op = [d for i, d in enumerate(dias) if i > 0 and ev[i - 1] > 0]
    allp = dias[1:]
    evop = sum(D[grp][d][1] for d in op) / sum(D[grp][d][0] for d in op) if op else float('nan')
    evall = sum(D[grp][d][1] for d in allp) / sum(D[grp][d][0] for d in allp)
    print(grp, 'serie', ' '.join('%+.3f' % x for x in ev))
    print(grp, 'r=%.3f p_perm=%.4f | P opera %d/%d dias EV %+.4f vs todos %+.4f dEV %+.4f' % (r, cnt / 5000, len(op), len(allp), evop, evall, evop - evall))
