#!/usr/bin/env bash
# watchdog_fast.sh — Vigila los DOS loops desacoplados (18-Ago) por separado:
#   - 'fast' (predict/live_trade): señal de vida = klines_HOY.json fresco.
#   - 'mantenimiento' (resolve/postmortem/resumen/git): señal de vida =
#     strategy_params.json fresco (exclusivo de shadow_postmortem.py --
#     antes era "último commit en data/shadow/", pero run_slow.sh también
#     commitea ahí, ver /code-review 18-Ago más abajo).
# Cron: */5 * * * * /root/polymarket-research/watchdog_fast.sh
#
# 18-Ago: antes de desacoplar, un solo chequeo (staleness de commit)
# bastaba porque TODO el pipeline era una única cadena secuencial -- un
# hang en cualquier punto paraba los commits. Ahora 'fast' puede seguir
# generando señales/operando con dinero real aunque 'mantenimiento' esté
# colgado (los commits pararían mientras 'fast' sigue sano), Y viceversa
# ('mantenimiento' puede seguir commiteando datos viejos aunque 'fast' esté
# colgado, si resolve/postmortem no dependen de klines nuevos para correr)
# -- un solo chequeo de staleness de commit ya NO detecta un 'fast' colgado
# de forma fiable. Dos señales de vida independientes, una por loop.

REPO_DIR="/root/polymarket-research"
LOG="$REPO_DIR/logs/watchdog.log"
MAX_SILENCE_S=900   # 15 min sin strategy_params.json fresco → loop
                    # 'mantenimiento' muerto (shadow_postmortem.py lo
                    # reescribe cada ciclo, ~45-90s -- margen amplio de
                    # sobra, heredado del umbral original de 08-Jul cuando
                    # la señal todavía era el commit de git)
MAX_KLINES_SILENCE_S=300  # 5 min sin klines_HOY.json fresco → loop 'fast'
                          # muerto (klines se escribe cada ciclo, ~20-23s).
                          # ⚠️ DELIBERADAMENTE duplicado del MAX_PRED_SILENCE
                          # de pipeline_watchdog.py (mismo valor, 300): son
                          # dos redes de seguridad independientes con
                          # propósitos distintos -- pipeline_watchdog.py solo
                          # usa esta señal para escanear fast.log en busca de
                          # errores conocidos (nunca reinicia 'fast' por
                          # puro silencio sin un patrón de error reconocido);
                          # este script SÍ reinicia por silencio solo, para
                          # cubrir un hang sin traceback identificable. Si se
                          # retoca uno, retocar el otro a mano -- no hay
                          # config compartida entre bash/python por una sola
                          # constante.

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" >> "$LOG"; }

# /code-review (18-Ago, hallazgo real): `stat -c %Y "$f" 2>/dev/null ||
# echo "$(date +%s)"` fallaba ABIERTO (edad=0, "recién escrito") si el
# fichero pasaba el `-f` pero `stat` fallaba por una carrera (rotado/
# borrado justo entre medias) -- inconsistente con la rama "fichero
# ausente" de al lado, que sí falla cerrado (999999). Un 'fast' colgado de
# verdad que coincidiera con esa carrera quedaría enmascarado como sano.
# Este helper falla SIEMPRE cerrado (999999) si `stat` no puede leer el
# mtime, sea cual sea el motivo.
edad_fichero_segundos() {
    local f="$1" mtime
    mtime=$(stat -c %Y "$f" 2>/dev/null) || { echo 999999; return; }
    echo $(( $(date +%s) - mtime ))
}

