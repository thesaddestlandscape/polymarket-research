#!/bin/bash
ulimit -v 3000000
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f3_carry
for d in 2026-10-24 2026-10-23 2026-10-22 2026-10-21 2026-10-20 2026-10-19 2026-10-18 2026-10-17 2026-10-16 2026-10-15 2026-10-14 2026-10-13 2026-10-12 2026-10-11 2026-10-10 2026-10-09 2026-10-08 2026-10-07 2026-10-06; do
  nice -n 19 ionice -c3 python3 -I scripts/f3_extrae.py $d 5min 15min
done
for d in 2026-10-18 2026-10-19 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do
  nice -n 19 ionice -c3 python3 -I scripts/f3_extrae.py $d 60min 240min 24h
done
echo FIN
