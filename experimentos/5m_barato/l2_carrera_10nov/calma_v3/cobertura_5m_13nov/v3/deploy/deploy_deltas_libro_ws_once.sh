#!/bin/bash
# deploy_deltas_libro_ws_once.sh -- despliegue UNICO de la cobertura 5m a +24 h (CB/v3): libro_estado_ws (delta horizonte+siembra nmu+pausa 429),
# capture_markets (adelanto + fix 429, APAGADOS por defecto) y universo_5m_io (modulo nuevo). Derivado de traspaso_bnreg_once.sh. ESTADO: ESCRITO, NO EJECUTADO. Por defecto DRY-RUN (solo lecturas + imprime acciones). Lo lanza la sesion principal.
# Uso:  bash deploy_deltas_libro_ws_once.sh                              -> dry-run (comprobaciones P0 reales)
#       bash deploy_deltas_libro_ws_once.sh --hora HH:MM                 -> dry-run simulando esa hora UTC
#       bash deploy_deltas_libro_ws_once.sh --ejecutar [--sustituye-restart-ram] [--activar]
#   --sustituye-restart-ram : ademas de observadores reinicia vigiasfreq (lo que hace restart_ram) -> pensado para lanzarse a las 22:19Z con `at`:
#                             retiene /tmp/restart_ram_fase0.lock (el cron 22:20 lo toma sin esperar => el cron se SALTA) y evita un 2o reinicio.
#   --activar               : tras verificar, escribe cfg_CAPTURE_5M_HORIZONTE_MIN=1440 y cfg_CAPTURE_429_FIX=1 en datalogs/universo_5m/ (el siguiente ciclo de
#                             capture_markets arranca el adelanto). Marcha atras: rm de esos dos ficheros. Sin --activar el codigo nuevo corre con comportamiento main.
# PLAN (Javi/red team 14-Nov): se despliega SOLO v3 (UN reinicio de observadores). v3 ya contiene v5 (cache de tokens + deltas): la base original de main
#   (a0196ee4) es aceptada; el antiguo deploy_tokens_cache_once.sh (v5) es ahora un wrapper que NO ejecuta nada. Sin --activar en la
#   primera ventana: el codigo nuevo se comporta como main hasta que existan los cfg. P2b siembra la cache de tokens (como v5) ANTES de P2.
# Marcha atras VERIFICADA: (retoma el lock de restart_ram si ya se solto; si no puede, NO reinicia y lo dice) restaura .pre, comprueba sha, reinicia, exige 1 hijo
#   nuevo sostenido + libro5 creciendo; el aviso critico va DESPUES con el resultado real (OK/FALLO). Las senales durante la marcha atras se DIFIEREN. Un trap
#   restaura si el script muere entre el cp y el final. Si el adelanto estaba activo (cfg), se PARA el capture_markets en curso (lee los cfg al importar) y se verifica
#   que no escribe mas adelanto_*. Se borra gamma_pausa.json si lo creo el despliegue.
# P0 exige ademas: contrato con el verify_deploy REAL (solo lectura) y el sello del ensayo e2e con procesos reales (tests/test_e2e_real.py, <24 h, sha actual).
# P6 es DETERMINISTA: 1) captura real aislada del codigo nuevo (p6_ciclo_aislado.py) 2) artefacto del proximo ciclo real (>1 ciclo slow; solo un ciclo que ARRANCA tras el cp y se
#   analiza desde su linea de inicio), ACOTADO para no cruzar una ventana prohibida. rc 4 = desplegado con una decision pendiente (P6 sin veredicto o --activar diferido por
#   ventana): ni OK ni marcha atras.
# VENTANAS (06:00-09:15Z, 13:30-21:00Z, huecos de 4 h xx:40-xx+1:05): P0 exige >= P0_MARGEN_MIN (20) min hasta la proxima. Si aun asi una marcha atras cae dentro de una: si observadores
#   ya estaba verificado (P5 ok) solo se restaura capture_markets y NO se reinicia (libro/io se quedan; aviso); si el fallo es anterior a P5 prevalece restaurar + reiniciar con aviso explicito.
# La marcha atras NO pisa un fichero de main que cambio por otra mano tras el despliegue (aviso critico) y solo borra los cfg que escribio este despliegue (manifiesto).
# --activar: el adelanto abarca las 6 monedas y CAPTURE_429_FIX afecta a ETH/SOL en data/markets: exige CONFIRMO_ADELANTO_6_MONEDAS=1 en TODOS los caminos que escriben cfg.
# DRY-RUN (M5): NO toca el repo ni las screens, pero ESCRIBE en datalogs/traspaso_deltas_ws/ (su log deploy_<ts>.log con la cabecera y las comprobaciones, el directorio, y _aplica.py temporal
#   de la guarda de base) y crea ficheros temporales en /tmp y /var/tmp; no escribe logs/deploy_deltas_ws_aviso.log ni manda Telegram. DEPLOY_SANDBOX=1 lo redirige todo a un sandbox.
# (e) AVISO libro_estado_ws.py de main tiene cambios SIN COMMITEAR (bnreg+v3 en el arbol de trabajo, no en HEAD): el .pre/base es ESA version de trabajo; un `git checkout/stash/reset` la perderia.
#   P0 lo avisa (git status del repo) y P3 guarda una copia con sello horario en datalogs/traspaso_deltas_ws/<fichero>.worktree_<ts> ANTES del cp (no se commitea nada).
# (M7) RIESGO BAJO, ACEPTADO: gamma-api es COMPARTIDA (limite 429 por IP) con precierre/observadores y P2b (siembra) + P6 (captura aislada) hacen peticiones: con precierre vivo el
#   presupuesto de P2b baja a P2B_PRESUPUESTO_PRECIERRE_S (60). El 429 en P2b/P6 es transitorio (BLANDO / inconcluso), nunca un fallo del codigo.
# No se lanza con bash -c ni heredoc ni pgrep/pkill -f; la linea de comandos no contiene los nombres de los .py.
# P0 guardas -> P1 flock restart_ram -> P2 tick del watchdog -> guarda de base otra vez -> P3 backup .pre + cp (universo_5m_io, capture, libro)
#   -> P4 verify_deploy --restart observadores [+ vigiasfreq] -> P5 comprobaciones -> P6 activar (opcional). Cualquier fallo DURO: marcha atras (.pre + reinicio).
# Idempotente: si los 3 ficheros ya son los objetivo => "ya desplegado", rc 0, sin tocar nada ni reiniciar.
# La lib se verifica contra SHA256SUMS ANTES de cargarla (copia temporal + sha256).
# La base de libro_estado_ws puede ser la ORIGINAL de main (a0196ee4) o v5 (f306815c, job at 57 de las 21:05Z): se acepta la que coincida y se exige
# base+diff == objetivo. capture_markets: base 5e2706bb. Perdida esperada: ~1 min de libro5 Polymarket y el historico ms en memoria de observadores.
set -u
REPO=${REPO:-/root/polymarket-research}
DL=${DL:-/root/polymarket-research-datalogs}
V3=${V3:-$(cd "$(dirname "$0")/.." && pwd)}
# #9: la lib se verifica ANTES de ejecutar nada de ella: se copia a un fichero temporal, se compara su sha256 con el de SHA256SUMS y se hace 'source' de ESA copia (sin hueco entre
# comprobar y usar). Dry-run incluido. (P0 sigue comprobando todo SHA256SUMS: sumas_ok.)
_LIB_COPIA=$(mktemp "${TMPDIR:-/tmp}/lib_espera_hijos.XXXXXX.sh") || { echo "ABORTO: no se pudo crear la copia temporal de lib_espera_hijos.sh"; exit 2; }
cp "$V3/deploy/lib_espera_hijos.sh" "$_LIB_COPIA" 2>/dev/null || { rm -f "$_LIB_COPIA"; echo "ABORTO: falta $V3/deploy/lib_espera_hijos.sh"; exit 2; }
_LIB_ESPERADO=$(awk '$2 == "deploy/lib_espera_hijos.sh" { print $1 }' "$V3/SHA256SUMS" 2>/dev/null)
[ -n "$_LIB_ESPERADO" ] && [ "$(sha256sum "$_LIB_COPIA" | cut -d' ' -f1)" = "$_LIB_ESPERADO" ] || { rm -f "$_LIB_COPIA"; echo "ABORTO: lib_espera_hijos.sh no coincide con $V3/SHA256SUMS (o no figura): NO se ejecuta nada"; exit 2; }
# H9: lo mismo para clases_error.conf (unica fuente de las listas de clases de error, la lee tambien p6_ciclo_aislado.py desde $V3/deploy): copia temporal verificada y CLASES_CONF apunta a ELLA.
_CONF_COPIA=$(mktemp "${TMPDIR:-/tmp}/clases_error.XXXXXX.conf") || { rm -f "$_LIB_COPIA"; echo "ABORTO: no se pudo crear la copia temporal de clases_error.conf"; exit 2; }
cp "$V3/deploy/clases_error.conf" "$_CONF_COPIA" 2>/dev/null || { rm -f "$_LIB_COPIA" "$_CONF_COPIA"; echo "ABORTO: falta $V3/deploy/clases_error.conf"; exit 2; }
_CONF_ESPERADO=$(awk '$2 == "deploy/clases_error.conf" { print $1 }' "$V3/SHA256SUMS" 2>/dev/null)
[ -n "$_CONF_ESPERADO" ] && [ "$(sha256sum "$_CONF_COPIA" | cut -d' ' -f1)" = "$_CONF_ESPERADO" ] || { rm -f "$_LIB_COPIA" "$_CONF_COPIA"; echo "ABORTO: clases_error.conf no coincide con $V3/SHA256SUMS (o no figura): NO se ejecuta nada"; exit 2; }
# R2: la copia VERIFICADA se conserva hasta el final (la lee tambien p6_ciclo_aislado.py via CLASES_CONF exportada) y se borra al salir (trap; al_salir de la lib tambien la borra).
# R3: si la lib no carga (conf vacio/ausente => return 2) NO se sigue con una lib a medias.
trap 'rm -f "${_CONF_COPIA:-}"' EXIT
export CLASES_CONF="$_CONF_COPIA"; . "$_LIB_COPIA" || { rc_lib=$?; rm -f "$_LIB_COPIA" "$_CONF_COPIA"; echo "ABORTO: la lib no cargo (rc=$rc_lib): NO se ejecuta nada"; exit 2; }; rm -f "$_LIB_COPIA"
PY=${PY:-$REPO/.venv/bin/python}
LIBRO5=${LIBRO5:-/mnt/HC_Volume_106538179/libro5_ms}
LOGOBS=${LOGOBS:-$REPO/logs/observadores_fase0.log}
WDLOG=${WDLOG:-$REPO/logs/watchdog.log}
RAMLOCK=${RAMLOCK:-/tmp/restart_ram_fase0.lock}
LOADAVG=${LOADAVG:-/proc/loadavg}
TESTS_MIN=${TESTS_MIN:-91}   # piso unico de tests del harness de libro_estado_ws (el v5 ya no se despliega)
MIN_GB=${MIN_GB:-15}   # >= MIN_LIBRE_GB (10) de libro5 + margen: por debajo libro5 se PAUSA y libro5_crece daria un falso DURO
CFGDIR=${CFGDIR:-$DL/universo_5m}
SEMBRAR_PY=${SEMBRAR_PY:-$V3/delta_v3/sembrar_cache_tokens.py}
T_LIBRO=$V3/delta_v3/libro_estado_ws.py; T_CAP=$V3/stage/capture_markets.py; T_IO=$V3/stage/universo_5m_io.py
M_LIBRO=$REPO/libro_estado_ws.py; M_CAP=$REPO/capture_markets.py; M_IO=$REPO/universo_5m_io.py
BASE_LIBRO_ORIG=${BASE_LIBRO_ORIG:-a0196ee481a2fb3c4caaf106fd317b28a13ca7d42e24230454cc8c3f828368aa}
BASE_LIBRO_V5=${BASE_LIBRO_V5:-f306815c700fcc6f}        # prefijo suficiente (se compara por prefijo)
BASE_CAP=${BASE_CAP:-5e2706bb28b07aa1}
if [ "${DEPLOY_SANDBOX:-0}" = "1" ]; then
  for _p in "$REPO" "$DL" "$LIBRO5" "$LOGOBS" "$RAMLOCK" "$CFGDIR"; do
    case "$(readlink -f -- "$_p" 2>/dev/null || echo "$_p")" in /root/polymarket-research|/root/polymarket-research/*|/root/polymarket-research-datalogs|/root/polymarket-research-datalogs/*|/mnt/HC_Volume_106538179|/mnt/HC_Volume_106538179/*|/tmp/restart_ram_fase0.lock)
      echo "SANDBOX: la ruta $_p apunta al sistema REAL; abortado"; exit 3;; esac
  done
fi
EJECUTAR=0; HORA_SIM=""; ACTIVAR=0; SUSTITUYE=0
while [ $# -gt 0 ]; do case "$1" in
  --ejecutar) EJECUTAR=1;; --activar) ACTIVAR=1;; --sustituye-restart-ram) SUSTITUYE=1;; --hora) shift; HORA_SIM=${1:-};;
  *) echo "argumento desconocido: $1"; exit 2;; esac; shift; done
[ $EJECUTAR -eq 1 ] && [ -n "$HORA_SIM" ] && { echo "--hora solo en dry-run"; exit 2; }
PRE=$DL/traspaso_deltas_ws; mkdir -p "$PRE"; SLOWLOG="$REPO/logs/slow.log"
CFG_MANIFEST="$PRE/cfg_manifest_$$.txt"     # #8: lo unico que el despliegue escribio en CFGDIR (y revertir_cfg puede borrar)
LOGF="$DL/traspaso_deltas_ws/deploy_$(date -u +%Y%m%dT%H%M%SZ).log"
log() { echo "[$(date -u +%FT%TZ)] $*" | tee -a "$LOGF"; }
AVISO_LOG="$REPO/logs/deploy_deltas_ws_aviso.log"
# #6: el fallo de Telegram (rc != 0 o enviar_telegram() == False) NO se oculta: queda en el log y en AVISO_LOG (el aviso ya esta escrito ahi). Nunca cambia el rc del deploy.
telegram() {
  [ $EJECUTAR -eq 1 ] && [ "${DEPLOY_SANDBOX:-0}" != "1" ] || return 0
  (cd "$REPO" && timeout 40 "$PY" -c 'import sys; from shadow_digest import enviar_telegram; sys.exit(0 if enviar_telegram(sys.argv[1]) else 3)' "$1" >/dev/null 2>&1); local r=$?
  [ $r -eq 0 ] || { log "AVISO: Telegram NO enviado (rc=$r)"; echo "[$(date -u +%FT%TZ)] AVISO: Telegram NO enviado (rc=$r) para: ${1:0:120}" >> "$AVISO_LOG"; }
  return 0
}
aviso_critico() {
  local m="CRITICO deploy deltas libro_ws: $*"
  # M4: ABORTO = nada modificado. El cron de restart_ram solo quedo OMITIDO si su hora cayo MIENTRAS teniamos el lock (LOCK_T0..ahora); si aun no ha llegado, correra normal.
  case "$*" in ABORTO*) [ $SUSTITUYE -eq 1 ] && [ $EJECUTAR -eq 1 ] && m="$m [restart_ram_fase0: $(estado_restart_ram)]";; esac
  log "$m"; [ $EJECUTAR -eq 1 ] && { mkdir -p "$(dirname "$AVISO_LOG")"; echo "[$(date -u +%FT%TZ)] $m" >> "$AVISO_LOG"; }      # H6: el dry-run no escribe el AVISO_LOG real
  case "$*" in ABORTO*) [ "${LOCK:-0}" = 1 ] && { liberar_lock; log "lock de restart_ram LIBERADO tras el ABORTO (antes de avisar por Telegram)"; };; esac
  telegram "$m"
}
# Aviso de EXITO (Telegram + log + AVISO_LOG): para distinguir "desplegado OK" de "el at no corrio". Mismo canal que aviso_critico.
aviso_ok() {
  local m="OK deploy deltas libro_ws: $*"
  log "$m"; [ $EJECUTAR -eq 1 ] && { mkdir -p "$(dirname "$AVISO_LOG")"; echo "[$(date -u +%FT%TZ)] $m" >> "$AVISO_LOG"; }      # H6
  telegram "$m"
}
act() { if [ $EJECUTAR -eq 1 ]; then log "ACCION: $*"; return 0; else log "[DRY] haria: $*"; return 1; fi; }
sha() { sha256sum "$1" 2>/dev/null | cut -d' ' -f1; }
# estado de cada fichero: ya | base | NO (vacio para el modulo nuevo ausente = base)
# H4: un objetivo vacio/ilegible NUNCA es 'ya' (sha vacio == sha vacio daba un falso 'ya'): se exige [ -s objetivo ] y sha no vacio antes de comparar.
_igual_obj() { [ -s "$2" ] && [ -n "$1" ] && [ "$1" = "$(sha "$2")" ]; }
estado_libro() { local s; s=$(sha "$M_LIBRO"); _igual_obj "$s" "$T_LIBRO" && { echo ya; return; }
  case "$s" in "$BASE_LIBRO_ORIG"|"$BASE_LIBRO_V5"*) echo base;; *) echo NO;; esac; }
estado_cap() { local s; s=$(sha "$M_CAP"); _igual_obj "$s" "$T_CAP" && { echo ya; return; }
  case "$s" in "$BASE_CAP"*) echo base;; *) echo NO;; esac; }
estado_io() { [ ! -e "$M_IO" ] && { echo base; return; }; _igual_obj "$(sha "$M_IO")" "$T_IO" && echo ya || echo NO; }
# guarda de base: cada fichero esta en su base conocida o ya es el objetivo; y base+diff == objetivo (el diff aplica y no lleva nada mas)
diff_ok() {   # $1 = main  $2 = diff  $3 = objetivo
  local tmp="$DL/traspaso_deltas_ws/_aplica.py"; rm -f "$tmp"
  patch -s -o "$tmp" "$1" "$2" >/dev/null 2>&1 || return 1; [ "$(sha "$tmp")" = "$(sha "$3")" ]; }
base_ok() {
  local e1 e2 e3; e1=$(estado_libro); e2=$(estado_cap); e3=$(estado_io)
  [ "$e1" != NO ] && [ "$e2" != NO ] && [ "$e3" != NO ] || { log "base: estado libro=$e1 capture=$e2 io=$e3 (NO = no coincide con base conocida ni con el objetivo)"; return 1; }
  if [ "$e1" = base ]; then
    local d="$V3/diffs/libro_estado_ws.main_orig_a_v3.diff"; [ "$(sha "$M_LIBRO" | cut -c1-16)" = "${BASE_LIBRO_V5:0:16}" ] && d="$V3/diffs/libro_estado_ws.v5_a_v3.diff"
    diff_ok "$M_LIBRO" "$d" "$T_LIBRO" || { log "base: libro_estado_ws + $(basename "$d") != objetivo"; return 1; }; fi
  if [ "$e2" = base ]; then diff_ok "$M_CAP" "$V3/diffs/capture_markets.main_a_v3.diff" "$T_CAP" || { log "base: capture_markets + diff != objetivo"; return 1; }; fi
  return 0
}
todo_ya() { [ "$(estado_libro)" = ya ] && [ "$(estado_cap)" = ya ] && [ "$(estado_io)" = ya ]; }
hora_min() { local h; h=${SANDBOX_HORA:-}; [ -n "${SANDBOX_HORA_FILE:-}" ] && [ -s "$SANDBOX_HORA_FILE" ] && h=$(cat "$SANDBOX_HORA_FILE")      # harness: la hora puede cambiar durante la ejecucion
  if [ "${DEPLOY_SANDBOX:-0}" = "1" ] && [ -n "$h" ]; then echo $(( 10#${h%:*} * 60 + 10#${h#*:} ));
  elif [ -n "$HORA_SIM" ]; then echo $(( 10#${HORA_SIM%:*} * 60 + 10#${HORA_SIM#*:} )); else echo $(( 10#$(date -u +%H) * 60 + 10#$(date -u +%M) )); fi; }
sumas_ok() { ( cd "$V3" && sha256sum -c --quiet SHA256SUMS 2>/dev/null ); }
tests_ok() {
  local w l a x y; w=$(mktemp -d); cp "$T_LIBRO" "$w/libro_estado_ws.py"; cp "$V3/delta_v3/test_tokens_universo.py" "$w/"; cp "$T_IO" "$w/"
  l=$(cd "$w" && "$PY" -I test_tokens_universo.py 2>&1 | grep "^TOTAL "); rm -rf "$w"
  a=${l#TOTAL }; x=${a%% /*}; y=${a##*/ }; [ -n "$l" ] && [ "$x" = "$y" ] && [ "${y:-0}" -ge "$TESTS_MIN" ]; }
