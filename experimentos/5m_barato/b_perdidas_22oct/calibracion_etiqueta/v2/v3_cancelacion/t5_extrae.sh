#!/bin/bash
# t5_extrae.sh D FICHERO_LIBRO5 : extrae filas G/d/B/T de los tokens de B (y complementarios) del libro5_ms. Idempotente.
D=$1; F=$2; O=/root/polymarket-research-datalogs/calibracion_etiqueta/v3_l2/l2_${D}.csv.gz
[ -f "$O" ] && { echo "ya existe $O"; exit 0; }
zcat "$F" | grep -F -f /root/polymarket-research-datalogs/calibracion_etiqueta/v3_l2/pats_${D}.txt | gzip -1 > "$O.tmp" && mv "$O.tmp" "$O" && echo hecho $(zcat "$O" | wc -l)
