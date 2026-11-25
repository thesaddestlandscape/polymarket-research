#!/bin/bash
# run_verif.sh  (env V5_ARR V5_CANC B_EX_ALTA B_EX_CANC V5_DSEND ...)  -- 4 dias 20-23 Oct, un job por dia via cron_pesado (cgroup+flock), nice 19, ionice 3. Idempotente (verif_v5 sale si el pkl existe). NO lanzar 06-09Z.
H=$(dirname "$(readlink -f "$0")"); h=$(date -u +%H); [ "$h" -ge 6 ] && [ "$h" -lt 9 ] && { echo "06-09Z: no se lanza"; exit 3; }
for d in 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do
  nice -n 19 ionice -c3 /root/polymarket-research/scripts/cron_pesado.sh bash -c "ulimit -v 6000000; cd $H; python3 verif_v5.py $d" >> $H/logs_verif_$(date -u +%F).log 2>&1
done
