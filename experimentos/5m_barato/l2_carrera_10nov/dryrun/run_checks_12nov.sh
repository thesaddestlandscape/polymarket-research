#!/bin/bash
# Cadena de comprobaciones pesadas del 12-Nov (B replay, C/E anclas y bid-sin-nosotros, F Calma-T1 sello v3). SECUENCIAL, una a la vez, cada etapa bajo guard_rss.py (nice 19, ionice idle, ulimit -v 7 GB virtual,
# vigilancia del RSS REAL: mata solo SU pid si RSS > tope o MemAvailable < 1200 MB; solo arranca fuera de 06-09Z con load5<6 y MemAvailable>=2500). 0 ordenes, solo lectura de datos. Espera a las 09:00Z.
# Uso: run_checks_12nov.sh   (lanzar en segundo plano; logs en out_replay/chain_12nov/)
set -u
R=/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov; DR=$R/dryrun; LG=$DR/out_replay/chain_12nov; mkdir -p "$LG"
PY=python3
G="$PY $DR/guard_rss.py --esperar-min 240"
until [ "$(date -u +%H)" -ge 9 ] && [ "$(date -u +%H)" -lt 23 ]; do sleep 60; done
echo "$(date -u +%FT%TZ) inicio cadena" >> "$LG/cadena.log"
# S1: C y E (anclas rx de B, inventario canal usuario, bid sin nosotros)
$G --max-rss-mb 3200 -- $PY -I $R/l_real_11nov/l_directo_y_bidsn_12nov.py > "$LG/S1_C_E.log" 2>&1; echo "$(date -u +%FT%TZ) S1 rc=$?" >> "$LG/cadena.log"
# S2: F Calma-T1 con sello v3, dias 10-26..11-08, EXTRA_SHIFT 0 y 100
for d in 2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-01 2026-11-02 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07 2026-11-08; do
  for xs in 0 100; do
    EXTRA_SHIFT_MS=$xs CALMA_V3_OUT=$R/calma_v3/out/ $G --max-rss-mb 3200 -- $PY -I $R/calma_v3/esc_dec2_v3.py $d > "$LG/S2_F_${d}_xs${xs}.log" 2>&1; echo "$(date -u +%FT%TZ) S2 $d xs=$xs rc=$?" >> "$LG/cadena.log"
  done
done
# S3: runner (formato maker_ms) == modo B en proceso, datos reales ETH 14-17Z del 27-Oct + coste del placebo 100 / c59
$G --max-rss-mb 3000 -- $PY -I $DR/replay_runner_vs_modeB.py 2026-10-27 --coin ETH --horas 14 17 > "$LG/S3_runner_vs_B.log" 2>&1; echo "$(date -u +%FT%TZ) S3 rc=$?" >> "$LG/cadena.log"
# S4: modo A (exactitud del nucleo vs motor original), dia completo 27-Oct, con el tope RSS de 3,5 GB; si el guard lo mata (rc 97) se reintenta SOLO el subconjunto ETH 14-17 (el preambulo ya es el techo)
$G --max-rss-mb 3500 -- $PY -I $DR/replay_train.py 2026-10-27 --sin-ws > "$LG/S4_modoA_dia.log" 2>&1; rc=$?; echo "$(date -u +%FT%TZ) S4 rc=$rc" >> "$LG/cadena.log"
if [ "$rc" = 97 ]; then $G --max-rss-mb 3500 -- $PY -I $DR/replay_train.py 2026-10-27 --sin-ws --ks-sel ETH:14-17 > "$LG/S4b_modoA_subconjunto.log" 2>&1; echo "$(date -u +%FT%TZ) S4b rc=$?" >> "$LG/cadena.log"; fi
echo "$(date -u +%FT%TZ) FIN cadena" >> "$LG/cadena.log"