espera_crons() {
  local m s dormir ms; m=$(date -u +%-M); s=$(date -u +%-S); ms=$(( m * 60 + s ))
  if [ $ms -ge 240 ] && [ $ms -lt 630 ]; then dormir=$(( 630 - ms )); else dormir=0; fi
  [ "${DEPLOY_SANDBOX:-0}" = "1" ] && dormir=0
  if [ $EJECUTAR -ne 1 ]; then
    [ -n "$HORA_SIM" ] && ms=$(( 10#${HORA_SIM#*:} * 60 )) && { [ $ms -ge 240 ] && [ $ms -lt 630 ] && dormir=$(( 630 - ms )) || dormir=0; }
    act "P0b si minuto UTC en :04-:10 dormir hasta :10:30 (aqui: ${dormir} s) y esperar load5/nproc<=3 (max 300 s; si no baja ABORTO sin tocar nada)"; return 0
  fi
  [ $dormir -gt 0 ] && { log "P0b: ${m} min -> racimo de crons horarios; duermo ${dormir} s"; sleep $dormir; }
  local i n l5; n=$(nproc)
  for i in $(seq 1 60); do l5=$(cut -d' ' -f2 "$LOADAVG")
    awk -v l="$l5" -v n="$n" 'BEGIN{exit !(l/n<=3)}' && { log "P0b: carga ok (load5=$l5, nproc=$n)"; return 0; }; sleep 5; done
  aviso_critico "ABORTO: load5=$l5 con nproc=$n no bajo de 3/nucleo en 300 s; nada modificado"; exit 1
}
# #8: idempotencia ANTES de tomar el lock/esperar crons/cargas: si ya esta todo desplegado no se bloquea restart_ram ni se manda ningun CRITICO.
# (e) aviso de cambios sin commitear en los ficheros de main que se van a sobrescribir (git sin locks opcionales: no compite con el commit automatico de los loops)
aviso_worktree() {
  local f out; git --no-optional-locks -C "$REPO" rev-parse --is-inside-work-tree >/dev/null 2>&1 || return 0
  for f in libro_estado_ws.py capture_markets.py universo_5m_io.py; do
    out=$(git --no-optional-locks -C "$REPO" status --porcelain -- "$f" 2>/dev/null); [ -n "$out" ] || continue
    log "AVISO (e): $f de main tiene cambios SIN COMMITEAR en el arbol de trabajo ('$out'): la base/.pre sera ESA version de trabajo y no HEAD; P3 guarda una copia en $PRE (un git checkout/stash/reset la perderia)"
  done
  return 0
}
# I2: --ejecutar --activar sobre algo YA DESPLEGADO escribe los cfg del adelanto: mismas garantias que la activacion de P6 (ventana libre con margen, lock de restart_ram, el codigo de
# main verificado AHORA con una captura aislada que NO sea inconclusa) y rc != 0 si no se activa (antes: 'IGNORADO' con rc 0).
ya_activar() {
  local hm0 peor r; log "== --activar sobre YA DESPLEGADO: ventana libre + lock + codigo verificado (P6 aislado) antes de escribir los cfg =="
  hm0=$(hora_min)
  ventana_de "$hm0" && { aviso_critico "--activar REHUSADO (rc 1): dentro de una ventana prohibida ($VENTANA); no se escribio ningun cfg"; return 1; }
  peor=$(( ${P6_AIS_INTENTOS:-3} * (${P6_AIS_TIMEOUT:-240} + ${P6_AIS_PAUSA:-70}) ))
  min_hasta_ventana "$hm0"; [ $(( MH * 60 )) -ge $(( peor + ${P6_MARGEN_S:-300} )) ] || { aviso_critico "--activar REHUSADO (rc 1): la proxima ventana prohibida ($VENTANA) empieza en $MH min y la verificacion aislada puede tardar ${peor}s; no se escribio ningun cfg"; return 1; }
  tomar_lock || { aviso_critico "--activar REHUSADO (rc 1): no se pudo tomar $RAMLOCK en ${P1_TIMEOUT:-60} s; no se escribio ningun cfg"; return 1; }
  cap_ok "$REPO" || { liberar_lock; aviso_critico "--activar REHUSADO (rc 1): el capture_markets de main no queda apagado por cfg: $CAP_OK_MOTIVO"; return 1; }
  p6_aislado; r=$?
  [ $r -eq 0 ] || { liberar_lock; aviso_critico "--activar REHUSADO (rc 1): P6 captura aislada del codigo de main no verifica (rc=$r): $CAP_MOTIVO"; return 1; }
  [ "${P6_INTERMITENTE:-0}" = 1 ] && { liberar_lock; aviso_critico "--activar REHUSADO (rc 1): P6 INTERMITENTE (un error de codigo de la captura aislada no se repitio: bug no determinista posible; no verificado): ${P6_INTERMITENTE_TXT:-?}; no se escribio ningun cfg"; return 1; }
  activar_cfg || { liberar_lock; aviso_critico "--activar FALLO (rc 1): activar_cfg no escribio los cfg (ver $LOGF)"; return 1; }
  liberar_lock; return 0
}
# #1: --ejecutar --activar sin CONFIRMO_ADELANTO_6_MONEDAS=1 se rechaza AQUI, antes de tomar el lock, de P0 y de cualquier captura (dry-run incluido): rc 4 + aviso critico, nada modificado.
if [ $ACTIVAR -eq 1 ] && [ "${CONFIRMO_ADELANTO_6_MONEDAS:-0}" != "1" ]; then
  aviso_critico "--activar RECHAZADO (rc 4): falta CONFIRMO_ADELANTO_6_MONEDAS=1 (el adelanto abarca 6 monedas y CAPTURE_429_FIX afecta a ETH/SOL en data/markets); nada modificado, repetir con la variable"; exit 4; fi
if todo_ya; then log "YA DESPLEGADO: libro_estado_ws, capture_markets y universo_5m_io ya son el objetivo; no se toca ni se reinicia nada (sin esperas ni reinicios)"
  [ $EJECUTAR -eq 1 ] && [ $ACTIVAR -eq 1 ] && { ya_activar; r=$?; [ $r -ne 0 ] || aviso_ok "--activar OK (rc 0) sobre YA DESPLEGADO: cfg del adelanto escritos (efecto en el siguiente ciclo de capture_markets)"; exit $r; }
  exit 0; fi
if [ $EJECUTAR -eq 1 ]; then      # M7: el lock ANTES de cualquier espera (dormir/carga): el cron 22:20 se salta y no hay doble reinicio; si no se toma, aborto limpio
  log "== P1 flock restart_ram_fase0 (temprano: antes de las esperas de carga) =="
  tomar_lock || { aviso_critico "ABORTO: no se pudo tomar $RAMLOCK en ${P1_TIMEOUT:-60} s; nada modificado"; exit 1; }
fi
espera_crons
hm=$(hora_min); fallos=0
chk() { if eval "$2"; then log "OK    $1"; else log "FALLA $1"; fallos=$((fallos+1)); fi; }
hueco4h() { ventana_de "$hm" && case "$VENTANA" in hueco*) return 0;; esac; return 1; }
hora_ok() { ! ventana_de "$hm"; }
log "== P0 comprobaciones (ejecutar=$EJECUTAR activar=$ACTIVAR sustituye_restart_ram=$SUSTITUYE hora_utc=$(printf '%02d:%02d' $((hm/60)) $((hm%60)))${HORA_SIM:+ SIMULADA}) =="
chk "fuera de 06:00-09:15Z"                         '[ $hm -lt 360 ] || [ $hm -ge 555 ]'
chk "fuera de 13:30-21:00Z (horario USA)"           '[ $hm -lt 810 ] || [ $hm -ge 1260 ]'
chk "fuera de los huecos de 4 h (xx:40-xx+1:05, xx=03,07,11,15,19,23)" '! hueco4h'
chk "margen: >= ${P0_MARGEN_MIN:-20} min hasta la proxima ventana prohibida (ni el despliegue, ni su reversion, ni P6 deben cruzarla)" 'min_hasta_ventana "$hm"; [ "$MH" -ge "${P0_MARGEN_MIN:-20}" ] || { log "  la proxima ventana prohibida ($VENTANA) empieza en $MH min"; false; }'
chk "bnreg activo y DUENO del lock de Binance"      'espera_bnreg ${P0_BN_S:-20}'
chk "centinela BNREG_HABILITADO presente"           '[ -e "$DL/BNREG_HABILITADO" ]'
chk "SHA256SUMS de CB/v3 integro (lo auditado == lo que se copia)" 'sumas_ok'
chk "objetivos compilan"                            '"$PY" -m py_compile "$T_LIBRO" "$T_CAP" "$T_IO"'
chk "objetivo libro conserva reserva/cesion bnreg y trae horizonte+nmu+pausa" 'grep -q "BNREG_LOCK" "$T_LIBRO" && grep -q "hijo_cede" "$T_LIBRO" && grep -q "_nmu_mercados" "$T_LIBRO" && grep -q "_gamma_pausado" "$T_LIBRO"'
chk "GUARDA DE BASE: libro/capture/io en base conocida y base+diff == objetivo" 'base_ok'
chk "harness libro_estado_ws TODOS en verde (>=$TESTS_MIN) y base re-validada" 'tests_ok && base_ok'
chk "datalogs escribible"                           '[ -w "$DL" ]'
aviso_worktree
chk "screen observadores viva"                      'screen -ls | grep -qE "[0-9]+\.observadores[[:space:]]"'
[ $SUSTITUYE -eq 1 ] && chk "screen vigiasfreq viva" 'screen -ls | grep -qE "[0-9]+\.vigiasfreq[[:space:]]"'
chk "hay hijo libro_estado_ws vivo y su padre se identifica como observadores_fase0.py (cmdline en cualquier posicion)" '[ -n "$(hijos_vivos)" ] || { log "  hijos del repo con padre NO reconocido: $(diag_padres | head -n 3 | tr "\n" "|")"; false; }'
chk "contrato con el verify_deploy REAL (solo lectura: informe + --restart + SCREEN_RESTART)" 'contrato_verify_deploy || { log "  $CONTRATO_MOTIVO"; false; }'
E2E_FILES=("$V3/deploy/deploy_deltas_libro_ws_once.sh" "$V3/deploy/lib_espera_hijos.sh" "$V3/deploy/p6_ciclo_aislado.py" "$V3/deploy/clases_error.conf" "$SEMBRAR_PY" "$T_LIBRO" "$T_CAP" "$T_IO")
E2E_STAMP=${E2E_STAMP:-$DL/traspaso_deltas_ws/e2e_ok.json}
chk "ensayo e2e con procesos REALES pasado (<${E2E_MAX_H:-24} h) con el sha actual de estos scripts (un skip no sella)" 'e2e_sello_ok "$E2E_STAMP" "${E2E_FILES[@]}" || { log "  $E2E_MOTIVO"; false; }'
chk "watchdog escribiendo (log <900 s: solo escribe cada ~10 min)"             '[ $(( $(date +%s) - $(stat -c %Y "$WDLOG") )) -lt 900 ]'
chk "disco del volumen libro5 con >=${MIN_GB} GB libres (>= MIN_LIBRE_GB de libro5 + margen)"   '[ $(df -BG --output=avail "$LIBRO5" | tail -n1 | tr -dc 0-9) -ge $MIN_GB ]'
chk "capture_markets objetivo: universo_5m_io importa y el adelanto sale apagado POR CFG (rc 0)" 'cap_ok "$V3/stage" || { log "  $CAP_OK_MOTIVO"; false; }'
if [ $EJECUTAR -ne 1 ]; then
  act "P0 tambien: contrato con verify_deploy real (solo lectura), sello del ensayo e2e con procesos reales (<${E2E_MAX_H:-24} h, sha actual), padre observadores identificable"
  act "P1 flock -w ${P1_TIMEOUT:-60} $RAMLOCK ANTES de las esperas de carga (bloquea restart_ram y guard_ram; con --sustituye-restart-ram el cron 22:20 se salta)"
  act "P2b siembra de la cache de tokens (BLANDO) y P2 sincronia con el watchdog (<=~135 s); repetir hora y guarda de base"
  act "(P2 antiguo) esperar un tick de $WDLOG (<=135 s) +10 s y repetir hora y guarda de base"
  act "P3 backup .pre de libro_estado_ws/capture_markets/universo_5m_io en $DL/traspaso_deltas_ws/ + copia con sello horario (.main_<ts>) de libro_estado_ws/capture_markets (arbol de trabajo, aunque no este commiteado); cp objetivos -> main (orden: io, capture, libro)"
  act "P4 verify_deploy.py --restart observadores$([ $SUSTITUYE -eq 1 ] && echo ' y luego vigiasfreq (blando)')"
  act "P5 DUROS (marcha atras): 1 hijo NUEVO 'conectado [' en 180 s, sin hijo viejo, sin Traceback de libro_estado_ws/universo_5m_io, bnreg conserva el lock, hijo vivo | rc4 (sin marcha atras): universo de tokens del hijo nuevo MENOR que el del viejo (aviso critico 'UNIVERSO REDUCIDO', no activa) | BLANDOS: RESERVA, G arranque, otros Traceback"
  act "P6 (determinista) 1) UNA captura real AISLADA del capture_markets nuevo (p6_ciclo_aislado.py, dir temporal, sin tocar el repo) 2) el artefacto del PROXIMO ciclo real (hasta ${P6_ESPERA_S:-2400} s: errores de codigo, data/markets crece, sin adelanto_* con el adelanto apagado); y con --activar (+CONFIRMO_ADELANTO_6_MONEDAS=1) los cfg en $CFGDIR"
  act "marcha atras si P5/P6 falla: (retomar el lock de restart_ram) restaurar los .pre, borrar cfg y PARAR el capture_markets en curso si el adelanto estaba activo ; verify_deploy --restart observadores ; senales diferidas"
  log "Modo dry-run: no se cambio nada. fallos previos=$fallos. Log: $LOGF"; exit $((fallos>0))
fi
[ $fallos -eq 0 ] || { aviso_critico "ABORTO: comprobaciones previas fallidas ($fallos); nada modificado. Ver $LOGF"; exit 1; }
GP="$CFGDIR/gamma_pausa.json"; GP0=0; [ -e "$GP" ] && GP0=1                 # si NO existia antes del despliegue y existe al hacer la marcha atras, lo creo el codigo nuevo
CP_CURSO=""; CP_HECHOS=""
# C: copia ATOMICA a main (un proceso que importe el fichero a mitad nunca ve una copia parcial): cp a un temporal en el MISMO directorio (mismo filesystem) + mv -f (rename atomico). Conserva
# el modo del destino previo (si existe). Ante cualquier fallo borra el temporal y devuelve 1 (main intacto). La marcha atras usa lo mismo (rest_uno).
cp_atomico() {   # $1 origen  $2 destino
  local tmp; tmp="$2.deltatmp.$$"
  cp "$1" "$tmp" && { [ ! -e "$2" ] || chmod --reference="$2" "$tmp" 2>/dev/null || true; } && mv -fT "$tmp" "$2" || { rm -f "$tmp"; return 1; }
}
cp_main() {      # $1 = nombre (io|cap|libro) $2 = objetivo $3 = main. CP_CURSO marca el cp a medias (senal/fallo: main puede quedar a medias y SI hay que restaurarlo)
  CP_CURSO=$1; cp_atomico "$2" "$3" || return 1; CP_CURSO=""; CP_HECHOS="$CP_HECHOS $1"
}
# #8: restaura UN fichero de main SOLO si sigue siendo lo que desplego este script (sha == objetivo) o su cp quedo a medias; si ya es la base no hace nada; si cambio por otra mano NO lo
# pisa: RB_OK=0 + aviso critico (restaurar lo demas sigue). $1 nombre  $2 main  $3 objetivo  $4 .pre (vacio = la base es AUSENTE: se borra).
rest_uno() {
  local n=$1 m=$2 t=$3 pre=$4 s ok=0 hecho=0
  case " $CP_HECHOS " in *" $n "*) hecho=1;; esac
  [ "$CP_CURSO" = "$n" ] || [ $hecho -eq 1 ] || return 0                  # no se llego a tocar
  if [ -n "$pre" ]; then s=$(sha "$m"); else s=$([ -e "$m" ] && sha "$m"); fi
  if [ "$CP_CURSO" = "$n" ] || [ "$s" = "$(sha "$t")" ]; then
    if [ -n "$pre" ]; then cp_atomico "$pre" "$m" && [ "$(sha "$m")" = "$(sha "$pre")" ] && ok=1; else rm -f "$m"; [ ! -e "$m" ] && ok=1; fi
    [ $ok -eq 1 ] || { RB_OK=0; RB_DET="${RB_DET}$n: no se pudo restaurar la base; "; }
  elif { [ -n "$pre" ] && [ "$s" = "$(sha "$pre")" ]; } || { [ -z "$pre" ] && [ -z "$s" ]; }; then :   # ya es la base
  else
    RB_OK=0; RB_DET="${RB_DET}main/$n CAMBIO tras el despliegue (sha ${s:0:12}): NO se pisa, revisar a mano; "
    aviso_critico "marcha atras: main/$n cambio por otra mano tras el despliegue (sha ${s:0:12} no es el objetivo ni la base): NO se restaura; el resto si"
  fi
}
restaurar_ficheros() {       # lo especifico de v3 (la marcha atras compartida esta en lib_espera_hijos.sh::restaurar). RB_ALCANCE=captura: solo capture_markets (ver restaurar)
  local cfg_previo=0
  { [ -e "$CFGDIR/cfg_CAPTURE_5M_HORIZONTE_MIN" ] || [ -e "$CFGDIR/cfg_CAPTURE_429_FIX" ]; } && cfg_previo=1
  rest_uno cap "$M_CAP" "$T_CAP" "$PRE/capture_markets.py.pre"
  if [ "$RB_ALCANCE" != captura ]; then
    rest_uno libro "$M_LIBRO" "$T_LIBRO" "$PRE/libro_estado_ws.py.pre"
    rest_uno io "$M_IO" "$T_IO" ""
  fi
  revertir_cfg                      # SOLO los cfg que escribio este despliegue (manifiesto), en orden inverso; los escritos a mano se quedan
  # L3: con el adelanto activo (cfg propio o escrito a mano), el capture_markets EN CURSO lo sigue haciendo hasta ~10 min (lee los cfg al importar): se para y se verifica que no escribe mas adelanto_*
  if [ $cfg_previo -eq 1 ]; then
    if parar_capture_en_curso; then log "marcha atras: $CAP_PARADA"; else RB_OK=0; RB_DET="${RB_DET}$CAP_PARADA; "; fi
  fi
  [ -e "$CFGDIR/cfg_CAPTURE_5M_HORIZONTE_MIN" ] && log "AVISO: queda un cfg_CAPTURE_5M_HORIZONTE_MIN escrito a mano en $CFGDIR (no lo escribio este despliegue: no se borra); con el codigo restaurado no tiene efecto"
}
# (d) gamma_pausa.json: estado de la pausa por 429 del libro NUEVO. Solo se borra en la marcha atras COMPLETA y DESPUES del reinicio (lib::restaurar llama a restaurar_post): con
# RB_ALCANCE=captura el libro nuevo sigue vivo y lo usa; borrarlo le haria olvidar la pausa y volver a golpear gamma durante el 429.
restaurar_post() {
  [ $GP0 -eq 0 ] && [ -e "$GP" ] || return 0
  if [ "$RB_ALCANCE" = captura ]; then log "marcha atras parcial: se CONSERVA $GP (lo creo el libro nuevo, que sigue vivo y lo usa)"
  else rm -f "$GP"; log "marcha atras: borrado $GP (lo creo el despliegue; el libro viejo ya esta de vuelta)"; fi
}
resumen_shas() { echo "sha256 libro=$(sha "$M_LIBRO" | cut -c1-16) capture=$(sha "$M_CAP" | cut -c1-16)"; }
trap_normales

