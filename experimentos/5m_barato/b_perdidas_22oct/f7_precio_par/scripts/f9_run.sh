#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f7_precio_par
ulimit -v 3000000
for d in 2026-10-18 2026-10-19 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do
  nice -n 19 ionice -c3 python3 scripts/f6_sim.py $d B,P2,P4,P6 > datos/f6_log_$d.txt 2>&1
done
echo FIN > datos/f6_fin.txt
