#!/bin/bash
# Rehace m5_registro y m15_registro del 22-Oct (truncados por un maker_ms corrupto) con el extractor original + tolerancia a zlib.error.
cd "$(dirname "$0")" || exit 1
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
LOG=/mnt/HC_Volume_106538179/agentes_datos/mapa_infra/logs/recupera_registro_$(date -u +%F).log; ulimit -v 3000000
for m in 5min 15min; do
  for i in $(seq 1 60); do l=$(cut -d' ' -f2 /proc/loadavg); [ "$(awk -v l="$l" 'BEGIN{print (l<8.0)?1:0}')" = 1 ] && break; sleep 60; done
  echo "=== $(date -u +%FT%TZ) $m load5=$l" >> "$LOG"
  nice -n 19 ionice -c3 /root/polymarket-research/.venv/bin/python registro_robusto.py 2026-10-22 --marco $m >> "$LOG" 2>&1; echo "rc=$?" >> "$LOG"
done
