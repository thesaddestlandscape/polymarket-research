#!/bin/bash
# H61b forward DIARIO (DRY-RUN / medicion offline; no envia ni firma nada). Procesa el dia UTC anterior (o los dias dados). Idempotente: salta lo hecho y valido.
# Cron sugerido (NO instalado; lo decide el chief):  10 10 * * *  nice -n 19 ionice -c3 bash /root/polymarket-research/experimentos/5m_barato/h23_maker/v3/h61b/run_h61b_diario.sh || aviso
# Un UNICO job pesado: si hay otro en curso (flock) no arranca. Guardas: nunca 06:00-09:15Z ni 22:15-22:30Z; MemAvailable>1,8 GB (suelo duro; guard_ram reinicia <900 MB); load5<16.
Z=/root/polymarket-research/experimentos/5m_barato/h23_maker/v3/h61b
R2=/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r2
V2=/root/polymarket-research/experimentos/5m_barato/h23_maker/v2
DL=/root/polymarket-research-datalogs/h61b
PY=/usr/bin/python3
mkdir -p $DL
LOG=$DL/run_$(date -u +%F).log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
avisa() { $PY -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e('🚨 H61b forward: $1 FALLÓ, ver $LOG')" >> $LOG 2>&1; }
exec 9>$DL/.lock; flock -n 9 || { log "otro job H61b en curso: salgo"; exit 0; }
DIAS="$@"; [ -z "$DIAS" ] && DIAS=$(date -u -d yesterday +%F)
ok_recursos() { h=$(date -u +%H%M); mem=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); l5=$(awk '{print int($1)}' /proc/loadavg)   # load1 como cota rapida
  if { [ "$h" -ge 0600 ] && [ "$h" -lt 0915 ]; } || { [ "$h" -ge 2215 ] && [ "$h" -lt 2230 ]; }; then return 1; fi
  [ "$mem" -gt 1800 ] && [ "$l5" -lt 16 ]; }
paso() { # $1 etiqueta, resto = comando
  local et="$1"; shift
  for i in $(seq 1 90); do ok_recursos && break; sleep 120; done
  ok_recursos || { log "BLOCKED $et (recursos/ventana)"; $PY -I $Z/h61b_manifest.py BLOCKED "$et" >> $LOG 2>&1; avisa "$et BLOCKED"; exit 4; }
  log "inicio $et"; ( ulimit -v 3000000; nice -n 19 ionice -c3 "$@" ) >> $LOG 2>&1 || { log "ERROR $et"; $PY -I $Z/h61b_manifest.py FAILED "$et" >> $LOG 2>&1; avisa "$et"; return 1; }
  log "fin $et"; }
$PY -I $Z/h61b_manifest.py inicio "dias: $DIAS" >> $LOG 2>&1
for D in $DIAS; do
  [ "$D" \> "$(date -u -d yesterday +%F)" ] && { log "$D es hoy o futuro: no se procesa"; continue; }
  paso "extrae BTC $D" bash $R2/extrae_btc.sh $D && paso "sim BTC $D" $PY -I $Z/h61b_sim.py $D BTC && paso "sim BTC ext $D" $PY -I $Z/h61b_sim.py $D BTC --ext
  if paso "extrae alts $D" bash $V2/extrae_alts.sh $D && paso "extrae doge/bnb $D" bash $V2/extrae_dogebnb.sh $D; then
    for C in ETH SOL XRP DOGE BNB; do paso "sim $C $D" $PY -I $Z/h61b_sim.py $D $C; done
  fi
  $PY -I $Z/h61b_manifest.py paso "dia $D procesado" >> $LOG 2>&1
done
paso "vigia BTC" $PY -I $Z/h61b_vigia.py --coin BTC --telegram
paso "vigia ext BTC" $PY -I $Z/h61b_vigia.py --coin BTC --ext
$PY -I $Z/h61b_manifest.py fin "ok" >> $LOG 2>&1
find /mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/alts \( -name 'rows_*_2026-10-19.csv.gz' -o -name 'rows_*_2026-1[0-2]-[2-3]*.csv.gz' \) -mtime +6 -delete   # extractos alts del forward (~0,3 GB/dia): retencion 6 d
 find $DL -name 'feed_live_*.npz' -mtime +30 -delete; find $DL -name 'run_*.log' -mtime +30 -delete
log "FIN $DIAS"
