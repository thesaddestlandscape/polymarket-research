#!/bin/bash
cd /root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/re_f5_23nov; export RF5_OUT=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/re_f5_23nov/out_rf5_ciego/
for f in K K6; do bash lanza_pesado.sh out_rf5_ciego/v32_ident$f.log out_rf5_ciego/v32_pico_ident$f.txt python3 -I rf5_nulo_inc.py ident $f 2026-11-17; done
