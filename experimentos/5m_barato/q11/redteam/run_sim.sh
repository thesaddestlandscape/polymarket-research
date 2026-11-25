#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/q11/redteam
ulimit -v 3000000
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
for d in "$@"; do nice -n 19 ionice -c3 python3 -W ignore -I rt_sim.py $d 2>&1 | tail -2; done
echo SIM_FIN
