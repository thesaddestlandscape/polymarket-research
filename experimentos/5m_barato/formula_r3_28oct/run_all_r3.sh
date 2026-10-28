#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r3_28oct || exit 1
export OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2
printf '%s\n' 2026-10-{05..26} | xargs -P2 -I{} bash run_one_r3.sh {}
echo "FIN_FEATURES n_npz=$(ls out/f_*.npz 2>/dev/null | wc -l)" >> run3.log
( ulimit -v 3500000; nice -n 19 ionice -c3 python3 identity3.py >> run3.log 2>&1 )
echo "FIN_IDENT" >> run3.log
( ulimit -v 6000000; nice -n 19 ionice -c3 python3 analysis3.py >> run3.log 2>&1 )
echo "FIN_R3" >> run3.log
