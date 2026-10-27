#!/bin/bash
# espera load5<8 y MemAvailable>2.5GB; secuencial
for d in 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do
  while true; do l=$(cut -d' ' -f2 /proc/loadavg); m=$(awk '/MemAvailable/{print $2}' /proc/meminfo); h=$(date -u +%H%M)
    if awk "BEGIN{exit !($l<8)}" && [ "$m" -gt 2500000 ] && { [ "$h" -ge 0930 ] || [ "$h" -lt 0600 ]; }; then break; fi; sleep 60; done
  ( ulimit -v 3000000; nice -n 19 ionice -c3 python3 e0_extraer.py --dia $d ) 
done
