#!/bin/bash
# Backfill idempotente de dec2_D/dec3s100_D (misma cadena que forward_calma.sh: prep_day -> esc_dec2 -> esc_dec2 con EXTRA_SHIFT_MS=100). DEV, solo lectura de datalogs, 0 ordenes.
# UN dia por pasada (el mas antiguo pendiente de DIAS). Se NIEGA a correr: 06:00-09:30Z, load5/nproc>0.5, MemAvailable<4 GB, / libre <2 GB, o con otro backfill/forward_calma vivo.
# Dia sin entradas => BLOCKED explicito (estado/<D>.json), nunca "procesado". Reanudable: prep_day/esc_dec2 saltan lo ya hecho (tmp+os.replace).
DIAS=${DIAS:-"2026-10-25"}   # 17-23 Oct bloqueados: sin libro5_tx (arranca 24-Oct); <17-Oct sin ms_D.npz ni maker_ms (arranca 19-Oct)
B=/root/polymarket-research/misiones/5m_barato/backfill_dec2; P2=/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2; DC=$P2/A3_guarda/ret_cinta_corregida/descomp; DL=/root/polymarket-research-datalogs
mkdir -p $B/estado; LOG=$B/backfill.log; log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
exec 8>/tmp/backfill_dec2.lock; flock -n 8 || { log "otro backfill vivo"; exit 0; }
hm=$(date -u +%H%M); { [ "$hm" -ge 0600 ] && [ "$hm" -le 0930 ]; } && { log "NO: ventana 06:00-09:30Z"; exit 0; }
l5=$(awk '{print $2}' /proc/loadavg); nc=$(nproc); awk -v l=$l5 -v n=$nc 'BEGIN{exit !(l/n>0.5)}' && { log "NO: load5=$l5 nproc=$nc"; exit 0; }
ma=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo); [ "$ma" -lt 4096 ] && { log "NO: MemAvailable=${ma}MB"; exit 0; }
lib=$(df --output=avail -BM / | tail -1 | tr -dc 0-9); [ "$lib" -lt 2048 ] && { log "NO: disco / libre ${lib}MB"; exit 0; }
pgrep -f "forward_calma.sh|esc_dec2.py" >/dev/null && { log "NO: forward_calma/esc_dec2 en marcha"; exit 0; }
est() { python3 -I -c "import json,sys;json.dump(dict(dia='$1',estado='$2',detalle='$3',hora='$(date -u +%FT%TZ)'),open('$B/estado/$1.json','w'))"; }
for D in $DIAS; do
  [ -f $DC/out/dec2_$D.pkl ] && [ -f $DC/out/dec3s100_$D.pkl ] && continue
  falta=""; [ -s $DL/sa_ms/ms_$D.npz ] || falta="$falta ms_$D.npz"
  ls $DL/keep_onchain_re_as_b/onchain_fills_$D*.csv.gz /mnt/HC_Volume_106538179/m5_onchain/m5_onchain_$D.csv.gz >/dev/null 2>&1 || falta="$falta onchain"
  [ -s $P2/clave_cancelacion/out/x_$D.csv.gz ] || [ -s $P2/A3_guarda/fwd/x_$D.csv.gz ] || falta="$falta x_$D"
  ls /mnt/HC_Volume_106538179/libro5_tx/libro5_tx_${D}_*.csv.gz >/dev/null 2>&1 || falta="$falta libro5_tx"
  [ -n "$falta" ] && { log "$D BLOCKED:$falta"; est $D BLOCKED "$falta"; continue; }
  log "$D inicio"; ( ulimit -v 3000000; export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    set -e; nice -n 19 ionice -c3 python3 -I $B/prep_day_bf.py $D
    cd $DC; nice -n 19 ionice -c3 python3 -I esc_dec2.py $D; EXTRA_SHIFT_MS=100 nice -n 19 ionice -c3 python3 -I esc_dec2.py $D ) >> $LOG 2>&1; rc=$?
  h=$(python3 -I -c "import json;print(24-len(json.load(open('$P2/precursores_barrido/out/bad_$D.json'))['bad']))" 2>/dev/null)
  if [ $rc -eq 0 ] && [ -f $DC/out/dec2_$D.pkl ] && [ -f $DC/out/dec3s100_$D.pkl ]; then log "$D COMPLETE horas_sanas=$h"; est $D COMPLETE "horas_sanas=$h"; else log "$D FAILED rc=$rc"; est $D FAILED "rc=$rc"; fi
  break   # un dia por pasada
done
log "pasada fin: $(for D in $DIAS; do [ -f $DC/out/dec2_$D.pkl ] && echo -n "$D:ok " || echo -n "$D:falta "; done)"
