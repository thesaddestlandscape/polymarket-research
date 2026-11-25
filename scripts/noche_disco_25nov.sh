#!/bin/bash
# noche_disco_25nov.sh -- tarea nocturna de UN solo uso (OK Javi 25-Nov), lanzada por at/cron a las 03:00Z con cron_pesado.
# 1) Acción B (PLAN_DISCO_RAM_24nov.md): borrar gz de libro5_ms/libro5_ms_prot con fecha < hoy-4 SOLO si su twin .zst
#    en keep_libro5_ms_prot_permanente existe y `cmp` del contenido descomprimido es idéntico (sin pérdida).
# 2) Repack de .git (25 packs, ~48 GB): bajo git_ops.lock, con guarda de disco (<15 GB libres => mata y limpia tmp_pack)
#    y tope de tiempo 2 h 30 min (debe acabar antes de las 06:00Z).
set -uo pipefail
V=/mnt/HC_Volume_106538179
KEEP=$V/keep_libro5_ms_prot_permanente
LOG=/root/polymarket-research-datalogs/noche_disco_25nov.log
REPO=/root/polymarket-research
libre_gb() { df -BG --output=avail "$V" | tail -1 | tr -dc 0-9; }
log() { echo "$(date -u +%FT%TZ) $*" >> "$LOG"; }

log "INICIO libre=$(libre_gb)G"
# ---------- 1) Acción B ----------
LIMITE=$(date -u -d '-4 days' +%F)
borrados=0; omitidos=0; fallos=0
for d in libro5_ms_prot libro5_ms; do
  for f in "$V/$d"/libro5_ms_*.csv.gz; do
    [ -f "$f" ] || continue
    b=$(basename "$f"); fe=$(echo "$b" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)
    [ -n "$fe" ] && [[ "$fe" < "$LIMITE" ]] || { omitidos=$((omitidos+1)); continue; }
    z="$KEEP/${b%.gz}.zst"
    if [ ! -s "$z" ]; then omitidos=$((omitidos+1)); continue; fi
    if fuser -s "$f" 2>/dev/null; then omitidos=$((omitidos+1)); log "abierto, se omite $f"; continue; fi
    if nice -n 19 ionice -c3 cmp -s <(gzip -dc "$f") <(zstd -dcq "$z"); then
      rm -f -- "$f" && borrados=$((borrados+1))
    else
      fallos=$((fallos+1)); log "CMP DISTINTO o error, NO se borra: $f"
    fi
  done
done
log "ACCION_B borrados=$borrados omitidos=$omitidos fallos_cmp=$fallos libre=$(libre_gb)G"

# ---------- 2) Repack de git ----------
cd "$REPO" || exit 1
GITDIR=$(git rev-parse --git-common-dir)
exec 200>data/shadow/git_ops.lock
if ! flock -w 600 200; then log "REPACK ABORTADO: git_ops.lock ocupado"; exit 0; fi
antes=$(du -sBG "$GITDIR/objects/pack" | cut -f1)
log "REPACK inicio packs=$(ls "$GITDIR"/objects/pack/*.pack | wc -l) tam=$antes libre=$(libre_gb)G"
timeout -k 30 9000 nice -n 19 ionice -c3 git -c pack.windowMemory=512m -c pack.threads=1 -c pack.deltaCacheSize=256m \
  repack -a -d --max-pack-size=2g >> "$LOG" 2>&1 &
RP=$!
while kill -0 $RP 2>/dev/null; do
  if [ "$(libre_gb)" -lt 15 ]; then log "GUARDA DISCO <15G: se mata el repack"; pkill -TERM -P $RP; kill -TERM $RP; break; fi
  sleep 30
done
wait $RP; rc=$?
if [ $rc -ne 0 ]; then
  find "$GITDIR/objects/pack" -maxdepth 1 -type f -name 'tmp_pack_*' -delete
  log "REPACK rc=$rc (fallido/abortado; tmp_pack limpiados; packs originales intactos)"
else
  git multi-pack-index write >> "$LOG" 2>&1; git prune-packed >> "$LOG" 2>&1
  log "REPACK OK"
fi
log "FIN packs=$(ls "$GITDIR"/objects/pack/*.pack | wc -l) tam=$(du -sBG "$GITDIR/objects/pack" | cut -f1) (antes $antes) libre=$(libre_gb)G"
