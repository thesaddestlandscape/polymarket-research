#!/bin/bash
# run_k6.sh -- juez CALMA v4 diario (ESPEC_HOOK_CALMA_V4_23nov; K6 = K1 + Calma-T1). Cron 11:50Z (antes del runner RF5 de las 12:30Z, que produce los dias COMPLETE que este job consume con 1 dia de retraso). Un job pesado a la vez (flock + scripts/cron_pesado.sh), nice 19, ionice -c3, ulimit -v 5 GB,
# MemAvailable>=5500 MB, nunca 06:00-09:15Z ni 22:15-22:30Z. Procesa SOLO dias >=18-Nov con manifest rf5dia COMPLETE y sin rf5K6 COMPLETE (idempotente; FAILED/BLOCKED se reintentan). Latido: out_rf5_ciego/heartbeat_k6.json (lo lee vigia_rf5.py: R6). Parada por PID guardado (out_rf5_ciego/run_k6.pid).
HV="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)/"; OUT=${RF5_OUT:-${HV}out_rf5_ciego/}; mkdir -p "$OUT"
exec 8>"${OUT}.run_k6.lock"; flock -n 8 || { echo "otro run_k6 en curso"; exit 0; }; echo $$ > "${OUT}run_k6.pid"
ts() { date -u +%FT%TZ; }; LOG="${OUT}run_k6_$(date -u +%Y%m%dT%H%M%SZ).log"
hb() { printf '{"estado":"%s","t":"%s","epoch":%s}\n' "$1" "$(ts)" "$(date +%s)" > "${OUT}heartbeat_k6.json.tmp" && mv "${OUT}heartbeat_k6.json.tmp" "${OUT}heartbeat_k6.json"; }
{
hb INICIO; echo "$(ts) run_k6 inicio"; rc=0
for f in "${OUT}"manifest_rf5dia_*.json; do [ -f "$f" ] || continue; d=${f##*manifest_rf5dia_}; d=${d%.json}; [ "$d" \< "2026-11-18" ] && continue
  python3 -I -c "import json,sys; sys.exit(0 if json.load(open(sys.argv[1])).get('status')=='COMPLETE' else 1)" "$f" || continue          # solo dias RF5 COMPLETE
  puerta=0; for i in $(seq 1 ${RF5_ESPERA:-240}); do h=$((10#$(date -u +%H%M))); ram=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
    { [ "$h" -lt 600 ] || [ "$h" -ge 915 ]; } && { [ "$h" -lt 2215 ] || [ "$h" -ge 2230 ]; } && [ "${ram:-0}" -ge "${RF5_RAM_MIN:-5500}" ] && { puerta=1; break; }; sleep 30; done
  # v3: si se agota la espera (RAM < minimo o ventana prohibida) el dia se ABORTA (NO se ejecuta igualmente): queda sin procesar (el runner es idempotente: lo reintenta el cron del dia siguiente) y rc=1 => el `|| vigia --aviso-*` del cron avisa
  if [ "$puerta" -ne 1 ]; then rc=1; echo "$(ts) ABORTADO dia $d: espera agotada (ram=${ram}MB hhmm=$h, minimo ${RF5_RAM_MIN:-5500} MB) -> sin ejecutar; reintento en el siguiente cron"; printf '{"dia":"%s","motivo":"espera_ram_agotada","ram_mb":%s,"hhmm":%s,"t":"%s"}\n' "$d" "${ram:-0}" "$h" "$(ts)" > "${OUT}abortado_${d}.json" ; continue; fi
  echo "$(ts) >>> rf5_k6_dia $d (ram=${ram}MB hhmm=$h)"
  ( ulimit -v 5000000; /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 /usr/bin/time -v -o "${OUT}pico_k6_$d.txt" python3 -I "${HV}rf5_k6_dia.py" "$d" ) 2>&1 | while IFS= read -r l; do echo "$(ts) $l"; done
  r=${PIPESTATUS[0]}; [ "$r" -ne 0 ] && { rc=1; echo "$(ts) dia $d rc=$r"; }
done
python3 -I "${HV}c4_btc.py" 2>&1 | while IFS= read -r l; do echo "$(ts) c4: $l"; done
find "$OUT" -maxdepth 1 \( -name 'run_k6_*.log' -o -name 'pico_k6_*.txt' \) -mtime +30 -delete          # retencion 30 d de logs/picos (los pkl rf5K6 se conservan: entrada de la evaluacion)
hb FIN; echo "$(ts) run_k6 fin rc=$rc"; exit $rc
} >> "$LOG" 2>&1
