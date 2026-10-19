#!/usr/bin/env python3
"""Solo lectura. Rejilla 6 offsets x 4 K de R5K (definicion de grid.py de la auditoria: BTC, T(60,270], cum global, dia de cierre)
por DIA, mas poblacion BTC de banda por dia; guarda unidades por celda para IC por cierre. Salida JSON a stdout-path."""
import csv, gzip, json, sys, os, datetime, pickle
from collections import defaultdict
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
AUD = "/root/polymarket-research/experimentos/5m_barato/h43_auditoria_datos"
des = json.load(open(AUD + "/des_cache_descubrimiento.json")); des.update(json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json")))
OFFS = (500.0, 1000.0, 2000.0, 3000.0, 5000.0, 8000.0); KS = (5.0, 50.0, 200.0, 1e12)
def banda(d):
    for f in (f"{DISC}/band_{d}.csv.gz", f"{VIGC}/{d}/out/band_{d}.csv.gz"):
        if os.path.exists(f): return f
cum = defaultdict(float)
U = defaultdict(lambda: [0.0, 0.0])      # (off,K,dia,mkt,lado) -> c,p
POP = defaultdict(lambda: [0.0, 0.0])    # (dia,mkt,lado) -> c,p   poblacion BTC banda T(60,270]
nodes = 0
days = sys.argv[2:]
for d in days:
    f = banda(d)
    if f is None: print("sin banda", d, file=sys.stderr); continue
    with gzip.open(f, "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        iA, iM, iL, iAc, iT, iTs, iC = ix["act"], ix["mkt"], ix["lado_c"], ix["acc"], ix["T"], ix["ts"], ix["coste"]
        for c in rd:
            if c[iA] != "BTC": continue
            mkt, lado = c[iM], c[iL]; acc = float(c[iAc]); T = float(c[iT])
            k = (mkt, lado); c0 = cum[k]; cum[k] = c0 + acc
            if acc <= 0 or not (60 < T <= 270): continue
            g = des.get(mkt)
            if g is None: nodes += 1; continue
            ts = float(c[iTs]); fin = round((ts + T) / 300) * 300
            dia = datetime.datetime.fromtimestamp(fin, datetime.timezone.utc).strftime("%Y-%m-%d")
            co = float(c[iC]); pn = acc * (1.0 if g == lado else 0.0) - co
            x = POP[(dia, mkt, lado)]; x[0] += co; x[1] += pn
            if c0 + acc <= OFFS[0]: continue
            for off in OFFS:
                lo, hi = max(c0 - off, 0.0), max(c0 + acc - off, 0.0)
                if hi <= 0: continue
                for K in KS:
                    tk = max(min(K, hi) - min(K, lo), 0.0)
                    if tk <= 0: continue
                    fr = tk / acc; y = U[(off, K, dia, mkt, lado)]; y[0] += co * fr; y[1] += pn * fr
pickle.dump({"U": dict(U), "POP": dict(POP), "nodes": nodes}, open(sys.argv[1], "wb"))
print("ok unidades", len(U), "pop", len(POP), "sin desenlace filas", nodes)
