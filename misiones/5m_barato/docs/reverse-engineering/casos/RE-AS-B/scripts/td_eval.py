#!/usr/bin/env python3
"""td_eval.py — E-RE-AS-B-TD (PREREG_TD.md sha f2849f99...). SOLO LECTURA. python3 -I td_eval.py <dir_x> <dir_vpv>
dir_x: x_D.csv (filas x de m5_registro_D: tipo,T,sym,precio,qty,m,E,RECV). Maker que cancela por Binance antes del taker delay."""
import sys, csv, gzip, bisect, random, collections
DX, DV = sys.argv[1], sys.argv[2]
DIAS = ['2026-10-24', '2026-10-25', '2026-10-26']
def carga_x(d):
    S = collections.defaultdict(list)
    for l in open('%s/x_%s.csv' % (DX, d)):
        c = l.rstrip('\n').split(',')
        if len(c) < 8 or c[0] != 'x': continue
        S[c[2]].append((int(c[7]), float(c[3])))
    out = {}
    for s, v in S.items():
        v.sort(); out[s] = ([a for a, _ in v], [b for _, b in v])
    return out
def saltos(X, k, w=300):
    """por simbolo: tiempos (recv) de saltos down (r<=-k bps) y up (r>=k) en w ms."""
    J = {}
    for s, (t, p) in X.items():
        dn, up = [], []
        for i in range(len(t)):
            j = bisect.bisect_right(t, t[i] - w) - 1
            if j < 0: continue
            r = (p[i] / p[j] - 1) * 1e4
            if r <= -k: dn.append(t[i])
            elif r >= k: up.append(t[i])
        J[s] = (dn, up)
    return J
def hay(arr, a, b):
    i = bisect.bisect_left(arr, a); return i < len(arr) and arr[i] <= b
V = []; cnt = collections.Counter()
for d in DIAS:
    X = carga_x(d); cnt['sym_' + d] = len(X)
    JJ = {k: saltos(X, k) for k in (1, 2, 4)}
    for r in csv.DictReader(gzip.open('%s/vpv_%s.csv.gz' % (DV, d), 'rt')):
        if r['gana'] == '': cnt['sin_gana'] += 1; continue
        s = r['coin'] + 'USDT'
        if s not in X: cnt['sin_bn'] += 1; continue
        t0 = int(r['t0_recv_ms']); b = float(r['b']); g = int(r['gana'])
        fin = min(t0 + 60000, int(r['cierre']) * 1000 - 2000)
        e = dict(dia=d, mk=r['mercado'], lado=r['lado'], coin=r['coin'], cie=r['cierre'], b=b, cost=5 * b, pnl=5 * (g - b))
        for m in ('pes', 'opt'):
            f = r['relleno_' + m] == '1'; tf = int(r['t_relleno_%s_ms' % m]) if f and r['t_relleno_%s_ms' % m] else None
            e[m] = tf if f else None
        for k in (1, 2, 4):
            dn, up = JJ[k][s]; arr = dn if r['lado'] == 'YES' else up
            for Lc in (60, 100, 250):
                for m in ('pes', 'opt'):
                    tf = e[m]
                    if tf is None: continue
                    e[('ret', m, k, Lc)] = not hay(arr, t0, tf - Lc)
                    e[('apa', m, k, Lc)] = hay(arr, tf - 2000, tf - Lc)
            if k == 2: e['canc_any'] = hay(arr, t0, (e['pes'] or fin))
        V.append(e)
print('vidas', len(V), dict(cnt))
def unidad(sel, m):
    best = {}
    for e in sel:
        if e[m] is None: continue
        key = (e['mk'], e['lado'])
        if key not in best or e[m] < best[key][m]: best[key] = e
    return list(best.values())
def evw(U): c = sum(u['cost'] for u in U); return sum(u['pnl'] for u in U) / c if c else float('nan')
def boot(U, U2=None, R=2000):
    rnd = random.Random(2711); G = collections.defaultdict(lambda: [0, 0, 0, 0])
    for u in U: G[u['cie']][0] += u['pnl']; G[u['cie']][1] += u['cost']
    for u in (U2 or []): G[u['cie']][2] += u['pnl']; G[u['cie']][3] += u['cost']
    ks = list(G); res = []
    for _ in range(R):
        a = [0, 0, 0, 0]
        for kk in (rnd.choice(ks) for _ in ks):
            for i in range(4): a[i] += G[kk][i]
        v = a[0] / a[1] if a[1] else 0
        if U2 is not None: v = v - (a[2] / a[3] if a[3] else 0)
        res.append(v)
    res.sort(); return res[int(.05 * R)], res[int(.95 * R)]
def linea(tag, U, U2=None):
    v = evw(U) - (evw(U2) if U2 is not None else 0); lo, hi = boot(U, U2)
    print('  %-34s n=%5d cierres=%4d EVw=%+.4f IC90=(%+.3f,%+.3f)' % (tag, len(U), len({u['cie'] for u in U}), v, lo, hi))
for nom, dd in (('DESC 24+25', DIAS[:2]), ('OOS 26', DIAS[2:]), ('TODO', DIAS)):
    S = [e for e in V if e['dia'] in dd]
    fr = sum(1 for e in S if e.get('canc_any')) / len(S)
    print('==', nom, 'vidas', len(S), 'frac vidas con salto adverso k=2 en vida (approx) %.3f' % fr)
    for m in ('pes', 'opt'):
        Uall = unidad(S, m)
        Uret = unidad([e for e in S if e.get(('ret', m, 2, 100))], m)
        Uapa = unidad([e for e in S if e.get(('apa', m, 2, 100))], m)
        Unoapa = unidad([e for e in S if e[m] is not None and not e.get(('apa', m, 2, 100))], m)
        linea(m + ' todas', Uall); linea(m + ' RETENIDOS politica primaria', Uret)
        linea(m + ' apartados justa', Uapa); linea(m + ' no apartados justa', Unoapa)
        linea(m + ' DIF apartados-no_apartados', Uapa, Unoapa)
        print('  %s fill-rate unidades retenidas/todas = %d/%d' % (m, len(Uret), len(Uall)))
print('== secundarias (TODO, Bonferroni x6)')
for k, Lc in ((2, 60), (2, 250), (1, 100), (4, 100)):
    for m in ('pes', 'opt'):
        linea('%s k=%d Lc=%d retenidos' % (m, k, Lc), unidad([e for e in V if e.get(('ret', m, k, Lc))], m))
        linea('%s k=%d Lc=%d DIF apa-noapa' % (m, k, Lc), unidad([e for e in V if e.get(('apa', m, k, Lc))], m),
              unidad([e for e in V if e[m] is not None and not e.get(('apa', m, k, Lc))], m))
print('== moneda x bucket (TODO, pes, retenidos primaria, n>=40, descriptivo)')
R = unidad([e for e in V if e.get(('ret', 'pes', 2, 100))], 'pes'); C = collections.defaultdict(list)
for u in R: C[(u['coin'], int(u['b'] / 0.05 + 1e-9) * 5)].append(u)
for kk in sorted(C):
    if len(C[kk]) >= 40: print('  %s b%02d  n=%d EVw=%+.3f' % (kk[0], kk[1], len(C[kk]), evw(C[kk])))
