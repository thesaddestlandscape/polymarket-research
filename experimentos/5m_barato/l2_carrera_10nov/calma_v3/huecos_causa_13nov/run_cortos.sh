#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/huecos_causa_13nov
ulimit -v 3000000
for d in 2026-11-05 2026-11-06 2026-11-07 2026-11-08 2026-11-09 2026-11-10 2026-11-11 2026-11-12; do
  [ -f out/cortos_$d.json ] || nice -n 19 ionice -c3 python3 -I detector_cortos.py $d >> out/cortos.log 2>&1
done
echo FIN >> out/cortos.log
