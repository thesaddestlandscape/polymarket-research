#!/usr/bin/env bash
# watchdog_fast.sh — Reinicia el loop fast si lleva más de 10min sin commits.
# Cron: */5 * * * * /root/polymarket-research/watchdog_fast.sh

REPO_DIR="/root/polymarket-research"
LOG="$REPO_DIR/logs/watchdog.log"
MAX_SILENCE_S=900   # 15 min sin commit → loop muerto (900 desde 08-Jul: el fast
                    # commitea en batch c/5min — con 600 un hipo puntual de git
                    # disparaba restart espurio; 900 mantiene margen 3×)

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" >> "$LOG"; }

LAST_COMMIT_TS=$(git -C "$REPO_DIR" log -1 --format="%ct" -- data/shadow/ 2>/dev/null || echo 0)
AGE_S=$(( $(date +%s) - LAST_COMMIT_TS ))

if [ "$AGE_S" -lt "$MAX_SILENCE_S" ]; then
    exit 0  # Commit reciente — el loop vive
fi

# No matar la screen si hay una orden real en vuelo hacia el CLOB ahora mismo
# (live_trade.py / nested_arb_trade.py escriben/borran estos markers justo
# antes/después de post_order). Sin esto, matar "fast" a mitad de una orden
# ya enviada al exchange deja la posición sin registrar y permite re-operar
# el mismo mercado. 14-Jul: se añadió el marker de nested_arb (2 patas) —
# antes solo se vigilaba el de 1 pata (live_trade.py) y el watchdog podía
# matar "fast" con una pata de nested_arb en vuelo sin ninguna protección.
MARKERS=(
    "$REPO_DIR/data/live/orden_en_curso.json"
    "$REPO_DIR/data/live/nested_arb_orden_en_curso.json"
)
for MARKER in "${MARKERS[@]}"; do
    if [ -f "$MARKER" ]; then
        MARKER_TS=$(python3 -c "
import json, sys
from datetime import datetime, timezone
try:
    d = json.load(open('$MARKER'))
    ts = datetime.fromisoformat(d['ts']).timestamp()
    print(int(datetime.now(timezone.utc).timestamp() - ts))
except Exception:
    print(99999)
" 2>/dev/null || echo 99999)
        if [ "$MARKER_TS" -lt 180 ]; then
            log "AVISO: orden en curso ($MARKER) hace ${MARKER_TS}s — se pospone el reinicio de 'fast' este ciclo."
            exit 0
        fi
        log "AVISO: marker $MARKER obsoleto (${MARKER_TS}s) — probablemente el proceso murió a mitad de una orden. Revisar manualmente."
    fi
done

log "ALERTA: último commit data/shadow/ hace ${AGE_S}s (>${MAX_SILENCE_S}s). Reiniciando loop fast..."
screen -S fast -X quit 2>/dev/null || true
sleep 2
screen -dmS fast bash "$REPO_DIR/run_fast.sh"
log "Loop fast reiniciado."
