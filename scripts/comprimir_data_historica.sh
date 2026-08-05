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
set -euo pipefail

DIAS_MANTENER=5
DIAS_BORRAR=90
CUTOFF_COMPRIMIR=$(date -u -d "-${DIAS_MANTENER} days" +%Y-%m-%d)
CUTOFF_BORRAR=$(date -u -d "-${DIAS_BORRAR} days" +%Y-%m-%d)

comprimir_dir() {
  local dir="$1" patron="$2"
  for f in "$dir"/$patron; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    fecha=$(echo "$base" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)
    if [ -z "$fecha" ]; then
      echo "SKIP (sin fecha en nombre): $f"
      continue
    fi
    if [[ "$fecha" > "$CUTOFF_COMPRIMIR" || "$fecha" == "$CUTOFF_COMPRIMIR" ]]; then
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

cd /root/polymarket-research-datalogs
comprimir_dir . "polymarket_activity_*.csv"
comprimir_dir . "libro_ambos_lados_*.csv"

cd /root/polymarket-research
borrar_gz_antiguos data/markets "*.csv"
borrar_gz_antiguos data/wallets "leaderboard_*.csv"
borrar_gz_antiguos data/wallets "positions_*.csv"
borrar_gz_antiguos data/trades "*.csv"
borrar_gz_antiguos data/prices "chainlink_*.csv"

cd /root/polymarket-research-datalogs
borrar_gz_antiguos . "polymarket_activity_*.csv"
borrar_gz_antiguos . "libro_ambos_lados_*.csv"

echo "=== DONE ==="
df -h / | tail -1
