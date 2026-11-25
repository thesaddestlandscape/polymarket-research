#!/bin/bash
# run_b_f5.sh -- t4d_b_f5.py por dia (26-Oct..16-Nov), un job por dia via cron_pesado, idempotente (manifiesto cache/bfill_man_D.json). Espera hasta 3 h a que run_b_passT genere el RT de cada dia.
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov; LOG=$H/run_b_f5.log; G=$H/guard_v4.sh; CP=/root/polymarket-research/scripts/cron_pesado.sh
exec 8>$H/.run_b_f5.lock; flock -n 8 || exit 0
for i in $(seq 0 21); do D=$(date -u -d "2026-10-26 +$i day" +%F)
  for n in $(seq 1 90); do
    python3 -I -c "import json,sys; sys.exit(0 if json.load(open('$H/cache/bfill_man_$D.json')).get('estado')=='COMPLETE' else 1)" 2>/dev/null && [ -s $H/cache/bfill_$D.pkl ] && break
    [ -s /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/out_v4/RT_v3dd_$D.pkl ] || [ -s $H/cache/passT_out/RT_v3dd_$D.pkl ] || { grep -q "FIN run_b_passT" $H/run_b_passT.log 2>/dev/null && { echo "$(date -u +%FT%TZ) SIN RT $D" >> $LOG; break; }; sleep 120; continue; }
    bash $G --check || { sleep 120; continue; }
    echo "$(date -u +%FT%TZ) INICIO $D" >> $LOG; bash $CP bash $G python3 -I $H/t4d_b_f5.py $D >> $H/out_bf5_$D.txt 2>&1; echo "$(date -u +%FT%TZ) FIN $D rc=$? $(tail -1 $H/out_bf5_$D.txt | cut -c1-140)" >> $LOG
  done
done; echo "$(date -u +%FT%TZ) ===== FIN run_b_f5" >> $LOG
