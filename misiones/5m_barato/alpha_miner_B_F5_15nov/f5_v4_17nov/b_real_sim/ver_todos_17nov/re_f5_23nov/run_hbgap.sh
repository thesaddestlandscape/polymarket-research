#!/bin/bash
# un dia cada vez; espera load5/nproc<3 (23-Nov chief: load5<4 absoluto nunca abria con 8 nucleos), MemAvailable>2,5 GB y fuera de 06-09Z; idempotente (salta dias ya hechos)
cd "$(dirname "$0")"; mkdir -p out/gaps
for d in 2026-11-05 2026-11-06 2026-11-07 2026-11-08 2026-11-09 2026-11-10 2026-11-11 2026-11-12 2026-11-13 2026-11-14; do
  [ -s out/gaps/gaps_$d.txt ] && grep -q FIN out/gaps/gaps_$d.txt && continue
  while :; do
    l=$(awk '{print int($2)}' /proc/loadavg); m=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); h=$(date -u +%H)
    if [ "$l" -lt $(( 3 * $(nproc) )) ] && [ "$m" -gt 2500 ] && { [ "$h" -lt 6 ] || [ "$h" -ge 9 ]; }; then break; fi
    sleep 60
  done
  ( ulimit -v 1500000; nice -n 19 ionice -c3 python3 -I hbgap.py $d ) > out/gaps/gaps_$d.tmp 2>>out/gaps/err.txt && echo FIN >> out/gaps/gaps_$d.tmp && mv out/gaps/gaps_$d.tmp out/gaps/gaps_$d.txt
  echo "$(date -u +%FT%TZ) $d hecho" >> out/gaps/progreso.log
done
echo FIN_TODO >> out/gaps/progreso.log
