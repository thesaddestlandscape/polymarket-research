#!/bin/bash
# Pasada unica por fichero libro5_ms: cuentas por segundo y tipo (B/d/T/G) + todas las filas G. Solo lectura.
D=/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/huecos_causa_13nov/out
for f in "$@"; do
  b=$(basename $f .csv.gz)
  nice -n 19 ionice -c3 zcat "$f" 2>/dev/null | nice -n 19 awk -v G="$D/${b}.G.txt" -v S="$D/${b}.seg.csv" '
    { ty=substr($0,1,1); s=substr($0,3,10); c[s","ty]++; if (ty=="G") print $0 > G }
    END { for (k in c) print k","c[k] > S }'
  echo "hecho $b" >> $D/seg_g.log
done
