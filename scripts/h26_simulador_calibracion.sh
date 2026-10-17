#!/bin/bash
# H26 simulador maker banda barata -- FASE CALIBRACIÓN (solo motores C0: JOIN/IMPROVE cola CONS/OPT SH=5 + capacidad SH 25/50).
# Sin guardas Binance ni placebo (sus parámetros Λ/k/W los congela H26-MS). Dos tramos con parada intermedia:
#   A) 05,06,07-Oct con --exigir-calibracion: si el veredicto no PASA (población H5M 'final de la cola' fuera del haz
#      [EV CONS - 0,05, EV OPT + 0,05]) sale con código 4 y NO sigue (el simulador está mal).
#   B) 05..15-Oct (reutiliza las cachés de A, idempotente) con --exigir-calibracion sobre DESC y OOS.
# SOLO LECTURA: no manda órdenes ni firma. Nunca 06:00-09:15Z ni con load>=16 (el propio script lo comprueba y sale con 3).
# Uso: setsid nohup bash scripts/h26_simulador_calibracion.sh > /dev/null 2>&1 &
cd /root/polymarket-research || exit 1
OUT=/root/polymarket-research-datalogs/m5barato_mision/h26_sim_calibracion
LOG=/root/polymarket-research/logs/h26_sim_calibracion.log
mkdir -p "$OUT"
HM=$((10#$(date -u +%H)*60 + 10#$(date -u +%M)))
# franja de crons 06:00-09:15Z (el chief amplió a 09:15 el 17-Oct por saturación de CPU/swap)
if [ "$HM" -ge 360 ] && [ "$HM" -lt 555 ]; then echo "$(date -u +%FT%TZ) BLOCKED franja 06:00-09:15Z" >> "$LOG"; exit 3; fi
# carga: no arrancar con la cola de CPU saturada
LOAD=$(cut -d' ' -f1 /proc/loadavg | cut -d. -f1)
if [ "$LOAD" -ge 16 ]; then echo "$(date -u +%FT%TZ) BLOCKED load=$LOAD >= 16" >> "$LOG"; exit 3; fi
ulimit -v 3000000
COMUN="--capas C0 --sh-cap 25,50 --sin-placebo --exigir-calibracion --out $OUT"
echo "$(date -u +%FT%TZ) INICIO tramo A (05-07 Oct)" >> "$LOG"
nice -n 19 ionice -c3 python3 analisis_5m_maker_banda_simulador.py --dias 2026-10-05,2026-10-06,2026-10-07 $COMUN >> "$LOG" 2>&1
RC=$?
echo "$(date -u +%FT%TZ) FIN tramo A rc=$RC" >> "$LOG"
if [ "$RC" -ne 0 ]; then echo "$(date -u +%FT%TZ) PARADA tras tramo A (rc=$RC): no se lanza el tramo B" >> "$LOG"; exit "$RC"; fi
DIAS=$(python3 -c "print(','.join(f'2026-10-{d:02d}' for d in range(5,16)))")
echo "$(date -u +%FT%TZ) INICIO tramo B ($DIAS)" >> "$LOG"
nice -n 19 ionice -c3 python3 analisis_5m_maker_banda_simulador.py --dias "$DIAS" $COMUN >> "$LOG" 2>&1
RC=$?
echo "$(date -u +%FT%TZ) FIN tramo B rc=$RC" >> "$LOG"
exit "$RC"
