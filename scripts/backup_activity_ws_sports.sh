#!/bin/bash
# backup_activity_ws_sports.sh -- backup diario de data/sports/activity_ws_*.csv
# fuera de git.
#
# Origen (19-Ago): vigia_tamano_ficheros_git.py cruzó el umbral warning
# (50MB) con activity_ws_2026-08-18.csv (69.5MB, un día completo, ~70MB/día
# de ritmo) -- mismo patrón que wallet_mirror_sniper_dry_run.csv (17-Ago) y
# results.csv (09-Ago): a ese ritmo cruza el bloqueo duro de GitHub (100MB)
# en pocos días, mismo riesgo que dejó el repo sin backup remoto 6.2 días
# el 05-Ago (ballenas_timing_history.csv). Desvinculado de git (git rm
# --cached + .gitignore) -- este script sustituye ese backup.
#
# Distinto de backup_results_csv.sh: aquí cada DÍA ya es un fichero propio
# (activity_ws_YYYY-MM-DD.csv, sports_activity_ws.py rota solo), así que
# no hace falta comprimir "el mismo fichero cada día" -- se comprime cada
# fichero diario UNA VEZ, cuando ya está completo (se salta el de HOY,
# todavía creciendo). sports_wallet_edge_tracker.py sigue leyendo del
# disco original (glob activity_ws_*.csv) -- este backup es solo la copia
# de seguridad fuera de git/disco raíz, no afecta a nada que lea el CSV.
#
# Cron diario 03:09 UTC (mismo bloque de rotación que backup_results_csv.sh
# 03:05 / backup_wallet_mirror_sniper_dry_run.sh 03:07, +2min para no
# competir por I/O en el mismo minuto).
set -euo pipefail

SRC_DIR=/root/polymarket-research/data/sports
DEST_DIR=/mnt/HC_Volume_106538179/backups_activity_ws_sports
DIAS_MANTENER=14
HOY=$(date -u +%Y-%m-%d)

mkdir -p "$DEST_DIR"

for SRC in "$SRC_DIR"/activity_ws_*.csv; do
  [ -f "$SRC" ] || continue
  FECHA=$(basename "$SRC" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
  [ -z "$FECHA" ] && continue
  [ "$FECHA" = "$HOY" ] && continue  # todavía creciendo, se backupea mañana

  DEST="$DEST_DIR/activity_ws_${FECHA}.csv.gz"
  if [ -f "$DEST" ]; then
    continue  # ya respaldado, un fichero diario completo no cambia después
  fi

  gzip -c "$SRC" > "${DEST}.tmp"
  if cmp -s <(zcat "${DEST}.tmp") "$SRC"; then
    mv "${DEST}.tmp" "$DEST"
    echo "$(date -u) OK: backup verificado -> $DEST ($(du -h "$DEST" | cut -f1))"
  else
    echo "$(date -u) ERROR: verificación de integridad falló para $FECHA, backup DESCARTADO"
    rm -f "${DEST}.tmp"
  fi
done

# poda: mantener solo los últimos DIAS_MANTENER backups
CUTOFF=$(date -u -d "-${DIAS_MANTENER} days" +%Y-%m-%d)
for f in "$DEST_DIR"/activity_ws_*.csv.gz; do
  [ -f "$f" ] || continue
  fecha=$(basename "$f" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
  [ -z "$fecha" ] && continue
  if [[ "$fecha" < "$CUTOFF" ]]; then
    rm "$f"
    echo "$(date -u) BORRADO (>${DIAS_MANTENER}d): $f"
  fi
done

echo "$(date -u) fin. Backups actuales: $(ls "$DEST_DIR"/activity_ws_*.csv.gz 2>/dev/null | wc -l)"
