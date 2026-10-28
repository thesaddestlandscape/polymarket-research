#!/usr/bin/env python3
"""segfav_eval.py <dir con sf_D.csv.gz> -- SOLO LECTURA. E-RE-AS-B-SEGFAV (PREREG_SEGFAV.md).
PRIMARIA: tipo S (senal), L=250, Tbuckets 20/60/120 (T<180 s), comprar 5 acc de F al ask nivel 1 del estado en td+L;
ejecutable si as>=5, edad<=30 s, 0<ask<1 y gana conocido. pnl = 5*gana - 5*ask - 5*0,07*ask*(1-ask); coste = 5*ask + fee.
EVw = Σpnl/Σcoste; EVu = media pnl/coste; IC90 bootstrap por CIERRE (2000, semilla 2711). DESC 19..25, OOS 26."""
import sys, gzip, csv, glob, collections
import numpy as np
D = sys.argv[1]; OOS = '2026-10-26'; B = 2000; FEE = 0.07
rows = []; cob = collections.Counter()
for fn in sorted(glob.glob(D + '/sf_*.csv.gz')):
    for r in csv.DictReader(gzip.open(fn, 'rt')): rows.append(r)
def unidad(r, L, lado='F'):
    k = 'F' if lado == 'F' else 'C'
    a, s = r['ask%s%d' % (k, L)], r['as%s%d' % (k, L)]
    if r['gana'] == '': return None, 'sin_gana'
    if a == '' or s == '': return None, 'sin_estado'
    a, s = float(a), float(s)
    if lado == 'F':
        age = r['ageF%d' % L]
        if age == '' or float(age) > 30000: return None, 'edad'
    if not 0 < a < 1: return None, 'ask_inv'
    if s < 5: return None, 'no_ejec'
    g = int(r['gana']) if lado == 'F' else 1 - int(r['gana'])
    cost = 5 * a + 5 * FEE * a * (1 - a)
    return (5 * g - cost, cost, a), 'ok'
def pob(tipo, L, tbs, lado='F', dias=None):
    out = []; c = collections.Counter()
    for r in rows:
        if r['tipo'] != tipo or int(r['tb']) not in tbs: continue
        if dias is not None and r['dia'] not in dias: continue
        u, m = unidad(r, L, lado); c[m] += 1
        if u: out.append((r['dia'], int(r['cierre']), r['coin'], int(r['tb']), u[0], u[1], u[2]))
    return out, c
def boot(us):
    if not us: return None
    cies = sorted(set(x[1] for x in us)); ix = {c: i for i, c in enumerate(cies)}
    P = np.zeros(len(cies)); C = np.zeros(len(cies))
    for x in us: P[ix[x[1]]] += x[4]; C[ix[x[1]]] += x[5]
    rng = np.random.default_rng(2711); W = rng.multinomial(len(cies), np.ones(len(cies)) / len(cies), size=B)
    ev = (W @ P) / (W @ C)
    return P.sum() / C.sum(), np.percentile(ev, 5), np.percentile(ev, 95), len(cies), float((ev <= 0).mean())
def linea(nom, us):
    b = boot(us)
    if b is None: print('  %-44s n=0' % nom); return None
    evu = np.mean([x[4] / x[5] for x in us]); pd = collections.defaultdict(lambda: [0.0, 0.0])
    for x in us: pd[x[0]][0] += x[4]; pd[x[0]][1] += x[5]
    dd = ' '.join('%s:%+.3f' % (d[8:], v[0] / v[1]) for d, v in sorted(pd.items()))
    print('  %-44s n=%5d cierres=%4d coste=%8.1f EVw=%+.4f IC90=(%+.3f,%+.3f) EVu=%+.4f ask=%.3f | %s' % (nom, len(us), b[3], sum(x[5] for x in us), b[0], b[1], b[2], evu, np.mean([x[6] for x in us]), dd))
    return b, pd
DIAS = sorted(set(r['dia'] for r in rows)); DESC = [d for d in DIAS if d < OOS]
print('dias', DIAS, 'filas', len(rows), collections.Counter((r['tipo'], r['dia']) for r in rows))
T180 = (20, 60, 120); TODOS = (20, 60, 120, 180, 240)
print('\n== COBERTURA');
for tipo in 'SP':
    _, c = pob(tipo, 250, TODOS); print('  tipo', tipo, 'L=250', dict(c))
print('\n== PRIMARIA: S, L=250, T<180 s')
us, _ = pob('S', 250, T180); res = linea('TODO 19-26', us)
linea('DESC 19-25', [x for x in us if x[0] in DESC]); linea('OOS 26', [x for x in us if x[0] == OOS])
if res:
    pd = res[1]; mej = sorted(pd, key=lambda d: pd[d][0] / pd[d][1])[-2:]
    linea('sin 2 mejores dias %s' % mej, [x for x in us if x[0] not in mej])
    print('  dias >0: %d/%d' % (sum(1 for d in pd if pd[d][0] > 0), len(pd)))
