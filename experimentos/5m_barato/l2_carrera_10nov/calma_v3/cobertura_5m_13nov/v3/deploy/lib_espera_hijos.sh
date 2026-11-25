# lib_espera_hijos.sh -- funciones de P5/P6, ventanas horarias, cfg de activacion y marcha atras de deploy_deltas_libro_ws_once.sh (se hace 'source' de una COPIA cuyo
# sha256 se comprueba contra v3/SHA256SUMS ANTES de cargarla; el script v3 es el unico despliegue vigente: el v5 quedo como un wrapper que no ejecuta).
# Requiere: REPO, LOGOBS, LIBRO5, PY, LOGF, log(), y (segun la funcion) $viejos y $off0 ya capturados ANTES del reinicio.
# Carrera 13-Nov 21:15Z: tras verify_deploy --restart la comprobacion "solo vive el hijo nuevo" vio 3 pids que NO eran hijos de observadores
# (0 lineas en logs/observadores_fase0.log; ver cabecera de los scripts): ahora un hijo cuenta SOLO si es hijo de observadores_fase0.py.

# "pid ppid obs" de cada proceso 'libro_estado_ws.py --hijo' de la RUTA de ESTE repo; obs=1 si su padre es observadores_fase0.py (un hijo de otra
# cosa -- harness, medicion, worktree dev -- tiene obs=0 y se ignora). El patron se arma dentro del awk (la linea del propio awk no lo contiene).
_ps_hijos() {
  ps -eo pid,ppid,args | awk -v r="$REPO" '
    { n = split($0, f, " "); k = f[1]; ln[NR] = k; pp[k] = f[2]; ar[k] = $0 }
    END { for (i = 1; i <= NR; i++) { k = ln[i]
            if (index(ar[k], r "/libro_estado_ws.py --hijo")) print k, pp[k], ((ar[pp[k]] ~ /(^| |\/)observadores_fase0\.py( |$)/) ? 1 : 0) } }'
}
# #9: el padre es observadores si SU linea de comandos lleva observadores_fase0.py en CUALQUIER posicion (envuelto en choom/nice/bash -c, con flags...), no solo
# como ultimo campo. Diagnostico de los hijos del repo cuyo padre NO se reconoce (para P0/espera_hijos: fallo explicito y claro en vez de un falso aborto).
diag_padres() {
  ps -eo pid,ppid,args | awk -v r="$REPO" '
    { k = $1; ln[NR] = k; pp[k] = $2; ar[k] = $0 }
    END { for (i = 1; i <= NR; i++) { k = ln[i]
            if (index(ar[k], r "/libro_estado_ws.py --hijo") && !(ar[pp[k]] ~ /(^| |\/)observadores_fase0\.py( |$)/)) { a = ar[pp[k]]; sub(/^ *[0-9]+ +[0-9]+ +/, "", a); print "hijo " k " padre " pp[k] ": " substr(a, 1, 120) } } }'
}

# Hijos lectores VIVOS de observadores (espacio-separados, sin espacio final). Para capturar $viejos antes del reinicio y para "hay hijo vivo".
hijos_vivos() { _ps_hijos | awk '$3 == 1 {print $1}' | sort -n | paste -sd' '; }
es_viejo() { case " $viejos " in *" $1 "*) return 0;; esac; return 1; }

# Log de observadores desde $off0; si el log desaparecio (0) o se ROTO (tamano actual < off0) se relee desde 0.
log_nuevo() { local sz off; sz=$(stat -c %s "$LOGOBS" 2>/dev/null || echo 0); off=${off0:-0}; [ "$sz" -lt "$off" ] && off=0; tail -c +$((off + 1)) "$LOGOBS" 2>/dev/null; }
# pids de las lineas 'conectado [' / 'lector hijo lanzado (pid N)' del log nuevo que NO eran viejos.
nuevos_pids() { log_nuevo | grep -a "conectado \[" | grep -ao "pid [0-9]*" | awk '{print $2}' | sort -u | grep -vxFf <(printf '%s\n' $viejos); }
lanzados_pids() { log_nuevo | grep -a "lector hijo lanzado (pid " | grep -ao "pid [0-9]*" | awk '{print $2}' | sort -u | grep -vxFf <(printf '%s\n' $viejos); }

# Tracebacks REALES de los modulos $2 (ERE) en el texto $1. Se ignoran los de apagado (KeyboardInterrupt/SystemExit/SIGTERM/BrokenPipeError): un hijo viejo
# que muere tras el reinicio los escribe en el mismo log (sin pid, no se pueden atribuir). Imprime el bloque y devuelve 0 si hay alguno real.
# Un Traceback real es solo AVISO: el DURO es que el hijo final deje de escribir libro5 (libro5_crece) o haya respawn.
traceback_fatal() {
  printf '%s\n' "$1" | awk -v re="$2" '
    function fin() { if (inb && hit && exc !~ /^(builtins\.)?(KeyboardInterrupt|SystemExit|SIGTERM|BrokenPipeError)/) { print blk; fatal = 1 } inb = 0 }
    /^Traceback \(most recent call last\)/ { if (!inb) { inb = 1; hit = 0; blk = ""; exc = "" } blk = blk $0 "\n"; next }
    inb && /^[ \t]/ { blk = blk $0 "\n"; if ($0 ~ re) hit = 1; next }
    inb && /^(During handling of the above exception|The above exception was the direct cause)/ { blk = blk $0 "\n"; next }
    inb { exc = $0; blk = blk $0 "\n"; fin(); next }
    END { fin(); exit (fatal ? 0 : 1) }'
}

# Espera SOSTENIDA: de forma continuada durante P5_ESTABLE_S s (30) ningun hijo viejo vivo y EXACTAMENTE 1 hijo nuevo (hijo de observadores, no viejo).
# Viejos/nuevos por CONJUNTO de pids previo ($viejos), no por cuenta; un proceso ajeno (otro padre) se ignora. Plazo total P5_MUEREN_S (90) + estable.
# Cualquier segundo hijo nuevo visto (respawn del hijo o duplicado) es DURO inmediato. Los viejos que siguen vivos P5_TERM_S s (30) tras el reinicio y cuyo
# padre ya NO es un observadores (huerfanos) reciben SIGTERM, y SIGKILL tras P5_KILL_GRACIA s (20); un viejo cuyo padre sigue siendo observadores NO se
# toca (lo apaga su padre). 0 = ok, $HIJO = su pid y $HIJO_PPID = el observadores nuevo; 1 = fallo (motivo en $ESPERA_MOTIVO).
espera_hijos() {
  local plazo=${P5_MUEREN_S:-90} estable=${P5_ESTABLE_S:-30} paso=${P5_PASO:-2} term=${P5_TERM_S:-30} gracia=${P5_KILL_GRACIA:-20}
  local t0=$SECONDS ts="" tt="" el snap k pp ob vv nv nvp vvi vistos="" n=0 e v dp
  HIJO=""; HIJO_PPID=""
  while :; do
    snap=$(_ps_hijos); vv=""; nv=""; nvp=""; vvi=""
    while read -r k pp ob; do
      [ -n "$k" ] || continue
      if es_viejo "$k"; then vv="${vv:+$vv }$k"; vvi="$vvi $k:$pp:$ob"
      elif [ "$ob" = 1 ]; then nv="${nv:+$nv }$k"; nvp=$pp; fi
    done <<< "$snap"
    for k in $nv; do case " $vistos " in *" $k "*) ;; *) vistos="${vistos:+$vistos }$k";; esac; done
    if [ "${vistos#* }" != "$vistos" ]; then
      ESPERA_MOTIVO="RESPAWN del hijo o hijo extra: hijos nuevos vistos '$vistos' (debe haber exactamente 1 y no cambiar); vivos ahora: nuevos '$nv', viejos '$vv'"; return 1
    fi
    el=$((SECONDS - t0))
    if [ -n "$vv" ] && [ -n "$nvp" ] && [ "$el" -ge "$term" ]; then       # escalada SOLO a viejos huerfanos (su padre ya no es observadores)
      for e in $vvi; do k=${e%%:*}; v=${e#*:}; pp=${v%%:*}; ob=${v##*:}
        [ "$ob" = 0 ] && [ "$pp" != "$nvp" ] || continue
        if [ -z "$tt" ]; then tt=$SECONDS; log "  P5: hijo viejo huerfano $k sigue vivo tras ${el}s: SIGTERM"; kill -TERM "$k" 2>/dev/null
        elif [ $((SECONDS - tt)) -ge "$gracia" ]; then log "  P5: hijo viejo huerfano $k sigue vivo tras la gracia: SIGKILL"; kill -KILL "$k" 2>/dev/null
        else kill -TERM "$k" 2>/dev/null; fi
      done
    fi
    if [ -z "$vv" ] && [ -n "$nv" ]; then
      [ -z "$ts" ] && ts=$SECONDS; HIJO=$nv; HIJO_PPID=$nvp
      [ $((SECONDS - ts)) -ge "$estable" ] && return 0
    else ts=""; fi
    if [ "$el" -ge $((plazo + estable)) ]; then
      ESPERA_MOTIVO="no hay EXACTAMENTE 1 hijo lector nuevo vivo, sin viejos, de forma sostenida ${estable}s en ${el}s: viejos aun vivos '$vv'; hijos nuevos vivos '$nv'$([ -z "$nv" ] && echo ' = 0 hijos'); viejos previos '$viejos'"
      [ -z "$nv" ] && { dp=$(diag_padres | head -n 3 | tr '\n' '|'); [ -n "$dp" ] && ESPERA_MOTIVO="$ESPERA_MOTIVO; hijos del repo con padre NO reconocido como observadores_fase0.py: $dp"; }
      return 1
    fi
    n=$((n + 1)); [ $((n % 10)) -eq 1 ] && log "  P5: esperando (viejos vivos '$vv', nuevos vivos '$nv'), ${el}s/$((plazo + estable))s"
    sleep "$paso"
  done
}

