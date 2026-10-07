#!/bin/bash
# Misión 15m §3-4 (OK Javi 07-Oct: T1/T2/T4, tope 5 $): repite T2+T4 en $1 ventanas 15m seguidas. Coste esperado 0 $.
# Se detiene si una pasada registra un T4_parada en el ledger (relleno o respuesta no reconocida).
N=${1:-4}
L=/root/polymarket-research-datalogs/medir_latencia_ordenes_15m_ledger.jsonl
for k in $(seq 1 "$N"); do
  sleep $(( (60 - $(date +%s) % 900 + 900) % 900 + 5 ))
  antes=$(grep -c '"T4_parada"' "$L" 2>/dev/null || echo 0)
  timeout 840 /root/polymarket-research/.venv/bin/python -u /root/polymarket-research/medir_latencia_ordenes_15m.py --t2 3 --t4 10 --confirmo-dinero-real >> /root/polymarket-research-datalogs/medir_latencia_t4_bucle.log 2>&1
  despues=$(grep -c '"T4_parada"' "$L" 2>/dev/null || echo 0)
  [ "$despues" -gt "$antes" ] && { echo "T4_parada nueva: fin del bucle" >> /root/polymarket-research-datalogs/medir_latencia_t4_bucle.log; exit 1; }
done
