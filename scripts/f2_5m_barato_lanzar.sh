#!/bin/bash
# Lanza/relanza los dos procesos DRY-RUN de F2 (5m barato). Guarda los PIDs en datalogs/f2_5m_barato/*.pid y mata SOLO esos
# PIDs (nunca pgrep/pkill -f: un comando que contiene el patrón se encuentra a sí mismo — trampa cazada 3 veces el 16-Oct).
# Uso: scripts/f2_5m_barato_lanzar.sh [btc|alt|ambos]   (por defecto ambos)
set -u
cd /root/polymarket-research || exit 1
D=/root/polymarket-research-datalogs/f2_5m_barato
mkdir -p "$D"
parar() {   # $1 = fichero pid; comprueba que el PID sigue siendo un python de F2 antes de matarlo
  local f="$1"
  [ -f "$f" ] || return 0
  local p; p=$(cat "$f")
  if [ -n "$p" ] && [ -r "/proc/$p/cmdline" ] && tr '\0' ' ' < "/proc/$p/cmdline" | grep -q "f2_5m_barato_dryrun.py"; then
    kill "$p"; sleep 4
  fi
  rm -f "$f"
}
que="${1:-ambos}"
if [ "$que" = "btc" ] || [ "$que" = "ambos" ]; then
  parar "$D/btc.pid"
  nohup nice -n -10 .venv/bin/python f2_5m_barato_dryrun.py --monedas BTC --cpu 3 --envio-inline >> logs/f2_5m_barato_btc.log 2>&1 &
  echo $! > "$D/btc.pid"
fi
if [ "$que" = "alt" ] || [ "$que" = "ambos" ]; then
  parar "$D/alt.pid"
  nohup nice -n 10 .venv/bin/python f2_5m_barato_dryrun.py --monedas ETH,SOL,XRP,DOGE,BNB --sin-firma >> logs/f2_5m_barato_alt.log 2>&1 &
  echo $! > "$D/alt.pid"
fi
cat "$D"/*.pid 2>/dev/null
