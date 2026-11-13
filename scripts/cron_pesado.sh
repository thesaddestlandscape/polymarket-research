#!/bin/bash
# Semaforo global de crons pesados (02-Nov, anti-OOM): UNO a la vez + espera a MemAvailable >= 3 GB (max 10 min; luego corre y lo anota).
# Uso en crontab: scripts/cron_pesado.sh <comando...>   (el comando conserva su propio flock -n / ulimit / nice)
LOG=/root/polymarket-research/logs/cron_pesado.log
exec 9>/tmp/cron_pesado.lock
if ! flock -w 3300 9; then echo "$(date -u +%FT%TZ) OMITIDO (cola >55 min): $*" >> "$LOG"; exit 0; fi
for i in $(seq 1 30); do
  a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
  # 10-Nov: shadow_postmortem.py pica a ~3,2 GB (OOM-kills): no arrancar un cron pesado mientras corre (fail-open tras el max de 10 min)
  [ "${a:-0}" -ge 3000 ] && ! pgrep -f "python.* /root/polymarket-research/shadow_postmortem.py" >/dev/null && break; sleep 20
done
[ "${a:-0}" -lt 3000 ] && echo "$(date -u +%FT%TZ) RAM baja (${a} MB) tras 10 min; se ejecuta igualmente: $*" >> "$LOG"
# 13-Nov (OOM): los crons pesados son reintentables -> victima PREFERIDA del OOM-killer (adj +500, lo heredan sus hijos), para que no caigan observadores/vigiasfreq.
exec choom -n 500 -- "$@"
