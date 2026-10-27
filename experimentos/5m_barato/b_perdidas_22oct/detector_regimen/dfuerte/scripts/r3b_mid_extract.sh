#!/bin/bash
# extrae cotizaciones q de tokens 5min y 15min en las ventanas de segundo-dentro-de-slot [270,300)U[0,1)U[120,181) -> mid/<dia>.csv.gz
D=/mnt/HC_Volume_106538179/agentes_datos/dfuerte; SRC=/mnt/HC_Volume_106538179/m5_registro
for d in 2026-10-05 2026-10-06 2026-10-07 2026-10-08 2026-10-09 2026-10-10 2026-10-11 2026-10-12 2026-10-13 2026-10-14 2026-10-15 2026-10-16 2026-10-17 2026-10-18 2026-10-19 2026-10-20 2026-10-21; do
  while [ "$(cut -d. -f1 /proc/loadavg | cut -d. -f1)" -gt 9 ]; do sleep 30; done
  f=$SRC/m5_registro_$d.csv.gz; [ -f $D/mid/$d.csv.gz ] && continue
  zcat $f | awk -F, '$1=="k" && ($5=="5min"||$5=="15min"){print $3","$4","$5","$6","$7}' > $D/mid/tok_$d.csv
  zcat $f | awk -F, 'NR==FNR{tok[$1]=1;next} $1=="q" && ($3 in tok){s=($2/1000)%300; if (s>=270||s<1||(s>=120&&s<181)) print $2","$3","$4","$5}' $D/mid/tok_$d.csv - | gzip > $D/mid/$d.csv.gz.tmp && mv $D/mid/$d.csv.gz.tmp $D/mid/$d.csv.gz
  echo $d $(date -u +%T) >> $D/mid/log.txt
done
echo FIN >> $D/mid/log.txt
