#!/bin/bash
# run_pred2.sh - orden de prioridad (OOS primero, luego IS intercalado); espera al python en curso; idempotente; pausa 06:00-09:30Z.
cd /root/polymarket-research/experimentos/5m_barato/predictor_as_b_28oct || exit 1
ulimit -v 3000000
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
P=$1
if [ "$P" != "0" ]; then while kill -0 $P 2>/dev/null; do sleep 5; done; fi
for d in 23 24 25 26 10 13 16 19 22 11 14 17 20 09 12 15 18 21; do
  D=2026-10-$d
  [ -s out/p_$D.npz ] && continue
  H=$(date -u +%H%M)
  if [ "$H" -ge 0600 ] && [ "$H" -lt 0930 ]; then echo "PAUSA franja 06-09:30Z antes de $D $(date -u +%FT%TZ)" >> run.log; exit 3; fi
  nice -n 19 ionice -c3 python3 pred_extract.py --dia $D >> run.log 2>&1 || echo "FALLO $D" >> run.log
done
echo "FIN2 $(ls out/p_2026-10-*.npz 2>/dev/null | wc -l)/22 $(date -u +%FT%TZ)" >> run.log
