#!/bin/bash
cd /root/polymarket-research
D=experimentos/5m_barato/b_perdidas_22oct/captura_eventos_nivel
ulimit -v 3000000
nice -n 19 ionice -c3 python3 -I $D/ciclo_vida_W.py --dia 2026-10-22 --tx 0x83b1b2e9df9b4d659263d255207a93bf7d08f4f0f2e80e2a0125800f536a707b > $D/demo_fill_ETH_22oct.txt 2>&1
nice -n 19 ionice -c3 python3 -I $D/ciclo_vida_W.py --dia 2026-10-23 --n 40 --seed 11 --pmin 0.03 --pmax 0.4 --min-acc 10 --hora-desde 14:00 --hora-hasta 16:30 --lote --ventana-ant 120 > $D/lote_23oct.txt 2>&1
