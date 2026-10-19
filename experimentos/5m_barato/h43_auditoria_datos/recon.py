#!/usr/bin/env python3
"""H43 R5K: reconstruccion unidad a unidad con VARIAS definiciones sobre los mismos band_D.csv.gz de pass1.py (solo lectura).
Variantes (OFFSET 5000, K 50):
  DISC_ALL  : como an/a13-a14 (descubrimiento): TODAS las monedas, cum global (cruza dias), sin filtro T de entrada (T<=300), dia = dia de cierre.
  DISC_BTC  : idem solo BTC
  DISC_BTC_T: idem BTC, entrada solo T en (60,270]  (lo que dice el REGISTRO)
  VIG       : como el vigia: BTC, cum reiniciado en cada fichero, entrada T en (60,270], dia = dia del fichero
Salida: units_<VAR>.csv (dia,mkt,lado,fin,act,c,p,acc) y resumen por dia.
"""
import csv, gzip, json, sys, os
from collections import defaultdict
OFFSET, K = 5000.0, 50.0
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
des = json.load(open("des_cache_descubrimiento.json"))
des.update(json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json")))

def banda(d):
    for f in (f"{DISC}/band_{d}.csv.gz", f"{VIGC}/{d}/out/band_{d}.csv.gz", f"{os.path.dirname(os.path.abspath(__file__))}/bands/band_{d}.csv.gz"):
        if os.path.exists(f):
            return f
    return None

def filas(f):
    with gzip.open(f, "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        a, m, l, ts, acc, co, T, p = (ix[x] for x in ("act", "mkt", "lado_c", "ts", "acc", "coste", "T", "pc"))
        for c in rd:
            yield c[a], c[m], c[l], float(c[ts]), float(c[acc]), float(c[co]), float(c[T]), float(c[p])

def tomar(cum0, acc):
    lo, hi = max(cum0 - OFFSET, 0.0), max(cum0 + acc - OFFSET, 0.0)
    return max(min(K, hi) - min(K, lo), 0.0)

VARS = {  # nombre: (solo_btc, tmax_entrada, cum_global, dia_fichero)
    "DISC_ALL": (False, 1e9, True, False),
    "DISC_BTC": (True, 1e9, True, False),
    "DISC_BTC_T": (True, 270.0, True, False),
    "VIG": (True, 270.0, False, True),
}
units = {v: {} for v in VARS}
cumg = {v: defaultdict(float) for v in VARS}
nonmono = 0; sin_des = defaultdict(set); filas_n = defaultdict(int)
dias = sys.argv[1:]
for d in dias:
    f = banda(d)
    if f is None:
        print("SIN band", d); continue
    cumf = {v: defaultdict(float) for v in VARS}
    lastts = {}
    for act, mkt, lado, ts, acc, coste, T, pc in filas(f):
        filas_n[d] += 1
        k = (mkt, lado)
        if k in lastts and ts < lastts[k] - 1e-6:
            nonmono += 1
        lastts[k] = ts
        for v, (btc, tmax, glob, difile) in VARS.items():
            if btc and act != "BTC":
                continue
            cd = cumg[v] if glob else cumf[v]
            c0 = cd[k]; cd[k] = c0 + acc
            if acc <= 0:
                continue
            tk = tomar(c0, acc)
            if tk <= 0 or not (60.0 < T <= tmax):
                continue
            g = des.get(mkt)
            if g is None:
                sin_des[v].add(mkt); continue
            fin = round((ts + T) / 300) * 300
            dia = d if difile else __import__("datetime").datetime.utcfromtimestamp(fin).strftime("%Y-%m-%d")
            fr = tk / acc
            u = units[v].setdefault((dia, mkt, lado), {"fin": fin, "act": act, "c": 0.0, "p": 0.0, "acc": 0.0})
            u["c"] += coste * fr; u["p"] += (acc * (1.0 if g == lado else 0.0) - coste) * fr; u["acc"] += acc * fr
    print(d, "filas band", filas_n[d], flush=True)
print("no monotonas (mismo mkt,lado, ts retrocede):", nonmono)
for v in VARS:
    with open(f"units_{v}.csv", "w") as fo:
        w = csv.writer(fo); w.writerow(["dia", "mkt", "lado", "fin", "act", "c", "p", "acc"])
        for (dia, mkt, lado), u in sorted(units[v].items()):
            w.writerow([dia, mkt, lado, u["fin"], u["act"], round(u["c"], 5), round(u["p"], 5), round(u["acc"], 4)])
    print(v, "unidades", len(units[v]), "sin desenlace", len(sin_des[v]))
