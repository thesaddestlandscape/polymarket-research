#!/bin/bash
# Curva EV(l) con motor v3 (TRAIN 26-Oct..09-Nov, HOLD NO leido): passT_cxb_l.py para STAMP v3 y v3p, un dia cada vez, nice 19, ulimit 3,7 GB, nunca 06-09Z, idempotente. 0 ordenes.
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/l_real_11nov || exit 2
LOG=out_l/run_l.log; ulimit -v 3700000; export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1
log(){ echo "$(date -u +%FT%TZ) $*" >> $LOG; }
espera(){ while true; do h=$(date -u +%H); if [ "$h" -ge 6 ] && [ "$h" -lt 9 ]; then sleep 120; else break; fi; done; }
mem(){ while [ "$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)" -lt 2600 ]; do sleep 60; done; }
echo "$$" > out_l/run_l.pid
DIAS="2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-01 2026-11-02 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07 2026-11-08 2026-11-09"
for st in ${@:-v3 v3p}; do for d in $DIAS; do
  [ -f out_l/CXL_${st}_$d.pkl ] && continue
  espera; mem; log "INICIO $st $d"; nice -n 19 ionice -c3 python3 -I passT_cxb_l.py $st $d >> $LOG 2>&1; rc=$?; log "FIN rc=$rc $st $d"
  if [ $rc -ne 0 ]; then sleep 30; fi
done; done
log "CURVA l COMPLETA $*"