log "== P2b siembra de la cache de tokens con el universo VIGENTE (como v5; BLANDO: si falla se sigue en frio), ANTES de la sincronia con el watchdog =="
P2B_B=${P2B_PRESUPUESTO_S:-240}
if screen -ls 2>/dev/null | grep -qE "[0-9]+\.(precierre|curvacierre)[[:space:]]" && [ "$P2B_B" -gt "${P2B_PRESUPUESTO_PRECIERRE_S:-60}" ]; then      # M7: gamma compartida con precierre (429 por IP)
  P2B_B=${P2B_PRESUPUESTO_PRECIERRE_S:-60}; log "AVISO (M7): precierre vivo y gamma-api compartida: presupuesto de peticiones de P2b reducido a ${P2B_B}s"; fi
if [ -f "$SEMBRAR_PY" ]; then
  REPO_SEMBRAR="$REPO" timeout $(( P2B_B + 60 )) "$PY" "$SEMBRAR_PY" --cache "$DL/libro_tokens_cache.json" --presupuesto-s "$P2B_B" 2>&1 | tee -a "$LOGF" | tail -n 4; rc_s=${PIPESTATUS[0]}
  [ "$rc_s" -eq 0 ] && log "OK    cache sembrada" || log "AVISO (blando): sembrar_cache_tokens salio con $rc_s (2 = gamma caida, 3 = fallo, 124 = timeout); el arranque sera en frio"
