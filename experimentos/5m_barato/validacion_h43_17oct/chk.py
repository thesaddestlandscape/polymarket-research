# Comprobaciones: orden de bloques en el fichero, T fuera de ventana, cobertura de desenlace, cruces con des_cache si existe.
import gzip, csv, json, sys, os
from collections import Counter
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
D = sys.argv[1]
SRC = f"/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{D}.csv.gz"
MAP = {}
from datetime import datetime
with open('map_raw.csv') as f:
    for r in csv.reader(f):
        MAP[r[0]] = (r[1], r[3], datetime.fromisoformat(r[2]).timestamp())
OUT = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
prev = None; dec = 0; n = 0; blocks_seen = set(); Tc = Counter(); mk_all = set(); nofin = 0
with gzip.open(SRC, 'rt') as f:
    next(f)
    for line in f:
        c = line.rstrip('\n').split(',')
        if c[0] != 'F' or c[7] == EXCH or c[9] not in MAP: continue
        b = int(c[1])
        if prev is not None and b < prev: dec += 1
        prev = b
        n += 1
        mkt, lado, fin = MAP[c[9]]
        mk_all.add(mkt)
        T = fin - float(c[2])
        if T <= 0: Tc['T<=0'] += 1
        elif T > 300: Tc['T>300'] += 1
        elif T <= 60: Tc['T<=60'] += 1
        else: Tc['(60,300]'] += 1
print(D, 'filas maker BTC5m', n, 'retrocesos de bloque en orden de fichero', dec)
print(' T:', dict(Tc))
print(' mercados con filas', len(mk_all), 'sin desenlace en caché', sum(1 for m in mk_all if m not in OUT or OUT[m] not in ('YES','NO')))
