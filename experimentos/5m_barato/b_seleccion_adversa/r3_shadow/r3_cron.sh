#!/bin/bash
# Cron del brazo shadow R2/R3 (solo lectura; sin ordenes ni claves). Dos modos:
#   r3_cron.sh desenlaces   -> */20: anade el desenlace oficial (gamma) a los mercados cerrados  (un solo escritor de r3_desenlaces_D.jsonl.gz)
#   r3_cron.sh vigia        -> 10:50Z diario: gate del preregistro + emparejado con B real + Telegram solo si cambia el veredicto
# Fuera del racimo 06-09:15Z. Todo cron con Telegram lleva `|| aviso`. El aviso de fallo del resolvedor se limita a 1 cada 3 h (corre cada 20 min).
cd "$(dirname "$0")" || exit 1
DL=/root/polymarket-research-datalogs/r3_shadow; mkdir -p "$DL"; LOG=$DL/cron.log
ulimit -v 2500000
aviso() { /usr/bin/python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e(sys.argv[1])" "$1"; }
PY=/root/polymarket-research/.venv/bin/python
case "$1" in
  desenlaces)
    nice -n 19 ionice -c3 $PY -I r3_desenlaces.py >> "$LOG" 2>&1; rc=$?
    # 02-Nov: un 429 aislado de gamma es transitorio (los pendientes se reintentan cada 20 min y solo se abandonan a las 6 h): avisar
    # solo con 3 fallos CONSECUTIVOS (>=1 h), y como mucho 1 aviso cada 3 h.
    if [ $rc -eq 0 ]; then
      rm -f "$DL/.fallos_desenlaces"
    else
      n=$(( $(cat "$DL/.fallos_desenlaces" 2>/dev/null || echo 0) + 1 )); echo $n > "$DL/.fallos_desenlaces"
      last=$(stat -c %Y "$DL/.aviso_desenlaces" 2>/dev/null || echo 0)
      if [ $n -ge 3 ] && [ $(( $(date +%s) - last )) -gt 10800 ]; then touch "$DL/.aviso_desenlaces"; aviso "🚨 R3 shadow: el resolvedor de desenlaces FALLÓ $n veces seguidas rc=$rc (gamma). Ver $LOG"; fi
    fi ;;
  vigia)
    echo "=== $(date -u +%FT%TZ) vigia" >> "$LOG"
    ulimit -v 3000000   # 09-Nov: loader filtra dec (pico 0,9 GB, antes 5-6 GB y OOM-kill diario); 05-Nov: MemoryError a 4,5 GB con 10 dias (era 4,5 desde 02-Nov); 02-Nov: RSS medido 3,0 GB con 5 dias (MemoryError a 2,5 GB); el resolvedor sigue a 2,5 GB
    nice -n 19 ionice -c3 $PY -I r3_vigia.py --telegram >> "$LOG" 2>&1 || aviso "🚨 R3 shadow: el vigía diario FALLÓ. Ver $LOG" ;;
  *) echo "uso: $0 desenlaces|vigia"; exit 2 ;;
esac
