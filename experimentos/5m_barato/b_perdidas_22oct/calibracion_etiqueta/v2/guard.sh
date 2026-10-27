#!/bin/bash
# uso: guard.sh cmd...  espera load5<8, MemAvailable>2.5GB, fuera de 06:00-09:30Z; luego ejecuta con nice/ionice/ulimit
while true; do l=$(cut -d' ' -f2 /proc/loadavg); m=$(awk '/MemAvailable/{print $2}' /proc/meminfo); h=$(date -u +%H%M)
  if awk "BEGIN{exit !($l<8)}" && [ "$m" -gt 2500000 ] && { [ "$h" -ge 0930 ] || [ "$h" -lt 0600 ]; }; then break; fi; sleep 30; done
ulimit -v 3000000; export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MALLOC_ARENA_MAX=1
exec nice -n 19 ionice -c3 "$@"
