#!/bin/bash
# Driver H23 v3 (offline, solo lectura salvo sus propias salidas). UN job, secuencial, idempotente. Orden: (1) extraer BTC 19-20 Oct (r2/extrae_btc.sh, idempotente);
# (2) replay v3 OOS 19-20; (3) replay del dia de validacion (13-Oct) y validacion vs v2; (4) replay del resto de 06-18; (5) analisis.
# Guardas: nunca 06:00-09:15Z; MemAvailable>1,8 GB (suelo duro, guard_ram reinicia <900 MB); load5<20; el job DOGE/BNB esta en SIGSTOP (el chief): no compite.
# Log con hora en $OUT/run_v3.log. Estado en $OUT/run_manifest.json. Reanudable: relanzar el mismo comando salta lo hecho.
Z=/root/polymarket-research/experimentos/5m_barato/h23_maker/v3
R2=/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r2
OUT=/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3
OOS="2026-10-19 2026-10-20"
VAL="2026-10-13"
DISC="2026-10-06 2026-10-07 2026-10-08 2026-10-09 2026-10-10 2026-10-11 2026-10-12 2026-10-14 2026-10-15 2026-10-16 2026-10-17 2026-10-18"
mkdir -p $OUT; cd $Z || exit 1
log() { echo "$(date -u +%FT%TZ) $*" >> $OUT/run_v3.log; }
estado() { python3 -I $Z/manifest_v3.py "$1" "${2:-}" >> $OUT/run_v3.log 2>&1; }
espera() {  # $1 = etiqueta ; hasta 8 h
  for i in $(seq 1 480); do
    h=$(date -u +%H%M); mem=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); l5=$(awk '{print int($2)}' /proc/loadavg)
    otro=$(pgrep -f '^bash run_v2_dogebnb.sh' | wc -l)
    if { [ "$h" -lt 0600 ] || [ "$h" -ge 0915 ]; } && [ "$mem" -gt 1800 ] && [ "$l5" -lt 20 ]; then return 0; fi
    sleep 60
  done
  log "BLOCKED $1 (h=$h mem=$mem l5=$l5 otro_job=$otro)"; return 1
}
estado inicio "arranque; esperando ventana/recursos"
for D in $OOS; do
  espera "extrae $D" || { estado BLOCKED "extrae $D"; exit 4; }
  ( nice -n 19 ionice -c3 bash $R2/extrae_btc.sh $D ) >> $OUT/run_v3.log 2>&1 || { log "ERROR extrae $D"; estado FAILED "extrae $D"; exit 5; }
  estado paso "extracto $D"
done
for D in $OOS $VAL $DISC; do
  espera "sim $D" || { estado BLOCKED "sim $D"; exit 4; }
  ( ulimit -v 2200000; nice -n 19 ionice -c3 python3 -I $Z/h23_sim_v3.py $D ) >> $OUT/run_v3.log 2>&1 || { log "ERROR sim $D"; estado FAILED "sim $D"; exit 5; }
  estado paso "sim $D"
  if [ "$D" = "$VAL" ]; then python3 -I $Z/h23_valida_v3.py $VAL >> $OUT/run_v3.log 2>&1 || { log "VALIDACION FALLA"; estado FAILED "validacion v2 vs v3 en $VAL"; exit 6; }; fi
done
python3 -I $Z/h23_analisis_v3.py > $OUT/analisis_v3.txt 2>> $OUT/run_v3.log
estado fin "analisis en $OUT/analisis_v3.txt"
log fin
