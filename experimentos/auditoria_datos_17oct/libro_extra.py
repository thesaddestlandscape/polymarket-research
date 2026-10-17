import csv, gzip, sys, collections, zlib, datetime
def iso(ms):
    return datetime.datetime.fromtimestamp(int(ms)/1000, datetime.timezone.utc).strftime("%H:%M:%S.%f")[:-3]
path = sys.argv[1]
caida = []; trav = collections.Counter(); samples = {}
prev = None; gt5 = []; nonmono = []
blag = []; dl = collections.Counter(); bper = {}; bint = []
n = 0
f = gzip.open(path, "rt", newline="")
r = csv.reader(f); next(r)
try:
    for row in r:
        if len(row) != 8: continue
        tipo, t, tok, c1, c2, c3, rec, seq = row
        n += 1
        rec = int(rec); seq = int(seq)
        if tipo not in samples: samples[tipo] = row[:6] + [row[6], row[7]]
        if tipo == "G" and c1 in ("caida","arranque") or (tipo=="G" and len(caida)<3000 and c1=="caida"):
            caida.append((iso(rec), c1, c2, c3, tok[:12], seq))
        if tipo == "G": trav[(c1, tok == "*")] += 1
        if prev is not None:
            d = rec - prev
            if d < 0 and len(nonmono) < 5: nonmono.append((seq, iso(prev), iso(rec)))
            if d > 5000 and len(gt5) < 30: gt5.append((iso(prev), iso(rec), round(d/1000,2), seq))
        prev = rec
        if tipo == "B":
            lag = rec - int(t)
            blag.append(lag)
            if tok in bper:
                bint.append(rec - bper[tok])
            bper[tok] = rec
except (EOFError, zlib.error, OSError) as e:
    print("TRUNC", type(e).__name__)
print("filas", n)
print("samples", samples)
print("G caida/arranque:", len(caida))
for x in caida[:40]: print("  ", x)
print("G motivos (c1, token=='*'):", dict(trav))
print("gaps >5s:", len(gt5)); [print("  ", x) for x in gt5[:15]]
print("rec no monotono (muestra):", nonmono)
bl = sorted(blag)
if bl:
    print("B lag rec-t s: n", len(bl), "p50", bl[len(bl)//2]/1000, "p99", bl[int(len(bl)*.99)]/1000, "max", bl[-1]/1000, "n>5s", sum(1 for x in bl if x>5000))
bi = sorted(bint)
if bi:
    print("B intervalo por token (ms): n", len(bi), "p50", bi[len(bi)//2], "p90", bi[int(len(bi)*.9)], "max", bi[-1])
