#!/usr/bin/env python3
"""Verifica con on-chain la clasificación consumo/cancelación de los no ejecutables (el WS puede perder trades)."""
import json, sys, collections
S = sys.argv[1]
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
O = json.load(open(f'{S}/cron2_out.json'))
nx = [r for r in O if r.get('acc215', 0) <= 0 and r['cls215'] != 'UNKNOWN']
def tipo(r):
    if r.get('gone_rx_t0_ms') is None: return 'NO_SALE'
    if r.get('trades_n_T_gone', 0) == 0: return 'CANCELA'
    if (r.get('sz_pre_gone') or 0) > 0 and r.get('trades_sz_T_gone', 0) >= 0.8 * r['sz_pre_gone']: return 'CONSUMO'
    return 'PARCIAL'
out = collections.Counter()
for dia in sorted({r['dia'] for r in nx}):
    toks = json.load(open(f'{S}/toks_{dia}.json'))
    oc = [c for c in (ln.rstrip('\n').split(',') for ln in open(f'{S}/oc_{dia}.txt')) if c[0] == 'F' and len(c) >= 13 and c[7] == EXCH and c[8] == '0']
    for r in [x for x in nx if x['dia'] == dia]:
        k5 = toks[r['event_id']][0]
        hits = []
        for c in oc:
            if c[9] != k5: continue
            ts = float(c[2])
            if not (r['t0'] / 1000 - 1.0 <= ts <= r['t0'] / 1000 + 6.0): continue
            try: pr = float(c[10]) / float(c[11])
            except Exception: continue
            if pr <= r['plim'] + 0.011: hits.append((round(ts - r['t0'] / 1000, 1), round(pr, 3), round(float(c[11]), 1), c[6][:8]))
        t = tipo(r)
        out[(t, bool(hits))] += 1
        if t == 'CANCELA' and hits: print('CANCELA(WS) pero hay fill on-chain:', r['dia'], r['moneda'], r['event_id'][-12:], hits[:4], 'ask0', r['ask0'], 'plim', r['plim'], 'gone', r['gone_rx_t0_ms'])
print(dict(out))
