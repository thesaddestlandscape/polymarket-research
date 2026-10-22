#!/bin/bash
# espera a 09:16Z y ejecuta, de uno en uno, nice 19 / ionice 3 / ulimit 3 GB
B=/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa; SP=/tmp/claude-0/-root-polymarket-research/46569fb1-feea-4c5a-8d2d-299a326f3bc5/scratchpad
LOG=$B/datos/pipeline.log; cd /tmp; export PYTHONDONTWRITEBYTECODE=1
until [ "$(date -u +%H%M)" -ge 0916 ]; do sleep 30; done
run() { echo "=== $(date -u +%T) $*" >> $LOG; nice -n 19 ionice -c3 bash -c "ulimit -v 3000000; $*" >> $LOG 2>&1; echo "rc=$?" >> $LOG; }
run "python3 $B/scripts/r1_fwd_extract.py 2026-10-20 2026-10-21"
for d in 2026-10-17 2026-10-18 2026-10-19 2026-10-20 2026-10-21; do run "python3 $B/scripts/ms_extract.py $d"; done
mkdir -p $B/datos/simv2
run "python3 $B/scripts/sim_v2.py $SP $B/datos/simv2 2026-10-17 2026-10-18 2026-10-19 2026-10-20 2026-10-21"
run "python3 $B/scripts/attach_ms.py $SP"
run "python3 $B/scripts/an_pie.py $B/datos/pie_celdas.csv"
echo "=== FIN $(date -u +%T)" >> $LOG
