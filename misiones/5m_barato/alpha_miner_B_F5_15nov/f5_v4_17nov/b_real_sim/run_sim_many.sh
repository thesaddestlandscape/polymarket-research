#!/bin/bash
# run_sim_many.sh "DIA1 DIA2 .." -- un dia a la vez via run_sim.sh (cron_pesado). Env heredado.
for d in $1; do "$(dirname "$(readlink -f "$0")")/run_sim.sh" $d; done
