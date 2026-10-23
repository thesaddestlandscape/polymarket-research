#!/usr/bin/env python3
"""c4_fetch_calldata.py -- descarga (JSON-RPC publico de Polygon, SOLO LECTURA eth_getTransactionByHash via polygon_rpc.llamar, sin claves) el input de las
txs on-chain donde B es maker (para leer el `timestamp` firmado de cada orden maker/taker de matchOrders). Cache: DL/cola_posicion/calldata_b.jsonl (reanudable)."""
import sys, json, time, os
sys.path.insert(0, '/root/polymarket-research')
from polygon_rpc import llamar
import pandas as pd
DL = '/root/polymarket-research-datalogs/cola_posicion/'
txs = sorted(set(pd.read_csv(DL + 'b_tx_all.csv', usecols=['tx']).tx))
hechas = set()
if os.path.exists(DL + 'calldata_b.jsonl'):
    for l in open(DL + 'calldata_b.jsonl'): hechas.add(json.loads(l)['tx'])
n = 0
with open(DL + 'calldata_b.jsonl', 'a') as o:
    for tx in txs:
        if tx in hechas: continue
        try:
            r = llamar("eth_getTransactionByHash", [tx], grupo="archivo", plazo_total_s=30)
        except Exception as e:
            print('fallo', tx[:12], type(e).__name__, str(e)[:100], flush=True); time.sleep(2); continue
        if not isinstance(r, dict): print('vacio', tx[:12], flush=True); continue
        o.write(json.dumps(dict(tx=tx, to=r.get('to'), frm=r.get('from'), block=int(r['blockNumber'], 16), input=r['input'])) + '\n'); o.flush(); n += 1
        time.sleep(0.15)
print('descargadas', n, 'ya', len(hechas), 'total txs', len(txs))
