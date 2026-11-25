#!/bin/bash
# lanzar.sh - orquestador reanudable e idempotente (checkpoint por dia) de CF1 (prereg d74fae89) + rejilla H3 + tb.py por dia.
# Solo lectura de datos publicos on-chain/registro; sin dinero, sin produccion. Salidas voluminosas en out/ (ignoradas por git).
# Recursos: nice 19 + ionice -c3 heredados, ulimit -v 3 GB; nunca 06:00-09:30Z; MemAvailable >= 2500 MB; load5 < 4 preferente y,
# tras 20 min con la ventana abierta, load5 < 8 (= nproc; autorizacion de Javi 26-Oct recogida en el prereg CF1 §8).
# Plazo duro 2026-11-07T05:50Z: si no termina, deja PARCIAL en out/estado.log.
B=/root/polymarket-research/experimentos/5m_barato/banda_0_30/cf1
O=$B/out; K=$O/k; mkdir -p $O $K
V=/mnt/HC_Volume_106538179
TB=/root/polymarket-research/experimentos/5m_barato/re_enjambre_05nov/tb.py
LOG=$O/estado.log
[ -f $O/.gitignore ] || printf '*\n!.gitignore\n!resultado.txt\n!resultado.json\n!estado.log\n!agg.log\n' > $O/.gitignore
renice -n 19 -p $$ >/dev/null 2>&1; ionice -c3 -p $$ >/dev/null 2>&1
ulimit -v 3000000
log(){ echo "$(date -u +%FT%TZ) $*" >> $LOG; }
FO=""
puerta(){
  local hm=$((10#$(date -u +%H%M)))
  if [ $hm -ge 600 ] && [ $hm -lt 930 ]; then FO=""; return 1; fi
  local ma=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo)
  [ "$ma" -lt 2500 ] && return 1
  local l5=$(cut -d' ' -f2 /proc/loadavg) now=$(date +%s)
  [ -z "$FO" ] && FO=$now
  awk -v l="$l5" 'BEGIN{exit !(l<4)}' && return 0
  [ $((now-FO)) -ge 1200 ] && awk -v l="$l5" 'BEGIN{exit !(l<8)}' && return 0
  return 1
}
LIM=$(date -d '2026-11-07T05:50:00Z' +%s)
esperar(){
  while ! puerta; do
    [ $(date +%s) -ge $LIM ] && { log "PARCIAL: plazo agotado esperando la puerta de recursos"; exit 3; }
    sleep 60
  done
}
DIAS=$(ls $V/m5_onchain/ | sed -n 's/^m5_onchain_\(2026-[0-9-]*\)\.csv\.gz$/\1/p' | sort)
log "inicio pid $$; dias m5_onchain: $(echo $DIAS | wc -w) ($(echo $DIAS | cut -d' ' -f1)..$(echo $DIAS | awk '{print $NF}'))"
for D in $DIAS; do
  f=$K/k${D:8:2}.csv
  [ -s $f ] && continue
  esperar
  if [ -f $V/m5_registro/m5_registro_$D.csv.gz ]; then
    zcat $V/m5_registro/m5_registro_$D.csv.gz | grep -a '^k,' | sort -u > $f.tmp && mv $f.tmp $f
    log "k $D filas $(wc -l < $f) load5 $(cut -d' ' -f2 /proc/loadavg)"
  else log "k $D SIN m5_registro"; fi
done
esperar
python3 $B/cf1_dia.py MAPA $O $K >> $LOG 2>&1 || { log "ERROR mapa"; exit 2; }
for D in $DIAS; do
  if [ ! -s $O/tb_$D.txt ]; then
    esperar; python3 $TB $D $K > $O/tb_$D.txt.tmp 2>> $LOG && mv $O/tb_$D.txt.tmp $O/tb_$D.txt || log "ERROR tb $D"
  fi
  if [ ! -s $O/dia_$D.json ]; then
    esperar; python3 $B/cf1_dia.py $D $O >> $LOG 2>&1 || log "ERROR cf1_dia $D"
  fi
done
python3 $B/agg.py $O > $O/agg.log 2>&1 && log "COMPLETO (agg.py ok)" || log "ERROR agg.py"
