#!/bin/bash
cd /tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/pred
export OMP_NUM_THREADS=1
ulimit -v 1500000
for H in 150 250 400; do
  nice -n 19 ionice -c3 python3 -u run3.py ds $H > run3_ds_H$H.log 2>&1
done
echo FIN > run3_fin.log