else log "AVISO (blando): no hay $SEMBRAR_PY; el arranque sera en frio"; fi
log "== P2 esperar un tick del watchdog =="
espera_tick_watchdog "$WDLOG" || { aviso_critico "ABORTO: el log del watchdog falta o lleva >900 s sin escribir (watchdog muerto?); nada modificado"; exit 1; }
sleep "${P2_SLEEP:-10}"
hm=$(hora_min)
hora_ok || { aviso_critico "ABORTO: tras la espera la hora ya no es valida; nada modificado"; exit 1; }
min_hasta_ventana "$hm"; [ "$MH" -ge "${P3_MARGEN_MIN:-10}" ] || { aviso_critico "ABORTO: tras las esperas (P2b/P2) queda menos de ${P3_MARGEN_MIN:-10} min hasta la ventana prohibida ($VENTANA en $MH min); nada modificado"; exit 1; }
base_ok || { aviso_critico "ABORTO por GUARDA DE BASE: algun main cambio mientras esperabamos; nada modificado. Ver $LOGF"; exit 1; }
espera_bnreg || { aviso_critico "ABORTO: bnreg sin latido fresco con el lock en ${P5_BN_S:-60} s; nada modificado"; exit 1; }
log "== P3 backup + cp =="
# .pre = la BASE: un .pre existente que ya es base no se sobrescribe; si main ya es el objetivo (despliegue parcial previo) se EXIGE un .pre base previo
e1=$(estado_libro); e2=$(estado_cap)
respaldar() {   # $1 main  $2 pre  $3 estado (base|ya)
  if [ "$3" = base ]; then cmp -s "$1" "$2" 2>/dev/null || cp "$1" "$2"; else [ -f "$2" ]; fi; }
