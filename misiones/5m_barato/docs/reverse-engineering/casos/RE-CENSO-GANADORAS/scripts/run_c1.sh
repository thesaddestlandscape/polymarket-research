#!/bin/bash
# runner idempotente del censo (dias 05..25); guarda de carga dentro de c1_extrae.py (espera load5<4)
ulimit -v 3000000
cd "$(dirname "$0")"
exec nice -n 19 ionice -c3 python3 c1_extrae.py "$@" >> /mnt/HC_Volume_106538179/agentes_datos/re_censo/c1.log 2>&1
