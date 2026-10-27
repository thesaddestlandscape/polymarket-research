#!/bin/bash
# espera a >=09:30Z y load5<4 (max 4 h) y lanza el run completo con nice/ionice/ulimit
D=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/r8_emparejado
end=$(( $(date +%s) + 4*3600 ))
while true; do
  h=$(date -u +%H%M); l=$(awk '{print $2}' /proc/loadavg)
  if [ "$h" -ge 0930 ] && [ "$h" -lt 2000 ] && awk -v l="$l" 'BEGIN{exit !(l<4)}'; then break; fi
  [ $(date +%s) -gt $end ] && { echo "TIMEOUT espera load/hora $(date -u)" > $D/datos/lanzador.log; exit 2; }
  sleep 60
done
echo "arranca $(date -u) load5=$l" > $D/datos/lanzador.log
ulimit -v 3000000
nice -n 19 ionice -c3 python3 -I $D/scripts/r8e_run.py > $D/datos/r8e_salida.txt 2>&1
echo "fin $(date -u) rc=$?" >> $D/datos/lanzador.log
