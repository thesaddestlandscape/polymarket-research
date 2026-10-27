#!/usr/bin/env python3
"""E-RE-CM-01: EV de rellenos maker 5m pre-apertura (tb=3) vs franja de B (tb=2), poblacion on-chain. Solo lectura."""
import csv, gzip, json, random, collections, glob

DL = '/root/polymarket-research-datalogs/mapa_escala'
des = json.load(open(DL + '/des.json'))
BANDS = ['0.01-0.05', '0.05-0.10', '0.10-0.20', '0.20-0.30', '0.30-0.50', '0.50-0.70', '0.70-0.90', '0.90-0.99']
# agg[(tb, coin, banda)][dia] = [coste, pnl, reb]
agg = collections.defaultdict(lambda: collections.defaultdict(lambda: [0.0, 0.0, 0.0]))
cov = collections.defaultdict(lambda: [0.0, 0.0])
for f in sorted(glob.glob(DL + '/cells_2026-10-*.csv.gz')):
    for r in csv.DictReader(gzip.open(f, 'rt')):
        if r['marco'] != '5min' or r['tb'] not in ('2', '3'):
            continue
        c = float(r['coste']); tb = r['tb']
        g = des.get(r['mid'])
        cov[tb][0] += c
        if g is None:
            continue
        cov[tb][1] += c
        pnl = float(r['acc']) * (1.0 if g == r['lc'] else 0.0) - c
        for key in ((tb, r['coin'], r['banda']), (tb, 'ALL', r['banda']), (tb, r['coin'], 'ALL'), (tb, 'ALL', 'ALL')):
            x = agg[key][r['dia']]; x[0] += c; x[1] += pnl; x[2] += float(r['reb'])
print('cobertura desenlace en EUR:', {k: round(v[1] / v[0], 4) for k, v in cov.items()})
random.seed(20261026)
res = []
for key in sorted(agg):
    D = agg[key]; dias = sorted(D)
    C = sum(D[d][0] for d in dias); P = sum(D[d][1] for d in dias); R = sum(D[d][2] for d in dias)
    if C < 50:
        continue
    ev = P / C
    bs = []
    for _ in range(2000):
        s = random.choices(dias, k=len(dias)); cc = sum(D[d][0] for d in s)
        bs.append(sum(D[d][1] for d in s) / cc if cc else 0)
    bs.sort(); lo, hi = bs[100], bs[1899]; p1 = sum(1 for b in bs if b <= 0) / len(bs)
    pos = sum(1 for d in dias if D[d][1] > 0)
    top = sorted(dias, key=lambda d: D[d][1], reverse=True)[2:]
    c2 = sum(D[d][0] for d in top); sin2 = sum(D[d][1] for d in top) / c2 if c2 else float('nan')
    res.append(dict(tb=key[0], coin=key[1], banda=key[2], n_dias=len(dias), coste_dia=C / len(dias), ev=ev, ev_reb=(P + R) / C,
                    lo=lo, hi=hi, p1=p1, dpos=pos, sin2=sin2))
# BH-FDR sobre celdas pre (tb=3) coin x banda concretas
cel = [x for x in res if x['tb'] == '3' and x['coin'] != 'ALL' and x['banda'] != 'ALL']
cel.sort(key=lambda x: x['p1']); m = len(cel)
for i, x in enumerate(cel, 1):
    x['bh'] = x['p1'] <= 0.10 * i / m
ok_bh = set()
kmax = max([i for i, x in enumerate(cel, 1) if x['p1'] <= 0.10 * i / m], default=0)
for i, x in enumerate(cel, 1):
    x['bh'] = i <= kmax
for x in res:
    b = x['banda']; bn = BANDS[int(b)] if b != 'ALL' else 'ALL'
    flag = ''
    if x['tb'] == '3' and x['coin'] != 'ALL' and b != 'ALL':
        if x['n_dias'] >= 12 and x['lo'] > 0 and x['sin2'] > 0 and x.get('bh'):
            flag = 'REABRIBLE'
    print('%s tb%s %-4s %-9s dias %2d coste/dia %9.1f EV %+.4f (+reb %+.4f) IC90 dias (%+.4f,%+.4f) p1 %.3f dias+ %2d sin2 %+.4f %s' % (
        'PRE' if x['tb'] == '3' else 'IN ', x['tb'], x['coin'], bn, x['n_dias'], x['coste_dia'], x['ev'], x['ev_reb'], x['lo'], x['hi'], x['p1'], x['dpos'], x['sin2'], flag))
print('celdas pre miradas (BH):', m, 'supervivientes BH q=0,10:', kmax)
