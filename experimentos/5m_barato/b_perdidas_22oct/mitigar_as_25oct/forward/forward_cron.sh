#!/bin/bash
# forward_cron.sh -- cron diario del forward pasivo A1/F5 (mitigar_as_25oct). SOLO LECTURA, sin dinero real. Nunca 06-09Z; solo con load5<4 (si no, reintenta mañana: idempotente).
# Procesa los dias nuevos >=24-Oct elegibles (fichero m5_registro_D cerrado) y regenera forward_diario.csv + RESUMEN.md. Log: datalogs/mitigar_as_25oct/forward/cron.log
cd "$(dirname "$0")" || exit 1
LOG=/root/polymarket-research-datalogs/mitigar_as_25oct/forward/cron.log; mkdir -p "$(dirname "$LOG")"
H=$(date -u +%H)
if [ "$H" -ge 6 ] && [ "$H" -lt 9 ]; then echo "=== $(date -u +%FT%TZ) fuera de horario (06-09Z): no se lanza" >> "$LOG"; exit 0; fi
if ! python3 -c "import os,sys; sys.exit(0 if os.getloadavg()[1]<4 else 1)"; then echo "=== $(date -u +%FT%TZ) load5>=4: no se lanza ($(cut -d' ' -f1-3 /proc/loadavg))" >> "$LOG"; exit 0; fi
aviso() { /usr/bin/python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e(sys.argv[1])" "$1"; }
echo "=== $(date -u +%FT%TZ) inicio" >> "$LOG"
ulimit -v 3000000
nice -n 19 ionice -c3 python3 -I forward_a1.py todo >> "$LOG" 2>&1; rc=$?
[ $rc -eq 0 ] && { nice -n 19 ionice -c3 python3 -I ../forward_r1/forward_r1.py >> "$LOG" 2>&1; rc=$?; }   # R1 (E1D reparado) lee las caches del extractor unico: no relee m5_registro
echo "=== $(date -u +%FT%TZ) fin rc=$rc" >> "$LOG"
[ $rc -ne 0 ] && aviso "⚠️ forward A1/F5 (mitigar_as_25oct) rc=$rc. Ver $LOG"
exit $rc
