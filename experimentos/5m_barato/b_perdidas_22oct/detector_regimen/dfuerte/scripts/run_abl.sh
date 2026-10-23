#!/bin/bash
cd "$(dirname "$0")/.." || exit 1
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 CTRLG2=1
nice -n 19 ionice -c3 bash -c "ulimit -v 3000000; python3 -I scripts/f2_walkforward.py" > datos_abl.log 2>&1
echo FIN >> datos_abl.log
