#!/usr/bin/env bash
# git_batch_sync.sh — Lógica compartida de commit+push por lotes, con
# recuperación de emergencia ante rebase huérfano / push rechazado.
#
# 18-Ago: extraído de run_fast.sh/run_fast_mantenimiento.sh y run_slow.sh,
# que llevaban cada uno su propia copia casi idéntica de este bloque
# (~100 líneas, historial de incidentes reales documentado en cada commit
# desde el 28-Jul) -- CLAUDE.md regla 6 ("escribir código que ya existe").
# Un solo fichero significa que un fix futuro (como los de 28/30-Jul) se
# aplica una vez, no dos veces con riesgo de que diverjan en silencio.
#
# Uso: se ejecuta en un subshell `( ... )` por el caller, NUNCA se hace
# `source` directo -- así el `exit 0` de "lock ocupado" corta solo el
# subshell, no el loop entero que lo invoca (mismo patrón que los
# bloques originales). El caller decide CUÁNDO llamar a este script
# (throttle propio, si aplica -- run_fast_mantenimiento.sh usa
# GIT_BATCH_S porque su cadencia (~45s) es mucho más rápida de lo que el
# commit/push necesita; run_slow.sh no necesita throttle porque su propia
# cadencia (~15min) ya lo es).
#
# Argumentos: COMMIT_MSG STASH_LABEL ADD_PATH... -- STASH_PATH...
#   COMMIT_MSG    mensaje de commit (con ciclo/timestamp ya interpolados)
#   STASH_LABEL   sufijo del stash de emergencia (ej. "fast"/"slow")
#   ADD_PATH...   rutas para `git add` (antes del separador --)
#   STASH_PATH... ámbito EXPLÍCITO del stash de emergencia (después de --,
#                 nunca el árbol entero -- ver comentario en el bloque de
#                 recuperación más abajo)
#
# LOG y REPO_DIR deben venir ya exportados/definidos por el caller.
set -u

COMMIT_MSG="$1"; shift
STASH_LABEL="$1"; shift
ADD_PATHS=()
while [ "$1" != "--" ]; do
    ADD_PATHS+=("$1"); shift
done
shift  # consume --
STASH_PATHS=("$@")

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG"; }

