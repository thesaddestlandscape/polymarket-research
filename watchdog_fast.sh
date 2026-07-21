#!/usr/bin/env bash
# watchdog_fast.sh — Reinicia el loop fast si lleva más de 10min sin commits.
# Cron: */5 * * * * /root/polymarket-research/watchdog_fast.sh

REPO_DIR="/root/polymarket-research"
LOG="$REPO_DIR/logs/watchdog.log"
MAX_SILENCE_S=900   # 15 min sin commit → loop muerto (900 desde 08-Jul: el fast
                    # commitea en batch c/5min — con 600 un hipo puntual de git
                    # disparaba restart espurio; 900 mantiene margen 3×)

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" >> "$LOG"; }

# Nadie más vigila la screen 'watchdog' (pipeline_watchdog.py) — si muere no
# puede reiniciarse a sí misma, y sin ella se pierden rotación de logs, disco,
# sintaxis y freno por ventana en silencio. Barrido de coherencia 17-Jul.
if ! screen -ls | grep -q '\.watchdog\s'; then
    log "ALERTA: screen 'watchdog' caída. Reiniciando..."
    screen -dmS watchdog bash -c "cd $REPO_DIR && python3 pipeline_watchdog.py"
    log "Screen 'watchdog' reiniciada."
fi

LAST_COMMIT_TS=$(git -C "$REPO_DIR" log -1 --format="%ct" -- data/shadow/ 2>/dev/null || echo 0)
AGE_S=$(( $(date +%s) - LAST_COMMIT_TS ))

if [ "$AGE_S" -lt "$MAX_SILENCE_S" ]; then
    exit 0  # Commit reciente — el loop vive
fi

log "ALERTA: último commit data/shadow/ hace ${AGE_S}s (>${MAX_SILENCE_S}s). Reiniciando loop fast..."

# 21-Jul: la lógica de reinicio seguro (chequeo orden_en_curso + espera/
# verificación antes de matar + kill por PID+grupo como red de seguridad)
# vive ahora en restart_fast_seguro.sh -- único punto de verdad, también
# invocado por pipeline_watchdog.py (que antes reiniciaba 'fast' con un
# screen -dmS desnudo, sin ninguna de estas protecciones, reabriendo la
# misma carrera por una vía distinta -- ver el propio script para el
# historial completo). No duplicar esta lógica aquí.
"$REPO_DIR/restart_fast_seguro.sh"
case $? in
    0) log "Loop fast reiniciado." ;;
    1) log "Reinicio pospuesto (orden en curso, o ya había otra invocación en marcha)." ;;
    3) log "🚨 CARRERA REAL: hay 2+ screens 'fast' vivas tras el reinicio — revisar manualmente YA." ;;
    *) log "Reinicio de 'fast' falló (no se pudo limpiar la screen vieja) — ver logs/watchdog.log arriba." ;;
esac
