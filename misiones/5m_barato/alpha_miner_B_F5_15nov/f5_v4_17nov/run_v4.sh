#!/bin/bash
# run_v4.sh -- bucle idempotente y reanudable de t2_dia_v4.py sobre 38 dias (08-Oct..14-Nov; 08-Oct, 16-Oct y 24-Oct solo histograma). Log: run_v4.log; salida por dia en cache/. Lanzar: setsid nohup bash run_v4.sh > /dev/null 2>&1 &
# Un dia COMPLETE valido se salta (t2_dia_v4 lo comprueba). rc 75 (sin ventana/calma): espera y reintenta; rc 137 (OOM): UN reintento tras 10 min; rc 1/3 (assert / desenlace pendiente): sin reintento, queda anotado. Se para si pasan las 23:30Z.
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov; LOG=$H/run_v4.log; G=$H/guard_v4.sh; CP=/root/polymarket-research/scripts/cron_pesado.sh
cd $H || exit 9
exec 8>$H/.run_v4.lock; flock -n 8 || { echo "$(date -u +%FT%TZ) otra instancia de run_v4: salgo" >> $LOG; exit 0; }
export ARROW_DEFAULT_MEMORY_POOL=system MALLOC_MMAP_THRESHOLD_=262144 MALLOC_TOP_PAD_=0 MALLOC_ARENA_MAX=2 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 MALLOC_TRIM_THRESHOLD_=262144
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
cd $H && sha256sum -c --status SPEC_F5_V4_17nov.sha256 || { log "ABORTO: SPEC modificada tras el sellado"; exit 8; }
{ echo "$(date -u +%FT%TZ) run_v4 arranca; sha de codigo:"; sha256sum run_v4.sh guard_v4.sh t2_dia_v4.py suelo_causal.py SPEC_F5_V4_17nov.md ../exp1/lib1.py ../lib_ev.py; } >> $H/MANIFEST_V4.txt
FALLOS=""; PEND=""
for i in $(seq 0 37); do D=$(date -u -d "2026-10-08 +$i day" +%F)
  case $D in 2026-10-08|2026-10-16|2026-10-24) EXTRA="--solo-hist";; *) EXTRA="";; esac
  for intento in 1 2 3 4 5 6 7 8; do
    [ "$(date -u +%H%M)" -ge 2330 ] && { log "hora >= 23:30Z: PARO antes de $D"; PEND="$PEND $D"; break; }
    bash $G --check || { log "espera ventana/calma ($(bash $G --estado))"; sleep 120; continue; }
    log "INICIO $D $EXTRA $(bash $G --estado)"
    bash $CP bash $G python3 -I $H/t2_dia_v4.py $D $EXTRA >> $H/out_$D.txt 2>&1; rc=$?
    log "FIN $D rc=$rc: $(tail -1 $H/out_$D.txt | cut -c1-240)"
    [ $rc -eq 0 ] && break
    if [ $rc -eq 137 ] || [ $rc -eq 124 ] || [ $rc -eq 75 ]; then sleep 600; continue; fi
    FALLOS="$FALLOS $D(rc=$rc)"; break
  done
  [ $rc -ne 0 ] && PEND="$PEND $D"
done
log "===== FIN run_v4 FALLOS/PENDIENTES=[$FALLOS |$PEND ]"
