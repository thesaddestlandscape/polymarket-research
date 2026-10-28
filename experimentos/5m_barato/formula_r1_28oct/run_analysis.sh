#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/formula_r1_28oct
ulimit -v 3000000
nice -n 19 ionice -c3 python3 -u analysis.py > analysis_salida.txt 2>&1
echo FIN_ANALISIS >> analysis_salida.txt
