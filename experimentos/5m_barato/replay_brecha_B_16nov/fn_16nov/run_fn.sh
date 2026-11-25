#!/bin/bash
# espera a que termine run_f3 (FIN en su log), luego verif_fn 4 dias con puerta de RAM (>=3,4 GB) y horario (fuera 06:00-09:30Z); idempotente (salta V3_<D>.pkl existente)
cd /root/polymarket-research/experimentos/5m_barato/replay_brecha_B_16nov/fn_16nov
until grep -q FIN run_f3.log 2>/dev/null; do sleep 20; done
for d in 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do
  while true; do
    m=$(awk '/MemAvailable/{print $2}' /proc/meminfo); h=$(date -u +%H%M)
    if [ "$m" -ge 3400000 ] && { [ "$h" -lt 0600 ] || [ "$h" -gt 0930 ]; }; then break; fi
    sleep 30
  done
  echo "$(date -u +%FT%TZ) $d MemAvail $m" >> run_fn.log
  (ulimit -v 3600000; nice -n 19 ionice -c3 /usr/bin/time -f "%e s %U user %M KB" timeout 600 python3 -I verif_fn.py $d) >> run_fn.log 2>&1
done
python3 -I f5_metricas.py > f5.log 2>&1
echo "$(date -u +%FT%TZ) FIN" >> run_fn.log
