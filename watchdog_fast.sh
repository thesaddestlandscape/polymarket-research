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

log "ALERTA: último commit data/shadow/ hace ${AGE_S}s (>${MAX_SILENCE_S}s). Reiniciando loop fast..."
screen -S fast -X quit 2>/dev/null || true
sleep 2
screen -dmS fast bash "$REPO_DIR/run_fast.sh"
log "Loop fast reiniciado."
