#!/bin/bash
# Una vez: validacion de tp1.dia vs pipeline original (20-Oct) + backfill descriptivo N4 (06..22-Oct). Espera load5<8; 1 hilo; nice 19.
cd "$(dirname "$0")" || exit 1
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1; ulimit -v 3000000
LOG=/mnt/HC_Volume_106538179/agentes_datos/mapa_infra/logs/validacion_$(date -u +%F).log
PY=/root/polymarket-research/.venv/bin/python
espera() { for i in $(seq 1 90); do l=$(cut -d' ' -f2 /proc/loadavg); [ "$(awk -v l="$l" 'BEGIN{print (l<8.0)?1:0}')" = 1 ] && return 0; sleep 60; done; return 1; }
espera || { echo "load5>=8 90 min: BLOCKED" >> "$LOG"; exit 9; }
echo "=== $(date -u +%FT%TZ) valida_tp1 2026-10-20" >> "$LOG"; nice -n 19 ionice -c3 $PY valida_tp1.py 2026-10-20 >> "$LOG" 2>&1; echo "rc=$?" >> "$LOG"
espera || { echo "load5>=8: backfill BLOCKED" >> "$LOG"; exit 9; }
echo "=== $(date -u +%FT%TZ) n4 backfill" >> "$LOG"; nice -n 19 ionice -c3 $PY n4.py backfill >> "$LOG" 2>&1; echo "rc=$?" >> "$LOG"
