#!/bin/bash
# run_replay_cuando_libre.sh DIA [--sin-ws] : lanza replay_train.py (prueba de reproduccion TRAIN) solo con memoria de sobra y fuera de 06-09Z. nice 19 ionice 3, ulimit 4,0 GB.
# Salvaguarda: vigila MemAvailable cada 3 s y MATA SOLO su propio proceso (por pid) si baja de 1600 MB (guard_ram reinicia observadores por debajo de 900 MB). Idempotente.
D=$1; shift; H=$(dirname "$(readlink -f "$0")"); cd "$H"
[ -f out_replay/replay_$D.json ] && { echo "ya $D"; exit 0; }
while true; do
  h=$(date -u +%H); av=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
  if [ "$h" -ge 6 ] && [ "$h" -lt 9 ]; then sleep 120; continue; fi
  if [ "$av" -ge 5000 ]; then break; fi
  sleep 30
done
echo "$(date -u +%FT%TZ) INICIO $D MemAvailable=${av}MB"
( ulimit -v 4000000; exec nice -n 19 ionice -c3 python3 -I replay_train.py $D "$@" ) > out_replay/replay_$D.log 2>&1 &
pid=$!
while kill -0 $pid 2>/dev/null; do
  av=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
  if [ "$av" -lt 1600 ]; then echo "$(date -u +%FT%TZ) ABORTA por memoria ($av MB): kill $pid"; kill $pid; break; fi
  sleep 3
done
wait $pid; echo "$(date -u +%FT%TZ) FIN rc=$? $D"