# 06-Ago: janitor de .git/index.lock huérfano -- INCIDENTE REAL el mismo día:
# un lock quedó huérfano a las 03:57 UTC (proceso que lo creó murió/fue matado
# sin limpiar) y bloqueó TODOS los commits/pushes del fast loop durante 2h29min
# en silencio (cada ciclo fallaba con "fatal: Unable to create index.lock" y
# seguía, `|| true` en run_fast.sh). Nadie lo detectó porque restart_fast_seguro.sh
# solo reinicia el PROCESO, no toca el lock en disco -- un fast nuevo pega
# contra el mismo lock y sigue fallando igual (verificado en vivo: reiniciado a
# las 06:15, siguió fallando hasta que se borró el lock a mano a las 06:26).
# Petición explícita de Javi tras el incidente: "no puede volver a pasar".
# Umbral 180s = 3x el timeout más largo de git en run_fast.sh (push, 60s) --
# ningún commit/push legítimo debería tardar más; fuser confirma que NINGÚN
# proceso tiene el fichero abierto antes de tocarlo (nunca borra un lock activo).
GIT_LOCK="$REPO_DIR/.git/index.lock"
GIT_LOCK_MAX_AGE_S=180
if [ -f "$GIT_LOCK" ]; then
    LOCK_AGE_S=$(( $(date +%s) - $(stat -c %Y "$GIT_LOCK" 2>/dev/null || echo "$(date +%s)") ))
    if [ "$LOCK_AGE_S" -gt "$GIT_LOCK_MAX_AGE_S" ]; then
        if fuser "$GIT_LOCK" >/dev/null 2>&1; then
            log "⚠️ .git/index.lock presente hace ${LOCK_AGE_S}s pero un proceso lo tiene abierto -- no se toca."
        else
            log "🚨 .git/index.lock HUÉRFANO hace ${LOCK_AGE_S}s (sin proceso activo) -- bloqueaba todos los commits/pushes. Eliminando."
            rm -f "$GIT_LOCK"
            python3 - "$LOCK_AGE_S" <<'PYEOF' >> "$LOG" 2>&1
import sys
sys.path.insert(0, "/root/polymarket-research")
try:
    from shadow_digest import enviar_telegram
    edad = sys.argv[1]
    enviar_telegram(
        f"🚨 watchdog_fast: .git/index.lock huérfano ({edad}s) eliminado "
        f"automáticamente -- estaba bloqueando TODOS los commits/pushes del "
        f"fast loop. Verificar que los commits se reanudan (git log -1)."
    )
except Exception as e:
    print(f"(no se pudo avisar por Telegram: {e})")
PYEOF
        fi
    fi
fi

# Nadie más vigila la screen 'watchdog' (pipeline_watchdog.py) — si muere no
# puede reiniciarse a sí misma, y sin ella se pierden rotación de logs, disco,
# sintaxis y freno por ventana en silencio. Barrido de coherencia 17-Jul.
if ! screen -ls | grep -q '\.watchdog\s'; then
    log "ALERTA: screen 'watchdog' caída. Reiniciando..."
    screen -dmS watchdog bash -c "cd $REPO_DIR && python3 pipeline_watchdog.py"
    log "Screen 'watchdog' reiniciada."
fi

# ── Chequeo 1: loop 'fast' (predict/live_trade, dinero real) ────────────
# Señal de vida propia, independiente de git -- klines_HOY.json lo escribe
# fetch_binance_klines.py cada ciclo (~20-23s), sin pasar por 'mantenimiento'.
KLINES_JSON="$REPO_DIR/data/binance/klines_$(date -u +%Y-%m-%d).json"
if [ -f "$KLINES_JSON" ]; then
    KLINES_AGE_S=$(edad_fichero_segundos "$KLINES_JSON")
