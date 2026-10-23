#!/bin/bash
# extraccion libro5 20-22 Oct ETH/SOL/XRP 5m (MEDIR). nice 19, ionice c3, ulimit 3 GB. Reanudable: salta ficheros ya en progreso.txt
ulimit -v 3000000
C=/root/polymarket-research-datalogs/cola_vs_cruce
S=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/cola_vs_cruce/scripts
cd $C
while read r f; do
  grep -qx "$f" progreso.txt 2>/dev/null && continue
  zcat /mnt/HC_Volume_106538179/libro5_ms/$f 2>/dev/null | grep -a -F -f tokens.txt | python3 -I $S/p2_extract.py $C 2>> extract_err.txt
  echo "$f" >> progreso.txt
done < orden_ficheros.txt
echo EXTFIN >> progreso.txt
