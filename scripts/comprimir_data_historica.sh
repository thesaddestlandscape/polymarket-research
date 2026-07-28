#!/bin/bash
# Comprime en el sitio (gzip) los CSV diarios de data/markets, data/wallets
# y data/trades más antiguos que $DIAS_MANTENER, verificando la integridad
# (comparación byte a byte tras descomprimir) antes de borrar el original.
# Un solo uso, 28-Jul, decisión explícita Javi tras barrido de disco (90% uso).
set -euo pipefail
cd /root/polymarket-research

DIAS_MANTENER=5
CUTOFF=$(date -u -d "-${DIAS_MANTENER} days" +%Y-%m-%d)

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
    if [[ "$fecha" > "$CUTOFF" || "$fecha" == "$CUTOFF" ]]; then
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

comprimir_dir data/markets "*.csv"
comprimir_dir data/wallets "leaderboard_*.csv"
comprimir_dir data/wallets "positions_*.csv"
comprimir_dir data/trades "*.csv"

echo "=== DONE ==="
df -h / | tail -1
