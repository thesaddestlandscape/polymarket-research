#!/bin/bash
# run_ident_v2v3_28nov.sh -- relanza la identidad del wrapper cobertura_bruta_v2v3 (dias 18 y 19-Nov) por cron_pesado, con log. 0 ordenes, 0 red.
R=/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/re_f5_23nov; OUT=/root/polymarket-research-datalogs/exp5bis_27nov/paso3; CP=/root/polymarket-research/scripts/cron_pesado.sh
LOG=$OUT/ident_v2v3_18_19_rerun.log
for D in 2026-11-18 2026-11-19; do
  while :; do h=$((10#$(date -u +%H%M))); if { [ $h -ge 600 ] && [ $h -lt 930 ]; } || [ $h -ge 2200 ] || [ $h -lt 245 ] || { [ $h -ge 1100 ] && [ $h -lt 1130 ]; }; then sleep 60; else break; fi; done
  echo "$(date -u +%FT%TZ) identidad $D INICIO" >> $LOG
  $CP bash -c "ulimit -v 3000000; cd $R; exec nice -n 19 ionice -c3 python3 -I -B -u cobertura_bruta_v2v3.py --identidad $D" >> $LOG 2>&1
done
echo "$(date -u +%FT%TZ) FIN" >> $LOG
