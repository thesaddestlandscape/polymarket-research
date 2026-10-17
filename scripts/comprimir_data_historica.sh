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
  local dir="$1" patron="$2" cutoff="${3:-$CUTOFF_COMPRIMIR}" preservar_mtime="${4:-}"
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
      [ -n "$preservar_mtime" ] && touch -r "$f" "${f}.gz.tmp"
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
# 24-Sep: PolyBolt (fetch_polybolt_prices.py), ~70 MB/día, sin lectores todavía
comprimir_dir data/prices "polybolt_*.csv"
# 11-Sep (barrido de salud, disco a 94%/5GB libres, git empezó a fallar por
# "No space left on device"): sports_spread_fase0_*.csv (sports_spread_
# observer_fase0.py) nunca se había añadido a esta rotación -- crecía sin
# control, 2-2.3GB/día, 5 días acumulados = ~11GB. Verificado antes de
# añadir: SOLO el propio writer lo toca (siempre al fichero de HOY, nunca
# lee días pasados) -- a diferencia de predictions_*.csv/results.csv (ver
# más abajo), que sí se escanean con glob de varios días.
comprimir_dir data/shadow "sports_spread_fase0_*.csv"
# 28-Sep (barrido de salud, disco a 91-93%, 5.6-7.6GB libres): predictions_
# *.csv (data/shadow, ~650MB/día) llevaba 18 días SIN rotar -- 11GB. El
# comentario que decía "shadow_resolve.py/shadow_postmortem.py escanean sin
# límite de días" estaba DESACTUALIZADO -- ambos ya acotan a
# sorted(glob(...))[-(dias+2):] con dias=10 (PRED_PENDIENTES_DIAS), o sea 12
# días como mucho; shadow_resumen.py acota a 2 días. El único lector que SÍ
# era unbounded, shadow_digest.py::pendientes_por_horizonte() (cron diario
# 20:00 UTC, escaneaba TODO + results.csv completo cada día -- mismo patrón
# de OOM que mató analisis_fade_regimen_arquetipoA.py hoy), se acotó el
# mismo día a 18 días Y se le enseñó a leer .csv.gz de forma transparente
# (mismo patrón que sports_wallet_edge_tracker.py::cargar_trades_whale) --
# así el cutoff de compresión puede ser el mínimo real (12 días, resolve/
# postmortem) sin dejar a digest sin datos en el tramo 12-18 días. Scripts
# de análisis puntual (no cron) que globean sin límite quedan sin tocar a
# propósito -- mismo criterio ya aplicado a analisis_wallets_crossdominio_
# 01sep.py.
# 05-Oct (disco al 91 %, ~8,3 GB de predictions sin comprimir): cutoff 12 -> 3
# días (quedan 4 planos: hoy + 3). shadow_resolve.py, shadow_postmortem.py,
# vigia_ritmo_predicciones.py, vigia_cobertura_fillability.py y
# conectar_infraestructura_candidato.py leen ya .csv.gz vía
# predicciones_archivos.py; el resto lee hoy/ayer o [-3:] (generate_report,
# shadow_digest, shadow_resumen) y shadow_digest ya leía .gz. "mtime" =
# `touch -r`: el .gz conserva el mtime del CSV y predicciones_archivos.
# stat_logico() da la misma firma (tamaño sin comprimir + mtime), así que las
# cachés por fichero de resolve/postmortem no se invalidan al comprimir.
comprimir_dir data/shadow "predictions_*.csv" "$(date -u -d "-3 days" +%Y-%m-%d)" mtime
# 23-Sep (barrido de disco, 92% usado, 6.2GB libres): data/sports/activity_ws_*.csv
# (firehose sports, sports_activity_ws.py) NUNCA estaba en esta rotación --
# backup_activity_ws_sports.sh solo copia una versión comprimida al volumen
# externo, nunca toca/borra el original en disco raíz. Acumulaba sin límite:
# 4.3GB+ en 17 días (06..22-Sep) sin comprimir. DIAS_MANTENER=3 es seguro:
# vigia_sports_categoria_sin_clasificar.py solo lee HOY+AYER (1 día), y los
# lectores de historial completo (sports_wallet_edge_tracker.py::
# cargar_trades_completo, analisis_sports_wallet_combos_09sep.py,
# analisis_sports_crossmercado_eventos.py) se actualizaron el mismo día para
# leer *.csv* con gzip transparente (mismo patrón que cargar_trades_whale()
# ya usaba). analisis_wallets_crossdominio_01sep.py (rutas de fecha
# hardcodeadas, sin glob) es un análisis puntual ya no ejecutable tal cual
# desde antes de este cambio -- no está en cron, no se toca.
comprimir_dir data/sports "activity_ws_*.csv"

