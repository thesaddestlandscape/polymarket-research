#!/usr/bin/env python3
"""Rejilla de a13 (6 offsets x 4 K) con la definicion DISC_BTC_T (BTC, T 60-270, cum global, dia de cierre) por periodo: 06-16, 05 (parcial, fuera del descubrimiento), y dias posteriores."""
import csv, gzip, json, sys, os, datetime
from collections import defaultdict
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
HERE = os.path.dirname(os.path.abspath(__file__))
des = json.load(open(HERE + "/des_cache_descubrimiento.json")); des.update(json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json")))
OFFS = (500.0, 1000.0, 2000.0, 3000.0, 5000.0, 8000.0); KS = (5.0, 50.0, 200.0, 1e12)
def banda(d):
    for f in (f"{DISC}/band_{d}.csv.gz", f"{VIGC}/{d}/out/band_{d}.csv.gz", f"{HERE}/bands/band_{d}.csv.gz"):
        if os.path.exists(f): return f
cum = defaultdict(float)
acc_ = defaultdict(lambda: [0.0, 0.0, 0])   # (off,K,periodo) -> c,p,nunits ; units set aparte
us = defaultdict(set)
def per(dia):
    if dia == "2026-10-05": return "05"
    if dia <= "2026-10-16": return "06-16"
    return dia[5:]
for d in sys.argv[1:]:
    with gzip.open(banda(d), "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        for c in rd:
            if c[ix["act"]] != "BTC": continue
            mkt, lado = c[ix["mkt"]], c[ix["lado_c"]]; acc = float(c[ix["acc"]]); T = float(c[ix["T"]])
            k = (mkt, lado); c0 = cum[k]; cum[k] = c0 + acc
            if acc <= 0 or not (60 < T <= 270): continue
            if c0 + acc <= OFFS[0]: continue
            g = des.get(mkt)
            if g is None: continue
            ts = float(c[ix["ts"]]); fin = round((ts + T) / 300) * 300
            dia = datetime.datetime.fromtimestamp(fin, datetime.timezone.utc).strftime("%Y-%m-%d"); p_ = per(dia)
            co = float(c[ix["coste"]]); pn = acc * (1.0 if g == lado else 0.0) - co
            for off in OFFS:
                lo, hi = max(c0 - off, 0.0), max(c0 + acc - off, 0.0)
                if hi <= 0: continue
                for K in KS:
                    tk = max(min(K, hi) - min(K, lo), 0.0)
                    if tk <= 0: continue
                    f = tk / acc; x = acc_[(off, K, p_)]; x[0] += co * f; x[1] += pn * f
                    us[(off, K, p_)].add((dia, mkt, lado))
pers = sorted({k[2] for k in acc_})
print("celda (offset,K): EV pond (n unidades) por periodo", pers)
for off in OFFS:
    for K in KS:
        print(f"off {off:>6g} K {K:>6g}: " + "  ".join(f"{p}:{(acc_[(off,K,p)][1]/acc_[(off,K,p)][0]):+.3f}({len(us[(off,K,p)])})" if acc_[(off,K,p)][0] > 0 else f"{p}: -" for p in pers))
