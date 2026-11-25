#!/bin/bash
# run_add3.sh (16-Nov-2026; ADDENDUM3_B_F5 sha 65ccdbb4) -- SEGUNDO job de EXP-1, encadenado DESPUES de run_add2.sh (pid 1665233): F5 por clase de suelo medida en los 35 dias decisivos.
# Lanzar:  nohup bash run_add3.sh > /dev/null 2>&1 &     Log: exp1/run_add3.log   Salida: exp1/E2_clase_suelo_add3.{txt,json}   Estado: STATUS.json (E2agg_add3, ADD3_job)
# Espera a que termine el pid 1665233 (comprobacion directa de /proc/1665233/cmdline; sin pgrep -f) y a que el lock de run_add2 quede libre. Despues, con las MISMAS reglas que run_add2:
# cada fase espera en shell a >= 09:20Z (hasta 22:00Z), load1 <= 8 y MemAvailable >= 3500 MB; pasa por scripts/cron_pesado.sh (flock global, adj +500) y add2_guard.sh (sin cambios: re-chequeo,
# timeout 45 min, nice 19, ionice -c3); ulimit -v 2,2 GB. Orden: smoke 3 M lineas del 23-Oct -> 23, 22, 17, 27-Oct -> agregado intermedio -> resto cronologico -> 2a pasada OOM -> agregado final.
# OOM (rc 137): UN reintento al final tras >= 10 min; assert (rc 1) o desenlace pendiente (rc 3): sin reintento; omitida por la cola/guarda: reintento cada 5 min (max 6). Sin fases nuevas tras las 21:30Z.
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1; LOG=$H/run_add3.log; CP=/root/polymarket-research/scripts/cron_pesado.sh; G=$H/add2_guard.sh; P2=1665233
cd $H || exit 9
exec 8>$H/.run_add3.lock; flock -n 8 || { echo "$(date -u +%FT%TZ) otra instancia de run_add3 en marcha: salgo" >> $LOG; exit 0; }
echo 500 > /proc/$$/oom_score_adj 2>/dev/null
ulimit -v 2200000
export MALLOC_ARENA_MAX=2 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
export MALLOC_MMAP_THRESHOLD_=262144 MALLOC_TRIM_THRESHOLD_=262144 MALLOC_TOP_PAD_=0
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
DEADLINE=$(date -u -d "$(date -u +%F) 21:30" +%s)  # r: dinamico (la copia original fijaba 2026-11-16 21:30)
vivo2() { [ -r /proc/$P2/cmdline ] && tr '\0' ' ' < /proc/$P2/cmdline 2>/dev/null | grep -q 'run_add2[.]sh'; }
log "===== run_add3 pid $$ ADDENDUM3 $(cut -c1-8 $H/../ADDENDUM3_B_F5.sha256): espero a que termine run_add2 (pid $P2)"
while vivo2; do [ "$(date -u +%s)" -ge "$DEADLINE" ] && { log "run_add2 sigue vivo a las 21:30Z: no arranco (PARTIAL)"; exit 0; }; sleep 60; done
exec 7>$H/.run_add2.lock; flock -w 600 7 || { log "el lock de run_add2 sigue ocupado tras 10 min: no arranco"; exit 0; }
log "run_add2 terminado; su ultima linea: $(tail -1 $H/run_add2.log | cut -c1-220)"
espera() { local n=0; while :; do bash $G --check && return 0; [ "$(date -u +%s)" -ge "$DEADLINE" ] && return 1; n=$((n+1)); [ $((n % 30)) -eq 1 ] && log "espera ventana/calma: $(bash $G --estado)"; sleep 60; done; }
fase() { local n=$1; shift; log "INICIO $n $(bash $G --estado)"
  /usr/bin/time -v -o $H/time_add3_$n.txt bash $CP bash $G "$@" >> $H/out_add3_$n.txt 2>&1; local rc=$?
  log "FIN $n rc=$rc maxrss_kB=$(awk -F: '/Maximum resident/{gsub(/ /,"",$2);print $2}' $H/time_add3_$n.txt 2>/dev/null)"; return $rc; }
st_nuevo() { python3 -I -c "import json,sys; e=json.load(open('$H/STATUS.json')).get('$1',{}); sys.exit(0 if e.get('t','')>='$2' else 1)"; }
dia_ok() { grep -q '"estado": "COMPLETE"' $H/cache/${2}pob_add3_$1.json 2>/dev/null && { [ -n "$2" ] || [ -s $H/cache/${1}_pob_add3.pkl.gz ]; }; }
corre() {  # corre NOMBRE 'CHEQUEO' CMD... -> 0 si la fase termino y su salida existe
  local n=$1 chk=$2; shift 2; local i rc
  for i in 1 2 3 4 5 6; do
    espera || { log "$n: SIN VENTANA/CALMA antes de las 21:30Z"; return 76; }
    T0=$(date -u +%FT%TZ); touch $H/.add3_t0; fase "$n" "$@"; rc=$?
    [ $rc -eq 0 ] && eval "$chk" && return 0
    if [ $rc -eq 0 ] || [ $rc -eq 75 ]; then log "$n omitida (cola pesada o guarda; rc=$rc): reintento en 5 min"; sleep 300; continue; fi
    return $rc
  done; log "$n: 6 intentos omitidos"; return 77; }
