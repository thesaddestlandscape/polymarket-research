#!/usr/bin/env python3
"""H43 auditoria (19-Oct, solo lectura, ligero). Coherencia del desenlace de la cache con el precio de mercado en banda:
por mercado, el lado con mayor p_s_last (ultimo precio del token antes de su ultima fila de banda) debe coincidir con el ganador.
Acuerdo por dia (y por cache). Un desenlace invertido produce acuerdo < 50 %. Uso: python3 -I a5_desenlace_vs_precio.py OUTJSON D..."""
import csv, gzip, json, os, sys
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
CACHES = {"disc": "/root/polymarket-research/experimentos/5m_barato/h43_auditoria_datos/des_cache_descubrimiento.json",
          "maker_ms": "/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json"}
C = {k: json.load(open(v)) for k, v in CACHES.items()}
OUT = sys.argv[1]; DIAS = sys.argv[2:]
def band(d):
    for f in (f"{DISC}/band_{d}.csv.gz", f"{VIGC}/{d}/out/band_{d}.csv.gz"):
        if os.path.exists(f): return f
res = {}
for d in DIAS:
    ult = {}   # (mkt, lado) -> (ts, li, p_s_last)
    with gzip.open(band(d), "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        for c in rd:
            if c[ix["act"]] != "BTC": continue
            k = (c[ix["mkt"]], c[ix["lado_c"]]); ts = float(c[ix["ts"]]); li = int(float(c[ix["li"]]))
            pl = c[ix["p_s_last"]]
            if pl == "": continue
            if k not in ult or (ts, li) > ult[k][:2]: ult[k] = (ts, li, float(pl))
    mercados = {}
    for (m, l), (_, _, p) in ult.items():
        mercados.setdefault(m, {})[l] = p
    res[d] = {}
    for nom, cache in C.items():
        ok = bad = sin = 0; empate = 0
        for m, pl in mercados.items():
            if "YES" not in pl or "NO" not in pl:
                continue   # solo un lado en banda: no hay comparacion limpia
            g = cache.get(m)
            if g is None: sin += 1; continue
            fav = "YES" if pl["YES"] > pl["NO"] else ("NO" if pl["NO"] > pl["YES"] else None)
            if fav is None: empate += 1; continue
            if fav == g: ok += 1
            else: bad += 1
        tot = ok + bad
        res[d][nom] = {"mercados_ambos_lados": ok + bad + sin + empate, "acuerdo": ok, "desacuerdo": bad,
                       "acuerdo_pct": round(100 * ok / tot, 1) if tot else None, "sin_desenlace": sin, "empate": empate}
    print(d, json.dumps(res[d]), flush=True)
json.dump(res, open(OUT, "w"), indent=1)
