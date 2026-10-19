#!/usr/bin/env python3
"""Candidata post hoc: actuar solo en el 2º evento (primer re-arm) de cada (cierre, moneda). Descriptivo sobre eventos del vigía V4 (95 eventos OOS)."""
import csv, glob, json, collections, random, statistics as st
from datetime import datetime, timezone
D = '/root/polymarket-research-datalogs/'
des = json.load(open(D + 'maker_ms_desenlaces_cache.json'))
cong = int(datetime.fromisoformat('2026-10-06T12:00:00+00:00').timestamp() * 1000)
def fee(p): return 0.07 * p * (1 - p)
E = []
for f in sorted(glob.glob(D + 'vigia_5m_barato/eventos_*.csv')): E += list(csv.DictReader(open(f)))
allB = [e for e in E if e['regla'] == 'B1_5m' and int(e['t_deteccion']) >= cong and e['market_compra'] in des]
def gana(e): return (des[e['market_compra']] == 'YES') == (e['lado'] == 'Up')
by = collections.defaultdict(list)
for e in allB: by[(e['moneda'], e['cierre'])].append(e)
rows = []
for k, v in by.items():
    v = sorted(v, key=lambda e: int(e['t_deteccion']))
    if len(v) > 1: rows.append((k, v[0], v[1]))
print('mercados con >=2 eventos:', len(rows), 'de', len(by), 'mercados con evento')
def pn(e, L):
    acc = float(e.get(f'L{L}_acciones') or 0)
    if acc <= 0: return None
    p = float(e[f'L{L}_precio']); return acc * ((1.0 if gana(e) else 0) - p - fee(p)), acc * (p + fee(p))
for L in (215, 150, 250):
    xs = [(k, b, pn(b, L)) for k, a, b in rows if pn(b, L)]
    pnl = sum(x[2][0] for x in xs); c = sum(x[2][1] for x in xs)
    print(f'L{L}: ejecutables {len(xs)} win {sum(gana(x[1]) for x in xs)} PnL {pnl:.2f} coste {c:.2f} EV {pnl/c:.3f}')
    if L == 215:
        for k, b, p in sorted(xs, key=lambda x: -x[2][0]):
            print('    ', k[0], datetime.fromtimestamp(int(k[1]), timezone.utc).strftime('%m-%d %H:%M'), b['lado'], 'ask', b['L215_precio'], 'acc', b['L215_acciones'], 'gana', gana(b), 'pnl', round(p[0], 2), 'resto', b['resto_s'])
        w = sorted(xs, key=lambda x: -x[2][0])
        print('    sin la mejor:', round(sum(x[2][0] for x in w[1:]) / sum(x[2][1] for x in w[1:]), 3), '| sin 2 mejores:', round(sum(x[2][0] for x in w[2:]) / sum(x[2][1] for x in w[2:]), 3))
        dias = collections.defaultdict(float)
        for k, b, p in xs: dias[datetime.fromtimestamp(int(k[1]), timezone.utc).date().isoformat()] += p[0]
        print('    días:', len(dias), dict(dias))
# comparación: primer evento de esos mismos mercados
xs1 = [(k, a, pn(a, 215)) for k, a, b in rows if pn(a, 215)]
print('primer evento de esos mismos mercados, L215 ejecutables', len(xs1), 'win', sum(gana(x[1]) for x in xs1), 'PnL', round(sum(x[2][0] for x in xs1), 2))
# papel: ganan el 2º evento en 12/15; test binomial contra precio
p2 = [float(b['ask_compra_t0']) for k, a, b in rows]
import math
from math import comb
n = len(rows); w = sum(gana(b) for k, a, b in rows)
mu = sum(p2)
# P(X>=w) bajo Poisson-binomial con p=ask
dist = [1.0]
for p in p2:
    nd = [0.0] * (len(dist) + 1)
    for i, q in enumerate(dist): nd[i] += q * (1 - p); nd[i + 1] += q * p
    dist = nd
print('2º evento: win', w, '/', n, 'esperado bajo acierto=precio', round(mu, 2), 'P(X>=w)=', round(sum(dist[w:]), 4))
