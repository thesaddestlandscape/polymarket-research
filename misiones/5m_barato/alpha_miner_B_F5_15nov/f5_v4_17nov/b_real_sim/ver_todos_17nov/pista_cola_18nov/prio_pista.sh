#!/bin/bash
# sube prioridad de los procesos del calculo de la pista (por debajo del loop fast, nice 0)
while pgrep -f 'pista_cola_18nov/run_p1.sh' >/dev/null; do
  for p in $(pgrep -f 'python3 p1_dia.py'); do renice -n 5 -p $p >/dev/null 2>&1; ionice -c2 -n6 -p $p 2>/dev/null; done
  sleep 20
done
