#!/bin/bash
# runner idempotente p1 + p7 (RE-B-COLA-CANCELA, ADENDA_06/07): un dia cada vez, cola global de pesados, nice19/ionice3, ulimit 3 GB.
# DIAS DEL VEREDICTO: solo 13, 14, 15, 17, 18 y 19-Nov. 12 y 16-Nov SOLO con la etiqueta DISENO: `P1_DISENO=1 ./run_p1.sh` (salida *_DISENO, nunca la lee p3 de veredicto).
# Un dia solo se procesa si esta COMPLETO (cierre 24 h UTC + 20 min, y existen onchain_fills y m5_registro de D+1); si no, se espera (nunca parcial).
# Tras p1 se ejecuta p7 (balance E + pesos; no lee desenlaces) -> out/p7_btc_D.json y out/p7w_btc_D.pkl. p3 NO se lanza aqui.
cd "$(dirname "$0")"
if [ "${P1_DISENO:-0}" = "1" ]; then DIAS="2026-11-12 2026-11-16"; SUF="_DISENO"; else DIAS="2026-11-13 2026-11-14 2026-11-15 2026-11-17 2026-11-18 2026-11-19"; SUF=""; fi
for D in $DIAS; do
  [ -f out/p1_btc_$D$SUF.pkl ] && [ -f out/p7w_btc_$D$SUF.pkl ] && continue
  DN=$(date -u -d "$D +1 day" +%F)
  if [ $(date -u +%s) -lt $(date -u -d "$DN 00:20" +%s) ]; then echo "$(date -u +%FT%TZ) $D aun no completo (cierre 24 h UTC): se espera" >> out/run_p1.log; continue; fi
  if [ ! -s /root/polymarket-research-datalogs/onchain_fills_$DN.csv.gz ] || [ ! -s /mnt/HC_Volume_106538179/m5_registro/m5_registro_$DN.csv.gz ]; then echo "$(date -u +%FT%TZ) $D sin onchain/m5_registro de $DN: se espera" >> out/run_p1.log; continue; fi
  for i in $(seq 1 20); do l=$(cut -d' ' -f2 /proc/loadavg); a=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
    awk -v l=$l 'BEGIN{exit !(l<4)}' && [ $a -gt 2500 ] && break; sleep 30; done
  h=$(date -u +%H); if [ $h -ge 6 ] && [ $h -lt 9 ]; then echo "franja 06-09Z: paro" ; exit 0; fi
  if [ ! -f out/p1_btc_$D$SUF.pkl ]; then
    echo "$(date -u +%FT%TZ) inicio p1 $D$SUF load=$(cut -d' ' -f2 /proc/loadavg)" >> out/run_p1.log
    PISTA_SUF=$SUF /root/polymarket-research/scripts/cron_pesado.sh bash -c "ulimit -v 3000000; nice -n 19 ionice -c3 python3 p1_dia.py $D btc" >> out/run_p1.log 2>&1
  fi
  if [ -f out/p1_btc_$D$SUF.pkl ]; then
    echo "$(date -u +%FT%TZ) inicio p7 $D$SUF" >> out/run_p1.log
    /root/polymarket-research/scripts/cron_pesado.sh bash -c "ulimit -v 3000000; nice -n 19 ionice -c3 python3 p7_ipw_balance.py out/p1_btc_$D$SUF.pkl out/p7_btc_$D$SUF.json out/p7w_btc_$D$SUF.pkl" > out/p7_stdout_$D$SUF.txt 2>> out/run_p1.log
  fi
done
echo "$(date -u +%FT%TZ) runner FIN" >> out/run_p1.log
