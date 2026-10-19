#!/bin/bash
# Etapa 1 (lanzar NO antes de 09:16Z): kmap 08-12, fills on-chain 5m (parquet) y filas t/x del registro ms (14-18 primero).
# Idempotente (salta lo que ya existe). Un proceso a la vez; nice 19 ionice idle; ulimit -v 1,5 GB; espera si hay poca RAM o carga alta.
C=/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct
SP=/tmp/claude-0/-root-polymarket-research/ce552a77-92f9-49c1-8c13-d01ef139d7f6/scratchpad
H=/root/polymarket-research/experimentos/5m_barato/wallets_18oct
LOG=$H/stage1.log
ulimit -v 1500000
esperar() {
  for i in $(seq 1 120); do
    av=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); ld=$(awk '{print int($1)}' /proc/loadavg)
    if [ "$av" -gt 1300 ] && [ "$ld" -lt 24 ]; then return 0; fi
    echo "$(date -u +%H:%M:%S) espera: MemAvailable=${av}MB load=${ld}" >> $LOG; sleep 60
  done
  return 0
}
# esperar a las 09:16Z
while [ "$(date -u +%H%M)" -lt 0916 ] && [ "$(date -u +%H)" -lt 12 ]; do sleep 30; done
echo "$(date -u +%FT%TZ) inicio etapa 1" >> $LOG
for d in 2026-10-13 2026-10-14 2026-10-15 2026-10-16 2026-10-17 2026-10-18; do [ -f $C/kmap_$d.txt ] || cp $SP/kmap_$d.txt $C/; done
for d in 2026-10-08 2026-10-09 2026-10-10 2026-10-11 2026-10-12; do
  if [ ! -f $C/kmap_$d.txt ]; then esperar; nice -n 19 ionice -c3 bash -c "zcat /mnt/HC_Volume_106538179/m15_registro/m15_registro_$d.csv.gz 2>/dev/null | grep -a '^k,' | grep -a ',5min,' > $C/kmap_$d.txt"; echo "$(date -u +%H:%M:%S) kmap $d $(wc -l < $C/kmap_$d.txt)" >> $LOG; fi
done
for d in 2026-10-18 2026-10-17 2026-10-16 2026-10-15 2026-10-14 2026-10-13 2026-10-12 2026-10-11 2026-10-10 2026-10-09; do
  if [ ! -f $C/fills_$d.parquet ]; then esperar; nice -n 19 ionice -c3 python3 -I $H/extrae_fills.py $d >> $LOG 2>&1; fi
done
for d in 2026-10-18 2026-10-17 2026-10-16 2026-10-15 2026-10-14; do
  if [ ! -f $C/tx_$d.csv.gz ]; then esperar; nice -n 19 ionice -c3 bash -c "zcat /mnt/HC_Volume_106538179/m5_registro/m5_registro_$d.csv.gz | grep -a -E '^(t|x),' | gzip -1 > $C/tx_$d.csv.gz.tmp && mv $C/tx_$d.csv.gz.tmp $C/tx_$d.csv.gz"; echo "$(date -u +%H:%M:%S) tx $d $(ls -la $C/tx_$d.csv.gz | awk '{print $5}')" >> $LOG; fi
done
echo "$(date -u +%FT%TZ) FIN etapa 1 (14-18 tx; 09-18 fills)" >> $LOG
