#!/usr/bin/env bash
# run_fast.sh — Dos velocidades:
#   Ciclo rápido (cada ~20s): klines + predict + live_trade
#   Ciclo lento  (cada 3er ciclo ~60s): + resolve + postmortem + resumen + git
# Arrancar con: screen -S fast bash run_fast.sh

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$REPO_DIR/.venv/bin/python"
LOG="$REPO_DIR/logs/fast.log"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG"; }

log "=== Proceso FAST arrancado (ciclo rápido 20s / lento cada 3) ==="

CICLO=0
while true; do
    CICLO=$((CICLO + 1))

    # ── CICLO RÁPIDO: siempre ────────────────────────────────────────────
    $PYTHON "$REPO_DIR/fetch_binance_klines.py"   >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/shadow_predict.py"         >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/live_trade.py"             >> "$LOG" 2>&1 || true

    # ── CICLO LENTO: cada 3 ciclos (~60s) ───────────────────────────────
    if [ $((CICLO % 3)) -eq 0 ]; then
        $PYTHON "$REPO_DIR/shadow_resolve.py"     >> "$LOG" 2>&1 || true
        $PYTHON "$REPO_DIR/shadow_postmortem.py"  >> "$LOG" 2>&1 || true
        $PYTHON "$REPO_DIR/shadow_resumen.py"     >> "$LOG" 2>&1 || true

        cd "$REPO_DIR"
        git add data/shadow/ data/live/ >> "$LOG" 2>&1 || true
        if ! git diff --cached --quiet 2>/dev/null; then
            timeout 30s git commit -m "shadow: ciclo $CICLO $(date -u +%Y-%m-%dT%H:%MZ)" >> "$LOG" 2>&1 || true
            timeout 60s git pull --rebase -X ours origin main >> "$LOG" 2>&1 || true
            timeout 60s git push origin main >> "$LOG" 2>&1 || true
        fi
    fi

    sleep 20
done
