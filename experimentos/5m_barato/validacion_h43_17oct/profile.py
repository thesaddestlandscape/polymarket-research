# Perfil de cabecera/filas on-chain de un día: tipos, filas taker (taker==EXCH), duplicados (tx,log_index), cobertura del mapa.
import gzip, sys, csv
from collections import Counter
src = sys.argv[1]
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
tok = {}
with open('map_raw.csv') as f:
    for r in csv.reader(f):
        tok[r[0]] = r
cnt = Counter(); seen = Counter(); side_c = Counter(); btc = Counter(); hdr = None
dup = 0; ex = []
with gzip.open(src, 'rt') as f:
    hdr = next(f).strip().split(',')
    for line in f:
        c = line.rstrip('\n').split(',')
        d = dict(zip(hdr, c))
        cnt[d['tipo']] += 1
        if d['tipo'] == 'F':
            cnt['F_taker_EXCH' if d['taker'] == EXCH else 'F_maker'] += 1
        key = (d['tx'], d['log_index'], d['tipo'])
        if key in seen: dup += 1
        seen[key] += 1
        if d['token_id'] in tok:
            btc[(d['tipo'], 'taker_EXCH' if d['taker'] == EXCH else 'maker_row')] += 1
            side_c[d['side']] += 1
print(src)
print('hdr', hdr)
print('tipos', dict(cnt))
print('duplicados (tx,log,tipo)', dup)
print('filas BTC5m mapa', dict(btc), 'side', dict(side_c))