# ⚠️ `date +%s%3N` en este sistema NO trunca a milisegundos (imprime
# nanosegundos completos) -- $EPOCHREALTIME (builtin bash 5.x) es fiable;
# el prefijo 10# fuerza base-10 para no interpretar un 0 inicial como octal.
now_ms() {
    local t=$EPOCHREALTIME
    local sec=${t%.*}
    local usec=${t#*.}
    usec=${usec:0:3}
    echo $(( 10#$sec * 1000 + 10#$usec ))
}

cd "$REPO_DIR"

# GIT_LOCK (28-Jul, causa raíz de los stashes huérfanos que se repitieron
# 3 veces en una sola sesión pese al fix del mismo día): los loops fast/
# slow/mantenimiento hacían CADA UNO su propio add→commit→push sobre el
# MISMO repo, sin ninguna exclusión mutua. Un lock compartido serializa
# TODA mutación de git entre ellos -- ya no puede haber dos rebases en
# vuelo a la vez. flock BLOQUEANTE (no -n): preferimos que este ciclo
# espere un poco a que el otro loop termine, antes que saltarse la
# sincronización -- con tope de 120s para no colgar el caller indefinidamente.
_t_lock0=$(now_ms)
exec 200>"$REPO_DIR/data/shadow/git_ops.lock"
if ! flock -w 120 200; then
    log "  ⚠️ git_ops.lock ocupado >120s -- se salta este ciclo de sync, se reintenta el siguiente"
    exit 0
fi
_t_lock1=$(now_ms)
log "  ⏱ git_ops.lock adquirido en $((_t_lock1 - _t_lock0))ms"

# rebase huérfano (ej. `timeout` matando un rebase a medias) -- limpiar
# ANTES de intentar uno nuevo, si no el rebase de emergencia de abajo lo
# hereda arrastrado indefinidamente (encontrado 27-Jul).
if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
    log "  ⚠️ rebase huérfano en .git -- limpiando antes de continuar"
    git rebase --abort >> "$LOG" 2>&1 || rm -rf .git/rebase-merge .git/rebase-apply
    # 28-Jul: --abort no siempre repone el autostash si el proceso murió a
    # medias. 30-Jul: quitada la precondición de "árbol limpio" (299
    # stashes huérfanos encontrados en vivo -- con ~10 procesos
    # persistentes escribiendo data/shadow|live|prices sin parar, esa
    # precondición casi nunca se cumple). git stash pop ya es seguro con
    # ruido de fondo -- se intenta siempre que haya un stash pendiente.
    if [ -n "$(git stash list 2>/dev/null | head -1)" ]; then
        log "  ⚠️ rebase huérfano con stash pendiente -- intentando recuperarlo"
        git stash pop >> "$LOG" 2>&1 \
            && log "  ✅ stash recuperado" \
            || log "  ⚠️ stash no aplica limpio -- se deja en git stash list para revisión manual"
    fi
fi

_t_add0=$(now_ms)
git add "${ADD_PATHS[@]}" >> "$LOG" 2>&1 || true
_t_add1=$(now_ms)
log "  ⏱ git add: $((_t_add1 - _t_add0))ms"

if ! git diff --cached --quiet 2>/dev/null; then
    N_STAGED=$(git diff --cached --name-only 2>/dev/null | wc -l)
    _t_commit0=$(now_ms)
    timeout -k 10 30s git commit -m "$COMMIT_MSG" >> "$LOG" 2>&1 || true
    _t_commit1=$(now_ms)
    log "  ⏱ git commit ($N_STAGED ficheros): $((_t_commit1 - _t_commit0))ms"
    # 23-Jul: -X ours bajo rebase favorece origin/main -- correcto para
    # datos, pero CATASTRÓFICO si este directorio queda checked out en una
    # rama de feature (commits propios descartados en silencio). Saltar
    # pull/rebase/push si no estamos en main.
    if [ "$(git branch --show-current)" = "main" ]; then
        # 30-Jul: push directo (fast-forward, no toca el árbol de trabajo).
        # Solo si el push es rechazado se entra en recuperación de
        # emergencia, con stash de ÁMBITO EXPLÍCITO (nunca el árbol entero
        # -- ver idea_git_autostash_trades_perdidos_30jul).
        _t_push0=$(now_ms)
        if ! timeout -k 10 60s git push origin main >> "$LOG" 2>&1; then
            _t_push1=$(now_ms)
            log "  ⏱ git push (fallido): $((_t_push1 - _t_push0))ms"
            # 30-Jul: el push también falla por motivos que NO son
            # divergencia (.git grande -> OOM, red). Comprobar con
            # rev-list si origin realmente avanzó ANTES de tocar el árbol.
            timeout -k 10 30s git fetch origin main >> "$LOG" 2>&1 || true
            DIVERGIO=$(git rev-list HEAD..origin/main --count 2>/dev/null || echo 0)
            if [ "$DIVERGIO" -gt 0 ] 2>/dev/null; then
                log "  ⚠️ push rechazado y origin SÍ avanzó ($DIVERGIO commits) -- recuperación de emergencia"
                STASH_EMERG=0
                if ! git diff --quiet -- "${STASH_PATHS[@]}" 2>/dev/null \
                   || ! git diff --cached --quiet -- "${STASH_PATHS[@]}" 2>/dev/null; then
                    git stash push -m "git_ops_emergencia_${STASH_LABEL}" -- "${STASH_PATHS[@]}" >> "$LOG" 2>&1 \
                        && STASH_EMERG=1
                fi
                if timeout -k 10 60s git rebase -X ours origin/main >> "$LOG" 2>&1; then
                    log "  ✅ rebase de emergencia OK"
                    if [ "$STASH_EMERG" = "1" ]; then
                        git stash pop >> "$LOG" 2>&1 \
                            && log "  ✅ stash de emergencia recuperado" \
                            || log "  ⚠️ stash de emergencia no aplica limpio -- revisión manual (git stash list)"
                    fi
                    timeout -k 10 60s git push origin main >> "$LOG" 2>&1 \
                        && log "  ✅ push tras recuperación OK" \
                        || log "  ⚠️ push tras recuperación sigue fallando -- revisar manualmente"
                else
                    log "  ⚠️ rebase de emergencia falló (probable: cambios sin commitear fuera del ámbito del stash) -- abortando sin forzar, revisar manualmente"
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
            _t_push1=$(now_ms)
            log "  ⏱ git push (OK): $((_t_push1 - _t_push0))ms"
        fi
    else
        log "  ⚠️ rama actual != main -- se salta push (solo commit local de datos)"
    fi
fi
log "  ⏱ git batch TOTAL (lock+add+commit+push): $(($(now_ms) - _t_lock0))ms"
