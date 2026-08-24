#!/bin/bash
# backup_kalshi_btchourly.sh -- backup diario de data/prices/kalshi_btchourly_*.csv
# fuera de git.
#
# Origen (21-Ago): kalshi_btchourly_2026-08-20.csv (escalera ~100 strikes
# cada 3s, fetch_kalshi_btc.py) creció a 129.9MB -- cruzó el bloqueo duro
# de GitHub (100MB) y dejó el push atascado 107 commits desde las 17:17
# UTC del día anterior (misma familia de incidente que results.csv 09-Ago,
# activity_ws_sports 19-Ago, wallet_mirror_sniper_dry_run 17-Ago).
# Desvinculado de git (git rm --cached + .gitignore) -- este script
# sustituye ese backup.
#
# Mismo patrón que backup_activity_ws_sports.sh: cada día ya es un fichero
# propio (kalshi_btchourly_YYYY-MM-DD.csv, fetch_kalshi_btc.py rota solo),
# se comprime cada fichero diario UNA VEZ cuando ya está completo (se
# salta el de HOY, todavía creciendo). fetch_kalshi_btc.py sigue
# escribiendo al disco original -- este backup es solo la copia de
# seguridad fuera de git/disco raíz, no afecta a nada que lea el CSV.
#
# Cron diario 03:11 UTC (mismo bloque de rotación que backup_results_csv.sh
# 03:05 / backup_wallet_mirror_sniper_dry_run.sh 03:07 /
# backup_activity_ws_sports.sh 03:09, +2min para no competir por I/O).
set -euo pipefail

SRC_DIR=/root/polymarket-research/data/prices
DEST_DIR=/mnt/HC_Volume_106538179/backups_kalshi_btchourly
DIAS_MANTENER=14
HOY=$(date -u +%Y-%m-%d)

mkdir -p "$DEST_DIR"

for SRC in "$SRC_DIR"/kalshi_btchourly_*.csv; do
  [ -f "$SRC" ] || continue
  FECHA=$(basename "$SRC" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
  [ -z "$FECHA" ] && continue
  [ "$FECHA" = "$HOY" ] && continue  # todavía creciendo, se backupea mañana

  DEST="$DEST_DIR/kalshi_btchourly_${FECHA}.csv.gz"
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
for f in "$DEST_DIR"/kalshi_btchourly_*.csv.gz; do
  [ -f "$f" ] || continue
  fecha=$(basename "$f" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
  [ -z "$fecha" ] && continue
  if [[ "$fecha" < "$CUTOFF" ]]; then
    rm "$f"
    echo "$(date -u) BORRADO (>${DIAS_MANTENER}d): $f"
  fi
done

echo "$(date -u) fin. Backups actuales: $(ls "$DEST_DIR"/kalshi_btchourly_*.csv.gz 2>/dev/null | wc -l)"
