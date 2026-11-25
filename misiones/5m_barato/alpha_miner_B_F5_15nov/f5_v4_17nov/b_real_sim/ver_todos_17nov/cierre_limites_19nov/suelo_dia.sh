#!/bin/bash
# suelo_dia.sh DIA -> out/h_DIA.csv (coin,bin10s,d,n) de filas q (bid 0,03-0,45, tokens 5min de las 6 monedas) por RX. Solo lectura de m5_registro. Streaming.
set -o pipefail
D=$1; OUT=$(dirname "$0")/out; REG=/mnt/HC_Volume_106538179/m5_registro; E=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov
DP=$(date -u -d "$D -1 day" +%F); D0=$(( $(date -u -d "$D" +%s) * 1000 ))
KP=""; for f in $E/exp1/cache/k_$DP.csv $E/exp1/cache/add3_k_$DP.csv; do [ -f $f ] && KP="$KP $f"; done
[ -s $OUT/h_$D.csv ] && [ -f $OUT/h_$D.done ] && { echo "$D ya"; exit 0; }
zcat $REG/m5_registro_$D.csv.gz | grep -E '^(q|k),' | nice -n 19 mawk -F, -v D0=$D0 -v D1=$((D0+86400000)) 'BEGIN{OFS=","}
FILENAME!="-"{ if($5=="5min") K[$3]=$4; next }
$1=="k"{ if($5=="5min") K[$3]=$4; next }
$1=="q" && ($3 in K) && $4>=0.03 && $4<=0.45 { rx=$8; if(rx>=D0 && rx<D1){ d=rx-$2; if(d<-50)d=-50; else if(d>400)d=400; H[K[$3] "," int((rx-D0)/10000) "," d]++ } }
END{ for(k in H) print k, H[k] }' $KP - > $OUT/h_$D.csv.tmp && mv $OUT/h_$D.csv.tmp $OUT/h_$D.csv && touch $OUT/h_$D.done && echo "$D ok $(wc -l < $OUT/h_$D.csv)"
