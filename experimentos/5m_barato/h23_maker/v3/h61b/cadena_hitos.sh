#!/bin/bash
# Cadena HITO 1-3 (descriptiva, offline, UN job pesado a la vez, reanudable: cada paso es idempotente). Guardas: 06:00-09:15Z y 22:15-22:30Z prohibidas, MemAvailable>1,8 GB, load1<16.
# Orden: BTC 21 -> BTC 17,18 -> extraccion alts 19-21 -> ETH/SOL/XRP 17-21 -> BTC ext 17-21 -> DOGE/BNB 17-21 -> BTC DISC 06-16 (solo v3 y C_reg).
Z=/root/polymarket-research/experimentos/5m_barato/h23_maker/v3/h61b; R2=/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r2; V2=/root/polymarket-research/experimentos/5m_barato/h23_maker/v2
DL=/root/polymarket-research-datalogs/h61b; PY=/usr/bin/python3; LOG=$DL/cadena_hitos.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
ok() { h=$(date -u +%H%M); mem=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); l1=$(awk '{print int($1)}' /proc/loadavg)
  if { [ "$h" -ge 0600 ] && [ "$h" -lt 0915 ]; } || { [ "$h" -ge 2215 ] && [ "$h" -lt 2230 ]; }; then return 1; fi; [ "$mem" -gt 1800 ] && [ "$l1" -lt 16 ]; }
paso() { local et="$1"; shift; for i in $(seq 1 600); do ok && break; sleep 60; done; ok || { log "BLOCKED $et"; exit 4; }
  log "inicio $et"; ( ulimit -v 3000000; nice -n 19 ionice -c3 "$@" ) >> $LOG 2>&1 || { log "ERROR $et"; return 1; }; log "fin $et"; }
D5="2026-10-17 2026-10-18 2026-10-19 2026-10-20 2026-10-21"
paso "extrae BTC 21" bash $R2/extrae_btc.sh 2026-10-21 && paso "sim BTC 21" $PY -I $Z/h61b_sim.py 2026-10-21 BTC
for D in 2026-10-17 2026-10-18; do paso "sim BTC $D" $PY -I $Z/h61b_sim.py $D BTC; done
paso "extrae alts 19-21" bash $V2/extrae_alts.sh 2026-10-19 2026-10-20 2026-10-21
for C in ETH SOL XRP; do for D in $D5; do paso "sim $C $D" $PY -I $Z/h61b_sim.py $D $C; done; done
for D in $D5; do paso "sim BTC ext $D" $PY -I $Z/h61b_sim.py $D BTC --ext; done
paso "extrae doge/bnb 19-21" bash $V2/extrae_dogebnb.sh 2026-10-19 2026-10-20 2026-10-21
for C in DOGE BNB; do for D in $D5; do paso "sim $C $D" $PY -I $Z/h61b_sim.py $D $C; done; done
for D in 2026-10-06 2026-10-07 2026-10-08 2026-10-09 2026-10-10 2026-10-11 2026-10-12 2026-10-13 2026-10-14 2026-10-15 2026-10-16; do paso "sim BTC DISC $D" $PY -I $Z/h61b_sim.py $D BTC; done
log "CADENA COMPLETA"
