#!/bin/bash
# PLAN C6 (NO instalado): resolvedor + informe diario del dry-run B-CXB60. Cron sugerido (despues de sa_r1 que escribe gmap_*.json; fuera de 06-09Z):
#   40 10 * * * nice -n 19 ionice -c3 flock -n /tmp/cxb60_resolve.lock /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/dryrun/cron_resolve_cxb60.sh
# Aviso de FALLO (trampa "vigia que muere en silencio"): cualquier error => Telegram. El informe solo lee/escribe en datalogs/cxb60_dryrun/.
set -u
SC=/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/dryrun; PY=${CXB60_PY:-/root/polymarket-research/.venv/bin/python}; O=${CXB60_OUT:-/root/polymarket-research-datalogs/cxb60_dryrun}; LOGR=${CXB60_LOG_RESOLVE:-/root/polymarket-research/logs/cxb60_resolve.log}   # CXB60_* solo para pruebas en seco
aviso() {
  [ -n "${CXB60_SIN_TELEGRAM:-}" ] && { echo "AVISO (seco, sin Telegram): cxb60 resolve FALLO: $1"; return; }
  cd /root/polymarket-research && $PY -c "import sys; from shadow_digest import enviar_telegram; enviar_telegram(sys.argv[1])" "cxb60 resolve FALLO: $1" ; }
ulimit -v 7000000
fallo=0
for i in 1 2 3 4 5 6; do   # ultimos dias cerrados (ayer, anteayer...): el gmap oficial de un dia puede tardar
  d=$(date -u -d "-$i day" +%F)
  [ -f "$O/dec_$d.csv.gz" ] || continue
  $PY -I "$SC/cxb60_resolve.py" "$d" --out "$O" >> "$LOGR" 2>&1 || fallo=1
  [ -f "$O/c59/dec_$d.csv.gz" ] && { $PY -I "$SC/cxb60_resolve.py" "$d" --out "$O/c59" >> "$LOGR" 2>&1 || fallo=1; }
done
$PY -I "$SC/cxb60_informe.py" --out "$O" >> "$LOGR" 2>&1 || fallo=1
[ "$fallo" = 1 ] && aviso "ver logs/cxb60_resolve.log"
exit $fallo
