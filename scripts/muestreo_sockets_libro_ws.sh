#!/bin/bash
# Misión definitiva 15m §3 (07-Oct): ¿el retraso de cola del libro BTC (P90 423 ms) es del servidor o nuestro?
# Muestrea cada 0,2 s durante $1 s la Recv-Q/Send-Q de cada conexión del hijo de libro_estado_ws, el load y la CPU del
# hijo. Solo lectura (ss/ps). Salida: datalogs/muestreo_sockets_libro_ws_<fecha>.csv
DUR=${1:-1200}
OUT=/root/polymarket-research-datalogs/muestreo_sockets_libro_ws_$(date -u +%Y-%m-%dT%H%M).csv
echo "t_ms,pid,local,peer,recvq,sendq,load1,cpu_hijo" > "$OUT"
FIN=$(( $(date +%s) + DUR ))
while [ "$(date +%s)" -lt "$FIN" ]; do
  P=$(pgrep -f "libro_estado_ws.py --hijo" | head -1)
  T=$(date +%s%3N); L=$(cut -d' ' -f1 /proc/loadavg); C=$(ps -o pcpu= -p "$P" 2>/dev/null | tr -d ' ')
  ss -tnp 2>/dev/null | grep "pid=$P," | awk -v t="$T" -v p="$P" -v l="$L" -v c="$C" '{print t","p","$4","$5","$2","$3","l","c}' >> "$OUT"
  sleep 0.2
done
gzip -f "$OUT"
