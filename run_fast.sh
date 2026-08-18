#!/usr/bin/env bash
# run_fast.sh — SOLO el bucle de predicción/ejecución (dinero real):
#   klines + predict + 4x micro-reintento live_trade, cadencia ~20-23s.
#
# 18-Ago: DESACOPLADO de resolve/postmortem/resumen/git-batch (movidos a
# run_fast_mantenimiento.sh, screen 'mantenimiento' independiente). Antes
# este mismo loop se paraba ~49-83s cada 3er ciclo mientras corría el
# mantenimiento (dominado por shadow_postmortem.py, ~49s) -- reducía la
# frecuencia real de generación de señales nuevas de ~20s a ~80-90s sin
# afectar la calidad de fill de señales YA detectadas (live_trade.py
# corría siempre ANTES del bloque lento en el mismo ciclo). Prerequisito
# resuelto antes de este cambio: escritura atómica de strategy_params.json
# (shadow_postmortem.py::_escribir_json_atomico, temp-file+os.replace) --
# sin eso, un lector de este loop podía capturar el fichero a medio
# escribir en cuanto el mantenimiento corriera de verdad en paralelo.
# trades.csv ya estaba protegido con fcntl.flock en live_trade.py/
# shadow_resolve.py (fix previo, carrera resolver_pendientes).
# predictions_HOY.csv (append-only, sin flock): shadow_resolve.py podría
# leerlo justo mientras este loop escribe -- protegido con try/except POR
# FICHERO en cargar_predicciones_pendientes() (shadow_resolve.py, 18-Ago):
# si pilla el fichero a medio escribir, salta ESE fichero y lo reintenta
# ~45s después (siguiente ciclo de run_fast_mantenimiento.sh), sin tumbar
# la resolución de otros ficheros ni la invocación completa.
# Ver project_desacoplar_fast_loop_postmortem_18ago (diseño completo).
#
# Micro-reintento live_trade (2026-07-10, hallazgo latencia): perfilado real
# mostró que klines+predict+live_trade tardan ~3s de trabajo real dentro de un
# ciclo de ~20-23s — el resto es sleep puro. El libro de estos mercados (~9
# bots de market-making activos 24/7, ver project_hallazgo_latencia_10jul)
# fluctúa de profundidad en segundos, así que reintentar la MISMA señal
# pendiente solo una vez cada ~20-23s (antes) desperdiciaba ese margen: una
# señal necesitaba 4-5 ciclos completos (80-115s) para tener 4-5 oportunidades
# de pasar el veto_profundidad, justo cuando SENAL_MAX_LATENCIA_SEG=100 la
# caduca. Ahora: klines+predict UNA vez, pero live_trade se reintenta 4x
# espaciado ~4-5s DENTRO del mismo ciclo — mismas ~15-20 oportunidades ahora
# caben en los 100s de vida de la señal, en vez de 4-5.
# Código de seguridad live — no minimizar. NO toca live_trade.py: la propia
# invalidación por latencia (SENAL_MAX_LATENCIA_SEG) ya acota los reintentos.
# Arrancar con: screen -S fast bash run_fast.sh (vía restart_fast_seguro.sh,
# el ÚNICO punto de verdad para reiniciar esta screen -- ver ese script).

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$REPO_DIR/.venv/bin/python"
LOG="$REPO_DIR/logs/fast.log"

# 11-Ago: bug real encontrado en vivo -- este script se lanza vía `screen
# -dmS fast bash "$REPO_DIR/run_fast.sh"` (restart_fast_seguro.sh) sin
# ningún `cd` explícito antes, así que el proceso hereda el cwd de quien
# lo invocó (pipeline_watchdog.py / watchdog_fast.sh vía cron, que por
# defecto usa $HOME=/root, NO el repo). Todas las llamadas a Python de
# aquí usan rutas absolutas ($REPO_DIR/...) así que funcionan igual, pero
# ALGUNOS scripts (live_guard.py::CONFIG_PATH/SWITCH_PATH) usan rutas
# RELATIVAS internamente -- con cwd=/root resuelven a la nada, y
# `estado_live()` reporta falsamente "switch OFF / config_live.json no
# encontrado" por Telegram sobre dinero real, aunque el bot esté sano.
cd "$REPO_DIR"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG"; }

log "=== Proceso FAST arrancado (predict/live_trade puro, ~20s, sin bloqueo de mantenimiento) ==="

while true; do
    $PYTHON "$REPO_DIR/fetch_binance_klines.py"   >> "$LOG" 2>&1 || true
    $PYTHON "$REPO_DIR/shadow_predict.py"         >> "$LOG" 2>&1 || true
    for _ in 1 2 3 4; do
        $PYTHON "$REPO_DIR/live_trade.py"         >> "$LOG" 2>&1 || true
        sleep 4
    done

    # sleep final 1s: el micro-loop de arriba (4×4s=16s) ya ocupa el margen
    # que antes absorbía un sleep mayor -- cadencia total del ciclo ~20-23s.
    sleep 1
done
