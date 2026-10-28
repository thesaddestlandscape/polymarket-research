#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r8_28oct
ulimit -v 3000000
while [ ! -f hz_BTC.npz ]; do sleep 20; done
sleep 5
nice -n 19 ionice -c3 python3 r8h_an.py BTC > log_an_BTC.txt 2>&1
nice -n 19 ionice -c3 python3 r8c.py > log_r8c.txt 2>&1
while [ $(ls ext_eth/b_*.npz | wc -l) -lt 22 ]; do sleep 20; done
nice -n 19 ionice -c3 python3 r8h_build.py ETH > log_hz_ETH.txt 2>&1
nice -n 19 ionice -c3 python3 r8h_an.py ETH > log_an_ETH.txt 2>&1
