#!/bin/bash
# run_5bis.sh (27-Nov, engineer 5m barato) -- etapa 1 (pesada) de los dias 18 y 24-Nov por scripts/cron_pesado.sh (cola global + cgroup), nice 19, ionice -c3. Idempotente (no rehace un dia con sus 3 salidas).
# Fuera de 06:00-09:30Z, 14:55-15:40Z, 22:00-02:45Z y de las puertas de P1b real (11:00-11:30, 15:00-15:30Z). 0 ordenes, 0 red.
H=/root/polymarket-research/experimentos/5m_barato/exp5bis_27nov; OUT=/root/polymarket-research-datalogs/exp5bis_27nov; CP=/root/polymarket-research/scripts/cron_pesado.sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1 PYTHONDONTWRITEBYTECODE=1
mkdir -p $OUT; LOG=$OUT/run_5bis.log
exec 7>$OUT/.run_5bis.lock; flock -n 7 || { echo "otro run_5bis en curso"; exit 0; }
ts() { date -u +%FT%TZ; }
espera() { while :; do h=$((10#$(date -u +%H%M))); if { [ $h -ge 600 ] && [ $h -lt 930 ]; } || { [ $h -ge 1455 ] && [ $h -lt 1540 ]; } || [ $h -ge 2200 ] || [ $h -lt 245 ] || { [ $h -ge 1100 ] && [ $h -lt 1130 ]; }; then sleep 60; else break; fi; done; }
[ $# -eq 0 ] && set -- 2026-11-18 2026-11-24
for D in "$@"; do
  [ -s $OUT/f2_replay_$D.json ] && [ -s $OUT/etapa1_$D.json ] && [ -s $OUT/status_motor_$D.pkl ] && { echo "$(ts) $D ya hecho" >> $LOG; continue; }
  espera; echo "$(ts) etapa1 $D INICIO" >> $LOG
  $CP bash -c "ulimit -v 7000000; cd $H; exec nice -n 19 ionice -c3 python3 -I -B -u fn5bis_etapa1.py $D" >> $LOG 2>&1
  [ -s $OUT/status_motor_$D.pkl ] && echo "$(ts) etapa1 $D OK" >> $LOG || echo "$(ts) etapa1 $D FALLO (sin f2_replay_$D.json; rc del lanzador NO fiable)" >> $LOG
done
echo "$(ts) run_5bis fin" >> $LOG
