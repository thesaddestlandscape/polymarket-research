#!/bin/bash
# Aplica parche_tx_v2.diff a libro_estado_ws.py (main) con copia, comprobaciones y vuelta atrás. Lanzar a las 22:15Z (24-Oct).
D=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/captura_eventos_nivel
R=/root/polymarket-research; LOG=$R/logs/aplicar_parche_tx.log
{
echo "== $(date -u +%FT%TZ)"
cmp -s $R/libro_estado_ws.py $D/libro_estado_ws.py.orig || { echo "ABORTA: libro_estado_ws.py cambio desde el parche"; exit 3; }
cp $R/libro_estado_ws.py $R/libro_estado_ws.py.bak_antes_tx
cp $R/libro_estado_ws.py /tmp/lews_probe.py
cd /tmp && python3 $D/aplicar.py /tmp/lews_probe.py && python3 -m py_compile /tmp/lews_probe.py || { echo "ABORTA: parche/compilacion"; exit 4; }
cp /tmp/lews_probe.py $R/libro_estado_ws.py && echo "APLICADO (el watchdog reinicia observadores)"
$R/.venv/bin/python $R/tests/test_libro5_registro.py $R 2>&1 | tail -2
} >> $LOG 2>&1
