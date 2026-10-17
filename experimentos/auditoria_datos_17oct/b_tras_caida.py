import csv, gzip, sys, zlib, datetime, bisect
path = sys.argv[1]
drops = {}  # hora UTC -> etiqueta
for s in sys.argv[2].split(","):
    drops[s] = 1
def ms_of(hms):
    d = datetime.datetime(2026, 10, 17, *map(int, hms.split(":")), tzinfo=datetime.timezone.utc)
    return int(d.timestamp() * 1000)
targets = sorted(ms_of(h) for h in drops)
Bs = []; Gs = []
f = gzip.open(path, "rt", newline=""); r = csv.reader(f); next(r)
try:
    for row in r:
        if len(row) != 8: continue
        if row[0] == "B":
            Bs.append((int(row[6]), row[2]))
except (EOFError, zlib.error, OSError) as e:
    print("TRUNC", type(e).__name__)
Bs.sort()
keys = [b[0] for b in Bs]
for h in sorted(drops, key=ms_of):
    t = ms_of(h)
    i = bisect.bisect_left(keys, t - 1000)
    j = bisect.bisect_right(keys, t + 10000)
    toks = {Bs[k][1] for k in range(i, j)}
    print(h, "B en [-1s,+10s]:", j - i, "tokens distintos:", len(toks))
