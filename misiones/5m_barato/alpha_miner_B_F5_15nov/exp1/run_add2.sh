#!/bin/bash
# run_add2.sh (16-Nov-2026; ADDENDUM2_B_F5 sha 28c39f45) -- EXP-1: cierra E2agg/E5/E6 sin tocar lo COMPLETE (E1, E3, E3x, E7 y los 35 dias ADD1 no se rehacen).
# Lanzar:  nohup bash run_add2.sh > /dev/null 2>&1 &      Log: exp1/run_add2.log   Estado: exp1/STATUS.json (claves *_add2 y ADD2_job)
# Orden: espera ventana+calma -> smoke agregado (2 dias ADD1, B=20) -> smoke e2_dia_add2 (3 M lineas del 24-Oct) -> 16-Oct y 24-Oct con ADD2 -> e2_agrega_add2 -> e5_regimen_add2 -> e6_brecha_add2 -> manifiesto.
# Cada fase: espera en shell a >= 09:20Z (hasta 22:00Z), load1 <= 8 y MemAvailable >= 3500 MB; pasa por scripts/cron_pesado.sh (flock global, oom_score_adj +500) y add2_guard.sh (re-chequeo, timeout 45 min, nice 19, ionice -c3);
# ulimit -v 2,2 GB; asignador glibc como run_exp1 v4. Un OOM (rc 137) se reintenta UNA vez al final tras >= 10 min y calma; un assert (rc 1) o desenlace pendiente (rc 3) no se reintentan;
# una fase omitida por la cola o por la guarda (rc 0 sin salida o rc 75) se reintenta tras 5 min, maximo 6 veces. Si no hay ventana+calma antes de las 21:30Z se rinde y lo deja escrito. Sin red, sin ordenes.
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1; LOG=$H/run_add2.log; CP=/root/polymarket-research/scripts/cron_pesado.sh; G=$H/add2_guard.sh
cd $H || exit 9
exec 8>$H/.run_add2.lock; flock -n 8 || { echo "$(date -u +%FT%TZ) otra instancia de run_add2 en marcha: salgo" >> $LOG; exit 0; }
echo 500 > /proc/$$/oom_score_adj 2>/dev/null
ulimit -v 2200000
export MALLOC_ARENA_MAX=2 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
export MALLOC_MMAP_THRESHOLD_=262144 MALLOC_TRIM_THRESHOLD_=262144 MALLOC_TOP_PAD_=0
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
DEADLINE=$(date -u -d '2026-11-16 21:30' +%s)
espera() { local n=0; while :; do bash $G --check && return 0; [ "$(date -u +%s)" -ge "$DEADLINE" ] && return 1; n=$((n+1)); [ $((n % 30)) -eq 1 ] && log "espera ventana/calma: $(bash $G --estado)"; sleep 60; done; }
fase() { local n=$1; shift; log "INICIO $n $(bash $G --estado)"
  /usr/bin/time -v -o $H/time_add2_$n.txt bash $CP bash $G "$@" >> $H/out_add2_$n.txt 2>&1; local rc=$?
  log "FIN $n rc=$rc maxrss_kB=$(awk -F: '/Maximum resident/{gsub(/ /,"",$2);print $2}' $H/time_add2_$n.txt 2>/dev/null)"; return $rc; }
st_nuevo() { python3 -I -c "import json,sys; e=json.load(open('$H/STATUS.json')).get('$1',{}); sys.exit(0 if e.get('t','')>='$2' else 1)"; }
dia_ok() { grep -q '"estado": "COMPLETE"' $H/cache/${2}pob_add2_$1.json 2>/dev/null && { [ -n "$2" ] || [ -s $H/cache/${1}_pob_add2.pkl.gz ]; }; }
corre() {  # corre NOMBRE 'CHEQUEO' CMD... -> 0 si la fase termino y su salida existe; otro rc si fallo
  local n=$1 chk=$2; shift 2; local i rc
  for i in 1 2 3 4 5 6; do
    espera || { log "$n: SIN VENTANA/CALMA antes de las 21:30Z"; return 76; }
    T0=$(date -u +%FT%TZ); touch $H/.add2_t0; fase "$n" "$@"; rc=$?
    [ $rc -eq 0 ] && eval "$chk" && return 0
    if [ $rc -eq 0 ] || [ $rc -eq 75 ]; then log "$n omitida (cola pesada o guarda; rc=$rc): reintento en 5 min"; sleep 300; continue; fi
    return $rc
  done; log "$n: 6 intentos omitidos"; return 77; }
