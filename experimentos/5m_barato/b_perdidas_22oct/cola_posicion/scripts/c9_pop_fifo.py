#!/usr/bin/env python3
"""c9_pop_fifo.py -- PREREG_COLA (sha a72007c5...). Valida a gran escala que el orden de log_index dentro de un nivel = orden de llegada: para una muestra aleatoria (semilla 20261022,
500) de txs de poblacion con >=2 makers del mismo nivel (20-22 Oct), descarga la calldata de matchOrders (RPC publico, solo lectura), decodifica el `timestamp` firmado de cada orden
maker y cuenta, entre pares del mismo nivel y de wallets distintas, cuantas veces el que se rellena DESPUES firmo ANTES (inversion), con margenes de 250 ms y 1 s.
Salida datos/pop_fifo.txt, datos/pop_ts_pares.csv."""
import sys, os, json, time, glob, hashlib, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research'); from polygon_rpc import llamar
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_posicion/'; SRC = os.path.join(AQ, '..', '..', 'cola_vs_cruce', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_COLA.md'), 'rb').read()).hexdigest().startswith('a72007c5deecc5e7')
EX = '0xe111180000d2663c0091e4f400237545b87b996b'; EPS = 0.0005
txs = list(pd.read_csv(DL + 'pop_tx_muestra.csv').tx); hechas = {}
cf = DL + 'pop_calldata.jsonl'
if os.path.exists(cf):
    for l in open(cf): d = json.loads(l); hechas[d['tx']] = d['input']
with open(cf, 'a') as o:
    for tx in txs:
        if tx in hechas: continue
        try: r = llamar("eth_getTransactionByHash", [tx], grupo="archivo", plazo_total_s=30)
        except Exception as e: print('fallo', tx[:10], type(e).__name__, flush=True); time.sleep(2); continue
        if isinstance(r, dict): hechas[tx] = r['input']; o.write(json.dumps(dict(tx=tx, input=r['input'])) + '\n'); o.flush(); time.sleep(0.15)
print('calldata', len(hechas), '/', len(txs), flush=True)
# filas on-chain de esas txs (oc_D) con token id
F = []
for d in ('2026-10-20', '2026-10-21', '2026-10-22'):
    T = pd.read_csv(os.path.join(SRC, f'tok_{d}.csv'), dtype={'mid': str, 'token': str}); comp = {}
    for mid, g in T.groupby('mid'):
        if len(g) == 2: a, b = g.tok_i.values; comp[a] = b; comp[b] = a
    x = pd.read_csv(os.path.join(SRC, f'oc_{d}.csv.gz'), dtype={'tx': str, 'maker': str, 'taker': str}); x = x[x.tx.isin(set(txs)) & (x.taker != EX)].copy()
    x['token'] = x.tok_i.map(T.set_index('tok_i').token); x['comp'] = x.tok_i.map(comp); x = x[x.comp.notna()]
    buy = x.side.values == 0; usd = np.where(buy, x.ma, x.ta); sh = np.where(buy, x.ta, x.ma); pr = usd / sh
    x['c'] = np.where(buy, x.tok_i, x.comp).astype(int); x['pe'] = np.where(buy, pr, 1 - pr); x['sh'] = sh
    F.append(x)
F = pd.concat(F, ignore_index=True)
def parse(inp):
    b = bytes.fromhex(inp[10:]); w = lambda i: int.from_bytes(b[i:i + 32], 'big'); off_m = w(64)
    n = w(off_m); mk = []
    for i in range(n):
        s = off_m + 32 + w(off_m + 32 * (1 + i)); f = [w(s + 32 * k) for k in range(12)]
        mk.append(dict(maker='0x' + f[1].to_bytes(32, 'big')[12:].hex(), token=str(f[3]), ts=f[8]))
    return mk
rows = []; nbad = 0; ncero = 0
for tx, g in F.groupby('tx'):
    inp = hechas.get(tx)
    if not inp or not inp.startswith('0x3c2b4399'): nbad += 1; continue
    try: mk = parse(inp)
    except Exception: nbad += 1; continue
    ts = {}
    for m in mk: ts.setdefault((m['maker'], m['token']), []).append(m['ts'])
    g = g.copy(); g['ts_firma'] = [ts.get((a, b), [np.nan])[0] for a, b in zip(g.maker, g.token)]
    g['pk'] = np.rint(g.pe * 1000).astype(int)
    for (c, pk), s in g.groupby(['c', 'pk']):
        s = s.sort_values(['bloque', 'li'])
        if len(s) < 2: continue
        v = s.ts_firma.values; mm = s.maker.values
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if mm[i] != mm[j] and not np.isnan(v[i]) and not np.isnan(v[j]): rows.append((tx, v[j] - v[i], v[i], v[j]))
P = pd.DataFrame(rows, columns=['tx', 'dts', 'ts_i', 'ts_j']); P.to_csv(os.path.join(D, 'pop_ts_pares.csv'), index=False)
cero = ((P.ts_i < 1e12) | (P.ts_j < 1e12)); Pv = P[~cero]
out = [f'Poblacion (muestra {len(txs)} txs, 20-22 Oct): txs decodificadas {P.tx.nunique()} (fallos {nbad}); pares de wallets distintas del mismo nivel: {len(P)}; con timestamp 0/invalido: {int(cero.sum())}; validos: {len(Pv)}',
       f'  inversion (el 2.o en li firmo ANTES, dts<0): {(Pv.dts<0).sum()} ({(Pv.dts<0).mean():.1%}); margen >250 ms: {(Pv.dts<-250).sum()} ({(Pv.dts<-250).mean():.1%}); >1 s: {(Pv.dts<-1000).sum()} ({(Pv.dts<-1000).mean():.1%}); >10 s: {(Pv.dts<-10000).sum()} ({(Pv.dts<-10000).mean():.1%})',
       '  dts cuantiles 1/5/10/25/50/75:' + str(np.percentile(Pv.dts, [1, 5, 10, 25, 50, 75]).round(0).tolist())]
open(os.path.join(D, 'pop_fifo.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
