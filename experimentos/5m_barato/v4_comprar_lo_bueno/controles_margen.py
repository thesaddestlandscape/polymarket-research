#!/usr/bin/env python3
"""EV por margen pre-existente (poblacion): controles B3 del vigia V4 (compra del 5m lado s cada 10 s, ejecutada a L215), desenlace oficial.
Unidad = fila de control (instante de 10 s; NO independientes). IC por cierre (clusters). Chronologico: 06-12 vs 13-18 Oct."""
import csv, glob, json, collections, random, statistics as st
from datetime import datetime, timezone
D = '/root/polymarket-research-datalogs/'
des = json.load(open(D + 'maker_ms_desenlaces_cache.json'))
def fee(p): return 0.07 * p * (1 - p)
rows = []
for f in sorted(glob.glob(D + 'vigia_5m_barato/controles_2026-10-*.csv')):
    dia = f[-14:-4]
    if dia < '2026-10-06': continue
    for r in csv.DictReader(open(f)):
        if r['market_compra'] not in des or r['clase'] == 'UNKNOWN': continue
        acc = float(r['acciones'] or 0)
        if acc <= 0 or r['precio'] in ('', 'None'): continue
        p = float(r['precio']); g = (des[r['market_compra']] == 'YES') == (r['lado'] == 'Up')
        rows.append(dict(dia=dia, mon=r['moneda'], cierre=r['cierre'], m=float(r['margen_neto']), p=p, acc=acc, g=g, pnl=acc * ((1.0 if g else 0) - p - fee(p)), c=acc * (p + fee(p)), t=int(r['t'])))
print('filas control ejecutables a L215:', len(rows))
bins = [(-9, -0.10), (-0.10, -0.05), (-0.05, 0.0), (0.0, 0.025), (0.025, 0.05), (0.05, 9)]
rng = random.Random(2)
def boot(g, key='cierre', n=2000):
    cl = collections.defaultdict(list)
    for r in g: cl[(r['dia'], r['mon'], r['cierre'])].append(r)
    ks = list(cl); res = []
    for _ in range(n):
        s = [cl[rng.choice(ks)] for _ in ks]
        c = sum(r['c'] for x in s for r in x)
        if c > 0: res.append(sum(r['pnl'] for x in s for r in x) / c)
    res.sort(); return (round(res[int(.05 * len(res))], 3), round(res[int(.95 * len(res))], 3)) if res else None
for nom, sel in (('TODO 06-18', lambda r: True), ('06-12', lambda r: r['dia'] <= '2026-10-12'), ('13-18', lambda r: r['dia'] >= '2026-10-13')):
    print('==', nom)
    for lo, hi in bins:
        g = [r for r in rows if sel(r) and lo <= r['m'] < hi]
        if not g: continue
        c = sum(r['c'] for r in g); pn = sum(r['pnl'] for r in g)
        print(f'  margen [{lo},{hi}): filas {len(g)} cierres {len({(r["dia"],r["mon"],r["cierre"]) for r in g})} gana {sum(r["g"] for r in g)/len(g):.3f} precio medio {st.mean(r["p"] for r in g):.3f} EV/€ {pn/c:+.3f} IC90 cierre {boot(g)}')
