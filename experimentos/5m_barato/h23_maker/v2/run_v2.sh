#!/bin/bash
# Driver H23 v2 (offline). UN job, secuencial, idempotente. Fases: (1) replay BTC con re-puja 0..1500 ms; (2) extraccion ETH/SOL/XRP; (3) replay alts.
# Guardas: fuera de 06:00-09:15Z; espera load5<20 y MemAvailable>2,5 GB (hasta 4 h por tarea). Log con hora en $OUT/run_v2.log. Estado en $OUT/run_manifest.json.
Z=/root/polymarket-research/experimentos/5m_barato/h23_maker/v2
OUT=/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2
DIAS="2026-10-06 2026-10-07 2026-10-08 2026-10-09 2026-10-10 2026-10-11 2026-10-12 2026-10-13 2026-10-14 2026-10-15 2026-10-16 2026-10-17 2026-10-18"
cd $Z || exit 1
log() { echo "$(date -u +%FT%TZ) $*" >> $OUT/run_v2.log; }
estado() { python3 -I $Z/manifest_v2.py "$1" "${2:-}" >> $OUT/run_v2.log 2>&1; }
espera() {  # $1 = etiqueta
  for i in $(seq 1 240); do
    h=$(date -u +%H%M); mem=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); l5=$(awk '{print int($2)}' /proc/loadavg)
    if { [ "$h" -lt 0600 ] || [ "$h" -ge 0915 ]; } && [ "$mem" -gt 2500 ] && [ "$l5" -lt 20 ]; then return 0; fi
    sleep 60
  done
  log "BLOCKED $1 (h=$h mem=$mem l5=$l5)"; return 1
}
estado inicio
for D in $DIAS; do
  espera "btc $D" || { estado BLOCKED "btc $D"; exit 4; }
  ( ulimit -v 3000000; nice -n 19 ionice -c3 python3 -I $Z/h23_sim_v2.py BTC $D ) >> $OUT/run_v2.log 2>&1 || log "ERROR btc $D"
done
estado fase1_ok
for D in $DIAS; do
  espera "extrae $D" || { estado BLOCKED "extrae $D"; exit 4; }
  bash $Z/extrae_alts.sh $D >> $OUT/run_v2.log 2>&1 || log "ERROR extrae $D"
  for CO in ETH SOL XRP; do
    espera "alts $CO $D" || { estado BLOCKED "alts $CO $D"; exit 4; }
    ( ulimit -v 3000000; export H23V2_IN=$OUT/alts/; nice -n 19 ionice -c3 python3 -I $Z/h23_sim_v2.py $CO $D ) >> $OUT/run_v2.log 2>&1 || log "ERROR alts $CO $D"
  done
done
estado fin
