#!/usr/bin/env python3
"""Evalua v_*.csv.gz (vsim.py) con desenlace oficial; compara con units/ del alpha miner."""
import gzip, csv, json, glob, random, sys
from collections import defaultdict
import numpy as np
B = '/root/polymarket-research/experimentos/5m_barato/validador_alpha_b_27oct/'
A = '/root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct/units/'
G = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
OOS = {'2026-10-23', '2026-10-24', '2026-10-25', '2026-10-26'}
def f(x): return None if x in (None, '', 'None', 'NA') else float(x)
def fee(p): return 0.07 * p * (1 - p)
V = {}
for p in sorted(glob.glob(B + 'v_2026-10-*.csv.gz')):
    for r in csv.DictReader(gzip.open(p, 'rt')): V[(r['mercado'], r['lado'])] = r
AU = {}
for p in sorted(glob.glob(A + 'u_*.csv.gz')):
    d = p[-17:-7]
    if not glob.glob(B + 'v_%s.csv.gz' % d): continue
    for r in csv.DictReader(gzip.open(p, 'rt')): AU[(r['mercado'], r['lado'])] = r
print('unidades validador', len(V), 'alpha (mismos dias)', len(AU), 'interseccion', len(set(V) & set(AU)))
# --- comparacion unidad a unidad
cmp = defaultdict(lambda: [0, 0]); common = sorted(set(V) & set(AU))
def eq(a, b, tol=1e-6):
    if a is None and b is None: return True
    if a is None or b is None: return False
    return abs(a - b) <= tol
for k in common:
    v, a = V[k], AU[k]
    Da = a['D'].split('|') if a['D'] not in ('', 'NA') else None
    dask = float(Da[2]) if Da and Da[2] else None
    for nm, x, y in (('te', f(v['te']), f(a['te'])), ('be', f(v['be']), f(a['be'])), ('P_sh', f(v['sh']), f(a['P_sh'])),
                     ('P_cost', f(v['cost']), f(a['P_cost'])), ('P_t1', f(v['t1']), f(a['P_t1'])), ('D_ask', f(v['d_ask']), dask),
                     ('X1_rem', f(v['xrem']) if f(v['sh']) else None, f(a['P_X1_rem']) if f(a['P_sh']) else None),
                     ('X1_proc', f(v['xproc']) if f(v['sh']) else None, f(a['P_X1_proc']) if f(a['P_sh']) else None)):
        cmp[nm][0] += 1; cmp[nm][1] += eq(x, y, 1e-4)
print('coincidencia por campo', {k: '%d/%d' % (v[1], v[0]) for k, v in cmp.items()})
random.seed(7); S50 = random.sample(common, min(50, len(common)))
ok50 = sum(1 for k in S50 if eq(f(V[k]['sh']), f(AU[k]['P_sh'])) and eq(f(V[k]['cost']), f(AU[k]['P_cost']), 1e-4)
           and eq(f(V[k]['te']), f(AU[k]['te'])) and eq(f(V[k]['be']), f(AU[k]['be'])))
print('muestra 50 (te,be,P_sh,P_cost identicos):', ok50, '/ 50')
for k in S50[:6]: print('  ', k, V[k]['dia'], 'val sh/cost/t1', V[k]['sh'], V[k]['cost'], V[k]['t1'], '| alpha', AU[k]['P_sh'], AU[k]['P_cost'], AU[k]['P_t1'])
# --- desenlace
rows = []; miss = 0; chk = [0, 0]
for k, r in V.items():
    w = G.get(r['mercado'])
    if w not in ('YES', 'NO'): miss += 1; continue
    r['g'] = 1.0 if w == r['lado'] else 0.0
    fm = f(r['fin_mid'])
    if fm is not None and (fm > 0.9 or fm < 0.1): chk[0] += 1; chk[1] += ((fm > 0.5) == (r['g'] == 1.0))
    rows.append(r)
print('con desenlace', len(rows), 'sin', miss, '| desenlace vs ultimo mid del libro (mid>0,9/<0,1): %d/%d coinciden' % (chk[1], chk[0]))
def boot(pn, co, cl, seed=99):
    keys = {}; idx = np.array([keys.setdefault(x, len(keys)) for x in cl]); n = len(keys)
    P = np.bincount(idx, weights=pn, minlength=n); C = np.bincount(idx, weights=co, minlength=n)
    rg = np.random.default_rng(seed); o = []
    for _ in range(4):
        I = rg.integers(0, n, size=(500, n)); o.append(P[I].sum(1) / C[I].sum(1))
    o = np.sort(np.concatenate(o)); return o[100], o[1899]
