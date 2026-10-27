#!/bin/bash
# espera a que x1 termine (marca "fin" en x1.log) y lanza rasgos + evaluacion (PREREG_A1)
DL=/root/polymarket-research-datalogs/mitigar_as_25oct; cd "$(dirname "$0")/.."
until grep -q '^fin' $DL/x1.log 2>/dev/null; do sleep 30; done
ulimit -v 3000000
nice -n 19 ionice -c3 python3 scripts/a1_rasgos.py > datos/a1_rasgos.stdout 2>&1
nice -n 19 ionice -c3 python3 scripts/a1_eval.py > datos/a1_eval.stdout 2>&1
echo hecho $(date -u +%FT%TZ) >> datos/a1_eval.stdout
