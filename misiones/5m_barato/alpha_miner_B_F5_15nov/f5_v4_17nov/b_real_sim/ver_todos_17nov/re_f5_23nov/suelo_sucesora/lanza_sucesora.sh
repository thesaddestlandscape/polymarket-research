#!/bin/bash
cd "$(dirname "$0")"; ulimit -v 1000000
for d in 2026-11-18 2026-11-19 2026-11-20 2026-11-21 2026-11-22; do
  ionice -c3 nice -n19 ./suelo_dia.sh $d >> lanza_sucesora.log 2>&1 || echo "$d FALLO" >> lanza_sucesora.log
done; echo FIN >> lanza_sucesora.log
