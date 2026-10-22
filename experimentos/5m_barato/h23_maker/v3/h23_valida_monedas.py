#!/usr/bin/env python3
"""h23_valida_monedas.py -- el replay v3 por moneda (sizing 2eur, cierre acum) debe reproducir el replay v2 (h23_sim_v2.py, ya validado contra v1) FILA A FILA (lleno, coste) para cada
(moneda, dia) con ambos ficheros. Solo lectura. Uso: python3 -I h23_valida_monedas.py [COIN ...] ; sale con 1 si hay diferencias. Complementa h23_valida_v3.py (BTC)."""
import glob, os, sys
import pandas as pd
V2 = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/'
V3 = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/'
coins = sys.argv[1:] or ['ETH', 'SOL', 'XRP', 'DOGE', 'BNB']
mal = n_ok = 0
k = ['cierre', 'brazo', 'rep', 'cola', 'lat_post', 'lat_cancel']
for c in coins:
    d2 = {os.path.basename(f)[len(f'v2_{c}_'):-4] for f in glob.glob(V2 + f'v2_{c}_20*.csv')}
    d3 = {os.path.basename(f)[len(f'v3_{c}_'):-4] for f in glob.glob(V3 + f'v3_{c}_20*.csv')}
    for d in sorted(d2 & d3):
        a = pd.read_csv(V2 + f'v2_{c}_{d}.csv')
        if not len(a): 
            continue
        a = a[(a.mult == 1.0) & (a.exact == 1)]
        b = pd.read_csv(V3 + f'v3_{c}_{d}.csv')
        b = b[(b.sizing == '2eur') & (b.modo == 'acum')]
        j = a.merge(b, on=k, how='outer', suffixes=('_2', '_3'), indicator=True)
        solo2 = int(((j._merge == 'left_only') & ~j.rep.isin([300])).sum()); solo3 = int(((j._merge == 'right_only') & ~j.rep.isin([300])).sum())
        ambos = j[j._merge == 'both']
        dif = ambos[(abs(ambos.lleno_2 - ambos.lleno_3) > 1e-6) | (abs(ambos.coste_2 - ambos.coste_3) > 1e-4)]
        n_ok += len(ambos)
        if solo2 or solo3 or len(dif):
            mal += solo2 + solo3 + len(dif)
            print(f'{c} {d}: comparadas={len(ambos)} solo_v2={solo2} solo_v3={solo3} diferentes={len(dif)}')
print(f'filas comparadas {n_ok}; discrepancias {mal}; VALIDACION', 'OK' if mal == 0 and n_ok else 'FALLA')
sys.exit(0 if mal == 0 and n_ok else 1)