else
    # /code-review (18-Ago, hallazgo real): justo tras medianoche UTC, el
    # fichero de HOY puede no existir todavía (fetch_binance_klines.py tarda
    # hasta ~20s en crearlo) -- sin este fallback, un cron que caiga en ese
    # hueco de segundos ve "ausente" = silencio máximo y reinicia un loop
    # 'fast' perfectamente sano con posiciones reales abiertas. Si el
    # fichero de AYER sigue fresco (el loop lo escribió hace poco, todavía
    # no ha rotado), eso ya demuestra que el loop está vivo.
    KLINES_JSON_AYER="$REPO_DIR/data/binance/klines_$(date -u -d '1 day ago' +%Y-%m-%d).json"
    if [ -f "$KLINES_JSON_AYER" ]; then
        KLINES_AGE_S=$(edad_fichero_segundos "$KLINES_JSON_AYER")
    else
        KLINES_AGE_S=999999  # ni hoy ni ayer existen -- tratar como máximo silencio
    fi
fi

if [ "$KLINES_AGE_S" -gt "$MAX_KLINES_SILENCE_S" ]; then
    log "ALERTA: klines_HOY.json sin actualizar hace ${KLINES_AGE_S}s (>${MAX_KLINES_SILENCE_S}s). Reiniciando loop fast..."
    # 21-Jul: la lógica de reinicio seguro (chequeo orden_en_curso + espera/
    # verificación antes de matar + kill por PID+grupo como red de seguridad)
    # vive ahora en restart_fast_seguro.sh -- único punto de verdad, también
    # invocado por pipeline_watchdog.py. No duplicar esta lógica aquí.
    "$REPO_DIR/restart_fast_seguro.sh"
    case $? in
        0) log "Loop fast reiniciado." ;;
        1) log "Reinicio pospuesto (orden en curso, o ya había otra invocación en marcha)." ;;
        3) log "🚨 CARRERA REAL: hay 2+ screens 'fast' vivas tras el reinicio — revisar manualmente YA." ;;
        *) log "Reinicio de 'fast' falló (no se pudo limpiar la screen vieja) — ver logs/watchdog.log arriba." ;;
    esac
fi

# ── Chequeo 2: loop 'mantenimiento' (resolve/postmortem/resumen/git) ────
# restart_mantenimiento_seguro.sh es el único punto de verdad para
# reiniciar esta screen (mismo motivo que restart_fast_seguro.sh para
# 'fast': dos disparadores independientes -- este cron y pipeline_
# watchdog.py -- no deben poder crear una screen duplicada cada uno por
# su lado). No duplicar esa lógica aquí.
#
# /code-review (18-Ago, hallazgo real): la señal original era "último
# commit tocando data/shadow/" -- pero run_slow.sh TAMBIÉN commitea bajo
# data/shadow/ (hipotesis_*.md, arb_scan_*.csv, combi_*.csv vía
# git_batch_sync.sh) con su propia cadencia independiente (~15min), así
# que un 'slow' vivo podía mantener AGE_S bajo mientras 'mantenimiento'
# llevaba colgado horas -- exactamente el incidente de shadow_postmortem.py
# atascado (CLAUDE.md pt.18) que este chequeo existe para detectar. Señal
# corregida: mtime de strategy_params.json, que SOLO shadow_postmortem.py
# escribe (dentro de 'mantenimiento', nunca 'slow') -- mismo patrón que el
# chequeo 1 de arriba (klines_HOY.json, exclusivo de 'fast').
PARAMS_JSON="$REPO_DIR/data/shadow/strategy_params.json"
if [ -f "$PARAMS_JSON" ]; then
    AGE_S=$(edad_fichero_segundos "$PARAMS_JSON")
else
    AGE_S=999999
fi

if [ "$AGE_S" -ge "$MAX_SILENCE_S" ]; then
    log "ALERTA: strategy_params.json sin actualizar hace ${AGE_S}s (>${MAX_SILENCE_S}s). Reiniciando loop mantenimiento..."
    "$REPO_DIR/restart_mantenimiento_seguro.sh"
    case $? in
        0) log "Loop mantenimiento reiniciado." ;;
        1) log "Reinicio pospuesto (otra invocación ya en marcha)." ;;
        *) log "🚨 Reinicio de 'mantenimiento' falló -- ver logs/watchdog.log arriba." ;;
    esac
fi
