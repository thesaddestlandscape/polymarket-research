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
# 17-Nov (45 OOM-kills/24 h, swap 8 GB lleno): cada job pesado corre en su propio cgroup dentro de pesados.slice con
# MemoryMax dinamico = MemAvailable al arrancar - 1200 MB de reserva (rango 2500..5500 MB). Si se pasa, el OOM del CGROUP mata
# solo a ese job (reintentable) en vez de agotar la RAM global, tirar de swap (ciclo postmortem 629 s) o matar sesiones/systemd.
# MemorySwapMax=0: el swap ya esta lleno con procesos de larga vida. Fallback sin cgroup si systemd-run falla.
a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); cap=$(( ${a:-0} - 1200 )); [ $cap -lt 2500 ] && cap=2500; [ $cap -gt 5500 ] && cap=5500
echo "$(date -u +%FT%TZ) INICIO cap=${cap}MB disp=${a}MB: $*" >> "$LOG"
if command -v systemd-run >/dev/null && systemd-run --scope --quiet --slice=pesados.slice -p MemoryMax=1G true 2>/dev/null; then
  exec choom -n 500 -- systemd-run --scope --quiet --slice=pesados.slice -p MemoryMax=${cap}M -p MemoryHigh=$((cap*9/10))M -p MemorySwapMax=0 -- "$@"
fi
exec choom -n 500 -- "$@"
