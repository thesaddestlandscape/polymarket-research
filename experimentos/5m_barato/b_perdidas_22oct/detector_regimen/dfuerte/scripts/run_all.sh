#!/bin/bash
# D-FUERTE: espera a >=09:00Z, luego f2 (walk-forward) y f4 (informe). nice 19, ionice idle, ulimit 3 GB, 2 hilos.
cd "$(dirname "$0")/.." || exit 1
while [ "$(date -u +%H%M)" -lt 0930 ]; do sleep 30; done
export OMP_NUM_THREADS=2
for T in 180; do
  nice -n 19 ionice -c3 bash -c "ulimit -v 3000000; python3 -I scripts/f2_walkforward.py" > datos_f2_T$T.log 2>&1
  nice -n 19 ionice -c3 bash -c "ulimit -v 3000000; python3 -I scripts/f4_report.py $T" > r_dfuerte_T$T.txt 2>&1
done
echo FIN >> datos_f2_T180.log
