#!/bin/bash
OUT=/root/polymarket-research-datalogs/w2_btc; AQ=$(dirname "$(readlink -f "$0")")
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MALLOC_ARENA_MAX=2
ulimit -v 6000000
for s in s4b_ledger; do
  echo "== $s $(date -u +%H:%M:%S)" >> $OUT/run.log
  nice -n 19 ionice -c3 python3 $AQ/$s.py > $OUT/$s.log 2>&1 || { echo "FALLO $s $(date -u +%H:%M:%S)" >> $OUT/run.log; exit 1; }
done
echo "FIN $(date -u +%H:%M:%S)" >> $OUT/run.log
