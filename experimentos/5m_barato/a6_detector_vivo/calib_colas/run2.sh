#!/bin/bash
ulimit -v 3000000
S=/tmp/claude-0/-root-polymarket-research/06f7b0e2-eafc-4b79-84cd-46f932c672b1/scratchpad
C=/mnt/HC_Volume_106538179/datalogs_analisis_caches/colas_20oct
cd $C
# 1) extraccion DOGE/BNB
while read r f; do
  zcat /mnt/HC_Volume_106538179/libro5_ms/$f 2>/dev/null | grep -a -F -f tokens_dn.txt | python3 -I $S/extract.py $C 2>> extract_err2.txt
  echo "$f" >> extract2_progreso.txt
done < orden_ficheros.txt
echo EXTFIN >> extract2_progreso.txt
# 2) analisis (ETH reanuda: ya tiene mercados hechos con stride 2; el resto se anade)
for coin in ETH SOL XRP DOGE BNB; do python3 -I $S/runner.py $coin >> runner2.log 2>&1; done
echo ANAFIN >> runner2.log
# 3) sensibilidades BTC dia 19 (mercados alternos)
for cfg in "L79 79 300 150" "L254 254 300 150" "W1000 85 1000 1000" "W150 85 150 75"; do
  set -- $cfg
  LALTA=$2 WB=$3 WA=$4 OUTTAG=_s$1 DIA=1 DIA_LO=1792368000 DIA_HI=1792454400 STRIDE2=2 python3 -I $S/runner.py BTC >> runner2.log 2>&1
done
echo SENSFIN >> runner2.log
