#!/bin/bash
# 26-Nov solo lectura: captura conexiones gamma + py-spy de observadores/ejeclive en el pico (~:45:03)
D=/root/polymarket-research-datalogs; TS=$(date -u +%Y%m%d_%H%M)
bash /root/polymarket-research/scripts/captura_429_gamma_v2.sh &
PYSPY=$(which py-spy || echo /root/polymarket-research/.venv/bin/py-spy)
OBS=$(pgrep -f "[o]bservadores_fase0.py" | head -1); EJ=$(pgrep -f "[e]xecutores_live_consolidado.py" | head -1)
sleep 58   # lanzado 19:44:00 -> ~19:44:58
for k in 1 2 3 4 5 6; do
  for p in $OBS $EJ; do echo "=== $(date -u +%T.%N) pid $p" >> $D/pyspy_429_${TS}.log; timeout 20 $PYSPY dump --pid $p --nonblocking >> $D/pyspy_429_${TS}.log 2>&1; done
  sleep 4
done
wait
