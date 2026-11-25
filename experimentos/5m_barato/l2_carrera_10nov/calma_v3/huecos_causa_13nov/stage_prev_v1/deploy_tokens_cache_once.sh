#!/bin/bash
# deploy_tokens_cache_once.sh -- despliegue UNICO de la cache de tokens de libro_estado_ws.py (HC/stage), derivado de
# experimentos/5m_barato/bnreg/traspaso_bnreg_once.sh. ESTADO: ESCRITO, NO EJECUTADO. Por defecto DRY-RUN (solo lecturas + imprime acciones).
# Uso:  bash deploy_tokens_cache_once.sh                      -> dry-run (comprobaciones P0 reales, acciones solo impresas)
#       bash deploy_tokens_cache_once.sh --hora HH:MM         -> dry-run simulando esa hora UTC (solo sin --ejecutar)
#       bash deploy_tokens_cache_once.sh --ejecutar           -> despliega
# No se lanza con bash -c ni heredoc ni pgrep/pkill -f; la linea de comandos no contiene los nombres de los .py.
# Que hace: (P0) guardas -> (P1) flock restart_ram -> (P2) espera tick del watchdog -> guarda de base otra vez -> (P3) backup .pre + cp
#   -> (P4) verify_deploy --restart observadores -> (P5) comprobaciones posteriores; si algo falla: marcha atras automatica (.pre + reinicio).
# Binance NO tiene hueco: bnreg (dueno del lock) sigue escribiendo; el hijo nuevo nace en RESERVA. Perdida esperada: ~1 min de libro5 del
# Polymarket (filas G arranque) y el historico ms en memoria de observadores.
set -u
REPO=${REPO:-/root/polymarket-research}
DL=${DL:-/root/polymarket-research-datalogs}
STAGE=${STAGE:-$REPO/experimentos/5m_barato/l2_carrera_10nov/calma_v3/huecos_causa_13nov/stage}
PY=${PY:-$REPO/.venv/bin/python}
MAIN=$REPO/libro_estado_ws.py
LIBRO5=${LIBRO5:-/mnt/HC_Volume_106538179/libro5_ms}
LOGOBS=$REPO/logs/observadores_fase0.log
EJECUTAR=0; HORA_SIM=""
while [ $# -gt 0 ]; do case "$1" in
  --ejecutar) EJECUTAR=1;; --hora) shift; HORA_SIM=${1:-};; *) echo "argumento desconocido: $1"; exit 2;; esac; shift; done
[ $EJECUTAR -eq 1 ] && [ -n "$HORA_SIM" ] && { echo "--hora solo en dry-run"; exit 2; }
mkdir -p "$DL/traspaso_tokens"
LOGF="$DL/traspaso_tokens/deploy_$(date -u +%Y%m%dT%H%M%SZ).log"
log() { echo "[$(date -u +%FT%TZ)] $*" | tee -a "$LOGF"; }
act() { if [ $EJECUTAR -eq 1 ]; then log "ACCION: $*"; return 0; else log "[DRY] haria: $*"; return 1; fi; }

