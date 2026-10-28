#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r9_28oct
until grep -q "end r9a.py" log_run.txt 2>/dev/null; do sleep 30; done
./run_r9.sh r9c.py r9d.py
