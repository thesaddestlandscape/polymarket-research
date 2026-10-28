#!/bin/bash
cd /root/polymarket-research
ulimit -v 3000000
for d in $(seq -w 5 26); do
  D=2026-10-$d
  [ -s experimentos/5m_barato/escalera_patas_28oct/out/e_$D.csv ] && continue
  L=$(cut -d' ' -f2 /proc/loadavg | cut -d. -f1); while [ "$L" -ge 7 ]; do sleep 60; L=$(cut -d' ' -f2 /proc/loadavg | cut -d. -f1); done
  nice -n 19 ionice -c3 python3 experimentos/5m_barato/escalera_patas_28oct/escalera.py $D >> experimentos/5m_barato/escalera_patas_28oct/run.log 2>&1
done
echo FIN >> experimentos/5m_barato/escalera_patas_28oct/run.log
