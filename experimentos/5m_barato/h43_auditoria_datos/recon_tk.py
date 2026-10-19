#!/usr/bin/env python3
"""H43: filas de la ventana de entrada (K=50 tras 5000, BTC, T(60,270], cum global) con taker, maker, clase del tomador y precio -> rows_tk.csv.gz"""
import csv, gzip, json, sys, os, datetime
from collections import defaultdict
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
HERE = os.path.dirname(os.path.abspath(__file__))
des = json.load(open(HERE + "/des_cache_descubrimiento.json")); des.update(json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json")))
OFF, K = 5000.0, 50.0
def banda(d):
    for f in (f"{DISC}/band_{d}.csv.gz", f"{VIGC}/{d}/out/band_{d}.csv.gz", f"{HERE}/bands/band_{d}.csv.gz"):
        if os.path.exists(f): return f
cum = defaultdict(float)
out = gzip.open("rows_tk.csv.gz", "wt"); W = csv.writer(out)
W.writerow(["dia", "mkt", "lado", "ts", "T", "pc", "w", "acc_tk", "c", "p", "gana", "maker", "taker", "tk_clase", "cum0"])
for d in sys.argv[1:]:
    with gzip.open(banda(d), "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        for c in rd:
            if c[ix["act"]] != "BTC": continue
            mkt, lado = c[ix["mkt"]], c[ix["lado_c"]]; acc = float(c[ix["acc"]]); T = float(c[ix["T"]])
            k = (mkt, lado); c0 = cum[k]; cum[k] = c0 + acc
            if acc <= 0 or not (60 < T <= 270): continue
            lo, hi = max(c0 - OFF, 0.0), max(c0 + acc - OFF, 0.0)
            tk = max(min(K, hi) - min(K, lo), 0.0)
            if tk <= 0: continue
            g = des.get(mkt)
            if g is None: continue
            ts = float(c[ix["ts"]]); fin = round((ts + T) / 300) * 300
            dia = datetime.datetime.fromtimestamp(fin, datetime.timezone.utc).strftime("%Y-%m-%d")
            fr = tk / acc; co = float(c[ix["coste"]]); gana = 1 if g == lado else 0
            W.writerow([dia, mkt, lado, ts, T, c[ix["pc"]], round(fr, 6), round(tk, 4), round(co * fr, 5), round((acc * gana - co) * fr, 5), gana,
                        c[ix["maker"]][:12], c[ix["taker"]][:12], c[ix["tk_clase"]], round(c0, 1)])
out.close()
