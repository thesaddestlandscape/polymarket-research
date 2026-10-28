#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r9_28oct
ulimit -v 3000000
nice -n 19 ionice -c3 python3 r9fwd.py --check 2026-10-27 > log_fwdcheck.txt 2>&1
echo "$(date -u +%FT%TZ) end fwdcheck rc=$?" >> log_run.txt
