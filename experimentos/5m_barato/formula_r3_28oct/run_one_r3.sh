#!/bin/bash
# uso: run_one_r3.sh DIA   (guard: load1<14 y MemAvailable>1200 MB; nice 19; ulimit 4,5 GB)
D=$1
cd /root/polymarket-research/experimentos/5m_barato/formula_r3_28oct || exit 1
if [ -s "out/f_${D}.npz" ]; then echo "OK_YA $D" >> run3.log; exit 0; fi
for i in $(seq 1 90); do
  L=$(cut -d' ' -f1 /proc/loadavg); M=$(awk '/MemAvailable/ {print int($2/1024)}' /proc/meminfo)
  if awk -v l="$L" 'BEGIN{exit !(l<14)}' && [ "$M" -gt 1200 ]; then break; fi
  sleep 20
done
ulimit -v 4500000
AWKBIN=mawk nice -n 19 ionice -c3 python3 feat3.py --dia "$D" >> run3.log 2>&1
echo "FIN_DIA $D rc=$?" >> run3.log
