#!/bin/bash
# Produce los 10 dias QUEMADOS 2026-10-26..11-04 (idempotente) y corre la aceptacion de PREREG_DB1. Lanzar detras de cola pesada y fuera de 06:00-09:15Z:
#   /root/polymarket-research/scripts/cron_pesado.sh bash /root/polymarket-research/experimentos/5m_barato/db1/aceptacion_quemados.sh
Q=/root/polymarket-research/experimentos/5m_barato/db1; LOG=$Q/aceptacion.log; echo "=== $(date -u +%FT%TZ) inicio" >> $LOG
for D in 2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-01 2026-11-02 2026-11-03 2026-11-04; do
  python3 -I $Q/eval_db1.py --producir $D --quemado >> $LOG 2>&1 || { echo "FALLO $D" >> $LOG; exit 1; }
done
python3 -I $Q/eval_db1.py --aceptacion >> $LOG 2>&1; echo "=== fin rc=$? $(date -u +%FT%TZ)" >> $LOG
