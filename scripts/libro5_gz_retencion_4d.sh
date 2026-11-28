#!/bin/bash
# 27-Nov (PRIORIDAD 1 disco sdb, OK Javi): ACCION B de PLAN_DISCO_RAM_24nov.md hecha RECURRENTE (antes solo la ejecuto noche_disco_25nov.sh una vez, 27-Nov 03:07Z: 102 gz borrados, 0 fallos).
# Borra los gz de libro5_ms/ y libro5_ms_prot/ con fecha < hoy-4 SOLO si su twin .zst en keep_libro5_ms_prot_permanente existe y
# cmp(gzip -dc gz, zstd -dc zst) es identico; ficheros abiertos (fuser) se omiten. Sin pérdida: el contenido permanece en el zst permanente.
# NO toca git ni nada mas. Cron 03:35Z (tras keep_libro5_ms_prot.sh 00:45Z). nice 19 / ionice idle.
V=/mnt/HC_Volume_106538179; KEEP=$V/keep_libro5_ms_prot_permanente; LOG=/root/polymarket-research-datalogs/libro5_gz_retencion_4d.log
LIMITE=$(date -u -d '-4 days' +%F); borrados=0; omitidos=0; fallos=0
for d in libro5_ms_prot libro5_ms; do
  for f in "$V/$d"/libro5_ms_*.csv.gz; do
    [ -f "$f" ] || continue
    b=$(basename "$f"); fe=$(echo "$b" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)
    [ -n "$fe" ] && [[ "$fe" < "$LIMITE" ]] || { omitidos=$((omitidos+1)); continue; }
    z="$KEEP/${b%.gz}.zst"
    [ -s "$z" ] || { omitidos=$((omitidos+1)); continue; }
    if fuser -s "$f" 2>/dev/null; then omitidos=$((omitidos+1)); echo "$(date -u +%FT%TZ) abierto, se omite $f" >> "$LOG"; continue; fi
    if nice -n 19 ionice -c3 cmp -s <(gzip -dc "$f") <(zstd -dcq "$z"); then rm -f -- "$f" && borrados=$((borrados+1))
    else fallos=$((fallos+1)); echo "$(date -u +%FT%TZ) CMP DISTINTO o error, NO se borra: $f" >> "$LOG"; fi
  done
done
echo "$(date -u +%FT%TZ) libro5_gz_retencion_4d limite<$LIMITE borrados=$borrados omitidos=$omitidos fallos_cmp=$fallos libre=$(df -BG --output=avail $V | tail -1 | tr -d ' ')" >> "$LOG"