def st(lab, L):
    if not L: print('%-28s n=0' % lab); return
    pn = np.array([x[2] for x in L]); co = np.array([x[3] for x in L])
    byd = defaultdict(lambda: [0., 0.])
    for x in L: byd[x[0]][0] += x[2]; byd[x[0]][1] += x[3]
    dv = {d: v[0] / v[1] for d, v in byd.items()}; top = sorted(dv, key=dv.get)[-2:]
    R = [x for x in L if x[0] not in top]
    s2 = sum(x[2] for x in R) / sum(x[3] for x in R) if R else float('nan')
    c1 = boot(pn, co, [x[1] for x in L]); c2 = boot(pn, co, [x[0] for x in L]) if len(dv) > 1 else (np.nan, np.nan)
    print('%-28s n=%6d EVw=%+.4f IC90cierre(%+.3f,%+.3f) IC90dia(%+.3f,%+.3f) dias>0 %d/%d sin2mejores %+.4f' % (
        lab, len(L), pn.sum() / co.sum(), c1[0], c1[1], c2[0], c2[1], sum(v > 0 for v in dv.values()), len(dv), s2))
def R1(r):
    sh, c = f(r['sh']), f(r['cost']); return (sh * r['g'] - c, c) if sh else None
def R1S(r):
    sh, c = f(r['shS']), f(r['costS']); return (sh * r['g'] - c, c) if sh else None
def R1C(r):
    sh, c = f(r['shC']), f(r['costC']); return (sh * r['g'] - c, c) if sh else None
def R1nx(r):
    return R1(r) if f(r['nfx']) == 0 and f(r['nfa']) == 0 else None
def R2(r):
    sh, c = f(r['sh']), f(r['cost'])
    if not sh: return None
    if r['xa'] in ('', 'None'): return (sh * r['g'] - c, c)
    return (f(r['xproc']) - f(r['xfee']) + f(r['xrem']) * r['g'] - c, c)
def R3(r):
    a, s = f(r['d_ask']), f(r['d_as'])
    if a is None or s is None or s < 5 - 1e-9: return None
    c = 5 * a + 5 * fee(a); return (5 * r['g'] - c, c)
def PL(r):
    be = f(r['be']); return (5 * r['g'] - 5 * be, 5 * be)
def mkpl(col):
    def fn(r):
        a = AU.get((r['mercado'], r['lado']))
        if a is None: return None
        bb, ba = f(a['bb_e']), f(a['ba_e'])
        p = {'bid': bb, 'mid': (bb + ba) / 2, 'ask_sinfee': ba, 'ask_fee': ba + fee(ba)}[col]
        return (5 * r['g'] - 5 * p, 5 * p)
    return fn
RU = [('R1', R1), ('R2', R2), ('R3', R3), ('PLACEBO bb+0,01', PL), ('R1 cola estricta', R1S), ('R1 + regla C', R1C),
      ('R1 sin rellenos cruzados/detras', R1nx), ('PL al bid', mkpl('bid')), ('PL al mid', mkpl('mid')),
      ('PL al ask sin fee', mkpl('ask_sinfee')), ('PL al ask+fee', mkpl('ask_fee'))]
for nm, fn in RU:
    for lab, sel in (('IS', lambda r: r['dia'] not in OOS), ('OOS', lambda r: r['dia'] in OOS)):
        L = []
        for r in rows:
            if not sel(r): continue
            v = fn(r)
            if v is None or v[1] <= 0: continue
            L.append((r['dia'], r['cierre'], v[0], v[1]))
        st(nm + ' ' + lab, L)
# rellenos y recotizaciones
P = [r for r in rows if f(r['sh'])]
nf = sum(f(r['nfill']) for r in P); print('rellenos R1: parciales %d; con ba<=b\' (libro ya cruzado) %.1f%%; con bb_actual>=b\' (no cabeza) %.1f%%' % (
    nf, 100 * sum(f(r['nfx']) for r in P) / nf, 100 * sum(f(r['nfa']) for r in P) / nf))
act = [r for r in rows if f(r['act_s']) and f(r['act_s']) > 0]
rr = sorted(f(r['nrep']) / f(r['act_s']) for r in act)
print('recotizaciones por unidad: mediana %.0f, p90 %.0f; por segundo activo p50 %.2f p90 %.2f' % (
    np.median([f(r['nrep']) for r in act]), np.percentile([f(r['nrep']) for r in act], 90), rr[len(rr) // 2], rr[9 * len(rr) // 10]))
for p in sorted(glob.glob(B + 'v_*_rate.json')):
    j = json.load(open(p)); print('  ', j['dia'], 'acciones/seg globales p99 %d max %d, total %d' % (j['rep_p99'], j['rep_max'], j['rep_total']))
