#!/usr/bin/env python3
"""frente_eval.py -- E-RE-AS-B-FRENTE (PREREG_FRENTE.md sha 1528f06b...). SOLO LECTURA.
python3 -I frente_eval.py <dir_fr (fr_D.csv.gz de frente_vpv.py)> <dir_x (x_D.csv, como td_eval)> <dir_vpv (vpv_D.csv.gz)>
Primaria: frente (b'=bb+0,01) Lp=85, regla A+B, TD real (k=2 bps/300 ms, Lc=100), unidad = primer print por mercado-lado."""
import sys, gzip, csv, bisect, random, collections
DF, DX, DV = sys.argv[1:4]
DIAS = ['2026-10-24', '2026-10-25', '2026-10-26']
INF = float('inf'); LC = 100; SHIFT = 60000
def carga_x(d):
    S = collections.defaultdict(list)
    with open('%s/x_%s.csv' % (DX, d)) as f:
        for l in f:
            c = l.split(',')
            if len(c) < 8 or c[0] != 'x': continue
            S[c[2]].append((int(c[7]), float(c[3])))
    out = {}
    for s, v in S.items():
        v.sort(); out[s] = ([a for a, _ in v], [b for _, b in v])
    return out
def saltos(X, k=2, w=300):                      # identico a td_eval.saltos
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
def primer(arr, a, b):
    i = bisect.bisect_left(arr, a)
    return arr[i] if i < len(arr) and arr[i] <= b else None
def fnum(x): return float(x) if x != '' else None
def relleno(v, lp, regla, canc, solo5=False):
    ba_arr = v['ba85'] if lp == 85 else (v['ba250'] if lp == 250 else None)
    if ba_arr is not None and ba_arr <= v['bp'] + 1e-9: return None          # post-only rechazada
    lim = canc + LC if canc is not None else INF
    A = B = 0.0; t1 = None
    for (t, sz, ty) in v['pr']:
        if t < v['t0'] + lp: continue
        if t >= lim: break
        if t1 is None: t1 = t
        if ty == 'A': A += sz
        else: B += sz
        if (A + B if regla == 'sum' else max(A, B)) >= 5: break
    tot = min(5.0, A + B if regla == 'sum' else max(A, B))
    if tot <= 0 or (solo5 and tot < 5 - 1e-9): return None
    return (t1, tot)