respaldar "$M_LIBRO" "$PRE/libro_estado_ws.py.pre" "$e1" && respaldar "$M_CAP" "$PRE/capture_markets.py.pre" "$e2" || { aviso_critico "ABORTO: backup .pre fallido (o main ya es el objetivo y no hay .pre base); nada modificado"; exit 1; }
case "$(sha "$PRE/libro_estado_ws.py.pre")" in "$BASE_LIBRO_ORIG"|"$BASE_LIBRO_V5"*) ;; *) aviso_critico "ABORTO: libro_estado_ws.py.pre no es una base conocida; nada modificado"; exit 1;; esac
case "$(sha "$PRE/capture_markets.py.pre")" in "$BASE_CAP"*) ;; *) aviso_critico "ABORTO: capture_markets.py.pre no es la base; nada modificado"; exit 1;; esac
rm -f "$PRE/universo_5m_io.py.pre"      # la base de universo_5m_io es AUSENTE
TSB=$(date -u +%Y%m%dT%H%M%SZ)          # (e) copia con sello horario del arbol de trabajo de main (nunca se sobrescribe; commiteado o no)
for f in libro_estado_ws.py capture_markets.py; do
  [ ! -e "$REPO/$f" ] || cp -p "$REPO/$f" "$PRE/$f.main_$TSB" || { aviso_critico "ABORTO: no se pudo copiar $f a $PRE/$f.main_$TSB; nada modificado"; exit 1; }
