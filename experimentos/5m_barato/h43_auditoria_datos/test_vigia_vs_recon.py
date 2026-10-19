#!/usr/bin/env python3
"""Prueba de equivalencia: el codigo REAL del vigia (importado, no copiado) sobre los band_D de pass1 vs la variante VIG de recon.py.
Uso: python3 test_vigia_vs_recon.py D [D ...]   (no escribe nada en produccion; no llama a la red: desenlaces desde cache de solo lectura)"""
import json, sys, os, csv
REPO = "/root/polymarket-research"; sys.path.insert(0, REPO)
import vigia_5m_barato_r5k_forward as V
HERE = os.path.dirname(os.path.abspath(__file__))
des = json.load(open(HERE + "/des_cache_descubrimiento.json")); des.update(json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json")))
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
ref = {}
for r in csv.DictReader(open(HERE + "/units_VIG.csv")):
    ref[(r["dia"], r["mkt"], r["lado"])] = (float(r["c"]), float(r["p"]))
bad = 0
for d in sys.argv[1:]:
    band = f"{DISC}/band_{d}.csv.gz"
    if not os.path.exists(band): band = f"{V.CACHE}/{d}/out/band_{d}.csv.gz"
    rs = V._filas(band); u, sd = V._unidades(d, rs, des)
    mine = {k[1:]: v for k, v in ref.items() if k[0] == d}
    vig = {(m, l): (x["c"], x["p"]) for (m, l), x in u.items()}
    dif = [k for k in set(mine) | set(vig) if k not in mine or k not in vig or abs(mine[k][0]-vig[k][0]) > 1e-3 or abs(mine[k][1]-vig[k][1]) > 1e-3]
    c = sum(v[0] for v in vig.values()); p = sum(v[1] for v in vig.values())
    print(d, "vigia: unidades", len(vig), "coste %.2f" % c, "EV %+.4f" % (p / c), "| recon VIG:", len(mine), "| unidades distintas:", len(dif), "| sin desenlace", len(sd))
    bad += len(dif)
print("OK" if bad == 0 else f"FALLO {bad}")
sys.exit(1 if bad else 0)
