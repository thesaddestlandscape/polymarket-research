import csv, gzip, sys, collections, zlib, datetime
path = sys.argv[1]
def hh(ms): return datetime.datetime.fromtimestamp(int(ms)/1000, datetime.timezone.utc).strftime("%H:%M:%S")
evs = collections.OrderedDict()
f = gzip.open(path, "rt", newline=""); r = csv.reader(f); next(r)
last = None
try:
    for row in r:
        if len(row) != 8 or row[0] != "G": continue
        rec = int(row[6]); key = (row[3], rec // 1000)
        evs.setdefault(key, [0, set()])
        evs[key][0] += 1; evs[key][1].add(row[2][:6])
except (EOFError, zlib.error, OSError) as e:
    print("TRUNC", type(e).__name__)
for (motivo, s), (n, toks) in evs.items():
    if motivo in ("caida", "traspaso", "arranque") or (motivo == "baja" and s % 1 == 0 and n >= 1):
        pass
cai = [(hh(s*1000), n) for (m, s), (n, t) in evs.items() if m == "caida"]
print("caida (hora_recepcion, filas):", cai)
print("total G (motivo,seg) por motivo:", collections.Counter(m for (m, s) in evs))
