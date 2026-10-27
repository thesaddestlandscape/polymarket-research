#!/usr/bin/env python3
"""e0_extraer.py --dia D : extrae del registro ms (m5_registro_D) SOLO filas k/q/t de los mercados donde B puso ordenes ese dia
(token de B + complementario). Salida datalogs/calibracion_etiqueta/v2/mk_D.csv.gz. Solo lectura de la fuente; idempotente."""
import sys, gzip, os, argparse
import pandas as pd
ap = argparse.ArgumentParser(); ap.add_argument('--dia', required=True); a = ap.parse_args()
DL = '/root/polymarket-research-datalogs/calibracion_etiqueta/'
OUT = DL + 'v2/mk_%s.csv.gz' % a.dia
if os.path.exists(OUT): print('ya existe', OUT); sys.exit(0)
B = pd.read_parquet(DL + 'ordenes_b.parquet'); toks = set(B[B.dia == a.dia].tok)
mk_of = {}; wantm = set(); WANT = set(); n = 0; nw = 0
with gzip.open('/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz' % a.dia, 'rt', errors='replace') as f, gzip.open(OUT + '.tmp', 'wt') as fo:
    try:
        for line in f:
            n += 1; ty = line[0]
            if ty == 'k':
                c = line.split(',')
                if len(c) >= 8 and c[4] == '5min':
                    tk, mid = c[2], c[5]; mk_of.setdefault(mid, set()).add(tk)
                    if tk in toks: wantm.add(mid)
                    if mid in wantm: WANT.update(mk_of[mid])
                    fo.write(line)
                continue
            if ty != 'q' and ty != 't': continue
            i = line.find(',', 2); i2 = line.find(',', i + 1)
            if line[i + 1:i2] in WANT: fo.write(line); nw += 1
    except EOFError: print('AVISO gz truncado', n)
os.replace(OUT + '.tmp', OUT); print(a.dia, 'lineas', n, 'escritas', nw, 'tokens', len(WANT))
