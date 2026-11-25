#!/bin/bash
# run_all.sh — extracción secuencial idempotente (un día por proceso) + eval.py congelado solo si están los 22 días.
cd /root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct || exit 1
mkdir -p units
ulimit -v 3000000
for d in $(seq -w 5 26); do
  D=2026-10-$d
  [ -s units/u_$D.csv.gz ] && continue
  H=$(date -u +%H%M)
  if [ "$H" -ge 0600 ] && [ "$H" -lt 0930 ]; then echo "PAUSA franja 06-09:30Z antes de $D" >> sim.log; exit 3; fi
  nice -n 19 ionice -c3 python3 sim.py --dia $D >> sim.log 2>&1 || echo "FALLO $D" >> sim.log
done
n=$(ls units/u_2026-10-*.csv.gz 2>/dev/null | wc -l)
if [ "$n" -eq 22 ]; then
  nice -n 19 ionice -c3 python3 eval.py > eval_salida.txt 2>&1; echo "EVAL rc=$? $(date -u +%FT%TZ)" >> sim.log
else
  echo "EVAL NO EJECUTADO: $n/22 dias" >> sim.log
fi
