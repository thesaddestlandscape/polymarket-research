#!/bin/bash
# run_sec7.sh -- R1v2 sec.7 (a)-(d). NO LANZAR antes de las 12:30Z. Idempotente (el runner salta lo COMPLETE y valida el sha de los outputs). Uno a la vez (flock), cron_pesado, nice 19, ionice -c3, ulimit -v 3 GB.
# Arranca solo si: hora UTC >= 12:30 (y fuera de 06:00-09:15Z), la cadena de la pista cola ha acabado (chain.status = COMPLETE; se SOLO LEE), RAM libre >= 5 GB. Espera hasta 10 h; si no, termina con codigo 3 (BLOQUEADO, nada hecho).
# EV: apagado por defecto (SEC7_EMITIR_EV=1 solo con permiso del chief tras cumplir CONTRATO_R1v2 sec.11).
HV="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)/"; BR="$(dirname "${HV%/}")/"
CHAIN="${BR}pista_cola_18nov/out/verif_adenda11/chain.status"
OUT="${SEC7_OUT:-${HV}out_sec7/}"; mkdir -p "$OUT"; LOG="${OUT}run_$(date -u +%Y%m%dT%H%M%SZ).log"
exec 8>"${OUT}.lock"; flock -n 8 || { echo "otro run_sec7 en curso"; exit 2; }
ts() { date -u +%FT%TZ; }
{
echo "$(ts) run_sec7 inicio (espera de condiciones)"
for i in $(seq 1 1200); do          # 1200 x 30 s = 10 h
  hm=$(date -u +%H%M); hm=$((10#$hm)); ram=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
  chain=$(cut -d' ' -f1 "$CHAIN" 2>/dev/null)
  if [ "$hm" -ge 1230 ] && [ "$chain" = "COMPLETE" ] && [ "${ram:-0}" -ge 5000 ]; then break; fi
  [ $((i % 20)) -eq 1 ] && echo "$(ts) espera: hhmm=$hm chain=${chain:-?} ram=${ram}MB"
  sleep 30
done
hm=$(date -u +%H%M); hm=$((10#$hm)); chain=$(cut -d' ' -f1 "$CHAIN" 2>/dev/null)
if [ "$hm" -lt 1230 ] || [ "$chain" != "COMPLETE" ]; then echo "$(ts) BLOQUEADO: condiciones no cumplidas (hhmm=$hm chain=${chain:-?})"; exit 3; fi
if { [ "$hm" -ge 600 ] && [ "$hm" -lt 915 ]; }; then echo "$(ts) BLOQUEADO: franja 06:00-09:15Z"; exit 3; fi
PY="nice -n 19 ionice -c3 python3"; rc=0
run() { echo "$(ts) >>> $*"; ( ulimit -v 3000000; /root/polymarket-research/scripts/cron_pesado.sh $PY "${HV}sec7_run.py" "$@" ) 2>&1 | while IFS= read -r l; do echo "$(ts) $l"; done; r=${PIPESTATUS[0]}; [ "$r" -ne 0 ] && rc=1; }
run global
for d in 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do run oct $d; done
for d in 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07 2026-11-08 2026-11-09; do run sim $d; done
run final
echo "$(ts) run_sec7 fin rc=$rc"; exit $rc
} >> "$LOG" 2>&1
