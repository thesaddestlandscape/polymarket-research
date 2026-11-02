#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r8_28oct
ulimit -v 3000000
nice -n 19 ionice -c3 python3 r8h_an_eth.py ETH > log_an_ETH_fix.txt 2>&1
nice -n 19 ionice -c3 python3 r8T.py ETH > log_r8T_ETH.txt 2>&1
nice -n 19 ionice -c3 python3 r8c_eth.py > log_r8c_ETH.txt 2>&1
