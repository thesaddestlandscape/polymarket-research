#!/usr/bin/env python3
"""p2_extract.py OUTDIR -- stdin: lineas libro5 prefiltradas por token. Escribe por mercado OUT/mk/<ACT>_<mid>.gz (append) con
L,B,recv,bids | L,d,recv,precio,tam (solo lado bids) | L,T,recv,side,precio,tam | L,G,recv,motivo ; G globales a OUT/g_all.txt.
(adaptado de a6_detector_vivo/calib_colas/extract.py: se omiten los asks, el ask de un token = 1 - mejor bid del contrario)"""
import sys, json, gzip, os
OUT = sys.argv[1]; TOK = json.load(open(OUT + '/tokens.json')); os.makedirs(OUT + '/mk', exist_ok=True)
H = {}
def fh(key):
    f = H.get(key)
    if f is None:
        if len(H) > 48: k0 = next(iter(H)); H.pop(k0).close()
        f = gzip.open(f'{OUT}/mk/{key}.gz', 'at', compresslevel=6); H[key] = f
    return f
gall = open(OUT + '/g_all.txt', 'a'); n = nk = 0
for ln in sys.stdin:
    c = ln.rstrip('\n').split(',')
    if len(c) < 8: continue
    t = c[0]
    try:
        if t == 'G':
            if c[2] == '*': gall.write(f'{c[6]},{c[3]}\n'); continue
            v = TOK.get(c[2])
            if v: fh(f'{v[0]}_{v[1]}').write(f'{v[2][0]},G,{c[6]},{c[3]}\n')
            continue
        v = TOK.get(c[2])
        if v is None: continue
        L = v[2][0]; key = f'{v[0]}_{v[1]}'
        if t == 'd':
            if c[3] == 'B': fh(key).write(f'{L},d,{c[6]},{c[4]},{c[5]}\n')
        elif t == 'T': fh(key).write(f'{L},T,{c[6]},{c[4]},{c[3]},{c[5]}\n')
        elif t == 'B': fh(key).write(f'{L},B,{c[6]},{c[3]},\n')
        n += 1
    except Exception: nk += 1
for f in H.values(): f.close()
gall.close(); print('filas', n, 'err', nk, file=sys.stderr)
