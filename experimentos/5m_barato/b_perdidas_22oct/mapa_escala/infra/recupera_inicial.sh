#!/bin/bash
# Recuperacion inicial OLA6/TP1-INFRA (una vez): re-extrae 22-Oct (5m/15m truncados) y respalda 60m/4h/24h de 18..22-Oct antes de que rote el on-chain.
cd "$(dirname "$0")" || exit 1
LOG=/mnt/HC_Volume_106538179/agentes_datos/mapa_infra/logs/recupera_inicial_$(date -u +%F).log; mkdir -p "$(dirname "$LOG")"
ulimit -v 3000000
for i in $(seq 1 90); do
  l=$(cut -d' ' -f2 /proc/loadavg); ok=$(awk -v l="$l" 'BEGIN{print (l<8.0)?1:0}')
  [ "$ok" = 1 ] && break; sleep 60
done
echo "=== $(date -u +%FT%TZ) load5=$(cut -d' ' -f2 /proc/loadavg) inicio" >> "$LOG"
[ "$ok" = 1 ] || { echo "load5>=8 tras 90 min: NO se ejecuta (BLOCKED)" >> "$LOG"; exit 9; }
for d in 2026-10-18 2026-10-19 2026-10-20 2026-10-21 2026-10-22; do
  nice -n 19 ionice -c3 /root/polymarket-research/.venv/bin/python extrae_onchain_ext.py $d >> "$LOG" 2>&1; echo "rc=$? $d" >> "$LOG"
done
echo "=== $(date -u +%FT%TZ) fin" >> "$LOG"
