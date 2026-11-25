#!/bin/bash
# corrida COMPLETA de 12-Nov (dia de DISENO, etiqueta _DISENO): prueba de memoria (ulimit 3 GB) y de balance E a escala de dia. No es dia de veredicto.
cd "$(dirname "$0")/../.."
PISTA_SUF=_DISENO /root/polymarket-research/scripts/cron_pesado.sh bash -c "ulimit -v 3000000; nice -n 19 ionice -c3 python3 p1_dia.py 2026-11-12 btc" > out/verif_adenda07/p1_full12.log 2>&1
if [ -f out/p1_btc_2026-11-12_DISENO.pkl ]; then
 /root/polymarket-research/scripts/cron_pesado.sh bash -c "ulimit -v 3000000; nice -n 19 ionice -c3 python3 p7_ipw_balance.py out/p1_btc_2026-11-12_DISENO.pkl out/p7_btc_2026-11-12_DISENO.json out/p7w_btc_2026-11-12_DISENO.pkl" > out/verif_adenda07/p7_full12_stdout.txt 2> out/verif_adenda07/p7_full12_err.txt
fi
echo done > out/verif_adenda07/run_full12.done
