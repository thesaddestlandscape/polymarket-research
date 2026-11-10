#!/bin/bash
nice -n 19 ionice -c3 /root/polymarket-research/scripts/cron_pesado.sh bash /root/polymarket-research/experimentos/5m_barato/db1/aceptacion_quemados.sh
