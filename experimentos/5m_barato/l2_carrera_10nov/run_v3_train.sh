#!/bin/bash
# passT v3 (sello por firma) sobre TRAIN 26-Oct..09-Nov: STAMP v3 con ENG dd y orig (+ v2 dd para aislar el dedupe con sellos viejos). Un dia cada vez, nice 19, ulimit 3 GB, nunca 06-09Z. Idempotente.
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov || exit 2
LOG=out_v3/run_v3.log; ulimit -v 3000000; export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1
log(){ echo "$(date -u +%FT%TZ) $*" >> $LOG; }
espera(){ while true; do h=$(date -u +%H); if [ "$h" -ge 6 ] && [ "$h" -lt 9 ]; then sleep 120; else break; fi; done; }
run(){ espera; log "INICIO $*"; nice -n 19 ionice -c3 "$@" >> $LOG 2>&1; rc=$?; log "FIN rc=$rc $*"; return $rc; }
echo "$$" > out_v3/run_v3.pid
DIAS="2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-01 2026-11-02 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07 2026-11-08 2026-11-09"
for d in $DIAS; do
  for t in "v3 dd" "v3 orig" "v2 dd"; do set -- $t; run python3 -I passT_v3.py $1 $2 $d || { log "ABORTO $t $d"; }; run python3 -I prep_fills_v3.py $1$2 $d; done
done
log "TRAIN v3 COMPLETA"
