#!/bin/bash
# espera a que termine el runner A (pid en out_v2/run_A.pid) sin poner su nombre en la linea de comandos
P=$(cat /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/out_v2/run_A.pid)
while kill -0 "$P" 2>/dev/null; do sleep 60; done
tail -3 /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/out_v2/run_A.log
