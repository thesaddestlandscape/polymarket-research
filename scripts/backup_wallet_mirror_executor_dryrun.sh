#!/bin/bash
# backup_wallet_mirror_executor_dryrun.sh -- backup diario de
# data/shadow/wallet_mirror_executor_dryrun.csv fuera de git (gitignorado).
#
# Origen (24-Sep, A2): este CSV NO tenía backup y un OOM-kill a mitad de su
# reescritura (23-Sep 06:01) se llevó 15 días (08-23 Sep), reconstruidos solo
# de forma aproximada (reconstruir_wallet_mirror_executor_08_22sep.py). Mismo
# patrón que backup_wallet_mirror_sniper_dry_run.sh, pero verificando contra
# una FOTO fija (el ejecutor añade filas sin parar: comparar el .gz con el
# fichero vivo fallaría si entra una fila entre gzip y cmp). Cron 03:09 UTC.
set -euo pipefail

SRC=/root/polymarket-research/data/shadow/wallet_mirror_executor_dryrun.csv
DEST_DIR=/mnt/HC_Volume_106538179/backups_wallet_mirror_executor_dryrun
DIAS_MANTENER=14

[ -f "$SRC" ] || { echo "$(date -u) ERROR: $SRC no existe" ; exit 1; }

mkdir -p "$DEST_DIR"
FECHA=$(date -u +%Y-%m-%d)
DEST="$DEST_DIR/wallet_mirror_executor_dryrun_${FECHA}.csv.gz"
FOTO="$DEST_DIR/.foto_${FECHA}.csv"

if [ -f "$DEST" ]; then
  echo "$(date -u) SKIP: ya existe backup de hoy ($DEST)"
else
  cp "$SRC" "$FOTO"
  gzip -c "$FOTO" > "${DEST}.tmp"
  if cmp -s <(zcat "${DEST}.tmp") "$FOTO"; then
    mv "${DEST}.tmp" "$DEST"
    echo "$(date -u) OK: backup verificado -> $DEST ($(du -h "$DEST" | cut -f1), $(wc -l < "$FOTO") filas)"
  else
    echo "$(date -u) ERROR: verificación de integridad falló, backup de hoy DESCARTADO"
    rm -f "${DEST}.tmp"
    rm -f "$FOTO"
    exit 1
  fi
  rm -f "$FOTO"
fi

CUTOFF=$(date -u -d "-${DIAS_MANTENER} days" +%Y-%m-%d)
for f in "$DEST_DIR"/wallet_mirror_executor_dryrun_*.csv.gz; do
  [ -f "$f" ] || continue
  fecha=$(basename "$f" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
  [ -z "$fecha" ] && continue
  if [[ "$fecha" < "$CUTOFF" ]]; then
    rm "$f"
    echo "$(date -u) BORRADO (>${DIAS_MANTENER}d): $f"
  fi
done

echo "$(date -u) fin. Backups actuales: $(ls "$DEST_DIR"/wallet_mirror_executor_dryrun_*.csv.gz 2>/dev/null | wc -l)"
