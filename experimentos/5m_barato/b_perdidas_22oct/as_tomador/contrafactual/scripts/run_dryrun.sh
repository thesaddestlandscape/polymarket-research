#!/bin/bash
cd "$(dirname "$0")/.."
ulimit -v 3000000
/usr/bin/time -v nice -n 19 ionice -c3 python3 -I scripts/cf_diario.py --desde 2026-10-22 --hasta 2026-10-23 --tag dryrun > logs/dryrun_22_23.log 2> logs/dryrun_22_23.time
echo "exit $?" > logs/dryrun.done
