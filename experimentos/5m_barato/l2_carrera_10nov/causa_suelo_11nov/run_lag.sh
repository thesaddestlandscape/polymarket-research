#!/bin/bash
ulimit -v 1500000
SP=/tmp/claude-0/-root-polymarket-research/b3d1b5f8-ea82-4aae-9729-80ae39fbc256/scratchpad
N=${1:-8000000}
shift
for d in "$@"; do
  f=/mnt/HC_Volume_106538179/m5_registro/m5_registro_$d.csv.gz
  [ -f $f ] || { echo "falta $d"; continue; }
  if [ "$N" = "0" ]; then
    nice -n 19 ionice -c3 bash -c "zcat $f | awk -f $SP/lag2.awk > $SP/lag_${d}_full.txt"
  else
    nice -n 19 ionice -c3 bash -c "zcat $f 2>/dev/null | head -n $N | awk -f $SP/lag2.awk > $SP/lag_${d}_pre.txt"
  fi
  echo "$d hecho $(date -u +%T)"
done
