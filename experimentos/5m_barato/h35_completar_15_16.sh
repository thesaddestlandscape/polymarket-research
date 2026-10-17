#!/bin/bash
# Completa H35 en 15 y 16-Oct (MemoryError con 3 GB): un día cada vez, ulimit 4,5 GB, solo con >5 GB disponibles,
# fuera de 06-09:15Z y de los reinicios de RAM (22:15-22:30Z). Reintenta cada 15 min hasta las 05:30Z de mañana.
cd /root/polymarket-research || exit 1
LOG=/root/polymarket-research/logs/h35_deep_peg_15_16.log
for D in 2026-10-15 2026-10-16; do
  while true; do
    HM=$((10#$(date -u +%H)*60 + 10#$(date -u +%M)))
    MEM=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
    LOAD=$(cut -d' ' -f1 /proc/loadavg | cut -d. -f1)
    if [ "$MEM" -gt 5000 ] && [ "$LOAD" -lt 12 ] && { [ "$HM" -lt 360 ] || [ "$HM" -ge 555 ]; } && { [ "$HM" -lt 1335 ] || [ "$HM" -ge 1350 ]; }; then break; fi
    if [ "$HM" -ge 330 ] && [ "$HM" -lt 360 ] && [ "$(date -u +%d)" != "17" ]; then echo "$(date -u +%FT%TZ) sin hueco: se deja" >> "$LOG"; exit 0; fi
    echo "$(date -u +%FT%TZ) espera $D (mem=${MEM}MB load=$LOAD)" >> "$LOG"; sleep 900
  done
  echo "$(date -u +%FT%TZ) INICIO $D" >> "$LOG"
  ( ulimit -v 4500000; nice -n 19 ionice -c3 python3 analisis_5m_maker_banda_deep_peg.py --dias "$D" --out /root/polymarket-research-datalogs/m5_maker_banda_deep_peg ) >> "$LOG" 2>&1
  echo "$(date -u +%FT%TZ) FIN $D rc=$?" >> "$LOG"
done
( nice -n 19 python3 analisis_5m_maker_banda_deep_peg.py --solo-informe --out /root/polymarket-research-datalogs/m5_maker_banda_deep_peg ) >> "$LOG" 2>&1
echo "$(date -u +%FT%TZ) informe regenerado" >> "$LOG"
