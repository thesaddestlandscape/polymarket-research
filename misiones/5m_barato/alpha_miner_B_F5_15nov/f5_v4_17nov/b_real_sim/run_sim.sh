#!/bin/bash
# run_sim.sh DIA  (env B_POLICY B_DEC_RX B_D_ALTA B_EX_ALTA B_D_CANC B_EX_CANC B_DET_FILL ...) -- un dia por job, via cron_pesado (cgroup+flock), nice 19, ionice 3, ulimit -v 6 GB. NO lanzar 06-09Z. Idempotente (manifiesto COMPLETE).
H=$(dirname "$(readlink -f "$0")"); h=$(date -u +%H); [ "$h" -ge 6 ] && [ "$h" -lt 9 ] && { echo "06-09Z: no se lanza"; exit 3; }
nice -n 19 ionice -c3 /root/polymarket-research/scripts/cron_pesado.sh bash -c "ulimit -v 6000000; cd $H; python3 b_policy_sim.py $1" >> $H/logs_sim_$(date -u +%F).log 2>&1
