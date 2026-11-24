#!/bin/bash
# run_nulo_inc.sh -- NULO INCREMENTAL de RF5E-COMB (ADENDA_RF5_NULO_INCREMENTAL_24nov): calcula las replicas del nulo POR DIA COMPLETE (>= 24-Nov), familias K, K6, A en ese orden; reanudable (checkpoint con fsync por replica; las hechas se saltan).
# Cron propio (el chief lo instala; ver cron_nulo_inc.txt): `flock -n /tmp/rf5_nulo_inc.lock run_nulo_inc.sh >> logs/run_nulo_inc.log 2>&1 || vigia_rf5.py --aviso-nulo --telegram`. Un job pesado a la vez (lanza_pesado -> scripts/cron_pesado.sh: flock global, nice 19, ionice -c3, ulimit -v 5 GB),
# espera MemAvailable>=5500 MB y ventana permitida (nunca 06:00-09:15Z ni 22:15-22:30Z); el propio rf5_nulo_inc.py PARA al entrar en una ventana prohibida (rc 0, 'PARCIAL': la siguiente invocacion reanuda). workers = 1 FIJO (el fork duplica RAM: OOM el 24-Nov con 2).
# Si se agota la espera de ventana/RAM => rc!=0 (aviso). Latido: heartbeat_nulo_inc.json (lo lee vigia_rf5.py R10). Parada: por PID guardado (out_rf5_ciego/nulo_inc.pid), nunca por patron. Retencion 30 d de logs/picos.
HV="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)/"; OUT=${RF5_OUT:-${HV}out_rf5_ciego/}; mkdir -p "$OUT"
exec 8>"${OUT}.nulo_inc.lock"; flock -n 8 || { echo "otro run_nulo_inc en curso"; exit 0; }; echo $$ > "${OUT}nulo_inc.pid"
ts() { date -u +%FT%TZ; }; LOG="${OUT}run_nulo_inc_$(date -u +%Y%m%dT%H%M%SZ).log"
hb() { printf '{"estado":"%s","t":"%s","epoch":%s}\n' "$1" "$(ts)" "$(date +%s)" > "${OUT}heartbeat_nulo_inc.json.tmp" && mv "${OUT}heartbeat_nulo_inc.json.tmp" "${OUT}heartbeat_nulo_inc.json"; }
{
hb INICIO; echo "$(ts) run_nulo_inc inicio"
RF5_OUT="$OUT" bash "${HV}lanza_pesado.sh" "${OUT}nulo_inc_lanza.log" "${OUT}pico_nulo_inc_$(date -u +%Y%m%d).txt" python3 -I "${HV}rf5_nulo_inc.py" cola; rc=$?
cat "${OUT}nulo_inc_lanza.log" 2>/dev/null | tail -5 | while IFS= read -r l; do echo "$(ts) $l"; done
find "$OUT" -maxdepth 1 \( -name 'run_nulo_inc_*.log' -o -name 'pico_nulo_inc_*.txt' \) -mtime +30 -delete
hb FIN; echo "$(ts) run_nulo_inc fin rc=$rc"; exit $rc
} >> "$LOG" 2>&1