V = []; cnt = collections.Counter()
for d in DIAS:
    X = carga_x(d); J = saltos(X); JP = {s: ([t + SHIFT for t in dn], [t + SHIFT for t in up]) for s, (dn, up) in J.items()}
    for s in X: cnt['ticks_bn_' + d] += len(X[s][0])
    del X
    base = {}
    for r in csv.DictReader(gzip.open('%s/vpv_%s.csv.gz' % (DV, d), 'rt')):
        base[(r['mercado'], r['lado'], r['t0_recv_ms'])] = (r['t_relleno_pes_ms'] if r['relleno_pes'] == '1' else '',
                                                            r['t_relleno_opt_ms'] if r['relleno_opt'] == '1' else '', r['b'])
    for r in csv.DictReader(gzip.open('%s/fr_%s.csv.gz' % (DF, d), 'rt')):
        cnt['vidas'] += 1
        if r['gana'] == '': cnt['sin_gana'] += 1; continue
        s = r['coin'] + 'USDT'
        if s not in J: cnt['sin_bn'] += 1; continue
        t0 = int(r['t0']); fin = int(r['fin']); bp = float(r['bp'])
        pr = []
        for x in (r['prints'].split(';') if r['prints'] else []):
            a_, b_, c_ = x.split(':'); pr.append((int(a_), float(b_), c_))
        pr.sort()
        ad = J[s][0] if r['lado'] == 'YES' else J[s][1]; adp = JP[s][0] if r['lado'] == 'YES' else JP[s][1]
        bb85 = fnum(r['bb85'])
        v = dict(dia=d, mk=r['mercado'], lado=r['lado'], coin=r['coin'], cie=r['cierre'], t0=t0, fin=fin, b=float(r['bb']), bp=bp,
                 g=int(r['gana']), ba85=fnum(r['ba85']), ba250=fnum(r['ba250']), cont=(bb85 is not None and bb85 >= bp - 1e-9), pr=pr,
                 canc=primer(ad, t0, fin), cancp=primer(adp, t0, fin))
        bs = base.get((r['mercado'], r['lado'], r['t0']))
        if bs is None: cnt['sin_vpv'] += 1; v['tp'] = v['to'] = None
        else:
            v['tp'] = int(bs[0]) if bs[0] else None; v['to'] = int(bs[1]) if bs[1] else None
            if abs(float(bs[2]) - v['b']) > 1e-9: cnt['b_distinto_vpv'] += 1
        v['P'] = relleno(v, 85, 'sum', v['canc']); v['NOTD'] = relleno(v, 85, 'sum', None); v['PLAC'] = relleno(v, 85, 'sum', v['cancp'])
        v['MAX'] = relleno(v, 85, 'max', v['canc']); v['FULL'] = relleno(v, 85, 'sum', v['canc'], True)
        v['LP0'] = relleno(v, 0, 'sum', v['canc']); v['LP250'] = relleno(v, 250, 'sum', v['canc'])
        nt = v['NOTD']; lim = v['canc'] + LC if v['canc'] is not None else INF
        v['APA'] = nt if (nt is not None and nt[0] >= lim) else None; v['NOAPA'] = nt if (nt is not None and nt[0] < lim) else None
        for m, kk in (('pes', 'tp'), ('opt', 'to')):
            tf = v[kk]
            v['BQ_' + m] = (tf, 5.0) if (tf is not None and (v['canc'] is None or tf < v['canc'] + LC)) else None
            v['BQN_' + m] = (tf, 5.0) if tf is not None else None
        V.append(v)
    del J, JP, base
print('conteos', dict(cnt))
def unidades(L, key, precio='bp'):
    best = {}
    for v in L:
        r = v.get(key)
        if r is None: continue
        k = (v['mk'], v['lado']); c = (r[0], v['t0'])
        if k not in best or c < best[k][0]: best[k] = (c, v, r)
    U = []
    for c, v, r in best.values():
        p = v[precio]; sh = r[1]
        U.append(dict(dia=v['dia'], cie=v['cie'], coin=v['coin'], bp=v['bp'], sh=sh, pnl=sh * (v['g'] - p), cost=sh * p,
                      reb=sh * 0.2 * 0.07 * p * (1 - p), dt=r[0] - v['t0']))
    return U
def evw(U, reb=False):
    c = sum(u['cost'] for u in U); return (sum(u['pnl'] + (u['reb'] if reb else 0) for u in U) / c) if c else float('nan')
def boot(U, U2=None, reb=False, R=2000):
    rnd = random.Random(2711); G = collections.defaultdict(lambda: [0.0, 0.0, 0.0, 0.0])
    for u in U: G[u['cie']][0] += u['pnl'] + (u['reb'] if reb else 0); G[u['cie']][1] += u['cost']
    for u in (U2 or []): G[u['cie']][2] += u['pnl']; G[u['cie']][3] += u['cost']
    ks = list(G); A = [G[k] for k in ks]; res = []
    for _ in range(R):
        a0 = a1 = a2 = a3 = 0.0
        for g in rnd.choices(A, k=len(A)): a0 += g[0]; a1 += g[1]; a2 += g[2]; a3 += g[3]
        x = a0 / a1 if a1 else 0.0
        if U2 is not None: x -= a2 / a3 if a3 else 0.0
        res.append(x)
    res.sort(); return res[int(.05 * R)], res[int(.95 * R)]
def linea(tag, U, U2=None, reb=False):
    if not U: print('  %-40s n=0' % tag); return
    e = evw(U, reb) - (evw(U2) if U2 is not None else 0); lo, hi = boot(U, U2, reb)
    eu = sum((u['pnl'] + (u['reb'] if reb else 0)) / u['cost'] for u in U) / len(U)
    print('  %-40s n=%5d cierres=%4d coste=%8.1f pnl=%+8.1f EVw=%+.4f IC90cierre=(%+.3f,%+.3f) EVu=%+.4f' % (
        tag, len(U), len({u['cie'] for u in U}), sum(u['cost'] for u in U), sum(u['pnl'] for u in U), e, lo, hi, eu))
