#!/bin/bash
# Cadena posterior al passT TRAIN v3: concat, paso0 (ev, e1n1, x1) sobre v3dd, triggers L2 03-07 + condicion1_v3, y familia CXB/F5 (passT_cxb_v3, un dia cada vez), analisis. nice 19, ulimit 3,7 GB, nunca 06-09Z. Idempotente.
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov || exit 2
LOG=out_v3/chain_v3.log; ulimit -v 3700000; export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1
log(){ echo "$(date -u +%FT%TZ) $*" >> $LOG; }
espera(){ while true; do h=$(date -u +%H); if [ "$h" -ge 6 ] && [ "$h" -lt 9 ]; then sleep 120; else break; fi; done; }
run(){ espera; log "INICIO $*"; nice -n 19 ionice -c3 "$@" >> $LOG 2>&1; rc=$?; log "FIN rc=$rc $*"; return $rc; }
echo "$$" > out_v3/chain_v3.pid
PA=$(cat out_v3/run_v3.pid); while kill -0 "$PA" 2>/dev/null; do sleep 20; done
DIAS="2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-01 2026-11-02 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07 2026-11-08 2026-11-09"
for t in v3dd v3orig v2dd; do run python3 -I concat_v3.py $t $DIAS; done
run python3 -I doble_conteo_v3.py
for f in ev e1n1 x1; do run python3 -I paso0_run_v3.py $f v3dd; done
for d in 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07; do run python3 -I l2_triggers_v3.py v3dd $d; done
run python3 -I condicion1_v3.py 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07
for d in $DIAS; do run python3 -I passT_cxb_v3.py v3 dd $d; done
run python3 -I analiza_cxb_v3.py v3dd
log "CADENA v3 COMPLETA"
