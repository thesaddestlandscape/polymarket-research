#!/bin/bash
# x2_extrae_q15.sh -- extrae de maker_ms (20-22 Oct) Binance aggTrade ETH/SOL/XRP (recv,c[7]) y q del 15m YES ETH/SOL/XRP. Solo lectura. Salida fuera de git.
OUT=/root/polymarket-research-datalogs/e1_cancelacion_ms
V=/mnt/HC_Volume_106538179/datalogs_auto
echo "inicio $(date -u +%FT%TZ)" > $OUT/x2.log
for f in maker_ms_2026-10-20_149871 maker_ms_2026-10-20_174318 maker_ms_2026-10-20_196560 maker_ms_2026-10-20_264769 maker_ms_2026-10-20_305136 \
         maker_ms_2026-10-21_379837 maker_ms_2026-10-21_519294 maker_ms_2026-10-21_575255 maker_ms_2026-10-21_641466 maker_ms_2026-10-21_696748 maker_ms_2026-10-21_734552 \
         maker_ms_2026-10-22_822520 maker_ms_2026-10-22_887720 maker_ms_2026-10-22_950547 maker_ms_2026-10-22_986560 maker_ms_2026-10-22_2662; do
  [ -s $OUT/$f.q2.gz ] && continue
  zcat $V/$f.csv.gz 2>>$OUT/x2.log | awk -F, -v fx="$OUT/$f.x.tmp" -v fq="$OUT/$f.q.tmp" '
    $1=="k" && $5=="15min" && $8=="YES" && ($4=="ETH"||$4=="SOL"||$4=="XRP") {K[$3]=$4; print "k,"$3","$4","$6","$7 > fq; next}
    $1=="x" {next}
    $1=="q" && ($3 in K) {print "q,"$8","$3","$4","$5 > fq}'
  gzip -c $OUT/$f.q.tmp > $OUT/$f.q2.gz && rm -f $OUT/$f.x.tmp $OUT/$f.q.tmp
  echo "$f ok $(date -u +%FT%TZ)" >> $OUT/x2.log
done
echo "fin $(date -u +%FT%TZ)" >> $OUT/x2.log
