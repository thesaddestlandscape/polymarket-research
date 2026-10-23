#!/bin/bash
# 23-Oct (Javi): el disco raiz (sda1) se llena; el volumen sdb tiene 80+ GB. Cron diario 03:20Z: mueve a sdb todo lo FRIO de datalogs
# y deja symlink en la misma ruta (los scripts no notan nada). Nunca toca nada abierto, reciente (<6 h), ni la lista negra de dinero real.
# Uso: DRY=1 bash mover_datalogs_a_sdb.sh   (solo informa)
SRC=/root/polymarket-research-datalogs
DST=/mnt/HC_Volume_106538179/datalogs_auto
LOG=$SRC/mover_a_sdb.log
DRY=${DRY:-0}
exec 9>/tmp/mover_datalogs.lock; flock -n 9 || exit 0
mkdir -p "$DST"
aviso() { /usr/bin/python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e(sys.argv[1])" "$1" >/dev/null 2>&1; }
say() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
# Lista negra: dinero real, locks, kills, ledgers, estado de supervisores. Patrones de nombre (bash glob).
NEGRA='h47*|experimento_*|*.lock|*.KILL|*ledger*|*.STOP|mover_a_sdb.log|*supervisor*|f2_5m_barato*|ejecutor*|*_estado*|*latch*'
[ -d /mnt/HC_Volume_106538179 ] && mountpoint -q /mnt/HC_Volume_106538179 || { say "ABORTO: sdb no montado"; aviso "🚨 mover_datalogs: sdb no montado, no se mueve nada"; exit 1; }
load=$(awk '{print int($2)}' /proc/loadavg); [ "$load" -gt "${LOADMAX:-12}" ] && { say "SKIP load5=$load"; exit 0; }
libre_antes=$(df -BG --output=avail / | tail -1 | tr -dc 0-9)
movidos=0; saltados=0; bytes=0
shopt -s nullglob dotglob
for p in "$SRC"/*; do
  n=$(basename "$p")
  [ -L "$p" ] && continue
  case "$n" in $NEGRA) continue;; esac
  # tamano minimo: no merece la pena por debajo de 20 MB
  sz=$(du -sb "$p" 2>/dev/null | cut -f1); [ "${sz:-0}" -lt 20971520 ] && continue
  # reciente?  algo modificado en las ultimas 6 h
  if [ -n "$(find "$p" -mmin -360 -print -quit 2>/dev/null)" ]; then say "SKIP $n (reciente)"; saltados=$((saltados+1)); continue; fi
  # abierto?
  if [ -d "$p" ]; then lsof +D "$p" >/dev/null 2>&1 && { say "SKIP $n (abierto)"; saltados=$((saltados+1)); continue; }
  else lsof "$p" >/dev/null 2>&1 && { say "SKIP $n (abierto)"; saltados=$((saltados+1)); continue; }; fi
  if [ "$DRY" = 1 ]; then say "DRY moveria $n $((sz/1048576)) MB"; continue; fi
  nice -n 19 ionice -c3 rsync -aH "$p" "$DST/" || { say "FALLO rsync $n"; continue; }
  b=$(du -sb "$DST/$n" | cut -f1)
  [ "$sz" = "$b" ] || { say "FALLO tamano $n $sz != $b (no se toca el original)"; continue; }
  # re-comprobar que sigue frio justo antes del intercambio
  if [ -n "$(find "$p" -mmin -5 -print -quit 2>/dev/null)" ]; then say "SKIP $n (cambio durante copia)"; rm -rf "$DST/$n"; continue; fi
  mv "$p" "$p.moviendo" && ln -s "$DST/$n" "$p" && rm -rf "$p.moviendo" && { say "OK $n $((sz/1048576)) MB"; movidos=$((movidos+1)); bytes=$((bytes+sz)); }
done
# huerfanos en DST (symlink borrado por una retencion) con mas de 10 dias: borrar
for f in "$DST"/*; do
  n=$(basename "$f"); [ -e "$SRC/$n" ] || [ -L "$SRC/$n" ] && continue
  [ -n "$(find "$f" -mtime -10 -print -quit 2>/dev/null)" ] && continue
  [ "$DRY" = 1 ] && { say "DRY borraria huerfano $n"; continue; }
  rm -rf "$f" && say "HUERFANO borrado $n"
done
libre_despues=$(df -BG --output=avail / | tail -1 | tr -dc 0-9)
say "FIN movidos=$movidos saltados=$saltados MB=$((bytes/1048576)) libre_raiz ${libre_antes}G -> ${libre_despues}G"
[ "$DRY" != 1 ] && [ "$movidos" -gt 0 ] && aviso "mover_datalogs 03:20Z: movidos $movidos a sdb ($((bytes/1048576)) MB); raiz libre ${libre_antes}G -> ${libre_despues}G"
exit 0
