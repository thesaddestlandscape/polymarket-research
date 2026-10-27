#!/bin/bash
# lanzamiento directo (load5 base de la maquina 8 nucleos ~6 nunca baja de 4: desviacion documentada). 1 hilo, nice 19, ionice idle.
D=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/r8_emparejado
echo "arranca $(date -u) load5=$(awk '{print $2}' /proc/loadavg)" > $D/datos/lanzador2.log
ulimit -v 3000000
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
nice -n 19 ionice -c3 python3 -I $D/scripts/r8e_run.py > $D/datos/r8e_salida.txt 2>&1
echo "fin $(date -u) rc=$?" >> $D/datos/lanzador2.log
