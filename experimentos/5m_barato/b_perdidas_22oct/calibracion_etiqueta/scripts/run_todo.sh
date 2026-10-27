#!/bin/bash
# Orquestador (PREREG_CALIB): espera ventana segura y ejecuta A (B 20-23), a_calib, P (05-24, 2 en paralelo), B1 (wf off1/off2/off0) y B2 (a1 off1/off2/off0). Idempotente (cal_*_D saltan si existen).
BASE=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/calibracion_etiqueta; CD=/root/polymarket-research-datalogs/calibracion_etiqueta; LOG=$CD/run_todo.log
cd $BASE/scripts
log(){ echo "$(date -u +%FT%TZ) $*" >> $LOG; }
seguro(){ H=$(date -u +%H%M); L=$(cut -d' ' -f2 /proc/loadavg); M=$(awk '/MemAvailable/{print $2}' /proc/meminfo)
  [ "$H" -ge 0930 ] && [ "$H" -lt 2200 ] || return 1; awk -v l=$L 'BEGIN{exit !(l<8)}' || return 1; [ "$M" -gt 2500000 ] || return 1; return 0; }
until seguro; do sleep 120; done
log "inicio (ventana segura)"
run(){ ( ulimit -v 3000000; nice -n 19 ionice -c3 "$@" >> $LOG 2>&1 ); }
run python3 -I c0_verdad_onchain.py && run python3 -I c1_build_b.py || { log 'FALLO c0/c1: abortado'; exit 1; }
for D in 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do until seguro; do sleep 120; done; run python3 -I calib_core.py --dia $D --modo B; done
run python3 -I a_calib.py && log "a_calib hecho" || { log 'FALLO a_calib: abortado'; exit 1; }
seq 5 24 | xargs -P 2 -I{} bash -c 'D=$(printf "2026-10-%02d" {}); until '"$(declare -f seguro | tr '\n' ' ')"' seguro; do sleep 120; done; ulimit -v 3000000; nice -n 19 ionice -c3 python3 -I calib_core.py --dia $D --modo P >> '$LOG' 2>&1'
log "P hecho"
for O in 1 2 0; do run python3 -I b1_tabla_cal.py $O; done
run python3 -I d_b_f5.py
for O in 1 2 0; do run python3 -I a1_cal.py $O f5; done
run python3 -I a1_cal.py 1 f5b
for O in 1 2 0; do until seguro; do sleep 120; done; run python3 -I wf_cal_off$O.py; log "wf off$O hecho"; done
log "FIN"
