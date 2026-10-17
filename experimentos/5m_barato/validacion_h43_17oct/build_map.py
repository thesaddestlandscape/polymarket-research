# Mapa token -> (mercado, lado, fin_epoch) para BTC 5min desde registro m5_registro (k rows). Lectura en streaming.
import gzip, sys, csv
src = sys.argv[1]; out = sys.argv[2]
seen = {}
n = 0
with gzip.open(src, 'rt') as f, open(out, 'a', newline='') as o:
    w = csv.writer(o)
    for line in f:
        if not line.startswith('k,'):
            continue
        c = line.rstrip('\n').split(',')
        if len(c) < 8 or c[3] != 'BTC' or c[4] != '5min':
            continue
        n += 1
        w.writerow([c[2], c[5], c[6], c[7], c[1]])
print(src, 'k BTC 5min rows', n)
