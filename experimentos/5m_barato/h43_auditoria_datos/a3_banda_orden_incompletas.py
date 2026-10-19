#!/usr/bin/env python3
"""H43 auditoria (19-Oct, solo lectura). Sobre band_D.csv.gz de pass1 (ligero):
 (1) orden: file order (pass1 = ts sorted) vs (ts, li) -> inversiones y unidades que cambian;
 (2) incompletas: unidades con <K acc cosechadas (vigia las incluye; validador 17-Oct las excluye);
 (3) frontera de dia: dia de FICHERO vs dia de CIERRE.
Uso: python3 -I a3_banda_orden_incompletas.py OUTDIR D1 D2 ...   (band en DISC o VIG segun dia)"""
import csv, gzip, json, os, sys, datetime
from collections import defaultdict
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
OFF, K, TMIN, TMAX, HTMAX = 5000.0, 50.0, 60.0, 300.0, 270.0
DES = {}
for f in ("/root/polymarket-research/experimentos/5m_barato/h43_auditoria_datos/des_cache_descubrimiento.json",
          "/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json"):
    DES.update(json.load(open(f)))
OUTDIR = sys.argv[1]; DIAS = sys.argv[2:]

def band(d):
    for f in (f"{DISC}/band_{d}.csv.gz", f"{VIGC}/{d}/out/band_{d}.csv.gz"):
        if os.path.exists(f): return f

def leer(d):
    rows = []
    with gzip.open(band(d), "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        for i, c in enumerate(rd):
            if c[ix["act"]] != "BTC": continue
            rows.append(dict(i=i, ts=float(c[ix["ts"]]), li=int(float(c[ix["li"]])) if c[ix["li"]] != "" else -1,
                             mkt=c[ix["mkt"]], lado=c[ix["lado_c"]], acc=float(c[ix["acc"]]), coste=float(c[ix["coste"]]),
                             T=float(c[ix["T"]])))
    return rows

def unidades(rows, orden):
    """Logica del vigia (cum por (mkt,lado) en el orden dado; prorrata K). Devuelve {(mkt,lado): dict}."""
    rs = sorted(rows, key=orden)
    cum = defaultdict(float); U = {}
    for r in rs:
        k = (r["mkt"], r["lado"]); c0 = cum[k]; cum[k] = c0 + r["acc"]
        if r["acc"] <= 0 or not (TMIN < r["T"] <= HTMAX): continue
        lo, hi = max(c0 - OFF, 0.0), max(c0 + r["acc"] - OFF, 0.0)
        tk = max(min(K, hi) - min(K, lo), 0.0)
        if tk <= 0: continue
        g = DES.get(r["mkt"])
        if g is None: continue
        f = tk / r["acc"]; fin = round((r["ts"] + r["T"]) / 300) * 300
        u = U.setdefault(k, {"fin": fin, "c": 0.0, "p": 0.0, "acc": 0.0, "gana": g == r["lado"]})
        u["c"] += r["coste"] * f; u["p"] += (r["acc"] * (1.0 if g == r["lado"] else 0.0) - r["coste"]) * f; u["acc"] += tk
    return U

def ev(U, filtro=lambda u: True):
    us = [u for u in U.values() if filtro(u)]
    c = sum(u["c"] for u in us); p = sum(u["p"] for u in us)
    return len(us), round(c, 2), (round(p / c, 4) if c else None)

os.makedirs(OUTDIR, exist_ok=True)
resumen = []
for d in DIAS:
    rows = leer(d)
    inv = 0; last = {}
    for r in rows:   # inversiones de ts dentro de (mkt,lado) en orden de fichero
        k = (r["mkt"], r["lado"])
        if k in last and r["ts"] < last[k] - 1e-9: inv += 1
        last[k] = r["ts"]
    li_ok = all(v >= 0 for v in (r["li"] for r in rows))
    U_file = unidades(rows, lambda r: (r["mkt"], r["lado"], r["i"]))      # orden de fichero (= vigia/pass1)
    U_tsli = unidades(rows, lambda r: (r["mkt"], r["lado"], r["ts"], r["li"]))  # orden (ts, li)
    cambian = [k for k in set(U_file) | set(U_tsli) if (k not in U_file) != (k not in U_tsli) or
               (k in U_file and k in U_tsli and abs(U_file[k]["p"] - U_tsli[k]["p"]) > 1e-6)]
    inc = lambda u: u["acc"] < K - 1e-6
    res = {"dia": d, "filas_btc_band": len(rows), "inversiones_ts_en_orden_fichero": inv, "li_disponible": li_ok,
           "unidades_file": ev(U_file), "unidades_ts_li": ev(U_tsli), "unidades_que_cambian": len(cambian),
           "incompletas_file": ev(U_file, inc), "completas_file": ev(U_file, lambda u: not inc(u)),
           "incompletas_ts_li": ev(U_tsli, inc)}
    print(json.dumps(res, ensure_ascii=False))
    resumen.append(res)
    with open(f"{OUTDIR}/unidades_{d}.csv", "w", newline="") as fo:
        w = csv.writer(fo); w.writerow(["mkt", "lado", "fin", "dia_cierre", "c", "p", "acc", "incompleta", "p_file", "p_ts_li", "cambia"])
        for k in sorted(set(U_file) | set(U_tsli)):
            a = U_file.get(k); b = U_tsli.get(k)
            u = a or b
            dia_c = datetime.datetime.fromtimestamp(u["fin"], datetime.timezone.utc).strftime("%Y-%m-%d")
            w.writerow([k[0], k[1], u["fin"], dia_c, round(u["c"], 4) if a else "", round(u["p"], 4) if a else "",
                        round(u["acc"], 3) if a else "", int(inc(u)) if a else "",
                        round(a["p"], 4) if a else "", round(b["p"], 4) if b else "", int(k in cambian)])
json.dump(resumen, open(f"{OUTDIR}/resumen_orden_incompletas.json", "w"), indent=1, ensure_ascii=False)
