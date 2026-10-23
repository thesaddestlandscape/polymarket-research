#!/usr/bin/env python3
"""c7_decode_calldata.py -- decodifica matchOrders (selector 0x3c2b4399) del exchange V2: taker order (offset w1) y array de maker orders (offset w2) con
[salt, maker, signer, tokenId, makerAmount, takerAmount, side, signatureType, timestamp(ms), metadata, builder, sigOffset] y makerFillAmounts (offset w4).
Emparejado con las filas F on-chain por (maker, tokenId, fill mas cercano). Anclas: la orden de B decodificada debe tener el timestamp de nuestra propia firma (ledger t_call0).
Salida datos/b_ts_orders.csv."""
import json, os, sys, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_posicion/'
EX = '0xe111180000d2663c0091e4f400237545b87b996b'
T = pd.read_csv(DL + 'b_tx_all.csv', dtype={'tok': str, 'tx': str, 'hash': str, 'maker': str, 'taker': str})
rows = []; bad = []
def parse(inp):
    b = bytes.fromhex(inp[10:]); w = lambda i: int.from_bytes(b[i:i + 32], 'big')
    cond = b[0:32].hex(); off_t, off_m, tfill, off_f = w(32), w(64), w(96), w(128)
    def order(s):
        f = [w(s + 32 * k) for k in range(12)]
        return dict(salt=f[0], maker='0x' + f[1].to_bytes(32, 'big')[12:].hex(), signer='0x' + f[2].to_bytes(32, 'big')[12:].hex(), tokenId=str(f[3]), makerAmount=f[4], takerAmount=f[5], side=f[6], sigtype=f[7], ts=f[8])
    to = order(off_t); n = w(off_m); mk = []
    for i in range(n):
        o = w(off_m + 32 * (1 + i)); mk.append(order(off_m + 32 + o))
    nf = w(off_f); fills = [w(off_f + 32 * (1 + i)) for i in range(nf)]
    return cond, to, mk, fills, tfill
for l in open(DL + 'calldata_b.jsonl'):
    d = json.loads(l); tx = d['tx']
    if not d['input'].startswith('0x3c2b4399'): bad.append((tx, d['input'][:10])); continue
    try: cond, to, mk, fills, tfill = parse(d['input'])
    except Exception as e: bad.append((tx, 'parse ' + str(e))); continue
    F = T[(T.tx == tx) & (T.taker != EX)]
    used = set()
    for i, o in enumerate(mk):
        cand = F[(F.maker == o['maker']) & (F.tok == o['tokenId']) & (~F.index.isin(used))]
        if len(cand) == 0: rows.append(dict(tx=tx, rol='M', idx=i, **o, fill=fills[i] if i < len(fills) else None, li=None, hash=None)); continue
        # fill de la orden = makerFillAmounts[i] (unidades del activo que da el maker): BUY -> USDC (ma), SELL -> acciones (ma)
        tgt = fills[i] / 1e6 if i < len(fills) else None
        j = (cand.ma - tgt).abs().idxmin() if tgt is not None else cand.index[0]
        used.add(j); r = F.loc[j]
        rows.append(dict(tx=tx, rol='M', idx=i, **o, fill=fills[i] if i < len(fills) else None, li=int(r.li), hash=r.hash, ma=r.ma, ta=r.ta, bloque=int(r.bloque)))
    rows.append(dict(tx=tx, rol='T', idx=-1, **to, fill=tfill, li=None, hash=None))
R = pd.DataFrame(rows); R.to_csv(os.path.join(D, 'b_ts_orders.csv'), index=False)
print('txs', R.tx.nunique(), 'ordenes maker', int((R.rol == 'M').sum()), 'emparejadas con F', int(R[R.rol == 'M'].li.notna().sum()), 'mal', bad[:5], len(bad))
