#!/bin/bash
# supervisor_exp1.sh (15-Nov 18:40Z). Lanza run_exp1.sh por la cola pesada SOLO con la maquina compartida en calma (load1<=8 y MemAvailable>=3500 MB, 2 comprobaciones seguidas a 45 s)
# y lo relanza (max 4 veces) si el orquestador muere sin su linea FIN (p. ej. OOM-killer). Plazo duro: no lanza nada a partir de las 01:30Z (deploy v3 04:10Z). No toca produccion; no instala nada.
H=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1; SL=$H/supervisor.log; cd $H || exit 9
echo "$(date -u +%FT%TZ) supervisor pid $$ inicio" >> $SL
for intento in 1 2 3 4; do
  ok=0
  while [ $ok -lt 2 ]; do
    h=$(date -u +%H%M)
    if [ "$h" -ge 0130 ] && [ "$h" -lt 0915 ]; then echo "$(date -u +%FT%TZ) plazo agotado (>=01:30Z) sin lanzar/relanzar: se detiene" >> $SL; exit 2; fi
    l=$(awk '{print $1}' /proc/loadavg); a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
    if awk -v l="$l" 'BEGIN{exit !(l<=8.0)}' && [ "${a:-0}" -ge 3500 ]; then ok=$((ok+1)); else ok=0; fi
    [ $ok -lt 2 ] && sleep 45
  done
  echo "$(date -u +%FT%TZ) intento $intento: calma (load1 $l, MemAvailable $a MB) -> lanzo run_exp1.sh por la cola pesada" >> $SL
  /root/polymarket-research/scripts/cron_pesado.sh nice -n 19 ionice -c3 bash $H/run_exp1.sh
  if tail -1 $H/run_exp1.log | grep -q "===== FIN run_exp1"; then echo "$(date -u +%FT%TZ) orquestador termino con su linea FIN: supervisor OK" >> $SL; exit 0; fi
  echo "$(date -u +%FT%TZ) el orquestador murio sin linea FIN (OOM-killer?): espero calma y relanzo (idempotente)" >> $SL; sleep 90
done
echo "$(date -u +%FT%TZ) 4 intentos agotados sin FIN" >> $SL; exit 3