# bnreg: basta UN latido fresco con el lock dentro de una ventana (P5_BN_S, 60 s) con reintentos. Fallo solo si no hay ninguno en toda la ventana
# (o bnreg perdio el lock de forma sostenida). Requiere bn_estado_ok y bn_es_duenyo del script.
espera_bnreg() {
  local plazo=${1:-${P5_BN_S:-60}} t0=$SECONDS
  while :; do
    bn_estado_ok activo 15 && bn_es_duenyo && return 0
    [ $((SECONDS - t0)) -ge "$plazo" ] && return 1
    sleep "${P5_PASO:-2}"
  done
}

# #7: los ficheros libro5_ms del hijo se identifican por su PID (libro5_ms_<fecha>_<pid>.csv.gz), NO por `date -u +%F` de ahora: un despliegue que cruce 00:00Z no da
# falso fallo (el hijo abre el fichero del dia nuevo). _f5_estado = "n_ficheros bytes_totales mtime_max" de TODAS las fechas de ese pid.
_f5_estado() {
  local f n=0 sz=0 mt=0 s m
  for f in "$LIBRO5"/libro5_ms_*_"$1".csv.gz; do [ -e "$f" ] || continue
    n=$((n + 1)); s=$(stat -c %s "$f" 2>/dev/null || echo 0); m=$(stat -c %Y "$f" 2>/dev/null || echo 0); sz=$((sz + s)); [ "$m" -gt "$mt" ] && mt=$m
  done
  echo "$n $sz $mt"
}
# libro5_ms del hijo $1 (PID, todas las fechas) CRECE (cualquier fila -- G arranque, B, T o d --; mtime, tamano o fichero nuevo) dentro de $2 s (P5_CRECE_S, 90).
# No depende de filas d.
libro5_crece() {
  local a=$1 plazo=${2:-${P5_CRECE_S:-90}} t0=$SECONDS s0 s1 m0 m1 n0 n1
  read -r n0 s0 m0 <<< "$(_f5_estado "$a")"
  while [ $((SECONDS - t0)) -lt "$plazo" ]; do
    sleep "${P5_PASO:-2}"; read -r n1 s1 m1 <<< "$(_f5_estado "$a")"
    { [ "$n1" -gt "$n0" ] || [ "$s1" -gt "$s0" ] || [ "$m1" -gt "$m0" ]; } && return 0
  done
  return 1
}
# Fichero MAS ANTIGUO del pid (el que lleva la fila G de arranque); si aun no existe, el nombre con la fecha de hoy (solo para mensajes).
f5_de() { local f; f=$(ls -tr "$LIBRO5"/libro5_ms_*_"$1".csv.gz 2>/dev/null | head -n1); [ -n "$f" ] && echo "$f" || echo "$LIBRO5/libro5_ms_$(date -u +%F)_$1.csv.gz"; }

# L5: el lock de Binance lo tiene tomado el pid $1 -- lectura de /proc/locks, SIN adquirirlo (una sonda de adquisicion podria quitarselo a bnreg si lo libera o retoma
# en ese instante). $2 = fichero de lock.
lock_tomado_por() {
  local ino; ino=$(stat -c %i "$2" 2>/dev/null) || return 1
  awk -v p="$1" -v i="$ino" '$2 == "FLOCK" && $5 == p { n = split($6, a, ":"); if (a[n] == i) f = 1 } END { exit !f }' /proc/locks 2>/dev/null
}

# A: tokens por clave de las lineas '[..] conectado [K], N tokens (lector en proceso separado, pid P)' del texto $1 (stdin si vacio): el ULTIMO N de cada clave K, solo de los pids de $2 (espacio-
# separados; vacio = todos). Imprime 'K N' por linea. Una linea sin 'N tokens' (o sin pid cuando se filtra por pid) no cuenta: sin dato = sin comparacion, nunca 0.
tokens_conectados() {
  awk -v pids=" ${2:-} " -v modo="${3:-}" 'index($0, "conectado [") { l = $0; k = l; sub(/^.*conectado \[/, "", k); sub(/\].*$/, "", k)
      if (!match(l, /\], [0-9]+ tokens/)) next; n = substr(l, RSTART + 3, RLENGTH - 3); sub(/ tokens.*$/, "", n)
      if (pids != "  ") { if (!match(l, /pid [0-9]+\)/)) next; p = substr(l, RSTART + 4, RLENGTH - 5); if (index(pids, " " p " ") == 0) next }
      if (modo == "max" && (k in v) && n + 0 <= v[k] + 0) next; v[k] = n } END { for (k in v) print k, v[k] }'
}
# A: compara el universo del hijo NUEVO ($2 = texto de log nuevo, $3 = pid nuevo) con el del viejo ($1 = texto de log anterior, $4 = pids viejos). 0 = igual o mayor / sin referencia (TOK_SINREF=1); 1 = REDUCIDO.
# R1: las claves 5min ROTAN con los mercados (hijo viejo 6 tokens a las 10:20 y 8 a las 11:07 en el mismo pid): comparar el ultimo N daba falsos 'REDUCIDO'. Para *#5min se compara contra el MAXIMO que el
# hijo viejo imprimio en la ventana con tolerancia TOK_TOL_5M (2): reducido si nuevo < max(1, max_viejo - 2) (fail-loud: una moneda 'ausente' o una caida >2 sigue avisando; un 6 vs 8 no). 15m/60m/240m (universo
# estable): estricto contra el ULTIMO N, como antes. Deja el detalle en TOK_DET.
compara_tokens() {
  local old oldmax new k n o m mx red="" tol=${TOK_TOL_5M:-2}; TOK_SINREF=0
  old=$(printf '%s\n' "$1" | tokens_conectados "" "$4"); oldmax=$(printf '%s\n' "$1" | tokens_conectados "" "$4" max); new=$(printf '%s\n' "$2" | tokens_conectados "" "$3"); TOK_DET=""
  [ -n "$old" ] || { TOK_SINREF=1; TOK_DET="SIN REFERENCIA de tokens del hijo viejo en el log (no se compara: universo NO verificado)"; return 0; }
  [ -n "$new" ] || { TOK_DET="el hijo nuevo no imprimio 'N tokens' (no se puede comparar)"; return 1; }
  while read -r k o; do
    n=$(printf '%s\n' "$new" | awk -v k="$k" '$1 == k {print $2}')
    if [ -z "$n" ]; then red="$red $k:$o->ausente"; continue; fi
    case $k in
      *#5min) mx=$(printf '%s\n' "$oldmax" | awk -v k="$k" '$1 == k {print $2}'); mx=${mx:-$o}; m=$(( mx - tol )); [ "$m" -ge 1 ] || m=1
              [ "$n" -ge "$m" ] || red="$red $k:$mx->$n(minimo $m = max_viejo-$tol)";;
      *) [ "$n" -ge "$o" ] || red="$red $k:$o->$n";;
    esac
  done <<< "$old"
  TOK_DET="viejo[$(printf '%s' "$old" | tr '\n' ';')] viejo_max[$(printf '%s' "$oldmax" | tr '\n' ';')] nuevo[$(printf '%s' "$new" | tr '\n' ';')]"
  [ -z "$red" ] || { TOK_DET="universo REDUCIDO:$red; $TOK_DET"; return 1; }
  return 0
}
# Verificacion FINAL (se llama DESPUES de todas las esperas, con el log releido): el mismo y unico hijo vivo, sin viejos, sin respawn ('conectado [' y
# 'lector hijo lanzado' de UN solo pid nuevo) y su libro5_ms crece. 0 = ok; 1 = fallo (motivo en $ESPERA_MOTIVO).
verif_final() {
  local hijo=$1 n l
  P5_ESTABLE_S=0 P5_MUEREN_S=0 espera_hijos || return 1
  [ "$HIJO" = "$hijo" ] || { ESPERA_MOTIVO="al final el hijo nuevo es $HIJO y no $hijo (respawn durante P5)"; return 1; }
  n=$(nuevos_pids | paste -sd' '); l=$(lanzados_pids | paste -sd' ')
  [ "$n" = "$hijo" ] || { ESPERA_MOTIVO="al final 'conectado [' viene de los pids nuevos '$n' y no solo del hijo $hijo (respawn o hijo extra)"; return 1; }
  [ -z "$l" ] || [ "$l" = "$hijo" ] || { ESPERA_MOTIVO="al final 'lector hijo lanzado' viene de los pids '$l' y no solo del hijo $hijo (respawn)"; return 1; }
  libro5_crece "$hijo" || { ESPERA_MOTIVO="el libro5_ms del hijo final $hijo NO crece en ${P5_CRECE_S:-90} s (hilo muerto o hijo mudo)"; return 1; }
  return 0
}

