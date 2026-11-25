#!/bin/bash
# run_seg2.sh -- t4d_seg2.py por dia (09-Oct..14-Nov) via cron_pesado (cgroup), idempotente, un dia por job, espera si no hay calma.
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov; LOG=$H/run_seg2.log; G=$H/guard_v4.sh; CP=/root/polymarket-research/scripts/cron_pesado.sh
exec 8>$H/.run_seg2.lock; flock -n 8 || exit 0
for i in $(seq 18 37) $(seq 1 17); do D=$(date -u -d "2026-10-08 +$i day" +%F)
  for n in $(seq 1 30); do
    python3 -I -c "import json,sys; sys.exit(0 if json.load(open('$H/cache/seg2man_$D.json')).get('estado')=='COMPLETE' else 1)" 2>/dev/null && [ -s $H/cache/seg2_$D.npz ] && break
    [ "$(date -u +%H%M)" -ge 2330 ] && { echo "$(date -u +%FT%TZ) hora>=23:30Z: paro en $D" >> $LOG; exit 0; }
    bash $G --check || { sleep 120; continue; }
    echo "$(date -u +%FT%TZ) INICIO $D" >> $LOG; bash $CP bash $G python3 -I $H/t4d_seg2.py $D >> $H/out_seg2_$D.txt 2>&1; echo "$(date -u +%FT%TZ) FIN $D rc=$? $(tail -1 $H/out_seg2_$D.txt | cut -c1-120)" >> $LOG
  done
done; echo "$(date -u +%FT%TZ) ===== FIN run_seg2" >> $LOG
