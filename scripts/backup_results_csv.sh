#!/bin/bash
# backup_results_csv.sh -- backup diario de data/shadow/results.csv fuera de git.
#
# Origen (09-Ago): results.csv (dataset central de IC/postmortem/hipótesis,
# el "moat" del proyecto) creció a 77.5MB trackeado en git, ~3.2MB/día --
# a ese ritmo cruzaba el bloqueo duro de GitHub (100MB) en ~1 semana, mismo
# patrón que dejó el repo sin backup remoto 6.2 días el 05-Ago
# (ballenas_timing_history.csv). Se desvinculó de git (git rm --cached +
# .gitignore) para no repetir el incidente -- este script sustituye ese
# backup: copia comprimida diaria al volumen dedicado (fuera del disco raíz
# y fuera de git), con verificación de integridad antes de confiar en ella
# y poda de copias viejas. Cron diario 03:05 UTC (justo después de
# comprimir_data_historica.sh a las 03:00, mismo patrón de rotación).
set -euo pipefail

SRC=/root/polymarket-research/data/shadow/results.csv
DEST_DIR=/mnt/HC_Volume_106538179/backups_results_csv
DIAS_MANTENER=14

[ -f "$SRC" ] || { echo "$(date -u) ERROR: $SRC no existe" ; exit 1; }

mkdir -p "$DEST_DIR"
FECHA=$(date -u +%Y-%m-%d)
DEST="$DEST_DIR/results_${FECHA}.csv.gz"

if [ -f "$DEST" ]; then
  echo "$(date -u) SKIP: ya existe backup de hoy ($DEST)"
else
  gzip -c "$SRC" > "${DEST}.tmp"
  if cmp -s <(zcat "${DEST}.tmp") "$SRC"; then
    mv "${DEST}.tmp" "$DEST"
    echo "$(date -u) OK: backup verificado -> $DEST ($(du -h "$DEST" | cut -f1))"
  else
    echo "$(date -u) ERROR: verificación de integridad falló, backup de hoy DESCARTADO"
    rm -f "${DEST}.tmp"
    exit 1
  fi
fi

# poda: mantener solo los últimos DIAS_MANTENER backups
CUTOFF=$(date -u -d "-${DIAS_MANTENER} days" +%Y-%m-%d)
for f in "$DEST_DIR"/results_*.csv.gz; do
  [ -f "$f" ] || continue
  fecha=$(basename "$f" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
  [ -z "$fecha" ] && continue
  if [[ "$fecha" < "$CUTOFF" ]]; then
    rm "$f"
    echo "$(date -u) BORRADO (>${DIAS_MANTENER}d): $f"
  fi
done

echo "$(date -u) fin. Backups actuales: $(ls "$DEST_DIR"/results_*.csv.gz 2>/dev/null | wc -l)"