# El screen existe (con reintentos: justo tras un --restart puede tardar en aparecer).
espera_screen() { local nom=$1 plazo=${2:-${P5_SCREEN_S:-30}} t0=$SECONDS
  while :; do screen -ls | grep -qE "[0-9]+\.${nom}[[:space:]]" && return 0; [ $((SECONDS - t0)) -ge "$plazo" ] && return 1; sleep "${P5_PASO:-2}"; done; }

# Sincroniza con el ciclo del watchdog (pipeline_watchdog.py: un tick cada ~121 s, pero su log solo lo marca cada tick con algo que decir: cada 121 s con la alerta de disco,
# cada ~605 s (5 ticks, 'Sintaxis OK') sin ella: datos reales 14-Nov, huecos de 120/121/122/363/605 s). M6: el periodo NO se supone: se MIDEN las marcas del log en la ventana
# WD_VENTANA_S (2400): >= WD_MIN_MARCAS (3) marcas (lineas [ts] a >60 s unas de otras) con huecos multiplos enteros de WD_PERIODO (121.2, tolerancia 3 s + 1 s/ciclo) => fase =
# ultima marca; espera hasta WD_MARGEN (12) s despues del proximo tick. Si no hay >= 3 marcas o los huecos no encajan: NO se sincroniza (AVISO; riesgo residual: un tick del watchdog
# entre el cp y el reinicio, que ve STALE y reinicia 1 vez antes que nosotros => P5 lo detecta como RESPAWN y hace marcha atras) y se espera WD_SIN_SYNC_S (0). Si el ultimo tick (hace <150 s) reinicia una
# screen STALE ('auto-reiniciando' en su bloque del log) se salta un tick entero (+P). Fallo (1) solo si el log falta o lleva >900 s sin escribir (watchdog muerto).
# wd_fase LOG AHORA: imprime 'SYNC <espera_s>' o 'NOSYNC <motivo>'.
wd_fase() {
  "$PY" -I -c '
import re, sys, time, calendar
w, now, P, vent, minm, g = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
f = open(w, "rb"); f.seek(0, 2); n = f.tell(); f.seek(max(0, n - 262144)); txt = f.read().decode("utf-8", "replace")
L = [(calendar.timegm(time.strptime(x, "%Y-%m-%dT%H:%M:%S")), r) for x, r in re.findall(r"^\[(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)Z\](.*)$", txt, re.M)]
L = sorted(l for l in L if now - vent <= l[0] <= now + 5); ts = [l[0] for l in L]
m = []
for t in ts:
    if not m or t - m[-1] > 60: m.append(t)
if len(m) < minm: print("NOSYNC solo %d marcas en los ultimos %d s (minimo %d)" % (len(m), vent, minm)); sys.exit(0)
for a, b in zip(m, m[1:]):
    d = b - a; k = max(1, round(d / P))
    if abs(d - k * P) > 3 + k: print("NOSYNC hueco de %d s entre marcas no es multiplo de %.1f s" % (d, P)); sys.exit(0)
el = now - m[-1]; e = P - (el - int(el / P) * P) + g
if el < 150 and any(t >= m[-1] and "auto-reiniciando" in r for t, r in L): e += P   # el ultimo tick esta reiniciando una screen STALE: se salta un tick
print("SYNC %.1f" % e)' "$1" "$2" "${WD_PERIODO:-121.2}" "${WD_VENTANA_S:-2400}" "${WD_MIN_MARCAS:-3}" "${WD_MARGEN:-12}" 2>/dev/null
}
espera_tick_watchdog() {
  local w=$1 m now el espera r
  m=$(stat -c %Y "$w" 2>/dev/null) || return 1
  now=$(date +%s); el=$((now - m)); [ "$el" -lt 900 ] || return 1
  r=$(wd_fase "$w" "$now")
  case "$r" in
    SYNC*) espera=${r#SYNC }; log "  watchdog: marcas medidas en el log; ultimo log hace ${el}s; espero ${espera}s hasta justo despues de su proximo tick"; sleep "$espera";;
    *) log "AVISO: sin sincronia con el watchdog (${r:-no se pudo medir}); espero ${WD_SIN_SYNC_S:-0}s; riesgo residual: un tick entre el cp y el reinicio (P5 lo detectaria)"; sleep "${WD_SIN_SYNC_S:-0}";;
  esac
}

# Reinicio de observadores VERIFICADO (para la marcha atras): captura viejos/off0, verify_deploy --restart, comprueba rc, 1 hijo nuevo sostenido y su libro5
# creciendo. 0 = ok (RB_DETALLE puede llevar un aviso blando); 1 = fallo (RB_DETALLE = motivo). $1 = fichero de salida de verify_deploy.
reinicio_verificado() {
  local out=$1 rc hij
  RB_DETALLE=""
  viejos=$(hijos_vivos); off0=$(stat -c %s "$LOGOBS" 2>/dev/null || echo 0)
  (cd "$REPO" && "$PY" verify_deploy.py --restart observadores) > "$out" 2>&1; rc=$?
  cat "$out" >> "$LOGF"
  if [ $rc -ne 0 ]; then
    espera_screen observadores || { RB_DETALLE="verify_deploy rc=$rc y no hay screen observadores"; return 1; }
    RB_DETALLE="aviso: verify_deploy rc=$rc (la screen existe); "
  fi
  espera_hijos || { RB_DETALLE="${RB_DETALLE}$ESPERA_MOTIVO"; return 1; }
  hij=$HIJO
  libro5_crece "$hij" || { RB_DETALLE="${RB_DETALLE}libro5_ms del hijo $hij no crece tras el reinicio"; return 1; }
  RB_DETALLE="${RB_DETALLE}hijo $hij vivo, sin viejos y libro5 creciendo"
  return 0
}

