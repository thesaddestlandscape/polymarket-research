#!/usr/bin/env python3
"""t5_pats.py D: patrones (tokens de B del dia D + complementarios, y ',*,' para filas G) para extraer libro5_ms. Solo lectura."""
import sys, gzip, collections, pandas as pd
D = sys.argv[1]; DL = '/root/polymarket-research-datalogs/calibracion_etiqueta/'
B = pd.read_parquet(DL + 'ordenes_b.parquet'); toks = set(B[B.dia == D].tok)
byk = collections.defaultdict(dict)
for line in gzip.open(DL + 'v2/mk_%s.csv.gz' % D, 'rt'):
    if line[0] == 'k':
        c = line.rstrip('\n').split(','); byk[c[5]][c[7]] = c[2]
out = set(toks)
for m, d in byk.items():
    if toks & set(d.values()): out |= set(d.values())
sys.stdout.write(''.join(',%s,\n' % t for t in sorted(out)) + ',*,\n'); sys.stderr.write('B toks %d, total %d\n' % (len(toks), len(out)))
