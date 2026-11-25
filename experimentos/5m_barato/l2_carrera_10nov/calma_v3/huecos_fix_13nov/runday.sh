#!/bin/bash
# runday.sh MODE DIA...
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/huecos_fix_13nov
M=$1; shift
for d in "$@"; do
  [ -f out/tape2_$d.pkl ] || (ulimit -v 3500000; PYTHONDONTWRITEBYTECODE=1 nice -n 19 ionice -c3 python3 -I prep_day2.py $d) >> out/prep2.log 2>&1
  [ -f out/${M}_dec2v3_$d.pkl ] || (ulimit -v 3500000; MODE=$M HF_OUT=$PWD/out PYTHONDONTWRITEBYTECODE=1 nice -n 19 ionice -c3 python3 -I esc_v3b.py $d) >> out/run_$M.log 2>&1
done
echo FIN $M >> out/run_$M.log
