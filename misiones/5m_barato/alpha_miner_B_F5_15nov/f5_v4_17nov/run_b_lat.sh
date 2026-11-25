#!/bin/bash
# run_b_lat.sh LAT -- por dia (26-Oct..14-Nov): passT_v4 con LAT_POST=LAT (latencia real alta ex-envio, paquete_l 13-Nov) via t4d_passT_lat.py y luego t4d_b_f5v2.py (rasgos en t_dec y en tf-63). Un job por dia via cron_pesado, idempotente. Log run_b_lat_LAT.log. Orden: 26,27 Oct (dias hi) primero.
LAT=${1:-35}; H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov; LOG=$H/run_b_lat_$LAT.log; G=$H/guard_v4.sh; CP=/root/polymarket-research/scripts/cron_pesado.sh
exec 8>$H/.run_b_lat_$LAT.lock; flock -n 8 || exit 0; mkdir -p $H/cache/passT$LAT
LISTA=${DIAS:-"2026-10-26 2026-10-27 $(for i in $(seq 2 20); do date -u -d "2026-10-26 +$i day" +%F; done | sed '/2026-11-15/,$d')"}
for D in $LISTA; do
  [ "$D" \> "2026-11-14" ] && continue
  for n in 1 2 3; do
    [ -s $H/cache/passT$LAT/RT_v3dd_$D.pkl ] && break
    [ "$(date -u +%H%M)" -ge 2330 ] && { echo "$(date -u +%FT%TZ) hora>=23:30Z: paro" >> $LOG; exit 0; }
    bash $G --check || { sleep 120; continue; }
    echo "$(date -u +%FT%TZ) passT INICIO $D" >> $LOG
    PASST_OUT=$H/cache/passT$LAT/ bash $CP bash -c "ulimit -v 4300000; exec timeout -k 60 3000 nice -n 19 ionice -c3 python3 -I $H/t4d_passT_lat.py $LAT v3 dd $D" >> $H/out_lat${LAT}_$D.txt 2>&1; echo "$(date -u +%FT%TZ) passT FIN $D $(tail -1 $H/out_lat${LAT}_$D.txt | cut -c1-90)" >> $LOG
  done
  for n in 1 2 3; do
    python3 -I -c "import json,sys; sys.exit(0 if json.load(open('$H/cache/bfill${LAT}_man_$D.json')).get('estado')=='COMPLETE' else 1)" 2>/dev/null && break
    [ -s $H/cache/passT$LAT/RT_v3dd_$D.pkl ] || break
    bash $G --check || { sleep 120; continue; }
    bash $CP bash $G python3 -I $H/t4d_b_f5v2.py $D $LAT >> $H/out_bf${LAT}_$D.txt 2>&1; echo "$(date -u +%FT%TZ) bfill FIN $D $(tail -1 $H/out_bf${LAT}_$D.txt | cut -c1-110)" >> $LOG
  done
done; echo "$(date -u +%FT%TZ) ===== FIN run_b_lat $LAT" >> $LOG
