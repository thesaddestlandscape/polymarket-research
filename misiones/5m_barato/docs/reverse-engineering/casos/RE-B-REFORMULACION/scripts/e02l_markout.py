#!/usr/bin/env python3
"""E-RE-BR-02L: perfil temporal del coste de condicionamiento de B (ledger puja_fin.rellenos + desenlace oficial). Solo lectura."""
import csv, gzip, json, glob, random, collections

DL = '/root/polymarket-research-datalogs'
gana = {}
for f in sorted(glob.glob(DL + '/etiquetado_pasivo_B/etiquetado_B_2026-10-2*.csv.gz')):
    for r in csv.DictReader(gzip.open(f, 'rt')):
        if r['resuelto'] == '1' and r['gana_lado'] != '':
            gana[(r['mercado'], r['lado'])] = float(r['gana_lado'])
F = []
seen = set()
for l in open(DL + '/experimento_h47_B_ledger.jsonl'):
    if '"puja_fin"' not in l:
        continue
    try:
        d = json.loads(l)
    except Exception:
        continue
    if d.get('tipo') != 'puja_fin':
        continue
    g = gana.get((d['slug'], d['lado']))
    for r in d.get('rellenos') or []:
        key = (r.get('oid'), r.get('t_deteccion'))
        if key in seen:
            continue
        seen.add(key)
        F.append(dict(slug=d['slug'], g=g, acc=float(r.get('acc') or 0), p=float(r['precio']), m0=r.get('mid0'),
                      m5=r.get('mid_5s'), m30=r.get('mid_30s'), m120=r.get('mid_120s'),
                      tc=bool(r.get('tras_cancel')), esp=r.get('espera_s')))
print('rellenos en puja_fin', len(F), 'con desenlace', sum(1 for x in F if x['g'] is not None))
F = [x for x in F if x['g'] is not None and x['acc'] > 0 and x['m0'] is not None]
miss = {h: sum(1 for x in F if x[h] is None) for h in ('m5', 'm30', 'm120')}
print('usables', len(F), 'missing', miss, 'acc', round(sum(x['acc'] for x in F), 1), 'coste', round(sum(x['acc'] * x['p'] for x in F), 2))
FF = [x for x in F if None not in (x['m5'], x['m30'], x['m120'])]

def stats(S):
    w = sum(x['acc'] * x['p'] for x in S)
    o = {}
    for nm, fn in (('ev', lambda x: x['g'] - x['p']), ('spread0', lambda x: x['m0'] - x['p']),
                   ('D5', lambda x: x['m5'] - x['m0']), ('D30', lambda x: x['m30'] - x['m0']),
                   ('D120', lambda x: x['m120'] - x['m0']), ('DG', lambda x: x['g'] - x['m0']),
                   ('mk5', lambda x: x['m5'] - x['p']), ('mk120', lambda x: x['m120'] - x['p'])):
        o[nm] = sum(x['acc'] * fn(x) for x in S) / w if w else float('nan')
    o['w'] = w; o['n'] = len(S)
    return o

b = stats(FF)
print('base', {k: round(v, 4) for k, v in b.items()})
print('ratio D5/DG %.3f  D30/DG %.3f  D120/DG %.3f' % (b['D5'] / b['DG'], b['D30'] / b['DG'], b['D120'] / b['DG']))
cl = collections.defaultdict(list)
for x in FF:
    cl[x['slug'].rsplit('-', 1)[1]].append(x)
ks = list(cl); random.seed(20261026)
acc = collections.defaultdict(list)
for _ in range(2000):
    S = [y for c in random.choices(ks, k=len(ks)) for y in cl[c]]
    s = stats(S)
    for k in ('ev', 'D5', 'D30', 'D120', 'DG', 'mk5'):
        acc[k].append(s[k])
    acc['r5'].append(s['D5'] / s['DG'] if s['DG'] else float('nan'))
for k, v in acc.items():
    v = sorted(z for z in v if z == z); print('  IC90 %-5s (%.4f, %.4f)' % (k, v[int(.05 * len(v))], v[int(.95 * len(v))]))
print('  cierres', len(ks))
for lab, S in (('tras_cancel', [x for x in FF if x['tc']]), ('resto', [x for x in FF if not x['tc']])):
    s = stats(S); print(lab, 'share_w %.3f' % (s['w'] / b['w']), {k: round(v, 3) for k, v in s.items()})
