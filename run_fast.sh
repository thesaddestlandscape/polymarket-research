#!/usr/bin/env bash
# run_fast.sh — Bucle rápido: klines → predict → resolve cada 60s
# Arrancar con: screen -S fast bash run_fast.sh

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$REPO_DIR/.venv/bin/python"
LOG="$REPO_DIR/logs/fast.log"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG"; }

log "=== Proceso FAST arrancado ==="

CICLO=0
while true; do
    CICLO=$((CICLO + 1))

    $PYTHON "$REPO_DIR/fetch_binance_klines.py"   >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/shadow_predict.py"         >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/shadow_resolve.py"         >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/shadow_postmortem.py"      >> "$LOG" 2>&1 || true

    # Git: solo datos shadow (binance está en .gitignore)
    cd "$REPO_DIR"
    git add data/shadow/ >> "$LOG" 2>&1 || true
    if ! git diff --cached --quiet 2>/dev/null; then
        git commit -m "shadow: ciclo $CICLO $(date -u +%Y-%m-%dT%H:%MZ)" >> "$LOG" 2>&1 || true
        git pull --rebase origin main >> "$LOG" 2>&1 || true
        git push origin main >> "$LOG" 2>&1 || true
    fi

    sleep 60
done
