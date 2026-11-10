#!/bin/bash
# 10-Nov: el escritor de libro5_ms borra por presupuesto (20 GB, ~6 d). Enlaces duros (mismo volumen, 0 GB extra) de los
# dias COMPLETOS recientes a libro5_ms_prot/ para que no se pierdan antes de extraer; se sueltan a los 12 dias (10-Nov, Javi: mitigar rotacion).
L=/mnt/HC_Volume_106538179/libro5_ms; P=/mnt/HC_Volume_106538179/libro5_ms_prot; mkdir -p "$P"
hoy=$(date -u +%F)
for f in "$L"/libro5_ms_*.csv.gz "$L"/libro5_tx_*.csv.gz; do
  [ -e "$f" ] || continue; b=$(basename "$f")
  d=$(echo "$b" | grep -oE '20[0-9]{2}-[0-9]{2}-[0-9]{2}' | head -1)
  [ -n "$d" ] && [ "$d" != "$hoy" ] && [ ! -e "$P/$b" ] && ln "$f" "$P/$b"
done
find "$P" -maxdepth 1 -name 'libro5_*' -mtime +12 -delete
echo "$(date -u +%FT%TZ) prot: $(ls $P | wc -l) ficheros $(du -sh $P | cut -f1) (enlaces duros)"
