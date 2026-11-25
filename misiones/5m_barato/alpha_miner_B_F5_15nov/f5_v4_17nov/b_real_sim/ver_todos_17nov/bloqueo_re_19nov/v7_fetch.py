"""v7_fetch.py -- SOLO LECTURA: eth_getTransactionByHash via polygon_rpc.llamar (RPC publico, sin claves) de las txs de out/v7_cand.csv.
Cache out/calldata_v7.jsonl (reanudable, idempotente; reutiliza calldata_b.jsonl y ../calldata_extra.jsonl). Ritmo 0,35 s/tx."""
import sys, json, os, time, csv
sys.path.insert(0, '/root/polymarket-research'); from polygon_rpc import llamar
H = os.path.dirname(os.path.abspath(__file__)) + '/'; C = H + 'out/calldata_v7.jsonl'
have = set()
for f in ('/root/polymarket-research-datalogs/cola_posicion/calldata_b.jsonl', H + '../calldata_extra.jsonl', C):
    if os.path.exists(f):
        for l in open(f):
            try: have.add(json.loads(l)['tx'])
            except Exception: pass
txs = []; seen = set()
for r in csv.DictReader(open(H + 'out/v7_cand.csv')):
    if r['tx'] not in seen: seen.add(r['tx']); txs.append((float(r['ts']), r['tx']))
txs.sort(); falta = [t for _, t in txs if t not in have]
print('total', len(seen), 'ya', len(seen) - len(falta), 'faltan', len(falta), flush=True)
ok = fl = 0; t0 = time.time()
with open(C, 'a') as o:
    for i, tx in enumerate(falta):
        try: r = llamar("eth_getTransactionByHash", [tx], grupo="archivo", plazo_total_s=30)
        except Exception as e:
            fl += 1; print('fallo', tx[:12], type(e).__name__, str(e)[:80], flush=True); time.sleep(3); continue
        if not r or 'input' not in r: fl += 1; continue
        o.write(json.dumps(dict(tx=tx, input=r['input'], blockNumber=r.get('blockNumber'))) + '\n'); o.flush(); ok += 1
        if (i + 1) % 200 == 0: print(f'{i+1}/{len(falta)} ok {ok} fallos {fl} {(time.time()-t0)/(i+1):.2f} s/tx', flush=True)
        time.sleep(0.35)
print('FIN ok', ok, 'fallos', fl, flush=True)
