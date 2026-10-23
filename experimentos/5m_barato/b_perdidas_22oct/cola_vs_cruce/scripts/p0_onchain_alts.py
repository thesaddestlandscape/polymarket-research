#!/usr/bin/env python3
"""p0_onchain_alts.py DIA... -- rellenos on-chain (filas F) de los tokens 5m ETH/SOL/XRP del npz del dia (salida/datos/ms_D.npz tmap),
desde VOL/m5_onchain (o DL/onchain_fills si no existe). Salida datos/oc_D.csv.gz: bloque,ts,tx,li,maker,taker,side,tok_i,ma,ta,fee
+ datos/tok_D.csv (tok_i,token,act,mid,fin,lado,des). Solo lectura."""
import sys, os, gzip, json, subprocess, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); MS = os.path.join(AQ, '../../salida/datos')
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json')); DES.update(json.load(open(os.path.join(MS, 'desenlaces_extra.json'))))
toks = {}
for d in sys.argv[1:]:
    for dd in (d,):
        z = np.load(os.path.join(MS, f'ms_{dd}.npz'))
        for t, (act, marco, mid, fin, lado) in zip(z['tokens'], z['tmap']):
            if str(marco) == '5min' and str(act) in ('ETH', 'SOL', 'XRP'):
                toks[str(t)] = (str(act), str(mid), int(pd.Timestamp(str(fin)).timestamp()), str(lado), DES.get(str(mid)))
    tl = sorted(toks); ti = {t: i for i, t in enumerate(tl)}
    pd.DataFrame([(ti[t], t) + toks[t] for t in tl], columns=['tok_i', 'token', 'act', 'mid', 'fin', 'lado', 'des']).to_csv(os.path.join(D, f'tok_{d}.csv'), index=False)
    src = f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz'
    if not os.path.exists(src): src = f'/root/polymarket-research-datalogs/onchain_fills_{d}.csv.gz'
    n = 0
    with gzip.open(src, 'rt') as f, gzip.open(os.path.join(D, f'oc_{d}.csv.gz'), 'wt', compresslevel=4) as o:
        o.write('bloque,ts,tx,li,maker,taker,side,tok_i,ma,ta,fee\n')
        for ln in f:
            c = ln.rstrip('\n').split(',')
            if c[0] != 'F' or len(c) < 13: continue
            k = ti.get(c[9])
            if k is None: continue
            o.write(f'{c[1]},{c[2]},{c[3]},{c[4]},{c[6].lower()},{c[7].lower()},{c[8]},{k},{c[10]},{c[11]},{c[12] or 0}\n'); n += 1
    print(d, src, 'tokens', len(tl), 'filas', n, flush=True)