# 05-Oct (disco al 91 %): dispersed_bot_executor_dryrun.csv (append-only, 1,2 GB,
# ~30 MB/día, sus lectores leen TODO el histórico) se rota a diario a partes
# .csv.gz en datalogs/csv_rotados/ -- sin pérdida: los lectores lo abren con
# csv_rotado.abrir() (partes + fichero vivo, mismas líneas en el mismo orden).
nice -n 15 /usr/bin/python3 /root/polymarket-research/csv_rotado.py rotar data/shadow/dispersed_bot_executor_dryrun.csv || echo "ERROR rotando dispersed_bot_executor_dryrun.csv"

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
borrar_gz_antiguos data/sports "activity_ws_*.csv"

cd /root/polymarket-research-datalogs
# 05-Oct: maker_ms_*.csv.gz (registro ms de libro_estado_ws, ~1 GB/día desde 16:20Z, ya nace en gz): retención 4 días.
# 17-Oct (OK Javi): ya NO se borran -- se MUEVEN al volumen (única fuente de la cola por niveles, filas l/L) y allí
# se borran a 30 días (~1 GB/día). Solo se borra el local si la copia del volumen tiene el mismo tamaño (fail-safe:
# si la copia falla, el fichero se queda en local y se reintenta mañana).
MS_VOL=/mnt/HC_Volume_106538179/maker_ms_crudo
if mountpoint -q /mnt/HC_Volume_106538179 && mkdir -p "$MS_VOL" 2>/dev/null; then   # nunca en el raíz si no está montado
  # retención ANTES de copiar (con el volumen casi lleno, la copia fallaría antes de liberar nada)
  find "$MS_VOL" -maxdepth 1 -name 'maker_ms_*.csv.gz' -mtime +30 -print -delete || true
  find "$MS_VOL" -maxdepth 1 -name '*.tmp' -mmin +120 -print -delete || true
  # 17-Oct: libro5_ms (feed crudo 5m de libro_estado_ws, se escribe YA en el volumen): 14 días como máximo
  L5=/mnt/HC_Volume_106538179/libro5_ms
  if [ -d "$L5" ]; then
    find "$L5" -maxdepth 1 -name 'libro5_ms_*.csv.gz' -mtime +14 -print -delete || true   # el escritor también borra: una carrera no aborta el script (set -e)
    # (el tamaño lo acota el propio escritor: presupuesto de 20 GB; aquí solo la retención por días)
  fi
  find /root/polymarket-research-datalogs -maxdepth 1 -name 'maker_ms_*_*.csv.gz' -mtime +4 -print0 |
  while IFS= read -r -d '' f; do
    b=$(basename "$f")
    if [ ! -f "$MS_VOL/$b" ] || [ "$(stat -c %s "$MS_VOL/$b")" -ne "$(stat -c %s "$f")" ]; then
      nice -n 19 ionice -c3 cp -p "$f" "$MS_VOL/$b.tmp" && mv "$MS_VOL/$b.tmp" "$MS_VOL/$b"
    fi
    if [ -f "$MS_VOL/$b" ] && [ "$(stat -c %s "$MS_VOL/$b")" -eq "$(stat -c %s "$f")" ]; then
      rm -f "$f" && echo "movido al volumen: $b"
    else
      echo "⚠ NO movido al volumen (copia fallida, se queda en local): $b"
    fi
  done
else
  echo "⚠ volumen no disponible: maker_ms se quedan en local (no se borran)"
fi
# 05-Oct: onchain_fills_*.csv.gz (fetch_polymarket_fills_onchain.py, ~315 MB/día, maker/tomador explícitos): 4 días.
find /root/polymarket-research-datalogs -maxdepth 1 -name 'onchain_fills_*.csv.gz' -mtime +4 -print -delete
# 07-Oct: requote_mejora_sombra_*.csv (registro en sombra de live_trade, pocas filas/día): gz a 3 días, borrar a 120 días.
comprimir_dir . "requote_mejora_sombra_*.csv" "$CUTOFF_COMPRIMIR_DATALOGS"
find /root/polymarket-research-datalogs -maxdepth 1 -name 'requote_mejora_sombra_*.csv.gz' -mtime +120 -print -delete
borrar_gz_antiguos . "polymarket_activity_*.csv"
borrar_gz_antiguos . "libro_ambos_lados_*.csv"
borrar_gz_antiguos . "libro_book_ws_*.csv"

echo "=== DONE ==="
df -h / | tail -1
# 05-Oct: hl_ctx_* (~3,5 MB/día) y hl_posiciones_* (~0,6 MB/día) de fetch_hyperliquid_perps.py, ya nacen en gz: 60 días.
find /root/polymarket-research-datalogs -maxdepth 1 -name 'hl_ctx_*.csv.gz' -mtime +60 -print -delete
find /root/polymarket-research-datalogs -maxdepth 1 -name 'hl_posiciones_*.csv.gz' -mtime +60 -print -delete
