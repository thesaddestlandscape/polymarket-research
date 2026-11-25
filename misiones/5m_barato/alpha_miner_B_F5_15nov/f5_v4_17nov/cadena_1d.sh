#!/bin/bash
# cadena_1d.sh: espera passT 13-14 Nov -> bfill de esos dias -> t4d_c; y espera seg2 completo -> t4d_a2. Escribe cadena_1d.log
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov; cd $H; CP=/root/polymarket-research/scripts/cron_pesado.sh
until grep -q "FIN run_b_passT" run_b_passT.log; do sleep 30; done; echo "$(date -u +%FT%TZ) passT fin" >> cadena_1d.log
bash run_b_f5.sh; echo "$(date -u +%FT%TZ) bfill fin" >> cadena_1d.log
( ulimit -v 3000000; bash $CP nice -n 19 ionice -c3 python3 -I t4d_c.py > T4d_C.out 2>&1 ); echo "$(date -u +%FT%TZ) t4d_c fin" >> cadena_1d.log
until grep -q "FIN run_seg2" run_seg2.log; do sleep 30; done; echo "$(date -u +%FT%TZ) seg2 fin" >> cadena_1d.log
( ulimit -v 3500000; bash $CP nice -n 19 ionice -c3 python3 -I t4d_a2.py > T4d_A2.out 2>&1 ); echo "$(date -u +%FT%TZ) a2 fin" >> cadena_1d.log
