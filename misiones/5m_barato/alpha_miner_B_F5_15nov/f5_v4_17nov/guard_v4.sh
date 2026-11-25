#!/bin/bash
# guard_v4.sh -- guarda de ventana y calma de run_v4.sh (misma politica que exp1/add2_guard.sh). Nunca 06:00-09:15Z; calma = load1 <= 8 y MemAvailable >= 3500 MB.
#   guard_v4.sh --check | --estado | CMD...  (CMD: re-chequea, ulimit -v 3 GB, timeout 45 min, nice 19, ionice -c3)
h=$(date -u +%H%M); l=$(awk '{print $1}' /proc/loadavg); a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
ok() { { [ "$h" -ge 0915 ] && [ "$h" -lt 2330 ]; } && awk -v l="$l" -v n="$(nproc --all)" 'BEGIN{exit !(l<=1.5*n)}' && [ "${a:-0}" -ge 3500 ]; }
case "$1" in --check) ok; exit $?;; --estado) echo "hora ${h}Z load1 $l MemAvailable_MB $a"; exit 0;; esac
ok || { echo "$(date -u +%FT%TZ) guard_v4: sin ventana o sin calma (hora ${h}Z load1 $l MemAvailable_MB $a)" >&2; exit 75; }
ulimit -v 3000000
exec timeout -k 60 2700 nice -n 19 ionice -c3 "$@"
