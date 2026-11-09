#!/bin/bash
# traspaso_bnreg_once.sh -- TRASPASO UNICO del registro Binance del hijo de `observadores` al proceso `bnreg` (FASE 1, DISENO_CAPTURA_INDEPENDIENTE_L2_09nov.md sec. 2).
# ESTADO: ESCRITO, NO EJECUTADO. Requiere OK de Javi (proceso nuevo permanente + un reinicio de observadores = se pierde el historico ms en memoria UNA vez) y /code-review medium previo.
# Uso (se despliega como scripts/traspaso_bnreg_once.sh):
#   bash scripts/traspaso_bnreg_once.sh                              -> SOLO plan: imprime las comprobaciones previas, no cambia nada
#   bash scripts/traspaso_bnreg_once.sh --ejecutar [--ok-horario-usa]
# No se lanza con `bash -c` ni heredoc ni por pgrep/pkill -f (trampa 14-Oct); el script no lleva en su linea de comandos el nombre de los .py.
#
# ORDEN (sin carrera: el hijo NUEVO de observadores nace cuando bnreg ya es el dueno del lock; cada paso falla en voz alta y revierte):
#   P0 comprobaciones previas: fuera de 06:00-09:15Z; fuera de horario USA 13:30-21:00Z salvo --ok-horario-usa; ficheros en main (bnreg, watchdog/verify_deploy con bnreg); screen bnreg viva y OCIOSA
#      (centinela ausente, latido fresco), con oom_score_adj = -200 aplicado (latido `oom_adj`, y /proc/<pid>/oom_score_adj); STAGING con el libro_estado_ws nuevo.
#   P1 flock /tmp/restart_ram_fase0.lock (bloquea restart_ram y guard_ram durante el traspaso).
#   P2 esperar un tick del watchdog (+10 s): quedan ~100 s hasta el siguiente, para que no relance observadores a mitad.
#   P3 backup del libro_estado_ws.py de main y cp del nuevo (observadores pasa a STALE; el watchdog no actua antes de su siguiente tick).
#   P4 PARAR observadores (screen quit por PID) y esperar a que no quede ningun hijo libro_estado_ws (TERM si hace falta).
#   P5 crear el centinela y ESPERAR (<=20 s) a que bnreg sea el DUENO del lock: latido estado=activo con lock=true, el fichero de lock dice "bnreg pid=<pid de bnreg vivo>" y un flock no bloqueante
#      desde aqui FALLA (alguien lo tiene). Si no ocurre en 20 s: ABORTO con RESTAURACION (borrar centinela, restaurar libro_estado_ws.py viejo, arrancar observadores).
#   P6 arrancar observadores con el codigo nuevo (verify_deploy --restart observadores): su hijo ve el lock tomado y nace en RESERVA. Si el watchdog ya lo habia relanzado, se deja.
#   P7 comprobaciones: bnreg sigue siendo el dueno; el hijo nuevo dice RESERVA en su log; x/b nuevos solo en el fichero de bnreg; marcas en binance_huecos.
# HUECO Binance esperado: entre la muerte del hijo viejo (P4) y la 1a conexion de bnreg (P5): ~2-5 s UNA vez [NO medido en produccion; en dev: relevo hijo<->bnreg 3-4 s]. Hoy: 46-148 s por evento.
#
# MARCHA ATRAS (con el ESTADO REAL que deja el traspaso: bnreg escribe, el hijo nuevo vive en reserva):
#   A) bnreg -> hijo (un solo escritor = el hijo nuevo):  rm $DL/BNREG_HABILITADO ; bnreg cierra, suelta el lock y queda ocioso; el hijo asume en <=5 s y deja la marca `hijo_asume`.
#      Volver a bnreg:  touch $DL/BNREG_HABILITADO ; bnreg anuncia espera_lock; el hijo CEDE el lock tras >=30 s de histeresis (una vez por episodio), bnreg lo toma en ~1-2 s (marca `hijo_cede`).
#   B) Volver al codigo ANTERIOR sin reserva (hijo viejo escribe solo):  rm $DL/BNREG_HABILITADO ; cp $DL/traspaso_bnreg/libro_estado_ws.py.pre $REPO/libro_estado_ws.py ;
#      $REPO/.venv/bin/python $REPO/verify_deploy.py --restart observadores  (el hijo viejo no mira el lock: bnreg ya esta ocioso sin centinela, no hay doble escritor).
#   Si el hijo no vive en reserva en el momento de A: $PY verify_deploy.py --restart observadores.
set -u
REPO=${REPO:-/root/polymarket-research}
DL=${DL:-/root/polymarket-research-datalogs}
STAGING=${STAGING:-$REPO/experimentos/5m_barato/bnreg/dev_main}
PY=${PY:-$REPO/.venv/bin/python}
OOM_ESPERADO=-200
EJECUTAR=0; OK_USA=0
for a in "$@"; do case "$a" in --ejecutar) EJECUTAR=1;; --ok-horario-usa) OK_USA=1;; *) echo "argumento desconocido: $a"; exit 2;; esac; done
mkdir -p "$DL/traspaso_bnreg"
LOGF="$DL/traspaso_bnreg/traspaso_$(date -u +%Y%m%dT%H%M%SZ).log"
log() { echo "[$(date -u +%FT%TZ)] $*" | tee -a "$LOGF"; }
# latido de bnreg: $1 = estado esperado, $2 = antiguedad maxima en s; "activo" exige ademas lock=true
bn_estado_ok() { "$PY" -c 'import json,time,sys;e=json.load(open(sys.argv[1]));esp=sys.argv[2];ok=e["estado"]==esp and (esp!="activo" or e["lock"]) and time.time()-e["ts"]/1000<float(sys.argv[3]);sys.exit(0 if ok else 1)' "$DL/binance_registro_estado.json" "$1" "$2" 2>/dev/null; }
# pid de bnreg segun su latido (vacio si no hay)
bn_pid() { "$PY" -c 'import json,sys;print(json.load(open(sys.argv[1]))["pid"])' "$DL/binance_registro_estado.json" 2>/dev/null; }
# bnreg es el DUENO del lock: el fichero dice bnreg pid=<vivo> y NADIE nos deja tomarlo (flock NB falla)
bn_es_duenyo() {
  local pid; pid=$(bn_pid); [ -n "$pid" ] || return 1
  kill -0 "$pid" 2>/dev/null || return 1
  grep -q "^bnreg pid=$pid\$" "$DL/.binance_registro.lock" 2>/dev/null || return 1
  ! flock -n "$DL/.binance_registro.lock" -c true 2>/dev/null
}
oom_de_bnreg() { local pid; pid=$(bn_pid); [ -n "$pid" ] && cat "/proc/$pid/oom_score_adj" 2>/dev/null; }
restaurar() {   # tras un aborto: sin centinela, codigo viejo, observadores arriba
  log "RESTAURANDO: rm centinela; restaurar libro_estado_ws.py previo; arrancar observadores"
  rm -f "$DL/BNREG_HABILITADO"
  [ -f "$DL/traspaso_bnreg/libro_estado_ws.py.pre" ] && cp "$DL/traspaso_bnreg/libro_estado_ws.py.pre" "$REPO/libro_estado_ws.py"
  (cd "$REPO" && "$PY" verify_deploy.py --restart observadores) 2>&1 | tee -a "$LOGF"
}
die() { log "ABORTO: $*"; restaurar; log "estado final: centinela=$([ -e "$DL/BNREG_HABILITADO" ] && echo presente || echo ausente)"; exit 1; }
hora_min=$(( 10#$(date -u +%H) * 60 + 10#$(date -u +%M) ))
fallos=0
chk() { if eval "$2"; then log "OK    $1"; else log "FALLA $1"; fallos=$((fallos+1)); fi; }
log "== P0 comprobaciones previas (ejecutar=$EJECUTAR) =="
chk "fuera de 06:00-09:15Z" '[ $hora_min -lt 360 ] || [ $hora_min -ge 555 ]'
chk "fuera de horario USA 13:30-21:00Z (o --ok-horario-usa)" '[ $OK_USA -eq 1 ] || [ $hora_min -lt 810 ] || [ $hora_min -ge 1260 ]'
chk "STAGING tiene libro_estado_ws.py nuevo (con reserva bnreg y cesion)" 'grep -q "BNREG_LOCK" "$STAGING/libro_estado_ws.py" && grep -q "hijo_cede" "$STAGING/libro_estado_ws.py"'
chk "binance_registro_ms.py presente en main" '[ -f "$REPO/binance_registro_ms.py" ]'
chk "SCREEN_RESTART tiene bnreg con choom -n $OOM_ESPERADO" 'grep -q "\"bnreg\":.*choom -n $OOM_ESPERADO -- " "$REPO/pipeline_watchdog.py"'
chk "verify_deploy.SCREENS tiene bnreg" 'grep -q "\"bnreg\":" "$REPO/verify_deploy.py"'
chk "screen bnreg viva" 'screen -ls | grep -qE "[0-9]+\.bnreg[[:space:]]"'
chk "centinela AUSENTE (bnreg ocioso)" '[ ! -e "$DL/BNREG_HABILITADO" ]'
chk "estado de bnreg = ocioso y fresco (<30 s)" 'bn_estado_ok ocioso 30'
chk "oom_score_adj de bnreg = $OOM_ESPERADO (/proc)" '[ "$(oom_de_bnreg)" = "$OOM_ESPERADO" ]'
chk "libro_estado_ws nuevo compila" '"$PY" -m py_compile "$STAGING/libro_estado_ws.py"'
log "CONFIRMAR A MANO (no comprobable aqui): el watchdog fue reiniciado DESPUES de registrar bnreg en su SCREEN_RESTART/check_screens"
if [ $EJECUTAR -ne 1 ]; then log "Modo plan: no se hace ningun cambio. fallos previos=$fallos"; exit $((fallos>0)); fi
[ $fallos -eq 0 ] || { log "ABORTO: comprobaciones previas fallidas ($fallos); nada modificado"; exit 1; }
log "== P1 flock del cron restart_ram / guard_ram =="
exec 9>/tmp/restart_ram_fase0.lock
flock -w 60 9 || { log "ABORTO: no se pudo tomar /tmp/restart_ram_fase0.lock en 60 s; nada modificado"; exit 1; }
log "== P2 esperar un tick del watchdog =="
ult=$(tail -n1 "$REPO/logs/watchdog.log" | cut -c1-22)
act=$ult
for i in $(seq 1 135); do
  act=$(tail -n1 "$REPO/logs/watchdog.log" | cut -c1-22)
  [ "$act" != "$ult" ] && break
  sleep 1
done
[ "$act" != "$ult" ] || { log "ABORTO: el watchdog no escribio ningun tick en 135 s; nada modificado"; exit 1; }
sleep 10
log "tick detectado ($act); +10 s"
log "== P3 backup + cp del libro_estado_ws nuevo =="
cp "$REPO/libro_estado_ws.py" "$DL/traspaso_bnreg/libro_estado_ws.py.pre" || { log "ABORTO: backup fallido; nada modificado"; exit 1; }
cp "$STAGING/libro_estado_ws.py" "$REPO/libro_estado_ws.py" || die "cp fallido"
log "== P4 parar observadores por PID =="
for pid in $(screen -ls | grep -oE "[0-9]+\.observadores[[:space:]]" | cut -d. -f1); do screen -S "$pid.observadores" -X quit; log "quit $pid.observadores"; done
sleep 1
for i in 1 2 3 4 5; do
  hijos=$(ps -eo pid,args | awk '/[l]ibro_estado_ws.py --hijo/ {print $1}')
  [ -z "$hijos" ] && break
  sleep 1
done
if [ -n "${hijos:-}" ]; then log "el hijo viejo sigue vivo tras 5 s ($hijos): TERM"; kill $hijos; sleep 2; hijos=$(ps -eo pid,args | awk '/[l]ibro_estado_ws.py --hijo/ {print $1}'); [ -z "$hijos" ] || die "hijo viejo no muere ($hijos)"; fi
log "observadores parado y sin hijo"
log "== P5 habilitar bnreg y esperar a que sea el DUENO del lock (<=20 s) =="
touch "$DL/BNREG_HABILITADO"; t5=$(date +%s)
duenyo=0
for i in $(seq 1 20); do
  if bn_estado_ok activo 15 && bn_es_duenyo; then duenyo=1; log "bnreg activo y dueno del lock tras $(( $(date +%s) - t5 )) s (pid $(bn_pid), oom_score_adj $(oom_de_bnreg))"; break; fi
  sleep 1
done
[ $duenyo -eq 1 ] || die "bnreg no es el dueno del lock en 20 s"
[ "$(oom_de_bnreg)" = "$OOM_ESPERADO" ] || log "AVISO: oom_score_adj de bnreg = $(oom_de_bnreg), esperado $OOM_ESPERADO"
log "== P6 arrancar observadores con el codigo nuevo =="
if screen -ls | grep -qE "[0-9]+\.observadores[[:space:]]"; then log "el watchdog ya relanzo observadores (codigo nuevo en disco): se deja"; else
  (cd "$REPO" && "$PY" verify_deploy.py --restart observadores) 2>&1 | tee -a "$LOGF"; fi
log "== P7 comprobaciones =="
sleep 25
dia=$(date -u +%F)
bn_es_duenyo && log "OK    bnreg sigue siendo el dueno del lock" || log "FALLA bnreg ya NO es el dueno (mirar binance_huecos: hijo_asume)"
ls -l "$DL"/maker_ms_${dia}_*.csv.gz 2>&1 | tee -a "$LOGF"
log "huecos (ultimas marcas):"; tail -n 6 "$DL/binance_huecos_${dia}.csv" 2>&1 | tee -a "$LOGF"
log "hijo nuevo (lineas RESERVA/ASUME):"; grep -h "RESERVA\|ASUME" "$REPO"/logs/observadores*.log 2>/dev/null | tail -n 3 | tee -a "$LOGF"
log "FIN. Revisar: x/b solo en el fichero de bnreg; binance_integridad sin faltantes salvo la marca del traspaso. Log: $LOGF"
