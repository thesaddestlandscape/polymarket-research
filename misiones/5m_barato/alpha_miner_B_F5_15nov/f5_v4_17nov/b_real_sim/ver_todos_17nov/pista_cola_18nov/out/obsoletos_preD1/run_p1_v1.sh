#!/bin/bash
# runner idempotente p1 (RE-B-COLA-CANCELA): un dia cada vez, cola global de pesados, nice19/ionice3, ulimit 3 GB
cd "$(dirname "$0")"
for D in 2026-11-12 2026-11-16 2026-11-14 2026-11-17 2026-11-13 2026-11-15; do
  [ -f out/p1_btc_$D.pkl ] && continue
  for i in $(seq 1 20); do l=$(cut -d' ' -f2 /proc/loadavg); a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
    awk -v l=$l 'BEGIN{exit !(l<4)}' && [ $a -gt 2500 ] && break; sleep 30; done
  h=$(date -u +%H); if [ $h -ge 6 ] && [ $h -lt 9 ]; then echo "franja 06-09Z: paro" ; exit 0; fi
  echo "$(date -u +%FT%TZ) inicio $D load=$(cut -d' ' -f2 /proc/loadavg)" >> out/run_p1.log
  /root/polymarket-research/scripts/cron_pesado.sh bash -c "ulimit -v 3000000; nice -n 19 ionice -c3 python3 p1_dia.py $D btc" >> out/run_p1.log 2>&1
done
echo "$(date -u +%FT%TZ) runner FIN" >> out/run_p1.log
