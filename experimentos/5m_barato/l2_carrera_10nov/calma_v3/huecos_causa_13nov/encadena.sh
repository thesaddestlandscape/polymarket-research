#!/bin/bash
D=/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/huecos_causa_13nov
until grep -q 1124981 $D/out/seg_g.log 2>/dev/null; do sleep 20; done
bash $D/run_cortos.sh
