#!/usr/bin/env python3
"""s1: rellenos on-chain (filas F) de los 3 cosechadores 0x21f4/0xaa1a/0x41e2 sobre tokens 5m (todas las monedas).
Rol: maker si la contraparte 'taker' de la fila NO es el contrato exchange; la fila del tomador lleva taker = contrato.
Salida DL/m5_cosechar_abrir/wf_D.csv.gz. Solo lectura. Uso: s1_wallets_fills.py DIA..."""
import sys, gzip, subprocess, json
VOL = '/mnt/HC_Volume_106538179'; OUT = '/root/polymarket-research-datalogs/m5_cosechar_abrir'
W = {'0x21f4c1a1be34a39a7bc20985df4b7e5a39fb691d': '21f4', '0xaa1a4f31c010d4a63fc49770d4ca2d69ea370602': 'aa1a', '0x41e2e1ccf1e4940029af02259a31c6b89b9fa354': '41e2'}
EXCH = {'0xe111180000d2663c0091e4f400237545b87b996b'}
def tokmap(d):
    m = {}
    with gzip.open(f'{VOL}/m5_registro/m5_registro_{d}.csv.gz', 'rt') as f:
        for ln in f:
            if ln[0] != 'k' or not ln.startswith('k,'): continue
            c = ln.rstrip('\n').split(',')
            if c[4] != '5min': continue
            m[c[2]] = (c[3], c[5], c[6], c[7])   # coin, mid, close, lado
    return m
for d in sys.argv[1:]:
    tm = tokmap(d)
    pat = '|'.join(W)
    p = subprocess.Popen(f"nice -n 19 ionice -c3 zcat {VOL}/m5_onchain/m5_onchain_{d}.csv.gz | grep -E '^F,' | grep -E '{pat}'", shell=True, stdout=subprocess.PIPE, text=True)
    n = 0; nt = 0
    with gzip.open(f'{OUT}/wf_{d}.csv.gz', 'wt') as o:
        o.write('wallet,coin,mid,close,lado,side,price,acc,usdc,ts,bloque,tx,li,role,fee\n')
        for ln in p.stdout:
            c = ln.rstrip('\n').split(',')
            mk = c[6].lower(); tk = c[7].lower()
            if mk not in W: continue
            t = tm.get(c[9])
            if t is None: nt += 1; continue
            side = int(c[8]); ma = float(c[10]); ta = float(c[11])
            usdc, acc = (ma, ta) if side == 0 else (ta, ma)
            if acc <= 0: continue
            role = 'T' if tk in EXCH else 'M'
            o.write(f"{W[mk]},{t[0]},{t[1]},{t[2]},{t[3]},{side},{usdc/acc:.6f},{acc:.6f},{usdc:.6f},{c[2]},{c[1]},{c[3]},{c[4]},{role},{c[12] or 0}\n"); n += 1
    print(d, 'filas', n, 'sin token 5m', nt, flush=True)