# ---- P6: verificacion DETERMINISTA del capture_markets nuevo (run_slow.sh lo lanza con `|| true`: un fallo no se ve en ningun sitio) ----
_ps_cap() { ps -eo pid,args | awk -v r="$REPO" 'index($0, r "/capture_markets.py") {print $1}' | sort -n | paste -sd' '; }
# Crecimiento de data/markets robusto al cambio de dia (#2): la foto previa guarda el tamano de CADA fichero de ayer/hoy/manana (el de manana aun no existe = 0); al final se compara
# fichero a fichero. Cruzar las 00:00Z no baja la suma (el de ayer deja de contarse) y el fichero nuevo del dia siguiente cuenta como crecimiento.
snap_markets() {
  local d; for d in "$(date -u -d yesterday +%F)" "$(date -u +%F)" "$(date -u -d tomorrow +%F)"; do echo "$d $(stat -c %s "${MARKETS_DIR:-$REPO/data/markets}/$d.csv" 2>/dev/null || echo 0)"; done; }
markets_crecio() {   # $1 = foto previa (snap_markets); $2 = (R4) epoch de arranque del pid NUEVO. 0 si ALGUN fichero crecio (o aparecio) y, con $2, su mtime es >= ese arranque (margen P6_MTIME_SLACK_S=3 s: proc_inicio = btime ENTERO de /proc/stat + starttime/CLK_TCK sobreestima el arranque hasta ~1 s, mas el salto de NTP; un ciclo viejo acaba segundos-minutos antes del nuevo):
  # lo que escribio un ciclo VIEJO que acabo tras la marca del cp (mtime anterior al arranque del nuevo) NO es crecimiento del ciclo nuevo.
  local d s0 s1 f mt; while read -r d s0; do [ -n "$d" ] || continue; f="${MARKETS_DIR:-$REPO/data/markets}/$d.csv"
    s1=$(stat -c %s "$f" 2>/dev/null || echo 0); [ "$s1" -gt "$s0" ] || continue
    if [ -n "${2:-}" ]; then mt=$(stat -c %.9Y "$f" 2>/dev/null || echo 0); awk -v m="$mt" -v i="$2" -v g="${P6_MTIME_SLACK_S:-3}" 'BEGIN { exit !(m + g >= i) }' || continue; fi
    return 0; done <<< "$1"; return 1; }
