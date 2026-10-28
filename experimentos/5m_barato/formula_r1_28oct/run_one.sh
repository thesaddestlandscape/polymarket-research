#!/bin/bash
D=$1
cd /root/polymarket-research/experimentos/5m_barato/formula_r1_28oct
[ -s out/f_$D.csv.gz ] && exit 0
ulimit -v 3000000
while :; do
  L=$(cut -d' ' -f1 /proc/loadavg | cut -d. -f1); M=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
  [ "$L" -lt 14 ] && [ "$M" -gt 1200 ] && break; sleep 30
done
nice -n 19 ionice -c3 python3 extract.py $D >> run.log 2>&1
