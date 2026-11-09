#!/bin/bash
# Muestreo anti-OOM (09-Nov, OK Javi): cada minuto, si MemAvailable < 3000 MB, anota top-10 procesos por RSS. Solo lectura. Salida logs/muestreo_ram_oom.log (rota a 5 MB).
LOG=/root/polymarket-research/logs/muestreo_ram_oom.log
a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
sw=$(awk '/SwapTotal/{t=$2}/SwapFree/{f=$2}END{if(t>0)print int((t-f)*100/t); else print 0}' /proc/meminfo)
if [ "${a:-9999}" -lt 3000 ]; then
  [ -f "$LOG" ] && [ "$(stat -c %s "$LOG")" -gt 5000000 ] && mv "$LOG" "$LOG.1"
  { echo "=== $(date -u +%FT%TZ) MemAvailable=${a}MB swap=${sw}%"; ps -eo rss,pid,etime,cmd --sort=-rss | head -11 | cut -c1-230; } >> "$LOG"
fi
