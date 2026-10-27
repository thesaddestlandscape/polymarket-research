#!/bin/bash
# s3: rellenos on-chain de tokens 60m+4h (mapa gamma propio). 18..23-Oct desde m60/m240_onchain (filas crudas ya filtradas por la infra; mismo esquema que onchain_fills),
# 24-Oct desde onchain_fills crudo. (Recorte por tiempo/CPU: la re-extracción completa desde crudo 19..23 queda pendiente para el red-team.)
D=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/fav_60m_4h/datos; O=/mnt/HC_Volume_106538179/agentes_datos/fav60_onchain; mkdir -p $O
ulimit -v 3000000; export LC_ALL=C
I=/mnt/HC_Volume_106538179/agentes_datos/mapa_infra
for d in 2026-10-18 2026-10-19 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do
  [ -s $O/oc_$d.csv.gz ] || (zcat $I/m60_onchain/m60_onchain_$d.csv.gz $I/m240_onchain/m240_onchain_$d.csv.gz | grep -F -f $D/tokens60_240.txt | gzip -1 > $O/oc_$d.csv.gz)
done
d=2026-10-24; [ -s $O/oc_$d.csv.gz ] || (zcat /root/polymarket-research-datalogs/onchain_fills_$d.csv.gz | grep -F -f $D/tokens60_240.txt | gzip -1 > $O/oc_$d.tmp && mv $O/oc_$d.tmp $O/oc_$d.csv.gz)
ls -la $O; echo FIN
