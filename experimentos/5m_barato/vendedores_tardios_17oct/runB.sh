#!/bin/bash
# grep de las 6 wallets en todas las fuentes on-chain (una a la vez, nice)
cd /tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/vend
mkdir -p B
for d in 17 16 15 14 13 12 11 10 09; do
  f=/root/polymarket-research-datalogs/onchain_fills_2026-10-$d.csv.gz
  [ -f B/all_$d.csv.gz ] || nice -n 19 ionice -c3 zcat $f | grep -F -f w6.txt | gzip > B/all_$d.csv.gz
done
for d in 05 06 07 08; do
  for m in m5 m15; do
    f=/mnt/HC_Volume_106538179/${m}_onchain/${m}_onchain_2026-10-$d.csv.gz
    [ -f B/${m}_$d.csv.gz ] || nice -n 19 ionice -c3 zcat $f | grep -F -f w6.txt | gzip > B/${m}_$d.csv.gz
  done
done
echo FINB
