#!/bin/bash
# run_seg.sh -- bucle idempotente de t4_dia_seg.py (09-Oct..14-Nov, 37 dias). Misma politica que run_v4.sh (guard_v4, cron_pesado, ulimit 3 GB) pero verifica el manifiesto tras cada dia (cron_pesado devuelve 0 si OMITE). Log run_seg.log.
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov; LOG=$H/run_seg.log; G=$H/guard_v4.sh; CP=/root/polymarket-research/scripts/cron_pesado.sh; cd $H || exit 9
exec 8>$H/.run_seg.lock; flock -n 8 || exit 0
export ARROW_DEFAULT_MEMORY_POOL=system MALLOC_MMAP_THRESHOLD_=262144 MALLOC_TOP_PAD_=0 MALLOC_ARENA_MAX=2 OMP_NUM_THREADS=1
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
for i in $(seq 1 37); do D=$(date -u -d "2026-10-08 +$i day" +%F)
  for n in $(seq 1 12); do
    python3 -I -c "import json,sys; sys.exit(0 if json.load(open('cache/segman_$D.json')).get('estado')=='COMPLETE' else 1)" 2>/dev/null && { [ -s cache/seg_$D.npz ] && break; }
    [ "$(date -u +%H%M)" -ge 2330 ] && { log "hora>=23:30Z: paro en $D"; exit 0; }
    bash $G --check || { sleep 120; continue; }
    log "INICIO $D"; bash $CP bash $G python3 -I $H/t4_dia_seg.py $D >> $H/out_seg_$D.txt 2>&1; log "FIN $D rc=$? $(tail -1 $H/out_seg_$D.txt | cut -c1-120)"
  done
done; log "===== FIN run_seg"
