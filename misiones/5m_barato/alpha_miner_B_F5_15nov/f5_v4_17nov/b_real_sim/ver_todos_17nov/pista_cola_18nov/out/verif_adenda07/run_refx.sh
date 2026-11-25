#!/bin/bash
cd "$(dirname "$0")/../.."
for M in fxM1 fxM2; do ( ulimit -v 3000000; P7_NOTE=fixture_$M nice -n 19 ionice -c3 python3 p7_ipw_balance.py out/p1_btc_2026-11-12_$M.pkl out/p7_btc_2026-11-12_$M.json out/p7w_btc_2026-11-12_$M.pkl > out/verif_adenda07/p7_${M}_stdout.txt 2> out/verif_adenda07/p7_${M}_err.txt ); done
( ulimit -v 3000000; P3_DISENO=1 PISTA_SUF=_fxM1 nice -n 19 ionice -c3 timeout 1500 python3 p3_agrega.py btc act > out/verif_adenda07/p3_fxM1_stdout.txt 2> out/verif_adenda07/p3_fxM1_err.txt )
( ulimit -v 3000000; nice -n 19 ionice -c3 timeout 1200 python3 out/verif_adenda07/checks_H.py > out/verif_adenda07/checks_H_stdout.txt 2> out/verif_adenda07/checks_H_err.txt )
echo fin > out/verif_adenda07/run_refx.done
