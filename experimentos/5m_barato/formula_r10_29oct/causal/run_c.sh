#!/bin/bash
# R10c: build causal (espera recursos; fuera de 06-09Z)
cd /root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/causal
ulimit -v 4500000
ok() { l5=$(cut -d' ' -f2 /proc/loadavg); ma=$(awk '/MemAvailable/{print $2}' /proc/meminfo); h=$(date -u +%H)
  awk -v l=$l5 -v m=$ma -v h=$h 'BEGIN{exit !(l<=9.0 && m>=2500000 && (h<6 || h>=9))}'; }
until ok; do sleep 30; done
echo "$(date -u +%FT%TZ) start build" >> log_run.txt
nice -n 19 ionice -c3 python3 r10c_build.py BTC > log_build.txt 2>&1; echo "$(date -u +%FT%TZ) end build rc=$?" >> log_run.txt
