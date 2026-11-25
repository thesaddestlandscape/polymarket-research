#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/validador_alpha_b_27oct || exit 1
ulimit -v 3000000
for d in 12 $(seq -w 5 11) $(seq 13 26); do
  D=2026-10-$(printf %02d $((10#$d)))
  [ -s v_$D.csv.gz ] && continue
  /usr/bin/time -f "%e s %M KB" nice -n 19 ionice -c3 python3 vsim.py $D >> vsim.log 2>&1 || echo "FALLO $D" >> vsim.log
done
echo FIN >> vsim.log
