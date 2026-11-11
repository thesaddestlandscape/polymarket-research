#!/bin/bash
# Parte C: espera a A; extrae el resto de dias 26-Oct..09-Nov (v2), passT causal de los 15 dias, regresion de paso0_lib_v2 con fills originales, E1/N1/X1 con reloj causal; y aceptacion completa 03-07 Nov (legacy vs causal).
# Un fichero/dia cada vez, nice 19 ionice -c3, ulimit -v 3 GB, nunca 06-09Z (espera). Idempotente.
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov || exit 2
LOG=out_v2/run_C.log; ulimit -v 3000000; export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1
log(){ echo "$(date -u +%FT%TZ) $*" >> $LOG; }
espera(){ while true; do h=$(date -u +%H); if [ "$h" -ge 6 ] && [ "$h" -lt 9 ]; then sleep 120; else break; fi; done; }
run(){ espera; log "INICIO $*"; nice -n 19 ionice -c3 "$@" >> $LOG 2>&1; rc=$?; log "FIN rc=$rc $*"; return $rc; }
echo "$$" > out_v2/run_C.pid
PA=$(cat out_v2/run_A.pid); while kill -0 "$PA" 2>/dev/null; do sleep 30; done
log "A terminada; arranca C"
DIAS="2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-01 2026-11-02 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07 2026-11-08 2026-11-09"
for d in $DIAS; do
  [ -f /root/polymarket-research-datalogs/sa_ms2/ms2_$d.npz ] || run python3 -I ms_extract_v2.py $d || { log "ABORTO extraccion $d"; exit 1; }
  run python3 -I passT_v2.py causal $d; run python3 -I prep_fills_v2.py causal $d
done
run python3 -I concat_v2.py causal $DIAS
run python3 -I paso0_run_v2.py e1n1 orig; run python3 -I paso0_run_v2.py x1 orig
run python3 -I paso0_run_v2.py e1n1 causal; run python3 -I paso0_run_v2.py x1 causal
for d in 2026-11-04 2026-11-05 2026-11-06 2026-11-07; do
  for m in legacy; do run python3 -I passT_v2.py $m $d; run python3 -I prep_fills_v2.py $m $d; run python3 -I l2_triggers_v2.py $m $d; done
  run python3 -I l2_triggers_v2.py causal $d
done
run python3 -I condicion1.py 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07
log "PARTE C COMPLETA"
