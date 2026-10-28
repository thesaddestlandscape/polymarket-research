#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r3_28oct || exit 1
export OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2
( ulimit -v 4500000; AWKBIN=mawk nice -n 19 ionice -c3 python3 feat3.py --dia 2026-10-10 --outdir out_smoke ) > smoke_feat.log 2>&1
echo FIN_SMOKE_FEAT >> smoke_feat.log
( ulimit -v 6000000; nice -n 19 ionice -c3 python3 analysis3.py --smoke 2026-10-10 ) > smoke_analysis.log 2>&1
echo FIN_SMOKE_AN >> smoke_analysis.log
( ulimit -v 3500000; nice -n 19 ionice -c3 python3 identity3.py --smoke ) > smoke_ident.log 2>&1
echo FIN_SMOKE_ID >> smoke_ident.log
