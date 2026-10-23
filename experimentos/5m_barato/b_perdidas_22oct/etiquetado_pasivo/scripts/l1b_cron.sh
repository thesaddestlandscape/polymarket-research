#!/bin/bash
# L1b etiquetado pasivo (23-Oct): pob | pobverif | ret | retbackfill | retres. Solo lectura de B/libro5/R1; salida en datalogs/etiquetado_pasivo_B (fuera de git). Nunca 06-09Z.
cd "$(dirname "$0")" || exit 1
LOG=/root/polymarket-research-datalogs/etiquetado_pasivo_B/cron_l1b.log; mkdir -p "$(dirname "$LOG")"
H=$(date -u +%H)
if [ "$H" -ge 6 ] && [ "$H" -lt 9 ]; then echo "=== $(date -u +%FT%TZ) $1 fuera de horario (06-09Z): no se lanza" >> "$LOG"; exit 0; fi
ulimit -v 3000000
aviso() { /usr/bin/python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e(sys.argv[1])" "$1"; }
run() { nice -n 19 ionice -c3 python3 -I "$@" >> "$LOG" 2>&1; }
echo "=== $(date -u +%FT%TZ) $1" >> "$LOG"; rc=0
case "$1" in
  pob) run etiquetar_poblacion.py etiquetar; rc=$?
       [ $rc -eq 0 ] && { nice -n 19 ionice -c3 python3 -I evaluar_poblacion.py > /root/polymarket-research-datalogs/etiquetado_pasivo_B/informe_poblacion_ultimo.txt 2>> "$LOG" || aviso "⚠️ L1b: evaluar_poblacion FALLÓ. Ver $LOG"; } ;;
  pobverif) run etiquetar_poblacion.py verificar; rc=$? ;;
  ret) for k in 2 1; do D=$(date -u -d "-$k day" +%F); run retirada_liquidez.py dia "$D"; r=$?
         case $r in 0|2) ;; 3) aviso "⚠️ L1b retirada $D BLOCKED (falta gmap de R1 o libro5; el libro5 se conserva ~3 d). Ver $LOG"; rc=3 ;; 4) aviso "⚠️ L1b retirada $D PARTIAL (cobertura <80 % o errores). Ver $LOG y etiquetado_pasivo_B/retirada/dias/$D.json"; rc=4 ;; *) rc=$r ;; esac; done ;;
  retbackfill) run retirada_liquidez.py backfill; rc=$? ;;
  retres) run retirada_liquidez.py resolver; rc=$?
       [ $rc -eq 0 ] && { nice -n 19 ionice -c3 python3 -I evaluar_retirada.py > /root/polymarket-research-datalogs/etiquetado_pasivo_B/informe_retirada_ultimo.txt 2>> "$LOG" || aviso "⚠️ L1b: evaluar_retirada FALLÓ. Ver $LOG"; } ;;
  *) echo "modo desconocido" >> "$LOG"; exit 1 ;;
esac
if [ $rc -ne 0 ] && [ $rc -ne 3 ] && [ $rc -ne 4 ]; then aviso "🚨 L1b etiquetado pasivo ($1) FALLÓ rc=$rc. Ver $LOG"; fi
[ "$(stat -c %s "$LOG")" -gt 5000000 ] && tail -c 1000000 "$LOG" > "$LOG.tmp" && mv "$LOG.tmp" "$LOG"
exit $rc
