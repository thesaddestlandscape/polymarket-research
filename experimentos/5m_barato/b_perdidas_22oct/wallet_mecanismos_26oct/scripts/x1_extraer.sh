#!/bin/bash
# x1: extrae, por día, TODAS las filas on-chain 5m de las tx donde aparecen W (pspspsps5) o MM (mo-money),
# y el mapa token->mercado (filas k de los registros m5/m15). Solo lectura del archivo. Idempotente (salta lo hecho).
# Espera a load5<8 y MemAvailable>2,5 GB (autorización Javi 26-Oct, VPS 8 núcleos) antes de cada día. Uso: nice -n 19 ionice -c3 bash x1_extraer.sh
V=/mnt/HC_Volume_106538179; D=/root/polymarket-research-datalogs/wallet_mecanismos_26oct
W=0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5; MM=0x32ed2e546b187ca15e2841edc82b22c713cf8ec3
ulimit -v 3000000
espera() { while :; do h=$(date -u +%H%M); l=$(cut -d' ' -f2 /proc/loadavg); if [ "$h" -ge 0600 ] && [ "$h" -lt 0930 ]; then sleep 300; continue; fi; m=$(awk "/MemAvailable/{print \$2}" /proc/meminfo); awk -v l=$l -v m=$m "BEGIN{exit !(l<8.0 && m>2600000)}" && break; sleep 60; done; }
for f in $V/m5_registro/m5_registro_2026-10-*.csv.gz; do
  o=$D/k_$(basename $f .csv.gz).csv; [ -s $o ] && continue; espera
  zcat $f 2>/dev/null | grep '^k,' | awk -F, '$5=="5min"||$5=="15min"' | sort -u -t, -k3,3 > $o.tmp && mv $o.tmp $o; echo "k $f $(wc -l < $o)"
done
for f in $V/m5_onchain/m5_onchain_2026-10-*.csv.gz; do
  d=$(basename $f .csv.gz | sed 's/m5_onchain_//'); o=$D/tx_$d.csv.gz; [ -s $o ] && continue; espera
  zcat $f | grep -F -e $W -e $MM | cut -d, -f4 | sort -u > $D/txs_$d.txt
  ( zcat $f | head -1; zcat $f | grep -F -f $D/txs_$d.txt ) | gzip > $o.tmp && mv $o.tmp $o
  echo "tx $d txs=$(wc -l < $D/txs_$d.txt) filas=$(zcat $o | wc -l) $(date -u +%H:%M)"
done
echo FIN
