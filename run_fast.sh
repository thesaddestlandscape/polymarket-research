#!/usr/bin/env bash
# run_fast.sh — Dos velocidades + batch git:
#   Ciclo rápido (~20-23s total): klines + predict + 4x micro-reintento live_trade
#   Ciclo lento  (cada 3er ciclo ~60s): + resolve + postmortem + resumen
#   Git batch    (cada ≥5min, aprobado Javi 08-Jul): commit+push agrupado —
#                antes commiteaba cada ciclo lento (~1100 commits/día, .git 1.1GB,
#                autostash/carreras de push constantes). El trading NO cambia:
#                los CSVs se escriben a disco cada 20s igual que siempre.
#
# Micro-reintento live_trade (2026-07-10, hallazgo latencia): perfilado real
# mostró que klines+predict+live_trade tardan ~3s de trabajo real dentro de un
# ciclo de ~20-23s — el resto es sleep puro. El libro de estos mercados (~9
# bots de market-making activos 24/7, ver project_hallazgo_latencia_10jul)
# fluctúa de profundidad en segundos, así que reintentar la MISMA señal
# pendiente solo una vez cada ~20-23s (antes) desperdiciaba ese margen: una
# señal necesitaba 4-5 ciclos completos (80-115s) para tener 4-5 oportunidades
# de pasar el veto_profundidad, justo cuando SENAL_MAX_LATENCIA_SEG=100 la
# caduca. Ahora: klines+predict UNA vez (cadencia sin cambios, no toca
# resolve/postmortem/git-batch), pero live_trade se reintenta 4x espaciado
# ~4-5s DENTRO del mismo ciclo — mismas ~15-20 oportunidades ahora caben en
# los 100s de vida de la señal, en vez de 4-5. Presupuesto total del ciclo
# rápido se mantiene ~igual (~20-23s) para no alterar la cadencia de
# resolve/postmortem/resumen/git-batch (atados a CICLO%3, no a tiempo).
# Código de seguridad live — no minimizar. NO toca live_trade.py: la propia
# invalidación por latencia (SENAL_MAX_LATENCIA_SEG) ya acota los reintentos.
# Arrancar con: screen -S fast bash run_fast.sh

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$REPO_DIR/.venv/bin/python"
LOG="$REPO_DIR/logs/fast.log"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG"; }

log "=== Proceso FAST arrancado (ciclo rápido ~20s / lento cada 3 / live_trade 4x micro-reintento) ==="

CICLO=0
LAST_GIT=0
GIT_BATCH_S=300
while true; do
    CICLO=$((CICLO + 1))

    # ── CICLO RÁPIDO: siempre ────────────────────────────────────────────
    $PYTHON "$REPO_DIR/fetch_binance_klines.py"   >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/shadow_predict.py"         >> "$LOG" 2>&1 || true
    for _ in 1 2 3 4; do
        $PYTHON "$REPO_DIR/live_trade.py"         >> "$LOG" 2>&1 || true
        sleep 4
    done

    # ── CICLO LENTO: cada 3 ciclos (~60s) ───────────────────────────────
    if [ $((CICLO % 3)) -eq 0 ]; then
        $PYTHON "$REPO_DIR/shadow_resolve.py"     >> "$LOG" 2>&1 || true
        $PYTHON "$REPO_DIR/shadow_postmortem.py"  >> "$LOG" 2>&1 || true
        $PYTHON "$REPO_DIR/shadow_resumen.py"     >> "$LOG" 2>&1 || true

        NOW=$(date +%s)
        if [ $((NOW - LAST_GIT)) -ge $GIT_BATCH_S ]; then
            LAST_GIT=$NOW
            cd "$REPO_DIR"
            # rebase huérfano (ej. `timeout 60s` matando un rebase a medias) --
            # limpiar ANTES de intentar uno nuevo, si no el pull de abajo lo
            # hereda arrastrado indefinidamente (encontrado 27-Jul, cruft de
            # semanas acumulado en .git/rebase-merge + git stash list).
            if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
                log "  ⚠️ rebase huérfano en .git -- limpiando antes de continuar"
                git rebase --abort >> "$LOG" 2>&1 || rm -rf .git/rebase-merge .git/rebase-apply
                # 28-Jul: --abort no siempre repone el autostash asociado si
                # el proceso murió a medias (visto: 82 stashes acumulados,
                # uno con un trade real perdido). Red de seguridad: si el
                # árbol quedó limpio tras el abort y hay un stash esperando,
                # intentar recuperarlo -- si aplica limpio, genial; si no,
                # se deja en el stash (nunca se descarta) para revisión
                # manual en vez de perderse en silencio.
                if git diff --quiet && git diff --cached --quiet \
                        && [ -n "$(git stash list 2>/dev/null | head -1)" ]; then
                    log "  ⚠️ árbol limpio tras abort con stash pendiente -- intentando recuperarlo"
                    git stash pop >> "$LOG" 2>&1 \
                        && log "  ✅ stash recuperado" \
                        || log "  ⚠️ stash no aplica limpio -- se deja en git stash list para revisión manual"
                fi
            fi
            # 28-Jul: data/prices/ faltaba aquí -- fetch_binance_klines.py lo
            # escribe cada ciclo rápido (~20s) pero solo run_slow.sh lo
            # añadía (cadencia ~23min), así que quedaba sucio entre medias.
            # git pull --rebase --autostash de abajo SIEMPRE tenía algo real
            # que stashear (no un no-op); si `timeout 60s` mataba el pull a
            # mitad de rebase, ese autostash quedaba huérfano para siempre
            # -- encontrado 28-Jul: 82 stashes acumulados, uno de ellos con
            # un trade real (BALLENAS_TARDIAS#ETH#5min, ganador +0.26€) que
            # nunca llegó a trades.csv ni al dashboard. Añadirlo aquí deja
            # el árbol de trabajo limpio tras el commit, así que el
            # autostash no tiene nada que perder aunque el pull muera.
            git add data/shadow/ data/live/ data/prices/ >> "$LOG" 2>&1 || true
            if ! git diff --cached --quiet 2>/dev/null; then
                timeout 30s git commit -m "shadow: ciclo $CICLO $(date -u +%Y-%m-%dT%H:%MZ)" >> "$LOG" 2>&1 || true
                # 23-Jul (feedback_run_fast_git_rebase_pierde_trabajo_23jul):
                # -X ours bajo `rebase` favorece origin/main en conflictos --
                # correcto para datos (mismo criterio que "siempre --theirs"
                # de CLAUDE.md), pero CATASTRÓFICO si este directorio queda
                # checked out en una rama de feature (commits propios
                # descartados en silencio). Saltar pull/rebase/push si no
                # estamos en main -- el commit de datos de arriba se queda
                # igual en cualquier rama.
                if [ "$(git branch --show-current)" = "main" ]; then
                    timeout 60s git pull --rebase --autostash -X ours origin main >> "$LOG" 2>&1 || true
                    timeout 60s git push origin main >> "$LOG" 2>&1 || true
                else
                    log "  ⚠️ rama actual != main -- se salta pull/rebase/push (solo commit local de datos)"
                fi
            fi
        fi
    fi

    # sleep final reducido de 20s a 1s: el micro-loop de arriba (4×4s=16s) ya
    # ocupa el margen que antes absorbía este sleep — mantiene la cadencia
    # TOTAL del ciclo ~igual (~20-23s) para no correr resolve/postmortem/
    # git-batch con menos frecuencia wall-clock de la que tenían (atados a
    # CICLO%3, no a tiempo transcurrido).
    sleep 1
done
