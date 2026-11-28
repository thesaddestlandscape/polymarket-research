#!/bin/bash
# run_btc_mapa_28nov.sh -- estado por moneda con el mapa gamma de BTC (dias 18,24,25,26-Nov) por cron_pesado (cola global), ulimit 3 GB, nice 19. 0 ordenes, 0 red. Fuera de 06:00-09:30Z, 22:00-02:45Z y 11:00-11:30Z.
H=/root/polymarket-research/experimentos/5m_barato/exp5bis_27nov; OUT=/root/polymarket-research-datalogs/exp5bis_27nov/paso3; CP=/root/polymarket-research/scripts/cron_pesado.sh
export OPENBLAS_NUM_THREADS=1 MALLOC_ARENA_MAX=1 PYTHONDONTWRITEBYTECODE=1
LOG=$OUT/run_btc_mapa.log; ts() { date -u +%FT%TZ; }
for D in 2026-11-18 2026-11-24 2026-11-25 2026-11-26; do
  [ -s $OUT/estado_monedas_btc_$D.json ] && { echo "$(ts) $D ya hecho" >> $LOG; continue; }
  while :; do h=$((10#$(date -u +%H%M))); if { [ $h -ge 600 ] && [ $h -lt 930 ]; } || [ $h -ge 2200 ] || [ $h -lt 245 ] || { [ $h -ge 1100 ] && [ $h -lt 1130 ]; }; then sleep 60; else break; fi; done
  echo "$(ts) btc mapa $D INICIO" >> $LOG
  $CP bash -c "ulimit -v 3000000; cd $H; exec nice -n 19 ionice -c3 python3 -I -B -u btc_mapa_gamma_28nov.py $D" >> $LOG 2>&1
  [ -s $OUT/estado_monedas_btc_$D.json ] && echo "$(ts) $D OK" >> $LOG || echo "$(ts) $D FALLO (sin json)" >> $LOG
done
echo "$(ts) FIN" >> $LOG