# Firma de lo que escribe el adelanto de capture_markets: SOLO adelanto_*.csv (la auditoria del ciclo). new_market_universo_*.csv.gz lo escribe tambien el listener independiente
# (otro proceso, sin relacion con este ciclo): incluirlo daba falsos 'escribio adelanto con el adelanto apagado' y falsos 'sigue escribiendo tras parar'.
adelanto_firma() { ls -l --time-style=+%s "$CFGDIR"/adelanto_*.csv 2>/dev/null | awk '{print $5, $6, $7}' | cksum; }
# T9: activo = horizonte ENTERO > 0 (como capture_markets._cfg: int, max(0,..)); '0', vacio o ilegible NO es activo (env var tiene prioridad sobre el fichero, igual que capture_markets).
adelanto_activo() { local v="${CAPTURE_5M_HORIZONTE_MIN:-}"; [ -n "$v" ] || v=$(tr -d '[:space:]' < "$CFGDIR/cfg_CAPTURE_5M_HORIZONTE_MIN" 2>/dev/null); [[ $v =~ ^[0-9]+$ ]] && [ "$((10#$v))" -gt 0 ]; }
# H9: las listas de clases/causas de error viven en UN solo fichero (deploy/clases_error.conf, sellado en SHA256SUMS) que tambien lee p6_ciclo_aislado.py. El despliegue lo copia a un
# temporal verificado contra SHA256SUMS y fija CLASES_CONF a esa copia ANTES de cargar esta lib; sin CLASES_CONF se usa el que esta junto a la lib.
CLASES_CONF=${CLASES_CONF:-$(dirname "${BASH_SOURCE[0]}")/clases_error.conf}
[ -s "$CLASES_CONF" ] && . "$CLASES_CONF" || { echo "ABORTO: falta o esta vacio $CLASES_CONF (listas de clases de error)"; return 2 2>/dev/null || exit 2; }
# T7/T6: UN SOLO clasificador de errores = p6_ciclo_aislado.py (--clasifica duro|blando, texto por stdin; lee clases_error.conf via CLASES_CONF). Aqui no queda logica duplicada en awk/bash.
# Un fallo del propio clasificador (python/conf rotos) devuelve rc 3: el llamador lo trata como INCONCLUSO (nunca como 'sin errores' ni como fallo del codigo).
if [ -n "${P6_CLASIF:-}" ]; then _CLASIF_PY=$P6_CLASIF; elif [ -n "${V3:-}" ]; then _CLASIF_PY=$V3/deploy/p6_ciclo_aislado.py; else _CLASIF_PY=$(dirname "${BASH_SOURCE[0]}")/p6_ciclo_aislado.py; fi
cap_error_codigo() { printf '%s\n' "$1" | "${PY:-python3}" "$_CLASIF_PY" --clasifica duro || return 3; }
cap_excusa() { printf '%s\n' "$1" | "${PY:-python3}" "$_CLASIF_PY" --clasifica transitorio || return 3; }
cap_error_blando() { printf '%s\n' "$1" | "${PY:-python3}" "$_CLASIF_PY" --clasifica blando || return 3; }
# (a) Ciclo AISLADO provocado por nosotros (deploy/p6_ciclo_aislado.py): 0 OK, 1 FALLO, 2 INCONCLUSO (causa transitoria en todos los intentos). CAP_MOTIVO = detalle.
p6_aislado() {
  local out rc tmp runner=${P6_RUNNER:-${V3:-.}/deploy/p6_ciclo_aislado.py}; P6_INTERMITENTE=0
  tmp=$(mktemp -d "${TMPDIR:-/var/tmp}/p6_aislado.XXXXXX") || { CAP_MOTIVO="no se pudo crear el dir temporal del ciclo aislado (entorno, no el codigo): inconcluso"; return 2; }
  out=$("$PY" "$runner" --repo "$REPO" --tmp "$tmp" --timeout "${P6_AIS_TIMEOUT:-240}" --intentos "${P6_AIS_INTENTOS:-3}" --pausa "${P6_AIS_PAUSA:-70}" ${PRE:+--pre "$PRE/capture_markets.py.pre"} 2>&1); rc=$?
  rm -rf "$tmp"; CAP_MOTIVO=$(printf '%s\n' "$out" | tail -n 3 | tr '\n' '|')
  # M3: un DURO que no se repitio (OK intermitente) NO es verificacion limpia: el deploy lo marca NO VERIFICADO (rc 4 + aviso critico), sin marcha atras
  printf '%s\n' "$out" | grep -q '^AVISO INTERMITENTE' && P6_INTERMITENTE=1 && P6_INTERMITENTE_TXT=$(printf '%s\n' "$out" | grep -m1 '^AVISO INTERMITENTE' | cut -c1-300)
  # solo un veredicto EXPLICITO del runner ('FALLO intento N: ...') es un fallo del codigo objetivo: un rc 1 de un runner roto (Traceback propio, argumentos) o cualquier otro rc es INCONCLUSO
  case $rc in 0|2) return $rc;; 1) printf '%s\n' "$out" | grep -q '^FALLO intento' && return 1;; esac
  CAP_MOTIVO="el runner de P6 salio con rc=$rc sin un veredicto 'FALLO intento' (fallo del runner, no evidencia contra el codigo): $CAP_MOTIVO"; return 2
}
# Epoch (con decimales) de arranque del proceso $1, leido de /proc (no de `ps`, sustituido en el harness): btime + starttime/CLK_TCK. Falla si el proceso ya no existe.
proc_inicio() {
  local st bt tck; st=$(awk '{ s = $0; sub(/^.*\) /, "", s); split(s, a, " "); print a[20] }' "/proc/$1/stat" 2>/dev/null) && [ -n "$st" ] || return 1
  bt=$(awk '$1 == "btime" { print $2 }' /proc/stat 2>/dev/null); tck=$(getconf CLK_TCK 2>/dev/null || echo 100)
  awk -v b="$bt" -v s="$st" -v t="$tck" 'BEGIN { printf "%.2f\n", b + s / t }'
}
# El pid $1 es un ciclo que SOLO puede correr el codigo nuevo y que podemos observar desde su principio: arranco >= P6_SLACK_S (2) s DESPUES de la marca del cp (P6_MARCA_TS: un
# proceso que arranco antes pudo importar el capture_markets viejo) y lleva <= P6_TARDE_MAX_S (120) s vivo (si se adopta ya a mitad, sus baselines de data/markets/adelanto no valen).
cap_arranca_tras_marca() {
  local ini; ini=$(proc_inicio "$1") || return 1
  awk -v i="$ini" -v m="${P6_MARCA_TS:-0}" -v n="$(date +%s.%N)" -v g="${P6_SLACK_S:-2}" -v t="${P6_TARDE_MAX_S:-120}" 'BEGIN { exit !(m > 0 && i >= m + g && n - i <= t) }'
}
# B1/M1: texto de slow.log (desde el byte $2) del ciclo $3 y SOLO de su capture_markets. FORMATO REAL (run_slow.sh:14, log() hace tee -a al mismo log que redirige el screen):
# cada cabecera '--- Ciclo slow N ---' y '--- Ciclo slow N completado ---' sale DOS veces seguidas. El segmento empieza en la 1a cabecera N (la repetida identica no corta),
# y acaba en: otra cabecera (N distinto), el 'completado', la cabecera de capture_wallets ('=== Captura wallets ===') o el '=== Fin ===' de capture_markets (lo ultimo que imprime;
# stdout se vuelca al salir). Asi no entra nada de capture_wallets/trades (HTTPError de data-api, ValueError de otros scripts) como error ni como excusa.
slow_segmento() {
  tail -c +$(( $2 + 1 )) "$1" 2>/dev/null | awk -v N="$3" '
    /--- Ciclo slow [0-9]+ completado ---/ { if (f) exit; next }
    /--- Ciclo slow [0-9]+ ---/ { n = $0; sub(/^.*Ciclo slow /, "", n); sub(/ ---.*$/, "", n)
      if (f) { if (n != N) exit; print; next } if (n == N) { f = 1; print } next }
    !f { next }
    /=== Captura wallets ===/ { exit }
    { print }
    /=== Fin ===[ \t]*$/ { exit }'
}
# (b) Artefacto del PROXIMO ciclo real. $1 = slow.log. Globales: $cap_pre (pids de capture_markets vivos ANTES del cp), $P6_MARCA_TS / $P6_MARCA_OFF (epoch y tamano de slow.log
# justo DESPUES del cp). Un ciclo es "el nuevo" solo si su pid no estaba en $cap_pre, arranco tras la marca (+slack) y lo vemos en sus primeros P6_TARDE_MAX_S s; se analiza el
# slow.log desde la linea '--- Ciclo slow N ---' de run_slow.sh (la escribe bash, sin buffer, justo ANTES de lanzar capture_markets: la 1a tras el offset de la marca; el ciclo
# viejo la escribio antes) hasta la cabecera del ciclo siguiente. Asi entran TODO el stdout (que python vuelca al salir, tras el stderr) y el stderr del ciclo nuevo y nada del
# viejo (run_slow.sh es secuencial). Sin esa linea (log rotado/otro lanzador) NO es atribuible => 2. Baselines (data/markets, adelanto) en la deteccion.
# Espera hasta P6_ESPERA_S (2400) a que aparezca y hasta P6_CICLO_S (900) a que termine.
# 0 = ok (data/markets CRECIO); 1 = FALLO (error de CODIGO duro; no crece sin excusa; adelanto escrito con el adelanto apagado); 2 = no observado / no atribuible / sin crecimiento verificable (excusa 429/red o error de datos).
verifica_capture() {
  local sl=$1 plazo=${P6_ESPERA_S:-2400} ciclo=${P6_CICLO_S:-900} t0=$SECONDS nuevo="" p m0 a0 act sz off seg ec eb ex ncic ini_nuevo
  CAP_MOTIVO=""
  [ "${P6_MARCA_TS:-0}" -gt 0 ] 2>/dev/null || { CAP_MOTIVO="sin marca de tiempo del despliegue (P6_MARCA_TS): no se puede atribuir ningun ciclo al codigo nuevo"; return 2; }
  # H7: las bases de data/markets y adelanto_* NO se toman al adoptar el pid (hasta P6_TARDE_MAX_S s tarde: una captura sana ya habria escrito y daria 'NO crecio'). Primera vuelta: las de la
  # marca del despliegue (P6_M0/P6_A0, tomadas junto a P6_MARCA_TS; sin ellas, las de ahora). Si en una vuelta no hay ciclo nuevo, se REFRESCAN antes de dormir: un ciclo que arranque
  # durante el sueno nace despues de la base (y lo que escribio el ciclo viejo no se le atribuye).
  m0=${P6_M0:-}; a0=${P6_A0:-}; [ -n "$m0" ] || m0=$(snap_markets); [ -n "$a0" ] || a0=$(adelanto_firma)
  while [ -z "$nuevo" ] && [ $((SECONDS - t0)) -lt "$plazo" ]; do
    for p in $(_ps_cap); do case " $cap_pre " in *" $p "*) continue;; esac
      cap_arranca_tras_marca "$p" && { nuevo=$p; break; }; done
    [ -n "$nuevo" ] || { m0=$(snap_markets); a0=$(adelanto_firma); sleep "${P6_PASO:-5}"; }
  done
  ini_nuevo=""; [ -z "$nuevo" ] || ini_nuevo=$(proc_inicio "$nuevo" 2>/dev/null || true)      # R4: arranque del pid nuevo (para exigir mtime >= arranque al contar crecimiento)
  [ -n "$nuevo" ] || { CAP_MOTIVO="no aparecio un ciclo nuevo de capture_markets (pid fuera de '$cap_pre', arrancado tras el despliegue y visto en sus primeros ${P6_TARDE_MAX_S:-120}s) en ${plazo}s (no verificado en ciclo real)"; return 2; }
  # B1/M1: numero N del ciclo del pid adoptado = la ULTIMA cabecera '--- Ciclo slow N ---' escrita tras la marca (run_slow.sh es secuencial y adoptamos en sus primeros
  # ${P6_TARDE_MAX_S:-120}s: la cabecera de ese ciclo es la ultima del log). Sin ella no se atribuye.
  ncic=$(tail -c +$(( ${P6_MARCA_OFF:-0} + 1 )) "$sl" 2>/dev/null | awk '/--- Ciclo slow [0-9]+ ---/ { n = $0; sub(/^.*Ciclo slow /, "", n); sub(/ ---.*$/, "", n); l = n } END { print l }')
  [ -n "$ncic" ] || { CAP_MOTIVO="slow.log no tiene la cabecera '--- Ciclo slow N ---' de ningun ciclo tras el despliegue: el ciclo del pid $nuevo no es atribuible"; return 2; }
  act=0; adelanto_activo && act=1
  t0=$SECONDS
  while kill -0 "$nuevo" 2>/dev/null; do
    [ $((SECONDS - t0)) -ge "$ciclo" ] && { CAP_MOTIVO="el ciclo nuevo de capture_markets (pid $nuevo) no termino en ${ciclo}s (no verificado en ciclo real)"; return 2; }
    sleep "${P6_PASO:-5}"
  done
  sz=$(stat -c %s "$sl" 2>/dev/null || echo 0); off=${P6_MARCA_OFF:-0}
  [ "$sz" -ge "$off" ] || { CAP_MOTIVO="slow.log rotado/truncado desde el despliegue: el ciclo nuevo no es atribuible"; return 2; }
  seg=$(slow_segmento "$sl" "$off" "$ncic")
  [ -n "$seg" ] || { CAP_MOTIVO="slow.log no tiene la cabecera '--- Ciclo slow $ncic ---' del ciclo nuevo tras el despliegue (no atribuible)"; return 2; }
  ec=$(cap_error_codigo "$seg") || { CAP_MOTIVO="el clasificador de errores (p6_ciclo_aislado.py --clasifica) fallo: no se puede decidir sobre el ciclo real (inconcluso, no es evidencia contra el codigo)"; return 2; }
  ec=$(printf '%s\n' "$ec" | head -n 4 | tr '\n' '|' | sed 's/||*$//'); [ "$ec" != "|" ] || ec=""
  [ -z "$ec" ] || { CAP_MOTIVO="error de codigo en el ciclo NUEVO de capture_markets ($sl): $ec"; return 1; }
  if [ "$act" = 0 ] && [ "$(adelanto_firma)" != "$a0" ]; then CAP_MOTIVO="el ciclo nuevo ESCRIBIO ficheros de adelanto (adelanto_*) con el adelanto apagado"; return 1; fi
  # el proceso adoptado MURIO sin su '=== Fin ===' (SIGKILL/OOM/rc != 0 sin traceback: nada en stderr que atribuir): inconcluso, NUNCA se le aplica la excusa transitoria
  printf '%s\n' "$seg" | grep -aqE '=== Fin ===[[:space:]]*$' || { CAP_MOTIVO="el capture_markets adoptado (pid $nuevo) termino SIN '=== Fin ===' en slow.log (matado/OOM/crash sin traceback): ciclo real inconcluso"; return 2; }
  # 0 SOLO si data/markets CRECIO en este ciclo. Una excusa transitoria (429/red) sin crecimiento NO aprueba (#7): inconcluso (2), el llamador exige la captura aislada OK. Un error dependiente
  # de datos de la API ('Error gamma ..: KeyError') con data/markets creciendo no revierte; sin crecimiento es inconcluso (#3).
  # T3: sin el arranque del pid nuevo no se puede atribuir el crecimiento (R4): FAIL-CLOSED, inconcluso; nunca se cae a la regla antigua (cualquier crecimiento desde la base).
  [ -n "$ini_nuevo" ] || { CAP_MOTIVO="no se pudo leer el arranque del pid nuevo ($nuevo) de /proc: el crecimiento de data/markets no es atribuible al ciclo nuevo (inconcluso)"; log "AVISO P6: $CAP_MOTIVO"; return 2; }
  markets_crecio "$m0" "$ini_nuevo" && return 0
  eb=$(cap_error_blando "$seg") || { CAP_MOTIVO="el clasificador de errores (--clasifica blando) fallo: inconcluso"; return 2; }
  eb=$(printf '%s\n' "$eb" | head -n 2 | tr '\n' '|' | sed 's/||*$//')
  [ -z "$eb" ] || { CAP_MOTIVO="error dependiente de los datos de la API en el ciclo real ($eb) y data/markets NO crecio: inconcluso"; return 2; }
  ex=$(cap_excusa "$seg") || { CAP_MOTIVO="el clasificador de errores (--clasifica transitorio) fallo: inconcluso"; return 2; }
  if [ -n "$ex" ]; then CAP_MOTIVO="excusa transitoria (429/red) en el ciclo real y data/markets NO crecio: crecimiento no verificado en el ciclo real"; return 2; fi
  CAP_MOTIVO="el ciclo nuevo termino sin error ni excusa transitoria pero data/markets NO crecio"; return 1
}

