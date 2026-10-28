#!/usr/bin/env python3
"""rewards5m_cuota.py LIBRO.csv.gz REGISTRO.csv.gz  (PREREG_REWARDS5M.md; SOLO LECTURA; python3 -I). Stream: libro5_ms -> libros por token -> muestras cierre-300+30+60k s."""
import sys, gzip, heapq, statistics as st, collections, json
LIB, REG = sys.argv[1], sys.argv[2]
COINS = ('BTC', 'ETH', 'SOL', 'XRP'); V = 4.5; C = 3.0; MINS = 50.0; OUR = 50.0
POOL = {'BTC': 300000/31/288, 'ETH': 50000/31/288, 'SOL': 50000/31/288, 'XRP': 50000/31/288}   # A4, escenario de agosto (programa terminado)
tok = {}; mk = collections.defaultdict(dict)
with gzip.open(REG, 'rt') as f:
    for ln in f:
        if ln[0] != 'k': continue
        p = ln.rstrip('\n').split(',')
        if len(p) < 8 or p[4] != '5min' or p[3] not in COINS: continue
        import datetime as dt
        cie = int(dt.datetime.fromisoformat(p[6]).timestamp())
        tok[p[2]] = (p[3], p[5], cie, p[7]); mk[p[5]][p[7]] = p[2]; mk[p[5]]['coin'] = p[3]; mk[p[5]]['cie'] = cie
with gzip.open(LIB, 'rt') as f:
    f.readline(); t0 = int(f.readline().split(',')[1]) // 1000
    last = None
    for ln in f: last = ln
t1 = int(last.split(',')[6]) // 1000
heap = []
for m, d in mk.items():
    if 'YES' in d and 'NO' in d and t0 + 5 < d['cie'] - 300 and d['cie'] < t1 - 5:
        for k in range(5): heapq.heappush(heap, ((d['cie'] - 300 + 30 + 60 * k) * 1000, m, k))
books = {}   # token -> [bids dict, asks dict]
rows = []
def S(s): return ((V - s) / V) ** 2 if 0 <= s < V else 0.0
def muestra(m, k, tms):
    d = mk[m]; b = books.get(d['YES'])
    if not b or not b[0] or not b[1]: rows.append((d['coin'], m, k, 'sin_libro')); return
    bb, ba = max(b[0]), min(b[1])
    if bb >= ba: rows.append((d['coin'], m, k, 'cruzado')); return
    mid = (bb + ba) / 2
    qb = [0.0, 0.0]; qa = [0.0, 0.0]
    for p, s in b[0].items():
        w = S((mid - p) * 100)
        if w: qb[0] += w * s; qb[1] += w * s * (s >= MINS)
    for p, s in b[1].items():
        w = S((p - mid) * 100)
        if w: qa[0] += w * s; qa[1] += w * s * (s >= MINS)
    rows.append((d['coin'], m, k, 'ok', mid, (bb, ba), qb, qa))
with gzip.open(LIB, 'rt') as f:
    f.readline()
    for ln in f:
        p = ln.rstrip('\n').split(',')
        if len(p) < 7: continue
        try: rec = int(p[6])
        except ValueError: continue
        while heap and heap[0][0] <= rec:
            tt, m, k = heapq.heappop(heap); muestra(m, k, tt)
        tp = p[0]
        if tp == 'd':
            if p[2] not in tok: continue
            b = books.setdefault(p[2], [{}, {}]); side = b[0] if p[3] == 'B' else b[1]
            pr = float(p[4]); sz = float(p[5])
            if sz <= 0: side.pop(pr, None)
            else: side[pr] = sz
        elif tp == 'B':
            if p[2] not in tok: continue
            def parse(x): return {float(a.split(':')[0]): float(a.split(':')[1]) for a in x.split(';') if a}
            books[p[2]] = [parse(p[3]), parse(p[4])]
res = collections.defaultdict(list); cnt = collections.Counter()
for r in rows:
    cnt[(r[0], r[3])] += 1
    if r[3] == 'ok': res[r[0]].append(r)
print('archivo', LIB.split('/')[-1], 'rango', t0, t1, 'mercados con tokens', len(mk), 'muestras', len(rows))
print('estado muestras', dict(cnt))
print('coin n_muestras n_mercados mid_med spread_med frac_bid_en_banda Qtot_a_med Qtot_b_med | V1(join bb) cuota[bajo,alto] a / b | V2(s=1c) cuota[bajo,alto] a / b | ingreso$/mercado escenario ag: V1b[bajo,alto] V2b[bajo,alto] | p*(equilibrio)')
for coin, L in sorted(res.items()):
    mids = [r[4] for r in L]; sp = [(r[5][1] - r[5][0]) * 100 for r in L]
    inb = [r for r in L if (r[4] - r[5][0]) * 100 < V]
    Qa = [r[6][0] + r[7][0] for r in L]; Qb = [r[6][1] + r[7][1] for r in L]
    def cuota(var, s_fn):
        lo = []; hi = []
        for r in L:
            s = s_fn(r)
            qo = S(s) * OUR / C if 0.10 <= r[4] <= 0.90 else 0.0
            Qt = r[6][var] + r[7][var]
            lo.append(qo / (qo + Qt / 2) if qo > 0 else 0.0)   # rival alto = Qt/2 -> cuota baja
            hi.append(qo / (qo + Qt / 6) if qo > 0 else 0.0)
        return st.mean(lo), st.mean(hi)
    v1 = [cuota(0, lambda r: (r[4] - r[5][0]) * 100), cuota(1, lambda r: (r[4] - r[5][0]) * 100)]
    v2 = [cuota(0, lambda r: 1.0), cuota(1, lambda r: 1.0)]
    P = POOL[coin]
    ing_v1 = (P * v1[1][0], P * v1[1][1]); ing_v2 = (P * v2[1][0], P * v2[1][1])   # variante b (>=50)
    print(coin, len(L), len({r[1] for r in L}), '%.3f' % st.median(mids), '%.2f' % st.median(sp), '%.2f' % (len(inb) / len(L)), '%.0f' % st.median(Qa), '%.0f' % st.median(Qb),
          '| V1 a[%.3f,%.3f] b[%.3f,%.3f] | V2 a[%.3f,%.3f] b[%.3f,%.3f] | pool$/mk %.2f -> V1b[%.3f,%.3f] V2b[%.3f,%.3f] | p*V2b<=%.3f' % (v1[0][0], v1[0][1], v1[1][0], v1[1][1], v2[0][0], v2[0][1], v2[1][0], v2[1][1], P, ing_v1[0], ing_v1[1], ing_v2[0], ing_v2[1], ing_v2[1] / 2.25))
