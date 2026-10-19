#!/usr/bin/env python3
"""Tablas finales: pareado por latencia, ventaja del competidor, wallets de los no ejecutables, CSV de cronología con IDs exactos."""
import json, sys, csv, glob, collections, statistics as st, random
from datetime import datetime, timezone
S = sys.argv[1]; OUTCSV = sys.argv[2]
D = '/root/polymarket-research-datalogs/'
O = json.load(open(f'{S}/cron2_out.json'))
des = json.load(open(D + 'maker_ms_desenlaces_cache.json'))
EV = {}
for f in sorted(glob.glob(D + 'vigia_5m_barato/eventos_*.csv')):
    for e in csv.DictReader(open(f)): EV[e['event_id']] = e
def fee(p): return 0.07 * p * (1 - p)
def q(v, p):
    v = sorted(x for x in v if x is not None); return None if not v else v[min(len(v) - 1, int(p * len(v)))]
def d(v):
    v = [x for x in v if x is not None]; return 'n=0' if not v else f'n={len(v)} P10/25/50/75/90=' + '/'.join(str(round(q(v, p))) for p in (.1, .25, .5, .75, .9))
for r in O:
    r['hueco'] = (r.get('gap_prev_q5_ms') or 0) > 60000 or (r.get('gap_prev_q15_ms') or 0) > 60000
    r['ej'] = r['acc215'] > 0
def tipo(r):
    if r.get('gone_rx_t0_ms') is None: return 'NO_SALE'
    if r.get('trades_n_T_gone', 0) == 0: return 'CANCELA'
    if (r.get('sz_pre_gone') or 0) > 0 and r.get('trades_sz_T_gone', 0) >= 0.8 * r['sz_pre_gone']: return 'CONSUMO'
    return 'PARCIAL'
# ---- pareado por latencia
print('== PAREADO por latencia (58 señales; PnL total en €, unidad = señal, stake oficial 2 €/5 acc mín)')
def pn(e, L):
    acc = float(e.get(f'L{L}_acciones') or 0)
    if acc <= 0 or e.get(f'L{L}_precio') in ('', 'None', None): return None
    p = float(e[f'L{L}_precio']); g = (des[e['market_compra']] == 'YES') == (e['lado'] == 'Up')
    return acc * ((1.0 if g else 0) - p - fee(p)), acc * (p + fee(p)), g
base = {r['event_id']: pn(EV[r['event_id']], 215) for r in O}
for L in (150, 175, 200, 225, 250):
    cur = {r['event_id']: pn(EV[r['event_id']], L) for r in O}
    both = [k for k in base if base[k] and cur[k]]; only_fast = [k for k in cur if cur[k] and not base[k]]; only_215 = [k for k in base if base[k] and not cur[k]]
    f = lambda ks, dct: (round(sum(dct[k][0] for k in ks), 2), len(ks), sum(1 for k in ks if dct[k][2]))
    print(f'  L{L}: comunes con L215 {len(both)} (PnL a L{L} {f(both, cur)[0]} vs a L215 {f(both, base)[0]}) | solo a L{L}: n {len(only_fast)} gana {f(only_fast, cur)[2]} PnL {f(only_fast, cur)[0]} | solo a L215: n {len(only_215)} gana {f(only_215, base)[2]} PnL {f(only_215, base)[0]}')
