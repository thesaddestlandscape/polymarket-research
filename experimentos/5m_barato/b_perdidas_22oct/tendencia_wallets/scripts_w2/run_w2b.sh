#!/bin/bash
OUT=/root/polymarket-research-datalogs/w2_btc; AQ=$(dirname "$(readlink -f "$0")")
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
ulimit -v 3000000
for s in s2_onchain_btc s3_feats s4_analisis; do
  echo "== $s $(date -u +%H:%M:%S)" >> $OUT/run.log
  nice -n 19 ionice -c3 python3 $AQ/$s.py > $OUT/$s.log 2>&1 || { echo "FALLO $s $(date -u +%H:%M:%S)" >> $OUT/run.log; exit 1; }
done
echo "FIN $(date -u +%H:%M:%S)" >> $OUT/run.log
