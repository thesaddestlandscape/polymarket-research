#!/bin/bash
# Despliegue DESATENDIDO de bnreg (Javi OK 09-Nov: "que se haga igualmente si se cierra la sesion"). Plan aprobado: DISENO_CAPTURA_INDEPENDIENTE_L2_09nov.md + traspaso_bnreg_once.sh.
# Lanzado por `at` a las 21:05Z. Fail-closed: cualquier fallo antes del traspaso restaura los ficheros y avisa por Telegram; el traspaso restaura solo ante fallo (P5).
# Ventana valida: 21:05Z-22:10Z (fuera de horario USA 13:30-21:00Z y antes del restart_ram 22:20Z). Marcha atras: rm $DL/BNREG_HABILITADO (el hijo asume en <=5 s).
set -u
REPO=/root/polymarket-research; DL=/root/polymarket-research-datalogs; B=$REPO/experimentos/5m_barato/bnreg; ST=$B/dev_main
PY=$REPO/.venv/bin/python; BK=$DL/traspaso_bnreg/backup_main_$(date -u +%Y%m%dT%H%M%SZ); LOGF=$DL/traspaso_bnreg/deploy_desatendido_$(date -u +%Y%m%dT%H%M%SZ).log
mkdir -p "$BK" "$DL/traspaso_bnreg"
log() { echo "[$(date -u +%FT%TZ)] $*" | tee -a "$LOGF"; }
avisar() { $PY -c "import sys; sys.path.insert(0,'$REPO'); from shadow_digest import enviar_telegram; enviar_telegram(sys.argv[1])" "$1" >/dev/null 2>&1; }
sha() { sha256sum "$1" | cut -c1-16; }
restaurar() { for f in pipeline_watchdog.py verify_deploy.py vigia_loggers_silenciosos.py; do [ -f "$BK/$f" ] && cp "$BK/$f" "$REPO/$f"; done; rm -f "$REPO/binance_registro_ms.py"; rm -f "$DL/BNREG_HABILITADO"; }
relanzar_watchdog() { wid=$(screen -ls | awk '/\.watchdog\t/{print $1}'); [ -n "$wid" ] && screen -S "$wid" -X quit; sleep 3; screen -dmS watchdog bash -c "cd $REPO && python3 pipeline_watchdog.py"; }
fallo() { log "FALLO: $1 -> restauro ficheros de main"; restaurar; b=$(screen -ls | awk '/\.bnreg\t/{print $1}'); [ -n "$b" ] && screen -S "$b" -X quit; [ -n "${WD_REINICIADO:-}" ] && relanzar_watchdog; avisar "🚨 Despliegue bnreg ABORTADO (nada cambiado en produccion salvo watchdog reiniciado si procede): $1. Log: $LOGF"; exit 1; }
hm=$(date -u +%H%M); { [ "$hm" -ge 2105 ] && [ "$hm" -lt 2210 ]; } || { log "fuera de ventana 21:05-22:10Z (hora $hm): no despliego"; avisar "ℹ️ Despliegue bnreg NO ejecutado: fuera de ventana ($hm Z). Plan en project_checkpoint_09nov_noche_q11_bnreg."; exit 0; }
log "== INICIO despliegue desatendido bnreg =="
# 0. bases de main intactas (si alguien edito estos ficheros, abortar: los parches se calcularon sobre estos sha16)
[ "$(sha $REPO/libro_estado_ws.py)" = a959ca9668c0865a ] || fallo "libro_estado_ws.py de main cambio (base a959ca96)"
[ "$(sha $REPO/pipeline_watchdog.py)" = 5833ef26640f24e5 ] || fallo "pipeline_watchdog.py de main cambio (base 5833ef26)"
[ "$(sha $REPO/verify_deploy.py)" = 7043903d85849205 ] || fallo "verify_deploy.py de main cambio (base 7043903d)"
[ "$(sha $REPO/vigia_loggers_silenciosos.py)" = 7df4c6da4d9ae003 ] || fallo "vigia_loggers_silenciosos.py de main cambio (base 7df4c6da)"
[ "$(sha $B/binance_registro_ms.py)" = 58a141fce2fa8431 ] && [ "$(sha $ST/libro_estado_ws.py)" = a0196ee481a2fb3c ] && [ "$(sha $ST/pipeline_watchdog.py)" = 1f8f0e5855d6e433 ] && [ "$(sha $ST/verify_deploy.py)" = 2c73a1f3c34535aa ] && [ "$(sha $ST/vigia_loggers_silenciosos.py)" = bc39009feeafbfb0 ] || fallo "sha16 del paquete no coinciden con el revisado"
[ ! -e $DL/BNREG_HABILITADO ] || fallo "centinela ya presente"
[ -z "$(screen -ls | awk '/\.bnreg\t/')" ] || fallo "ya hay screen bnreg"
for f in pipeline_watchdog.py verify_deploy.py vigia_loggers_silenciosos.py; do cp "$REPO/$f" "$BK/$f"; done
# 1. copiar a main (libro_estado_ws.py lo copia el traspaso en P3, con su backup)
for f in pipeline_watchdog.py verify_deploy.py vigia_loggers_silenciosos.py; do $PY -m py_compile "$ST/$f" || fallo "no compila $f"; done
$PY -m py_compile $B/binance_registro_ms.py || fallo "no compila binance_registro_ms.py"
cp $B/binance_registro_ms.py $REPO/binance_registro_ms.py && for f in pipeline_watchdog.py verify_deploy.py vigia_loggers_silenciosos.py; do cp "$ST/$f" "$REPO/$f"; done || fallo "copia a main"
log "ficheros copiados a main; reinicio el watchdog (screen por id, no pkill -f)"
# 2. reiniciar watchdog a mano (no se autodespliega); el nuevo watchdog creara la screen bnreg en su siguiente tick
WD_REINICIADO=1; relanzar_watchdog; sleep 5
screen -ls | grep -q "\.watchdog" || fallo "watchdog no relanzado"
# 3. esperar a que el watchdog cree bnreg (<=4 min); si no, arrancarla con la misma linea
for i in $(seq 1 24); do screen -ls | grep -q "\.bnreg" && break; sleep 10; done
if ! screen -ls | grep -q "\.bnreg"; then
  log "el watchdog no creo bnreg en 4 min; la arranco a mano con la linea de SCREEN_RESTART"
  screen -dmS bnreg bash -c "cd $REPO && ulimit -v 2000000; choom -n -200 -- .venv/bin/python -u binance_registro_ms.py >> logs/binance_registro_ms.log 2>&1"; sleep 8
