#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""alpha_miner_b_27oct/eval.py — manda PREREG_ALPHA_B.md (congelado antes de ver resultados; OOS se mira UNA vez).
Lee units/u_*.csv.gz (sim.py) + desenlace oficial (maker_ms_desenlaces_cache.json)."""
import gzip, csv, json, glob, sys
from collections import defaultdict
import numpy as np

BASE = '/root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct/'
G = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
OOS = {'2026-10-23', '2026-10-24', '2026-10-25', '2026-10-26'}
B = 2000; SEED = 2711


def fee(p): return 0.07 * p * (1 - p)
def F(x):
    if x in (None, '', 'None'): return None
    return float(x)
def PR(x):
    if x in (None, '', 'NA'): return None
    return [None if y == '' else float(y) for y in x.split('|')]   # bb, bs, ba, as


rows = []; seen = set(); dup = 0; miss = 0; cov = defaultdict(lambda: [0, 0])
for p in sorted(glob.glob(BASE + 'units/u_*.csv.gz')):
    with gzip.open(p, 'rt') as f:
        for r in csv.DictReader(f):
            key = (r['mercado'], r['lado'])
            if key in seen: dup += 1; continue
            seen.add(key)
            w = G.get(str(r['mercado'])); cov[r['dia']][0] += 1
            if w not in ('YES', 'NO'): miss += 1; continue
            cov[r['dia']][1] += 1
            r['g'] = 1.0 if w == r['lado'] else 0.0
            rows.append(r)
print('unidades evaluables', len(rows), 'duplicadas', dup, 'sin desenlace', miss)
print('cobertura desenlace por dia', ' '.join('%s:%d/%d' % (d[-2:], v[1], v[0]) for d, v in sorted(cov.items())))


def ordpnl(r, nm, g):
    if r.get(nm + '_sh0') in (None, ''): return None
    return F(r[nm + '_proc']) - F(r[nm + '_fee']) + F(r[nm + '_rem']) * g
def R_hold(k):
    def f(r, g):
        sh = F(r[k + '_sh']); c = F(r[k + '_cost'])
        if not sh or sh <= 0: return None
        return (sh * g - c, c)
    return f
def R_ord(k, nm):
    def f(r, g):
        sh = F(r[k + '_sh']); c = F(r[k + '_cost'])
        if not sh or sh <= 0: return None
        v = ordpnl(r, nm, g)
        return (sh * g - c, c) if v is None else (v - c, c)
    return f
def R_x4(r, g):
    sh = F(r['P_sh']); c = F(r['P_cost'])
    if not sh or sh <= 0: return None
    v = PR(r['X4'])
    if v is None or v[0] is None or v[1] is None: return (sh * g - c, c)
    q = min(sh, v[1]); bid = v[0]
    return (q * bid - q * fee(bid) + (sh - q) * g - c, c)
def R_x5(r, g):
    sh = F(r['P_sh']); c = F(r['P_cost'])
    if not sh or sh <= 0: return None
    v = PR(r['X5'])
    if v is None or v[2] is None or v[3] is None: return (sh * g - c, c)
    q = min(sh, v[3]); ask = v[2]; hc = q * ask + q * fee(ask)
    return (sh * g + q * (1 - g) - c - hc, c + hc)
def R_pl_hold(r, g):
    be = F(r['be']); return (5 * g - 5 * be, 5 * be)
def R_pl_x1(r, g):
    be = F(r['be']); v = ordpnl(r, 'PL_X1', g)
    return (5 * g - 5 * be, 5 * be) if v is None else (v - 5 * be, 5 * be)
def dask(r):
    v = PR(r['D'])
    if v is None or v[2] is None or v[3] is None or v[3] < 5 - 1e-9: return None
    return v[2]
def R_d(r, g):
    a = dask(r)
    if a is None: return None
    c = 5 * a + 5 * fee(a); return (5 * g - c, c)
def R_d_x1(r, g):
    a = dask(r)
    if a is None: return None
    c = 5 * a + 5 * fee(a); v = ordpnl(r, 'D_X1', g)
    return (5 * g - c, c) if v is None else (v - c, c)
def R_di(r, g):
    v = PR(r['DI'])
    if v is None or v[2] is None or v[3] is None or v[3] < 5 - 1e-9: return None
    a = v[2]; c = 5 * a + 5 * fee(a); return (5 * (1 - g) - c, c)


RULES = [('R1_P_HOLD', R_hold('P')), ('R2_P_X1', R_ord('P', 'P_X1')), ('R3_D_HOLD', R_d),
         ('s_P_X2', R_ord('P', 'P_X2')), ('s_P_X3_dumpT30', R_ord('P', 'P_X3')), ('s_P_XI_inversion', R_ord('P', 'P_XI')),
         ('s_P_X4_dumpnow', R_x4), ('s_P_X5_hedge', R_x5),
         ('s_L1_HOLD', R_hold('L1')), ('s_L1_X1', R_ord('L1', 'L1_X1')), ('s_L5_HOLD', R_hold('L5')), ('s_L5_X1', R_ord('L5', 'L5_X1')),
         ('s_PC_HOLD_conC', R_hold('PC')), ('s_PC_X1_conC', R_ord('PC', 'PC_X1')),
         ('PLAC_HOLD', R_pl_hold), ('PLAC_X1', R_pl_x1), ('s_D_X1', R_d_x1), ('INV_D_favorito', R_di)]


def tb(r):
    T = F(r['Te'])
    return '060-120' if T < 120 else '120-180' if T < 180 else '180-240' if T < 240 else '240-290'
def hb(r):
    h = int(r['hora']); return '00-07' if h < 8 else '08-15' if h < 16 else '16-23'
def vb(r):
    v = F(r.get('v60'))
    return 'NA' if v is None else '<3' if v < 3 else '3-10' if v < 10 else '>=10'


def items(name, fn, sel=None):
    out = []
    for r in rows:
        if sel is not None and not sel(r): continue
        v = fn(r, r['g'])
        if v is None or v[1] <= 0: continue
        out.append((r['dia'], int(r['cierre']), v[0], v[1], r))
    return out


def boot(pn, co, cl):
    keys = {}
    idx = np.array([keys.setdefault(k, len(keys)) for k in cl]); n = len(keys)
    P = np.bincount(idx, weights=pn, minlength=n); C = np.bincount(idx, weights=co, minlength=n)
    rg = np.random.default_rng(SEED); out = []
    for _ in range(B // 500):
        I = rg.integers(0, n, size=(500, n)); out.append(P[I].sum(1) / C[I].sum(1))
    o = np.sort(np.concatenate(out))
    return float(o[int(0.05 * B)]), float(o[int(0.95 * B) - 1]), n


def stats(L):
    if not L: return None
    pn = np.array([x[2] for x in L]); co = np.array([x[3] for x in L])
    d = {'n': len(L), 'coste': float(co.sum()), 'EVw': float(pn.sum() / co.sum()), 'EVu': float((pn / co).mean())}
    d['ICc'] = boot(pn, co, [x[1] for x in L])
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


def fmt(lab, d, dias=False):
    if d is None: return '%-22s n=0' % lab
    s = '%-22s n=%5d cierres=%4d coste=%8.1f EVw=%+.4f EVu=%+.4f IC90c=(%+.3f,%+.3f)' % (
        lab, d['n'], d['ICc'][2], d['coste'], d['EVw'], d['EVu'], d['ICc'][0], d['ICc'][1])
    if 'ICd' in d: s += ' IC90d=(%+.3f,%+.3f)' % d['ICd'][:2]
    s += ' dias>0=%d/%d' % (d['pos'], d['ndias'])
    if 'sin2' in d: s += ' sin2mejores=%+.4f' % d['sin2']
    if dias: s += '\n      ' + ' '.join('%s:%+.3f' % (k[-2:], v) for k, v in sorted(d['dias'].items()))
    return s


def delta(fa, fb, sel):
    L = []
    for r in rows:
        if not sel(r): continue
        a = fa(r, r['g']); b = fb(r, r['g'])
        if a is None or b is None or b[1] <= 0: continue
        L.append((r['dia'], int(r['cierre']), a[0] - b[0], b[1], r))
    return stats(L)


IS = lambda r: r['dia'] not in OOS
OO = lambda r: r['dia'] in OOS
RES = {}
print('\n===== REGLAS (IS = 05-22 Oct; OOS = 23-26 Oct, mirado una vez)')
for nm, fn in RULES:
    dI = stats(items(nm, fn, IS)); dO = stats(items(nm, fn, OO)); RES[nm] = (dI, dO)
    print(fmt(nm + ' IS', dI, dias=nm.startswith('R')))
    print(fmt(nm + ' OOS', dO, dias=True))

print('\n===== DELTAS emparejados (misma base de coste; IS | OOS)')
DL = {}
for lab, fa, fb in (('R2-R1 (X1 vs HOLD)', R_ord('P', 'P_X1'), R_hold('P')), ('PLAC_X1-PLAC_HOLD', R_pl_x1, R_pl_hold),
                    ('X2-R1', R_ord('P', 'P_X2'), R_hold('P')), ('X3-R1', R_ord('P', 'P_X3'), R_hold('P')),
                    ('XI(inv)-R1', R_ord('P', 'P_XI'), R_hold('P')), ('X4-R1', R_x4, R_hold('P')),
                    ('L1_X1-L1_HOLD', R_ord('L1', 'L1_X1'), R_hold('L1')), ('D_X1-D_HOLD', R_d_x1, R_d)):
    a = delta(fa, fb, IS); b = delta(fa, fb, OO); DL[lab] = (a, b)
    print(fmt(lab + ' IS', a)); print(fmt(lab + ' OOS', b))

print('\n===== DIAGNOSTICO de rellenos (todas las fechas)')
P = [r for r in rows if F(r['P_sh']) and F(r['P_sh']) > 0]
full = [r for r in P if r['P_tc'] not in ('', None)]
print('unidades', len(rows), 'con relleno P', len(P), 'completas', len(full), 'causa 1er relleno',
      {c: sum(1 for r in P if r['P_cause'] == c) for c in 'ABC'})
lat = sorted((F(r['P_t1']) - F(r['te'])) / 1000.0 for r in P)
if lat: print('segundos te->1er relleno p10/p50/p90 %.1f/%.1f/%.1f' % (lat[len(lat) // 10], lat[len(lat) // 2], lat[9 * len(lat) // 10]))
for nm in ('P_X1', 'P_X2', 'PL_X1', 'D_X1'):
    S = [r for r in rows if r.get(nm + '_sh0') not in (None, '')]
    if not S: continue
    vend = sum(1 for r in S if F(r[nm + '_rem']) <= 1e-9); modes = defaultdict(int)
    for r in S: modes[r[nm + '_mode']] += 1
    print('%-6s ordenes %d vendidas enteras %d (%.1f%%) modos %s' % (nm, len(S), vend, 100.0 * vend / len(S), dict(modes)))
ex = [r for r in full if F(r['P_X1_rem']) <= 1e-9]; nx = [r for r in full if F(r['P_X1_rem']) > 1e-9]
for lab, S in (('X1 vendidas', ex), ('X1 no vendidas', nx)):
    if S: print('%-15s n=%d acierto del barato %.3f precio medio entrada %.3f' % (lab, len(S), sum(r['g'] for r in S) / len(S), sum(F(r['P_cost']) for r in S) / sum(F(r['P_sh']) for r in S)))

print('\n===== REGIMENES (todas las fechas, EVw e IC90 por cierre)')
for nm in ('R1_P_HOLD', 'R2_P_X1', 'R3_D_HOLD', 'PLAC_HOLD'):
    fn = dict(RULES)[nm]
    for dim, f in (('moneda', lambda r: r['coin']), ('T_te', tb), ('hora', hb), ('vol60', vb)):
        vals = sorted(set(f(r) for r in rows))
        parts = []
        for v in vals:
            d = stats(items(nm, fn, lambda r, v=v, f=f: f(r) == v))
            if d: parts.append('%s:%+.3f(n=%d,%+.2f..%+.2f)' % (v, d['EVw'], d['n'], d['ICc'][0], d['ICc'][1]))
        print('%-10s %-7s %s' % (nm, dim, ' '.join(parts)))


def verdict(nm):
    dI, dO = RES[nm]
    if dI is None or dI['n'] < 400: return 'INSUFFICIENT_EVIDENCE (n IS < 400)'
    if dI['ICd'][1] < 0 or (dI['EVw'] < 0 and dO is not None and dO['EVw'] < 0): return 'REJECTED'
    ok = (dI['EVw'] > 0 and dI['ICd'][0] > 0 and dI['pos'] >= 0.6 * dI['ndias'] and dI.get('sin2', -1) > 0
          and dO is not None and dO['EVw'] > 0 and dO['ICc'][0] > 0)
    if nm == 'R2_P_X1':
        a = DL['R2-R1 (X1 vs HOLD)'][0]; pl = DL['PLAC_X1-PLAC_HOLD'][0]
        ok = ok and a is not None and a['ICc'][0] > 0 and pl is not None and a['EVw'] > pl['EVw']
    return 'PROMISING' if ok else 'INSUFFICIENT_EVIDENCE'


print('\n===== VEREDICTOS PRERREGISTRADOS')
for nm in ('R1_P_HOLD', 'R2_P_X1', 'R3_D_HOLD'): print(nm, '->', verdict(nm))
