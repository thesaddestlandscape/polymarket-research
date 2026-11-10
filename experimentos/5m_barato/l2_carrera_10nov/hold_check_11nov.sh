#!/bin/bash
# 10-Nov (Javi): primera noche de la proteccion/extraccion del HOLD L2 (>=10-Nov). Lanzado con `at` a las 00:55Z del 11-Nov.
# 1) comprueba enlaces duros del 10-Nov en libro5_ms_prot (si faltan: proteger_libro5_ms.sh)
# 2) espera (max 30 min) a que acabe el cron de extraccion (00:50Z)
# 3) comprueba libro5_b40_2026-11-10 (existe, gzip -t, stats.json); si falta: la extrae a mano UNA vez
# 4) avisa por Telegram con el resultado (OK o FALLO). No toca crons ni datos de produccion salvo esas dos acciones idempotentes.
R=/root/polymarket-research
P=/mnt/HC_Volume_106538179/libro5_ms_prot
B=/mnt/HC_Volume_106538179/libro5_b40
DIA=${1:-2026-11-10}
LOG=$R/logs/hold_check_11nov.log
msg=""
log(){ echo "$(date -u +%FT%TZ) $*" >> "$LOG"; }
tg(){ python3 -c "import sys; sys.path.insert(0,'$R'); from shadow_digest import enviar_telegram; enviar_telegram(sys.argv[1])" "$1" >> "$LOG" 2>&1; }

n_prot=$(ls "$P" 2>/dev/null | grep -c "libro5_ms_$DIA")
n_orig=$(ls /mnt/HC_Volume_106538179/libro5_ms 2>/dev/null | grep -c "libro5_ms_$DIA")
log "prot $DIA: $n_prot de $n_orig"
if [ "$n_prot" -lt "$n_orig" ]; then
  log "faltan enlaces: ejecuto proteger_libro5_ms.sh"
  nice -n 19 ionice -c3 "$R/scripts/proteger_libro5_ms.sh" >> "$R/logs/proteger_libro5_ms.log" 2>&1
  n_prot=$(ls "$P" 2>/dev/null | grep -c "libro5_ms_$DIA")
  log "prot tras reintento: $n_prot de $n_orig"
fi
[ "$n_prot" -ge "$n_orig" ] && [ "$n_orig" -gt 0 ] && msg="enlaces OK ($n_prot/$n_orig)" || msg="ENLACES FALTAN ($n_prot/$n_orig)"

for i in $(seq 1 60); do pgrep -f "l2_extraer_dia.py" >/dev/null || break; sleep 30; done

ok_b40() { [ -s "$B/libro5_b40_$DIA.csv.gz" ] && [ -s "$B/libro5_b40_$DIA.stats.json" ] && nice -n 19 gzip -t "$B/libro5_b40_$DIA.csv.gz" 2>/dev/null; }
if ! ok_b40; then
  log "b40 $DIA ausente o corrupto: extraigo a mano"
  ( ulimit -v 3000000; nice -n 19 ionice -c3 "$R/experimentos/5m_barato/l2_b5m/extraer_l2_b5m.sh" "$DIA" >> "$R/logs/extraer_l2_b5m.log" 2>&1 )
fi
if ok_b40; then
  tam=$(du -h "$B/libro5_b40_$DIA.csv.gz" | cut -f1)
  filas=$(python3 -c "import json,sys; print(json.load(open('$B/libro5_b40_$DIA.stats.json')).get('total_filas_salida'))" 2>/dev/null)
  msg="$msg; b40 $DIA OK ($tam, filas=$filas)"
  ult=$(tail -3 "$R/logs/extraer_l2_b5m.log" | grep -c FALLO)
  [ "$ult" -gt 0 ] && msg="$msg (ojo: FALLO en las ultimas lineas del log)"
  tg "HOLD L2 $DIA: $msg"
else
  tg "HOLD L2 $DIA: FALLO. $msg; b40 $DIA NO disponible tras reintento. Revisar logs/extraer_l2_b5m.log y logs/hold_check_11nov.log; libro5_ms sigue protegido si los enlaces estan OK."
fi
log "fin: $msg"
