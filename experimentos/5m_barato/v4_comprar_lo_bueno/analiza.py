#!/usr/bin/env python3
"""Tablas del informe a partir de cron2_out.json (primeros) y cron2_out_todos.json. Solo lectura."""
import json, sys, statistics as st, collections, random, math
from datetime import datetime, timezone
S = sys.argv[1]
O = json.load(open(f'{S}/cron2_out.json'))
def fee(p): return 0.07 * p * (1 - p)
def q(v, p):
    v = sorted(x for x in v if x is not None)
    return None if not v else v[min(len(v) - 1, int(p * len(v)))]
def dist(v, nom):
    v = [x for x in v if x is not None]
    if not v: return f'{nom}: n=0'
    return f'{nom}: n={len(v)} P10/P25/P50/P75/P90 = ' + '/'.join(str(round(q(v, p))) for p in (.1, .25, .5, .75, .9)) + f' min={round(min(v))} max={round(max(v))}'
ex = [r for r in O if r.get('acc215', 0) > 0]
nx = [r for r in O if r.get('acc215', 0) <= 0 and r['cls215'] != 'UNKNOWN']
print('n eventos', len(O), 'ejecutables L215', len(ex), 'no ejecutables', len(nx))
print('con q5 y q15 en extracto:', sum(1 for r in O if r['n_q5'] and r['n_q15']))
for nom, g in (('TODAS', O), ('NO EJECUTABLES L215', nx), ('EJECUTABLES L215', ex)):
    print('\n==', nom, 'n=', len(g), 'win', sum(1 for r in g if r['gana']))
    print(' trigger:', dict(collections.Counter(r.get('trigger') for r in g)))
    print(' ', dist([r.get('feed_ms') for r in g], 'feed (t0 rx - exchange del trigger) ms'))
    print(' ', dist([r.get('cons_ex_trig_ms') for r in g], 'primera compra <=plim DESPUES del trigger, exchange - trig_ex ms'))
    print(' ', dist([r.get('cons_rx_t0_ms') for r in g], 'primera compra, rx - t0 ms'))
    print(' ', dist([r.get('gone_rx_t0_ms') for r in g], 'ask>plim (rx) - t0 ms'))
    print('  consumo ya en curso antes del trigger (cons_pre_n>0):', sum(1 for r in g if r.get('cons_pre_n', 0) > 0), '/', len(g))
    print('  hay compra posterior al trigger:', sum(1 for r in g if r.get('cons_ex_trig_ms') is not None), '/', len(g))

# ------------------------------------------------------------------ B. tipo de desaparición
def tipo_desaparicion(r):
    """Evidencia por trades del WS (side BUY, precio<=plim) entre el trigger y la q que saca el ask de la banda."""
    if r.get('gone_rx_t0_ms') is None: return 'NO_SALE_EN_VENTANA'
    sz, tr = r.get('sz_pre_gone') or 0, r.get('trades_sz_T_gone') or 0
    if r.get('trades_n_T_gone', 0) == 0: return 'CANCELA_O_RECOTIZA(sin trades)'
    if sz > 0 and tr >= 0.8 * sz: return 'CONSUMO_CONFIRMADO'
    return 'CONSUMO_PARCIAL+CANCELA'
print('\n=== B. tipo de desaparición del nivel <=plim (primera q que lo saca, rx>t0)')
for nom, g in (('NO EJECUTABLES', nx), ('EJECUTABLES', ex)):
    c = collections.Counter(tipo_desaparicion(r) for r in g)
    print(nom, dict(c))
    for t in c:
        gg = [r for r in g if tipo_desaparicion(r) == t]
        print('   ', t, 'n', len(gg), 'win', sum(1 for r in gg if r['gana']), dist([r.get('gone_rx_t0_ms') for r in gg], 'gone rx-t0'), '|', dist([r.get('gone_ex_trig_ms') for r in gg], 'gone ex-trig'))
# clase vigía vs mi tipo
print('clase vigía L215 x tipo (no ejecutables):', dict(collections.Counter((r['cls215'][:1], tipo_desaparicion(r)) for r in nx)))

# ------------------------------------------------------------------ C. ventana frente a nuestra llegada
print('\n=== C. margen de tiempo frente a NUESTRA llegada (ms, + = llegamos antes)')
FLOOR = 215  # ms desde t0 (rx) hasta casado, F1
for nom, g in (('NO EJECUTABLES', nx), ('EJECUTABLES', ex), ('TODAS', O)):
    m = [r['cons_rx_t0_ms'] - FLOOR for r in g if r.get('cons_rx_t0_ms') is not None]
    print(nom, dist(m, 'cons_rx_t0 - 215'), '| llegamos antes de la 1ª compra posterior:', sum(1 for x in m if x > 0), '/', len(m))
    m2 = [r['gone_rx_t0_ms'] - FLOOR for r in g if r.get('gone_rx_t0_ms') is not None]
    print('   ', dist(m2, 'gone_rx_t0 - 215'), '| ask sigue en banda a t0+215:', sum(1 for x in m2 if x > 0), '/', len(m2))

# ------------------------------------------------------------------ D. wallets
print('\n=== D. quién consumió (on-chain, tomador del casado que hizo la 1ª compra posterior al trigger)')
cw = collections.Counter(r['wallet'] for r in O if r.get('wallet'))
print('eventos con 1ª compra posterior:', sum(1 for r in O if r.get('cons_ex_trig_ms') is not None), '| con wallet on-chain:', sum(cw.values()), '| wallets distintas:', len(cw))
for w, n in cw.most_common(12):
    rs = [r for r in O if r.get('wallet') == w]
    print(' ', w[:12], n, 'monedas', dict(collections.Counter(r['moneda'] for r in rs)), 'ex-trig ms', sorted(r['cons_ex_trig_ms'] for r in rs))
