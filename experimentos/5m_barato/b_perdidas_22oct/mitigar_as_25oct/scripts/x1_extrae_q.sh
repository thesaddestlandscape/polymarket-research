#!/bin/bash
# x1_extrae_q.sh -- PREREG_A1: filas q de tokens 5m ETH/SOL/XRP (lista tokens.csv) con bid en [0,03,0,45], de VOL/m5_registro_D 06..23-Oct.
# Salida DL/mitigar_as_25oct/q_D.gz: id,recv,bid,ask,tb,ta. Solo lectura, reanudable por dia.
OUT=/root/polymarket-research-datalogs/mitigar_as_25oct; V=/mnt/HC_Volume_106538179/m5_registro
for d in $(seq -w 6 23); do D=2026-10-$d; [ -s $OUT/q_$D.gz ] && continue
  zcat $V/m5_registro_$D.csv.gz 2>>$OUT/x1.err | awk -F, 'NR==FNR{id[$1]=$2; next} $1=="q" && ($3 in id) && $4>=0.03 && $4<=0.45 {print id[$3]","$8","$4","$5","$6","$7}' $OUT/tokens.csv - | gzip -c > $OUT/q_$D.tmp.gz && mv $OUT/q_$D.tmp.gz $OUT/q_$D.gz
  echo "$D ok $(date -u +%FT%TZ) $(stat -c %s $OUT/q_$D.gz)" >> $OUT/x1.log
done
echo fin >> $OUT/x1.log
