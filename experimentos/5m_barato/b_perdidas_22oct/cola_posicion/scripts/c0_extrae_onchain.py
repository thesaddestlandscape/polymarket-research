#!/usr/bin/env python3
"""c0_extrae_onchain.py DIA... -- rellenos on-chain F (OrderFilled) de los tokens 5m ETH/SOL/XRP (token map de cola_vs_cruce/tokens.json)
CON order_hash (que oc_D de cola_vs_cruce no guarda). Solo lectura de DL/onchain_fills_D.csv.gz.
Salida (fuera de git): /root/polymarket-research-datalogs/cola_posicion/oc_hash_D.csv.gz con columnas
bloque,ts,tx,li,hash,maker,taker,side,tok,ma,ta,fee   (tok = id completo del token). Fila 'taker==EXCH' = orden tomadora."""
import sys, gzip, json
TOK = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json'))
OUT = '/root/polymarket-research-datalogs/cola_posicion/'
for d in sys.argv[1:]:
    src = f'/root/polymarket-research-datalogs/onchain_fills_{d}.csv.gz'
    n = k = 0
    with gzip.open(src, 'rt') as f, gzip.open(OUT + f'oc_hash_{d}.csv.gz', 'wt', compresslevel=4) as o:
        o.write('bloque,ts,tx,li,hash,maker,taker,side,tok,ma,ta,fee\n')
        for ln in f:
            if ln[0] != 'F': continue
            c = ln.rstrip('\n').split(',')
            if len(c) < 13 or c[9] not in TOK: continue
            o.write(','.join([c[1], c[2], c[3], c[4], c[5], c[6].lower(), c[7].lower(), c[8], c[9], c[10], c[11], c[12] or '0']) + '\n'); n += 1
    print(d, 'filas', n, flush=True)
