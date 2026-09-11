#!/usr/bin/env bash
# run_fast_mantenimiento.sh — Bucle de mantenimiento (18-Ago, desacoplado de
# run_fast.sh): resolve + postmortem + resumen + git batch, en su propio
# loop/screen independiente del bucle predict/live_trade.
#
# Motivo: antes este bloque corría DENTRO de run_fast.sh cada 3er ciclo
# (~60s), y mientras corría (dominado por shadow_postmortem.py, ~49s) el
# bucle de predicción se PARABA por completo -- reducía la frecuencia de
# generación de señales nuevas de ~20s a ~80-90s. live_trade.py siempre
# corría ANTES de este bloque en el mismo ciclo, así que esto nunca afectó
# la calidad de fill de señales ya detectadas -- solo la frecuencia con la
# que aparecían señales nuevas. Ver project_desacoplar_fast_loop_
# postmortem_18ago (diseño completo, perfilado py-spy).
#
# Nada de este script envía órdenes ni toca el exchange -- resolve/
# postmortem/resumen/git son de solo lectura+aprendizaje+persistencia, así
# que NO necesita la protección anti-duplicado de restart_fast_seguro.sh
# (esa existe específicamente porque dos 'fast' vivas a la vez pueden
# duplicar ENVÍOS de órdenes) -- reinicio real vía restart_mantenimiento_
# seguro.sh, más simple (solo evita 2 screens duplicadas, no toca dinero).
# trades.csv ya está protegido con fcntl.flock en live_trade.py/
# shadow_resolve.py; strategy_params.json (el único fichero compartido de
# alta frecuencia con el otro loop) se escribe de forma atómica desde el
# 18-Ago (shadow_postmortem.py::_escribir_json_atomico); predictions_
# HOY.csv (leído aquí vía shadow_resolve.py, escrito por el otro loop) está
# protegido con try/except por fichero en cargar_predicciones_pendientes()
# -- los tres prerequisitos de concurrencia real quedaron resueltos antes
# de separar este loop.
#
# Comparte logs/fast.log con run_fast.sh a propósito (mismo log rotado por
# pipeline_watchdog.py, mismas herramientas de diagnóstico ya conocidas --
# CLAUDE.md ya dice "logs/fast.log — los tracebacks live van ahí").
#
# Arrancar con: screen -dmS mantenimiento bash run_fast_mantenimiento.sh
# (o, preferido, restart_mantenimiento_seguro.sh)

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$REPO_DIR/.venv/bin/python"
LOG="$REPO_DIR/logs/fast.log"
export REPO_DIR LOG

cd "$REPO_DIR"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [mantenimiento] $*" | tee -a "$LOG"; }

