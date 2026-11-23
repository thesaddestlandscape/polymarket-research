#!/bin/bash
cd "$(dirname "$0")/.."; O=out_rf5_ciego
ulimit -v 5000000
/root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 /usr/bin/time -v -o $O/pico_acople_17nov.txt python3 -I rf5_acople_real.py 2026-11-17 30 > $O/acople_real_17nov.log 2>&1
echo "FIN rc=$?" >> $O/acople_real_17nov.log