# #5: el adelanto debe estar apagado POR CFG, no por falta del modulo: capture_markets.U (universo_5m_io) tiene que importar (modulo presente en el directorio probado), el horizonte
# efectivo ser 0 y solo_adelanto() salir con rc 0. La salida lleva un marcador propio (APAGADO_POR_CFG / SIN_MODULO / ACTIVO): el texto 'apagado' de solo_adelanto no vale,
# lo imprime tambien sin modulo. $1 = directorio con capture_markets.py y universo_5m_io.py (stage o REPO). Requiere REPO, DL y PY. CAP_OK_MOTIVO = detalle.
cap_ok() {
  local out rc; CAP_OK_MOTIVO=""
  out=$( cd "$1" && env -u CAPTURE_5M_HORIZONTE_MIN UNIVERSO_5M_DIR="$DL/traspaso_deltas_ws/_vacio" timeout 60 "$PY" -I -B -c "
import sys
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, '.')
import capture_markets as c
if c.U is None: print('SIN_MODULO'); sys.exit(3)
if c.HORIZONTE_5M_MIN > 0: print('ACTIVO'); sys.exit(4)
r = c.solo_adelanto(); print('APAGADO_POR_CFG'); sys.exit(r)" "$REPO" 2>&1 ); rc=$?
  [ $rc -eq 0 ] && printf '%s\n' "$out" | grep -qx APAGADO_POR_CFG && return 0
  case "$out" in *SIN_MODULO*) CAP_OK_MOTIVO="universo_5m_io no importa en $1 (capture_markets.U es None): el adelanto saldria 'apagado' por falta de modulo, no por cfg";;
    *ACTIVO*) CAP_OK_MOTIVO="el adelanto sale ACTIVO en $1 con el cfg vacio (horizonte > 0)";; *) CAP_OK_MOTIVO="rc=$rc: $(printf '%s' "$out" | tail -n 2 | tr '\n' '|')";; esac
  return 1
}
# L3: tras quitar los cfg, parar el capture_markets EN CURSO (lee los cfg al importar: seguiria ~10 min con el adelanto) y verificar que ya no escribe adelanto_*.
# SIGTERM y, si no sale en P6_TERM_S (15), SIGKILL: solo mata ese proceso (run_slow.sh lo lanza con `|| true` y sigue; el siguiente ciclo arranca con el codigo ya restaurado).
# Cada escritura del ciclo es un unico O_APPEND (sin lineas partidas). 0 = parado y sin escrituras de adelanto; 1 = sigue vivo o escribiendo.
parar_capture_en_curso() {
  local pids p t0 f1 f2 vivo=0; pids=$(_ps_cap)
  [ -z "$pids" ] && { CAP_PARADA="no habia capture_markets en curso"; return 0; }
  for p in $pids; do kill -TERM "$p" 2>/dev/null; done
  t0=$SECONDS
  while [ $((SECONDS - t0)) -lt "${P6_TERM_S:-15}" ]; do vivo=0; for p in $pids; do kill -0 "$p" 2>/dev/null && vivo=1; done; [ $vivo -eq 0 ] && break; sleep 0.5; done
  for p in $pids; do kill -0 "$p" 2>/dev/null && kill -KILL "$p" 2>/dev/null; done
  sleep 1; for p in $pids; do kill -0 "$p" 2>/dev/null && { CAP_PARADA="capture_markets $p sigue vivo tras SIGKILL"; return 1; }; done
  f1=$(adelanto_firma); sleep "${P6_ESTABLE_ADEL_S:-5}"; f2=$(adelanto_firma)
  [ "$f1" = "$f2" ] || { CAP_PARADA="los ficheros de adelanto siguen cambiando tras parar capture_markets ($pids)"; return 1; }
  CAP_PARADA="capture_markets en curso ($pids) parado y sin escrituras de adelanto"; return 0
}

