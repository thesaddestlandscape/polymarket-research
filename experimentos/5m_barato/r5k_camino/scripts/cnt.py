"""Solo lectura, SIN desenlaces: unidades mercado-lado por moneda con fills de banda T(60,270] y cuantiles del acumulado final (para dimensionar H46; no mira resultados)."""
import csv, gzip, sys
from collections import defaultdict
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
cum = defaultdict(float); has = set()
for d in sys.argv[1:]:
    with gzip.open(f"{DISC}/band_{d}.csv.gz", "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        for c in rd:
            k = (c[ix["act"]], c[ix["mkt"]], c[ix["lado_c"]]); cum[k] += float(c[ix["acc"]])
            if 60 < float(c[ix["T"]]) <= 270: has.add(k)
by = defaultdict(list)
for k in has: by[k[0]].append(cum[k])
nd = len(sys.argv) - 1
for a, v in sorted(by.items()):
    v.sort(); q = lambda x: round(v[int(len(v)*x)])
    print(a, "unid/dia", round(len(v)/nd), "q0.50", q(.5), "q0.74", q(.74), "q0.93", q(.93), "q0.95", q(.95), "unid/dia>=q0.95", round(len(v)*0.05/nd, 1))
