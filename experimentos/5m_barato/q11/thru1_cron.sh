#!/bin/bash
# Cron diario thru1 (Javi OK 09-Nov): produce RT de D-1 y D-2 (>=2026-11-09, idempotente) y evalua. Solo lectura de datos + salida en thru1_fwd; 0 ordenes.
# 13:20Z: x_D se extrae ~11:15Z y bad_D ~12:18Z (ADDENDUM7: dia asentado = ficheros producidos tras el cierre y quietos 10 min).
Q=/root/polymarket-research/experimentos/5m_barato/q11
OUT=$Q/thru1_fwd; LOG=$OUT/cron.log; mkdir -p $OUT
avisar() { python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram; enviar_telegram(sys.argv[1])" "$1" >/dev/null 2>&1; }
echo "=== $(date -u +%FT%TZ) inicio" >> $LOG
for k in 1 2; do
  D=$(date -u -d "$k day ago" +%F)
  [[ "$D" < "2026-11-09" ]] && continue
  if [ ! -f $Q/toxicidad_thru1/out/RT_$D.pkl ] || [ ! -f $Q/redteam/out/RT_$D.pkl ] || [ ! -f $Q/redteam/out_cxj150/RX_$D.pkl ]; then
    python3 -I $Q/eval_thru1.py --producir $D >> $LOG 2>&1 || echo "producir $D: fallo/pendiente (se reintenta manana)" >> $LOG
  fi
done
python3 -I $Q/eval_thru1.py --evaluar > $OUT/ultimo_informe.txt 2>> $LOG; rc=$?
cat $OUT/ultimo_informe.txt >> $LOG
echo "=== fin rc=$rc" >> $LOG
if [ $rc -ne 0 ]; then avisar "🚨 thru1 forward: eval_thru1 --evaluar rc=$rc (ver $LOG)"; exit $rc; fi
V=$(grep -E "^VEREDICTO|CANDIDATO|REFUTA|CONFIRMA|ERROR_DATOS" $OUT/ultimo_informe.txt | head -6 | cut -c1-200)
avisar "thru1 forward $(date -u +%F): $(grep -c . $OUT/ultimo_informe.txt) lineas. $V"
