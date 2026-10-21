#!/usr/bin/env python3
"""h23_valida_v3.py -- el replay v3 (sizing 2eur, cierre acum) debe reproducir el replay v2 FILA A FILA (lleno, coste) en los dias que existan en ambos, para rep 0/50/150/500/1500
y todas las colas/latencias. Solo lectura. Uso: python3 -I h23_valida_v3.py [dia ...]  (por defecto, todos los comunes). Sale con codigo 1 si hay diferencias."""
import glob, os, sys
import pandas as pd
V2 = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/'
V3 = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/'
dias = sys.argv[1:] or sorted(set(os.path.basename(f)[7:17] for f in glob.glob(V2 + 'v2_BTC_20*.csv')) & set(os.path.basename(f)[7:17] for f in glob.glob(V3 + 'v3_BTC_20*.csv')))
mal = 0
for d in dias:
    a = pd.read_csv(V2 + f'v2_BTC_{d}.csv'); a = a[(a.mult == 1.0) & (a.exact == 1)]
    b = pd.read_csv(V3 + f'v3_BTC_{d}.csv'); b = b[(b.sizing == '2eur') & (b.modo == 'acum')]
    k = ['cierre', 'brazo', 'rep', 'cola', 'lat_post', 'lat_cancel']
    j = a.merge(b, on=k, how='outer', suffixes=('_2', '_3'), indicator=True)
    solo2 = int(((j._merge == 'left_only') & ~j.rep.isin([300])).sum()); solo3 = int((j._merge == 'right_only').sum() - (j[j._merge == 'right_only'].rep == 300).sum())
    ambos = j[j._merge == 'both']
    dif = ambos[(abs(ambos.lleno_2 - ambos.lleno_3) > 1e-6) | (abs(ambos.coste_2 - ambos.coste_3) > 1e-4)]
    print(f'{d}: filas v2={len(a)} v3(2eur/acum)={len(b)} comparadas={len(ambos)} solo_v2={solo2} solo_v3(sin r300)={solo3} diferentes={len(dif)}')
    mal += len(dif) + solo2 + solo3
    if len(dif): print(dif[k + ['lleno_2', 'lleno_3']].head(8).to_string())
print('VALIDACION', 'OK' if mal == 0 and dias else 'FALLA')
sys.exit(0 if mal == 0 and dias else 1)
