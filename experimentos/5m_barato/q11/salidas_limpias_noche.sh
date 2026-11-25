#!/bin/bash
# Procesa los dias pendientes (una pasada por dia) con puerta de carga. NO instala nada. Lanzar con at/nohup cuando toque. Log: out_salidas/noche.log
H=/root/polymarket-research/experimentos/5m_barato/q11/; DEC=/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/out/
ulimit -v 3000000; mkdir -p ${H}out_salidas
for f in $(ls ${DEC}dec2_2026-*.pkl); do
  d=$(basename $f .pkl); d=${d#dec2_}; [ -f ${H}out_salidas/sal_$d.pkl ] && continue
  hh=$(date -u +%H%M); if [ $hh -ge 0600 ] && [ $hh -lt 0930 ]; then echo "$(date -u) ventana 06-09:30Z, paro" >> ${H}out_salidas/noche.log; exit 0; fi
  l5=$(awk '{print $2}' /proc/loadavg); n=$(nproc); mem=$(awk '/MemAvailable/{print $2}' /proc/meminfo)
  if awk -v l=$l5 -v n=$n 'BEGIN{exit !(l/n>0.5)}' || [ $mem -lt 2500000 ]; then echo "$(date -u) puerta cerrada load5=$l5 mem=$mem" >> ${H}out_salidas/noche.log; exit 0; fi
  nice -n 19 ionice -c3 python3 -I ${H}salidas_limpias.py $d >> ${H}out_salidas/noche.log 2>&1
done
echo "$(date -u) fin pasada" >> ${H}out_salidas/noche.log
