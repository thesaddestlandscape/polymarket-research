#!/bin/bash
# lanza_pesado.sh LOG PICO cmd... -- espera (hasta 6 h) a ventana permitida (no 06:00-09:15Z ni 22:15-22:30Z) y MemAvailable>=5500 MB y ejecuta cmd por scripts/cron_pesado.sh (nice 19, ionice -c3, /usr/bin/time -v -> PICO, ulimit -v 5 GB). Una sola vez, sin reintentos.
LOG=$1; PICO=$2; shift 2; ulimit -v 5000000
ok_ahora() { h=$((10#$(date -u +%H%M))); ram=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
  { [ "$h" -lt 600 ] || [ "$h" -ge 915 ]; } && { [ "$h" -lt 2215 ] || [ "$h" -ge 2230 ]; } && [ "${ram:-0}" -ge "${RF5_RAM_MIN:-5500}" ]; }
for i in $(seq 1 ${RF5_ESPERA:-720}); do ok_ahora && break; sleep 30; done
ok_ahora || { echo "$(date -u +%FT%TZ) BLOCKED: ventana/RAM (ram=${ram}MB hhmm=$h)" >> "$LOG"; exit 3; }
echo "$(date -u +%FT%TZ) lanzado (ram=${ram}MB)" >> "$LOG"
/root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 /usr/bin/time -v -o "$PICO" "$@" >> "$LOG" 2>&1; rc=$?; echo "$(date -u +%FT%TZ) FIN rc=$rc" >> "$LOG"; exit $rc  # 24-Nov: propaga el rc del hijo (antes devolvia 0 aunque muriera)
