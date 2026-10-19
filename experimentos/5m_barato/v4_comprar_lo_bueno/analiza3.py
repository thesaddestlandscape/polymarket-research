#!/usr/bin/env python3
"""Mecanismo 'bid15 transitorio' y rasgos pre-decisión. Exploratorio, post hoc."""
import json, sys, csv, glob, statistics as st, collections, random
S = sys.argv[1]
O = json.load(open(f'{S}/cron2_out.json'))
D = '/root/polymarket-research-datalogs/'
ev = {}
for f in sorted(glob.glob(D + 'vigia_5m_barato/eventos_*.csv')):
    for e in csv.DictReader(open(f)): ev[e['event_id']] = e
for r in O:
    r['hueco'] = (r.get('gap_prev_q5_ms') or 0) > 60000 or (r.get('gap_prev_q15_ms') or 0) > 60000
    r['ej'] = r.get('acc215', 0) > 0
    e = ev[r['event_id']]
    def f(k):
        v = e.get(k); return None if v in (None, '', 'None') else float(v)
    r['o_bid_sz'] = f('o_bid_sz'); r['o_spread'] = f('o_spread'); r['c_spread'] = f('c_spread'); r['c_edad_ask'] = f('c_edad_ask_ms'); r['o_cambios_1s'] = f('o_cambios_1s'); r['c_cambios_1s'] = f('c_cambios_1s')
    r['c_trades_1s'] = f('c_trades_1s'); r['o_trades_1s'] = f('o_trades_1s'); r['c_cancel_1s'] = f('c_cancel_1s'); r['margen'] = f('margen_neto'); r['c_ask_sz'] = f('c_ask_sz'); r['c_bid_sz'] = f('c_bid_sz')
    r['jump15'] = None if r.get('bid15_prev') is None else round(r['bid15_0'] - r['bid15_prev'], 3)
    r['persist215'] = None if r.get('bid15_p215') is None else (r['bid15_p215'] >= r['bid15_0'] - 0.015)
    r['persist1000'] = None if r.get('bid15_p1000') is None else (r['bid15_p1000'] >= r['bid15_0'] - 0.015)
S1 = [r for r in O if not r['hueco']]
print('n sin huecos', len(S1))
def wr(g): return f'{sum(r["gana"] for r in g)}/{len(g)}'
for nom, g in (('ejec', [r for r in S1 if r['ej']]), ('noejec', [r for r in S1 if not r['ej'] and r['cls215'] != 'UNKNOWN'])):
    for k in (True, False):
        gg = [r for r in g if r['persist215'] is k]
        print(nom, 'bid15 persiste a +215 (>= bid0-1c):', k, 'n', len(gg), 'gana', wr(gg))
for k in (True, False):
    gg = [r for r in S1 if r['persist1000'] is k]; print('todas, bid15 persiste a +1000:', k, len(gg), wr(gg))
# AUC de rasgos pre-decisión
def auc(pos, neg):
    if not pos or not neg: return None
    c = 0.0
    for a in pos:
        for b in neg: c += 1.0 if a > b else 0.5 if a == b else 0.0
    return c / (len(pos) * len(neg))
def boot_auc(pos, neg, n=2000, seed=7):
    rng = random.Random(seed); v = []
    for _ in range(n):
        p = [rng.choice(pos) for _ in pos]; q = [rng.choice(neg) for _ in neg]; v.append(auc(p, q))
    v.sort(); return round(v[int(.05 * n)], 2), round(v[int(.95 * n)], 2)
feats = ['jump15', 'o_bid_sz', 'o_spread', 'c_spread', 'c_edad_ask', 'o_cambios_1s', 'c_cambios_1s', 'c_trades_1s', 'o_trades_1s', 'c_cancel_1s', 'margen', 'c_ask_sz', 'c_bid_sz', 'ask0', 'bid15_0', 'resto', 'binR_R1000', 'binR_R250', 'edad_bid15_prev', 'n_bid15_chg_1000']
print('\nAUC rasgo -> GANA (pos = gana). Sin huecos. IC90 bootstrap')
for nom, g in (('todas', S1), ('ejecutables', [r for r in S1 if r['ej']])):
    print('==', nom, len(g), 'win', wr(g))
    for k in feats:
        pos = [r[k] for r in g if r['gana'] and r.get(k) is not None]; neg = [r[k] for r in g if not r['gana'] and r.get(k) is not None]
        a = auc(pos, neg)
        if a is not None: print(f'   {k:18s} AUC {a:.2f} IC90 {boot_auc(pos, neg)}  n {len(pos)}+{len(neg)}')
print('\nAUC rasgo -> NO EJECUTABLE (pos = noejec), sin huecos')
for k in feats:
    pos = [r[k] for r in S1 if (not r['ej']) and r.get(k) is not None]; neg = [r[k] for r in S1 if r['ej'] and r.get(k) is not None]
    a = auc(pos, neg)
    if a is not None: print(f'   {k:18s} AUC {a:.2f} IC90 {boot_auc(pos, neg)}  n {len(pos)}+{len(neg)}')
