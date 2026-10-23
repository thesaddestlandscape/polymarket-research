#!/bin/bash
# Espera a las 09:00Z (regla: nada pesado 06-09Z) y ejecuta s1..s4 en serie, nice 19 ionice idle, ulimit 3 GB.
OUT=/root/polymarket-research-datalogs/w2_btc; AQ=$(dirname "$(readlink -f "$0")")
while [ "$(date -u +%H)" -lt 9 ]; do sleep 60; done
ulimit -v 3000000
for s in s1_binance_btc s2_onchain_btc s3_feats s4_analisis; do
  echo "== $s $(date -u +%H:%M:%S)" >> $OUT/run.log
  nice -n 19 ionice -c3 python3 $AQ/$s.py >> $OUT/$s.log 2>&1 || { echo "FALLO $s $(date -u +%H:%M:%S)" >> $OUT/run.log; exit 1; }
done
echo "FIN $(date -u +%H:%M:%S)" >> $OUT/run.log
