#!/bin/bash
# suelo_diario.sh [DIA] -- (E2) genera la tabla de suelo sucesora hasta DIA (por defecto AYER UTC) y la PROPONE al chief (no firma nada). Cron 04:40Z (m5_registro de DIA cierra ~04:03Z de DIA+1). Pesado => scripts/cron_pesado.sh, nice 19, ionice -c3, ulimit -v 1.5 GB,
# nunca 06:00-09:15Z ni 22:15-22:30Z (aborta si cae ahi). Idempotente: suelo_dia.sh salta dias con .done. Avisa por Telegram con ruta+sha; si falla: aviso de fallo (nunca tragado). Parada por PID: no aplica (corta).
HERE="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)/"; cd "$HERE"; D=${1:-$(date -u -d yesterday +%F)}
ts() { date -u +%FT%TZ; }; h=$((10#$(date -u +%H%M)))
{ [ "$h" -ge 600 ] && [ "$h" -lt 915 ]; } || { [ "$h" -ge 2215 ] && [ "$h" -lt 2230 ]; } && { echo "$(ts) ventana prohibida, no se lanza"; exit 0; }
aviso() { /usr/bin/python3 -I -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram; enviar_telegram(sys.argv[1])" "$1" >/dev/null 2>&1; }
fallo() { echo "$(ts) FALLO $1"; aviso "RF5 suelo_diario FALLO ($D): $1. Ver suelo_sucesora/suelo_diario.log"; exit 1; }
[ -f /mnt/HC_Volume_106538179/m5_registro/m5_registro_$D.csv.gz ] || fallo "falta m5_registro_$D"
[ "$(date -u +%s)" -ge "$(date -u -d "$D +1 day 04:10" +%s)" ] || fallo "m5_registro de $D aun no cerrado (cierra 04:03Z de D+1)"
exec 9>"${HERE}.suelo.lock"; flock -n 9 || { echo "otro suelo_diario en curso"; exit 0; }
d=2026-11-18; while [ "$d" \< "$(date -u -d "$D +1 day" +%F)" ]; do
  ( ulimit -v 1500000; /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 ./suelo_dia.sh "$d" ) || fallo "suelo_dia $d"; d=$(date -u -d "$d +1 day" +%F); done
( ulimit -v 1500000; /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 /usr/bin/python3 -I suelo_tabla.py ) > suelo_tabla.out 2>&1 || fallo "suelo_tabla.py"
R=$(/usr/bin/python3 -I suelo_filtra.py "$D") || fallo "comprobaciones de la tabla: $R"
aviso "RF5 tabla de suelo sucesora hasta $D: $(echo "$R" | /usr/bin/python3 -I -c "import sys,json; j=json.load(sys.stdin); print(j['ruta'].split('/')[-1], j['sha256'][:16])") PROPUESTA para firma del chief (rf5_cortes.json::tabla_suelo_sucesora); sin ella el dia $D no es VALIDO (suelo_pendiente)."
echo "$(ts) OK $D $R"
