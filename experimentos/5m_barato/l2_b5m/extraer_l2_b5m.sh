#!/bin/bash
# extraer_l2_b5m.sh DIA [ORIG] [DEST] : extracto diario del plano de B (bids <= PMAX=0,40 de TODOS los tokens 5m, T y G integras)
# a libro5_b40/. v2 (10-Nov): lectura TOLERANTE de gzip truncado (l2_gzcat.py: lee hasta el punto de corrupcion, descarta la
# linea parcial, cuenta filas perdidas en libro5_b40_DIA.stats.json, nunca escribe basura). Idempotente (.tmp+rename).
# Cron 00:50Z (extrae AYER). Solo LEE libro5_ms (enlaces duros protegidos).
set -u
D="$(cd "$(dirname "$0")" && pwd)"
DIA="$1"
exec python3 -I "$D/l2_extraer_dia.py" "$DIA" --orig "${2:-/mnt/HC_Volume_106538179/libro5_ms}" --dest "${3:-/mnt/HC_Volume_106538179/libro5_b40}" --pmax "${PMAX:-0.40}"
