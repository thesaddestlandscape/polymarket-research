#!/usr/bin/env python3
"""Dosis-respuesta por tramo de cum_banda (acciones de maker acumuladas antes de la fila; cum global entre dias) y por dia de cierre:
BTC, T en (60,270], banda (0,10;0,30]. Prorrata de cada fila entre tramos. EV pond. = sum(w*pnl)/sum(w*coste). n = mercados-lado con peso>0."""
import csv, gzip, json, sys, os, datetime
from collections import defaultdict
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
HERE = os.path.dirname(os.path.abspath(__file__))
des = json.load(open(HERE + "/des_cache_descubrimiento.json"))
des.update(json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json")))
TIERS = [(0, 500), (500, 2000), (2000, 5000), (5000, 1e12)]
def banda(d):
    for f in (f"{DISC}/band_{d}.csv.gz", f"{VIGC}/{d}/out/band_{d}.csv.gz", f"{HERE}/bands/band_{d}.csv.gz"):
        if os.path.exists(f): return f
cum = defaultdict(float)
agg = defaultdict(lambda: [0.0, 0.0, set()])     # (dia,tier) -> c, p, units
sin = 0
for d in sys.argv[1:]:
    f = banda(d)
    with gzip.open(f, "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        for c in rd:
            if c[ix["act"]] != "BTC": continue
            mkt, lado = c[ix["mkt"]], c[ix["lado_c"]]; acc = float(c[ix["acc"]]); T = float(c[ix["T"]])
            k = (mkt, lado); c0 = cum[k]; cum[k] = c0 + acc
            if acc <= 0 or not (60 < T <= 270): continue
            g = des.get(mkt)
            if g is None: sin += 1; continue
            ts = float(c[ix["ts"]]); fin = round((ts + T) / 300) * 300
            dia = datetime.datetime.fromtimestamp(fin, datetime.timezone.utc).strftime("%Y-%m-%d")
            co = float(c[ix["coste"]]); pn = acc * (1.0 if g == lado else 0.0) - co
            for ti, (a, b) in enumerate(TIERS):
                w = (min(c0 + acc, b) - max(c0, a)) / acc
                if w <= 0: continue
                x = agg[(dia, ti)]; x[0] += w * co; x[1] += w * pn; x[2].add(k)
print("sin desenlace", sin)
dias = sorted({k[0] for k in agg})
print("EV pond (n mercados-lado) por dia de cierre y tramo de cum:  " + "  ".join(f"[{a},{int(b) if b<1e11 else 'inf'})" for a, b in TIERS))
for dia in dias:
    print(dia[5:], "  ".join(f"{agg[(dia,t)][1]/agg[(dia,t)][0]:+.3f}({len(agg[(dia,t)][2])})" if agg[(dia,t)][0] > 0 else "  -  " for t in range(4)))
for lo, hi, nom in (("2026-10-06", "2026-10-16", "06-16"), ("2026-10-17", "2026-10-18", "17-18")):
    r = []
    for t in range(4):
        C = sum(agg[(d, t)][0] for d in dias if lo <= d <= hi); P = sum(agg[(d, t)][1] for d in dias if lo <= d <= hi)
        n = len(set().union(*[agg[(d, t)][2] for d in dias if lo <= d <= hi] or [set()]))
        r.append(f"{P/C:+.3f}({n}, {C:.0f}$)" if C > 0 else "-")
    print("TOTAL", nom, "  ".join(r))
