#!/bin/bash
# Rotación de datos históricos pesados: comprime (gzip) los CSV diarios más
# antiguos que $DIAS_MANTENER, verificando integridad (comparación byte a
# byte tras descomprimir) antes de borrar el original, y BORRA los .gz más
# antiguos que $DIAS_BORRAR (capturas en bruto: ya se extrajo lo que importa
# a results.csv/trades.csv/estado en su momento, no hace falta guardarlas
# para siempre). Cron diario 03:00 UTC desde 2026-08-03 (antes: un solo uso
# 28-Jul, decisión explícita Javi tras barrido de disco al 90%; ampliado a
# política permanente el 03-Ago tras un segundo episodio con el disco a 0
# bytes libres — el script de un solo uso nunca se dejó programado).
# 02-Sep: DIAS_BORRAR 90->45 (barrido de salud de sesión) — disco al 93%,
# 5.8GB libres, ritmo real ~2.7GB/día (crisis en ~2 días). >45d de .gz
# eran 6.5GB recuperables de golpe vs solo 2.6GB con el umbral de 90d.
# Los .gz siguen siendo capturas en bruto ya extraídas a results.csv/
# trades.csv, nada que dependa de leer más allá de 45d en producción.
set -euo pipefail

DIAS_MANTENER=3
DIAS_BORRAR=20
# 05-Sep: bajado de 45->30 (barrido de salud) — disco al 92-93% pese al ajuste
# del 02-Sep, ritmo real ~2.7GB/día, crisis en ~2 días con margen de 45d.
# Recupera ~2.2GB de golpe (verificado antes de aplicar). Mismo criterio que
# el cambio 90->45: .gz son capturas en bruto ya extraídas a results.csv/
# trades.csv, nada en producción lee más allá de 30d.
# 09-Sep: bajado otra vez, DIAS_MANTENER 5->3 y DIAS_BORRAR 30->20 (barrido
# de salud) — disco al 96%, 3.2GB libres pese al ajuste del 05-Sep, el ritmo
# de captura (markets+wallets+sports crecen ~3.2GB/día sin comprimir en los
# 5 días recientes) sigue superando el margen. Comprimido a mano el mismo
# día liberó 3.2GB->9.9GB libres (96%->87%). Único lector afectado conocido
# (verificado antes de aplicar): analisis_ballenas_dosis_respuesta_16jul.py
# pide 5 días de data/markets/*.csv sin extensión .gz -- con 3 días de
# ventana ve menos histórico ahí, pero es un script de análisis puntual, no
# cron ni infraestructura live; analisis_gate_microbucket_precio.py (el que
# sí importa) ya soporta leer .gz nativamente.
CUTOFF_COMPRIMIR=$(date -u -d "-${DIAS_MANTENER} days" +%Y-%m-%d)
CUTOFF_BORRAR=$(date -u -d "-${DIAS_BORRAR} days" +%Y-%m-%d)
# 08-Sep (barrido de salud, disco a 2.0GB libres a media tarde pese a que
# este cron había corrido normal a las 03:00 con 5.8GB libres -- ritmo real
# ~270MB/hora, el mayor contribuyente con diferencia es polymarket_activity_
# *.csv en polymarket-research-datalogs, 800MB-1GB/día): ventana propia más
# corta SOLO para datalogs (3 días en vez de 5) -- nada en producción lee
# más allá de "los últimos 3 días" de ahí (verificado: peor caso encontrado,
# analisis_arbitraje_secuencial_yesno_03ago.py/analisis_sol60min_precio_
# entrada_03ago.py, usa glob(...)[-3:]). DIAS_MANTENER (5) sigue igual para
# el resto de directorios, sin cambios.
DIAS_MANTENER_DATALOGS=3
CUTOFF_COMPRIMIR_DATALOGS=$(date -u -d "-${DIAS_MANTENER_DATALOGS} days" +%Y-%m-%d)

