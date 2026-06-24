#!/usr/bin/env bash
# run_slow.sh — Bucle lento: markets + wallets + trades cada ~15 min
# Arrancar con: screen -S slow bash run_slow.sh

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$REPO_DIR/.venv/bin/python"
LOG="$REPO_DIR/logs/slow.log"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG"; }

log "=== Proceso SLOW arrancado ==="

CICLO=0
while true; do
    CICLO=$((CICLO + 1))
    log "--- Ciclo slow $CICLO ---"

    # capture_markets tiene su propio bucle interno de 10 capturas × 60s ≈ 10 min
    $PYTHON "$REPO_DIR/capture_markets.py"  >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/capture_wallets.py"  >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/capture_trades.py"   >> "$LOG" 2>&1 || true

    # Git: precios y leaderboard (archivos pequeños rastreados en GitHub)
    # markets, trades y positions están en .gitignore por ser demasiado grandes
    cd "$REPO_DIR"
    git add data/prices/ data/wallets/leaderboard_*.csv >> "$LOG" 2>&1 || true
    if ! git diff --cached --quiet 2>/dev/null; then
        git commit -m "data: ciclo slow $CICLO $(date -u +%Y-%m-%dT%H:%MZ)" >> "$LOG" 2>&1 || true
        git pull --rebase origin main >> "$LOG" 2>&1 || true
        git push origin main >> "$LOG" 2>&1 || true
        log "  Push OK"
    fi

    log "--- Ciclo slow $CICLO completado ---"
done
