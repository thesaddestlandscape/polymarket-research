#!/bin/bash
# extraer_libro5_bajos.sh DIA [ORIGEN_DIR] [DESTINO_DIR]
# Extracto de libro5 para el ciclo de vida de makers de nivel bajo (W = pspspsps5 rellena casi todo <0,10): conserva
#   T (todas), G (todas), d de bids con precio <= PMAX y B con los bids <= PMAX (asks vaciados).
# MISMO formato de 8 columnas que libro5 (ciclo_vida_W.py lo lee cambiando LIBRO5_DIR). ~13-20 % del tamano.
# Idempotente: escribe a .tmp y renombra; si ya existe el destino sale sin hacer nada. nice/ionice los pone el cron.
set -u
DIA="$1"; ORIG="${2:-/mnt/HC_Volume_106538179/libro5_ms}"; DEST="${3:-/mnt/HC_Volume_106538179/libro5_bajos}"
PMAX="${PMAX:-0.20}"
mkdir -p "$DEST"; OUT="$DEST/libro5_bajos_${DIA}.csv.gz"
[ -s "$OUT" ] && { echo "ya existe $OUT"; exit 0; }
TMP="$OUT.tmp.$$"
N=$(ls "$ORIG"/libro5_ms_${DIA}_*.csv.gz 2>/dev/null | wc -l)
for f in "$ORIG"/libro5_ms_${DIA}_*.csv.gz; do
  [ -e "$f" ] || continue
  zcat "$f" 2>/dev/null | awk -F, -v pmax="$PMAX" -v OFS=, '
    NR==1 {next}
    $1=="T" || $1=="G" {print; next}
    $1=="d" { if ($4=="B" && $5+0 <= pmax) print; next }
    $1=="B" { n=split($4,a,";"); s=""; for(i=1;i<=n;i++){ split(a[i],kv,":"); if (kv[1]+0<=pmax) s=(s==""?a[i]:s";"a[i]) }
              print $1,$2,$3,s,"","",$7,$8; next }'
done | gzip -6 > "$TMP"
echo "$DIA: ficheros origen=$N"
[ "$N" -gt 0 ] && mv "$TMP" "$OUT" && ls -la "$OUT" || rm -f "$TMP"
