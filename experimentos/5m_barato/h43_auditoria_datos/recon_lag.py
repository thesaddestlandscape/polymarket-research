#!/usr/bin/env python3
"""H43: test de observabilidad (look-ahead de entrada). BTC, banda, cum global, T de entrada (60,270], K=50 acciones.
Unidad = primeras K acciones de filas con ts >= ts_cruce + L (L = retardo de observacion: bloque ~2,4 s + decision + 0,05 s de maker en el libro).
L=0 reproduce la definicion congelada (incluye el sobrante de la fila que cruza). Dia = dia de cierre del mercado."""
import csv, gzip, json, sys, os, datetime
from collections import defaultdict
sys.path.insert(0, ".")
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
HERE = os.path.dirname(os.path.abspath(__file__))
des = json.load(open(HERE + "/des_cache_descubrimiento.json")); des.update(json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json")))
OFF, K = 5000.0, 50.0
LS = [0, 3, 5, 10, 20, 60]
def banda(d):
    for f in (f"{DISC}/band_{d}.csv.gz", f"{VIGC}/{d}/out/band_{d}.csv.gz", f"{HERE}/bands/band_{d}.csv.gz"):
        if os.path.exists(f): return f
st = {L: {} for L in LS}                  # L -> (mkt,lado) -> [cum, ts_cruce, need]
units = {L: {} for L in LS}
tx_same = [0, 0]
for d in sys.argv[1:]:
    with gzip.open(banda(d), "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        for c in rd:
            if c[ix["act"]] != "BTC": continue
            mkt, lado = c[ix["mkt"]], c[ix["lado_c"]]; acc = float(c[ix["acc"]]); T = float(c[ix["T"]]); ts = float(c[ix["ts"]])
            co = float(c[ix["coste"]]); k = (mkt, lado)
            for L in LS:
                s = st[L].setdefault(k, [0.0, None, K])
                c0 = s[0]; s[0] = c0 + acc
                if acc <= 0: continue
                if s[1] is None:
                    if s[0] >= OFF:
                        s[1] = ts; avail = s[0] - OFF
                    else:
                        continue
                else:
                    avail = acc
                if ts < s[1] + L or s[2] <= 0 or not (60 < T <= 270): continue
                g = des.get(mkt)
                if g is None: continue
                tk = min(avail, s[2], acc); s[2] -= tk
                if tk <= 0: continue
                fr = tk / acc; fin = round((ts + T) / 300) * 300
                dia = datetime.datetime.fromtimestamp(fin, datetime.timezone.utc).strftime("%Y-%m-%d")
                u = units[L].setdefault((dia, mkt, lado), {"fin": fin, "c": 0.0, "p": 0.0, "acc": 0.0})
                u["c"] += co * fr; u["p"] += (acc * (1.0 if g == lado else 0.0) - co) * fr; u["acc"] += tk
    print(d, flush=True, file=sys.stderr)
for L in LS:
    with open(f"units_LAG{L}.csv", "w") as fo:
        w = csv.writer(fo); w.writerow(["dia", "mkt", "lado", "fin", "act", "c", "p", "acc"])
        for (dia, mkt, lado), u in sorted(units[L].items()):
            w.writerow([dia, mkt, lado, u["fin"], "BTC", round(u["c"], 5), round(u["p"], 5), round(u["acc"], 4)])
