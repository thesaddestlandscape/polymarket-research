#!/bin/bash
# PROPUESTA de cron (NO instalado): 00:25 UTC etiqueta AYER; fuera de 06-09Z. Telegram si falla (usar el helper del repo que ya usa l1_cron.sh).
# 25 0 * * * /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/scripts/regimen_cron.sh
ulimit -v 3000000
D=$(date -u -d "yesterday" +%F)
flock -n /tmp/regimen_etiquetas.lock nice -n 19 ionice -c3 python3 -I /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/scripts/etiquetar_regimen.py dia "$D" >> /root/polymarket-research-datalogs/regimen_5m/cron.log 2>&1 || echo "regimen_cron FALLO $D" >> /root/polymarket-research-datalogs/regimen_5m/cron.log
