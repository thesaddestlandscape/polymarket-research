#!/bin/bash
# espera (max 100 min) a que acaben 19 y 20 Oct en el log de extraccion
LOG=/mnt/HC_Volume_106538179/datalogs_analisis_caches/h55_forward/extraccion.log
for i in $(seq 1 100); do
  if grep -q "fin 2026-10-19" $LOG 2>/dev/null && grep -q "fin 2026-10-20" $LOG 2>/dev/null; then exit 0; fi
  sleep 60
done
exit 1
