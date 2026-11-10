#!/bin/bash
# Cron diario PROPUESTO de PREREG_DB1 (NO instalado). Produce RX de D-1 y D-2 (>=2026-11-10, idempotente), evalua y avisa por Telegram. Solo lectura de datos + salida en db1/; 0 ordenes.
# Va detras de scripts/cron_pesado.sh (cola global + RAM>=3 GB). Los dias >= 2026-11-10 dependen de x_D / bad_D / tape_D / ms_D.npz que producen los crons existentes a ~10:42-12:18Z del dia siguiente.
# Los placebos (99 semillas, horas) NO corren aqui: solo en checkpoints, a mano: python3 -I eval_db1.py --placebo 10 DB1 (y DB2), en cola pesada, fuera de 06:00-09:15Z.
Q=/root/polymarket-research/experimentos/5m_barato/db1
LOG=$Q/cron.log; mkdir -p $Q/out
avisar() { python3 -c "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram; enviar_telegram(sys.argv[1])" "$1" >/dev/null 2>&1; }
echo "=== $(date -u +%FT%TZ) inicio" >> $LOG
for k in 1 2; do
  D=$(date -u -d "$k day ago" +%F)
  [[ "$D" < "2026-11-10" ]] && continue
  if [ ! -f $Q/out/RX_$D.pkl ]; then
    python3 -I $Q/eval_db1.py --producir $D >> $LOG 2>&1 || echo "producir $D: fallo/pendiente (se reintenta manana)" >> $LOG
  fi
done
python3 -I $Q/eval_db1.py --evaluar > $Q/ultimo_informe.txt 2>> $LOG; rc=$?
cat $Q/ultimo_informe.txt >> $LOG
echo "=== fin rc=$rc" >> $LOG
if [ $rc -ne 0 ]; then avisar "🚨 DB1 forward: eval_db1 --evaluar rc=$rc (ver $LOG)"; exit $rc; fi
V=$(grep -E "CHECKPOINT|INSUFFICIENT|REFUTA|CANDIDATO|ERROR_DATOS|dPnL BASE" $Q/ultimo_informe.txt | head -8 | cut -c1-220)
avisar "DB1 forward $(date -u +%F): $(grep -c . $Q/ultimo_informe.txt) lineas. $V" || echo "aviso Telegram fallo" >> $LOG