cd $H/.. && sha256sum -c --status ADDENDUM1_B_F5.sha256 && sha256sum -c --status ADDENDUM3_B_F5.sha256 || { cd $H; log "ABORTO: addendum modificado tras el sellado"; exit 8; }; cd $H
{ echo "$(date -u +%FT%TZ) run_add3 arranca; sha de codigo:"; sha256sum run_add3.sh add2_guard.sh e2_dia_add3.py e2_dia_add2.py e2_agrega_add3.py popdata.py lib1.py ../lib_ev.py; } >> $H/MANIFEST_ADD3.txt
corre smoke_dia3 "[ $H/cache/smoke_pob_add3_2026-10-23.json -nt $H/.add3_t0 ] && dia_ok 2026-10-23 smoke_" python3 -I $H/e2_dia_add3.py 2026-10-23 --smoke 3000000 || { log "ABORTO: smoke de e2_dia_add3 fallo (ver out_add3_smoke_dia3.txt)"; exit 2; }
PRIO="2026-10-23 2026-10-22 2026-10-17 2026-10-27"
RESTO=$(for i in $(seq 0 36); do d=$(date -u -d "2026-10-09 +$i day" +%F); case " 2026-10-16 2026-10-24 $PRIO " in *" $d "*) ;; *) echo $d;; esac; done)
MUERTOS=""; FALLOS=""; PARAR=""
uno() { local D=$1; dia_ok $D && { log "E2add3_$D ya COMPLETE (se salta)"; return 0; }
  corre E2add3_$D "dia_ok $D" python3 -I $H/e2_dia_add3.py $D; local rc=$?
  [ $rc -eq 0 ] && return 0; [ $rc -eq 76 ] && PARAR=1; [ $rc -eq 137 ] && MUERTOS="$MUERTOS $D" || FALLOS="$FALLOS $D(rc=$rc)"; }
agrega() { corre $1 'st_nuevo E2agg_add3 $T0' python3 -I $H/e2_agrega_add3.py && { [ "$1" = e2_agrega_add3_parcial ] && cp -f $H/E2_clase_suelo_add3.txt $H/E2_clase_suelo_add3_parcial4.txt; true; } || log "$1 fallo (ver out_add3_$1.txt)"; }
for D in $PRIO; do [ -n "$PARAR" ] && break; uno $D; done
[ -z "$PARAR" ] && agrega e2_agrega_add3_parcial
for D in $RESTO; do [ -n "$PARAR" ] && break; uno $D; done
if [ -n "$MUERTOS" ] && [ -z "$PARAR" ]; then log "dias matados por OOM:$MUERTOS -> UNA segunda pasada tras >= 10 min y calma"; sleep 600
  for D in $MUERTOS; do corre E2add3_${D}_r2 "dia_ok $D" python3 -I $H/e2_dia_add3.py $D || FALLOS="$FALLOS $D(OOM x2)"; done; fi
log "dias ADD3: FALLOS=[$FALLOS ] PARADO_POR_HORA=[${PARAR:-no}]"
[ -z "$PARAR" ] && agrega e2_agrega_add3
{ echo "$(date -u +%FT%TZ) run_add3 FIN; sha de salidas:"; sha256sum E2_clase_suelo_add3.txt E2_clase_suelo_add3.json STATUS.json 2>&1; } >> $H/MANIFEST_ADD3.txt
python3 -I -c "
import json,time,os; p='$H/STATUS.json'; S=json.load(open(p)); S['ADD3_job']=dict(estado='FIN', t=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), fallos_dias='$FALLOS'.split(), parado_por_hora=bool('$PARAR'), addendum3='$(cut -c1-8 $H/../ADDENDUM3_B_F5.sha256)', E2agg_add3=S.get('E2agg_add3', {}).get('estado'))
json.dump(S, open(p + '.tmp', 'w'), indent=1); os.replace(p + '.tmp', p)"
log "===== FIN run_add3 FALLOS=[$FALLOS ] E2agg_add3=$(python3 -I -c "import json; print(json.load(open('$H/STATUS.json')).get('E2agg_add3', {}).get('estado'))")"
