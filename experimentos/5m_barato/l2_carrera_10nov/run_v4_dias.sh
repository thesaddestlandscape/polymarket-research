#!/bin/bash
# run_v4_dias.sh [DIA...]  (27-Nov, engineer 5m barato) -- genera sa_ms2/ms2_D.npz (ms_extract_v2.py) y out_v4/RT_v3dd_D.pkl (passT_v4.py v3 dd D) para los dias pedidos.
# Sin argumentos: dias >= $DESDE (def. 2026-11-25) hasta ayer, con tape_D.pkl+bad_D.json (precursores_barrido/out) y SIN RT_v3dd_D.pkl. Idempotente (no rehace lo existente).
# NO toca passT_v4.py (sello) ni run_v4_validacion.sh (su sha esta en V4_SHA256.txt). Cada paso = 1 job por scripts/cron_pesado.sh (cola global + cgroup), nice 19, ionice -c3, nunca 06:00-09:15Z.
# Picos medidos 27-Nov (dia 25): ms_extract_v2 2,2 GB RSS / 5,3 min; passT_v4 2,8 GB RSS / 56 s. 0 ordenes, solo lectura de datos y escritura en sa_ms2/ y out_v4/.
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov || exit 2
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1
CP=/root/polymarket-research/scripts/cron_pesado.sh; LOG=out_v4_run.log; DL=/root/polymarket-research-datalogs
PB=/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out
# 27-Nov: flock con espera (<=90 min) en vez de -n: el at 95 (12:45Z, dia 26) no debe morir en silencio si un backfill manual esta en curso.
exec 8>.run_v4_dias.lock; flock -w 5400 8 || { echo "otro run_v4_dias en curso (>90 min)"; exit 0; }
ts() { date -u +%FT%TZ; }
# 27-Nov (OOM): cron_pesado fija MemoryMax = MemAvailable - 1200 MB (min 2500). passT_v4 pica a 2,8 GB y ms_extract_v2 a 2,2 GB => antes de cada paso se espera a
# MemAvailable >= RAM_MS2 / RAM_PT (def. 4200 / 4600 MB => cap >= 3000 / 3400 MB). cron_pesado.sh NO se toca. Max 30 min de espera; si no llega, el dia queda PARTIAL (rc=1) y se reanuda.
RAM_MS2=${RAM_MS2:-4200}; RAM_PT=${RAM_PT:-4600}
esperar_ram() { local need=$1 a i; for i in $(seq 1 90); do a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); [ "${a:-0}" -ge "$need" ] && return 0; sleep 20; done; echo "$(ts) RAM insuficiente (${a} MB < ${need}) tras 30 min" >> $LOG; return 1; }
# 27-Nov: ventanas de pruebas reales/seco del chief (P1b 11:05 y 15:15Z, KS 14:00Z): se ESPERA a que pasen (no se compite por CPU/disco con ellas).
esperar_pruebas() { local h; while :; do h=$((10#$(date -u +%H%M))); { { [ "$h" -ge 1100 ] && [ "$h" -lt 1120 ]; } || { [ "$h" -ge 1355 ] && [ "$h" -lt 1415 ]; } || { [ "$h" -ge 1510 ] && [ "$h" -lt 1530 ]; }; } || break; sleep 30; done; }
# Ventanas prohibidas: 06:00-09:15Z (racimo de crons) y 22:00-02:30Z (seco 22:35Z, nulo incremental 22:35Z).
ventana_prohibida() { local h=$((10#$(date -u +%H%M))); { [ "$h" -ge 600 ] && [ "$h" -lt 915 ]; } || [ "$h" -ge 2200 ] || [ "$h" -lt 230 ]; }
if [ $# -gt 0 ]; then DIAS="$*"; else DIAS=""; d=${DESDE:-2026-11-25}; while [ "$d" \< "$(date -u +%F)" ]; do
  [ -f $PB/tape_$d.pkl ] && [ -f $PB/bad_$d.json ] && [ ! -f out_v4/RT_v3dd_$d.pkl ] && DIAS="$DIAS $d"; d=$(date -u -d "$d + 1 day" +%F); done; fi
echo "$(ts) run_v4_dias: dias ${DIAS:-ninguno}" >> $LOG
rc=0
for d in $DIAS; do
  [ -s out_v4/RT_v3dd_$d.pkl ] && continue
  if [ ! -f $PB/tape_$d.pkl ] || [ ! -f $PB/bad_$d.json ]; then echo "$(ts) PENDING $d: sin tape/bad (los crea run_rf5.sh 12:30Z)" >> $LOG; rc=1; continue; fi
  esperar_pruebas
  if ventana_prohibida; then echo "$(ts) ventana prohibida (06:00-09:15Z / 22:00-02:30Z), no se lanza $d" >> $LOG; rc=1; continue; fi
  python3 -I cobertura_dia_v4.py check $d >> $LOG 2>&1; [ $? -eq 3 ] && { echo "$(ts) BLOCKED $d (cobertura de insumos <0,90 o sin maker_ms; ver out_v4/MANIFIESTO_backfill_27nov.json)" >> $LOG; continue; }
  if [ ! -s $DL/sa_ms2/ms2_$d.npz ]; then
    esperar_ram $RAM_MS2 || { rc=1; continue; }
    echo "$(ts) EXTRAE ms2 $d" >> $LOG
    $CP bash -c "ulimit -v 5000000; exec timeout -k 60 3000 nice -n 19 ionice -c3 python3 -I ms_extract_v2.py $d" >> $LOG 2>&1
    [ -s $DL/sa_ms2/ms2_$d.npz ] || { echo "$(ts) FALLO ms2 $d" >> $LOG; python3 -I cobertura_dia_v4.py fin $d >> $LOG 2>&1; rc=1; continue; }
  fi
  esperar_ram $RAM_PT || { rc=1; continue; }
  echo "$(ts) passT_v4 v3 dd $d" >> $LOG
  $CP bash -c "ulimit -v 3600000; exec timeout -k 60 1800 nice -n 19 ionice -c3 python3 -I passT_v4.py v3 dd $d" >> $LOG 2>&1
  python3 -I cobertura_dia_v4.py fin $d >> $LOG 2>&1
  [ -s out_v4/RT_v3dd_$d.pkl ] && echo "$(ts) OK RT_v3dd_$d.pkl" >> $LOG || { echo "$(ts) FALLO passT_v4 $d" >> $LOG; rc=1; }
done
echo "$(ts) run_v4_dias fin rc=$rc" >> $LOG; exit $rc
