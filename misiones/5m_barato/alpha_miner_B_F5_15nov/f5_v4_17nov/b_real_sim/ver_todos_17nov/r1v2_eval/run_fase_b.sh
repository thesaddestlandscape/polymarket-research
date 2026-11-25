#!/bin/bash
# run_fase_b.sh -- R1v2 FASE B (V1-V6 dentro del replay; DIAGNOSTICO, no confirmatorio). Mismas guardas que run_puerta0.sh (condiciones re-chequeadas, sha de PREREG+ADENDA_01..07, flock, PID tras flock; las variables de prueba conservan el prefijo P0_) + FB_T_PROC_MS obligatorio. NO LANZAR sin OK del chief. Idempotente (fase_b_run.py salta lo COMPLETE y valida el sha de los outputs). Uno a la vez (flock), cron_pesado, nice 19, ionice -c3, ulimit -v 3 GB (ADENDA_06).
# Arranca solo si: hora UTC >= 12:30 y fuera de 06:00-09:15Z, la cadena de la pista cola ha acabado (chain.status = COMPLETE; solo se LEE) y RAM libre >= 5 GB. Espera hasta 10 h; si no, termina con codigo 3 (BLOQUEADO, nada hecho).
# Parada: por PID guardado (out_fb/run.pid) con kill; el script se lanza por su ruta.
HV="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)/"; V="$(dirname "${HV%/}")/"
CHAIN="${P0_CHAIN:-${V}pista_cola_18nov/out/verif_adenda11/chain.status}"      # P0_CHAIN/P0_HM/P0_RAM_MIN/P0_ESPERA/P0_PREREG_DIR: solo para tests de las puertas
RAM_MIN="${P0_RAM_MIN:-5000}"; ESPERA="${P0_ESPERA:-1200}"; PRD="${P0_PREREG_DIR:-$V}"
OUT="${FB_OUT:-${HV}out_fb/}"; mkdir -p "$OUT"; LOG="${OUT}run_$(date -u +%Y%m%dT%H%M%SZ).log"
exec 8>"${OUT}.lock"; flock -n 8 || { echo "otro run_fase_b en curso"; exit 2; }
echo $$ > "${OUT}run.pid"      # solo tras tomar el flock: nunca se pisa el PID del run en curso
ts() { date -u +%FT%TZ; }
[ -n "$FB_T_PROC_MS" ] || { echo "FB_T_PROC_MS obligatorio (t_proc medido, ms); sin default"; exit 3; }; export FB_T_PROC_MS
hm_now() { if [ -n "$P0_HM" ]; then echo $((10#$P0_HM)); else h=$(date -u +%H%M); echo $((10#$h)); fi; }
prereg_ok() { local f; for f in PREREG_R1v2_19nov PREREG_R1v2_19nov_ADENDA_01 PREREG_R1v2_19nov_ADENDA_02 PREREG_R1v2_19nov_ADENDA_03 PREREG_R1v2_19nov_ADENDA_04 PREREG_R1v2_19nov_ADENDA_05 PREREG_R1v2_19nov_ADENDA_06 PREREG_R1v2_19nov_ADENDA_07 CONTRATO_R1v2_19nov_v2; do
  [ -f "${PRD}${f}.md" ] && [ -f "${PRD}${f}.sha256" ] || return 1
  [ "$(sha256sum "${PRD}${f}.md" | cut -d' ' -f1)" = "$(cut -d' ' -f1 "${PRD}${f}.sha256")" ] || return 1; done; return 0; }
# TODAS las condiciones juntas (se usan en la espera Y se re-chequean al salir del bucle: fail-closed)
cond_ok() { hm=$(hm_now); ram=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); chain=$(cut -d' ' -f1 "$CHAIN" 2>/dev/null)
  [ "$hm" -ge 1230 ] && { [ "$hm" -lt 600 ] || [ "$hm" -ge 915 ]; } && [ "$chain" = "COMPLETE" ] && [ "${ram:-0}" -ge "$RAM_MIN" ]; }
{
prereg_ok || { echo "$(ts) BLOQUEADO: PREREG/ADENDAS no cuadran con sus .sha256 (fail-closed)"; exit 3; }
echo "$(ts) run_fase_b inicio (espera de condiciones)"
for i in $(seq 1 "$ESPERA"); do
  if cond_ok; then break; fi
  [ $((i % 20)) -eq 1 ] && echo "$(ts) espera: hhmm=$hm chain=${chain:-?} ram=${ram}MB"
  sleep 30
done
cond_ok || { echo "$(ts) BLOQUEADO: condiciones no cumplidas tras la espera (hhmm=$hm chain=${chain:-?} ram=${ram:-?}MB, min $RAM_MIN)"; exit 3; }
prereg_ok || { echo "$(ts) BLOQUEADO: PREREG/ADENDAS no cuadran (fail-closed)"; exit 3; }
PY="nice -n 19 ionice -c3 python3"; rc=0
ventana_ok() { hm=$(hm_now); [ "$hm" -lt 600 ] || [ "$hm" -ge 915 ]; }      # fuera de 06:00-09:15Z
run() { for i in $(seq 1 "$ESPERA"); do ventana_ok && break; sleep 30; done      # re-chequeo ANTES de cada paso pesado (la cadena dura horas)
  ventana_ok || { echo "$(ts) BLOQUEADO: dentro de 06:00-09:15Z antes de $*"; echo "$(ts) run_fase_b fin rc=3"; exit 3; }
  echo "$(ts) >>> $*"; ( ulimit -v 3000000; /root/polymarket-research/scripts/cron_pesado.sh $PY "${HV}fase_b_run.py" "$@" ) 2>&1 | while IFS= read -r l; do echo "$(ts) $l"; done; r=${PIPESTATUS[0]}; [ "$r" -ne 0 ] && rc=1; return "$r"; }
aborta() { echo "$(ts) ABORTO: fallo en $* (rc!=0): no se sigue (los pasos siguientes dependen de este)"; echo "$(ts) run_fase_b fin rc=1"; exit 1; }
TRAIN_DIAS="2026-10-26 2026-10-27 2026-10-28 2026-11-03 2026-11-04 2026-11-05 2026-11-06"; EVAL_DIAS="${FB_DIAS_EVAL:-2026-11-08,2026-11-09}"
for d in $TRAIN_DIAS ${EVAL_DIAS//,/ }; do run l2 $d || aborta "l2 $d"; done       # paso previo: eventos L2 + MAPA DE HUECOS por (dia, token)
for d in $TRAIN_DIAS; do run base $d || aborta "base $d"; done
run entrena || aborta entrena
for d in ${EVAL_DIAS//,/ }; do run variantes $d || aborta "variantes $d"; done
run final
echo "$(ts) run_fase_b fin rc=$rc"; exit $rc
} >> "$LOG" 2>&1
