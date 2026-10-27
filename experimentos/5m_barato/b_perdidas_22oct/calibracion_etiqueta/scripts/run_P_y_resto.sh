#!/bin/bash
# Continuacion de run_todo.sh (su paso P fallo por un bug de xargs/declare -f). 1 proceso secuencial, nice 19, ionice idle, ulimit 3 GB. Idempotente.
BASE=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/calibracion_etiqueta; CD=/root/polymarket-research-datalogs/calibracion_etiqueta; LOG=$CD/run_P.log
cd $BASE/scripts
log(){ echo "$(date -u +%FT%TZ) $*" >> $LOG; }
seguro(){ H=$(date -u +%H%M); L=$(cut -d' ' -f2 /proc/loadavg); M=$(awk '/MemAvailable/{print $2}' /proc/meminfo)
  { [ "$H" -ge 0930 ] && [ "$H" -lt 2200 ]; } || return 1; awk -v l=$L 'BEGIN{exit !(l<8)}' || return 1; [ "$M" -gt 2500000 ] || return 1; return 0; }
run(){ ( ulimit -v 3000000; nice -n 19 ionice -c3 "$@" >> $LOG 2>&1 ); }
for N in $(seq 5 24); do D=$(printf "2026-10-%02d" $N); [ -f $CD/cal_P_$D.csv.gz ] && continue
  until seguro; do sleep 60; done; run python3 -I calib_core.py --dia $D --modo P; log "P $D rc=$?"; done
log "P hecho"
for O in 1 2 0; do until seguro; do sleep 60; done; run python3 -I b1_tabla_cal.py $O; done
until seguro; do sleep 60; done; run python3 -I d_b_f5.py
for O in 1 2 0; do until seguro; do sleep 60; done; run python3 -I a1_cal.py $O f5; done
for O in 1 2 0; do until seguro; do sleep 60; done; run python3 -I wf_cal_off$O.py; log "wf off$O hecho"; done
log FIN
