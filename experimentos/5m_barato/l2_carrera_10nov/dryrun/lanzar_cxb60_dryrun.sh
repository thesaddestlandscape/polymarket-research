#!/bin/bash
# PLAN C6 (NO EJECUTADO, NO DESPLEGADO): lanza/relanza el dry-run B-CXB60 (solo simula, 0 ordenes). Mata SOLO el PID guardado y tras comprobar su cmdline (nunca pgrep/pkill -f).
# Uso: lanzar_cxb60_dryrun.sh [--forzar] [--probar]  (--probar: hace TODAS las comprobaciones y escribe el comando que ejecutaria, sin matar ni lanzar nada)  -- exige: fuera de 06-09Z, MemAvailable >= 2 GB, load5 < 6, HASHES_CONGELADOS.json valido.
set -u
D=${CXB60_DIR:-/root/polymarket-research-datalogs/cxb60_dryrun}; PY=/root/polymarket-research/.venv/bin/python; SC=/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/dryrun
mkdir -p "$D"
h=$(date -u +%H); a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); l=$(awk '{print $2}' /proc/loadavg)
FORZ=0; PROB=0; for a in "$@"; do [ "$a" = "--forzar" ] && FORZ=1; [ "$a" = "--probar" ] && PROB=1; done
if [ "$FORZ" = 0 ]; then
  [ "$h" -ge 6 ] && [ "$h" -lt 9 ] && { echo "06-09Z: no se arranca"; exit 2; }
  [ "${a:-0}" -lt 2000 ] && { echo "MemAvailable ${a} MB < 2000: no se arranca"; exit 2; }
  awk -v l="$l" 'BEGIN{exit !(l>=6)}' && { echo "load5 $l >= 6: no se arranca"; exit 2; }
fi
$PY "$SC/congelar_hashes_cxb60.py" --verificar >/dev/null || { echo "hashes distintos de los congelados: no se arranca"; exit 3; }
f="$D/cxb60.pid"
if [ "$PROB" = 1 ]; then echo "PROBAR: comprobaciones OK; lanzaria: cd $SC && (ulimit -v 7000000; nohup nice -n 15 ionice -c3 $PY -I cxb60_dryrun_fase0.py >> logs/cxb60_dryrun.log 2>&1 &) ; pid en $f"; exit 0; fi
if [ -f "$f" ]; then p=$(cat "$f"); if [ -n "$p" ] && [ -r "/proc/$p/cmdline" ] && tr '\0' ' ' < "/proc/$p/cmdline" | grep -q "cxb60_dryrun_fase0.py"; then kill "$p"; sleep 5; fi; rm -f "$f"; fi
cd "$SC" || exit 1
# ulimit -v 7 GB (el limite es VIRTUAL: numpy/pandas mapeados; el tope real es el RSS, vigilado por --max-rss-mb 3000)
( ulimit -v 7000000; nohup nice -n 15 ionice -c3 $PY -I cxb60_dryrun_fase0.py >> /root/polymarket-research/logs/cxb60_dryrun.log 2>&1 & echo $! > "$f" )
sleep 2; cat "$f"
