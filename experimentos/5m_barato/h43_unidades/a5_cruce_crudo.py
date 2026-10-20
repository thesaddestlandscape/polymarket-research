#!/usr/bin/env python3
"""A5 H43 (20-Oct): cruce CRUDO onchain_fills_D (datalogs) vs m5_onchain_D para las filas F de tokens BTC 5min, con el kall DEL PROPIO DIA
(vigia_5m_barato_r5k/D/kall.csv: tokens de D-1 y D). rawcheck18.out del 19-Oct era INVALIDO porque usaba el kall del 17-Oct.
Solo lectura, una pasada por fichero, memoria ~ numero de claves (tx,log_index) BTC5m (~1 M).
Uso: python3 -I a5_cruce_crudo.py D [D ...]   (ejecutar con nice -n 19 ionice -c3 y ulimit -v)"""
import csv, gzip, sys, json
VIG = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
RAW = "/root/polymarket-research-datalogs/onchain_fills_%s.csv.gz"
M5 = "/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_%s.csv.gz"
csv.field_size_limit(1 << 20)

def toks(d):
    t = set()
    with open(f"{VIG}/{d}/kall.csv") as fh:
        for c in csv.reader(fh):
            if len(c) > 3 and c[1] == "BTC" and c[2] == "5min":
                t.add(c[0])
    return t

def cnt(f, T):
    keys = {}
    with gzip.open(f, "rt", errors="replace") as fh:
        rd = csv.reader(fh); next(rd)
        for c in rd:
            if c and c[0] == "F" and len(c) > 9 and c[9] in T:
                keys[(c[3], c[4])] = (c[10], c[11])
    return keys

out = {}
for d in sys.argv[1:]:
    T = toks(d)
    a, b = cnt(RAW % d, T), cnt(M5 % d, T)
    sa, sb = set(a), set(b)
    dif_monto = sum(1 for k in sa & sb if a[k] != b[k])
    out[d] = {"tokens_btc5_kall": len(T), "filas_F_raw": len(a), "filas_F_m5_onchain": len(b), "solo_raw": len(sa - sb),
              "solo_m5": len(sb - sa), "importes_distintos_en_comun": dif_monto}
    print(d, json.dumps(out[d]), flush=True)
