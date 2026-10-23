#!/bin/bash
# E1b forward (PREREG_E1b_CONFIRMACION_S1.md + ADDENDUM_E1b.md): extraccion diaria IDEMPOTENTE del registro ms archivado (m5/m15_registro del volumen, 60 d),
# simulacion congelada + extras, evaluador V0/V1, conciliacion del maker rebate y A7. SOLO LECTURA: no toca B, procesos, config ni ordenes.
# Cron 11:30Z (fuera de 06-09Z y del horario USA pesado). Heavy: nice 19 + ionice idle + ulimit -v 3 GB (RSS medido 1,5 GB, ~5 min por dia).
cd "$(dirname "$0")" || exit 1
D=${E1B_DIR:-/root/polymarket-research-datalogs/e1b}; D=${D%/}; export E1B_DIR="$D/"; FWD0=${E1B_FWD0:-2026-10-23}; mkdir -p "$D/logs"; LOG="$D/logs/e1b_$(date -u +%F).log"
ulimit -v 3000000
aviso() { /usr/bin/python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e(sys.argv[1])" "$1"; }
H=$(date -u +%H)
if [ "$H" -ge 6 ] && [ "$H" -lt 9 ]; then echo "$(date -u +%FT%TZ) fuera de horario (06-09Z): no se lanza" >> "$LOG"; exit 0; fi
echo "=== $(date -u +%FT%TZ)" >> "$LOG"
# 1) unidades de B (posiciones liquidadas + hora de deteccion) para A3 y el descriptivo de B real: solo lectura del ledger/posiciones.csv
nice -n 19 ionice -c3 /usr/bin/python3 -I unidades_b_e1b.py >> "$LOG" 2>&1 || aviso "⚠️ E1b: unidades_b_e1b FALLÓ (A3/B real usan el CSV anterior). Ver $LOG"
# 2) extraccion + simulacion de los dias forward cerrados que falten (rc 1 = FAILED, 3 = firma nueva de PARTIAL/BLOCKED, 4 = preregistro cambiado)
nice -n 19 ionice -c3 /usr/bin/python3 -I e1b_diario.py run --fwd0 "$FWD0" >> "$LOG" 2>&1; rc=$?
case $rc in
  0) ;;
  3) aviso "⚠️ E1b forward: algun dia forward NO esta COMPLETE (PARTIAL/BLOCKED: cobertura <80 % o fuentes ausentes/corruptas; el registro rota). Ver $LOG y $D/dias/*.json" ;;
  *) aviso "🚨 E1b forward: la extraccion diaria FALLÓ rc=$rc. Ver $LOG. El registro ms 5m se conserva 60 d en el volumen; no se pierde nada si se arregla pronto." ;;
esac
# 3) evaluador (V0 original + V1 addendum). Telegram solo si cambia el veredicto o se cruzan 5 dias validos.
nice -n 19 /usr/bin/python3 -I e1b_eval.py --fwd0 "$FWD0" --json --telegram >> "$LOG" 2>&1 || aviso "🚨 E1b forward: el evaluador FALLÓ. Ver $LOG"
# 4) maker rebate de B (API publica sin autenticacion) + A7 (ledger)
nice -n 19 /usr/bin/python3 -I rebate_maker_check.py --telegram >> "$LOG" 2>&1 || aviso "🚨 E1b: rebate_maker_check FALLÓ. Ver $LOG"
nice -n 19 /usr/bin/python3 -I a7_ledger.py --desde "$FWD0" > "$D/a7_ledger.json" 2>> "$LOG"
find "$D/logs" -name 'e1b_*.log' -mtime +45 -delete
exit 0
