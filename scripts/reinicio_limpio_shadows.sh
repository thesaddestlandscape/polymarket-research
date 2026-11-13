#!/bin/bash
# Reinicio SIN PERDIDA de los shadows de 5m barato cuando RSS+swap supera el umbral (13-Nov, OK Javi).
# Por que: su guarda interna «sale si RSS > 400-450 MB» no ve la memoria en swap (h23shadowv3: RSS 122 MB + 1,0 GB en swap) y
# los ficheros son los del prerregistro (no se editan). Un reinicio a ciegas deja el par/mercado en curso como completo=false.
# Como: se para SOLO en el hueco en que no vigilan ningun mercado y se relanza al instante con el MISMO comando del watchdog:
#   h23shadow / h23shadowv3 / F2 dry-run: par 5m/15m que cierra en C (C%900==0), vigilado desde C-370 s hasta C  -> hueco [C+60, C+290]
#   r3shadow: cada 5m, vigilado desde apertura-25 s hasta cierre-45 s; arranca en ~7-16 s                          -> parar en [cierre-38, cierre-32]
# Cron: 3,33 * * * * (fase 180 s del cuarto de hora). Verificado a mano el 13-Nov 07:33Z (sin_cierre=0, par 07:45 completo).
# Uso: reinicio_limpio_shadows.sh [--forzar]     (--forzar ignora el umbral)
set -u
REPO=/root/polymarket-research
UMBRAL_MB=450
FORZAR=${1:-}
LOG=$REPO/logs/reinicio_limpio_shadows.log
exec 8>/tmp/reinicio_limpio_shadows.lock; flock -n 8 || exit 0
log() { echo "$(date -u +%FT%TZ) $*" >> "$LOG"; }

pid_python() {   # $1 = nombre del script .py; solo procesos cuyo ejecutable es python (no el bash/screen que lo envuelve)
  for p in $(pgrep -f -- "$1"); do
    case "$(cat /proc/$p/comm 2>/dev/null)" in python*) echo "$p"; return;; esac
  done
}
mem_mb() { awk '/^VmRSS|^VmSwap/{s+=$2} END{print int(s/1024)}' /proc/$1/status 2>/dev/null; }
esperar_fase() {  # $1 periodo, $2 min, $3 max ; espera como mucho un periodo
  local fin=$(( $(date +%s) + $1 + 5 ))
  while [ "$(date +%s)" -lt "$fin" ]; do f=$(( $(date +%s) % $1 )); [ $f -ge $2 ] && [ $f -le $3 ] && return 0; sleep 0.5; done
  return 1
}
parar() {  # $1 pid ; True si ha salido
  kill -TERM "$1"; for i in $(seq 1 60); do kill -0 "$1" 2>/dev/null || return 0; sleep 0.25; done; return 1
}

shadow() {  # $1 screen, $2 script, $3 periodo, $4 fase_min, $5 fase_max
  local pid; pid=$(pid_python "$2"); [ -n "$pid" ] || return 0
  local m; m=$(mem_mb "$pid"); [ -n "$FORZAR" ] || [ "${m:-0}" -gt $UMBRAL_MB ] || return 0
  local cmd; cmd=$(cd $REPO && python3 -c "import pipeline_watchdog as w; print(w.SCREEN_RESTART['$1'])") || { log "$1: sin comando del watchdog, no toco"; return 0; }
  [ -n "$cmd" ] || return 0
  esperar_fase "$3" "$4" "$5" || { log "$1: ventana no alcanzada, no toco"; return 0; }
  parar "$pid" || { log "$1 pid=$pid NO sale con TERM: no relanzo (lo hara el watchdog si muere)"; return 0; }
  sleep 0.5
  if screen -ls | grep -q "\.$1[[:space:]]"; then log "$1: la screen ya existe (watchdog), no relanzo"; else screen -dmS "$1" bash -c "$cmd"; fi
  log "$1 reiniciado en ventana (pid $pid, RSS+swap ${m} MB)"
}

f2() {  # $1 = btc|alt
  local pf=/root/polymarket-research-datalogs/f2_5m_barato/$1.pid; [ -f "$pf" ] || return 0
  local pid; pid=$(cat "$pf"); [ -r "/proc/$pid/status" ] || return 0
  local m; m=$(mem_mb "$pid"); [ -n "$FORZAR" ] || [ "${m:-0}" -gt $UMBRAL_MB ] || return 0
  esperar_fase 900 60 280 || { log "f2 $1: ventana no alcanzada, no toco"; return 0; }
  "$REPO/scripts/f2_5m_barato_lanzar.sh" "$1" >/dev/null 2>&1
  log "f2 $1 reiniciado en ventana (pid $pid, RSS+swap ${m} MB)"
}

shadow h23shadowv3 "-I h23_shadow_v3.py" 900 60 290
shadow h23shadow   "-I h23_shadow.py"    900 60 290
f2 btc
f2 alt
shadow r3shadow    "-I r3_shadow.py"     300 262 268
