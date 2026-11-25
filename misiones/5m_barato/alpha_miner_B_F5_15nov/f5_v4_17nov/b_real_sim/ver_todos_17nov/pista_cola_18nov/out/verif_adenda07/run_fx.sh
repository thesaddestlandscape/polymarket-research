#!/bin/bash
# fixture 12-Nov 03:40-06:40Z (DISENO), dos corridas con el MISMO codigo para comprobar semilla estable
cd "$(dirname "$0")/../.."
FX=/tmp/claude-0/-root-polymarket-research/5055698c-f1c6-493f-8e00-51095bf98a56/scratchpad/fx3h/fx3h.csv.gz
for S in M1 M2; do
 PISTA_SUF=_fx$S PISTA_FILES=$FX /root/polymarket-research/scripts/cron_pesado.sh bash -c "ulimit -v 3000000; nice -n 19 ionice -c3 python3 p1_dia.py 2026-11-12 btc" > out/verif_adenda07/p1_fx$S.log 2>&1
done
echo done > out/verif_adenda07/run_fx.done
