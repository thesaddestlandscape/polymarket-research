#!/bin/bash
D=$1
cd /root/polymarket-research/experimentos/5m_barato/formula_r2_28oct || exit 1
[ -s out/s_$D.csv.gz ] && exit 0
for i in $(seq 1 120); do
  L1=$(cut -d' ' -f1 /proc/loadavg | cut -d. -f1); M=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
  if [ "$L1" -lt 14 ] && [ "$M" -gt 1200 ]; then break; fi
  sleep 20
done
export AWKBIN=mawk OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
ulimit -v 4500000
nice -n 19 ionice -c3 python3 sim2.py --dia $D >> run2.log 2>&1 || echo "FALLO $D" >> run2.log
