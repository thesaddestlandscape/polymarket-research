#!/usr/bin/env python3
"""E-RE-CM-02: EV poblacional maker 5m banda barata T 60-300 s, BTC vs ETH+SOL+XRP, DESC 06-13 / HOLD 14-21. Solo lectura."""
import csv, gzip, json, random, collections, glob

DL = '/root/polymarket-research-datalogs/mapa_escala'
des = json.load(open(DL + '/des.json'))
BN = {'1': '0.05-0.10', '2': '0.10-0.20', '3': '0.20-0.30'}
agg = collections.defaultdict(lambda: collections.defaultdict(lambda: [0.0, 0.0, 0.0]))
mk = collections.defaultdict(lambda: collections.defaultdict(float))
for f in sorted(glob.glob(DL + '/cells_2026-10-*.csv.gz')):
    for r in csv.DictReader(gzip.open(f, 'rt')):
        if r['marco'] != '5min' or r['tb'] not in ('1', '2') or r['banda'] not in BN:
            continue
        g = des.get(r['mid'])
        if g is None:
            continue
        grp = 'BTC' if r['coin'] == 'BTC' else ('ALT3' if r['coin'] in ('ETH', 'SOL', 'XRP') else None)
        if grp is None:
            continue
        mitad = 'DESC' if r['dia'] <= '2026-10-13' else 'HOLD'
        c = float(r['coste']); pnl = float(r['acc']) * (1.0 if g == r['lc'] else 0.0) - c
        for b in (BN[r['banda']], '0.05-0.30'):
            x = agg[(grp, mitad, b)][r['dia']]; x[0] += c; x[1] += pnl; x[2] += float(r['reb'])
            mk[(grp, mitad, b)][r['maker']] += c
random.seed(20261026)
for key in sorted(agg):
    D = agg[key]; dias = sorted(D)
    C = sum(D[d][0] for d in dias); P = sum(D[d][1] for d in dias); R = sum(D[d][2] for d in dias)
    bs = []
    for _ in range(2000):
        s = random.choices(dias, k=len(dias)); cc = sum(D[d][0] for d in s); bs.append(sum(D[d][1] for d in s) / cc)
    bs.sort()
    top = sorted(dias, key=lambda d: D[d][1], reverse=True)[2:]
    sin2 = sum(D[d][1] for d in top) / sum(D[d][0] for d in top)
    m = mk[key]; t1 = max(m.values()) / sum(m.values())
    print('%-4s %s %-9s dias %d coste/dia %9.0f EV %+.4f (+reb %+.4f) IC90 dias (%+.4f,%+.4f) dias+ %d sin2 %+.4f top1 %.3f makers %d' % (
        key[0], key[1], key[2], len(dias), C / len(dias), P / C, (P + R) / C, bs[100], bs[1899], sum(1 for d in dias if D[d][1] > 0), sin2, t1, len(m)))
