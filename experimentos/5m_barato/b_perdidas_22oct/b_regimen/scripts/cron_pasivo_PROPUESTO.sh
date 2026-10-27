#!/bin/bash
# PROPUESTA (NO instalada; decide el chief): etiquetado pasivo B-REGIMEN. Linea de cron sugerida (despues del L1b y del etiquetador de regimen, fuera de 06-09Z):
#   50 10 * * * /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/b_regimen/scripts/cron_pasivo_PROPUESTO.sh >> /root/polymarket-research-datalogs/b_regimen_pasivo/cron.log 2>&1
H=$(date -u +%H); if [ "$H" -ge 6 ] && [ "$H" -lt 9 ]; then echo "fuera de horario"; exit 0; fi
mkdir -p /root/polymarket-research-datalogs/b_regimen_pasivo; ulimit -v 3000000
for k in 2 1; do D=$(date -u -d "-$k day" +%F); nice -n 19 ionice -c3 python3 -I "$(dirname "$0")/etiquetar_politica_regimen.py" dia "$D" || echo "FALLO etiquetado $D"; done
