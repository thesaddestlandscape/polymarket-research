#!/bin/bash
# cron_juez_calma_v3.sh [DIA] -- juez forward Calma-T1 con sello v3 (paralelo al forward actual). Envolver con scripts/cron_pesado.sh; fuera de 06-09Z. Un fallo (rc!=0) => Telegram (nunca silencio). Solo lectura; 0 ordenes.
# Linea de cron propuesta (NO instalada por defecto; ver informe):
#   50 14 * * * /root/polymarket-research/scripts/cron_pesado.sh flock -n /tmp/calma_v3_juez.lock bash /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/recalc_13nov/cron_juez_calma_v3.sh || <aviso>
R=/root/polymarket-research; H=$R/experimentos/5m_barato/l2_carrera_10nov/calma_v3/recalc_13nov; LOG=${JUEZ_V3_LOG:-/root/polymarket-research-datalogs/juez_calma_v3.log}
h=$(date -u +%H); [ -z "${JUEZ_V3_FORZAR_HORA:-}" ] && [ "$h" -ge 6 ] && [ "$h" -lt 9 ] && { echo "$(date -u +%FT%TZ) 06-09Z: no se ejecuta" >> "$LOG"; exit 0; }
echo "$(date -u +%FT%TZ) inicio ${1:-ayer}" >> "$LOG"
python3 -I "$H/juez_calma_v3_dia.py" "$@" >> "$LOG" 2>&1; rc=$?
echo "$(date -u +%FT%TZ) fin rc=$rc" >> "$LOG"
if [ "$rc" -ne 0 ]; then
  cd $R && python3 -c "import sys; from shadow_digest import enviar_telegram; sys.exit(0 if enviar_telegram(sys.argv[1]) is True else 3)" "juez Calma v3 FALLO rc=$rc dia=${1:-ayer} (ver $LOG y calma_v3/recalc_13nov/out/manifest_juez_v3_*.json)" && exit 0   # aviso enviado: rc 0 para que el `|| aviso` del crontab no duplique; si Telegram falla, rc real
  echo "$(date -u +%FT%TZ) AVISO TELEGRAM FALLO" >> "$LOG"
fi
exit $rc