for nom, dd in (('DESC 24+25', DIAS[:2]), ('OOS 26', DIAS[2:]), ('TODO', DIAS)):
    S = [v for v in V if v['dia'] in dd]
    lados = len({(v['mk'], v['lado']) for v in S})
    print('== %s vidas %d mercado-lados %d | rechazo85 %.3f disputada85 %.3f | TD cancela (vidas con salto en vida) real %.3f placebo %.3f' % (
        nom, len(S), lados, sum(1 for v in S if v['ba85'] is not None and v['ba85'] <= v['bp'] + 1e-9) / len(S),
        sum(1 for v in S if v['cont']) / len(S), sum(1 for v in S if v['canc'] is not None) / len(S), sum(1 for v in S if v['cancp'] is not None) / len(S)))
    P = unidades(S, 'P'); linea('PRIMARIA frente Lp85 A+B TD', P)
    linea('frente SIN TD', unidades(S, 'NOTD')); linea('frente TD PLACEBO (-60 s)', unidades(S, 'PLAC'))
    linea('frente regla max(A,B) TD', unidades(S, 'MAX'))
    for m in ('pes', 'opt'):
        linea('cola-final vpv %s TD (mismas vidas)' % m, unidades(S, 'BQ_' + m, 'b'))
        linea('cola-final vpv %s sin TD' % m, unidades(S, 'BQN_' + m, 'b'))
        linea('DIF primaria - cola-final %s TD' % m, P, unidades(S, 'BQ_' + m, 'b'))
    print('  fill: unidades primaria %d / mercado-lados %d; dt mediana primer print %s ms' % (
        len(P), lados, sorted(u['dt'] for u in P)[len(P) // 2] if P else '-'))
print('== robustez y controles (TODO; descriptivas, Bonferroni x12)')
P = unidades(V, 'P')
linea('primaria +rebate (supuesto)', P, reb=True)
linea('solo rellenos completos 5 acc', unidades(V, 'FULL'))
linea('excluyendo disputadas', unidades([v for v in V if not v['cont']], 'P'))
linea('Lp=0', unidades(V, 'LP0')); linea('Lp=250', unidades(V, 'LP250'))
linea('INVERSION apartados por TD (sin TD)', unidades(V, 'APA')); linea('no apartados (sin TD)', unidades(V, 'NOAPA'))
linea('DIF apartados - no apartados', unidades(V, 'APA'), unidades(V, 'NOAPA'))
pd = {d: sum(u['pnl'] for u in P if u['dia'] == d) for d in DIAS}
for d in DIAS: linea('primaria dia %s' % d, [u for u in P if u['dia'] == d])
orden = sorted(DIAS, key=lambda d: -pd[d])
linea('sin el mejor dia (%s)' % orden[0], [u for u in P if u['dia'] != orden[0]])
linea('sin los 2 mejores dias (= %s)' % orden[2], [u for u in P if u['dia'] == orden[2]])
pc = collections.defaultdict(float)
for u in P: pc[u['cie']] += u['pnl']
top2 = set(sorted(pc, key=lambda k: -pc[k])[:2])
linea('sin los 2 mejores cierres', [u for u in P if u['cie'] not in top2])
print('== por moneda (TODO, primaria) y moneda x bucket b\' (n>=40, descriptivo)')
for c in sorted({u['coin'] for u in P}):
    Uc = [u for u in P if u['coin'] == c]; linea(c, Uc)
    for d in DIAS:
        Ud = [u for u in Uc if u['dia'] == d]
        print('      %s %s n=%d EVw=%+.3f' % (c, d, len(Ud), evw(Ud) if Ud else float('nan')))
C = collections.defaultdict(list)
for u in P: C[(u['coin'], int(u['bp'] / 0.05 + 1e-9) * 5)].append(u)
for kk in sorted(C):
    if len(C[kk]) >= 40: linea('%s b%02d' % kk, C[kk])
