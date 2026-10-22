#!/bin/bash
# run_h23_datos_diario.sh -- datos completos de H23, pasada DIARIA (22-Oct-2026). PROPUESTA de cron para el chief (NO instalada): 40 10 * * * (fuera de 06:00-09:15Z; tras controles 04:35 y archivos 04:xx)
#   cd /root/polymarket-research && bash -c "nice -n 19 ionice -c3 bash experimentos/5m_barato/h23_maker/v3/run_h23_datos_diario.sh" >> logs/h23_datos_diario.log 2>&1 || <aviso Telegram de fallo>
# Pasos (idempotentes, de uno en uno; cada uno valida su salida y no recalcula lo valido): (1) libro de huecos del registro maker_ms (log de observadores) ; (2) extraccion de alts del dia D=ayer
# (extrae_alts.sh + extrae_dogebnb.sh; BTC lo extrae/replaya ya vigia_h23_repuja) ; (3) replay v3 `registro` de las 5 alts ; (4) replay v3 `pares` de las 6 monedas SI existe registro propio ;
# (5) manifiesto de cobertura diaria ; (6) estadisticas por estado de cierre. Cualquier paso fallido => exit 2 (PARTIAL), nunca se oculta.
Z=/root/polymarket-research/experimentos/5m_barato/h23_maker/v3
V2=/root/polymarket-research/experimentos/5m_barato/h23_maker/v2
DL=/root/polymarket-research-datalogs
D=${1:-$(date -u -d "yesterday" +%F)}
H=$(date -u +%H%M)
if [ "$H" -ge 0600 ] && [ "$H" -lt 0915 ]; then echo "$(date -u +%FT%TZ) franja 06:00-09:15Z: no se ejecuta"; exit 3; fi
exec 9>$DL/h23_cobertura/diario.lock 2>/dev/null || { mkdir -p $DL/h23_cobertura; exec 9>$DL/h23_cobertura/diario.lock; }
flock -n 9 || { echo "$(date -u +%FT%TZ) ya hay una pasada en curso"; exit 0; }
log() { echo "$(date -u +%FT%TZ) $*"; }
rc=0
log "== H23 datos diario D=$D"
python3 -I $Z/h23_huecos_ws.py --guardar || { log "FALLO huecos"; rc=2; }
if [ ! -f $DL/vigia_5m_barato/controles_$D.csv ] || [ ! -f /mnt/HC_Volume_106538179/m5_registro/m5_registro_$D.csv.gz ]; then
  log "PARTIAL: faltan controles_$D.csv o m5_registro_$D (se crean ~04:35/04:2xZ del dia siguiente)"; rc=2
else
  ( ulimit -v 3000000; bash $V2/extrae_alts.sh $D && bash $V2/extrae_dogebnb.sh $D ) || { log "FALLO extraccion alts $D"; rc=2; }
  nice -n 19 python3 -I $Z/h23_job_replay.py --job h23_v3_alts_$D --fuente registro --monedas ETH,SOL,XRP,DOGE,BNB --dias $D:$D --respeta-otros || rc=2
  if ls /mnt/HC_Volume_106538179/h23_pares/h23_pares_*_$D.csv.gz >/dev/null 2>&1; then
    nice -n 19 python3 -I $Z/h23_job_replay.py --job h23_v3_pares_$D --fuente pares --monedas BTC,ETH,SOL,XRP,DOGE,BNB --dias $D:$D --respeta-otros || rc=2
  else log "sin registro propio de pares para $D (h23_shadow_v3r --registro-dir no desplegado)"; fi
fi
python3 -I $Z/h23_cobertura_diaria.py --dia $D || rc=2
python3 -I $Z/h23_estadisticas_datos.py --monedas BTC,ETH,SOL,XRP,DOGE,BNB --dias 2026-10-19:$D --reps 150,1500 > $DL/h23_cobertura/estadisticas_$D.txt 2>&1 || rc=2
log "fin rc=$rc"
exit $rc
