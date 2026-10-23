#!/usr/bin/env python3
"""c8_fifo_timestamps.py -- PREREG_COLA (sha a72007c5...). Con el `timestamp` firmado de cada orden maker (calldata de matchOrders):
(1) ancla: timestamp de las ordenes de B vs t_call0 del ledger; (2) para cada relleno de B, los co-makers del MISMO nivel que se rellenan ANTES (li menor): su firma
fue antes (consistente con FIFO), entre nuestra firma y nuestro ack (ambiguo) o despues del ack de B (llegaron despues con certeza: «llegaron despues y se rellenaron antes»);
(3) inversiones de timestamp entre pares del mismo nivel en las 198 txs (todas las wallets). Salida datos/fifo_timestamps.txt, datos/b_ts_pares.csv."""
import os, json, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_posicion/'
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_COLA.md'), 'rb').read()).hexdigest().startswith('a72007c5deecc5e7')
W = '0x659a40ff9920febc5a66836213040924343d297f'; EPS = 0.0005
O = {o['oid']: o for o in json.load(open(DL + 'ordenes_b.json'))}
R = pd.read_csv(os.path.join(D, 'b_ts_orders.csv'), dtype={'hash': str, 'tokenId': str})
TOK = {}
for l in open(DL + 'snap/ledger_B.jsonl'):
    d = json.loads(l)
    if d.get('tipo') == 'intencion_post': TOK[d['oid']] = d['tok']
out = []
def P(*a): out.append(' '.join(str(x) for x in a))
M = R[R.rol == 'M'].copy()
# precio equivalente largo-c del maker, c = token de la orden BUY de B en esa tx
M['usd'] = np.where(M.side == 0, M.ma, M.ta); M['acc'] = np.where(M.side == 0, M.ta, M.ma); M['px'] = M.usd / M.acc
rows = []
for tx, g in M.groupby('tx'):
    b = g[g.maker == W]
    if len(b) == 0: continue
    c = TOK[b.hash.iloc[0]]
    g = g.copy(); g['pe'] = np.where((g.tokenId == c) & (g.side == 0), g.px, np.where((g.tokenId != c) & (g.side == 1), 1 - g.px, np.nan))
    g = g.sort_values('li')
    for _, bb in b.iterrows():
        o = O[bb.hash]
        pcb = g.loc[g.hash == bb.hash, 'pe'].iloc[0]
        s = g[np.abs(g.pe - pcb) < EPS]
        for _, x in s.iterrows():
            if x.hash == bb.hash: continue
            rows.append(dict(tx=tx, b_hash=bb.hash, other=x.maker, other_hash=x.hash, antes=int(x.li < bb.li), dts_ms=x.ts - bb.ts, dack_ms=x.ts - o['t_ret'] * 1000, b_ts=bb.ts, acc=x.acc, same_wallet=int(x.maker == W)))
Pp = pd.DataFrame(rows); Pp.to_csv(os.path.join(D, 'b_ts_pares.csv'), index=False)
P('ANCLA: timestamp firmado de las ordenes de B vs t_call0 del ledger (ms): mediana', round(float((M[M.maker == W].ts - M[M.maker == W].hash.map(lambda h: O[h]['t_call0'] * 1000)).median()), 2), '| n', int((M.maker == W).sum()))
a = Pp[(Pp.antes == 1) & (Pp.same_wallet == 0)]; d = Pp[(Pp.antes == 0) & (Pp.same_wallet == 0)]
P(f'\nCo-makers del MISMO nivel rellenados ANTES que B (li menor), n={len(a)} ordenes en {a.tx.nunique()} txs:')
P(f'  firmaron ANTES que B (consistente con FIFO): {(a.dts_ms<0).sum()} ({(a.dts_ms<0).mean():.1%})')
P(f'  firmaron despues de B pero antes de su ack (ambiguo): {((a.dts_ms>=0)&(a.dack_ms<=0)).sum()} ({((a.dts_ms>=0)&(a.dack_ms<=0)).mean():.1%})')
P(f'  firmaron despues del ack de B => LLEGARON DESPUES con certeza y se rellenaron ANTES: {(a.dack_ms>0).sum()} ({(a.dack_ms>0).mean():.1%}), acciones {a[a.dack_ms>0].acc.sum():.1f} de {a.acc.sum():.1f}')
P('  dts_ms (firma_otro - firma_B) cuantiles 0/10/25/50/75/90/100:', np.percentile(a.dts_ms, [0, 10, 25, 50, 75, 90, 100]).round(0).tolist())
P(f'\nCo-makers del MISMO nivel rellenados DESPUES que B (li mayor), n={len(d)}: firmaron antes que B {(d.dts_ms<0).sum()} ({(d.dts_ms<0).mean():.1%}) [esperado ~0 si FIFO por llegada]; firmaron despues {(d.dts_ms>=0).sum()}')
P('  dts_ms cuantiles 0/10/25/50/75/90/100:', np.percentile(d.dts_ms, [0, 10, 25, 50, 75, 90, 100]).round(0).tolist() if len(d) else '-')
# (3) inversiones entre todos los pares del mismo nivel en las txs (todas las wallets)
inv = []
for tx, g in M.groupby('tx'):
    b = g[g.maker == W]
    if len(b) == 0: continue
    c = TOK[b.hash.iloc[0]]
    g = g.copy(); g['pe'] = np.where((g.tokenId == c) & (g.side == 0), g.px, np.where((g.tokenId != c) & (g.side == 1), 1 - g.px, np.nan)); g['pk'] = np.rint(g.pe * 1000)
    for pk, s in g.groupby('pk'):
        s = s.sort_values('li')
        if len(s) < 2: continue
        v = s.ts.values; n = len(v)
        for i in range(n):
            for j in range(i + 1, n): inv.append((tx, v[j] - v[i], s.maker.iloc[i] == s.maker.iloc[j]))
I = pd.DataFrame(inv, columns=['tx', 'dts', 'misma']); I = I[~I.misma]
P(f'\nINVERSIONES entre pares del mismo nivel (todas las wallets, {len(I)} pares en {I.tx.nunique()} txs): el segundo en li firmo ANTES que el primero (dts<0): {(I.dts<0).sum()} ({(I.dts<0).mean():.1%}); con margen >250 ms: {(I.dts<-250).sum()} ({(I.dts<-250).mean():.1%}); >1 s: {(I.dts<-1000).sum()} ({(I.dts<-1000).mean():.1%})')
P('  dts cuantiles 1/5/10/25/50:', np.percentile(I.dts, [1, 5, 10, 25, 50]).round(0).tolist())
open(os.path.join(D, 'fifo_timestamps.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
