#!/bin/bash
# run_v2.sh (18-Nov): corridas del PREREG_VER_TODOS_v2 (idempotente: v9 salta dias ya hechos)
cd "$(dirname "$0")"; ulimit -v 3000000
for cfg in "35 33" "147 33" "35 74" "35 111" "147 111"; do set -- $cfg
  for d in 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do
    B_EX_ALTA=$1 B_EX_CANC=$2 nice -n 19 ionice -c3 python3 v9_verif_v2.py $d >> out_v2/run.log 2>&1 || echo "FALLO $1 $2 $d" >> out_v2/run.log
  done; done; echo FIN >> out_v2/run.log
