#!/bin/bash
# Extraccion DOGE/BNB (H60 adenda 21-Oct; clon de extrae_alts.sh) (solo lectura del archivo del volumen) para el replay H23 v2 (H60/H68). Clon de v4_comprar_lo_bueno/r2/extrae_btc.sh con salida por moneda
# (rows_<COIN>_<D>.csv.gz, k_<COIN>_<D>.csv) y SIN x (Binance solo hace falta en BTC). Ventana [C-305 s, C] por RECEPCION, clave de grupo = C15.
# Idempotente (marca <D>.dogebnb.done). Uso: extrae_alts.sh D1 D2 ...   (nice 19, ionice 3, ulimit 3 GB)
set -u
ulimit -v 3000000
O=/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/alts
V=/mnt/HC_Volume_106538179
mkdir -p $O; cd $O
for D in "$@"; do
  [ -f $O/$D.dogebnb.done ] && { echo "$D ya hecho"; continue; }
  echo "$(date -u +%T) $D inicio"
  ( nice -n 19 ionice -c3 zcat $V/m5_registro/m5_registro_$D.csv.gz | grep -a '^k,' ; nice -n 19 ionice -c3 zcat $V/m15_registro/m15_registro_$D.csv.gz | grep -a '^k,' ) | sort -u > $O/kall2_$D.csv
  python3 -I - "$O/kall2_$D.csv" "$O/win2_$D.csv" "$O" "$D" <<'PY'
import sys
from datetime import datetime
seen = {}; out = {c: open(f'{sys.argv[3]}/k_{c}_{sys.argv[4]}.csv', 'w') for c in ('DOGE', 'BNB')}
for ln in open(sys.argv[1]):
    c = ln.rstrip('\n').split(',')
    if len(c) < 8 or c[3] not in out or c[4] not in ('5min', '15min'): continue
    out[c[3]].write(ln)
    C = int(datetime.fromisoformat(c[6]).timestamp())
    g = -(-C // 900) * 900 if c[4] == '5min' else C
    seen[c[2]] = ((C - 305) * 1000, C * 1000, g, c[3])
with open(sys.argv[2], 'w') as f:
    for t, (lo, hi, g, co) in seen.items(): f.write(f'{t},{lo},{hi},{g},{co}\n')
print('tokens', len(seen))
PY
  for M in m5 m15; do
    nice -n 19 ionice -c3 zcat $V/${M}_registro/${M}_registro_$D.csv.gz | nice -n 19 awk -F, -v O="$O" -v M="$M" -v D="$D" '
      NR==FNR {lo[$1]=$2; hi[$1]=$3; g[$1]=$4; co[$1]=$5; next}
      $1=="q" { if (!($3 in g)) next; r=($8!=""?$8:$2); if (r+0>=lo[$3] && r+0<=hi[$3]) print g[$3] "," $0 > (O "/rows_" co[$3] "_" M "_" D ".tmp"); next }
      $1=="t" { if (!($3 in g)) next; r=($7!=""?$7:$2); if (r+0>=lo[$3] && r+0<=hi[$3]) print g[$3] "," $0 > (O "/rows_" co[$3] "_" M "_" D ".tmp"); next }
      $1=="l" { if (!($3 in g)) next; r=$10; if (r+0>=lo[$3] && r+0<=hi[$3]) print g[$3] "," $0 > (O "/rows_" co[$3] "_" M "_" D ".tmp"); next }' $O/win2_$D.csv -
  done
  for CO in DOGE BNB; do
    nice -n 19 sort -t, -k1,1n -s -S 300M -T $O $O/rows_${CO}_m5_$D.tmp $O/rows_${CO}_m15_$D.tmp 2>/dev/null | gzip -1 > $O/rows_${CO}_$D.csv.gz.tmp && mv $O/rows_${CO}_$D.csv.gz.tmp $O/rows_${CO}_$D.csv.gz
    rm -f $O/rows_${CO}_m5_$D.tmp $O/rows_${CO}_m15_$D.tmp
  done
  rm -f $O/kall2_$D.csv
  echo "$(date -u +%T) $D fin: $(ls -la $O/rows_*_$D.csv.gz | awk '{printf "%s=%d ", $9, $5}')"
  touch $O/$D.dogebnb.done
done
echo FIN_DOGEBNB