# L4: contrato con el verify_deploy REAL, SOLO LECTURA (sin --restart): (1) el informe sin argumentos (lee ps; rc 1 si OTRA screen esta STALE: no importa) trae la linea
# de 'observadores' con veredicto y pid; (2) acepta `--restart` (el parseo existe) y la pantalla 'observadores' esta en pipeline_watchdog.SCREEN_RESTART con
# observadores_fase0.py (de donde verify_deploy saca el comando de arranque). Detalle en CONTRATO_MOTIVO.
contrato_verify_deploy() {
  local inf; CONTRATO_MOTIVO=""
  [ -f "$REPO/verify_deploy.py" ] || { CONTRATO_MOTIVO="no existe $REPO/verify_deploy.py"; return 1; }
  grep -q -- '"--restart"' "$REPO/verify_deploy.py" || { CONTRATO_MOTIVO="verify_deploy.py ya no parsea --restart"; return 1; }
  grep -E '^[[:space:]]*"observadores"[[:space:]]*:' "$REPO/pipeline_watchdog.py" 2>/dev/null | grep -q 'observadores_fase0\.py' || { CONTRATO_MOTIVO="pipeline_watchdog.SCREEN_RESTART no trae observadores -> observadores_fase0.py"; return 1; }
  inf=$(cd "$REPO" && timeout 60 "$PY" verify_deploy.py 2>&1)
  printf '%s\n' "$inf" | grep -qE '^[^ ]+ +observadores +(FRESH|STALE) +pid=[0-9]+' || { CONTRATO_MOTIVO="el informe de verify_deploy.py no trae la linea 'observadores FRESH|STALE pid=N' (formato cambiado?)"; return 1; }
  return 0
}

# L1: el ensayo e2e con procesos reales (tests/test_e2e_real.py) debe haber PASADO (los 5 tests, sin skip) en las ultimas E2E_MAX_H horas con el sha ACTUAL de los
# scripts: el sello lo escribe tests/conftest.py al terminar el ensayo. Un skip (sin red, sin espacio) NO sella => P0 falla. sha = de la concatenacion de los ficheros.
e2e_sha() { cat "$@" 2>/dev/null | sha256sum | cut -c1-32; }
e2e_sello_ok() {   # $1 = sello  $2.. = ficheros cuyo sha debe coincidir
  local st=$1 h max=${E2E_MAX_H:-24} t ahora; shift; E2E_MOTIVO=""
  [ -s "$st" ] || { E2E_MOTIVO="no hay sello del ensayo e2e ($st): ejecutar tests/test_e2e_real.py (necesita red) antes de desplegar"; return 1; }
  h=$(e2e_sha "$@"); t=$("$PY" -I -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d.get("sha",""), int(d.get("ts",0)), d.get("pasados",0))' "$st" 2>/dev/null) || { E2E_MOTIVO="sello e2e ilegible"; return 1; }
  set -- $t; ahora=$(date +%s)
  [ "$1" = "$h" ] || { E2E_MOTIVO="el sello e2e es de OTRA version de los scripts (sello ${1:0:12} != actual ${h:0:12}): repetir tests/test_e2e_real.py"; return 1; }
  [ "${3:-0}" -ge "${E2E_N_TESTS:-5}" ] || { E2E_MOTIVO="el sello e2e cubre ${3:-0} tests (<${E2E_N_TESTS:-5})"; return 1; }
  [ $((ahora - ${2:-0})) -le $((max * 3600)) ] || { E2E_MOTIVO="el sello e2e tiene mas de ${max} h"; return 1; }
  return 0
}

# ---- #7 ventanas horarias prohibidas (UTC): 06:00-09:15 (racimo de crons), 13:30-21:00 (horario USA) y los huecos de 4 h xx:40-xx+1:05 con xx = 03,07,11,15,19,23 (23:40-00:05). ----
# ventana_de M: M = minuto del dia (cualquier entero; se normaliza mod 1440). Si cae en una ventana prohibida pone VENTANA (nombre) y devuelve 0; si no, VENTANA="" y 1.
ventana_de() {
  local m=$(( ($1 % 1440 + 1440) % 1440 )) h; VENTANA=""
  if [ $m -ge 360 ] && [ $m -lt 555 ]; then VENTANA="06:00-09:15Z"
  elif [ $m -ge 810 ] && [ $m -lt 1260 ]; then VENTANA="13:30-21:00Z (horario USA)"
  else for h in 3 7 11 15 19 23; do [ $(( (m - h * 60 - 40 + 1440) % 1440 )) -lt 25 ] && { VENTANA=$(printf 'hueco de 4 h %02d:40-%02d:05Z' $h $(( (h + 1) % 24 ))); break; }; done
  fi
  [ -n "$VENTANA" ]
}
# Minutos desde el minuto del dia $1 hasta la proxima ventana prohibida -> MH (0 = ya dentro; VENTANA = su nombre); 1440 y VENTANA="" si no hay ninguna en 24 h.
# Sin subshell (MH/VENTANA son globales): no usar con $(...).
min_hasta_ventana() {
  for MH in $(seq 0 1439); do ventana_de $(( $1 + MH )) && return 0; done; MH=1440; VENTANA=""
}

# ---- #6/#8 cfg de activacion del adelanto. Cada fichero se escribe ATOMICAMENTE (tmp + mv -T) y SOLO si no existia (lo escrito a mano no se pisa ni se registra); lo que
# escribe ESTE despliegue queda en el manifiesto $CFG_MANIFEST (una ruta por linea, en orden) y es lo UNICO que revertir_cfg borra, en orden INVERSO. Orden de escritura: el fix
# 429 ANTES del horizonte (el adelanto nunca corre sin el fix). ----
_cfg_escribe() {   # $1 = nombre del fichero  $2 = valor
  local d="$CFGDIR/$1" t
  if [ -e "$d" ]; then   # T9: solo cuenta como activado si el contenido es el ESPERADO; con otro valor (a mano) no se pisa, no se registra y se devuelve 1 (activar_cfg => rc 4 + aviso)
    if [ "$(tr -d '[:space:]' < "$d" 2>/dev/null)" = "$2" ]; then log "  cfg $1 ya existia con el valor esperado ($2): no se toca ni se registra"; return 0; fi
    log "  cfg $1 ya existia con OTRO valor ($(head -c 20 "$d" | tr -d '\n') != $2): no se toca; NO cuenta como activado"; return 1; fi
  t=$(mktemp "$CFGDIR/.cfg.XXXXXX") || return 1
  { echo "$2" > "$t" && echo "$d" >> "$CFG_MANIFEST" && mv -fT "$t" "$d"; } || { rm -f "$t"; return 1; }
}
revertir_cfg() {
  local f; [ -s "${CFG_MANIFEST:-}" ] || return 0
  while read -r f; do [ -n "$f" ] && rm -f -- "$f" && log "  cfg revertido (lo escribio este despliegue): $f"; done < <(tac "$CFG_MANIFEST"); : > "$CFG_MANIFEST"
}
activar_cfg() {      # UNICO camino que escribe los cfg (tambien el de 'YA DESPLEGADO'): exige la confirmacion de las 6 monedas
  if [ "${CONFIRMO_ADELANTO_6_MONEDAS:-0}" != "1" ]; then
    log "AVISO: --activar IGNORADO: el adelanto abarca 6 monedas y CAPTURE_429_FIX afecta a ETH/SOL en data/markets; repetir con CONFIRMO_ADELANTO_6_MONEDAS=1"; return 1; fi
  mkdir -p "$CFGDIR" && mkdir -p "$(dirname "$CFG_MANIFEST")" || { log "AVISO (blando): no se pudo crear $CFGDIR"; return 1; }
  if _cfg_escribe cfg_CAPTURE_429_FIX 1 && _cfg_escribe cfg_CAPTURE_5M_HORIZONTE_MIN 1440; then
    log "OK    ACTIVADO adelanto 24 h (6 monedas) y fix 429 (ETH/SOL en data/markets) (cfg en $CFGDIR, manifiesto $CFG_MANIFEST; efecto en el SIGUIENTE ciclo de capture_markets, ~10 min); desactivar: rm de esos 2 ficheros"
  else revertir_cfg; log "AVISO (blando): no se pudieron escribir los cfg de activacion (revertido lo escrito)"; return 1; fi
}

