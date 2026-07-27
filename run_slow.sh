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
    $PYTHON "$REPO_DIR/generate_report.py"  >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/arb_scanner.py"           >> "$LOG" 2>&1 || true
    # cross_platform_arb DESACTIVADO 2026-07-06: 6 días sin una sola opp accionable
    # real — todas Polymarket→Kalshi con liqB=0 (sin libro; Kalshi es US-only,
    # inaccesible desde el VPS finlandés). Generaba ~5MB/día de CSV humo. Reactivar
    # solo si se añade una plataforma con libro accesible y se exige liq>0 en ambas patas.
    # $PYTHON "$REPO_DIR/cross_platform_arb.py"    >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/combi_arb.py"             >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/combi_arb_prep.py"        >> "$LOG" 2>&1 || true

    # LLM hypothesis generator: solo una vez al día (ciclo 1 de cada día)
    HORA_UTC=$(date -u +%H)
    if [ "$HORA_UTC" -ge 20 ] && [ "$HORA_UTC" -le 21 ] && [ -n "$ANTHROPIC_API_KEY" ]; then
        log "  Ejecutando LLM hypothesis generator..."
        $PYTHON "$REPO_DIR/llm_hypothesis.py" >> "$LOG" 2>&1 || true
    fi

    # Git: precios, leaderboard e hipótesis LLM
    cd "$REPO_DIR"
    # rebase huérfano -- mismo guard que run_fast.sh, ver comentario ahí.
    if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
        log "  ⚠️ rebase huérfano en .git -- limpiando antes de continuar"
        git rebase --abort >> "$LOG" 2>&1 || rm -rf .git/rebase-merge .git/rebase-apply
    fi
    git add data/prices/ data/wallets/leaderboard_*.csv data/shadow/hipotesis_*.md data/shadow/hipotesis_pendientes.json data/shadow/arb_scan_*.csv data/shadow/cross_arb_*.csv data/shadow/combi_arb_*.csv data/shadow/combi_candidates.json >> "$LOG" 2>&1 || true
    if ! git diff --cached --quiet 2>/dev/null; then
        timeout 30s git commit -m "data: ciclo slow $CICLO $(date -u +%Y-%m-%dT%H:%MZ)" >> "$LOG" 2>&1 || true
        # 23-Jul (feedback_run_fast_git_rebase_pierde_trabajo_23jul): -X ours
        # bajo rebase favorece origin/main -- correcto para datos, pero
        # catastrófico si el directorio queda checked out en una rama de
        # feature (commits propios descartados en silencio). Saltar
        # pull/rebase/push fuera de main -- el commit de datos ya quedó hecho.
        if [ "$(git branch --show-current)" = "main" ]; then
            timeout 60s git pull --rebase --autostash -X ours origin main >> "$LOG" 2>&1 || true
            timeout 60s git push origin main >> "$LOG" 2>&1 || true
            log "  Push OK"
        else
            log "  ⚠️ rama actual != main -- se salta pull/rebase/push (solo commit local de datos)"
        fi
    fi

    log "--- Ciclo slow $CICLO completado ---"
done
