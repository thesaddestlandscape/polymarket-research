#!/bin/bash
# x3_extrae_registro.sh -- de VOL/m5_registro_D (05-23 Oct): k 5min ETH/SOL/XRP, t de esos tokens, x Binance ETH/SOL/XRP. Solo lectura. Reanudable por dia.
OUT=/root/polymarket-research-datalogs/e1_cancelacion_ms/reg; mkdir -p $OUT; V=/mnt/HC_Volume_106538179/m5_registro
echo "inicio $(date -u +%FT%TZ)" >> $OUT/x3.log
for f in $(ls $V/m5_registro_2026-10-*.csv.gz | sort -r); do
  d=$(basename $f .csv.gz | sed 's/m5_registro_//'); [ -s $OUT/$d.gz ] && continue
  zcat $f 2>>$OUT/x3.log | awk -F, '
    $1=="k" && $5=="5min" && ($4=="ETH"||$4=="SOL"||$4=="XRP") {K[$3]=1; print; next}
    $1=="x" && ($3=="ETHUSDT"||$3=="SOLUSDT"||$3=="XRPUSDT") {print "x,"$8","substr($3,1,3)","$4; next}
    $1=="t" {print "t,"$7","$3","$4","$5","$6}' | gzip -c > $OUT/$d.tmp.gz && mv $OUT/$d.tmp.gz $OUT/$d.gz
  echo "$d ok $(date -u +%FT%TZ)" >> $OUT/x3.log
done
echo "fin $(date -u +%FT%TZ)" >> $OUT/x3.log
