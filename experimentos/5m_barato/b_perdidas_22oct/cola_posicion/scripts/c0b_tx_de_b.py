#!/usr/bin/env python3
"""c0b_tx_de_b.py -- todas las filas F (cualquier token) de las transacciones donde B (0x659a40ff...) es maker de un relleno, por order hash del
ledger (snapshot). Cubre tambien los 3 rellenos de 22-Oct >14:40Z sin mapa de tokens. Salida (fuera de git): DL/cola_posicion/b_tx_all.csv
(bloque,ts,tx,li,hash,maker,taker,side,tok,ma,ta,fee,rolB)"""
import gzip, json, sys
DL = '/root/polymarket-research-datalogs/cola_posicion/'
O = json.load(open(DL + 'ordenes_b.json')); H = {o['oid'] for o in O if 'lect' in o or 'pf' in o or 'tardio' in o}
txs = {}
for d in ('2026-10-20', '2026-10-21', '2026-10-22'):
    with gzip.open(f'/root/polymarket-research-datalogs/onchain_fills_{d}.csv.gz', 'rt') as f:
        for ln in f:
            if ln[0] != 'F': continue
            c = ln.split(',', 6)
            if c[5] in H: txs[c[3]] = c[5]
print('hashes', len(H), 'txs B', len(txs), flush=True)
n = 0
with open(DL + 'b_tx_all.csv', 'w') as o:
    o.write('bloque,ts,tx,li,hash,maker,taker,side,tok,ma,ta,fee\n')
    for d in ('2026-10-20', '2026-10-21', '2026-10-22'):
        with gzip.open(f'/root/polymarket-research-datalogs/onchain_fills_{d}.csv.gz', 'rt') as f:
            for ln in f:
                if ln[0] != 'F': continue
                c = ln.rstrip('\n').split(',')
                if len(c) >= 13 and c[3] in txs:
                    o.write(','.join([c[1], c[2], c[3], c[4], c[5], c[6].lower(), c[7].lower(), c[8], c[9], c[10], c[11], c[12] or '0']) + '\n'); n += 1
print('filas', n)
