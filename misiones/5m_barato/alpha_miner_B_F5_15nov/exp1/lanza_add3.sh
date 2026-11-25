#!/bin/bash
# lanza_add3.sh (16-Nov-2026, Javi: "programarlo para que se lance independientemente de que esta sesion siga abierta")
# Supervisor de ADD3, lanzado por atd (sobrevive a la sesion). NO calcula nada: espera ventana y calma y llama a run_add3_r.sh (copia de run_add3.sh con DEADLINE dinamico, mismas reglas, retoma dias COMPLETE).
# Condiciones para lanzar: hora 09:25-21:30Z (nunca 06:00-09:15Z), load1 <= 8 y MemAvailable >= 4000 MB (antes 5500; Javi 16-Nov, pico medido ADD3 1,0-1,3 GB) durante 3 comprobaciones seguidas (cada 60 s; condicion de la revision de integridad 16-Nov).
# Si run_add3_r.sh acaba sin dejar ADD3_job=FIN en STATUS.json (OOM, 21:30Z), vuelve a esperar y reintenta; se rinde a las 48 h. Log: exp1/lanza_add3.log
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1; LOG=$H/lanza_add3.log
export PATH=/usr/local/bin:/usr/bin:/bin
cd $H || exit 9
exec 9>$H/.lanza_add3.lock; flock -n 9 || { echo "$(date -u +%FT%TZ) otro supervisor vivo: salgo" >> $LOG; exit 0; }
# 16-Nov: el supervisor ya NO se pone oom_score_adj 500 (murio en OOM global 16:15Z); el +500 queda solo en run_add3_r.sh (el trabajo)
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
T0=$(date -u +%FT%TZ); MAXT=$(( $(date -u +%s) + 48*3600 ))
fin() { python3 -I -c "
import json,sys
S=json.load(open('$H/STATUS.json')); j=S.get('ADD3_job') or {}
sys.exit(0 if j.get('estado')=='FIN' and j.get('t','')>='$T0' else 1)"; }
ventana() { local h; h=$(date -u +%H%M); [ "$h" -ge 0925 ] && [ "$h" -lt 2130 ]; }
calma() { local l a; l=$(awk '{print $1}' /proc/loadavg); a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); awk -v l="$l" 'BEGIN{exit !(l<=8.0)}' && [ "${a:-0}" -ge 4000 ]; }
log "===== supervisor ADD3 pid $$ arrancado; espero ventana 09:25-21:30Z + load1<=8 + MemAvailable>=4000 MB (x3)"
n=0; k=0
while [ "$(date -u +%s)" -lt "$MAXT" ]; do
  if ventana && calma; then n=$((n+1)); else n=0; fi
  [ $((k % 30)) -eq 0 ] && log "espera: n_ok=$n hora $(date -u +%H%M)Z load1 $(awk '{print $1}' /proc/loadavg) MemAvailable_MB $(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)"
  k=$((k+1))
  if [ "$n" -ge 3 ]; then
    log "lanzo run_add3_r.sh"; bash $H/run_add3_r.sh; rc=$?; log "run_add3_r.sh termino rc=$rc"
    fin && { log "ADD3 FIN verificado en STATUS.json: supervisor termina"; exit 0; }
    log "ADD3 NO terminado (sin FIN en STATUS): reintento tras 10 min y calma"; n=0; sleep 600
  fi
  sleep 60
done
log "48 h sin completar ADD3: me rindo (revisar run_add3.log)"
