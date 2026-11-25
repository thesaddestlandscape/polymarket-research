#!/bin/bash
# espera MemAvailable >= 3,4 GB y fuera de 06:00-09:30Z; un dia cada vez (cache eventos_<D>.pkl idempotente)
cd /root/polymarket-research/experimentos/5m_barato/replay_brecha_B_16nov/fn_16nov
for d in 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do
  while true; do
    m=$(awk '/MemAvailable/{print $2}' /proc/meminfo); h=$(date -u +%H%M)
    if [ "$m" -ge 3400000 ] && { [ "$h" -lt 0600 ] || [ "$h" -gt 0930 ]; }; then break; fi
    sleep 30
  done
  echo "$(date -u +%FT%TZ) $d MemAvail $m" >> run_f3.log
  (ulimit -v 3600000; nice -n 19 ionice -c3 /usr/bin/time -f "%e s %U user %M KB" timeout 600 python3 -I f3_evento_vacio.py $d) >> run_f3.log 2>&1
done
(ulimit -v 3600000; nice -n 19 python3 -I f3_evento_vacio.py) > f3_final.log 2>&1
echo "$(date -u +%FT%TZ) FIN" >> run_f3.log
