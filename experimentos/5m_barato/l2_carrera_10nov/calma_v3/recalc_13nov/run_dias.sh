#!/bin/bash
# Recalcula dec2v3/dec3v3s100 con sello v3 (calma_v3/esc_dec2_v3.py, esc_dec2.py de dev SIN editar) para los dias dados, UNO A LA VEZ, nice19/ionice3, ulimit -v 3 GB, guard RSS. Idempotente (esc_dec2 sale si el pkl existe).
# Uso: run_dias.sh 2026-11-09 2026-11-10 ...   Salida: calma_v3/recalc_13nov/out/  Log: out/run_<ts>.log
R=/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov; O=$R/calma_v3/recalc_13nov/out; export CALMA_V3_OUT=$O; L=$O/run_$(date -u +%Y%m%dT%H%M%S).log
for d in "$@"; do
  for xs in 0 100; do
    echo "$(date -u +%FT%TZ) inicio $d EXTRA_SHIFT_MS=$xs" >> $L
    EXTRA_SHIFT_MS=$xs python3 -I $R/dryrun/guard_rss.py --max-rss-mb 2800 --min-avail-mb 1500 --vmem-kb 3000000 --esperar-min 5 -- python3 -I $R/calma_v3/esc_dec2_v3.py $d >> $L 2>&1
    rc=$?; echo "$(date -u +%FT%TZ) fin $d xs=$xs rc=$rc" >> $L
  done
done
