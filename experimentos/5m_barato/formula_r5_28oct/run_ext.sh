#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r5_28oct
ulimit -v 4500000
for d in 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 09 08 07 06 05; do nice -n 19 ionice -c3 python3 r5.py ext 2026-10-$d; done >> log_ext.txt 2>&1
cd ../formula_r4_28oct
[ -f salida_build_R4_original.txt ] || cp salida_build.txt salida_build_R4_original.txt
nice -n 19 ionice -c3 python3 r4.py build 2026-10-05 2026-10-06 2026-10-07 2026-10-08 >> ../formula_r5_28oct/log_build.txt 2>&1
echo FIN > ../formula_r5_28oct/FIN_EXT.txt
