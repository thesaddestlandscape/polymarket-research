#!/bin/bash
cd $(dirname $0); LOG=/root/polymarket-research-datalogs/calibracion_etiqueta/run_resto2.log
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1 ARROW_DEFAULT_MEMORY_POOL=system
run(){ L=$(cut -d' ' -f2 /proc/loadavg); awk -v l=$L 'BEGIN{exit !(l<8)}' || { echo "load alto $L, espera" >> $LOG; sleep 120; }; ( ulimit -v 3000000; nice -n 19 ionice -c3 "$@" >> $LOG 2>&1 ); echo "$(date -u +%T) $* rc=$?" >> $LOG; }
run python3 -I d_b_f5.py
for O in 1 2 0; do run python3 -I a1_cal.py $O f5; done
for O in 1 2 0; do run python3 -I wf_cal_off$O.py; done
echo FIN >> $LOG
