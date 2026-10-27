#!/bin/bash
# extrae trades BTCUSDT (fila x) de m5_registro: columnas t_ms(c[...]), precio, qty, recepcion(c[7]). Solo lectura del registro.
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/huerfana_exante/datos
for d in 2026-10-18 2026-10-19 2026-10-20 2026-10-21 2026-10-22 2026-10-23; do
  nice -n 19 ionice -c3 bash -c "zcat /mnt/HC_Volume_106538179/m5_registro/m5_registro_$d.csv.gz | grep -a '^x,[0-9]*,BTCUSDT,' | cut -d, -f2,4,5,8 | gzip -1 > bn_btc_$d.csv.gz.tmp && mv bn_btc_$d.csv.gz.tmp bn_btc_$d.csv.gz"
  echo $d $(date -u +%T) >> extrae_binance.log
done
echo FIN >> extrae_binance.log
