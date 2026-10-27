#!/bin/bash
# s2: filas q/t del registro ms de los tokens 60m (grep -F por token), un fichero de salida por fichero fuente; idempotente.
D=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/fav_60m_4h/datos; O=/mnt/HC_Volume_106538179/agentes_datos/fav60_ms; mkdir -p $O
ulimit -v 3000000; export LC_ALL=C
for f in $(ls /mnt/HC_Volume_106538179/maker_ms_crudo/maker_ms_2026-10-1[2-8]_*.csv.gz /mnt/HC_Volume_106538179/datalogs_auto/maker_ms_2026-10-*.csv.gz /root/polymarket-research-datalogs/maker_ms_2026-10-2[45]_*.csv.gz 2>/dev/null | xargs -n1 realpath | sort -u); do
  b=$(basename $f .csv.gz); [ -s $O/$b.60m.gz ] && continue
  case $b in maker_ms_2026-10-25_1191885) continue;; esac   # fichero vivo
  zcat $f 2>/dev/null | python3 -I /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/fav_60m_4h/scripts/s2_filtro.py $D/tokens60.txt | gzip -1 > $O/$b.60m.gz.tmp && mv $O/$b.60m.gz.tmp $O/$b.60m.gz
  echo "$(date -u +%T) $b $(stat -c %s $O/$b.60m.gz)"
done
echo FIN
