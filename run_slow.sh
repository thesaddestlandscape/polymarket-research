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
  (
    # GIT_LOCK (28-Jul): mismo candado compartido que run_fast.sh -- ver el
    # comentario extenso ahí. run_fast (~5min) y run_slow (aquí, cada ciclo)
    # hacían cada uno su propio add→commit→pull --rebase --autostash→push
    # sin exclusión mutua; si coincidían, sus rebases se entrelazaban y el
    # autostash de uno podía quedar huérfano cuando el otro avanzaba la rama
    # en paralelo. flock BLOQUEANTE con tope 120s -- preferible esperar un
    # poco a arriesgar otro huérfano.
    exec 200>"$REPO_DIR/data/shadow/git_ops.lock"
    if ! flock -w 120 200; then
        log "  ⚠️ git_ops.lock ocupado >120s (run_fast.sh probablemente sincronizando) -- se salta este ciclo de sync"
        exit 0
    fi
    # rebase huérfano (ej. `timeout 60s` matando el rebase de emergencia a
    # medias) -- mismo guard que run_fast.sh, ver comentario extenso ahí.
    if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
        log "  ⚠️ rebase huérfano en .git -- limpiando antes de continuar"
        git rebase --abort >> "$LOG" 2>&1 || rm -rf .git/rebase-merge .git/rebase-apply
        # 30-Jul: mismo fix que run_fast.sh -- quitada la precondición de
        # "árbol limpio" (299 stashes huérfanos encontrados en vivo, la
        # precondición casi nunca se cumplía con ~10 procesos persistentes
        # escribiendo continuamente). git stash pop ya es seguro con ruido
        # de fondo -- se intenta siempre que haya un stash pendiente.
        if [ -n "$(git stash list 2>/dev/null | head -1)" ]; then
            log "  ⚠️ rebase huérfano con stash pendiente -- intentando recuperarlo"
            git stash pop >> "$LOG" 2>&1 \
                && log "  ✅ stash recuperado" \
                || log "  ⚠️ stash no aplica limpio -- se deja en git stash list para revisión manual"
        fi
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
            # 30-Jul: eliminado el pull/rebase/autostash de la ruta común --
            # mismo cambio y mismo razonamiento que run_fast.sh (ver comentario
            # extenso ahí). fast/slow comparten este working directory y nadie
            # más pushea a origin/main en operación normal, así que el pull era
            # innecesario en ~99% de los ciclos y la fuente real de los stashes
            # huérfanos (conflictos con los ~10 procesos sin candado) y de la
            # pérdida de código real del 30-Jul (autostash barría el árbol
            # entero, incluyendo ediciones manuales sin commitear). Ahora: push
            # directo; solo si lo rechazan se entra en recuperación de
            # emergencia con stash de ámbito explícito.
            if ! timeout 60s git push origin main >> "$LOG" 2>&1; then
                # 30-Jul (mismo hallazgo que run_fast.sh, encontrado minutos tras
                # desplegar esto): el push también falla por motivos que NO son
                # divergencia (.git de 12GB, OOM) -- comprobar con rev-list si
                # origin realmente tiene commits nuevos antes de tocar el árbol,
                # si no los tiene no hay nada que reconciliar.
                timeout 30s git fetch origin main >> "$LOG" 2>&1 || true
                DIVERGIO=$(git rev-list HEAD..origin/main --count 2>/dev/null || echo 0)
                if [ "$DIVERGIO" -gt 0 ] 2>/dev/null; then
                    log "  ⚠️ push rechazado y origin SÍ avanzó ($DIVERGIO commits) -- recuperación de emergencia"
                    STASH_EMERG=0
                    if ! git diff --quiet -- data/shadow data/live data/prices data/wallets 2>/dev/null \
                       || ! git diff --cached --quiet -- data/shadow data/live data/prices data/wallets 2>/dev/null; then
                        git stash push -m "git_ops_emergencia_slow" -- data/shadow data/live data/prices data/wallets >> "$LOG" 2>&1 \
                            && STASH_EMERG=1
                    fi
                    if timeout 60s git rebase -X ours origin/main >> "$LOG" 2>&1; then
                        log "  ✅ rebase de emergencia OK"
                        if [ "$STASH_EMERG" = "1" ]; then
                            git stash pop >> "$LOG" 2>&1 \
                                && log "  ✅ stash de emergencia recuperado" \
                                || log "  ⚠️ stash de emergencia no aplica limpio -- revisión manual (git stash list)"
                        fi
                        timeout 60s git push origin main >> "$LOG" 2>&1 \
                            && log "  ✅ push tras recuperación OK" \
                            || log "  ⚠️ push tras recuperación sigue fallando -- revisar manualmente"
                    else
                        log "  ⚠️ rebase de emergencia falló (probable: cambios sin commitear fuera de data/shadow|live|prices|wallets) -- abortando sin forzar, revisar manualmente"
                        git rebase --abort >> "$LOG" 2>&1 || true
                        if [ "$STASH_EMERG" = "1" ]; then
                            git stash pop >> "$LOG" 2>&1 \
                                && log "  ✅ stash de emergencia recuperado tras abort" \
                                || log "  ⚠️ stash de emergencia no aplica limpio -- revisión manual (git stash list)"
                        fi
                    fi
                else
                    log "  ⚠️ push falló pero origin NO avanzó -- no es divergencia (probable OOM/red/tamaño de .git), se reintenta el siguiente ciclo sin tocar el árbol"
                fi
            else
                log "  Push OK"
            fi
        else
            log "  ⚠️ rama actual != main -- se salta push (solo commit local de datos)"
        fi
    fi
  )

    log "--- Ciclo slow $CICLO completado ---"
done
