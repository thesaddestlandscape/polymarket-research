#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r1_28oct
export AWKBIN=mawk
printf '%s\n' 2026-10-25 2026-10-26 2026-10-22 2026-10-20 2026-10-18 2026-10-16 2026-10-14 2026-10-12 2026-10-10 2026-10-08 2026-10-21 2026-10-19 2026-10-17 2026-10-15 2026-10-13 2026-10-11 2026-10-09 2026-10-07 | xargs -P3 -I{} bash run_one.sh {}
echo FIN2 >> run.log
