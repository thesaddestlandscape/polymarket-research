#!/usr/bin/env bash
# live_switch.sh — Activa o desactiva el live trading manualmente.
#
# Uso:
#   bash live_switch.sh on    → activa  (crea data/live/LIVE_MODE_ON)
#   bash live_switch.sh off   → desactiva
#   bash live_switch.sh       → muestra estado actual

SWITCH="$(dirname "$0")/data/live/LIVE_MODE_ON"

case "${1,,}" in
  on)
    touch "$SWITCH"
    echo "✅ LIVE MODE: ON — el bot puede operar dentro de las ventanas horarias."
    ;;
  off)
    rm -f "$SWITCH"
    echo "🛑 LIVE MODE: OFF — bot en shadow mode únicamente."
    ;;
  *)
    if [ -f "$SWITCH" ]; then
      echo "✅ LIVE MODE: ON"
    else
      echo "❌ LIVE MODE: OFF"
    fi
    python3 "$(dirname "$0")/live_guard.py" 2>/dev/null || true
    ;;
esac
