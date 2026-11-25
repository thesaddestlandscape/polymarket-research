#!/bin/bash
# Placebo CXJ150 (99 semillas) sobre los 10 dias QUEMADOS (solo informativo, etiqueta cp0). Un solo proceso, nice 19, ionice 3, ulimit 3 GB. Idempotente (salta RT ya generados).
cd /root/polymarket-research/experimentos/5m_barato/q11 || exit 1
DIAS=2026-10-26,2026-10-27,2026-10-28,2026-10-29,2026-10-30,2026-10-31,2026-11-01,2026-11-02,2026-11-03,2026-11-04
ulimit -v 3000000; export OMP_NUM_THREADS=1
H=$(date -u +%H%M); if [ "$H" -ge 0600 ] && [ "$H" -lt 0915 ]; then echo "BLOQUEADO 06:00-09:15Z"; exit 2; fi
echo "inicio $(date -u +%FT%TZ)"
for s in $(seq 1 99); do
  for d in ${DIAS//,/ }; do
    H=$(date -u +%H%M); if [ "$H" -ge 0600 ] && [ "$H" -lt 0915 ]; then echo "PARADO por franja 06:00-09:15Z en semilla $s dia $d (reanudar: idempotente)"; exit 3; fi
    nice -n 19 ionice -c3 python3 -W ignore -I placebo_cxj150.py dia $d $s > /dev/null 2>> thru1_fwd/placebo_cxj150_quemados.err || { echo "FALLO semilla $s dia $d"; exit 1; }
  done
  echo "semilla $s completa $(date -u +%T)"
done
nice -n 19 ionice -c3 python3 -W ignore -I placebo_cxj150.py agregar 0 $DIAS && echo "AGREGADO thru1_fwd/placebo_cxj150_cp0.json $(date -u +%FT%TZ)"
echo FIN
