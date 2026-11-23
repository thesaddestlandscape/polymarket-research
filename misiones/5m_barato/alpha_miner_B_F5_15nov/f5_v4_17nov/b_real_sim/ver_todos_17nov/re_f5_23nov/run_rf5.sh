#!/bin/bash
# run_rf5.sh -- runner diario RF5E-COMB-23NOV-v1 (prereg 16be06b6). Cron D+2 12:30Z. Un job pesado a la vez (flock + scripts/cron_pesado.sh), nice 19, ionice -c3, ulimit -v 5 GB, MemAvailable>=5500 MB, nunca 06:00-09:15Z ni 22:15-22:30Z.
# 1) cintas tape/bad (prep_tapes_rf5.sh, sha en TAPES_SHA256_ciegos.txt) de 17-Nov a ayer; 2) rf5_run.py dia D para cada dia >=18-Nov hasta ayer (idempotente: COMPLETE/INCOMPLETE se saltan; PENDING/BLOCKED/FAILED se reintentan = recupera pendientes).
# Latido: out_rf5_ciego/heartbeat.json (inicio y fin; lo lee vigia_rf5.py). Salida !=0 si algun dia FAILED. Parada: por PID guardado (out_rf5_ciego/run.pid). Lanzar siempre por su ruta.
HV="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)/"; OUT=${RF5_OUT:-${HV}out_rf5_ciego/}; mkdir -p "$OUT"
exec 8>"${OUT}.run.lock"; flock -n 8 || { echo "otro run_rf5 en curso"; exit 0; }; echo $$ > "${OUT}run.pid"
ts() { date -u +%FT%TZ; }; LOG="${OUT}run_$(date -u +%Y%m%dT%H%M%SZ).log"
hb() { printf '{"estado":"%s","t":"%s","epoch":%s}\n' "$1" "$(ts)" "$(date +%s)" > "${OUT}heartbeat.json.tmp" && mv "${OUT}heartbeat.json.tmp" "${OUT}heartbeat.json"; }
{
hb INICIO; echo "$(ts) run_rf5 inicio"
HOY=$(date -u +%F); DIAS=(); d=2026-11-17; while [ "$d" \< "$HOY" ]; do DIAS+=("$d"); d=$(date -u -d "$d + 1 day" +%F); done
[ ${#DIAS[@]} -gt 0 ] && "${HV}prep_tapes_rf5.sh" "${DIAS[@]}"
rc=0
for d in "${DIAS[@]}"; do
  [ "$d" \< "2026-11-18" ] && continue            # calendario ciego >= 18-Nov
  for i in $(seq 1 ${RF5_ESPERA:-240}); do h=$((10#$(date -u +%H%M))); ram=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
    { [ "$h" -lt 600 ] || [ "$h" -ge 915 ]; } && { [ "$h" -lt 2215 ] || [ "$h" -ge 2230 ]; } && [ "${ram:-0}" -ge "${RF5_RAM_MIN:-5500}" ] && break; sleep 30; done
  echo "$(ts) >>> rf5_run dia $d (ram=${ram}MB hhmm=$h)"
  ( ulimit -v 5000000; /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 /usr/bin/time -v -o "${OUT}pico_dia_$d.txt" python3 -I "${HV}rf5_run.py" dia "$d" ) 2>&1 | while IFS= read -r l; do echo "$(ts) $l"; done
  r=${PIPESTATUS[0]}; [ "$r" -ne 0 ] && { rc=1; echo "$(ts) dia $d rc=$r"; }
done
hb FIN; echo "$(ts) run_rf5 fin rc=$rc"; exit $rc
} >> "$LOG" 2>&1
