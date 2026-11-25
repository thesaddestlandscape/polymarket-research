#!/bin/bash
cd "$(dirname "$0")/../.."
( ulimit -v 3000000; nice -n 19 ionice -c3 python3 p7_ipw_balance.py out/p1_btc_2026-11-12_DISENO.pkl out/p7_btc_2026-11-12_DISENO.json out/p7w_btc_2026-11-12_DISENO.pkl > out/verif_adenda07/p7_full12_stdout.txt 2> out/verif_adenda07/p7_full12_err.txt )
echo $? > out/verif_adenda07/run_p7_full12.done
