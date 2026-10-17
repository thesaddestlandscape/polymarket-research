import csv, gzip, sys, collections, zlib, datetime
path = sys.argv[1]
ev = collections.Counter(); evtok = collections.Counter()
lastB = {}; Bdup = 0; Bn = 0; Bdup_t = 0
seq_tokens_after_G = 0
f = gzip.open(path, "rt", newline=""); r = csv.reader(f); next(r)
def hh(ms): return datetime.datetime.fromtimestamp(int(ms)/1000, datetime.timezone.utc).strftime("%H:%M:%S")
try:
    for row in r:
        if len(row) != 8: continue
        tipo, t, tok, c1, c2, c3, rec, seq = row
        if tipo == "G":
            ev[(c1, rec[:-3])] += 1  # agrupa por segundo de recepcion
            evtok[c1] += 1
        elif tipo == "B":
            Bn += 1
            if lastB.get(tok) == t: Bdup += 1
            lastB[tok] = t
except (EOFError, zlib.error, OSError) as e:
    print("TRUNC", type(e).__name__)
secs = collections.Counter()
for (motivo, sec), n in ev.items():
    secs[(motivo)] += 1
print("G filas por motivo:", dict(evtok))
print("G eventos distintos por motivo (segundos de recepcion):", dict(secs))
# eventos grandes: segundos con >=5 filas G
big = sorted([(sec, m, n) for (m, sec), n in ev.items() if n >= 5], key=lambda x: x[0])
for sec, m, n in big[:30]:
    print("  ", hh(int(sec+'000')), m, "filas", n)
print("B filas", Bn, "B con mismo t_ms que el B previo del token", Bdup)
