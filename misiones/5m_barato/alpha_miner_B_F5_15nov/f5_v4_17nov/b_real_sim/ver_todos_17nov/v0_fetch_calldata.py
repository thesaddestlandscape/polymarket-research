#!/usr/bin/env python3
"""v0_fetch_calldata.py (ver_todos_17nov) -- SOLO LECTURA: eth_getTransactionByHash via polygon_rpc.llamar (RPC publico, sin claves) de las txs
de rellenos reales de B (inventario2.pkl, 20-23 Oct) que faltan en la cache de cola_posicion. Cache propia calldata_extra.jsonl (reanudable, idempotente)."""
import sys, json, os, time
sys.path.insert(0, '/root/polymarket-research'); from polygon_rpc import llamar
import pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
X = pd.read_pickle('/root/polymarket-research/experimentos/5m_barato/replay_brecha_B_16nov/fn_16nov/inventario2.pkl')
have = set(json.loads(l)['tx'] for l in open('/root/polymarket-research-datalogs/cola_posicion/calldata_b.jsonl'))
if os.path.exists(H + 'calldata_extra.jsonl'): have |= set(json.loads(l)['tx'] for l in open(H + 'calldata_extra.jsonl'))
falta = sorted(set(X.tx) - have); print('faltan', len(falta), flush=True)
with open(H + 'calldata_extra.jsonl', 'a') as o:
    for tx in falta:
        try: r = llamar("eth_getTransactionByHash", [tx], grupo="archivo", plazo_total_s=30)
        except Exception as e: print('fallo', tx[:12], type(e).__name__, str(e)[:80], flush=True); time.sleep(2); continue
        o.write(json.dumps(dict(tx=tx, input=r['input'], blockNumber=r.get('blockNumber'))) + '\n'); o.flush(); time.sleep(0.3)
print('ok', flush=True)
