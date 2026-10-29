#!/bin/bash
# R10: espera recursos (load5<=8, MemAvailable>=2,5 GB, fuera de 06-09Z) y ejecuta build -> train en serie
cd /root/polymarket-research/experimentos/5m_barato/formula_r10_29oct
ulimit -v 4500000
ok() { l5=$(cut -d' ' -f2 /proc/loadavg); ma=$(awk '/MemAvailable/{print $2}' /proc/meminfo); h=$(date -u +%H)
  awk -v l=$l5 -v m=$ma -v h=$h 'BEGIN{exit !(l<=8.0 && m>=2500000 && (h<6 || h>=9))}'; }
until ok; do sleep 30; done
echo "$(date -u +%FT%TZ) start build" >> log_run.txt
nice -n 19 ionice -c3 python3 r10_build.py BTC > log_build.txt 2>&1; rc=$?; echo "$(date -u +%FT%TZ) end build rc=$rc" >> log_run.txt
[ $rc -eq 0 ] || exit 1
until ok; do sleep 30; done
echo "$(date -u +%FT%TZ) start train" >> log_run.txt
nice -n 19 ionice -c3 python3 r10_train.py > log_train.txt 2>&1; echo "$(date -u +%FT%TZ) end train rc=$?" >> log_run.txt
