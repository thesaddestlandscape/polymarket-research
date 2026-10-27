#!/bin/bash
ulimit -v 3500000
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_ex_ante/scripts
for d in 2026-10-23 2026-10-22; do
 nice -n 19 ionice -c3 python3 -I vida_puja_virtual_5m.py --dia $d --out /mnt/HC_Volume_106538179/agentes_datos/f2_menos_as/vpv_$d.csv.gz --purgar 100000
done
echo FIN
