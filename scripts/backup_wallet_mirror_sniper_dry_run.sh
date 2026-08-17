#!/bin/bash
# backup_wallet_mirror_sniper_dry_run.sh -- backup diario de
# data/shadow/wallet_mirror_sniper_dry_run.csv fuera de git.
#
# Origen (17-Ago): mismo patrón que backup_results_csv.sh (09-Ago) --
# 53.7MB trackeado en git, ~2.7MB/día (34.9MB 10-Ago -> 53.7MB 17-Ago),
# a ~2.5 semanas del bloqueo duro de GitHub (100MB). Desvinculado de git
# (git rm --cached + .gitignore) para no repetir el incidente de
# ballenas_timing_history.csv (05-Ago, 6.2 días sin backup remoto).
# Dataset de análisis (wallet_mirror_tracker.py y los analisis_wallet_
# mirror_*.py lo leen), no un cache rolling -- SÍ necesita backup
# dedicado. Cron diario 03:07 UTC (2min después de backup_results_csv.sh,
# mismo patrón de rotación, evita competir por I/O en el mismo minuto).
set -euo pipefail

SRC=/root/polymarket-research/data/shadow/wallet_mirror_sniper_dry_run.csv
DEST_DIR=/mnt/HC_Volume_106538179/backups_wallet_mirror_sniper_dry_run
DIAS_MANTENER=14

[ -f "$SRC" ] || { echo "$(date -u) ERROR: $SRC no existe" ; exit 1; }

mkdir -p "$DEST_DIR"
FECHA=$(date -u +%Y-%m-%d)
DEST="$DEST_DIR/wallet_mirror_sniper_dry_run_${FECHA}.csv.gz"

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
for f in "$DEST_DIR"/wallet_mirror_sniper_dry_run_*.csv.gz; do
  [ -f "$f" ] || continue
  fecha=$(basename "$f" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
  [ -z "$fecha" ] && continue
  if [[ "$fecha" < "$CUTOFF" ]]; then
    rm "$f"
    echo "$(date -u) BORRADO (>${DIAS_MANTENER}d): $f"
  fi
done

echo "$(date -u) fin. Backups actuales: $(ls "$DEST_DIR"/wallet_mirror_sniper_dry_run_*.csv.gz 2>/dev/null | wc -l)"
