#!/bin/bash
# cron_cxb60_forward.sh {heartbeat|diario} -- operacion del forward B-CXB (PREREG_CXB_MULTIVARIANTE_FORWARD.md §7). Solo lectura sobre el runner; 0 ordenes. NO calcula EV ni puertas (prereg §6: entre miradas no se calculan);
#   las puertas solo salen de forward_gates.py --mirada N, a mano y por el validador.
#   heartbeat (*/5): vigia_cxb60_forward.py --heartbeat (ligero).  Un crash del vigia (rc>1) avisa UNA vez al dia por Telegram; rc=1 = problema ya avisado por el propio vigia (latch).
#   diario (10:55Z, tras sa_r1 10:40Z; envolver con scripts/cron_pesado.sh): 1) fuente de desenlace BTC D-1..D-3 (fwd_gmap_btc.py), 2) enlaza los gmap de sa_r1 (8 dias) en el MISMO directorio de gmap,
#   3) resolvedor CONGELADO por dia (primario y c59) con --gmap-dir, 4) vigia --diario. Cualquier fallo => Telegram (nunca silencio: el `&&` que se traga el aviso fue la trampa del vigia 5m barato).
set -u
R=/root/polymarket-research; SC=$R/experimentos/5m_barato/l2_carrera_10nov/dryrun; FW=$SC/forward; PY=${CXB60_PY:-$R/.venv/bin/python}
O=${CXB60_DIR:-/root/polymarket-research-datalogs/cxb60_dryrun}; G=${CXB60_GMAP_DIR:-/root/polymarket-research-datalogs/cxb60_dryrun_gmap}; SA=${CXB60_SA_R1:-/root/polymarket-research-datalogs/sa_r1}
LOGR=${CXB60_LOG:-$R/logs/cxb60_forward_cron.log}; MODO=${1:-}; TAG=${CXB60_TAG:-}; HOY=${CXB60_HOY:-$(date -u +%F)}   # TAG/HOY: solo ensayos ('[TEST CXB]' / fecha UTC simulada)
export CXB60_DIR=$O CXB60_GMAP_DIR=$G CXB60_HOY=$HOY
aviso() {       # rc 0 SOLO si enviar_telegram devolvio True (antes el rc ignoraba el resultado y aviso_dia marcaba el dia como avisado aunque Telegram fallase)
  [ -n "${CXB60_SIN_TELEGRAM:-}" ] && { echo "AVISO (seco, sin Telegram): ${TAG:+$TAG }cxb60 forward $MODO FALLO: $1"; return 0; }
  cd $R && $PY -c "import sys; from shadow_digest import enviar_telegram; sys.exit(0 if enviar_telegram(sys.argv[1]) is True else 3)" "${TAG:+$TAG }cxb60 forward $MODO FALLO: $1"; }
aviso_dia() {   # un aviso por clave y dia UTC (evita spam si falla cada 5 min)
  m="$O/cron_aviso_$1_$(date -u +%F)"; [ -f "$m" ] && return; aviso "$2" && touch "$m"; }
case "$MODO" in
heartbeat)
  $PY -I "$FW/vigia_cxb60_forward.py" --heartbeat >> "$LOGR" 2>&1; rc=$?
  [ "$rc" -gt 1 ] && aviso_dia hb_crash "el vigia de heartbeat murio rc=$rc (ver $LOGR)"
  exit 0 ;;
diario)
  ulimit -v 7000000; fallo=0; mkdir -p "$G"
  for k in 1 2 3; do
    d=$(date -u -d "$HOY -$k day" +%F); [ -f "$O/dec_$d.csv.gz" ] || continue
    $PY -I "$FW/fwd_gmap_btc.py" "$d" --dir "$G" >> "$LOGR" 2>&1; rc=$?     # rc=3 (cobertura<0,99) lo avisa el vigia diario con su latch
    [ "$rc" -ne 0 ] && [ "$rc" -ne 3 ] && { fallo=1; aviso "fuente BTC $d rc=$rc (ver $LOGR)"; }
  done
  for k in 0 1 2 3 4 5 6 7 8; do d=$(date -u -d "$HOY -$k day" +%F); [ -f "$SA/gmap_$d.json" ] && ln -sfn "$SA/gmap_$d.json" "$G/gmap_$d.json"; done
  for i in 1 2 3 4 5 6; do
    d=$(date -u -d "$HOY -$i day" +%F); [ -f "$O/dec_$d.csv.gz" ] || continue
    $PY -I "$SC/cxb60_resolve.py" "$d" --out "$O" --gmap-dir "$G" >> "$LOGR" 2>&1 || { fallo=1; aviso "resolvedor $d (primario) fallo"; }
    [ -f "$O/c59/dec_$d.csv.gz" ] && { $PY -I "$SC/cxb60_resolve.py" "$d" --out "$O/c59" --gmap-dir "$G" >> "$LOGR" 2>&1 || { fallo=1; aviso "resolvedor $d (c59) fallo"; }; }
  done
  $PY -I "$FW/vigia_cxb60_forward.py" --diario >> "$LOGR" 2>&1; rc=$?
  [ "$rc" -gt 1 ] && { fallo=1; aviso "el vigia diario murio rc=$rc (ver $LOGR)"; }
  exit $fallo ;;
*) echo "uso: $0 {heartbeat|diario}"; exit 2 ;;
esac
