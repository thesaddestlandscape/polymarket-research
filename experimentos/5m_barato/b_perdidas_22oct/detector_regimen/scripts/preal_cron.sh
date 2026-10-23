#!/bin/bash
# PROPUESTA de cron (NO instalado; lo decide el chief): 30 10 * * *  (fuera de 06-09Z; m5_registro_D lo deja listo el extractor ~04:00-04:20Z, etiquetas de regimen 00:25Z).
# Extrae el estado REAL del libro (ask/bid/print) en la decision de TODA ventana 5m x moneda x token del dia D-1, resuelve desenlace oficial (gamma closed=true) y reevalua H1-REAL FORWARD (dias >= 2026-10-23).
# Salidas (fuera de git): /root/polymarket-research-datalogs/preal/ask_t0_D.csv.gz (+manifest), desenl_cache.json, informe_forward_ultimo.txt. Retencion: 400 d (borra ask_t0_* mas viejos); ~0,25 MB/dia.
ulimit -v 3000000
S=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/scripts; OUT=/root/polymarket-research-datalogs/preal; LOG=$OUT/cron.log
D=${1:-$(date -u -d "yesterday" +%F)}
{
 echo "== $(date -u +%FT%TZ) preal $D"
 if [ ! -f /mnt/HC_Volume_106538179/m5_registro/m5_registro_$D.csv.gz ]; then echo "SIN m5_registro_$D (extractor fallido? ver logs/extraer_registro_5m_barato.log); se puede usar --src maker_ms_$D*.csv.gz"; exit 4; fi
 flock -n /tmp/preal.lock nice -n 19 ionice -c3 python3 -I $S/preal_extrae.py $D || exit 5
 nice -n 19 ionice -c3 python3 -I $S/preal_resolver.py $D
 nice -n 19 ionice -c3 python3 -I $S/preal_analisis.py --desde 2026-10-23 --hasta $D --forward --salida $OUT/informe_forward_ultimo.txt > /dev/null
 find $OUT -name 'ask_t0_*' -mtime +400 -delete
} >> $LOG 2>&1 || echo "preal_cron FALLO $D (ver $LOG)" >> $LOG
