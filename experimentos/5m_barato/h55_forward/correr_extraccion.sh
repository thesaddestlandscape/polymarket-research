#!/bin/bash
# Extraccion BTC de dias del registro ms para el vigia H55/H53. Espera a load5<20, MemAvailable>2,5 GB y fuera de 06-09Z.
# Uso: bash correr_extraccion.sh 2026-10-19 2026-10-20 2026-10-18   (un dia tras otro; nice 19, ionice idle, ulimit 3 GB)
LOG=/mnt/HC_Volume_106538179/datalogs_analisis_caches/h55_forward/extraccion.log
cd /root/polymarket-research/experimentos/5m_barato/h55_forward || exit 1
for D in "$@"; do
  for i in $(seq 1 360); do
    L5=$(awk '{print int($2)}' /proc/loadavg); MEM=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); H=$(date -u +%H)
    if [ "$L5" -lt 20 ] && [ "$MEM" -gt 2500 ] && { [ "$H" -lt 6 ] || [ "$H" -ge 9 ]; }; then break; fi
    sleep 60
  done
  echo "$(date -u +%FT%TZ) inicio $D load5=$L5 mem=$MEM" >> $LOG
  ( ulimit -v 3000000; nice -n 19 ionice -c3 python3 -I m5b_anidado_dia.py --dia "$D" ) >> $LOG 2>&1
  echo "$(date -u +%FT%TZ) fin $D rc=$?" >> $LOG
done
echo "$(date -u +%FT%TZ) TODO_HECHO" >> $LOG
