#!/bin/bash
ulimit -v 3500000
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f2_menos_as
until grep -q FIN datos/vpv.log; do sleep 5; done
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_ex_ante/scripts
for d in 2026-10-21 2026-10-20 2026-10-19 2026-10-18 2026-10-17 2026-10-16 2026-10-15; do
 nice -n 19 ionice -c3 python3 -I vida_puja_virtual_5m.py --dia $d --out /mnt/HC_Volume_106538179/agentes_datos/f2_menos_as/vpv_$d.csv.gz --purgar 100000
done
echo FIN2
