#!/bin/bash
# git_maintenance_incremental.sh -- mantenimiento incremental de .git para
# que NUNCA vuelva a acumularse a un tamaño peligroso (evita repetir el
# incidente del 04-Ago: git gc monolítico agotando el disco).
#
# Distinto de scripts/git_gc_programado.sh (ese es el gc completo, pesado,
# de emergencia -- se deja como último recurso, ya no debería hacer falta
# con esto corriendo). `git maintenance` empaqueta solo los objetos sueltos
# NUEVOS desde la última pasada, en trozos pequeños -- cada corrida tarda
# segundos, no minutos, y no necesita headroom grande de disco.
#
# 04-Ago: .git vive en /mnt/HC_Volume_106538179 (volumen dedicado, 70GB,
# comprado tras el incidente de disco) -- este script asume ese volumen y
# comprueba su espacio libre, no el de `/`.
set -euo pipefail
cd /root/polymarket-research || exit 1

LOG=logs/git_maintenance.log
VOLUMEN=/mnt/HC_Volume_106538179
MIN_LIBRE_MB=2000  # suelo de seguridad en el volumen dedicado

libre_mb() { df --output=avail "$VOLUMEN" | tail -1 | awk '{print int($1/1024)}'; }

libre=$(libre_mb)
if [ "$libre" -lt "$MIN_LIBRE_MB" ]; then
  echo "$(date -u) ABORTADO: solo ${libre}MB libres en $VOLUMEN, esperando a la próxima pasada." >> "$LOG"
  exit 0
fi

echo "$(date -u) inicio (libre=${libre}MB)" >> "$LOG"
nice -n 10 git -c pack.windowMemory=100m -c pack.threads=1 maintenance run \
  --task=loose-objects --task=incremental-repack --task=commit-graph \
  >> "$LOG" 2>&1
echo "$(date -u) fin (libre=$(libre_mb)MB)" >> "$LOG"
