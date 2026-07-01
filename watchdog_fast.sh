#!/usr/bin/env bash
# watchdog_fast.sh — Reinicia el loop fast si lleva más de 10min sin commits.
# Cron: */5 * * * * /root/polymarket-research/watchdog_fast.sh

REPO_DIR="/root/polymarket-research"
LOG="$REPO_DIR/logs/watchdog.log"
MAX_SILENCE_S=600   # 10 minutos sin commit → loop muerto

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" >> "$LOG"; }

LAST_COMMIT_TS=$(git -C "$REPO_DIR" log -1 --format="%ct" -- data/shadow/ 2>/dev/null || echo 0)
AGE_S=$(( $(date +%s) - LAST_COMMIT_TS ))

if [ "$AGE_S" -lt "$MAX_SILENCE_S" ]; then
    exit 0  # Commit reciente — el loop vive
fi

# No matar la screen si hay una orden real en vuelo hacia el CLOB ahora mismo
# (live_trade.py escribe/borra este marker justo antes/después de post_order).
# Sin esto, matar "fast" a mitad de una orden ya enviada al exchange deja la
# posición sin registrar en trades.csv y permite re-operar el mismo mercado.
MARKER="$REPO_DIR/data/live/orden_en_curso.json"
if [ -f "$MARKER" ]; then
    MARKER_TS=$(python3 -c "
import json, sys
from datetime import datetime, timezone
try:
    d = json.load(open('$MARKER'))
    ts = datetime.fromisoformat(d['ts']).timestamp()
    print(int(datetime.now(timezone.utc).timestamp() - ts))
except Exception:
    print(99999)
" 2>/dev/null || echo 99999)
    if [ "$MARKER_TS" -lt 180 ]; then
        log "AVISO: orden en curso hace ${MARKER_TS}s — se pospone el reinicio de 'fast' este ciclo."
        exit 0
    fi
    log "AVISO: marker orden_en_curso.json obsoleto (${MARKER_TS}s) — probablemente el proceso murió a mitad de una orden. Revisar trades.csv manualmente."
fi

log "ALERTA: último commit data/shadow/ hace ${AGE_S}s (>${MAX_SILENCE_S}s). Reiniciando loop fast..."
screen -S fast -X quit 2>/dev/null || true
sleep 2
screen -dmS fast bash "$REPO_DIR/run_fast.sh"
log "Loop fast reiniciado."
