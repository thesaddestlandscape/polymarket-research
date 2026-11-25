#!/bin/bash
# Produce en STAGING (db1_staging/out) los 10 dias QUEMADOS con el arnes ADDENDUM3 (RX sin exclusion de Binance dentro de la simulacion). Lanzar: scripts/cron_pesado.sh bash <esta ruta>
Q=/root/polymarket-research/experimentos/5m_barato/db1_staging; LOG=$Q/produccion_staging.log; echo "=== $(date -u +%FT%TZ) inicio" >> $LOG
for D in 2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-01 2026-11-02 2026-11-03 2026-11-04; do
  python3 -I $Q/eval_db1.py --producir $D --quemado >> $LOG 2>&1 || { echo "FALLO $D" >> $LOG; exit 1; }
done
echo "=== fin ok $(date -u +%FT%TZ)" >> $LOG
