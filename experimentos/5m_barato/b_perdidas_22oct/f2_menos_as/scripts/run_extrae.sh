#!/bin/bash
# secuencial, un dia cada vez; fuera de 06:00-09:15Z se asume (lanzado 12:00Z)
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f2_menos_as/scripts
ulimit -v 3500000
for d in 2026-10-23 2026-10-22 2026-10-21 2026-10-20 2026-10-19 2026-10-18 2026-10-17 2026-10-16 2026-10-15 2026-10-14 2026-10-13 2026-10-12 2026-10-11 2026-10-10 2026-10-09 2026-10-08 2026-10-07 2026-10-06; do
  M="5min 15min"; case $d in 2026-10-18|2026-10-19|2026-10-2*) M="5min 15min 60min 240min 24h";; esac
  nice -n 19 ionice -c3 python3 -I f2_extrae.py $d $M
done
echo FIN
