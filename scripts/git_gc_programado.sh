#!/bin/bash
# git_gc_programado.sh — reempaqueta el repo (24.7GB de objetos sueltos,
# nunca compactados), acotado en memoria (RAM limitada, 3.7GB).
# Programado explícitamente por Javi (03-Ago) para franja SIN ventana de
# trading (11:31-15:00 Madrid = 09:31-13:00 UTC) tras comprobar que
# correrlo en horario live competía por recursos con git push y causaba
# huecos de varios minutos en el loop fast. Un solo uso vía `at`, no cron
# recurrente (decisión pendiente de si hace falta repetirlo periódicamente
# una vez esté al día).
#
# 04-Ago, tras incidente real: la corrida de las 09:31 UTC se cortó a mano
# porque el disco cayó de 2.9GB a 478MB libres en minutos (el pack temporal
# que construye `git gc` llegó a 1.89GB antes de que hubiera espacio para
# terminar y limpiar los objetos sueltos viejos) -- sin ningún límite de
# seguridad propio en el script, dependía de que alguien lo vigilara a mano.
# Dos capas nuevas para que esto no dependa de vigilancia humana:
#  1. Pre-flight: no arrancar si no hay margen de sobra para el pack nuevo.
#  2. Watchdog en background: mata el gc si el disco cae por debajo del
#     suelo de seguridad mientras corre, y limpia el pack temporal huérfano.
cd /root/polymarket-research || exit 1

LOG=logs/git_gc_programado.log
MIN_LIBRE_GB_ARRANQUE=5   # no arrancar sin al menos esto libre
MIN_LIBRE_MB_ABORTAR=1000 # matar el gc si cae por debajo de esto en marcha

libre_mb() { df --output=avail / | tail -1 | awk '{print int($1/1024)}'; }

echo "=== git gc programado, inicio $(date -u) ===" >> "$LOG"

libre_ahora=$(libre_mb)
if [ "$libre_ahora" -lt $((MIN_LIBRE_GB_ARRANQUE * 1024)) ]; then
  echo "ABORTADO: solo ${libre_ahora}MB libres al arrancar, hace falta >= ${MIN_LIBRE_GB_ARRANQUE}GB de margen para construir el pack nuevo sin arriesgar el disco. No se ejecuta git gc." >> "$LOG"
  exit 1
fi

nice -n 10 git -c pack.windowMemory=200m -c pack.threads=1 -c pack.window=10 gc >> "$LOG" 2>&1 &
GC_PID=$!

# Watchdog: vigila el disco mientras el gc corre; si cae del suelo de
# seguridad, mata el árbol de procesos de git y borra el pack temporal
# huérfano que deja atrás (nunca está referenciado hasta que gc termina,
# borrarlo es seguro).
(
  while kill -0 "$GC_PID" 2>/dev/null; do
    libre=$(libre_mb)
    if [ "$libre" -lt "$MIN_LIBRE_MB_ABORTAR" ]; then
      echo "WATCHDOG: disco crítico (${libre}MB < ${MIN_LIBRE_MB_ABORTAR}MB) durante el gc -- abortando para proteger el live." >> "$LOG"
      pkill -TERM -P "$GC_PID" 2>/dev/null
      kill -TERM "$GC_PID" 2>/dev/null
      sleep 2
      rm -f .git/objects/pack/tmp_pack_* .git/objects/pack/.tmp-*-pack* 2>/dev/null
      echo "WATCHDOG: pack temporal huérfano limpiado. Disco libre tras limpieza: $(libre_mb)MB" >> "$LOG"
      break
    fi
    sleep 15
  done
) &
WATCHDOG_PID=$!

wait "$GC_PID" 2>/dev/null
kill "$WATCHDOG_PID" 2>/dev/null

echo "=== git gc programado, fin $(date -u) ===" >> "$LOG"
git count-objects -v >> "$LOG" 2>&1
df -h / | tail -1 >> "$LOG"
