# Verificación independiente de la orientación del desenlace: precio del YES en los últimos 30 s (T in (0,30]) vs etiqueta de la caché.
import gzip, csv, json, sys
from collections import defaultdict
from datetime import datetime
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
D = sys.argv[1]
MAP = {}
with open('map_raw.csv') as f:
    for r in csv.reader(f):
        MAP[r[0]] = (r[1], r[3], datetime.fromisoformat(r[2]).timestamp())
OUT = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
px = defaultdict(list)
with gzip.open(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{D}.csv.gz', 'rt') as f:
    next(f)
    for line in f:
        c = line.rstrip('\n').split(',')
        if c[0] != 'F' or c[9] not in MAP: continue
        mkt, lado, fin = MAP[c[9]]
        T = fin - float(c[2])
        if not (0 < T <= 30): continue
        sh = float(c[11]) if c[8] == '0' else float(c[10])
        usd = float(c[10]) if c[8] == '0' else float(c[11])
        if sh <= 0: continue
        q = usd / sh
        qy = q if lado == 'YES' else 1 - q
        px[mkt].append((qy, sh))
ok = bad = 0; ambiguos = 0; bad_ex = []
for m, lst in px.items():
    tot = sum(s for _, s in lst)
    qy = sum(q * s for q, s in lst) / tot
    if abs(qy - 0.5) < 0.2: ambiguos += 1; continue
    lab = OUT.get(m)
    if (qy > 0.5) == (lab == 'YES'): ok += 1
    else: bad += 1; bad_ex.append((m, round(qy, 3), lab))
print(D, 'mercados con fills T(0,30]:', len(px), 'concordantes', ok, 'discordantes', bad, 'ambiguos(|q-0.5|<0.2)', ambiguos)
print(' ejemplos discordantes', bad_ex[:5])
