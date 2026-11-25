#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""salida_dinamica_28oct/eval_sal.py - manda PREREG_SALIDA_DIN.md (sha en HASHES.txt). SOLO LECTURA:
units/u_*.csv.gz (alpha_miner_b_27oct/sim.py, reloj de RECEPCION) + desenlace oficial. No escribe en data/ ni toca produccion."""
import gzip, csv, json, glob
import numpy as np

SRC = '/root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct/units/'
G = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
OOS = {'2026-10-23', '2026-10-24', '2026-10-25', '2026-10-26'}
B = 2000; SEED = 2711
PESS = {'IS': -0.015, 'OOS': -0.046}   # validador: R1 cola estricta (HOLD pesimista)


def fee(p): return 0.07 * p * (1 - p)
def F(x):
    if x in (None, '', 'None', 'NA'): return None
    return float(x)
def PR(x):
    if x in (None, '', 'NA'): return None
    v = [None if y == '' else float(y) for y in x.split('|')]
    return v if (len(v) == 4 and v[0] is not None and v[1] is not None) else None


# ---------------- carga ----------------
U = []; seen = set(); miss = 0; tot = 0; x3c = {'blank': 0, 'NA': 0, 'probe': 0}
for p in sorted(glob.glob(SRC + 'u_*.csv.gz')):
    with gzip.open(p, 'rt') as f:
        for r in csv.DictReader(f):
            k = (r['mercado'], r['lado'])
            if k in seen: continue
            seen.add(k); tot += 1
            w = G.get(str(r['mercado']))
            if w not in ('YES', 'NO'): miss += 1; continue
            sh = F(r['P_sh'])
            if not sh or sh <= 0: continue
            g = 1.0 if w == r['lado'] else 0.0
            cost = F(r['P_cost']); avg = cost / sh
            tx = F(r['P_tx']); te = F(r['te'])
            u = dict(dia=r['dia'], cie=int(r['cierre']), coin=r['coin'], g=g, sh=sh, cost=cost, avg=avg, h=sh * g - cost,
                     cause=r['P_cause'], npart=int(r['P_np']), Te=F(r['Te']), spr=F(r['ba_e']) - F(r['bb_e']),
                     v60=F(r.get('v60')), hora=int(r['hora']),
                     wait=((tx - te) / 1000.0 if (tx is not None and te is not None) else None),
                     d4=None, x4=None, q4=0.0, x3=None, ns=False, d30=None, q3=0.0, rem3=0.0)
            v4 = PR(r['X4'])
            if v4 is not None:
                q = min(sh, v4[1]); u['x4'] = v4; u['q4'] = q; u['d4'] = q * (v4[0] - fee(v4[0]) - g)
            raw3 = r['X3']; x3c['blank' if raw3 == '' else ('NA' if raw3 == 'NA' else 'probe')] += 1
            v3 = PR(raw3)
            if v3 is not None:
                bb3, bs3 = v3[0], v3[1]; f3 = fee(bb3); qns = min(sh, bs3)
                proc = F(r['P_X3_proc']); fe = F(r['P_X3_fee']); rem = F(r['P_X3_rem'])
                ns = (abs(proc - qns * bb3) < 2e-5 and abs(fe - qns * f3) < 2e-5 and abs(rem - (sh - qns)) < 2e-5)
                u['x3'] = v3; u['ns'] = ns
                if ns: q = qns; u['rem3'] = sh
                else:
                    q = min((fe / f3) if f3 > 1e-12 else 0.0, bs3); u['rem3'] = rem + q
                u['q3'] = q; u['d30'] = q * (bb3 - f3 - g)
            U.append(u)
IS = [u for u in U if u['dia'] not in OOS]; OO = [u for u in U if u['dia'] in OOS]
print('unidades totales dedup', tot, 'sin desenlace', miss, '| con relleno P: IS', len(IS), 'OOS', len(OO))
print('sonda X3 (P rellenadas): vacia(orden vendida entera/no colocada)', x3c['blank'], 'NA(libro rancio)', x3c['NA'], 'con sonda', x3c['probe'],
      '| NS', sum(1 for u in U if u['ns']), 'PS', sum(1 for u in U if u['x3'] is not None and not u['ns']),
      '| X4 valida', sum(1 for u in U if u['x4'] is not None))


# ---------------- estadistica (copiada de eval.py) ----------------
def boot(pn, co, cl):
    keys = {}
    idx = np.array([keys.setdefault(k, len(keys)) for k in cl]); n = len(keys)
    P = np.bincount(idx, weights=pn, minlength=n); C = np.bincount(idx, weights=co, minlength=n)
    rg = np.random.default_rng(SEED); out = []
    for _ in range(B // 500):
        I = rg.integers(0, n, size=(500, n)); out.append(P[I].sum(1) / C[I].sum(1))
    o = np.sort(np.concatenate(out))
    return float(o[int(0.05 * B)]), float(o[int(0.95 * B) - 1]), n


def stats(L, cierre=True):
    if not L: return None
    pn = np.array([x[2] for x in L]); co = np.array([x[3] for x in L])
    d = {'n': len(L), 'coste': float(co.sum()), 'EVw': float(pn.sum() / co.sum()), 'EVu': float((pn / co).mean())}
    if cierre: d['ICc'] = boot(pn, co, [x[1] for x in L])
    days = sorted(set(x[0] for x in L)); d['ndias'] = len(days)
    byd = {dd: [0.0, 0.0] for dd in days}
    for x in L: byd[x[0]][0] += x[2]; byd[x[0]][1] += x[3]
    d['dias'] = {dd: v[0] / v[1] for dd, v in byd.items()}
    d['pos'] = sum(1 for v in d['dias'].values() if v > 0)
    if len(days) >= 2: d['ICd'] = boot(pn, co, [x[0] for x in L])
    if len(days) >= 3:
        top = sorted(d['dias'], key=d['dias'].get)[-2:]
        R = [x for x in L if x[0] not in top]
        d['sin2'] = float(sum(x[2] for x in R) / sum(x[3] for x in R))
    return d


def fmt(lab, d):
    if d is None: return '%-26s n=0' % lab
    s = '%-26s n=%5d coste=%8.1f EVw=%+.4f EVu=%+.4f' % (lab, d['n'], d['coste'], d['EVw'], d['EVu'])
    if 'ICc' in d: s += ' IC90c=(%+.3f,%+.3f)' % d['ICc'][:2]
    if 'ICd' in d: s += ' IC90d=(%+.3f,%+.3f)' % d['ICd'][:2]
    s += ' dias>0=%d/%d' % (d['pos'], d['ndias'])
    if 'sin2' in d: s += ' sin2mejores=%+.4f' % d['sin2']
    return s


def tot_hold(u): return u['h']
def tot_i1(u): return u['h'] + (u['d4'] if u['d4'] is not None else 0.0)
def tot_a30(u): return u['h'] + (u['d30'] if u['ns'] else 0.0)
def titems(L, fn): return [(u['dia'], u['cie'], fn(u), u['cost']) for u in L]
def ditems(L, fn): return [(u['dia'], u['cie'], fn(u) - u['h'], u['cost']) for u in L]


print('\n===== A) EV TOTAL (todas las unidades con relleno P; Σpnl/Σcoste)  [esperado HOLD IS +0,0004 n=25427 | OOS -0,0318 n=5711]')
RS = {}
for nm, fn in (('HOLD', tot_hold), ('I1_vender_ya', tot_i1), ('A30_sin_rebote', tot_a30)):
    for lab, L in (('IS', IS), ('OOS', OO)):
        RS[(nm, lab)] = stats(titems(L, fn)); print(fmt(nm + ' ' + lab, RS[(nm, lab)]))
print('dias A30 IS ', ' '.join('%s:%+.3f' % (k[-2:], v) for k, v in sorted(RS[('A30_sin_rebote', 'IS')]['dias'].items())))
print('dias A30 OOS', ' '.join('%s:%+.3f' % (k[-2:], v) for k, v in sorted(RS[('A30_sin_rebote', 'OOS')]['dias'].items())))
ok = abs(RS[('HOLD', 'IS')]['EVw'] - 0.0004) < 0.0006 and abs(RS[('HOLD', 'OOS')]['EVw'] + 0.0318) < 0.0006
print('REPRODUCCION R1 HOLD:', 'OK' if ok else 'FALLA (no fiarse)')

print('\n===== B) Δ(regla − HOLD) PAREADO sobre todas las unidades (= ΔEV total por € de coste total) + pesimista')
DD = {}
for nm, fn in (('I1_vender_ya', tot_i1), ('A30_sin_rebote', tot_a30)):
    for lab, L in (('IS', IS), ('OOS', OO)):
        DD[(nm, lab)] = d = stats(ditems(L, fn)); print(fmt('Δ ' + nm + ' ' + lab, d))
for lab in ('IS', 'OOS'):
    d = DD[('A30_sin_rebote', lab)]
    print('EV total PESIMISTA A30 %s = HOLD_pes %+.3f + Δ %+.4f = %+.4f  (IC90d inferior %+.4f)' % (
        lab, PESS[lab], d['EVw'], PESS[lab] + d['EVw'], PESS[lab] + d['ICd'][0]))

print('\n===== C) A30 sobre el conjunto DISPARADO: NS (sin rebote) vs INVERSION PS vs PLACEBO; Δ por € de coste del conjunto')
NS = [u for u in U if u['ns']]; PS = [u for u in U if u['x3'] is not None and not u['ns']]
for nm, S in (('NS (regla)', NS), ('PS (inversion)', PS)):
    for lab, L in (('IS', [u for u in S if u['dia'] not in OOS]), ('OOS', [u for u in S if u['dia'] in OOS])):
        print(fmt('Δ %s %s' % (nm, lab), stats([(u['dia'], u['cie'], u['d30'], u['cost']) for u in L])))
UN = [u for u in U if u['x3'] is not None and u['dia'] not in OOS]; nI = sum(1 for u in NS if u['dia'] not in OOS)
dv = np.array([u['d30'] for u in UN]); cv = np.array([u['cost'] for u in UN]); rg = np.random.default_rng(SEED)
pl = []
for _ in range(500):
    ix = rg.choice(len(UN), size=nI, replace=False); pl.append(dv[ix].sum() / cv[ix].sum())
pl = np.array(pl); evns = sum(u['d30'] for u in NS if u['dia'] not in OOS) / sum(u['cost'] for u in NS if u['dia'] not in OOS)
print('PLACEBO IS (500 aleatorios de NS∪PS, n=%d): media %+.4f p5..p95 (%+.4f,%+.4f) | NS IS %+.4f | frac placebo>=NS %.3f' % (
    nI, pl.mean(), np.percentile(pl, 5), np.percentile(pl, 95), evns, float(np.mean(pl >= evns))))


def fill(lab, T):
    if not T: return
    full = sum(1 for u in T if u['bsx'] >= u['rem'] - 1e-9) / len(T); frac = sum(u['qx'] / u['rem'] for u in T if u['rem'] > 0) / len(T)
    print('FILL-ABILITY salida %-12s n=%d  bs>=restante %.1f%%  q/restante medio %.3f  bid medio %.3f  acierto medio %.3f' % (
        lab, len(T), 100 * full, frac, sum(u['bbx'] for u in T) / len(T), sum(u['g'] for u in T) / len(T)))


T4 = []; T3 = []
for u in U:
    if u['d4'] is not None: T4.append(dict(u, D=u['d4'], bbx=u['x4'][0], bsx=u['x4'][1], rem=u['sh'], qx=u['q4']))
    if u['ns']: T3.append(dict(u, D=u['d30'], bbx=u['x3'][0], bsx=u['x3'][1], rem=u['sh'], qx=u['q3']))
fill('I1 (tx+250ms)', T4); fill('A30 NS (T-30s)', T3)
print('unidades P rellenadas con ASK/BID ausente en la sonda de salida: I1 %d de %d | A30: ver bloque NA/vacia arriba' % (
    sum(1 for u in U if u['d4'] is None), len(U)))


# ---------------- D) calibracion del bid (descriptiva, sonda de ejecucion) ----------------
def bk(b):
    return ('<=0.02' if b <= 0.02 else '0.02-0.05' if b <= 0.05 else '0.05-0.10' if b <= 0.10 else '0.10-0.20' if b <= 0.20
            else '0.20-0.40' if b <= 0.40 else '>0.40')
print('\n===== D) CALIBRACION del bid de salida (todas las fechas; Δ/acción = bid − fee − acierto; <0 => salir cuesta)')
for lab, T in (('I1 tx+250ms', T4), ('A30 NS T-30s', T3)):
    for b in ('<=0.02', '0.02-0.05', '0.05-0.10', '0.10-0.20', '0.20-0.40', '>0.40'):
        S = [u for u in T if bk(u['bbx']) == b]
        if len(S) < 20: continue
        sh = sum(u['qx'] for u in S)
        print('%-13s bid %-9s n=%5d bid medio %.3f acierto %.3f Δ/acc %+.4f (por € de coste del tramo %+.4f)' % (
            lab, b, len(S), sum(u['bbx'] for u in S) / len(S), sum(u['g'] for u in S) / len(S),
            sum(u['D'] for u in S) / sh if sh > 0 else float('nan'), sum(u['D'] for u in S) / sum(u['cost'] for u in S)))


# ---------------- E) escaneo de celdas con max-statistic ----------------
def cells(exec_based=True):
    C = []
    for c in ('BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB'): C.append(('coin=' + c, lambda u, c=c: u['coin'] == c))
    for c in 'AB': C.append(('causa=' + c, lambda u, c=c: u['cause'] == c))
    C += [('np=1', lambda u: u['npart'] == 1), ('np>=2', lambda u: u['npart'] >= 2),
          ('Te<120', lambda u: u['Te'] < 120), ('Te120-180', lambda u: 120 <= u['Te'] < 180),
          ('Te180-240', lambda u: 180 <= u['Te'] < 240), ('Te>=240', lambda u: u['Te'] >= 240),
          ('spr=0.02', lambda u: u['spr'] < 0.025), ('spr>=0.03', lambda u: u['spr'] >= 0.025),
          ('v60NA', lambda u: u['v60'] is None), ('v60<3', lambda u: u['v60'] is not None and u['v60'] < 3),
          ('v60 3-10', lambda u: u['v60'] is not None and 3 <= u['v60'] < 10), ('v60>=10', lambda u: u['v60'] is not None and u['v60'] >= 10),
          ('hora00-07', lambda u: u['hora'] < 8), ('hora08-15', lambda u: 8 <= u['hora'] < 16), ('hora16-23', lambda u: u['hora'] >= 16),
          ('espera<10s', lambda u: u['wait'] is not None and u['wait'] < 10), ('espera10-60s', lambda u: u['wait'] is not None and 10 <= u['wait'] < 60),
          ('espera>=60s', lambda u: u['wait'] is not None and u['wait'] >= 60)]
    if exec_based:
        for b in ('<=0.02', '0.02-0.05', '0.05-0.10', '0.10-0.20', '0.20-0.40', '>0.40'): C.append(('EX bid ' + b, lambda u, b=b: bk(u['bbx']) == b))
        C += [('EX dbid<=-0.10', lambda u: u['bbx'] - u['avg'] <= -0.10), ('EX dbid-0.10..-0.05', lambda u: -0.10 < u['bbx'] - u['avg'] <= -0.05),
              ('EX dbid-0.05..-0.02', lambda u: -0.05 < u['bbx'] - u['avg'] <= -0.02), ('EX dbid-0.02..0', lambda u: -0.02 < u['bbx'] - u['avg'] <= 0.0),
              ('EX dbid>0', lambda u: u['bbx'] - u['avg'] > 0.0), ('EX bs>=restante', lambda u: u['bsx'] >= u['rem'] - 1e-9),
              ('EX bs<restante', lambda u: u['bsx'] < u['rem'] - 1e-9)]
    return C


def scan(lab, T, nmin=40, mind=10, Bn=4000):
    Ti = [u for u in T if u['dia'] not in OOS]; To = [u for u in T if u['dia'] in OOS]
    days = sorted(set(u['dia'] for u in Ti)); di = {d: i for i, d in enumerate(days)}; nd = len(days); rows = []
    for nm, pr in cells():
        sel = [u for u in Ti if pr(u)]
        if len(sel) < nmin or len(set(u['dia'] for u in sel)) < mind: continue
        P = np.zeros(nd); Cc = np.zeros(nd)
        for u in sel: P[di[u['dia']]] += u['D']; Cc[di[u['dia']]] += u['cost']
        so = [u for u in To if pr(u)]
        evo = sum(u['D'] for u in so) / sum(u['cost'] for u in so) if so else float('nan')
        rows.append((nm, len(sel), P, Cc, evo, len(so)))
    Pm = np.array([r[2] for r in rows]); Cm = np.array([r[3] for r in rows]); ev = Pm.sum(1) / Cm.sum(1)
    rg = np.random.default_rng(SEED); cnt = rg.multinomial(nd, [1.0 / nd] * nd, size=Bn).astype(float)
    with np.errstate(divide='ignore', invalid='ignore'):
        evb = (cnt @ Pm.T) / (cnt @ Cm.T)
    se = np.nanstd(evb, axis=0); lo = np.nanpercentile(evb, 5, axis=0); hi = np.nanpercentile(evb, 95, axis=0)
    z = ev / se; zb = (evb - ev) / se; pmax = float(np.mean(np.nanmax(zb, axis=1) >= np.nanmax(z)))
    order = np.argsort(-ev)
    print('\n===== E) CELDAS %s: K=%d (n>=%d y >=%d dias en IS); Δ por € de coste de la celda; max-statistic p=%.3f; celdas con IC90d inferior>0: %d' % (
        lab, len(rows), nmin, mind, pmax, int(np.sum(lo > 0))))
    for i in order:
        r = rows[i]
        print('  %-20s n=%5d coste=%7.1f Δ_IS=%+.4f IC90d=(%+.3f,%+.3f) | OOS Δ=%+.4f n=%d' % (r[0], r[1], float(Cm[i].sum()), ev[i], lo[i], hi[i], r[4], r[5]))


scan('I1 (vender ya, tx+250ms)', T4)
scan('A30 NS (T-30s)', T3)
print('\nFIN eval_sal.py')
