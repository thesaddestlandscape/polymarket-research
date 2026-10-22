#!/bin/bash
# Reanuda TODO lo pendiente de forma idempotente. Lanzar: setsid nohup nice -n 19 ionice -c3 bash $D/run3_reanudar.sh > $C/run3.out 2>&1 &
ulimit -v 3000000
D=/root/polymarket-research/experimentos/5m_barato/a6_detector_vivo/calib_colas
C=/mnt/HC_Volume_106538179/datalogs_analisis_caches/colas_20oct
cd $C
if ! grep -q EXTFIN extract2_progreso.txt 2>/dev/null; then
  rm -f mk/DOGE_*.gz mk/BNB_*.gz extract2_progreso.txt   # extraccion DOGE/BNB desde cero (evita filas duplicadas)
  while read r f; do
    zcat /mnt/HC_Volume_106538179/libro5_ms/$f 2>/dev/null | grep -a -F -f tokens_dn.txt | python3 -I $D/extract.py $C 2>> extract_err2.txt
    echo "$f" >> extract2_progreso.txt
  done < orden_ficheros.txt
  echo EXTFIN >> extract2_progreso.txt
fi
for coin in ETH SOL XRP DOGE BNB; do python3 -I $D/runner.py $coin >> runner2.log 2>&1; done   # runner reanuda: salta mercados hechos
echo ANAFIN >> runner2.log
for cfg in "L79 79 300 150" "L254 254 300 150" "W1000 85 1000 1000" "W150 85 150 75"; do
  set -- $cfg
  LALTA=$2 WB=$3 WA=$4 OUTTAG=_s$1 DIA=1 DIA_LO=1792368000 DIA_HI=1792454400 STRIDE2=2 python3 -I $D/runner.py BTC >> runner2.log 2>&1
done
echo SENSFIN >> runner2.log
