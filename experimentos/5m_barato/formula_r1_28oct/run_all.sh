#!/bin/bash
# lanzador FORMULA_R1_B: 2 trabajadores, idempotente (salta dias hechos), guardas load5<7 y RAM>3 GB, nice 19 ionice idle, ulimit 3 GB
cd /root/polymarket-research/experimentos/5m_barato/formula_r1_28oct
ulimit -v 3000000
worker() {
  for D in "$@"; do
    [ -s out/f_$D.csv.gz ] && continue
    while :; do
      L=$(cut -d' ' -f2 /proc/loadavg | cut -d. -f1); M=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
      [ "$L" -lt 7 ] && [ "$M" -gt 3000 ] && break; sleep 60
    done
    nice -n 19 ionice -c3 python3 extract.py $D >> run.log 2>&1
  done
}
worker 2026-10-23 2026-10-05 2026-10-07 2026-10-09 2026-10-11 2026-10-13 2026-10-15 2026-10-17 2026-10-19 2026-10-21 2026-10-25 &
worker 2026-10-24 2026-10-06 2026-10-08 2026-10-10 2026-10-12 2026-10-14 2026-10-16 2026-10-18 2026-10-20 2026-10-22 2026-10-26 &
wait
echo FIN >> run.log
