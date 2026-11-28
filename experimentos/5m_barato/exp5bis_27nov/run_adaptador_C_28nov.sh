#!/bin/bash
# run_adaptador_C_28nov.sh -- adaptador 5a con la FORMULA C (28-Nov) de los dias 18, 24, 25, 26-Nov por scripts/cron_pesado.sh (cola global + cgroup), ulimit -v 7 GB, nice 19, ionice -c3, 2 ejecuciones por dia (hash_tabla). 0 ordenes, 0 red.
# Fuera de 06:00-09:30Z, 14:55-15:40Z, 22:00-02:45Z y de las puertas de P1b real (11:00-11:30, 15:00-15:30Z). Idempotente (no rehace un dia con su f2_adaptador5a_C_DIA.json).
H=/root/polymarket-research/experimentos/5m_barato/exp5bis_27nov; OUT=/root/polymarket-research-datalogs/exp5bis_27nov/paso3; CP=/root/polymarket-research/scripts/cron_pesado.sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1 PYTHONDONTWRITEBYTECODE=1
mkdir -p $OUT; LOG=$OUT/run_adaptador_C.log
exec 7>$OUT/.run_adaptador_C.lock; flock -n 7 || { echo "otro run en curso"; exit 0; }
ts() { date -u +%FT%TZ; }
espera() { while :; do h=$((10#$(date -u +%H%M))); if { [ $h -ge 600 ] && [ $h -lt 930 ]; } || { [ $h -ge 1455 ] && [ $h -lt 1540 ]; } || [ $h -ge 2200 ] || [ $h -lt 245 ] || { [ $h -ge 1100 ] && [ $h -lt 1130 ]; }; then sleep 60; else break; fi; done; }
[ $# -eq 0 ] && set -- 2026-11-18 2026-11-24 2026-11-25 2026-11-26
for D in "$@"; do
  [ -s $OUT/f2_adaptador5a_C_$D.json ] && { echo "$(ts) $D ya hecho" >> $LOG; continue; }
  espera; echo "$(ts) adaptador C $D INICIO" >> $LOG
  $CP bash -c "ulimit -v 7000000; cd $H; exec nice -n 19 ionice -c3 python3 -I -B -u f2_adaptador5a_28nov.py $D" >> $LOG 2>&1
  [ -s $OUT/f2_adaptador5a_C_$D.json ] && echo "$(ts) adaptador C $D OK" >> $LOG || echo "$(ts) adaptador C $D FALLO (sin json; rc del lanzador NO fiable)" >> $LOG
done
echo "$(ts) FIN" >> $LOG
