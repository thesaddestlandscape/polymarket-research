#!/bin/bash
# Ronda 3 V4 "comprar lo bueno": simulación por día (sim_dia3) y rival_re, UNO A UNO, con guardas de recursos.
# Guardas: load5<16, MemAvailable>2,5 GB, fuera de 06:00-09:15Z y 22:15-22:30Z. Idempotente (los scripts saltan lo ya hecho).
R=/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r3
O=/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno
mkdir -p $O/r3_out
espera() {
  while true; do
    l5=$(awk '{print int($2)}' /proc/loadavg); ma=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); h=$(date -u +%H%M)
    if [ $l5 -lt 16 ] && [ $ma -gt 2500 ] && { [ $h -lt 0600 ] || [ $h -gt 0915 ]; } && { [ $h -lt 2215 ] || [ $h -gt 2230 ]; }; then return; fi
    echo "$(date -u +%T) espera load5=$l5 mem=${ma}MB" >> $O/r3_out/espera.log; sleep 90
  done
}
cd $R
for D in 2026-10-16 2026-10-17 2026-10-18 2026-10-13 2026-10-14 2026-10-15 2026-10-10 2026-10-11 2026-10-12 2026-10-09 2026-10-08 2026-10-07 2026-10-06; do
  espera; echo "$(date -u +%T) sim $D" >> $O/r3_out/log.txt
  ( ulimit -v 3000000; nice -n 19 ionice -c3 python3 -I sim_dia3.py $D >> $O/r3_out/log.txt 2>&1 )
done
for D in 2026-10-16 2026-10-17 2026-10-18 2026-10-13 2026-10-14 2026-10-15 2026-10-10 2026-10-11 2026-10-12 2026-10-09; do
  espera; echo "$(date -u +%T) rival $D" >> $O/r3_out/log.txt
  ( ulimit -v 3000000; nice -n 19 ionice -c3 python3 -I rival_re.py $D >> $O/r3_out/log.txt 2>&1 )
done
echo "$(date -u +%T) FIN_R3" >> $O/r3_out/log.txt
