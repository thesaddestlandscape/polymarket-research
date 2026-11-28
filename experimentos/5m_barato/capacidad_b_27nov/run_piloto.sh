#!/bin/bash
# run_piloto.sh DIA  (27-Nov, engineer 5m barato) -- piloto M1/M4/libro cruzado de capacidad de B. Etapas 1-4 en serie; 1 y 2 por scripts/cron_pesado.sh (cola global + cgroup), nice 19, ionice -c3.
# Idempotente por etapa (no rehace una etapa cuya salida existe; borrar el fichero para rehacerla). Espera fuera de 06:00-09:15Z / 22:00-02:30Z y de las ventanas de P1b real (11:00-11:30, 15:00-15:30Z).
# 0 ordenes, 0 red. Solo lectura de datos y de dev-bk/dev (importa, sin escribir); escribe SOLO en datalogs/capacidad_b_27nov/.
D=${1:-2026-11-25}; H=/root/polymarket-research/experimentos/5m_barato/capacidad_b_27nov; OUT=/root/polymarket-research-datalogs/capacidad_b_27nov
CP=/root/polymarket-research/scripts/cron_pesado.sh; LOG=$OUT/run_piloto_$D.log; mkdir -p $OUT
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1 PYTHONDONTWRITEBYTECODE=1
exec 7>$OUT/.run_piloto.lock; flock -n 7 || { echo "otro run_piloto en curso"; exit 0; }
ts() { date -u +%FT%TZ; }
espera_ventana() { while :; do h=$((10#$(date -u +%H%M))); if { [ $h -ge 600 ] && [ $h -lt 915 ]; } || [ $h -ge 2200 ] || [ $h -lt 230 ] || { [ $h -ge 1100 ] && [ $h -lt 1130 ]; } || { [ $h -ge 1500 ] && [ $h -lt 1530 ]; }; then sleep 60; else break; fi; done; }
paso() { # paso N salida ulimit
  local n=$1 sal=$2 ul=$3
  [ -s "$sal" ] && { echo "$(ts) etapa $n ya hecha ($sal)" >> $LOG; return 0; }
  espera_ventana; echo "$(ts) etapa $n INICIO" >> $LOG
  if [ $n -le 2 ]; then $CP bash -c "ulimit -v $ul; cd $H; exec nice -n 19 ionice -c3 python3 -I -B -u piloto_m1_m4.py $D --etapa $n" >> $LOG 2>&1
  else ( ulimit -v $ul; cd $H; exec nice -n 19 ionice -c3 python3 -I -B -u piloto_m1_m4.py $D --etapa $n ) >> $LOG 2>&1; fi
  [ -s "$sal" ] && echo "$(ts) etapa $n OK" >> $LOG || { echo "$(ts) etapa $n FALLO (sin $sal)" >> $LOG; return 1; }
}
echo "$(ts) run_piloto $D" >> $LOG
paso 1 $OUT/etapa1_$D.json 7000000 || exit 1
paso 2 $OUT/etapa2_${D}_cobertura.json 6500000 || exit 1
paso 3 $OUT/capacidad_b_27nov_piloto_$D.json 4000000 || exit 1
python3 -I -B -c "import json,sys; d=json.load(open('$OUT/capacidad_b_27nov_piloto_$D.json')); sys.exit(0 if d.get('status')=='PILOTO_1_DIA_NO_CONFIRMATORIO' else 3)" || { echo "$(ts) etapa 3 no dejo PILOTO (ver json: BLOCKED?)" >> $LOG; exit 3; }
( ulimit -v 2000000; cd $H; nice -n 19 python3 -I -B piloto_m1_m4.py $D --etapa 4 ) >> $LOG 2>&1
echo "$(ts) run_piloto fin rc=$?" >> $LOG
