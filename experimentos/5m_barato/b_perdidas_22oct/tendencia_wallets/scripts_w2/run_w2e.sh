#!/bin/bash
OUT=/root/polymarket-research-datalogs/w2_btc; AQ=$(dirname "$(readlink -f "$0")")
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MALLOC_ARENA_MAX=2
ulimit -v 6000000
nice -n 19 ionice -c3 python3 $AQ/s4_analisis.py > $OUT/s4_analisis.log 2>&1 && echo "FIN $(date -u +%H:%M:%S)" >> $OUT/run.log || echo "FALLO s4 $(date -u +%H:%M:%S)" >> $OUT/run.log
