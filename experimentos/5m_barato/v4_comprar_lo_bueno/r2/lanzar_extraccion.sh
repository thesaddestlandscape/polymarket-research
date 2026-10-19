#!/bin/bash
# Lanza extrae_btc.sh día a día solo cuando la máquina lo permite: load5<12, MemAvailable>2,5 GB, fuera de 06:00-09:15Z
# y sin otro descompresor (gzip/zcat) de otro agente corriendo. Log: v4_comprar_lo_bueno/extraccion.log en el volumen.
R=/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r2
O=/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno
for D in 2026-10-16 2026-10-17 2026-10-18 2026-10-13 2026-10-14 2026-10-15 2026-10-10 2026-10-11 2026-10-12 2026-10-07 2026-10-08 2026-10-09 2026-10-06; do
  while true; do
    l5=$(awk '{print int($2)}' /proc/loadavg); ma=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
    h=$(date -u +%H%M); ng=$(ps -eo comm | grep -c -E '^(gzip|zcat)$')
    if [ $l5 -lt 12 ] && [ $ma -gt 2500 ] && { [ $h -lt 0600 ] || [ $h -gt 0915 ]; } && [ $ng -eq 0 ]; then break; fi
    echo "$(date -u +%T) espera load5=$l5 mem=${ma}MB gz=$ng" >> $O/espera.log; sleep 60
  done
  bash $R/extrae_btc.sh $D >> $O/extraccion.log 2>&1
done
echo TODO_HECHO >> $O/extraccion.log