# ---- helpers bnreg, lock de restart_ram y MARCHA ATRAS compartidos por los dos scripts de despliegue (requieren DL, PY, RAMLOCK, WDLOG, PRE, log, aviso_critico) ----
bn_pid() { "$PY" -c 'import json,sys;print(json.load(open(sys.argv[1]))["pid"])' "$DL/binance_registro_estado.json" 2>/dev/null; }
bn_estado_ok() { "$PY" -c 'import json,time,sys;e=json.load(open(sys.argv[1]));esp=sys.argv[2];ok=e["estado"]==esp and (esp!="activo" or e["lock"]) and time.time()-e["ts"]/1000<float(sys.argv[3]);sys.exit(0 if ok else 1)' "$DL/binance_registro_estado.json" "$1" "$2" 2>/dev/null; }
bn_es_duenyo() {
  local pid; pid=$(bn_pid); [ -n "$pid" ] || return 1
  kill -0 "$pid" 2>/dev/null || return 1
  grep -q "^bnreg pid=$pid\$" "$DL/.binance_registro.lock" 2>/dev/null || return 1
  lock_tomado_por "$pid" "$DL/.binance_registro.lock"        # L5: lectura de /proc/locks; NUNCA se adquiere el lock de bnreg (una sonda de adquisicion podria quitarselo)
}
LOCK=0
LOCK_T0=0
tomar_lock() { exec 9>"$RAMLOCK"; flock -w "${P1_TIMEOUT:-60}" 9 && { LOCK=1; LOCK_T0=$(date +%s); }; }
# M4: horas UTC ("HH:MM ...") de restart_ram_fase0 en el crontab (SOLO lectura; RESTART_RAM_CRONS las fija en el harness) y si alguna cayo mientras teniamos el lock (LOCK_T0..ahora) =>
# el cron intento tomar el lock sin esperar y se SALTO. Imprime el estado en una frase para el aviso.
restart_ram_horas() {
  [ -n "${RESTART_RAM_CRONS+x}" ] && { echo "$RESTART_RAM_CRONS"; return; }
  crontab -l 2>/dev/null | awk '!/^[ \t]*#/ && /restart_ram_fase0\.sh/ && $1 ~ /^[0-9]+$/ && $2 ~ /^[0-9]+$/ { printf "%02d:%02d ", $2, $1 }'
}
estado_restart_ram() {
  local hs h d s omit=0 t0=${LOCK_T0:-0} now; hs=$(restart_ram_horas); now=$(date +%s)
  [ "$t0" -gt 0 ] || { echo "el lock no se llego a tomar: restart_ram no se omitio"; return; }
  [ -n "$hs" ] || { echo "no se pudo leer su horario del crontab: revisar logs/restart_ram_fase0.log y ejecutarlo a mano si falta"; return; }
  for d in $(date -u -d yesterday +%F) $(date -u +%F); do for h in $hs; do s=$(date -u -d "$d $h UTC" +%s 2>/dev/null) || continue; [ "$s" -ge "$t0" ] && [ "$s" -le "$now" ] && omit=1; done; done
  if [ $omit -eq 1 ]; then echo "OMITIDO por el lock (su hora cayo durante el despliegue): ejecutarlo a mano"; else echo "NO omitido: ninguna de sus horas UTC (${hs% }) cayo mientras teniamos el lock"; fi
}
liberar_lock() { exec 9>&-; LOCK=0; }
ROLLBACK_HECHO=0; P5_VERIFICADO=0; RB_ALCANCE=completo; EN_VUELO=0; FALLO_MOTIVO=""; ROLLBACK_RESULTADO="no hecha"; ROLLBACK_DETALLE=""; SENAL=0
trap_normales() { trap al_salir EXIT; trap 'exit 130' INT; trap 'exit 143' TERM; trap 'exit 129' HUP; }
# Marcha atras VERIFICADA. El script define restaurar_ficheros (restaura main segun $RB_ALCANCE y pone RB_OK/RB_DET), resumen_shas y hora_min. #3: el lock de restart_ram pudo liberarse antes de P6
# -> se RETOMA; si no se logra NO se reinicia (evita el doble reinicio con guard_ram/restart_ram). #4: una senal DURANTE la marcha atras se difiere (un handler, no
# `trap ''`: los hijos -- screen, verify_deploy -- no heredan senales ignoradas) y se completa y verifica antes de salir.
restaurar() {
  [ "$ROLLBACK_HECHO" = 1 ] && return 0; ROLLBACK_HECHO=1
  trap 'SENAL=1' HUP TERM INT
  local vent=""; ventana_de "$(hora_min)" && vent=$VENTANA
  # #7: dentro de una ventana prohibida NO se reinicia observadores si ya esta VERIFICADO sano (P5 ok) con libro/io nuevos: solo se restaura capture_markets (lo que P6 juzga) y
  # libro/io se quedan desplegados (restaurarlos reiniciaria observadores en la ventana: el watchdog lo haria solo por STALE). Un fallo anterior a P5 (observadores puede correr
  # codigo roto) prevalece: marcha atras COMPLETA con reinicio, con aviso explicito.
  RB_ALCANCE=completo
  if [ -n "$vent" ] && [ "${P5_VERIFICADO:-0}" = 1 ]; then RB_ALCANCE=captura
  elif [ -n "$vent" ]; then log "AVISO EXPLICITO: marcha atras COMPLETA con reinicio de observadores DENTRO de una ventana prohibida ($vent): el fallo es anterior a la verificacion de P5 (observadores puede correr codigo roto) y prevalece restaurar + reiniciar"; fi
  log "MARCHA ATRAS ($RB_ALCANCE): restaurar .pre${vent:+ [ventana prohibida: $vent]} y reiniciar observadores (verificada)"
  RB_OK=1; RB_DET=""
  restaurar_ficheros
  if [ "$RB_ALCANCE" = captura ]; then
    RB_DET="${RB_DET}SIN REINICIAR observadores (ventana prohibida $vent; libro/io verificados quedan DESPLEGADOS, solo se restauro capture_markets): revertir libro/io a mano en ventana libre si se desea"
  elif [ $LOCK -eq 1 ] || tomar_lock; then
    espera_tick_watchdog "$WDLOG" || log "AVISO: el watchdog no tiene log reciente; el reinicio de la marcha atras va sin sincronizar"
    reinicio_verificado "$PRE/vd_out_restaurar_$$.txt" || RB_OK=0
    RB_DET="${RB_DET}${RB_DETALLE}"
  else
    RB_OK=0; RB_DET="${RB_DET}SIN REINICIAR: no se pudo retomar $RAMLOCK en ${P1_TIMEOUT:-60} s (guard_ram/restart_ram lo tiene); ficheros restaurados, el watchdog reiniciara observadores por STALE o hacerlo a mano"
  fi
  [ "$(type -t restaurar_post)" = function ] && restaurar_post      # tras el reinicio (el libro viejo ya no puede recrear nada): p.ej. borrar gamma_pausa.json si lo creo el despliegue
  if [ $RB_OK -ne 1 ]; then ROLLBACK_RESULTADO="FALLO"; elif [ "$RB_ALCANCE" = captura ]; then ROLLBACK_RESULTADO="PARCIAL"; else ROLLBACK_RESULTADO="OK"; fi
  ROLLBACK_DETALLE=$RB_DET
  log "marcha atras hecha ($ROLLBACK_RESULTADO): $RB_DET; $(resumen_shas)"
  [ $SENAL -eq 1 ] && log "AVISO: se recibio una senal durante la marcha atras: se difirio y la marcha atras se completo y verifico antes de salir"
  trap_normales
}
die() { FALLO_MOTIVO="$*"; restaurar; aviso_critico "FALLO tras el despliegue: $FALLO_MOTIVO -> marcha atras $ROLLBACK_RESULTADO ($ROLLBACK_DETALLE) (ver $LOGF)"; exit 1; }
al_salir() {      # el script murio (senal / error inesperado) con main a medio cambiar: restaurar y avisar con el resultado real
  local rc=$?
  if [ $EN_VUELO -eq 1 ] && [ $ROLLBACK_HECHO -eq 0 ]; then
    FALLO_MOTIVO="script interrumpido/terminado (rc=$rc) entre el cp y el final"; restaurar
    aviso_critico "$FALLO_MOTIVO -> marcha atras $ROLLBACK_RESULTADO ($ROLLBACK_DETALLE)"
  fi
  rm -f "${_CONF_COPIA:-}"      # R2: copia verificada de clases_error.conf (la crea el despliegue)
}
