#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r2_28oct || exit 1
printf '2026-10-%02d\n' $(seq 5 26) | xargs -P3 -I{} bash run_one_r2.sh {}
echo "FIN_R2 $(date -u +%FT%TZ)" >> run2.log
