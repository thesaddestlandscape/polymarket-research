#!/bin/bash
# Forward R1 (seleccion adversa de B): extraccion on-chain diaria + vigia. SOLO MEDICION, no toca B ni ejecutores. Cron 10:40Z (fuera del racimo 06-09:15Z).
cd "$(dirname "$0")" || exit 1
LOG=/root/polymarket-research-datalogs/sa_r1/cron.log; mkdir -p "$(dirname "$LOG")"
ulimit -v 3000000
aviso() { /usr/bin/python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e('$1')"; }
echo "=== $(date -u +%FT%TZ) extract" >> "$LOG"
nice -n 19 ionice -c3 python3 -I r1_fwd_extract.py >> "$LOG" 2>&1; rc=$?
if [ $rc -ne 0 ] && [ $rc -ne 2 ] && [ $rc -ne 3 ]; then aviso "🚨 R1 forward (selección adversa B): la extracción on-chain FALLÓ rc=$rc. Ver $LOG. El on-chain rota a los 4 días."; fi
# libro WS (registro ms, rota a ~5 d): extraer D-1 y D-2 si faltan y unir rasgos 15m / vol30ws
for k in 1 2; do D=$(date -u -d "-$k day" +%F); \
  [ -f /root/polymarket-research-datalogs/sa_r1/units_$D.csv.gz ] || continue; \
  [ -f /root/polymarket-research-datalogs/sa_ms/ms_$D.npz ] || (ulimit -v 6000000; OMP_NUM_THREADS=1 nice -n 19 ionice -c3 python3 -I ms_extract.py $D >> "$LOG" 2>&1) || aviso "🚨 R1/R2 forward: ms_extract $D FALLÓ (el registro ms rota a ~5 d). Ver $LOG"; \
  [ -f /root/polymarket-research-datalogs/sa_r1/units2_$D.csv.gz ] || [ ! -f /root/polymarket-research-datalogs/sa_ms/ms_$D.npz ] || (ulimit -v 6000000; nice -n 19 ionice -c3 python3 -I r2_fwd_attach.py $D >> "$LOG" 2>&1) || aviso "🚨 R2 forward: r2_fwd_attach $D FALLÓ. Ver $LOG"; done
nice -n 19 ionice -c3 python3 -I r1_fwd_vigia.py --telegram >> "$LOG" 2>&1 || aviso "🚨 R1 forward: el vigía FALLÓ. Ver $LOG"
