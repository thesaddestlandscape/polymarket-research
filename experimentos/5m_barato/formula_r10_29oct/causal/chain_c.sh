#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/causal
until grep -q "^fin" log_build.txt; do sleep 20; if ! pgrep -f "python3 r10c_build" >/dev/null && ! grep -q "^fin" log_build.txt; then echo "$(date -u +%FT%TZ) build murio" >> log_run.txt; exit 1; fi; done
sleep 5; ulimit -v 4500000
echo "$(date -u +%FT%TZ) start analysis" >> log_run.txt
nice -n 19 ionice -c3 python3 r10c_analysis.py > log_analysis.txt 2>&1; echo "$(date -u +%FT%TZ) end analysis rc=$?" >> log_run.txt
