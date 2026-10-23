#!/bin/bash
# L1 etiquetado pasivo rpre/r900 de B (23-Oct). Uso: l1_cron.sh etiquetar|resolver. Solo lectura de B; salida en datalogs/etiquetado_pasivo_B (fuera de git).
cd "$(dirname "$0")" || exit 1
LOG=/root/polymarket-research-datalogs/etiquetado_pasivo_B/cron.log; mkdir -p "$(dirname "$LOG")"
ulimit -v 3000000
echo "=== $(date -u +%FT%TZ) $1" >> "$LOG"
nice -n 19 ionice -c3 python3 -I etiquetar_pasivo.py "$1" >> "$LOG" 2>&1; rc=$?
if [ $rc -ne 0 ]; then /usr/bin/python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e('🚨 L1 etiquetado pasivo B ($1) FALLÓ rc=$rc. Ver $LOG')"; fi
# retencion del log (>5 MB: se conserva la cola)
[ "$(stat -c %s "$LOG")" -gt 5000000 ] && tail -c 1000000 "$LOG" > "$LOG.tmp" && mv "$LOG.tmp" "$LOG"
exit $rc
