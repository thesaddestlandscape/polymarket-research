#!/bin/bash
# F8: genera vpv8_D para 05..24 Oct (3 en paralelo, nice 19, ulimit 3GB). Idempotente (salta existentes).
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f8_estructura
seq 5 24 | xargs -P 3 -I{} bash -c 'D=$(printf "2026-10-%02d" {}); ulimit -v 3000000; nice -n 19 ionice -c3 python3 -I scripts/vpv_f8.py --dia $D >> /root/polymarket-research-datalogs/f8_estructura/vpv8_run.log 2>&1'
echo FIN >> /root/polymarket-research-datalogs/f8_estructura/vpv8_run.log
