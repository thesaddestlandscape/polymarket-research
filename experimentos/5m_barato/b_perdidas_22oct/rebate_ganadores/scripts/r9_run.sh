#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/rebate_ganadores
ulimit -v 5000000
for d in 2026-10-20 2026-10-21 2026-10-22; do (nice -n 19 python3 scripts/r9_sim.py $d > datos/r9_log_$d.txt 2>&1 &) ; done
