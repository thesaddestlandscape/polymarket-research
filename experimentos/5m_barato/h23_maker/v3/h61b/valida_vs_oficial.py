#!/usr/bin/env python3
"""Valida: v3 de h61b_sim (var v3, central, mult 1, primer) == v3_BTC_D.csv oficial (sizing real, modo primer, rep 150) en lleno/coste/n_fill/t_rel por (cierre, brazo, cola, lp, lc). Uso: valida_vs_oficial.py D"""
import csv, sys, gzip
D = sys.argv[1]
of = {}
for r in csv.DictReader(open(f"/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/v3_BTC_{D}.csv")):
    if r["sizing"] == "real" and r["modo"] == "primer" and r["rep"] == "150":
        of[(r["cierre"], r["brazo"], r["cola"], r["lat_post"], r["lat_cancel"])] = (float(r["lleno"]), float(r["coste"]), int(r["n_fill"]), r["t_rel"])
mi = {}
for r in csv.DictReader(gzip.open(f"/root/polymarket-research-datalogs/h61b/rows_BTC_{D}.csv.gz", "rt")):
    if r["var"] == "v3" and r["mult"] == "1" and r["modo"] == "primer":
        mi[(r["cierre"], r["brazo"], r["cola"], r["lp"], r["lc"])] = (float(r["lleno"]), float(r["coste"]), int(r["n_fill"]), r["t_rel"])
com = set(of) & set(mi)
dif = [k for k in com if of[k][:3] != mi[k][:3] or str(of[k][3]).replace(".0", "") != str(mi[k][3]).replace(".0", "")]
print(D, "oficial", len(of), "mio", len(mi), "comunes", len(com), "solo_oficial", len(set(of) - set(mi)), "solo_mio", len(set(mi) - set(of)), "diferentes", len(dif), dif[:3])
