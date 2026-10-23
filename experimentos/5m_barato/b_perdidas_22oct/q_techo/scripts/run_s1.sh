#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/q_techo
ulimit -v 5000000
for d in 2026-10-09 2026-10-10 2026-10-11 2026-10-12 2026-10-13 2026-10-14 2026-10-15 2026-10-16 2026-10-17 2026-10-19 2026-10-20 2026-10-21; do
  nice -n 19 ionice -c3 python3 -I scripts/s1_attach.py $d >> /root/polymarket-research-datalogs/q_techo/s1.log 2>&1
done
echo FIN >> /root/polymarket-research-datalogs/q_techo/s1.log
