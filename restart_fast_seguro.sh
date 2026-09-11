#!/usr/bin/env bash
# restart_fast_seguro.sh — Único punto de verdad para reiniciar la screen
# 'fast' (dinero real: live_trade.py corre dentro de su loop).
#
# Origen (21-Jul): duplicados reales en results.csv (FAVORITO_CONFIRMADO#
# 2866629#BUY_YES 11-Jul, LATE_WINDOW_5MIN#2998086#BUY_NO 21-Jul) causados
# por 'fast' reiniciada dos veces casi a la vez -- watchdog_fast.sh (cron
# */5min) mataba la screen por NOMBRE y solo esperaba 2s antes de crear
# una nueva; si el proceso viejo estaba a mitad de un git push/pull
# --rebase (hasta 60s de timeout en run_fast.sh), 2s no bastaban, dejando
# 2 screens 'fast' vivas corriendo shadow_resolve.py en paralelo.
#
# code-review 21-Jul (2ª pasada) encontró un SEGUNDO disparador totalmente
# independiente y sin ninguna de estas protecciones: pipeline_watchdog.py
# (proceso persistente aparte, screen 'watchdog', check_screens() cada
# 120s) también reiniciaba 'fast' con un `screen -dmS` desnudo. Este
# script es el ÚNICO lugar que sabe reiniciar 'fast' con seguridad;
# watchdog_fast.sh Y pipeline_watchdog.py lo invocan en vez de
# reimplementar la lógica cada uno por su lado.
#
# code-review 21-Jul (3ª pasada) encontró DOS gaps más, verificados
# empíricamente, ambos corregidos aquí:
# 1. Sin lock propio: si watchdog_fast.sh (cron) y pipeline_watchdog.py
#    (cada 120s) invocaban este script casi a la vez, ambos podían pasar
#    el chequeo "screen ausente" antes de que ninguno creara la nueva --
#    y los dos crearla, reabriendo la misma carrera un nivel más arriba.
#    Fix: flock propio (RESTART_LOCK), no-bloqueante -- una 2ª invocación
#    simultánea se aparta sola en vez de competir.
# 2. `screen -X quit` mata el bash de run_fast.sh pero NO garantiza matar
#    a sus hijos: los `git commit/pull/push` van envueltos en `timeout`
#    (GNU coreutils), que por defecto pone al hijo en su PROPIO grupo de
#    proceso -- verificado en vivo que ese hijo sobrevive reparentado a
#    PID 1 aunque `screen -ls` ya no liste la sesión. `kill -9 -$pid`
#    (por grupo) nunca lo alcanza, porque ya no comparte grupo. Fix:
#    capturar el árbol COMPLETO de PIDs descendientes ANTES de tocar nada
#    (mientras el parentesco todavía es el real), y matar cada PID
#    exacto de esa lista si el 'quit' normal no basta -- un kill por PID
#    numérico funciona aunque el proceso haya sido reparentado después.
#
# Salida: 0 = 'fast' corriendo al terminar (ya lo estaba, o se reinició
# limpio). 1 = pospuesto (orden en curso, o ya hay otra invocación de
# este mismo script en marcha). 2 = no se pudo limpiar la screen vieja,
# 'fast' queda SIN reiniciar (fail-closed). 3 = tras reiniciar hay más de
# una screen 'fast' viva (carrera real detectada, no solo "no se pudo
# limpiar") -- distinto de 2 a propósito, este caso es más grave (dos
# loops de dinero real corriendo a la vez) y no debe leerse en el log
# como el mismo "restart falló" benigno del caso 2.
set -u
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="$REPO_DIR/logs/watchdog.log"
log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [restart_fast_seguro] $*" >> "$LOG"; }

# Lock propio no-bloqueante: si otra invocación (el otro disparador, o un
# cron-tick solapado) ya está en marcha, esta se aparta en vez de competir
# por matar/crear la misma screen a la vez.
RESTART_LOCK="$REPO_DIR/data/shadow/restart_fast_seguro.lock"
exec 200>"$RESTART_LOCK"
if ! flock -n 200; then
    log "AVISO: otra invocación de restart_fast_seguro.sh ya en marcha — se aparta esta."
    exit 1
fi

