#!/bin/bash
# corre s3 dia a dia; espera fuera de 22:14-22:31Z y de 06:00-09:15Z; ulimit 3 GB, nice 19
cd /root/polymarket-research
ulimit -v 3000000
for D in "$@"; do
  while true; do h=$(date -u +%H%M); if { [ "$h" -ge 2214 ] && [ "$h" -le 2231 ]; } || { [ "$h" -ge 0600 ] && [ "$h" -le 0915 ]; }; then sleep 30; else break; fi; done
  m=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); while [ "$m" -lt 2300 ]; do sleep 30; m=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); done
  nice -n 19 ionice -c3 python3 experimentos/5m_barato/diseccion_bots_b_09nov/scripts/s3_registro.py "$D" || echo "FALLO $D"
done
echo FIN