done
log "copias del arbol de trabajo de main (libro/capture) en $PRE/*.main_$TSB"
off0=$(stat -c %s "$LOGOBS" 2>/dev/null || echo 0); viejos=$(hijos_vivos); cap_pre=$(_ps_cap)
log_previo=$(head -c "$off0" "$LOGOBS" 2>/dev/null | tail -c 3000000)          # A: log hasta el reinicio (para los tokens del hijo viejo)
EN_VUELO=1
cp_main io "$T_IO" "$M_IO" && cp_main cap "$T_CAP" "$M_CAP" && cp_main libro "$T_LIBRO" "$M_LIBRO" || die "cp fallido"
"$PY" -m py_compile "$M_IO" "$M_CAP" "$M_LIBRO" || die "py_compile de main fallo tras el cp"
P6_MARCA_TS=$(date +%s); P6_MARCA_OFF=$(stat -c %s "$SLOWLOG" 2>/dev/null || echo 0); P6_M0=$(snap_markets); P6_A0=$(adelanto_firma)      # H7: bases de data/markets y adelanto_* tomadas en la marca (antes de que arranque el ciclo nuevo)      # marca del cp: un ciclo de capture_markets solo es "el nuevo" si arranca DESPUES (lib::verifica_capture)
log "== P4 reinicio de observadores (verify_deploy) =="
vd_out="$PRE/vd_out_$$.txt"
(cd "$REPO" && "$PY" verify_deploy.py --restart observadores) > "$vd_out" 2>&1; rc_vd=$?
cat "$vd_out" >> "$LOGF"; tail -n 12 "$vd_out"
if [ $rc_vd -ne 0 ]; then
  espera_screen observadores && log "AVISO (blando): verify_deploy salio con $rc_vd pero la screen observadores existe" || die "DURO: verify_deploy fallo ($rc_vd) y no hay screen observadores"; fi
