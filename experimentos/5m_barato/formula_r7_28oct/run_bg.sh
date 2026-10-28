#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r7_28oct
ulimit -v 3000000
nice -n 19 ionice -c3 python3 r7_15m.py > log_15m.txt 2>&1
nice -n 19 ionice -c3 python3 r7_simc.py > log_simc.txt 2>&1
