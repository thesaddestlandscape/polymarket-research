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
          (
            # GIT_LOCK (28-Jul, causa raíz de los stashes huérfanos que se
            # repitieron 3 veces en una sola sesión pese al fix del mismo día):
            # run_fast.sh (aquí, cada ~5min) y run_slow.sh (cada ~23min) hacían
            # CADA UNO su propio add→commit→pull --rebase --autostash→push
            # sobre el MISMO repo, sin ninguna exclusión mutua entre ellos. Si
            # ambos caían casi a la vez, sus rebases se entrelazaban: el pop
            # del autostash de uno podía acabar en un commit de merge que el
            # OTRO, avanzando la rama por su cuenta en paralelo, dejaba fuera
            # de la historia de HEAD -- huérfano para siempre, exactamente el
            # patrón ya diagnosticado (feedback_incidente_autostash_trade_
            # perdido_28jul) pero nunca cerrado de raíz hasta ahora. Un lock
            # compartido serializa TODA mutación de git entre los dos loops:
            # ya no puede haber dos rebases en vuelo a la vez, así que un
            # stash de cualquiera de los dos siempre hace pop limpio antes de
            # que el otro toque nada. flock BLOQUEANTE (no -n): preferimos que
            # este ciclo espere un poco a que el otro loop termine, antes que
            # saltarse la sincronización -- con tope de 120s para no colgar
            # el ciclo rápido indefinidamente si algo va realmente mal.
            exec 200>"$REPO_DIR/data/shadow/git_ops.lock"
            if ! flock -w 120 200; then
                log "  ⚠️ git_ops.lock ocupado >120s (run_slow.sh probablemente sincronizando) -- se salta este ciclo de sync, se reintenta el siguiente"
                exit 0
            fi
            # rebase huérfano (ej. `timeout 60s` matando un rebase a medias) --
            # limpiar ANTES de intentar uno nuevo, si no el rebase de emergencia
            # de abajo lo hereda arrastrado indefinidamente (encontrado 27-Jul,
            # cruft de semanas acumulado en .git/rebase-merge + git stash list).
            if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
                log "  ⚠️ rebase huérfano en .git -- limpiando antes de continuar"
                git rebase --abort >> "$LOG" 2>&1 || rm -rf .git/rebase-merge .git/rebase-apply
                # 28-Jul: --abort no siempre repone el autostash asociado si
                # el proceso murió a medias. 30-Jul (Javi: "aquí está pasando
                # algo", trades desapareciendo del dashboard): encontrados 299
                # stashes huérfanos acumulados EN VIVO -- la condición "árbol
                # limpio" de abajo casi NUNCA se cumple en este sistema (hay
                # ~10 procesos persistentes escribiendo data/shadow y
                # data/live continuamente, así que siempre hay algo
                # modificado), así que la recuperación NUNCA se intentaba en
                # la práctica pese a decir "nunca se pierde en silencio".
                # `git stash pop` en sí ya es seguro con ruido de fondo (solo
                # falla si hay conflicto de HUNK en el mismo fichero/líneas,
                # y si falla deja el stash intacto para revisión manual) --
                # se quita la precondición de árbol limpio, se intenta
                # SIEMPRE que haya un stash pendiente tras el abort.
                if [ -n "$(git stash list 2>/dev/null | head -1)" ]; then
                    log "  ⚠️ rebase huérfano con stash pendiente -- intentando recuperarlo"
                    git stash pop >> "$LOG" 2>&1 \
                        && log "  ✅ stash recuperado" \
                        || log "  ⚠️ stash no aplica limpio -- se deja en git stash list para revisión manual"
                fi
            fi
            # 28-Jul: data/prices/ faltaba aquí -- fetch_binance_klines.py lo
            # escribe cada ciclo rápido (~20s) pero solo run_slow.sh lo
            # añadía (cadencia ~23min), así que quedaba sucio entre medias.
            # Se mantiene incluido aunque el 30-Jul se quitó el pull/rebase de
            # la ruta común (ver más abajo) -- sigue haciendo falta para que
            # el commit local capture también los precios, no solo shadow/live.
            git add data/shadow/ data/live/ data/prices/ >> "$LOG" 2>&1 || true
            if ! git diff --cached --quiet 2>/dev/null; then
                timeout -k 10 30s git commit -m "shadow: ciclo $CICLO $(date -u +%Y-%m-%dT%H:%MZ)" >> "$LOG" 2>&1 || true
                # 23-Jul (feedback_run_fast_git_rebase_pierde_trabajo_23jul):
                # -X ours bajo `rebase` favorece origin/main en conflictos --
                # correcto para datos (mismo criterio que "siempre --theirs"
                # de CLAUDE.md), pero CATASTRÓFICO si este directorio queda
                # checked out en una rama de feature (commits propios
                # descartados en silencio). Saltar pull/rebase/push si no
                # estamos en main -- el commit de datos de arriba se queda
                # igual en cualquier rama.
                if [ "$(git branch --show-current)" = "main" ]; then
                    # 30-Jul: eliminado el pull/rebase/autostash de la ruta común.
                    # Causa raíz investigada a fondo el mismo día: fast/slow NO son
                    # clones separados, comparten este MISMO working directory, y en
                    # operación normal NADIE MÁS pushea a origin/main (verificado:
                    # únicos autores de los commits recientes = este loop; los otros
                    # 2 clones del repo están dormidos). El pull era un round-trip de
                    # red innecesario en ~99% de los ciclos, y la ventana stash->pop
                    # que abría era la causa real de dos problemas: (a) conflictos
                    # con los ~10 procesos sin candado que escriben data/shadow|live|
                    # prices sin parar, y (b) el autostash barría CUALQUIER edición
                    # manual sin commitear que hubiera en el árbol -- perdió código
                    # real el mismo 30-Jul (ver idea_git_autostash_trades_perdidos_30jul,
                    # recuperado en el commit 03bc454443). Ahora: push directo
                    # (fast-forward, no toca el árbol de trabajo -- nada que estashear
                    # en el caso común). Solo si el push es rechazado (raro: origin
                    # avanzó desde otro sitio) se entra en recuperación de emergencia,
                    # con stash de ÁMBITO EXPLÍCITO (solo data/shadow|live|prices,
                    # nunca el árbol entero) -- si hay algo sucio FUERA de esas rutas
                    # (ej. una edición de código a medias), el rebase de abajo se
                    # niega a correr (git rebase exige árbol limpio) y falla alto en
                    # vez de tragárselo, coherente con fail-loud.
                    if ! timeout -k 10 60s git push origin main >> "$LOG" 2>&1; then
                        # 30-Jul (encontrado en vivo minutos después de desplegar
                        # este mecanismo): el push también falla por motivos que NO
                        # son divergencia -- el .git de 12GB hace que `git push`
                        # muera por OOM (ya diagnosticado, 129 commits sin subir
                        # antes de este fix). Entrar en la recuperación de
                        # emergencia (fetch+stash+rebase) SIN comprobar primero si
                        # origin realmente avanzó recreaba el mismo problema que
                        # esto vino a resolver -- 2 stashes en 6 minutos. Ahora se
                        # comprueba con `git fetch` + `rev-list` si origin tiene
                        # commits que local no tiene ANTES de tocar el árbol; si no
                        # los tiene, el push falló por otra causa (tamaño/red/OOM)
                        # y no hay nada que reconciliar -- se deja para el siguiente
                        # ciclo, sin stash.
                        timeout -k 10 30s git fetch origin main >> "$LOG" 2>&1 || true
                        DIVERGIO=$(git rev-list HEAD..origin/main --count 2>/dev/null || echo 0)
                        if [ "$DIVERGIO" -gt 0 ] 2>/dev/null; then
                            log "  ⚠️ push rechazado y origin SÍ avanzó ($DIVERGIO commits) -- recuperación de emergencia"
                            STASH_EMERG=0
                            if ! git diff --quiet -- data/shadow data/live data/prices 2>/dev/null \
                               || ! git diff --cached --quiet -- data/shadow data/live data/prices 2>/dev/null; then
                                git stash push -m "git_ops_emergencia_fast" -- data/shadow data/live data/prices >> "$LOG" 2>&1 \
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
                                log "  ⚠️ rebase de emergencia falló (probable: cambios sin commitear fuera de data/shadow|live|prices) -- abortando sin forzar, revisar manualmente"
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
                    fi
                else
                    log "  ⚠️ rama actual != main -- se salta push (solo commit local de datos)"
                fi
            fi
          )
        fi
    fi

    # sleep final reducido de 20s a 1s: el micro-loop de arriba (4×4s=16s) ya
    # ocupa el margen que antes absorbía este sleep — mantiene la cadencia
    # TOTAL del ciclo ~igual (~20-23s) para no correr resolve/postmortem/
    # git-batch con menos frecuencia wall-clock de la que tenían (atados a
    # CICLO%3, no a tiempo transcurrido).
    sleep 1
done
