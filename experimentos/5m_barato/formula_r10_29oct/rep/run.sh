#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r10_29oct
ulimit -v 4500000
nice -n 19 ionice -c3 python3 rep/r8h_an.py BTC > rep/log_r8h.txt 2>&1; echo rc=$? >> rep/log_r8h.txt
nice -n 19 ionice -c3 python3 rep/r8T.py BTC > rep/log_r8T.txt 2>&1; echo rc=$? >> rep/log_r8T.txt
