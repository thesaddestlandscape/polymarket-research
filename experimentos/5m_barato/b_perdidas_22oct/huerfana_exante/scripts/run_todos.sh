#!/bin/bash
# un dia por proceso, nice 19 ionice idle, ulimit 3 GB (load5>=4); fallo de memoria => dia MISSING (log)
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/huerfana_exante
for d in ${DIAS:-2026-10-22 2026-10-23 2026-10-18 2026-10-19 2026-10-20 2026-10-21}; do
  ( ulimit -v ${ULIM:-3000000}; nice -n 19 ionice -c3 python3 -I scripts/ps_run.py $d > datos/ps_log_$d.txt 2>&1 ); echo "$d rc=$? $(date -u +%T)" >> datos/ps_runs.log
done
echo FIN >> datos/ps_runs.log
