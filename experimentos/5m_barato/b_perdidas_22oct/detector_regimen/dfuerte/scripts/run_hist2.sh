#!/bin/bash
cd "$(dirname "$0")/.." || exit 1
until grep -q FIN datos_hist_bf.log; do sleep 20; done
nice -n 19 python3 -I scripts/r3c_hist_fetch.py backfill 2026-05-01 2026-07-26 0 > datos_hist_bf2.log 2>&1
nice -n 19 python3 -I scripts/r3c_hist_fetch.py backfill 2026-03-26 2026-04-30 0 > datos_hist_bf3.log 2>&1