NAMED = ['0x56f609c6', '0x29efa7c2', '0x9783f45c', '0xe38cc08b', '0x1df41c8f', '0x6515bf17', '0x32ed2e54']
for nm in NAMED:
    rs = [r for r in O if (r.get('wallet') or '').startswith(nm)]
    print('  named', nm, len(rs), [(r['dia'][5:], r['moneda'], r['cons_ex_trig_ms']) for r in rs])
# por día, quien: días
print(' por día (n con wallet):', dict(sorted(collections.Counter(r['dia'] for r in O if r.get('wallet')).items())))
# recurrencia: wallets con >=2
print(' wallets con >=2:', sum(1 for w, n in cw.items() if n >= 2), 'eventos cubiertos por ellas:', sum(n for w, n in cw.items() if n >= 2))

# ------------------------------------------------------------------ E. precursores
print('\n=== E. precursores (Binance E-clock vs trigger exchange; visibilidad para nosotros = E + ~140 ms)')
for nom, g in (('TODAS', O), ('NO EJEC', nx), ('EJEC', ex)):
    on = [r.get('binE_onset_vs_trig_ms') for r in g]
    nn = [x for x in on if x is not None]
    print(nom, 'n', len(g), 'con onset Binance >=1bp orientado en [-3s,+0.3s]:', len(nn), '| anterior al trigger (<0):', sum(1 for x in nn if x < 0),
          '| con >=255 ms de antelación (visible para nosotros >=115 ms antes del trigger):', sum(1 for x in nn if x <= -255), '| tras el trigger:', sum(1 for x in nn if x >= 0))
    print('   ', dist(nn, 'onset-trig'))
    for k in ('binE_R250', 'binE_R1000', 'binR_R1000'):
        v = [r.get(k) for r in g if r.get(k) is not None]
        print('   ', dist([x * 10 for x in v], k + ' x10 (bp*10)'), '| >=+1bp a favor:', sum(1 for x in v if x >= 1), '/', len(v), '| <=-1bp en contra:', sum(1 for x in v if x <= -1))
print('Binance DESPUES del trigger (binE_fwd500, oriented bp): ', dist([ (r.get('binE_fwd500') or 0)*10 for r in O if r.get('binE_fwd500') is not None], 'fwd500 x10'))
# grupo ganadoras vs perdedoras en binR_R1000
for nom, f in (('gana', lambda r: r['gana']), ('pierde', lambda r: not r['gana'])):
    v = [r.get('binR_R1000') for r in O if f(r) and r.get('binR_R1000') is not None]
    print(' ', nom, 'binR_R1000 (bp) media', round(st.mean(v), 3) if v else None, 'n', len(v), '| >=+0.5bp', sum(1 for x in v if x >= .5))

# ------------------------------------------------------------------ G. apertura / forzado por t_ini
print('\n=== G. señales forzadas por la regla de t_ini (condición ya vigente a C-300+1,5 s)')
for r in O:
    pass
fo = [r for r in O if r.get('t0_desde_apertura_ms') is not None and r['t0_desde_apertura_ms'] <= 1700]
print('n forzadas (t0-apertura <=1,7 s):', len(fo), 'win', sum(1 for r in fo if r['gana']), 'clases', dict(collections.Counter(r['cls215'][:1] for r in fo)))
for r in fo:
    print('  ', r['dia'][5:], r['moneda'], r['lado'], 'ask', r['ask0'], 'bid15', r['bid15_0'], 'start-open', r.get('start_desde_apertura_ms'), 'run_start-t0', r.get('run_start_vs_t0_ms'), 'cls', r['cls215'][:1], 'cons', r.get('cons_ex_trig_ms'), 'pre', r.get('cons_pre_n'), 'gana', r['gana'])
lat = [r for r in O if r.get('run_start_vs_t0_ms') is not None and r['run_start_vs_t0_ms'] < -150]
print('n con inicio latente de la condición >150 ms antes de t0:', len(lat), [(r['dia'][5:], r['moneda'], r['run_start_vs_t0_ms'], r.get('start_desde_apertura_ms')) for r in lat])

# ------------------------------------------------------------------ F. maker pre-posicionado (H23)
print('\n=== F. maker pre-posicionado (puja de compra puesta en t0-1 s, toque = relleno, SIN cola => cota optimista)')
def pnl_mk(r, k):
    f = r.get(k)
    if not f: return None
    p = f['precio']; w = 1.0 if r['gana'] else 0.0
    return (w - p) / p, p   # sin fee de maker; rendimiento por € 
for nom in ('join', 'mejora'):
    for W in (2000, 10000, 60000):
        k = f'mk_{nom}_{W}'
        rs = [(r, pnl_mk(r, k)) for r in O if r.get(k) is not None]
        n = len(O)
        if rs:
            c = sum(p[1] for _, p in rs); pn = sum((1.0 if r['gana'] else 0.0) - p[1] for r, p in rs)
            print(f'  {nom} W={W}: llena {len(rs)}/{n} ({len(rs)/n:.2f}); gana|llena {sum(1 for r,_ in rs if r["gana"])}/{len(rs)}; precio medio {st.mean(p[1] for _, p in rs):.3f}; PnL/acc {pn:.2f}; EV/€ {pn/c:+.3f}')
        else:
            print(f'  {nom} W={W}: llena 0/{n}')
print('  referencia: no llenas (ganan) vs llenas:')
for k in ('mk_join_10000', 'mk_mejora_10000'):
    a = [r for r in O if r.get(k)]; b = [r for r in O if not r.get(k)]
    print('   ', k, 'llena n', len(a), 'win', sum(1 for r in a if r['gana']), '| no llena n', len(b), 'win', sum(1 for r in b if r['gana']))
