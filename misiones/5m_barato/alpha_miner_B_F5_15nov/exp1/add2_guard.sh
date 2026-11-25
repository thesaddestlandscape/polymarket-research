#!/bin/bash
# add2_guard.sh (16-Nov, ADDENDUM2 §7) -- guarda de ventana y calma de run_add2.sh. Ventana 09:20-22:00Z (nunca 06:00-09:15Z, ni 22:15-22:30Z, ni 01:45-06:00Z); calma = load1 <= 8 y MemAvailable >= 3500 MB.
#   add2_guard.sh --check   -> rc 0 si se puede arrancar ahora
#   add2_guard.sh --estado  -> imprime hora, load1 y MemAvailable
#   add2_guard.sh CMD...    -> vuelve a comprobar (rc 75 si no) y hace exec de timeout 45 min + nice 19 + ionice -c3 del comando (lo llama scripts/cron_pesado.sh, que pone oom_score_adj +500)
h=$(date -u +%H%M); l=$(awk '{print $1}' /proc/loadavg); a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
ok() { [ "$h" -ge 0920 ] && [ "$h" -lt 2200 ] && awk -v l="$l" 'BEGIN{exit !(l<=8.0)}' && [ "${a:-0}" -ge 3500 ]; }
case "$1" in
  --check) ok; exit $?;;
  --estado) echo "hora ${h}Z load1 $l MemAvailable_MB $a"; exit 0;;
esac
ok || { echo "$(date -u +%FT%TZ) add2_guard: sin ventana o sin calma (hora ${h}Z load1 $l MemAvailable_MB $a): no se arranca" >&2; exit 75; }
exec timeout -k 60 2700 nice -n 19 ionice -c3 "$@"
