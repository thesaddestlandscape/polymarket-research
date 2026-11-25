#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/huecos_fix_13nov
./runday.sh hora 2026-11-12
./runday.sh hole60 2026-11-12 2026-11-11 2026-11-10 2026-11-09 2026-11-08 2026-11-07 2026-11-06 2026-11-05 2026-11-04 2026-11-03 2026-11-02
echo CHAIN_DONE > out/chain_done.txt
