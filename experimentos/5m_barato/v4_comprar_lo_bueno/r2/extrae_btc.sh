#!/bin/bash
# Extracción BTC (solo lectura del archivo del volumen) para V4 «comprar lo bueno» ronda 2.
# Por día D: k de m5/m15; filas q/t/l de TODOS los tokens BTC 5min (ventana [C-305 s, C]) y 15min (ventana [C-305 s, C]: último tramo, el de V4) por RECEPCIÓN,
# con clave de grupo C15 (cierre del 15m que contiene al 5m) y ordenadas por (C15) estable; x BTCUSDT del día entero.
# Idempotente: salta días con salida .done. Uso: extrae_btc.sh D1 D2 ...
set -u
ulimit -v 3000000
O=/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno
V=/mnt/HC_Volume_106538179
cd $O
for D in "$@"; do
  [ -f $O/$D.done ] && { echo "$D ya hecho"; continue; }
  echo "$(date -u +%T) $D inicio"
  # k (5min y 15min BTC) -> token,lo,hi,grupo
  ( nice -n 19 ionice -c3 zcat $V/m5_registro/m5_registro_$D.csv.gz | grep -a '^k,' ; nice -n 19 ionice -c3 zcat $V/m15_registro/m15_registro_$D.csv.gz | grep -a '^k,' ) | sort -u > $O/k_$D.csv
  python3 -I - "$O/k_$D.csv" "$O/win_$D.csv" <<'PY'
import sys
from datetime import datetime
seen = {}
for ln in open(sys.argv[1]):
    c = ln.rstrip('\n').split(',')
    if len(c) < 8 or c[3] != 'BTC' or c[4] not in ('5min', '15min'): continue
    C = int(datetime.fromisoformat(c[6]).timestamp())
    if c[4] == '5min': lo, g = (C - 305) * 1000, -(-C // 900) * 900
    else: lo, g = (C - 305) * 1000, C
    seen[c[2]] = (lo, C * 1000, g)
with open(sys.argv[2], 'w') as f:
    for t, (lo, hi, g) in seen.items(): f.write(f'{t},{lo},{hi},{g}\n')
print('tokens BTC', len(seen))
PY
  for M in m5 m15; do
    nice -n 19 ionice -c3 zcat $V/${M}_registro/${M}_registro_$D.csv.gz | nice -n 19 awk -F, -v XF="$O/x_${M}_$D.tmp" '
      NR==FNR {lo[$1]=$2; hi[$1]=$3; g[$1]=$4; next}
      $1=="q" { if (!($3 in g)) next; r=($8!=""?$8:$2); if (r+0>=lo[$3] && r+0<=hi[$3]) print g[$3] "," $0; next }
      $1=="t" { if (!($3 in g)) next; r=($7!=""?$7:$2); if (r+0>=lo[$3] && r+0<=hi[$3]) print g[$3] "," $0; next }
      $1=="l" { if (!($3 in g)) next; r=$10; if (r+0>=lo[$3] && r+0<=hi[$3]) print g[$3] "," $0; next }
      $1=="x" && $3=="BTCUSDT" { print > XF }' $O/win_$D.csv - > $O/rows_${M}_$D.tmp
  done
  # unir, ordenar por grupo (estable) y comprimir
  nice -n 19 sort -t, -k1,1n -s -S 400M -T $O $O/rows_m5_$D.tmp $O/rows_m15_$D.tmp | gzip -1 > $O/rows_$D.csv.gz.tmp && mv $O/rows_$D.csv.gz.tmp $O/rows_$D.csv.gz
  cat $O/x_m5_$D.tmp $O/x_m15_$D.tmp 2>/dev/null | sort -u -t, -k8,8n -k2,2n -S 300M -T $O | gzip -1 > $O/x_$D.csv.gz.tmp && mv $O/x_$D.csv.gz.tmp $O/x_$D.csv.gz
  rm -f $O/rows_m5_$D.tmp $O/rows_m15_$D.tmp $O/x_m5_$D.tmp $O/x_m15_$D.tmp
  echo "$(date -u +%T) $D fin rows=$(zcat $O/rows_$D.csv.gz | wc -l) x=$(zcat $O/x_$D.csv.gz | wc -l)"
  touch $O/$D.done
done
echo FIN_TODO