# Delta estratificado vs placebo: celdas (coin, tb, bucket ask 0,05), pesos = coste de S; bootstrap conjunto por cierre
def delta(L, tbs, nom):
    S, _ = pob('S', L, tbs); P, _ = pob('P', L, tbs)
    cel = lambda x: (x[2], x[3], int(x[6] / 0.05 + 1e-9))
    cells = sorted(set(cel(x) for x in S) & set(cel(x) for x in P)); ci = {c: i for i, c in enumerate(cells)}
    cies = sorted(set(x[1] for x in S) | set(x[1] for x in P)); ix = {c: i for i, c in enumerate(cies)}
    M = np.zeros((4, len(cies), len(cells)))
    for k, pop in ((0, S), (2, P)):
        for x in pop:
            j = ci.get(cel(x))
            if j is None: continue
            M[k, ix[x[1]], j] += x[4]; M[k + 1, ix[x[1]], j] += x[5]
    def est(w):
        s = np.tensordot(w, M, axes=([-1], [1])) if w.ndim == 1 else None
        return s
    rng = np.random.default_rng(2711); W = rng.multinomial(len(cies), np.ones(len(cies)) / len(cies), size=B)
    Sp, Sc, Pp, Pc = (W @ M[0], W @ M[1], W @ M[2], W @ M[3])
    with np.errstate(invalid='ignore', divide='ignore'):
        evP = np.where(Pc > 0, Pp / Pc, np.nan); evS = np.where(Sc > 0, Sp / Sc, np.nan)
        ok = (Sc > 0) & (Pc > 0); d = np.where(ok, Sc * (evS - evP), 0).sum(1) / np.where(ok, Sc, 0).sum(1)
    t = M.sum(1); okt = (t[1] > 0) & (t[3] > 0)
    d0 = (t[1][okt] * (t[0][okt] / t[1][okt] - t[2][okt] / t[3][okt])).sum() / t[1][okt].sum()
    evP0 = (t[1][okt] * t[2][okt] / t[3][okt]).sum() / t[1][okt].sum()
    print('  %-44s celdas=%d  EV placebo reponderado=%+.4f  DELTA S-P=%+.4f IC90=(%+.3f,%+.3f)' % (nom, len(cells), evP0, d0, np.nanpercentile(d, 5), np.nanpercentile(d, 95)))
print('\n== DELTA vs PLACEBO (estratificado moneda x Tbucket x ask 0,05)')
delta(250, T180, 'PRIMARIA L=250 T<180')
print('\n== SECUNDARIAS')
for L in (100, 250, 400):
    for tb in TODOS:
        u, _ = pob('S', L, (tb,)); linea('S L=%d Tb=%d' % (L, tb), u)
    u, _ = pob('S', L, TODOS); linea('S L=%d TODOS T' % L, u)
for tb in TODOS:
    u, _ = pob('P', 250, (tb,)); linea('PLACEBO L=250 Tb=%d' % tb, u)
for tb in TODOS: delta(250, (tb,), 'DELTA L=250 Tb=%d' % tb)
print('\n== INVERSA (comprar el complementario C tras el print), L=250')
for tbs, nom in ((T180, 'T<180'), ((180, 240), 'T>=180')):
    u, _ = pob('S', 250, tbs, 'C'); linea('INV ' + nom, u)
print('\n== DESCRIPTIVO: EV del propio tomador al precio del print (NO ejecutable para nosotros)')
for tb in TODOS:
    us2 = []
    for r in rows:
        if r['tipo'] != 'S' or int(r['tb']) != tb or r['gana'] == '': continue
        p = float(r['p_print']); cost = 5 * p + 5 * FEE * p * (1 - p)
        us2.append((r['dia'], int(r['cierre']), r['coin'], tb, 5 * int(r['gana']) - cost, cost, p))
    linea('TOMADOR al print Tb=%d' % tb, us2)
print('\n== DESCRIPTIVO: movimiento del ask de F (pre -> td+250) en S')
mv = [float(r['askF250']) - float(r['askpre']) for r in rows if r['tipo'] == 'S' and r['askpre'] != '' and r['askF250'] != '']
mv = np.array(mv); print('  n=%d sube %.1f%% igual %.1f%% baja %.1f%% medio %+.4f' % (len(mv), 100 * (mv > 1e-9).mean(), 100 * (abs(mv) <= 1e-9).mean(), 100 * (mv < -1e-9).mean(), mv.mean()))
print('\n== EXPLORATORIO moneda x Tbucket (S, L=250), n>=40; BH-FDR 10%% sobre p bootstrap unilateral')
cel = []
for coin in ('BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB'):
    for tb in TODOS:
        u = [x for x in pob('S', 250, (tb,))[0] if x[2] == coin]
        if len(u) < 40: continue
        b = boot(u); cel.append((b[4], coin, tb, len(u), b))
cel.sort(); m = len(cel)
kmax = max([i + 1 for i, x in enumerate(cel) if x[0] <= 0.10 * (i + 1) / m] or [0])
for i, (p, coin, tb, n, b) in enumerate(cel):
    print('  %-4s Tb=%3d n=%4d EVw=%+.4f IC90=(%+.3f,%+.3f) p=%.4f BH_ok=%s' % (coin, tb, n, b[0], b[1], b[2], p, i + 1 <= kmax))
