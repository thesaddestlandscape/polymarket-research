#!/usr/bin/env python3
"""Lee por stdin lineas libro5 (ya prefiltradas por grep -F de tokens) y escribe, por mercado, un fichero gz
 (append) con filas compactas:  Y|N,tipo,recv,... ; G globales a g_all.txt.  Argumento: dir de salida, orden de fichero (prefijo)."""
import sys, json, gzip, os
OUT=sys.argv[1]; TOK=json.load(open(OUT+'/tokens.json'))
os.makedirs(OUT+'/mk',exist_ok=True)
H={}
def fh(key):
    f=H.get(key)
    if f is None:
        if len(H)>48:
            k0=next(iter(H)); H.pop(k0).close()
        f=gzip.open(f'{OUT}/mk/{key}.gz','at',compresslevel=1); H[key]=f
    return f
gall=open(OUT+'/g_all.txt','a')
n=0; nk=0
for ln in sys.stdin:
    c=ln.rstrip('\n').split(',')
    if len(c)<8: continue
    t=c[0]
    try:
        if t=='G':
            if c[2]=='*': gall.write(f'{c[6]},{c[3]}\n'); continue
            v=TOK.get(c[2])
            if v is None: continue
            fh(f'{v[0]}_{v[1]}').write(f'{v[2][0]},G,{c[6]},{c[3]}\n'); continue
        v=TOK.get(c[2])
        if v is None: continue
        L=v[2][0]  # Y/N  (YES/NO)
        key=f'{v[0]}_{v[1]}'
        if t=='d':
            fh(key).write(f'{L},d,{c[6]},{c[3]},{c[4]},{c[5]}\n')
        elif t=='T':
            fh(key).write(f'{L},T,{c[6]},{c[4]},{c[3]},{c[5]}\n')   # side,price,size
        elif t=='B':
            # bids string c[3]; asks c[4]
            fh(key).write(f'{L},B,{c[6]},{c[3]},{c[4]}\n')
        n+=1
    except Exception as e:
        nk+=1
for f in H.values(): f.close()
gall.close()
print('filas',n,'err',nk,file=sys.stderr)
