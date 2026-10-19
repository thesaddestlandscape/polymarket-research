#!/usr/bin/env python3
import json, sys, statistics as st, collections
S = sys.argv[1]
O = json.load(open(f'{S}/cron2_out.json'))
OK = json.load(open(f'{S}/ws_ok.json'))
for r in O:
    r['hueco'] = (r.get('gap_prev_q5_ms') or 0) > 60000 or (r.get('gap_prev_q15_ms') or 0) > 60000
    r['ws_ok'] = OK.get(r['event_id'], True)
    r['ej'] = r.get('acc215', 0) > 0
def q(v, p):
    v = sorted(x for x in v if x is not None); return None if not v else v[min(len(v) - 1, int(p * len(v)))]
def d(v):
    v = [x for x in v if x is not None]
    return 'n=0' if not v else f'n={len(v)} P10/25/50/75/90=' + '/'.join(str(round(q(v, p))) for p in (.1, .25, .5, .75, .9))
print('hueco de feed (>60 s sin q en una pata antes de t0):', sum(r['hueco'] for r in O), [ (r['event_id'][-18:], r['cls215'][0], r['gana']) for r in O if r['hueco']])
print('  entre ejecutables:', sum(1 for r in O if r['hueco'] and r['ej']), '(ganan', sum(1 for r in O if r['hueco'] and r['ej'] and r['gana']), ') entre no ejecutables:', sum(1 for r in O if r['hueco'] and not r['ej']), '(ganan', sum(1 for r in O if r['hueco'] and not r['ej'] and r['gana']), ')')
sin = [r for r in O if not r['hueco']]
nx = [r for r in sin if not r['ej'] and r['cls215'] != 'UNKNOWN']; ex = [r for r in sin if r['ej']]
print('SIN huecos: n', len(sin), 'win', sum(r['gana'] for r in sin), 'ejec', len(ex), 'win', sum(r['gana'] for r in ex), 'noejec', len(nx), 'win', sum(r['gana'] for r in nx))
# Fisher
from math import comb
def fisher(a, b, c, dd):
    N = a + b + c + dd
    def h(x): return comb(a + b, x) * comb(c + dd, a + c - x) / comb(N, a + c)
    p0 = h(a); return sum(h(x) for x in range(max(0, a + c - (c + dd)), min(a + b, a + c) + 1) if h(x) <= p0 + 1e-12)
a, b, c, dd = sum(r['gana'] for r in ex), len(ex) - sum(r['gana'] for r in ex), sum(r['gana'] for r in nx), len(nx) - sum(r['gana'] for r in nx)
print('Fisher sin huecos:', round(fisher(a, b, c, dd), 4), f'ejec {a}/{a+b} vs noejec {c}/{c+dd}')

print('\n--- tiempos del consumo en no ejecutables con consumo confirmado (sin huecos)')
def tipo(r):
    if r.get('gone_rx_t0_ms') is None: return 'NO_SALE'
    if r.get('trades_n_T_gone', 0) == 0: return 'CANCELA'
    if (r.get('sz_pre_gone') or 0) > 0 and r.get('trades_sz_T_gone', 0) >= 0.8 * r['sz_pre_gone']: return 'CONSUMO'
    return 'PARCIAL'
cons = [r for r in nx if tipo(r) == 'CONSUMO']; canc = [r for r in nx if tipo(r) == 'CANCELA']; par = [r for r in nx if tipo(r) == 'PARCIAL']
print('nx', len(nx), 'CONSUMO', len(cons), 'win', sum(r['gana'] for r in cons), '| CANCELA', len(canc), 'win', sum(r['gana'] for r in canc), '| PARCIAL', len(par))
print('CONSUMO: gone ex - trig (ms)', d([r['gone_ex_trig_ms'] for r in cons]))
print('CONSUMO: gone rx - t0   (ms)', d([r['gone_rx_t0_ms'] for r in cons]))
for thr in (100, 145, 175, 200, 215):
    print(f'  consumo (gone) a <{thr} ms del trigger [exchange]:', sum(1 for r in cons if r['gone_ex_trig_ms'] < thr), '/', len(cons), '| [rx]:', sum(1 for r in cons if r['gone_rx_t0_ms'] < thr), '/', len(cons))
