#!/bin/bash
# run_pred.sh - extraccion secuencial idempotente (un dia por proceso), nice 19, ulimit 3 GB, pausa 06:00-09:30Z.
cd /root/polymarket-research/experimentos/5m_barato/predictor_as_b_28oct || exit 1
mkdir -p out
ulimit -v 3000000
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
for d in $(seq -w 5 26); do
  D=2026-10-$d
  [ -s out/p_$D.npz ] && continue
  H=$(date -u +%H%M)
  if [ "$H" -ge 0600 ] && [ "$H" -lt 0930 ]; then echo "PAUSA franja 06-09:30Z antes de $D $(date -u +%FT%TZ)" >> run.log; exit 3; fi
  for i in 1 2 3 4 5 6 7 8 9 10; do
    MA=$(awk '/MemAvailable/ {print int($2/1024)}' /proc/meminfo)
    L5=$(awk '{print int($2)}' /proc/loadavg)
    if [ "$MA" -ge 1800 ] && [ "$L5" -le 7 ]; then break; fi
    echo "espera MemAvailable=$MA load5=$L5 antes de $D" >> run.log; sleep 60
  done
  nice -n 19 ionice -c3 python3 pred_extract.py --dia $D >> run.log 2>&1 || echo "FALLO $D" >> run.log
done
echo "FIN $(ls out/p_2026-10-*.npz 2>/dev/null | wc -l)/22 $(date -u +%FT%TZ)" >> run.log
