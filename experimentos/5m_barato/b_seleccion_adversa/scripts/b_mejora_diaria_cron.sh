#!/bin/bash
# Postmortem diario de B real (solo lectura): re-ejecuta b_postmortem.py sobre el ledger y envía el resumen por Telegram. Cron 10:55Z (tras r1_fwd 10:40Z). No toca B.
cd "$(dirname "$0")" || exit 1
LOG=/root/polymarket-research-datalogs/sa_r1/mejora_diaria.log; mkdir -p "$(dirname "$LOG")"
ulimit -v 3000000
aviso() { /usr/bin/python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e(sys.argv[1])" "$1"; }
echo "=== $(date -u +%FT%TZ)" >> "$LOG"
OUT=$(nice -n 19 ionice -c3 python3 -I b_postmortem.py 2>>"$LOG") || { aviso "🚨 B mejora diaria: b_postmortem FALLÓ. Ver $LOG"; exit 1; }
echo "$OUT" >> "$LOG"
aviso "📊 B postmortem diario (solo lectura)
$(echo "$OUT" | head -14 | cut -c1-200)
Detalle: experimentos/5m_barato/b_seleccion_adversa/datos/b_postmortem_*.json · reglas R2/R3: INFORME.md"
