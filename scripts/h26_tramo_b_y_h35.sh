#!/bin/bash
# 17-Oct (OK Javi "haz la 1 y la 2"): tras aceptar el control 'primeras K acciones' como criterio v2 de calibración
# (DECISION_LOG 10:25Z, no preregistrado), corre en cadena -- un pesado a la vez -- el tramo B del simulador maker banda
# (05-15 Oct, motores C0, reutiliza cachés del tramo A; SIN --exigir-calibracion, porque el criterio v1 compara objetos
# distintos) y después H35 DEEP_PEG. Solo lectura, sin órdenes. Reintenta cada 10 min si la carga lo bloquea.
cd /root/polymarket-research || exit 1
LOG=/root/polymarket-research/logs/h26_tramo_b_y_h35.log
OUT=/root/polymarket-research-datalogs/m5barato_mision/h26_sim_calibracion
esperar_hueco() {
  while true; do
    HM=$((10#$(date -u +%H)*60 + 10#$(date -u +%M)))
    LOAD=$(cut -d' ' -f1 /proc/loadavg | cut -d. -f1)
    MEM=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
    if { [ "$HM" -lt 360 ] || [ "$HM" -ge 555 ]; } && [ "$LOAD" -lt 16 ] && [ "$MEM" -gt 1500 ]; then return 0; fi
    echo "$(date -u +%FT%TZ) espera (load=$LOAD mem=${MEM}MB)" >> "$LOG"; sleep 600
  done
}
esperar_hueco
DIAS=$(python3 -c "print(','.join(f'2026-10-{d:02d}' for d in range(5,16)))")
echo "$(date -u +%FT%TZ) INICIO tramo B ($DIAS)" >> "$LOG"
( ulimit -v 3000000; nice -n 19 ionice -c3 python3 analisis_5m_maker_banda_simulador.py --dias "$DIAS" --capas C0 --sh-cap 25,50 --sin-placebo --out "$OUT" ) >> "$LOG" 2>&1
echo "$(date -u +%FT%TZ) FIN tramo B rc=$?" >> "$LOG"
esperar_hueco
echo "$(date -u +%FT%TZ) INICIO H35" >> "$LOG"
bash scripts/h35_deep_peg_corrida.sh >> "$LOG" 2>&1
echo "$(date -u +%FT%TZ) FIN H35 rc=$?" >> "$LOG"
