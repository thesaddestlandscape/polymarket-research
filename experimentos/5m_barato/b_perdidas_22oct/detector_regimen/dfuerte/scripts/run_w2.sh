#!/bin/bash
# D-FUERTE ola 2: espera a que termine la ola 1 (marca FIN) y entonces f2/f4 con WAVE2=1.
cd "$(dirname "$0")/.." || exit 1
until grep -q FIN datos_f2_T180.log 2>/dev/null; do sleep 30; done
export OMP_NUM_THREADS=2 WAVE2=1
nice -n 19 ionice -c3 bash -c "ulimit -v 3000000; python3 -I scripts/f2_walkforward.py" > datos_f2_T180_w2.log 2>&1
TAGF=_w2 nice -n 19 ionice -c3 bash -c "ulimit -v 3000000; python3 -I scripts/f4_report.py 180" > r_dfuerte_T180_w2.txt 2>&1
echo FIN >> datos_f2_T180_w2.log
