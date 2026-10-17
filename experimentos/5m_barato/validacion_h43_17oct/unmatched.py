# Tokens del on-chain del día sin mapa BTC5m: ¿son de otro activo/marco según el registro (k rows de TODOS los activos)?
import gzip, csv, sys
from collections import Counter
D = sys.argv[1]
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
MAP = set()
with open('map_raw.csv') as f:
    for r in csv.reader(f): MAP.add(r[0])
unk = Counter(); rows_unk = 0; rows_btc = 0
with gzip.open(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{D}.csv.gz', 'rt') as f:
    next(f)
    for line in f:
        c = line.split(',', 10)
        if c[0] != 'F': continue
        tok = line.split(',')[9]
        if tok in MAP: rows_btc += 1; continue
        unk[tok] += 1; rows_unk += 1
print(D, 'filas F en mapa BTC5m', rows_btc, 'filas F fuera del mapa', rows_unk, 'tokens distintos fuera', len(unk))
want = set(unk)
found = Counter()
for day in ['2026-10-10']:
    with gzip.open(f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{day}.csv.gz', 'rt') as f:
        for line in f:
            if not line.startswith('k,'): continue
            c = line.rstrip('\n').split(',')
            if len(c) >= 8 and c[2] in want:
                found[(c[3], c[4])] += 1
                want.discard(c[2])
print('tokens fuera del mapa encontrados en registro k (todos activos), por (activo,marco):', dict(found))
print('tokens fuera del mapa SIN k en 09-15 Oct:', len(want), 'de', len(unk), '; filas en esos tokens:', sum(unk[t] for t in want))
