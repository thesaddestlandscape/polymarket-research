#!/bin/bash
# espera recursos (load5<=4, MemAvailable>=2,5 GB, fuera de 06-09Z) y ejecuta los pasos en serie
cd /root/polymarket-research/experimentos/5m_barato/formula_r9_28oct
ulimit -v 3000000
ok() { l5=$(cut -d' ' -f2 /proc/loadavg); ma=$(awk '/MemAvailable/{print $2}' /proc/meminfo); h=$(date -u +%H)
  awk -v l=$l5 -v m=$ma -v h=$h 'BEGIN{exit !(l<=8.0 && m>=2500000 && (h<6 || h>=9))}'; }
for step in "$@"; do
  until ok; do sleep 30; done
  echo "$(date -u +%FT%TZ) start $step" >> log_run.txt
  nice -n 19 ionice -c3 python3 $step > log_${step%.py}.txt 2>&1; echo "$(date -u +%FT%TZ) end $step rc=$?" >> log_run.txt
done