log "== P5 comprobaciones =="
ok_conn=0; for i in $(seq 1 "${P5_CONN_S:-180}"); do [ "$(nuevos_pids | wc -l)" -ge 1 ] && { ok_conn=1; break; }; sleep 1; done
[ $ok_conn -eq 1 ] || die "DURO: ningun 'conectado [' de un hijo NUEVO en ${P5_CONN_S:-180} s"
espera_hijos || die "DURO: $ESPERA_MOTIVO"
hijo=$HIJO
nuevo=$(log_nuevo)
tb=$(traceback_fatal "$nuevo" 'libro_estado_ws|universo_5m_io|websockets') && log "AVISO (DURO solo si el hijo final deja de escribir libro5_ms o hay respawn): Traceback no de apagado: $(echo "$tb" | head -n 6 | tr '\n' '|')"
espera_bnreg || die "DURO: bnreg sin latido fresco con el lock en toda la ventana de ${P5_BN_S:-60} s (o perdio el lock)"
echo "$nuevo" | grep -a -q "RESERVA" && log "OK    el hijo nuevo dice RESERVA de Binance" || log "AVISO (blando): sin linea RESERVA (bnreg es dueno: comprobado)"
echo "$nuevo" | grep -a -c "refresco de universo fall" | grep -qx 0 || log "AVISO (blando): 'refresco de universo fallo' en el log nuevo"
g_ok=0
for i in $(seq 1 $(( (${P5_G_S:-60} + 2) / 3 ))); do f5=$(f5_de "$hijo"); if [ -f "$f5" ] && zcat "$f5" 2>/dev/null | head -n 200 | awk -F, '$1=="G" && $4 ~ /arranque/ {f=1} END{exit !f}'; then g_ok=1; break; fi; sleep 3; done
[ $g_ok -eq 1 ] && log "OK    fila G arranque visible en $f5" || log "AVISO (blando): G arranque aun no visible en $f5"
cap_ok "$REPO" || die "DURO: el capture_markets de main (codigo nuevo, cfg vacio) no queda apagado por cfg tras el despliegue: $CAP_OK_MOTIVO"
verif_final "$hijo" || die "DURO: $ESPERA_MOTIVO"            # al FINAL: mismo hijo, sin respawn, 'conectado [' releido, libro5 creciendo
P5_VERIFICADO=1                  # observadores verificado sano con libro/io nuevos: una marcha atras posterior en ventana prohibida ya no lo reinicia (lib::restaurar)
nuevo=$(log_nuevo); tb=$(traceback_fatal "$nuevo" 'libro_estado_ws|universo_5m_io|websockets') && log "AVISO: Traceback no de apagado releido al final (libro5 crece: sin marcha atras): $(echo "$tb" | head -n 6 | tr '\n' '|')"
nt=$(echo "$nuevo" | grep -a -c "Traceback"); [ "$nt" -eq 0 ] || log "AVISO (blando): $nt Traceback(s) en el log nuevo (apagados de hijos viejos o de otros modulos; revisar a mano)"
# A: universo del hijo nuevo vs el viejo. Un universo MENOR no es un fallo del codigo (el hijo arranca en frio y crece al refrescar; lo viejo se comparo a sus ultimos tokens): NO marcha atras, pero
# NUNCA pasa en silencio: rc 4 'universo reducido' + aviso critico (decide la sesion principal) y --activar no se aplica.
UNIV_RED=0; compara_tokens "$log_previo" "$nuevo" "$hijo" "$viejos" || UNIV_RED=1
if [ $UNIV_RED -ne 0 ]; then log "AVISO (rc 4): $TOK_DET"
elif [ "${TOK_SINREF:-0}" = 1 ]; then log "AVISO: $TOK_DET"
else log "OK    universo del hijo nuevo >= viejo (5min con tolerancia ${TOK_TOL_5M:-2} sobre el maximo viejo): $TOK_DET"; fi
ntb=$(printf '%s\n' "$tb" | grep -a -c '^Traceback' || true)        # bloques Traceback propios (libro_estado_ws|universo_5m_io|websockets) no de apagado, releidos al final
if [ $SUSTITUYE -eq 1 ]; then
  (cd "$REPO" && "$PY" verify_deploy.py --restart vigiasfreq) > "$PRE/vd_out_vf_$$.txt" 2>&1; rc_vf=$?; cat "$PRE/vd_out_vf_$$.txt" >> "$LOGF"
  [ $rc_vf -eq 0 ] && log "OK    vigiasfreq reiniciada (sustituye el reinicio de restart_ram)" || log "AVISO (blando): reinicio de vigiasfreq rc=$rc_vf; revisar a mano"
fi
liberar_lock          # libera el lock de restart_ram antes de la espera larga de P6 (restaurar() lo RETOMA si hace falta)
log "== P6 verificacion DETERMINISTA del capture_markets nuevo (run_slow.sh lo lanza con '|| true': un fallo no se ve en ningun sitio) =="
r_ais=3; P6_AIS=""
# M2: la captura aislada (peor caso: intentos x (timeout + pausa)) tampoco puede cruzar la proxima ventana prohibida (+ P6_MARGEN_S): si no cabe se OMITE con aviso (queda el ciclo real si cabe)
peor_ais=$(( ${P6_AIS_INTENTOS:-3} * (${P6_AIS_TIMEOUT:-240} + ${P6_AIS_PAUSA:-70}) )); min_hasta_ventana "$(hora_min)"
if [ "${P6_AISLADO:-1}" != 1 ]; then :
elif [ $(( MH * 60 - peor_ais )) -lt "${P6_MARGEN_S:-300}" ]; then
  log "AVISO P6: captura aislada OMITIDA: peor caso ${peor_ais}s y la proxima ventana prohibida ($VENTANA) empieza en ${MH} min (< peor caso + margen ${P6_MARGEN_S:-300}s)"; P6_AISLADO=0
else p6_aislado; r_ais=$?; P6_AIS=$CAP_MOTIVO; fi
case $r_ais in 0) AIS_TXT="ok";; 1) AIS_TXT="FALLO";; 2) AIS_TXT="inconclusa";; *) AIS_TXT="omitida (no cabe antes de la ventana prohibida o P6_AISLADO=0)";; esac   # #8
case $r_ais in
  1) die "DURO: P6 captura aislada del codigo nuevo: $P6_AIS";;
  0) log "OK    P6 captura real AISLADA del codigo nuevo: $P6_AIS";;
  2) log "AVISO P6: captura aislada INCONCLUSA (429/red en todos los intentos): $P6_AIS; se confia en el ciclo real";;
  *) log "AVISO P6: captura aislada omitida (P6_AISLADO=0)";;
