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
while true; do
    CICLO=$((CICLO + 1))
    _t_ciclo0=$(now_ms)

    _t0=$(now_ms); $PYTHON "$REPO_DIR/shadow_resolve.py"     >> "$LOG" 2>&1 || true; log "  ⏱ shadow_resolve.py: $(($(now_ms) - _t0))ms"
    _t0=$(now_ms); $PYTHON "$REPO_DIR/shadow_postmortem.py"  >> "$LOG" 2>&1 || true; log "  ⏱ shadow_postmortem.py: $(($(now_ms) - _t0))ms"
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
