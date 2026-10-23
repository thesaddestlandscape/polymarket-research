#!/bin/bash
# Construye grid + simv3m para R0 (18-21) y OOS (09-16). Un dia a la vez. Log en datalogs/v3m_puerta/build.log
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/v3m
ulimit -v 2000000
export ARROW_DEFAULT_MEMORY_POOL=system OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
for d in 2026-10-18 2026-10-19 2026-10-20 2026-10-21 2026-10-09 2026-10-10 2026-10-11 2026-10-12 2026-10-13 2026-10-14 2026-10-15 2026-10-16; do
  echo "=== $(date -u +%FT%TZ) $d"
  nice -n 19 ionice -c3 python3 book_grid.py $d || echo "FALLO grid $d"
  nice -n 19 ionice -c3 python3 sim_v3m.py $d || echo "FALLO sim $d"
done
echo "FIN $(date -u +%FT%TZ)"
