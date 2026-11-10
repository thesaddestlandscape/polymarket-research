#!/bin/bash
# Espera a las 09:16Z (fuera de la franja 06:00-09:15Z) y lanza la aceptacion de quemados detras de la cola pesada global.
while true; do m=$(date -u +%H%M); [ "$((10#$m))" -ge 916 ] && [ "$((10#$m))" -lt 2200 ] && break; sleep 60; done
exec /root/polymarket-research/scripts/cron_pesado.sh bash /root/polymarket-research/experimentos/5m_barato/db1/aceptacion_quemados.sh
