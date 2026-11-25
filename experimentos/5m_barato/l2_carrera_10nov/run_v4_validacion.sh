#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov || exit 2
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 MALLOC_ARENA_MAX=1
SP=$PWD; mkdir -p $SP/out_v3_actual_16nov; LOG=out_v4_run.log; T_END=$(( $(date +%s) + 3000 ))
for d in 2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-01 2026-11-02 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07 2026-11-08 2026-11-09; do
 [ -f out_v4/RT_v3dd_$d.pkl ] && [ -f $SP/out_v3_actual_16nov/RT_v3dd_$d.pkl ] && continue
 while true; do
  [ $(date +%s) -gt $T_END ] && { echo "$(date -u +%FT%TZ) TIMEOUT espera RAM en $d" >> $LOG; exit 5; }
  h=$(date -u +%H%M); if [ "$h" -ge 0600 ] && [ "$h" -lt 0930 ]; then echo "ventana prohibida $h" >> $LOG; exit 3; fi
  av=$(awk '/MemAvailable/{print $2}' /proc/meminfo); [ "$av" -ge 3400000 ] && break; sleep 20
 done
 echo "$(date -u +%FT%TZ) passT v4 + v3-actual $d (MemAvail ${av} kB)" >> $LOG
 (ulimit -v 3600000; nice -n 19 ionice -c3 python3 -I passT_v4.py v3 dd $d >> $LOG 2>&1); rc=$?
 [ -f out_v4/RT_v3dd_$d.pkl ] || { echo "FALLO passT v4 $d rc=$rc" >> $LOG; exit 4; }
 (ulimit -v 3600000; PASST_OUT=$SP/out_v3_actual_16nov/ nice -n 19 ionice -c3 python3 -I passT_v3.py v3 dd $d >> $LOG.v3actual 2>&1); rc=$?
 [ -f $SP/out_v3_actual_16nov/RT_v3dd_$d.pkl ] || { echo "FALLO passT v3actual $d rc=$rc" >> $LOG; exit 4; }
done
echo "$(date -u +%FT%TZ) FIN OK" >> $LOG
