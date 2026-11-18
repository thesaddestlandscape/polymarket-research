#!/usr/bin/env python3
"""v5_fetch_dem.py -- SOLO LECTURA: eth_getTransactionByHash (polygon_rpc.llamar, RPC publico, sin claves) de out/needed_*.txt -> calldata_dem.jsonl
(reanudable, idempotente: salta lo ya cacheado). 3 hilos, pausa 0,2 s por llamada."""
import sys, json, os, glob, time, threading
sys.path.insert(0, '/root/polymarket-research'); from polygon_rpc import llamar
from concurrent.futures import ThreadPoolExecutor
H = os.path.dirname(os.path.abspath(__file__)) + '/'; C = H + 'calldata_dem.jsonl'
have = set(json.loads(l)['tx'] for l in open(C)) if os.path.exists(C) else set()
todo = sorted({l.strip() for f in glob.glob(H + 'out/needed_*.txt') for l in open(f) if l.strip()} - have); print('pendientes', len(todo), flush=True)
lk = threading.Lock(); n = [0, 0]
o = open(C, 'a')
def one(tx):
    for i in range(3):
        try:
            r = llamar("eth_getTransactionByHash", [tx], grupo="archivo", plazo_total_s=30)
            with lk: o.write(json.dumps(dict(tx=tx, input=r['input'])) + '\n'); o.flush(); n[0] += 1
            time.sleep(0.2); return
        except Exception as e: time.sleep(2 + 3 * i)
    with lk: n[1] += 1
with ThreadPoolExecutor(3) as ex:
    for i, _ in enumerate(ex.map(one, todo)):
        if i % 500 == 0: print(i, 'ok', n[0], 'fallos', n[1], time.strftime('%H:%M:%S'), flush=True)
print('fin ok', n[0], 'fallos', n[1], flush=True)
