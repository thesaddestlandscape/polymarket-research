#!/bin/bash
# run_b_passT.sh -- passT_v4 (STAMP v3, ENG dd) para los dias de cinta SIN salida en out_v4 (10-14 Nov, y 15-16 Nov si hay cinta). Un dia por job via cron_pesado (cgroup), idempotente (passT sale con 'ya' si existe la salida), salida en cache/passT_out (no toca out_v4). 0 ordenes. Politica G0 congelada = la de passT_v4.
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov; LOG=$H/run_b_passT.log; G=$H/guard_v4.sh; CP=/root/polymarket-research/scripts/cron_pesado.sh; L2=/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov
exec 8>$H/.run_b_passT.lock; flock -n 8 || exit 0
for D in 2026-11-13 2026-11-14; do
  [ -s $H/cache/passT_out/RT_v3dd_$D.pkl ] && continue
  [ -s /root/polymarket-research-datalogs/sa_ms2/ms2_$D.npz ] || { bash $G --check && echo "$(date -u +%FT%TZ) EXTRAE ms2 $D" >> $LOG && ( cd $L2 && bash $CP bash -c "ulimit -v 5000000; exec timeout -k 60 3000 nice -n 19 ionice -c3 python3 -I $L2/ms_extract_v2.py $D" ) >> $H/out_ms2_$D.txt 2>&1; }
  [ -s /root/polymarket-research-datalogs/sa_ms2/ms2_$D.npz ] || { echo "$(date -u +%FT%TZ) SIN ms2 $D: $(tail -1 $H/out_ms2_$D.txt | cut -c1-120)" >> $LOG; continue; }
  for n in $(seq 1 3); do
    bash $G --check || { sleep 120; continue; }
    echo "$(date -u +%FT%TZ) INICIO $D" >> $LOG
    ( cd $L2 && PASST_OUT=$H/cache/passT_out/ bash $CP bash -c "ulimit -v 4300000; exec timeout -k 60 3000 nice -n 19 ionice -c3 python3 -I $L2/passT_v4.py v3 dd $D" ) >> $H/out_passT_$D.txt 2>&1; echo "$(date -u +%FT%TZ) FIN $D rc=$? $(tail -1 $H/out_passT_$D.txt | cut -c1-160)" >> $LOG
    [ -s $H/cache/passT_out/RT_v3dd_$D.pkl ] && break
  done
done; echo "$(date -u +%FT%TZ) ===== FIN run_b_passT" >> $LOG
