#!/bin/bash
# Lanza el constructor de dataset de colocación (H43) en cadena, un día cada vez, con RAM acotada y espera de hueco (MemAvailable>2,5 GB,
# load<16, fuera de 06:00-09:15Z). Reanuda solo: los días con caché válida se saltan. Uso: bash lanzar_dataset.sh [dias_separados_por_coma]
cd /root/polymarket-research || exit 1
DIAS=${1:-2026-10-10,2026-10-09,2026-10-08,2026-10-07,2026-10-06,2026-10-05,2026-10-14,2026-10-15,2026-10-16}
OUT=/root/polymarket-research-datalogs/m5_maker_colocacion
mkdir -p "$OUT"
ulimit -v 2000000
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
nice -n 19 ionice -c3 python3 experimentos/5m_barato/colocacion_17oct/coloc_dataset.py --esperar --dias "$DIAS" --out "$OUT" >> "$OUT/driver.log" 2>&1
echo "$(date -u +%FT%TZ) driver rc=$?" >> "$OUT/driver.log"
