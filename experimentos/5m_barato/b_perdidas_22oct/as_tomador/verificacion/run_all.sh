#!/bin/bash
# lanzador (ejecutar >= 09:00Z): extrae 09..23-Oct (crudo) y corre v2,v3,v4. nice 19 / ionice idle / ulimit.
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/verificacion
ulimit -v 3000000
for d in 09 10 11 12 13 14 15 16 17 18 19 20 21; do
  nice -n 19 ionice -c3 python3 -I v1_extract.py 2026-10-$d || exit 1
done
nice -n 19 ionice -c3 python3 -I v2_analisis.py > v2_stdout.txt 2>&1
nice -n 19 ionice -c3 python3 -I v4_desenlaces.py > v4_stdout.txt 2>&1
nice -n 19 ionice -c3 python3 -I v3_B.py > v3_stdout.txt 2>&1
echo DONE > run_all.done
