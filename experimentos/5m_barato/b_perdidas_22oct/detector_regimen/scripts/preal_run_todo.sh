#!/bin/bash
# Corrida unica P-REAL 05..21-Oct: espera a las 09:00Z, extrae (idempotente), resuelve, audita F-B y analiza. nice 19 ionice -c3, ulimit 3 GB, un solo trabajo.
S=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/scripts; OUT=/root/polymarket-research-datalogs/preal; LOG=$OUT/run_todo.log
ulimit -v 3000000
until [ "$(date -u +%H)" -ge 9 ]; do sleep 20; done
echo "== inicio $(date -u +%FT%TZ)" >> $LOG
for d in 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21; do
  load=$(cut -d' ' -f1 /proc/loadavg | cut -d. -f1); [ "$load" -ge 14 ] && sleep 120
  nice -n 19 ionice -c3 python3 -I $S/preal_extrae.py 2026-10-$d >> $LOG 2>&1 || echo "FALLO extrae $d" >> $LOG
done
nice -n 19 ionice -c3 python3 -I $S/preal_resolver.py --todos >> $LOG 2>&1
nice -n 19 ionice -c3 python3 -I $S/preal_audit_fb.py 2026-10-17 >> $LOG 2>&1
nice -n 19 ionice -c3 python3 -I -u $S/preal_analisis.py --desde 2026-10-05 --hasta 2026-10-21 > $OUT/analisis_05_21.txt 2>&1
echo "== fin $(date -u +%FT%TZ)" >> $LOG