# ---- headline sin huecos
ex = [r for r in O if r['ej']]
tot = sum(base[r['event_id']][0] for r in ex); c = sum(base[r['event_id']][1] for r in ex)
exs = [r for r in ex if not r['hueco']]
tots = sum(base[r['event_id']][0] for r in exs); cs = sum(base[r['event_id']][1] for r in exs)
print(f'\nV4 L215 todas: n {len(ex)} PnL {tot:.2f} coste {c:.2f} EV {tot/c:.3f} | sin los 5 huecos de feed: n {len(exs)} PnL {tots:.2f} coste {cs:.2f} EV {tots/cs:.3f}')
byd = collections.defaultdict(float)
for r in exs: byd[datetime.fromtimestamp(r['cierre'], timezone.utc).date().isoformat()] += base[r['event_id']][0]
print('  sin huecos: sin la mejor operación', round((tots - max(base[r["event_id"]][0] for r in exs)) / (cs - [base[r["event_id"]][1] for r in exs if base[r["event_id"]][0] == max(base[x["event_id"]][0] for x in exs)][0]), 3))
# ---- ventaja del competidor (exchange): our_match = trig_ex + feed + 215 ; their = cons_ex / gone_ex
print('\n== Ventaja del competidor sobre NUESTRO casado a L215 (ms; + = nos ganan por esos ms), reloj exchange: feed_ms+215 - t_evento_ex_desde_trigger')
for nom, f in (('CONSUMO', lambda r: tipo(r) == 'CONSUMO'), ('CANCELA/RECOTIZA', lambda r: tipo(r) == 'CANCELA')):
    g = [r for r in O if not r['ej'] and r['cls215'] != 'UNKNOWN' and not r['hueco'] and f(r)]
    vals = [(r['feed_ms'] + 215 - r['gone_ex_trig_ms']) for r in g]
    print(f'  {nom}: {d(vals)}  | nos ganan por >0 ms: {sum(1 for v in vals if v > 0)}/{len(vals)}; por >=100 ms: {sum(1 for v in vals if v >= 100)}; por >=200: {sum(1 for v in vals if v >= 200)}')
# ---- wallets en no ejecutables
print('\n== wallets que consumen (no ejecutables, sin huecos, con compra posterior al trigger)')
nxw = [r for r in O if not r['ej'] and not r['hueco'] and r.get('wallet')]
print('  eventos', len(nxw), 'wallets', len({r['wallet'] for r in nxw}), collections.Counter(r['wallet'][:10] for r in nxw).most_common(6))
# ---- CSV
campos = ['event_id', 'dia', 'moneda', 'lado', 'market_5m', 'market_15m', 'token_5m_s', 'token_15m_s', 't_trigger_exchange_ms', 't0_recepcion_ms', 'feed_ms', 'trigger', 'ask0', 'bid15_0', 'p_limite', 'resto_s',
          'cls150', 'cls215', 'cls250', 'gana', 'hueco_feed', 'barrido_previo_3s', 'tipo_desaparicion', 'gone_ex_tras_trigger_ms', 'gone_rx_tras_t0_ms', 'primera_compra_ex_tras_trigger_ms', 'primera_compra_rx_tras_t0_ms',
          'wallet_tomador', 'tx', 'precio_onchain', 'acc_onchain', 'bloque_ts_s', 'binE_onset_vs_trigger_ms', 'binR_R1000_bp_orientado']
toks_all = {}
for f in glob.glob(f'{S}/toks_*.json'): toks_all.update(json.load(open(f)))
with open(OUTCSV, 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(campos)
    for r in sorted(O, key=lambda r: r['t0']):
        e = EV[r['event_id']]; k5, k15 = toks_all[r['event_id']]
        w.writerow([r['event_id'], r['dia'], r['moneda'], r['lado'], e['market_compra'], e['market_otro'], k5, k15, r['t_trig_ex'], r['t0'], r['feed_ms'], r['trigger'], r['ask0'], r['bid15_0'], r['plim'], r['resto'],
                    r['cls150'], r['cls215'], r['cls250'], int(r['gana']), int(r['hueco']), r['cons_pre_n'], tipo(r), r.get('gone_ex_trig_ms'), r.get('gone_rx_t0_ms'), r.get('cons_ex_trig_ms'), r.get('cons_rx_t0_ms'),
                    r.get('wallet'), r.get('w_tx'), r.get('w_precio'), r.get('w_acc'), r.get('w_block_ts'), r.get('binE_onset_vs_trig_ms'), r.get('binR_R1000')])
print('CSV escrito', OUTCSV, len(O))
