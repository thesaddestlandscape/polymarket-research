#!/bin/bash
# MAPA-ESCALA infra (OLA 6 / TP1-INFRA, 23-Oct): extraccion on-chain 5m/15m (guardian) + 60m/4h/24h, TP1 forward pasivo y resolvedor de desenlaces.
# Solo lectura de datos publicos; escribe en datalogs/mapa_infra, datalogs/mapa_tp1 y volumen/m60|m240|m24h_onchain. No toca B ni ejecutores.
# Cron 12:15Z (fuera de 06:00-09:15Z y 22:15-22:30Z); espera a load5<=7 (hasta 45 min); un proceso a la vez (flock); Telegram si falla.
cd "$(dirname "$0")" || exit 1
LOGD=/root/polymarket-research-datalogs/mapa_infra/logs; mkdir -p "$LOGD"; LOG="$LOGD/diario_$(date -u +%F).log"
ulimit -v 3000000
echo "=== $(date -u +%FT%TZ)" >> "$LOG"
nice -n 19 ionice -c3 /root/polymarket-research/.venv/bin/python diario.py >> "$LOG" 2>&1; rc=$?
if [ $rc -ne 0 ]; then /usr/bin/python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e('🚨 MAPA-ESCALA infra: diario.py FALLÓ rc=$rc. Ver $LOG. El on-chain rota a ~5 d.')"; fi
find "$LOGD" -name 'diario_*.log' -mtime +45 -delete
exit $rc
