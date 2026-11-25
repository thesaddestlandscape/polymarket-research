#!/bin/bash
# Cadena ADENDA_11 (19-Nov): fixture p1 -> comparacion con fxN1 -> p7/p3/checks_H sobre el fixture -> p1+p7 de 12-Nov DISENO -> p1+p7 de 16-Nov DISENO -> SMD absr5 antes/despues -> checks_H --final.
# UN trabajo a la vez (scripts/cron_pesado.sh: flock global + RAM), nice 19, ionice -c3, ulimit -v 3 GB. No arranca ningun paso en 06:00-09:00Z ni 22:15-22:30Z. NO procesa dias de veredicto.
# Idempotente: cada paso se salta si su salida ya existe (el pkl se escribe atomico al final). Estado final en out/verif_adenda11/chain.status (COMPLETE | FAILED_<paso>), log en chain.log.
cd "$(dirname "$0")/../.."; P=$(pwd); V=out/verif_adenda11; LOG=$V/chain.log; ST=$V/chain.status
FX=/root/polymarket-research-datalogs/pista_cola_18nov/fx3h/fx3h.csv.gz; CP=/root/polymarket-research/scripts/cron_pesado.sh
say() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
fail() { say "FALLO en $1"; echo "FAILED_$1 $(date -u +%FT%TZ)" > $ST; exit 1; }
ventana() { while true; do hm=$(date -u +%H%M); if { [ $hm -ge 0600 ] && [ $hm -lt 0900 ]; } || { [ $hm -ge 2215 ] && [ $hm -lt 2230 ]; }; then sleep 60; else break; fi; done; }
heavy() { local nm=$1; shift; ventana; say "inicio $nm"; $CP bash -c "ulimit -v 3000000; nice -n 19 ionice -c3 $*" >> $V/$nm.log 2>&1; local rc=$?; say "fin $nm rc=$rc"; return $rc; }
echo "RUNNING $(date -u +%FT%TZ)" > $ST; say "cadena ADENDA_11 inicio (pid $$)"
# 1) fixture p1 v11
if [ ! -f out/p1_btc_2026-11-12_fxP1.pkl ]; then heavy p1_fxP1 "env PISTA_SUF=_fxP1 PISTA_FILES=$FX python3 p1_dia.py 2026-11-12 btc"; [ -f out/p1_btc_2026-11-12_fxP1.pkl ] || fail p1_fxP1; fi
python3 -I $V/cmp_fx_p1.py > $V/cmp_fx_p1.out 2>&1 || fail cmp_fx_p1; say "fixture identico a fxN1 salvo absr5/r5/absr5_rx (cmp_fx_p1.json)"
# 2) p7 + p3 + checks_H sobre el fixture
if [ ! -f out/p7w_btc_2026-11-12_fxP1.pkl ]; then heavy p7_fxP1 "env P7_NOTE=fixture_fxP1 python3 p7_ipw_balance.py out/p1_btc_2026-11-12_fxP1.pkl out/p7_btc_2026-11-12_fxP1.json out/p7w_btc_2026-11-12_fxP1.pkl"; [ -f out/p7w_btc_2026-11-12_fxP1.pkl ] || fail p7_fxP1; fi
if [ ! -f out/p3_btc_act_fxP1_DISENO.json ]; then heavy p3_fxP1 "env P3_DISENO=1 PISTA_SUF=_fxP1 timeout 1500 python3 p3_agrega.py btc act"; [ -f out/p3_btc_act_fxP1_DISENO.json ] || fail p3_fxP1; fi
heavy checks_H "timeout 2400 python3 $V/checks_H.py"; [ -f $V/checks_H.json ] || fail checks_H
# 3) 12-Nov y 16-Nov DISENO (p1 + p7), uno a uno
for D in 2026-11-16 2026-11-12; do
  if [ ! -f out/p1_btc_${D}_DISENO.pkl ]; then heavy p1_$D "env PISTA_SUF=_DISENO python3 p1_dia.py $D btc"; [ -f out/p1_btc_${D}_DISENO.pkl ] || fail p1_$D; fi
  if [ ! -f out/p7w_btc_${D}_DISENO.pkl ]; then heavy p7_$D "env P7_NOTE=DISENO_ADENDA11 python3 p7_ipw_balance.py out/p1_btc_${D}_DISENO.pkl out/p7_btc_${D}_DISENO.json out/p7w_btc_${D}_DISENO.pkl"; [ -f out/p7w_btc_${D}_DISENO.pkl ] || fail p7_$D; fi
  [ $D = 2026-11-16 ] && say "LISTO_PARA_VALIDADOR fixture+16-Nov"
done
python3 -I $V/cmp_absr5.py > $V/cmp_absr5.out 2>&1 || fail cmp_absr5
# 4) comprobacion final de hashes (H1/H25) y cierre
heavy checks_H_final "timeout 2400 python3 $V/checks_H.py --final"; say "checks_H --final rc=$? (ver checks_H_final.json)"
echo "COMPLETE $(date -u +%FT%TZ)" > $ST; say "cadena COMPLETE"
