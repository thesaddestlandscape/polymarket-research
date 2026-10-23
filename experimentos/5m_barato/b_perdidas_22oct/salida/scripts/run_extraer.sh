#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/salida
ulimit -v 3000000
for d in "$@"; do nice -n 19 ionice -c3 /usr/bin/time -f "%e s maxrss %M KB" python3 scripts/extraer.py $d; done
