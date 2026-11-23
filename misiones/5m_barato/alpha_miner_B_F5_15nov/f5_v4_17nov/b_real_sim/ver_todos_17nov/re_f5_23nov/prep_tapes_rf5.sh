#!/bin/bash
# prep_tapes_rf5.sh DIA...  -- produce tape/bad con prep_day.py (DEV, sin modificar) un dia cada vez; anota sha en TAPES_SHA256_ciegos.txt (append-only).
# cron_pesado + nice 19 + ionice -c3 + ulimit -v 5 GB; espera MemAvailable>=5500 MB y fuera de 06:00-09:15Z y 22:15-22:30Z. Idempotente (prep_day sale si ya existe; el sha se anota una sola vez por fichero).
HV="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)/"
PD=/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido; OUT=$PD/out/; REF=${HV}TAPES_SHA256_ciegos.txt; LOGD=${HV}out_rf5_ciego/; mkdir -p "$LOGD"; touch "$REF"
ts() { date -u +%FT%TZ; }
exec 7>"${LOGD}.prep.lock"; flock -n 7 || { echo "$(ts) otro prep_tapes en curso"; exit 2; }
ok_ahora() { h=$((10#$(date -u +%H%M))); ram=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
  { [ "$h" -lt 600 ] || [ "$h" -ge 915 ]; } && { [ "$h" -lt 2215 ] || [ "$h" -ge 2230 ]; } && [ "${ram:-0}" -ge "${RF5_RAM_MIN:-5500}" ]; }
for d in "$@"; do
  if { [ ! -f "${OUT}tape_$d.pkl" ] || [ ! -f "${OUT}bad_$d.json" ]; } && [ ! -f "/root/polymarket-research-datalogs/sa_ms/ms_$d.npz" ]; then echo "$(ts) PENDING $d: sin sa_ms/ms_$d.npz (lo produce el cron 10:40Z del dia siguiente)"; continue; fi
  for i in $(seq 1 ${RF5_ESPERA:-480}); do ok_ahora && break; sleep 30; done
  ok_ahora || { echo "$(ts) BLOCKED $d: ventana/RAM no cumplida (ram=${ram}MB hhmm=$h)"; continue; }
  if [ ! -f "${OUT}tape_$d.pkl" ] || [ ! -f "${OUT}bad_$d.json" ]; then
    echo "$(ts) >>> prep_day $d"
    ( cd "$PD" && ulimit -v 5000000 && /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 /usr/bin/time -v -o "${LOGD}pico_prep_$d.txt" python3 -I "$PD/prep_day.py" "$d" ) 2>&1 | while IFS= read -r l; do echo "$(ts) $l"; done
  fi
  for f in "${OUT}tape_$d.pkl" "${OUT}bad_$d.json"; do
    if [ -f "$f" ]; then grep -q " $f\$" "$REF" || { echo "$(sha256sum "$f")" >> "$REF"; echo "$(ts) sha anotado $f"; }; else echo "$(ts) FALTA $f"; fi
  done
done
