#!/usr/bin/env bash
# restart_mantenimiento_seguro.sh — Único punto de verdad para reiniciar la
# screen 'mantenimiento' (resolve/postmortem/resumen/git-batch).
#
# 18-Ago: mismo problema de fondo que motivó restart_fast_seguro.sh
# (21-Jul) -- DOS disparadores independientes pueden querer reiniciar la
# misma screen casi a la vez (watchdog_fast.sh vía cron */5min, y
# pipeline_watchdog.py vía su loop persistente cada 120s). Sin coordinación,
# ambos podrían crear una screen 'mantenimiento' duplicada. A diferencia de
# 'fast' (dinero real, duplicar = riesgo de doble ENVÍO de orden), duplicar
# 'mantenimiento' no envía nada al exchange -- el peor caso es un commit/push
# redundante (ya serializado por git_ops.lock) o una escritura redundante de
# strategy_params.json (ya atómica desde el 18-Ago). Por eso este script es
# deliberadamente más simple que restart_fast_seguro.sh: solo un flock
# no-bloqueante, sin chequeo de "orden en curso" ni kill por árbol de PIDs.
#
# Salida: 0 = 'mantenimiento' corriendo al terminar. 1 = pospuesto (otra
# invocación de este script ya en marcha -- se aparta en vez de competir).
set -u
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="$REPO_DIR/logs/watchdog.log"
log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [restart_mantenimiento_seguro] $*" >> "$LOG"; }

RESTART_LOCK="$REPO_DIR/data/shadow/restart_mantenimiento_seguro.lock"
exec 201>"$RESTART_LOCK"
if ! flock -n 201; then
    log "AVISO: otra invocación ya en marcha -- se aparta esta."
    exit 1
fi

if screen -ls | grep -q '\.mantenimiento\s'; then
    log "Screen 'mantenimiento' presente -- reiniciando (quit + relanzar)."
    screen -S mantenimiento -X quit >> "$LOG" 2>&1
    sleep 2
else
    log "Screen 'mantenimiento' ausente -- lanzando."
fi

cd "$REPO_DIR"
# /code-review (18-Ago, hallazgo real, reproducido en local): SIN el
# ">> logs/fast.log 2>&1" de aquí -- run_fast_mantenimiento.sh ya redirige
# cada línea explícitamente a $LOG (su propio log() hace `tee -a "$LOG"`,
# y cada $PYTHON ... hace `>> "$LOG" 2>&1` por su cuenta, mismo patrón
# exacto que run_fast.sh). Un redirect EXTERNO aquí duplicaba cada línea:
# tee la escribe directamente en el fichero Y la deja pasar por su propio
# stdout, que con el redirect externo volvía a caer en el MISMO fichero.
# restart_fast_seguro.sh (línea con `screen -dmS fast bash run_fast.sh`,
# sin redirect externo) es el patrón correcto -- replicado aquí.
screen -dmS mantenimiento bash "$REPO_DIR/run_fast_mantenimiento.sh"
sleep 1
if screen -ls | grep -q '\.mantenimiento\s'; then
    log "Screen 'mantenimiento' reiniciada OK."
    exit 0
else
    log "🚨 Screen 'mantenimiento' no aparece tras relanzarla -- revisar manualmente."
    exit 2
fi
