#!/bin/bash
# Replay H23 sobre los dias 06..18-Oct (extracto v4_comprar_lo_bueno). UN job, idempotente (salta dias hechos). Fuera de 06:00-09:15Z.
cd /root/polymarket-research/experimentos/5m_barato/h23_maker || exit 1
ulimit -v 3000000
for D in 2026-10-06 2026-10-07 2026-10-08 2026-10-09 2026-10-10 2026-10-11 2026-10-12 2026-10-13 2026-10-14 2026-10-15 2026-10-16 2026-10-17 2026-10-18; do
  h=$(date -u +%H%M); if [ "$h" -ge 0600 ] && [ "$h" -lt 0915 ]; then echo "$(date -u) ventana 06-09:15Z: paro en $D"; exit 3; fi
  for i in $(seq 1 240); do   # espera (max 4 h) a MemAvailable>2,5 GB y load5<20
    mem=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); l5=$(awk '{print int($2)}' /proc/loadavg)
    [ "$mem" -gt 2500 ] && [ "$l5" -lt 20 ] && break; sleep 60
  done
  [ "$mem" -gt 2500 ] || { echo "$(date -u) sin RAM: paro en $D"; exit 4; }
  nice -n 19 ionice -c3 python3 -I h23_sim_dia.py $D
done
echo "$(date -u) FIN"