esac
NOVERIF=0; ACT_DIFERIDA=0; ACT_FALLO=0; ACT_HECHO=0; : "${UNIV_RED:=0}"
# #7: el ciclo real de P6 se ACOTA para no cruzar una ventana prohibida: espera = min(P6_ESPERA_S, tiempo hasta la ventana - P6_CICLO_S - P6_MARGEN_S (300)); <= 0 => se omite
# (queda la captura aislada). Asi ni la verificacion ni su eventual marcha atras ni la activacion caen dentro de una ventana.
esp6=${P6_ESPERA_S:-2400}; min_hasta_ventana "$(hora_min)"; mh=$MH; vent6=$VENTANA; lim6=$(( mh * 60 - ${P6_CICLO_S:-900} - ${P6_MARGEN_S:-300} ))
if [ "$esp6" -gt 0 ] && [ "$lim6" -lt "$esp6" ]; then
  if [ "$lim6" -le 0 ]; then log "AVISO P6: ciclo real OMITIDO: la proxima ventana prohibida ($vent6) empieza en ${mh} min (< ciclo + margen)"; esp6=0
  else log "AVISO P6: ciclo real ACOTADO a ${lim6}s (en vez de ${esp6}s): la proxima ventana prohibida ($vent6) empieza en ${mh} min"; esp6=$lim6; fi
fi
if [ "$esp6" -gt 0 ]; then
  P6_ESPERA_S=$esp6 verifica_capture "$SLOWLOG"; rc6=$?
  if [ $rc6 -eq 1 ]; then die "DURO: P6 ciclo real: $CAP_MOTIVO"
  elif [ $rc6 -eq 0 ]; then log "OK    P6 ciclo real de capture_markets con el codigo nuevo: sin error de codigo, data/markets CRECE, sin adelanto con el adelanto apagado"; P6_RES="ok (aislado: $AIS_TXT + ciclo real con crecimiento)"
  elif [ $r_ais -eq 0 ]; then log "AVISO P6: $CAP_MOTIVO; verificado por la captura aislada"; P6_RES="ok (aislado; ciclo real no observado)"
  else log "AVISO P6: $CAP_MOTIVO y la captura aislada $AIS_TXT; el codigo nuevo se queda desplegado (sin marcha atras): mirar logs/slow.log a mano"; P6_RES="NO VERIFICADO (ciclo real: crecimiento no verificado; captura aislada $AIS_TXT)"; NOVERIF=1; fi
else
  log "AVISO: P6 ciclo real omitido (P6_ESPERA_S=0 o ventana prohibida inminente)"; [ $r_ais -eq 0 ] && P6_RES="ok (solo aislado)" || { P6_RES="NO VERIFICADO (ciclo real omitido; captura aislada $AIS_TXT)"; NOVERIF=1; }
fi
if [ "${P6_INTERMITENTE:-0}" = 1 ] && [ "$r_ais" -eq 0 ]; then       # M3: rc 4 + aviso critico (no mudo); no bloquea el despliegue ni hace marcha atras
  log "AVISO P6: ${P6_INTERMITENTE_TXT:-error de codigo intermitente}"; P6_RES="NO VERIFICADO (error de codigo INTERMITENTE en la captura aislada, no se repitio: ${P6_INTERMITENTE_TXT:-?}; $P6_RES)"; NOVERIF=1
fi
if [ $ACTIVAR -eq 1 ]; then
  if [ $NOVERIF -eq 1 ]; then log "AVISO: --activar NO aplicado: P6 sin veredicto (el codigo nuevo no esta verificado); activar a mano tras revisar"
  elif [ $UNIV_RED -eq 1 ]; then log "AVISO: --activar NO aplicado: universo de tokens REDUCIDO respecto al hijo viejo ($TOK_DET); decidir a mano"
  elif ventana_de "$(hora_min)"; then log "AVISO: --activar NO aplicado: estamos dentro de una ventana prohibida ($VENTANA); activar a mano en ventana libre (CONFIRMO_ADELANTO_6_MONEDAS=1 y re-lanzar con --ejecutar --activar: ya desplegado => solo escribe los cfg)"; ACT_DIFERIDA=1
  elif activar_cfg; then ACT_HECHO=1
  else ACT_FALLO=1; fi       # sin CONFIRMO_ADELANTO_6_MONEDAS=1 (o cfg no escribible): decision pendiente => rc 4 + aviso critico, nunca un rc 0 silencioso
else log "NO activado (sin --activar): el codigo nuevo se comporta como main hasta que existan los cfg"; fi
EN_VUELO=0
log "OK: desplegado. libro=$(sha "$M_LIBRO" | cut -c1-16) capture=$(sha "$M_CAP" | cut -c1-16) io=$(sha "$M_IO" | cut -c1-16); .pre en $PRE; hijo pid $hijo; P6=$P6_RES"
# I1: las dos decisiones pendientes NUNCA pasan en silencio: aviso critico (Telegram + aviso_log) ademas del log.
[ $NOVERIF -eq 0 ] || aviso_critico "DESPLEGADO SIN VERIFICAR (rc 4): P6=$P6_RES; el codigo nuevo queda en main sin veredicto de capture_markets: revisar logs/slow.log y decidir (marcha atras a mano o aceptar)$([ $ACTIVAR -eq 1 ] && echo "; --activar NO aplicado")"
[ $ACT_DIFERIDA -eq 0 ] || aviso_critico "--activar DIFERIDO (rc 4): desplegado y verificado pero la hora cae en una ventana prohibida; activar a mano en ventana libre (CONFIRMO_ADELANTO_6_MONEDAS=1, --ejecutar --activar)"
[ $ACT_FALLO -eq 0 ] || aviso_critico "--activar NO APLICADO (rc 4): activar_cfg no escribio los cfg (falta CONFIRMO_ADELANTO_6_MONEDAS=1 o cfg no escribible; ver $LOGF); el codigo nuevo queda desplegado con el adelanto APAGADO"
[ $UNIV_RED -eq 0 ] || aviso_critico "DESPLEGADO CON UNIVERSO REDUCIDO (rc 4): $TOK_DET; el hijo nuevo conecta con menos tokens que el viejo (arranque en frio o refresco pendiente): vigilar 'refresco de universo' y decidir (marcha atras a mano o aceptar)$([ $ACTIVAR -eq 1 ] && echo "; --activar NO aplicado")"
[ $NOVERIF -eq 0 ] && [ $ACT_DIFERIDA -eq 0 ] && [ $ACT_FALLO -eq 0 ] && [ $UNIV_RED -eq 0 ] || exit 4
# Exito (rc 0): aviso 'DESPLIEGUE OK' con el resumen (tambien con P6 'aislado; ciclo real no observado').
aviso_ok "DESPLIEGUE OK (rc 0): sha libro=$(sha "$M_LIBRO" | cut -c1-16) capture=$(sha "$M_CAP" | cut -c1-16) io=$(sha "$M_IO" | cut -c1-16); hijo nuevo pid $hijo; universo $TOK_DET; Tracebacks no fatales de libro_estado_ws/universo/websockets en el log nuevo: $ntb (el libro5 crece: sin reversion); P6=$P6_RES; $([ $ACT_HECHO -eq 1 ] && echo 'ADELANTO ACTIVADO (cfg escritos; efecto en el siguiente ciclo de capture_markets)' || echo 'FALTA ACTIVAR: el adelanto sigue APAGADO (relanzar con --ejecutar --activar y CONFIRMO_ADELANTO_6_MONEDAS=1)'); .pre en $PRE"      # desplegado pero con una decision pendiente (P6 sin veredicto o --activar diferido por ventana): ni OK ni marcha atras (decide la sesion principal)
