#!/bin/bash
# H35 DEEP_PEG (+H37 +H38) -- corrida completa del motor NUEVO analisis_5m_maker_banda_deep_peg.py (DESC 05-10 Oct, OOS 14-16 Oct; 11-13 excluidos).
# SOLO LECTURA: no manda órdenes ni firma. Cachés en OTRO directorio que la calibración H26 (no toca scripts/h26_simulador_calibracion.sh).
# Un único trabajo pesado a la vez: NO lanzar mientras corra la calibración H26 ni entre 06:00 y 09:15Z (el script lo comprueba) ni con load>=16.
# Reanudable e idempotente (caché por día con hash de código+parámetros): relanzar el mismo comando continúa donde murió.
# Uso: setsid nohup bash scripts/h35_deep_peg_corrida.sh > /dev/null 2>&1 &
cd /root/polymarket-research || exit 1
OUT=/root/polymarket-research-datalogs/m5_maker_banda_deep_peg
LOG=/root/polymarket-research/logs/h35_deep_peg.log
mkdir -p "$OUT"
HM=$((10#$(date -u +%H)*60 + 10#$(date -u +%M)))
if [ "$HM" -ge 360 ] && [ "$HM" -lt 555 ]; then echo "$(date -u +%FT%TZ) BLOCKED franja 06:00-09:15Z" >> "$LOG"; exit 3; fi
LOAD=$(cut -d' ' -f1 /proc/loadavg | cut -d. -f1)
if [ "$LOAD" -ge 16 ]; then echo "$(date -u +%FT%TZ) BLOCKED load=$LOAD >= 16" >> "$LOG"; exit 3; fi
ulimit -v 3000000
echo "$(date -u +%FT%TZ) INICIO H35 DEEP_PEG" >> "$LOG"
nice -n 19 ionice -c3 python3 analisis_5m_maker_banda_deep_peg.py --out "$OUT" >> "$LOG" 2>&1
RC=$?
echo "$(date -u +%FT%TZ) FIN rc=$RC" >> "$LOG"
exit "$RC"