comprimir_dir() {
  local dir="$1" patron="$2" cutoff="${3:-$CUTOFF_COMPRIMIR}"
  for f in "$dir"/$patron; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    fecha=$(echo "$base" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)
    if [ -z "$fecha" ]; then
      echo "SKIP (sin fecha en nombre): $f"
      continue
    fi
    if [[ "$fecha" > "$cutoff" || "$fecha" == "$cutoff" ]]; then
      continue  # dentro de la ventana reciente, no tocar
    fi
    if [ -f "${f}.gz" ]; then
      echo "SKIP (ya existe .gz): $f"
      continue
    fi
    gzip -c "$f" > "${f}.gz.tmp"
    if cmp -s <(zcat "${f}.gz.tmp") "$f"; then
      mv "${f}.gz.tmp" "${f}.gz"
      rm "$f"
      echo "OK: $f -> ${f}.gz"
    else
      echo "ERROR verificacion, NO se borra original: $f"
      rm -f "${f}.gz.tmp"
    fi
  done
}

borrar_gz_antiguos() {
  local dir="$1" patron="$2"
  for f in "$dir"/$patron.gz; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    fecha=$(echo "$base" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)
    if [ -z "$fecha" ]; then
      echo "SKIP borrado (sin fecha en nombre): $f"
      continue
    fi
    if [[ "$fecha" > "$CUTOFF_BORRAR" || "$fecha" == "$CUTOFF_BORRAR" ]]; then
      continue  # dentro de la ventana de retención, no borrar
    fi
    rm "$f"
    echo "BORRADO (>${DIAS_BORRAR}d): $f"
  done
}

cd /root/polymarket-research
comprimir_dir data/markets "*.csv"
comprimir_dir data/wallets "leaderboard_*.csv"
comprimir_dir data/wallets "positions_*.csv"
comprimir_dir data/trades "*.csv"
# 04-Ago: chainlink_*.csv es el mayor fichero diario del repo (35-37MB/día)
# y ninguno de sus lectores (fetch_chainlink_prices.py, resolution_sniper_
# observer.py, pipeline_watchdog.py) mira más allá del día actual -- y
# dashboard_server.py lo EXCLUYE explícitamente de su glob de históricos
# (ver comentario en cargar_precios_multi_activo). Verificado antes de
# añadir: data/prices/*.csv SIN prefijo (klines) NO se toca, dashboard_
# server sí lee hasta 7 días de esos -- se rompería con DIAS_MANTENER=5.
comprimir_dir data/prices "chainlink_*.csv"
# 11-Sep (barrido de salud, disco a 94%/5GB libres, git empezó a fallar por
# "No space left on device"): sports_spread_fase0_*.csv (sports_spread_
# observer_fase0.py) nunca se había añadido a esta rotación -- crecía sin
# control, 2-2.3GB/día, 5 días acumulados = ~11GB. Verificado antes de
# añadir: SOLO el propio writer lo toca (siempre al fichero de HOY, nunca
# lee días pasados) -- a diferencia de predictions_*.csv/results.csv, que
# shadow_resolve.py/shadow_postmortem.py sí escanean con glob sin límite de
# días y por tanto NO se pueden comprimir sin romper el resolver (dejarían
# de verse señales pendientes, mismo bug que el digest de GitHub Actions).
comprimir_dir data/shadow "sports_spread_fase0_*.csv"

cd /root/polymarket-research-datalogs
comprimir_dir . "polymarket_activity_*.csv" "$CUTOFF_COMPRIMIR_DATALOGS"
comprimir_dir . "libro_ambos_lados_*.csv" "$CUTOFF_COMPRIMIR_DATALOGS"
# 08-Sep: libro_book_ws_*.csv (desplegado 01-Sep, fetch_libro_book_ws.py)
# nunca se había añadido a esta rotación -- hueco real encontrado en el
# barrido de salud, 4 días acumulados sin comprimir ni borrar nunca.
comprimir_dir . "libro_book_ws_*.csv" "$CUTOFF_COMPRIMIR_DATALOGS"

cd /root/polymarket-research
borrar_gz_antiguos data/markets "*.csv"
borrar_gz_antiguos data/wallets "leaderboard_*.csv"
borrar_gz_antiguos data/wallets "positions_*.csv"
borrar_gz_antiguos data/trades "*.csv"
borrar_gz_antiguos data/prices "chainlink_*.csv"
borrar_gz_antiguos data/shadow "sports_spread_fase0_*.csv"

cd /root/polymarket-research-datalogs
borrar_gz_antiguos . "polymarket_activity_*.csv"
borrar_gz_antiguos . "libro_ambos_lados_*.csv"
borrar_gz_antiguos . "libro_book_ws_*.csv"

echo "=== DONE ==="
df -h / | tail -1
