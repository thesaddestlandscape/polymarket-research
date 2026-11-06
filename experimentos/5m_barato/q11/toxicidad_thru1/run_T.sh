#!/bin/bash
# espera a la ventana permitida (>=09:16Z), comprueba RAM/carga, corre passT por dia y el analisis
cd /root/polymarket-research/experimentos/5m_barato/q11/toxicidad_thru1
while [ "$(date -u +%H%M)" -lt 0916 ]; do sleep 30; done
ulimit -v 3000000; export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
for d in 2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-01 2026-11-02 2026-11-03 2026-11-04; do
  while [ "$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)" -lt 2600 ]; do sleep 60; done
  nice -n 19 ionice -c3 /usr/bin/time -f "%e s %M KB" python3 -W ignore -I passT.py $d >> out/passT.log 2>&1
done
echo T_FIN >> out/passT.log
nice -n 19 python3 -W ignore -I anaT.py > out/anaT.log 2>&1; echo ANA_FIN >> out/anaT.log
