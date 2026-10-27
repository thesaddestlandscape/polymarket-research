#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/verificacion
ulimit -v 3000000
while [ ! -f run_all.done ]; do sleep 30; done
for d in 05 06 07 08; do nice -n 19 ionice -c3 python3 -I v1_extract.py 2026-10-$d || exit 1; done
nice -n 19 ionice -c3 python3 -I v5_sel7.py > v5_stdout.txt 2>&1
echo DONE > run2.done
