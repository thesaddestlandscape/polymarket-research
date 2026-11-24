#!/bin/bash
# btc_backfill.sh -- E7 BTC (ESPEC RF5 / ADENDA C4): backfill SERIAL de btc_ms (ms_extract_lowmem.py, SA_COINS=BTC SA_TAG=btc) para 02..22-Nov (prioridad 03..17, luego 18..22, luego 02) y prep_day_btc (tape_btc/bad_btc) para 03..17, un trabajo pesado a la vez
# por scripts/cron_pesado.sh, nice 19, ionice -c3, ulimit -v 3,5 GB (extraccion) / 5 GB (prep). Nunca 06:00-09:15Z ni 22:15-22:30Z; espera MemAvailable>=5500 MB (hasta ~4 h por trabajo y luego lo salta). Idempotente: omite lo ya hecho.
# Estado: out_rf5_ciego/btc_backfill_estado.json (por dia: ms/tape) + log con marca de tiempo. Parada: por PID guardado (out_rf5_ciego/btc_backfill.pid), nunca por patron. Lanzar siempre por su ruta (setsid nohup).
HV="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)/"; OUT=${RF5_OUT:-${HV}out_rf5_ciego/}; mkdir -p "$OUT"; DL=/root/polymarket-research-datalogs; SC=/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/scripts
exec 8>"${OUT}.btc_backfill.lock"; flock -n 8 || { echo "otro btc_backfill en curso"; exit 0; }; echo $$ > "${OUT}btc_backfill.pid"
ts() { date -u +%FT%TZ; }; LOG="${OUT}btc_backfill_$(date -u +%Y%m%d).log"
ok_ahora() { h=$((10#$(date -u +%H%M))); ram=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
  { [ "$h" -lt 600 ] || [ "$h" -ge 915 ]; } && { [ "$h" -lt 2215 ] || [ "$h" -ge 2230 ]; } && [ "${ram:-0}" -ge "${RF5_RAM_MIN:-5500}" ]; }
espera() { for i in $(seq 1 ${RF5_ESPERA:-480}); do ok_ahora && return 0; sleep 30; done; return 1; }
{
echo "$(ts) btc_backfill inicio"
# v3 (ordenes 24-Nov): ANTES de usar cualquier tape_btc/btc_ms nuevo, c4_equiv_lowmem sobre 17-Nov (lowmem frente a ms_extract) debe dar igual:true con los sha de los scripts vigentes; si no, BLOQUEADO y no se extrae nada (no se mezcla con los btc_ms 17-Oct..01-Nov de otro extractor sin esa equivalencia)
EQ="$DL/rf5_btc/equiv_lowmem_2026-11-17.json"
equiv_ok() { python3 -I -c "import json,sys,hashlib; j=json.load(open(sys.argv[1])); sc=sys.argv[2]; sys.exit(0 if j.get('igual') is True and j.get('sha_lowmem')==hashlib.sha256(open(sc+'ms_extract_lowmem.py','rb').read()).hexdigest() and j.get('sha_orig')==hashlib.sha256(open(sc+'ms_extract.py','rb').read()).hexdigest() else 1)" "$EQ" "$SC/" 2>/dev/null; }
if ! equiv_ok; then
  espera && ( ulimit -v 3500000 && /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 python3 -I "${HV}c4_equiv_lowmem.py" 2026-11-17 ) 2>&1 | while IFS= read -r l; do echo "$(ts) $l"; done
fi
if ! equiv_ok; then echo "$(ts) BLOQUEADO_EQUIV: lowmem != ms_extract (o sin ensayo) en 2026-11-17: no se extrae ningun dia BTC"; python3 -I "${HV}c4_btc.py" 2>&1 | while IFS= read -r l; do echo "$(ts) c4: $l"; done; echo "$(ts) btc_backfill fin (BLOQUEADO)"; exit 1; fi
echo "$(ts) equivalencia lowmem OK en 2026-11-17: se reanuda el backfill"
ORDEN=(); for d in $(seq 3 17); do ORDEN+=("2026-11-$(printf %02d $d)"); done; for d in $(seq 18 22); do ORDEN+=("2026-11-$d"); done; ORDEN+=("2026-11-02")
for d in "${ORDEN[@]}"; do
  if [ ! -f "$DL/sa_ms/btc_ms_$d.npz" ]; then
    ls $DL/maker_ms_${d}_*.csv.gz >/dev/null 2>&1 || { echo "$(ts) SIN_RAW $d (maker_ms crudo no esta en datalogs)"; continue; }
    espera || { echo "$(ts) BLOCKED $d: ventana/RAM"; continue; }
    echo "$(ts) >>> btc_ms $d"
    ( cd "$SC" && ulimit -v 3500000 && SA_COINS=BTC SA_TAG=btc OMP_NUM_THREADS=1 /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 /usr/bin/time -v -o "${OUT}pico_btcms_$d.txt" python3 -I "$SC/ms_extract_lowmem.py" "$d" ) 2>&1 | while IFS= read -r l; do echo "$(ts) $l"; done
  fi
  if [[ "$d" > "2026-11-02" && "$d" < "2026-11-18" ]] && [ -f "$DL/sa_ms/btc_ms_$d.npz" ] && { [ ! -f "$DL/rf5_btc/tape_btc_$d.pkl" ] || [ ! -f "$DL/rf5_btc/bad_btc_$d.json" ]; }; then
    espera || { echo "$(ts) BLOCKED prep $d: ventana/RAM"; continue; }
    echo "$(ts) >>> prep_day_btc $d"
    ( ulimit -v 5000000 && /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 /usr/bin/time -v -o "${OUT}pico_prepbtc_$d.txt" python3 -I "${HV}prep_day_btc.py" "$d" ) 2>&1 | while IFS= read -r l; do echo "$(ts) $l"; done
  fi
done
python3 -I "${HV}c4_btc.py" 2>&1 | while IFS= read -r l; do echo "$(ts) c4: $l"; done
find "$OUT" -maxdepth 1 \( -name 'btc_backfill_*.log' -o -name 'pico_btcms_*.txt' -o -name 'pico_prepbtc_*.txt' \) -mtime +30 -delete          # retencion 30 d (btc_ms y tape_btc se conservan: entrada de los cortes BTC)
echo "$(ts) btc_backfill fin"
} >> "$LOG" 2>&1
