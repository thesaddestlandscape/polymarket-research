#!/usr/bin/env python3
"""Analiza ledgers/informes de runs REALES de paquete_l (solo lectura). Uso: analiza_latencias.py RUN_DIR [RUN_DIR ...]
Une los runs y reporta n, p50/p90/p95/p99/max (+IC90 bootstrap de p50 y p90) de: ack de POST, RTT de DELETE, ack del DELETE (exchange),
jitter interno (disparo->envio), vida real vs hold, detección de relleno (push vs sondeo) y corte tras el push; todo por moneda y modo."""
import json, sys, os, random, collections

def pct(v, q):
    if not v: return None
    v = sorted(v); k = (len(v) - 1) * q; f = int(k); c = min(f + 1, len(v) - 1); return v[f] + (v[c] - v[f]) * (k - f)

def boot(v, q, B=2000, seed=7):
    if len(v) < 8: return None
    r = random.Random(seed); xs = sorted(pct([r.choice(v) for _ in v], q) for _ in range(B)); return (round(xs[int(B * .05)], 1), round(xs[int(B * .95)], 1))

def fila(nombre, v):
    if not v: return f'{nombre:<34} n=0'
    return (f'{nombre:<34} n={len(v):<4} p50={pct(v,.5):8.1f} p90={pct(v,.9):8.1f} p95={pct(v,.95):8.1f} p99={pct(v,.99):8.1f} max={max(v):8.1f}'
            f'  IC90 p50={boot(v,.5)} p90={boot(v,.9)}')

def cargar(d):
    return [json.loads(l) for l in open(os.path.join(d, 'ledger.jsonl')) if l.strip()]

def main(dirs):
    post_ack = collections.defaultdict(list); canc = collections.defaultdict(list); canc_ack = []; jit = []; trig_rx = []; vida = []; hold_err = []
    f_push = []; f_poll_menos_push = []; f_cut = []; cancel_tras_fill = []; fills = []; anclas = []; n_ord = 0; n_ok = 0
    for d in dirs:
        rows = cargar(d); inte = {r['clave']: r for r in rows if r['k'] == 'intencion'}; post = {r['clave']: r for r in rows if r['k'] == 'post'}
        for c, p in post.items():
            n_ord += 1; i = inte.get(c, {}); coin = i.get('coin', '?'); modo = i.get('modo', '?')
            if p.get('t_ack_ns') and p.get('t_send_ns'): post_ack[(coin, modo)].append((p['t_ack_ns'] - p['t_send_ns']) / 1e6)
            if i.get('t_decision_ns') and p.get('t_send_ns'): jit.append((p['t_send_ns'] - i['t_decision_ns']) / 1e6)
        for r in rows:
            if r['k'] != 'cancel': continue
            i = inte.get(r['clave'], {}); coin = i.get('coin', '?'); modo = i.get('modo', '?'); p = post.get(r['clave'], {})
            if r.get('ok') and r.get('t_ack_ns') and r.get('t_send_ns'):
                n_ok += 1; canc[(coin, modo)].append((r['t_ack_ns'] - r['t_send_ns']) / 1e6)
                if r.get('t_trig_rx_ns'): trig_rx.append((r['t_send_ns'] - r['t_trig_rx_ns']) / 1e6)
                if p.get('t_ack_ns'): vida.append((r['t_send_ns'] - p['t_ack_ns']) / 1e9)
                if i.get('hold_s') is not None and p.get('t_ack_ns'): hold_err.append(((r['t_send_ns'] - p['t_ack_ns']) / 1e9 - i['hold_s']) * 1000)
        by = collections.defaultdict(list)
        for r in rows: by[r.get('clave')].append(r)
        for c, rs in by.items():
            pf = [r for r in rs if r['k'] == 'push_fill']
            if not pf or c not in post: continue
            t0 = post[c]['t_send_ns']; i = inte.get(c, {}); t_push = min(r['t_ns'] for r in pf)
            polls = [r for r in rs if r['k'] == 'estado' and r.get('fuente') == 'poll_top' and (r.get('matched') or 0) > 0]
            tpoll = min((r['t_ns'] for r in polls), default=None); cs = [r for r in rs if r['k'] == 'cancel']
            f_push.append((t_push - t0) / 1e6)
            if tpoll: f_poll_menos_push.append((tpoll - t_push) / 1e6)
            if cs: cancel_tras_fill.append((min(x['t_send_ns'] for x in cs) - t_push) / 1e6)
            fills.append(dict(run=os.path.basename(d), clave=c[-6:], coin=i.get('coin'), size=max(r.get('size_matched') or 0 for r in rs if r['k'] == 'fill') if any(r['k'] == 'fill' for r in rs) else None,
                              push_ms=round((t_push - t0) / 1e6, 1), poll_menos_push_ms=round((tpoll - t_push) / 1e6, 1) if tpoll else None, hold_s=i.get('hold_s'), q_bid=(i.get('libro') or {}).get('q_bid')))
        try:
            f = json.load(open(os.path.join(d, 'informe_final.json'))); anclas.append((os.path.basename(d), f.get('anclas_detalle'), f.get('cobertura', {}).get('anclas_directas'), f.get('presupuesto')))
        except Exception: pass
    print(f'RUNS={len(dirs)}  ordenes={n_ord}  cancelaciones_ok={n_ok}  rellenos={len(fills)}\n')
    print('== ACK del POST (ms, cliente) por modo'); allp = []
    for (coin, modo), v in sorted(post_ack.items()): allp += v
    for modo in sorted({m for _, m in post_ack}): print(fila(f'POST ack [{modo}]', [x for (c, m), v in post_ack.items() if m == modo for x in v]))
    for (coin, modo), v in sorted(post_ack.items()): print(fila(f'  {coin}/{modo}', v))
    print('\n== RTT del DELETE (ms, cliente)'); print(fila('DELETE rtt [todas]', [x for v in canc.values() for x in v]))
    for modo in sorted({m for _, m in canc}): print(fila(f'DELETE rtt [{modo}]', [x for (c, m), v in canc.items() if m == modo for x in v]))
    for (coin, modo), v in sorted(canc.items()): print(fila(f'  {coin}/{modo}', v))
    print('\n== Jitter interno'); print(fila('decision->send POST (ms)', jit)); print(fila('trigger rx->send DELETE (ms)', trig_rx))
    print(fila('error del hold (vida-hold, ms)', hold_err)); print(fila('vida en libro (s)', vida))
    print('\n== Rellenos (fase B)'); print(fila('push canal usuario desde POST (ms)', f_push)); print(fila('sondeo menos push (ms; + = push antes)', f_poll_menos_push)); print(fila('envio DELETE menos push (ms)', cancel_tras_fill))
    for x in fills: print('  ', x)
    print('\n== Anclas del exchange (informe, por run; ms)')
    for nom, a, n, pr in anclas:
        print(f'  {nom}: anclas_directas={n}'); [print(f'     {k:<24}', {q: v.get(q) for q in ('n', 'p10', 'p50', 'p90')}) for k, v in (a or {}).items()]
        if pr: print('     presupuesto', {k: pr.get(k) for k in ('gasto', 'saldo_inicial', 'saldo_final')})

if __name__ == '__main__': main(sys.argv[1:])