fi
screen -ls | grep -q "\.bnreg" || fallo "screen bnreg no arranca"
[ ! -e $DL/BNREG_HABILITADO ] || fallo "centinela aparecio solo"
# 4. plan del traspaso: debe terminar SIN fallos previos
bash $B/traspaso_bnreg_once.sh >> "$LOGF" 2>&1; rc=$?
[ $rc -eq 0 ] || { tail -15 "$LOGF" | cut -c1-200; fallo "plan del traspaso con fallos previos (rc=$rc)"; }
log "plan sin fallos: ejecuto el traspaso"
# 5. traspaso (restaura solo si falla en P5)
bash $B/traspaso_bnreg_once.sh --ejecutar >> "$LOGF" 2>&1; rc=$?
if [ $rc -ne 0 ]; then log "traspaso rc=$rc"; avisar "🚨 Traspaso bnreg FALLO rc=$rc (el script restaura libro_estado_ws; revisar). bnreg desplegada ociosa. Log: $LOGF"; exit $rc; fi
log "== TRASPASO OK =="
avisar "✅ bnreg DESPLEGADA: Binance se registra en su proceso propio (centinela puesto, observadores reiniciado una vez). Marcha atras: rm $DL/BNREG_HABILITADO. Log: $LOGF. Pendiente: T5 y medir primer hueco."
