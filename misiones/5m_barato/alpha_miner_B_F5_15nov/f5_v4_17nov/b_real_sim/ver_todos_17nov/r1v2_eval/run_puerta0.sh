#!/bin/bash
# run_puerta0.sh -- R1v2 FASE A (Puerta 0). NO LANZAR sin OK del chief. Idempotente (puerta0_run.py salta lo COMPLETE y valida el sha de los outputs). Uno a la vez (flock), cron_pesado, nice 19, ionice -c3, ulimit -v 5 GB (ADENDA_06b, OK Javi 23-Nov; antes 3 GB), RAM >= 5,5 GB.
# Arranca solo si: hora UTC >= 12:30 y fuera de 06:00-09:15Z, la cadena de la pista cola ha acabado (chain.status = COMPLETE; solo se LEE) y RAM libre >= 5 GB. Espera hasta 10 h; si no, termina con codigo 3 (BLOQUEADO, nada hecho).
# Parada: por PID guardado (out_p0/run.pid) con kill; el script se lanza por su ruta.
HV="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)/"; V="$(dirname "${HV%/}")/"
CHAIN="${P0_CHAIN:-${V}pista_cola_18nov/out/verif_adenda11/chain.status}"      # P0_CHAIN/P0_HM/P0_RAM_MIN/P0_ESPERA/P0_PREREG_DIR: solo para tests de las puertas
RAM_MIN="${P0_RAM_MIN:-5500}"; ESPERA="${P0_ESPERA:-1200}"; PRD="${P0_PREREG_DIR:-$V}"
OUT="${P0_OUT:-${HV}out_p0/}"; mkdir -p "$OUT"; LOG="${OUT}run_$(date -u +%Y%m%dT%H%M%SZ).log"
exec 8>"${OUT}.lock"; flock -n 8 || { echo "otro run_puerta0 en curso"; exit 2; }
echo $$ > "${OUT}run.pid"      # solo tras tomar el flock: nunca se pisa el PID del run en curso
ts() { date -u +%FT%TZ; }
hm_now() { if [ -n "$P0_HM" ]; then echo $((10#$P0_HM)); else h=$(date -u +%H%M); echo $((10#$h)); fi; }
prereg_ok() { local f; for f in PREREG_R1v2_19nov PREREG_R1v2_19nov_ADENDA_01 PREREG_R1v2_19nov_ADENDA_02 PREREG_R1v2_19nov_ADENDA_03 PREREG_R1v2_19nov_ADENDA_04 PREREG_R1v2_19nov_ADENDA_05 PREREG_R1v2_19nov_ADENDA_06 PREREG_R1v2_19nov_ADENDA_06b PREREG_R1v2_19nov_ADENDA_07 PREREG_R1v2_19nov_ADENDA_08 CONTRATO_R1v2_19nov_v2; do
  [ -f "${PRD}${f}.md" ] && [ -f "${PRD}${f}.sha256" ] || return 1
  [ "$(sha256sum "${PRD}${f}.md" | cut -d' ' -f1)" = "$(cut -d' ' -f1 "${PRD}${f}.sha256")" ] || return 1; done; return 0; }
# TODAS las condiciones juntas (se usan en la espera Y se re-chequean al salir del bucle: fail-closed)
cond_ok() { hm=$(hm_now); ram=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); chain=$(cut -d' ' -f1 "$CHAIN" 2>/dev/null)
  [ "$hm" -ge 1230 ] && { [ "$hm" -lt 600 ] || [ "$hm" -ge 915 ]; } && [ "$chain" = "COMPLETE" ] && [ "${ram:-0}" -ge "$RAM_MIN" ]; }
{
prereg_ok || { echo "$(ts) BLOQUEADO: PREREG/ADENDAS no cuadran con sus .sha256 (fail-closed)"; exit 3; }
echo "$(ts) run_puerta0 inicio (espera de condiciones)"
for i in $(seq 1 "$ESPERA"); do
  if cond_ok; then break; fi
  [ $((i % 20)) -eq 1 ] && echo "$(ts) espera: hhmm=$hm chain=${chain:-?} ram=${ram}MB"
  sleep 30
done
cond_ok || { echo "$(ts) BLOQUEADO: condiciones no cumplidas tras la espera (hhmm=$hm chain=${chain:-?} ram=${ram:-?}MB, min $RAM_MIN)"; exit 3; }
prereg_ok || { echo "$(ts) BLOQUEADO: PREREG/ADENDAS no cuadran (fail-closed)"; exit 3; }
PY="nice -n 19 ionice -c3 python3"; rc=0
run() { echo "$(ts) >>> $*"; ( ulimit -v 5000000; /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 /usr/bin/time -v -o "${OUT}pico_${2:-$1}.txt" python3 "${HV}puerta0_run.py" "$@" ) 2>&1 | while IFS= read -r l; do echo "$(ts) $l"; done; r=${PIPESTATUS[0]}; [ "$r" -ne 0 ] && rc=1; }
for d in 2026-11-10 2026-11-11 2026-11-12 2026-11-13 2026-11-14 2026-11-05 2026-11-06 2026-11-09 2026-11-04 2026-11-03 2026-11-07 2026-11-08; do run dia $d; done
run final
echo "$(ts) run_puerta0 fin rc=$rc"; exit $rc
} >> "$LOG" 2>&1