print('CANCELA: gone ex - trig (ms)', d([r['gone_ex_trig_ms'] for r in canc]))
print('CANCELA: gone rx - t0   (ms)', d([r['gone_rx_t0_ms'] for r in canc]))
for thr in (100, 145, 175, 200, 215):
    print(f'  cancel/reprice a <{thr} ms del trigger [exchange]:', sum(1 for r in canc if r['gone_ex_trig_ms'] < thr), '/', len(canc), '| [rx]:', sum(1 for r in canc if r['gone_rx_t0_ms'] < thr), '/', len(canc))
print('gone ex<0 (el nivel se fue ANTES del trigger según sello exchange):', sum(1 for r in canc + cons if r['gone_ex_trig_ms'] < 0))
# barrido previo
pre = [r for r in nx if r.get('cons_pre_n', 0) > 0]; nopre = [r for r in nx if r.get('cons_pre_n', 0) == 0]
print('\nno ejecutables con barrido previo (>=1 compra <=plim en los 3 s antes del trigger):', len(pre), 'win', sum(r['gana'] for r in pre), '| sin barrido previo', len(nopre), 'win', sum(r['gana'] for r in nopre))
print('  con barrido previo, tipo:', dict(collections.Counter(tipo(r) for r in pre)), '| sin:', dict(collections.Counter(tipo(r) for r in nopre)))
print('  sin barrido previo y CONSUMO: ex-trig', d([r['cons_ex_trig_ms'] for r in nopre if tipo(r) == 'CONSUMO']))
print('  con  barrido previo y CONSUMO: ex-trig', d([r['cons_ex_trig_ms'] for r in pre if tipo(r) == 'CONSUMO']))
# tipo de trigger
for t in ('15m_bid', '5m_ask', 'otro'):
    g = [r for r in nx if r['trigger'] == t]; ge = [r for r in ex if r['trigger'] == t]
    print('trigger', t, 'noejec', len(g), 'win', sum(r['gana'] for r in g), 'cons', sum(1 for r in g if tipo(r) == 'CONSUMO'), 'cancela', sum(1 for r in g if tipo(r) == 'CANCELA'), '| ejec', len(ge), 'win', sum(r['gana'] for r in ge))
# bid15 despues del trigger: ¿el bid15 sigue ahí a +215?
print('\nbid15 en t0+215 vs bid15_0:', 'cae' , sum(1 for r in nx if r.get('bid15_p215') is not None and r['bid15_p215'] < r['bid15_0'] - 0.0001), 'igual', sum(1 for r in nx if r.get('bid15_p215') is not None and abs(r['bid15_p215'] - r['bid15_0']) < 1e-4), 'sube', sum(1 for r in nx if r.get('bid15_p215') is not None and r['bid15_p215'] > r['bid15_0'] + 1e-4))
print('   ejec: cae', sum(1 for r in ex if r.get('bid15_p215') is not None and r['bid15_p215'] < r['bid15_0'] - 0.0001), 'igual', sum(1 for r in ex if r.get('bid15_p215') is not None and abs(r['bid15_p215'] - r['bid15_0']) < 1e-4), 'sube', sum(1 for r in ex if r.get('bid15_p215') is not None and r['bid15_p215'] > r['bid15_0'] + 1e-4))
# ganadoras: pérdida de valor
# tamaño del nivel
print('\ntamaño nivel 1 a t0 (acciones) no ejec:', d([r['ask0_sz'] for r in nx]), '| ejec:', d([r['ask0_sz'] for r in ex]))
print('nocional nivel 1 $ no ejec:', d([r['ask0_sz'] * r['ask0'] for r in nx if r.get('ask0_sz') is not None]), '| ejec:', d([r['ask0_sz'] * r['ask0'] for r in ex if r.get('ask0_sz') is not None]))