# No matar la screen si hay una orden real en vuelo hacia el CLOB ahora
# mismo (live_trade.py escribe/borra este marker justo antes/después de
# post_order).
MARKER="$REPO_DIR/data/live/orden_en_curso.json"
if [ -f "$MARKER" ]; then
    MARKER_TS=$(python3 -c "
import json
from datetime import datetime, timezone
try:
    d = json.load(open('$MARKER'))
    ts = datetime.fromisoformat(d['ts']).timestamp()
    print(int(datetime.now(timezone.utc).timestamp() - ts))
except Exception:
    print(99999)
" 2>/dev/null || echo 99999)
    if [ "$MARKER_TS" -lt 180 ]; then
        log "AVISO: orden en curso hace ${MARKER_TS}s — se pospone el reinicio de 'fast'."
        exit 1
    fi
    log "AVISO: marker orden_en_curso.json obsoleto (${MARKER_TS}s) — probablemente el proceso murió a mitad de una orden. Revisar trades.csv manualmente."
fi

# Árbol de descendientes: recursivo vía pgrep -P, capturado ANTES de
# enviar ninguna señal -- si se capturara DESPUÉS de "screen -X quit",
# los hijos ya reparentados a PID 1 se habrían perdido de la búsqueda
# (pgrep -P sigue el ppid real, que ya no sería el nuestro).
arbol_descendientes() {
    local pid=$1
    local hijo
    for hijo in $(pgrep -P "$pid" 2>/dev/null); do
        arbol_descendientes "$hijo"
        echo "$hijo"
    done
}

SCREEN_PID=$(screen -ls | grep '\.fast\s' | awk -F'.' '{print $1}' | tr -d '[:space:]')

if [ -z "$SCREEN_PID" ]; then
    log "'fast' ya está ausente, nada que matar."
else
    PIDS_A_MATAR="$(arbol_descendientes "$SCREEN_PID") $SCREEN_PID"
    log "Matando screen 'fast' vieja (pid=$SCREEN_PID, árbol capturado: $(echo $PIDS_A_MATAR | tr '\n' ' '))..."
    screen -S fast -X quit 2>/dev/null || true
    for _ in $(seq 1 15); do
        if ! screen -ls | grep -q '\.fast\s'; then
            break
        fi
        sleep 1
    done
    if screen -ls | grep -q '\.fast\s'; then
        log "AVISO: screen 'fast' seguía viva tras 15s de 'quit' — matando por PID exacto."
        for pid in $PIDS_A_MATAR; do
            kill -9 "$pid" 2>/dev/null || true
        done
    else
        # 'screen -ls' ya no la lista, pero eso no confirma que TODOS los
        # descendientes murieron (el caso git/timeout huérfano reparentado
        # a PID 1 verificado en code-review) -- comprobar cada PID
        # capturado y matar los que sigan vivos, sin esperar a que
        # 'screen -ls' lo detecte (nunca lo hará, ya no es descendiente
        # de la screen).
        for pid in $PIDS_A_MATAR; do
            if kill -0 "$pid" 2>/dev/null; then
                log "AVISO: pid=$pid (del árbol de 'fast') seguía vivo pese a que la screen ya no aparece en screen -ls — matando (huérfano probable, ej. git bajo timeout)."
                kill -9 "$pid" 2>/dev/null || true
            fi
        done
    fi
    # screen -wipe limpia las entradas 'Dead' que -X quit/kill -9 pueden
    # dejar listadas en screen -ls sin proceso real detrás.
    screen -wipe > /dev/null 2>&1 || true
fi

if screen -ls | grep -q '\.fast\s'; then
    log "ERROR: no se pudo limpiar la screen 'fast' vieja — NO se crea una nueva, fail-closed."
    exit 2
fi

screen -dmS fast bash "$REPO_DIR/run_fast.sh"
sleep 1
N_FAST_POST=$(screen -ls | grep -c '\.fast\s' || true)
if [ "$N_FAST_POST" -gt 1 ]; then
    log "ALERTA GRAVE: tras reiniciar hay ${N_FAST_POST} screens 'fast' vivas — carrera real detectada (2 loops de dinero real corriendo a la vez). Revisar YA manualmente (screen -ls, matar por PID, dejar solo una)."
    exit 3
fi
log "'fast' reiniciada limpio."
exit 0
