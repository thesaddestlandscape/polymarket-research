#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/frente2_sueltos_10nov/motor
ulimit -v 3000000; export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
for d in 2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-01 2026-11-02 2026-11-03 2026-11-04 2026-11-07 2026-11-08; do
  [ -f out/MI_$d.pkl ] && { echo ya $d; continue; }
  h=$(date -u +%H%M); if [ "$h" -ge 0600 ] && [ "$h" -lt 0915 ]; then echo "VENTANA 06-09:15Z, paro"; exit 3; fi
  while [ "$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)" -lt 2600 ]; do sleep 30; done
  nice -n 19 ionice -c3 python3 -W ignore -I passT_iw.py $d >> out/run.log 2>&1
done
echo FIN >> out/run.log
