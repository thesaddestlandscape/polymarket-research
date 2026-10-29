#!/bin/bash
ulimit -v 4500000
cd /root/polymarket-research/experimentos/5m_barato/formula_r11_29oct/validacion
zcat /mnt/HC_Volume_106538179/libro5_ms/libro5_ms_2026-10-23_331840.csv.gz | grep -F -f toks23.txt | gzip -1 > /root/polymarket-research-datalogs/calibracion_etiqueta/l2_b23_libro5.csv.gz
echo FIN $? > extrae.done
