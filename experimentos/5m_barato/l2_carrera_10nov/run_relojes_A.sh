#!/bin/bash
# Parte A (nucleo): extraccion v2 + calibracion de 03/05/09-Nov, regresion, condicion 1 sobre 03-Nov (legacy/causal/rx), anclas. Un fichero/dia cada vez, nice 19 ionice -c3, ulimit -v 3 GB.
# Fuera de 06:00-09:00Z: si cae dentro, ESPERA (no arranca trabajo pesado). Idempotente: cada paso salta lo ya hecho.
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov || exit 2
mkdir -p out_v2; LOG=out_v2/run_A.log
ulimit -v 3000000; export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1
log(){ echo "$(date -u +%FT%TZ) $*" >> $LOG; }
espera(){ while true; do h=$(date -u +%H); if [ "$h" -ge 6 ] && [ "$h" -lt 9 ]; then sleep 120; else break; fi; done; }
run(){ espera; log "INICIO $*"; nice -n 19 ionice -c3 "$@" >> $LOG 2>&1; rc=$?; log "FIN rc=$rc $*"; return $rc; }
echo "$$" > out_v2/run_A.pid
for d in 2026-11-03 2026-11-05 2026-11-09; do
  run python3 -I ms_extract_v2.py $d || { log "ABORTO extraccion $d"; exit 1; }
  run python3 -I calib_relojes.py $d
done
run python3 -I regresion_extractor.py 2026-11-03
d=2026-11-03
for m in legacy causal rx; do run python3 -I passT_v2.py $m $d; run python3 -I prep_fills_v2.py $m $d; run python3 -I l2_triggers_v2.py $m $d; done
run python3 -I condicion1.py $d
run python3 -I anclas_relojes.py sonda 2026-11-04
for d in 2026-10-20 2026-10-21 2026-10-22; do run python3 -I anclas_relojes.py breal $d; done
log "PARTE A COMPLETA"
