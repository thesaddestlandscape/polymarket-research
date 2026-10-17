import csv, gzip, sys, collections, zlib, datetime
path = sys.argv[1]
cnt = collections.Counter(); prev = {}; gmax = {}; g30 = collections.Counter()
f = gzip.open(path, "rt", newline=""); r = csv.reader(f); next(r)
try:
    for row in r:
        if len(row) != 8: continue
        bolsa, tipo, sim, sello, rec, c1, c2, c3 = row
        if tipo not in ("Q", "T"): continue
        rec = int(rec)
        h = datetime.datetime.fromtimestamp(rec/1000, datetime.timezone.utc).strftime("%H")
        cnt[(sim, h, tipo)] += 1
        k = (bolsa, sim)
        if k in prev:
            d = rec - prev[k]
            if d > 30000: g30[k] += 1
            gmax[k] = max(gmax.get(k, 0), d)
        prev[k] = rec
except (EOFError, zlib.error, OSError) as e:
    print("TRUNC", type(e).__name__)
bolsa_name = sorted({k[0] for k in prev})
print("bolsa", bolsa_name)
sims = sorted({k[0] for k in cnt})
hrs = sorted({k[1] for k in cnt})
for s in sims:
    line = []
    for h in hrs:
        q = cnt.get((s, h, "Q"), 0); t = cnt.get((s, h, "T"), 0)
        line.append(f"{h}h Q{q}/T{t}")
    print(s, " | ".join(line))
for k in sorted(prev):
    print("maxgap", k, round(gmax.get(k, 0)/1000, 1), "s; gaps>30s:", g30.get(k, 0))
