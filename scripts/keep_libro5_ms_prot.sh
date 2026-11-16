#!/bin/bash
# 16-Nov (Javi): copia PERMANENTE de libro5_ms_prot (que se suelta a los 12 d) en keep_libro5_ms_prot_permanente/ como zstd-9
# (~56 % del gzip). Cada fichero se verifica con cmp (descomprimido gz == descomprimido zst) antes de quitar el enlace duro
# antiguo de keep_; el original sigue en libro5_ms/prot hasta que rote. gz truncado (no verificable) -> enlace duro tal cual.
# Lectura: abrir_comprimido.abrir(path) o `zstd -dc`. Sin retencion: decidir con Javi (punto 3).
V=/mnt/HC_Volume_106538179; P=$V/libro5_ms_prot; K=$V/keep_libro5_ms_prot_permanente; mkdir -p "$K"; n=0; t=0; mal=0
for f in "$P"/libro5_*; do
  [ -e "$f" ] || continue; b=$(basename "$f"); z="$K/${b%.gz}.zst"
  [ -e "$z" ] && { rm -f "$K/$b"; continue; }
  if gzip -t "$f" 2>/dev/null; then
    nice -n 19 ionice -c3 sh -c "gzip -dc '$f' | zstd -9 -T1 -q -c > '$z.tmp'" || { rm -f "$z.tmp"; mal=$((mal+1)); continue; }
    if cmp -s <(gzip -dc "$f") <(zstd -dc "$z.tmp"); then touch -r "$f" "$z.tmp"; mv "$z.tmp" "$z"; rm -f "$K/$b"; n=$((n+1))
    else rm -f "$z.tmp"; echo "CMP NO COINCIDE: $b"; mal=$((mal+1)); fi
  else
    [ -e "$K/$b" ] || ln "$f" "$K/$b"; t=$((t+1))
  fi
done
echo "$(date -u +%FT%TZ) keep: zstd_nuevos=$n truncados_enlazados=$t fallos=$mal total=$(ls $K | wc -l) $(du -sh $K | cut -f1)"