# ---- helpers bnreg (copiados de traspaso_bnreg_once.sh) ----
bn_pid() { "$PY" -c 'import json,sys;print(json.load(open(sys.argv[1]))["pid"])' "$DL/binance_registro_estado.json" 2>/dev/null; }
bn_estado_ok() { "$PY" -c 'import json,time,sys;e=json.load(open(sys.argv[1]));esp=sys.argv[2];ok=e["estado"]==esp and (esp!="activo" or e["lock"]) and time.time()-e["ts"]/1000<float(sys.argv[3]);sys.exit(0 if ok else 1)' "$DL/binance_registro_estado.json" "$1" "$2" 2>/dev/null; }
bn_es_duenyo() {
  local pid; pid=$(bn_pid); [ -n "$pid" ] || return 1
  kill -0 "$pid" 2>/dev/null || return 1
  grep -q "^bnreg pid=$pid\$" "$DL/.binance_registro.lock" 2>/dev/null || return 1
  ! flock -n "$DL/.binance_registro.lock" -c true 2>/dev/null
}
# ---- guarda de base: main == base registrada Y main+diff == stage ----
sha() { sha256sum "$1" | cut -d' ' -f1; }
base_ok() {
  [ "$(sha "$MAIN")" = "$(tr -d ' \n' < "$STAGE/BASE_main.sha256")" ] || { log "base: sha256 de main ($(sha "$MAIN")) != base registrada"; return 1; }
  local tmp="$DL/traspaso_tokens/main_mas_diff.py"
  patch -s -o "$tmp" "$MAIN" "$STAGE/libro_estado_ws.tokens_cache.diff" >/dev/null 2>&1 || { log "base: el diff no aplica sobre main"; return 1; }
  [ "$(sha "$tmp")" = "$(sha "$STAGE/libro_estado_ws.py")" ] || { log "base: main+diff != stage (stage lleva algo mas que el diff)"; return 1; }
  return 0
}
hora_min() { if [ -n "$HORA_SIM" ]; then echo $(( 10#${HORA_SIM%:*} * 60 + 10#${HORA_SIM#*:} )); else echo $(( 10#$(date -u +%H) * 60 + 10#$(date -u +%M) )); fi; }
hm=$(hora_min)
fallos=0
chk() { if eval "$2"; then log "OK    $1"; else log "FALLA $1"; fallos=$((fallos+1)); fi; }
hueco4h() {  # True si cae en xx:40..xx+1:05 de xx en {03,07,11,15,19,23}: hueco de captura de gamma
  local h; for h in 3 7 11 15 19 23; do
    local a=$(( h * 60 + 40 )) b=$(( (h + 1) * 60 + 5 )); [ $hm -ge $a ] && [ $hm -lt $b ] && return 0
    [ $b -gt 1440 ] && [ $hm -lt $(( b - 1440 )) ] && return 0
  done; return 1; }
log "== P0 comprobaciones (ejecutar=$EJECUTAR hora_utc=$(printf '%02d:%02d' $((hm/60)) $((hm%60)))${HORA_SIM:+ SIMULADA}) =="
chk "fuera de 06:00-09:15Z"                         '[ $hm -lt 360 ] || [ $hm -ge 555 ]'
chk "fuera de 13:30-21:00Z (horario USA)"           '[ $hm -lt 810 ] || [ $hm -ge 1260 ]'
chk "fuera de los huecos de 4 h (xx:40-xx+1:05, xx=03,07,11,15,19,23; incl. 19:40-20:05 y 23:40-00:05)" '! hueco4h'
chk "bnreg activo y DUENO del lock de Binance"      'bn_estado_ok activo 15 && bn_es_duenyo'
chk "centinela BNREG_HABILITADO presente"           '[ -e "$DL/BNREG_HABILITADO" ]'
chk "stage compila"                                 '"$PY" -m py_compile "$STAGE/libro_estado_ws.py"'
chk "stage contiene la cache y conserva reserva/cesion bnreg" 'grep -q "_MKT" "$STAGE/libro_estado_ws.py" && grep -q "BNREG_LOCK" "$STAGE/libro_estado_ws.py" && grep -q "hijo_cede" "$STAGE/libro_estado_ws.py"'
chk "GUARDA DE BASE: main == base registrada y main+diff == stage" 'base_ok'
chk "tests de stage 26/26"                          '"$PY" -I "$STAGE/test_tokens_universo.py" 2>&1 | tail -n1 | grep -q "TOTAL 26 / 26"'
chk "screen observadores viva"                      'screen -ls | grep -qE "[0-9]+\.observadores[[:space:]]"'
chk "hay hijo libro_estado_ws vivo"                 'ps -eo args | grep -q "[l]ibro_estado_ws.py --hijo"'
chk "watchdog escribiendo (log <120 s)"             '[ $(( $(date +%s) - $(stat -c %Y "$REPO/logs/watchdog.log") )) -lt 120 ]'
chk "disco del volumen libro5 con >=10 GB libres"   '[ $(df -BG --output=avail "$LIBRO5" | tail -n1 | tr -dc 0-9) -ge 10 ]'
if [ $EJECUTAR -ne 1 ]; then
  act "P1 flock -w 60 /tmp/restart_ram_fase0.lock (bloquea restart_ram y guard_ram)"
  act "P2 esperar un tick de logs/watchdog.log (<=135 s) +10 s y repetir la guarda de base"
  act "P3 cp $MAIN -> $DL/traspaso_tokens/libro_estado_ws.py.pre ; cp $STAGE/libro_estado_ws.py -> $MAIN"
  act "P4 $PY verify_deploy.py --restart observadores"
  act "P5 esperar <=120 s: 'conectado [' nuevo en observadores_fase0.log, hijo en RESERVA de Binance, filas G arranque en libro5_ms, 0 Traceback, bnreg sigue dueno"
  act "marcha atras si P5 falla: cp .pre -> main ; verify_deploy --restart observadores"
  log "Modo dry-run: no se cambio nada. fallos previos=$fallos. Log: $LOGF"; exit $((fallos>0))
fi
[ $fallos -eq 0 ] || { log "ABORTO: comprobaciones previas fallidas ($fallos); nada modificado"; exit 1; }

restaurar() {
  log "MARCHA ATRAS: restaurar .pre en main y reiniciar observadores"
  [ -f "$DL/traspaso_tokens/libro_estado_ws.py.pre" ] && cp "$DL/traspaso_tokens/libro_estado_ws.py.pre" "$MAIN"
  (cd "$REPO" && "$PY" verify_deploy.py --restart observadores) 2>&1 | tee -a "$LOGF"
  log "marcha atras hecha; sha256 main=$(sha "$MAIN")"
}
die() { log "FALLO: $*"; restaurar; exit 1; }

log "== P1 flock restart_ram_fase0 =="
exec 9>/tmp/restart_ram_fase0.lock
flock -w 60 9 || { log "ABORTO: no se pudo tomar /tmp/restart_ram_fase0.lock en 60 s; nada modificado"; exit 1; }
log "== P2 esperar un tick del watchdog =="
ult=$(tail -n1 "$REPO/logs/watchdog.log" | cut -c1-22); act_=$ult
for i in $(seq 1 135); do act_=$(tail -n1 "$REPO/logs/watchdog.log" | cut -c1-22); [ "$act_" != "$ult" ] && break; sleep 1; done
[ "$act_" != "$ult" ] || { log "ABORTO: el watchdog no escribio ningun tick en 135 s; nada modificado"; exit 1; }
sleep 10
hm=$(hora_min)
{ { [ $hm -lt 360 ] || [ $hm -ge 555 ]; } && { [ $hm -lt 810 ] || [ $hm -ge 1260 ]; } && ! hueco4h; } || { log "ABORTO: tras la espera la hora ya no es valida; nada modificado"; exit 1; }
base_ok || { log "ABORTO: main cambio mientras esperabamos (guarda de base); nada modificado"; exit 1; }
bn_estado_ok activo 15 && bn_es_duenyo || { log "ABORTO: bnreg ya no es dueno del lock; nada modificado"; exit 1; }
log "== P3 backup + cp =="
cp "$MAIN" "$DL/traspaso_tokens/libro_estado_ws.py.pre" || { log "ABORTO: backup fallido; nada modificado"; exit 1; }
[ "$(sha "$DL/traspaso_tokens/libro_estado_ws.py.pre")" = "$(tr -d ' \n' < "$STAGE/BASE_main.sha256")" ] || { log "ABORTO: .pre != base; nada modificado"; exit 1; }
off0=$(stat -c %s "$LOGOBS"); t0=$(date +%s); dia=$(date -u +%F)
cp "$STAGE/libro_estado_ws.py" "$MAIN" || die "cp fallido"
log "== P4 reinicio de observadores (verify_deploy) =="
(cd "$REPO" && "$PY" verify_deploy.py --restart observadores) 2>&1 | tee -a "$LOGF" || die "verify_deploy --restart fallo"
log "== P5 comprobaciones (<=120 s) =="
ok_conn=0
for i in $(seq 1 120); do
  tail -c +$((off0 + 1)) "$LOGOBS" 2>/dev/null | grep -q "conectado \[" && { ok_conn=1; break; }; sleep 1
done
[ $ok_conn -eq 1 ] || die "ningun 'conectado [' en 120 s"
sleep 15
nuevo=$(tail -c +$((off0 + 1)) "$LOGOBS" 2>/dev/null)
echo "$nuevo" | grep -q "Traceback" && die "Traceback en el log de observadores tras el reinicio"
echo "$nuevo" | grep -q "RESERVA" || die "el hijo nuevo no dice RESERVA de Binance"
bn_estado_ok activo 15 && bn_es_duenyo || die "bnreg ya NO es dueno del lock"
f5=$(ls -t "$LIBRO5"/libro5_ms_${dia}_*.csv.gz 2>/dev/null | head -n1)
[ -n "$f5" ] && [ "$(stat -c %Y "$f5")" -ge "$t0" ] || die "no hay fichero libro5_ms nuevo (>= inicio del despliegue)"
zcat "$f5" 2>/dev/null | head -n 200000 | awk -F, '$1=="G" && $4 ~ /arranque/ {f=1} END{exit !f}' || die "sin fila G arranque en $f5"
ps -eo args | grep -q "[l]ibro_estado_ws.py --hijo" || die "no hay hijo vivo"
log "OK: desplegado. sha256 main=$(sha "$MAIN"); .pre en $DL/traspaso_tokens/libro_estado_ws.py.pre; libro5 nuevo: $f5"
log "Vigilar: logs/observadores_fase0.log (sesion caida / refresco de universo fallo / universo parcial), proxima ventana 23:45-00:01 con el sondeo."
