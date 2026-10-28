#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r8_28oct
ulimit -v 3000000
nice -n 19 ionice -c3 python3 r8L.py > log_r8L.txt 2>&1