log "===== run_add2 pid $$ ADDENDUM2 $(cut -c1-8 $H/../ADDENDUM2_B_F5.sha256) $(bash $G --estado)"
cd $H/.. && sha256sum -c --status ADDENDUM1_B_F5.sha256 && sha256sum -c --status ADDENDUM2_B_F5.sha256 || { cd $H; log "ABORTO: addendum modificado tras el sellado"; exit 8; }; cd $H
{ echo "$(date -u +%FT%TZ) run_add2 arranca; sha de codigo:"; sha256sum run_add2.sh add2_guard.sh e2_dia_add2.py popdata_add2.py e2_agrega_add2.py e5_regimen_add2.py e6_brecha_add2.py e2_dia.py e5_regimen.py e6_brecha.py popdata.py lib1.py ../lib_ev.py; } >> $H/MANIFEST_ADD2.txt
# ---- smokes (segundos): si fallan, nada pesado arranca
corre smoke_agrega "[ $H/smoke_E2_poblacion_add2.txt -nt $H/.add2_t0 ] && grep -q 'RESUMEN' $H/smoke_E2_poblacion_add2.txt" python3 -I $H/e2_agrega_add2.py --smoke 2026-10-25,2026-10-28 || { log "ABORTO: smoke de e2_agrega_add2 fallo (ver out_add2_smoke_agrega.txt)"; exit 2; }
corre smoke_dia "[ $H/cache/smoke_pob_add2_2026-10-24.json -nt $H/.add2_t0 ] && dia_ok 2026-10-24 smoke_" python3 -I $H/e2_dia_add2.py 2026-10-24 --smoke 3000000 || { log "ABORTO: smoke de e2_dia_add2 fallo (ver out_add2_smoke_dia.txt y cache/smoke_pob_add2_2026-10-24.json)"; exit 2; }
# ---- dias ADD2
MUERTOS=""; FALLOS=""
for D in 2026-10-16 2026-10-24; do
  if dia_ok $D; then log "E2add2_$D ya COMPLETE (se salta)"; continue; fi
  corre E2add2_$D "dia_ok $D" python3 -I $H/e2_dia_add2.py $D; rc=$?
  [ $rc -eq 0 ] && continue; [ $rc -eq 137 ] && MUERTOS="$MUERTOS $D" || FALLOS="$FALLOS $D(rc=$rc)"
done
if [ -n "$MUERTOS" ]; then log "dias matados por OOM:$MUERTOS -> UNA segunda pasada tras >= 10 min de pausa y calma"; sleep 600
  for D in $MUERTOS; do corre E2add2_${D}_r2 "dia_ok $D" python3 -I $H/e2_dia_add2.py $D || FALLOS="$FALLOS $D(OOM x2)"; done; fi
log "dias ADD2: FALLOS=[$FALLOS ]"
# ---- agregados (solo lectura de caches)
RC_AG=1; corre e2_agrega_add2 'st_nuevo E2agg_add2 $T0' python3 -I $H/e2_agrega_add2.py; RC_AG=$?
if [ $RC_AG -eq 137 ]; then log "e2_agrega_add2 OOM: reintento unico tras 10 min"; sleep 600; corre e2_agrega_add2_r2 'st_nuevo E2agg_add2 $T0' python3 -I $H/e2_agrega_add2.py; RC_AG=$?; fi
if [ $RC_AG -eq 0 ]; then
  corre e5_regimen_add2 'st_nuevo E5_add2 $T0' python3 -I $H/e5_regimen_add2.py || log "e5_regimen_add2 fallo"
  corre e6_brecha_add2 'st_nuevo E6_add2 $T0' python3 -I $H/e6_brecha_add2.py || log "e6_brecha_add2 fallo"
else log "e2_agrega_add2 fallo (rc=$RC_AG; si es la regresion C10, ver out_add2_e2_agrega_add2.txt): E5/E6 _add2 NO se lanzan"; fi
{ echo "$(date -u +%FT%TZ) run_add2 FIN; sha de salidas:"; sha256sum E2_poblacion_add2.txt E2_poblacion_add2.json E5_regimen_add2.txt E5_regimen_add2.json E6_brecha_add2.txt E6_brecha_add2.json cache/pob_add2_2026-10-16.json cache/pob_add2_2026-10-24.json STATUS.json 2>&1; } >> $H/MANIFEST_ADD2.txt
python3 -I -c "
import json,time; p='$H/STATUS.json'; S=json.load(open(p)); S['ADD2_job']=dict(estado='FIN', t=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), fallos_dias='$FALLOS'.split(), rc_e2_agrega=$RC_AG, addendum2='$(cut -c1-8 $H/../ADDENDUM2_B_F5.sha256)', estados={k: S.get(k, {}).get('estado') for k in ('E2agg_add2', 'E5_add2', 'E6_add2')})
json.dump(S, open(p + '.tmp', 'w'), indent=1); import os; os.replace(p + '.tmp', p)"
log "===== FIN run_add2 FALLOS=[$FALLOS ] rc_e2_agrega=$RC_AG estados: $(python3 -I -c "import json; S=json.load(open('$H/STATUS.json')); print({k: S.get(k, {}).get('estado') for k in ('E2agg_add2', 'E5_add2', 'E6_add2')})")"
