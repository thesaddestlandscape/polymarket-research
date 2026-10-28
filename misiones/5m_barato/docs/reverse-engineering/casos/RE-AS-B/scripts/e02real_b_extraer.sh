#!/bin/bash
# E02-real paso B: prefiltra libro5_ms y m5_registro por los tokens de los fills (sufijo de 22 digitos + coma) y filas G. Solo lectura.
SC=$1; OUT=$SC/ext; mkdir -p $OUT; ulimit -v 3000000
L=/mnt/HC_Volume_106538179/libro5_ms
for f in $L/libro5_ms_2026-10-20_379837.csv.gz $L/libro5_ms_2026-10-21_*.csv.gz $L/libro5_ms_2026-10-22_*.csv.gz $L/libro5_ms_2026-10-23_2662.csv.gz $L/libro5_ms_2026-10-23_331840.csv.gz; do
  b=$(basename $f .csv.gz)
  [ -f $OUT/$b.done ] && continue
  L1=$(load=$(cut -d' ' -f2 /proc/loadavg); echo $load)
  zcat $f | tee >(grep -a '^G,' > $OUT/$b.G) | grep -a -F -f $SC/pats.txt > $OUT/$b.txt && touch $OUT/$b.done
  echo "$(date -u +%T) $b $(wc -l < $OUT/$b.txt) load5=$(cut -d' ' -f2 /proc/loadavg)"
done
for d in 20 21 22 23; do
  f=/mnt/HC_Volume_106538179/m5_registro/m5_registro_2026-10-$d.csv.gz; b=m5_$d
  [ -f $OUT/$b.done ] && continue
  zcat $f | grep -a -F -f $SC/pats.txt > $OUT/$b.txt && touch $OUT/$b.done
  echo "$(date -u +%T) $b $(wc -l < $OUT/$b.txt)"
done
echo FIN
