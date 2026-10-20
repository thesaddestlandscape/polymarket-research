#!/bin/bash
# espera a que termine el replay (FIN / paro) y ejecuta el analisis agregado -> analisis_h23.txt (max 8 h de espera)
O=/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_maker
for i in $(seq 1 960); do grep -qE "FIN|paro" $O/correr.log && break; sleep 30; done
cd /root/polymarket-research/experimentos/5m_barato/h23_maker
ulimit -v 3000000
nice -n 19 ionice -c3 python3 -I h23_analisis.py > $O/analisis_h23.txt 2>&1
echo "analisis listo $(date -u)" >> $O/correr.log