# ⚠️ `date +%s%3N` en este sistema NO trunca a milisegundos (imprime
# nanosegundos completos, 9 dígitos) -- verificado en vivo el 18-Ago.
# $EPOCHREALTIME (builtin bash 5.x, sin subproceso) da segundos.microsegundos
# de forma fiable; el prefijo 10# fuerza base-10 para no interpretar un 0
# inicial como octal.
#
# Duplicado (a propósito) en git_batch_sync.sh -- /code-review 18-Ago:
# ambos son procesos bash INDEPENDIENTES (git_batch_sync.sh se invoca aquí
# como `bash git_batch_sync.sh ...`, nunca `source`, ver docstring de ese
# fichero -- el aislamiento en subshell es deliberado), así que no pueden
# compartir esta función sin `export -f` o romper ese aislamiento. A
# diferencia del bloque de ~100 líneas de git-batch que SÍ se extrajo
# (riesgo real: un fix aplicado a una copia y no a la otra), esto son 8
# líneas de matemática de fechas sin lógica de negocio -- duplicación
# aceptada, no vale la complejidad de compartirla entre procesos.
now_ms() {
    local t=$EPOCHREALTIME
    local sec=${t%.*}
    local usec=${t#*.}
    usec=${usec:0:3}
    echo $(( 10#$sec * 1000 + 10#$usec ))
}

CADENCIA_S=60  # objetivo de cadencia total (trabajo + sleep), misma que la
               # cadencia efectiva de "cada 3er ciclo" del run_fast.sh original

log "=== Proceso MANTENIMIENTO arrancado (resolve/postmortem/resumen/git, objetivo ~${CADENCIA_S}s/ciclo) ==="

CICLO=0
LAST_GIT=0
GIT_BATCH_S=300
LAST_POSTMORTEM=0
POSTMORTEM_MIN_INTERVAL_S=600  # 04-Sep (subido de 300->600, ver aviso
# Telegram "pipeline lento" 06:01 UTC y project_incidente_swap_pipeline_
# lento_02sep): con results.csv ya en 385k filas/310MB, cada ejecución de
# shadow_postmortem.py tarda 180-285s (antes ~49-95s cuando se fijó 300s el
# 03-Sep) -- con un intervalo de 300s, casi TODA ejecución de postmortem ya
# empuja al ciclo por encima del umbral de alarma de 120s de
# vigia_pipiline_latencia, y swap subía activamente (4,2->5,3GB en 40s)
# mientras corría. 600s da el doble de margen para que RAM/swap se
# asienten entre picos, sin recortar ni un dato del cálculo (el histórico
# completo se sigue procesando igual cuando corre). Diagnóstico 04-Sep:
# NO hubo OOM-kill nuevo (los 2 de dmesg siguen siendo los del 02-Sep), la
# CPU (git pack-objects + swap-in) y no un bug de loop es la causa directa
# -- este es un alivio de cadencia, el rediseño real pendiente (ventana
# rolling/streaming, CLAUDE.md pt.18) sigue sin hacer, requiere diseño +
# /code-review por tocar el motor de aprendizaje causal compartido.
# 03-Sep (rediseño de memoria, paso 2 -- ver project_incidente_swap_
# pipeline_lento_02sep): shadow_postmortem.py sostiene ~2,7GB de RSS
# mientras procesa el histórico completo (~373k filas, necesario para no
# perder rigor estadístico -- nunca se recorta la ventana). Antes se
# re-encadenaba SIN NINGÚN hueco (siguiente ciclo arrancaba en cuanto
# terminaba el anterior), así que ese pico de memoria estaba presente casi
# de forma continua, chocando con cualquier otro proceso pesado del
# sistema (el mismo día, un `git repack` programado). Los patrones
# causales/IC no necesitan actualizarse más rápido que cada pocos minutos
# para que las decisiones de trading sigan bien informadas -- limitar el
# ARRANQUE de postmortem a como mucho una vez cada POSTMORTEM_MIN_INTERVAL_S
# da tiempo real a que el sistema libere RAM/swap entre ejecuciones, sin
# recortar ni un solo dato del cálculo en sí cuando SÍ corre.
# shadow_resolve.py (cierra trades reales) sigue corriendo TODOS los
# ciclos sin throttle -- esto solo afecta al aprendizaje causal, nunca a
# la resolución de dinero real.
while true; do
    CICLO=$((CICLO + 1))
    _t_ciclo0=$(now_ms)

    _t0=$(now_ms); $PYTHON "$REPO_DIR/shadow_resolve.py"     >> "$LOG" 2>&1 || true; log "  ⏱ shadow_resolve.py: $(($(now_ms) - _t0))ms"
    NOW_PM=$(date +%s)
    if [ $((NOW_PM - LAST_POSTMORTEM)) -ge $POSTMORTEM_MIN_INTERVAL_S ]; then
        LAST_POSTMORTEM=$NOW_PM
        _t0=$(now_ms); $PYTHON "$REPO_DIR/shadow_postmortem.py"  >> "$LOG" 2>&1 || true; log "  ⏱ shadow_postmortem.py: $(($(now_ms) - _t0))ms"
    else
        log "  ⏭ shadow_postmortem.py: saltado (último hace $((NOW_PM - LAST_POSTMORTEM))s < ${POSTMORTEM_MIN_INTERVAL_S}s)"
    fi
    _t0=$(now_ms); $PYTHON "$REPO_DIR/shadow_resumen.py"     >> "$LOG" 2>&1 || true; log "  ⏱ shadow_resumen.py: $(($(now_ms) - _t0))ms"

    NOW=$(date +%s)
    if [ $((NOW - LAST_GIT)) -ge $GIT_BATCH_S ]; then
        LAST_GIT=$NOW
        (
          bash "$REPO_DIR/git_batch_sync.sh" \
              "shadow: ciclo $CICLO $(date -u +%Y-%m-%dT%H:%MZ)" \
              "mantenimiento" \
              data/shadow/ data/live/ data/prices/ data/sports/ \
              -- data/shadow data/live data/prices data/sports
        )
    fi

    # Cadencia real ajustada al trabajo ya hecho (18-Ago, /code-review: un
    # `sleep 45` fijo ignoraba la duración real de resolve+postmortem+
    # resumen -- shadow_postmortem.py solo puede tardar ~49s bajo carga,
    # dando un ciclo real de ~95-150s en vez de los ~45-90s pretendidos).
    # Con esto: si el trabajo tardó más que CADENCIA_S, no se duerme nada
    # (se encadena el siguiente ciclo inmediatamente, igual que antes
    # cuando el ciclo lento se comía su propio presupuesto).
    _elapsed_ms=$(( $(now_ms) - _t_ciclo0 ))
    _sleep_ms=$(( CADENCIA_S * 1000 - _elapsed_ms ))
    if [ "$_sleep_ms" -gt 0 ]; then
        sleep "$(awk -v ms="$_sleep_ms" 'BEGIN { printf "%.1f", ms / 1000 }')"
    fi
done
