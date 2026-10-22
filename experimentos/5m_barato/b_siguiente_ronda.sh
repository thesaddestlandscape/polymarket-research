#!/bin/bash
# Siguiente ronda (tanda) de B real: reseteo de suelo VEZ <n> + relanzar h47B con --n 500. NO se ejecuta solo: lo lanza el chief/Javi.
# Uso: bash b_siguiente_ronda.sh <n>      (n = nº de reseteos previos + 1; el último fue VEZ 18 el 22-Oct => 19)
# Precondiciones que comprueba (aborta si falla alguna): n dado, tanda agotada de verdad, B sin órdenes vivas, sin KILL.
set -u
N="${1:?uso: $0 <n_VEZ>}"
PY=/root/polymarket-research/.venv/bin/python
DEV=/root/polymarket-research-dev
DL=/root/polymarket-research-datalogs
SUP=/root/polymarket-research/experimentos/5m_barato

ESTADO=$(cd $SUP && $PY - <<'PYEOF'
import h47_tandas_supervisor as s
print("agotada" if (s.tanda_agotada_inactiva() or s.parada_sin_reseteo()) else "viva")
print("vivas=%d" % len(s.ordenes_vivas()))
print("kill=%s" % bool(s.kill_pendiente()))
print("saldo=%s" % s.saldo())
PYEOF
)
echo "$ESTADO"
echo "$ESTADO" | grep -q '^agotada$' || { echo "ABORTO: la tanda NO está agotada"; exit 1; }
echo "$ESTADO" | grep -q '^vivas=0$' || { echo "ABORTO: B con órdenes vivas"; exit 1; }
echo "$ESTADO" | grep -q '^kill=False$' || { echo "ABORTO: KILL pendiente"; exit 1; }

# 1) parar B limpio (SIGTERM al python, nunca screen -X quit)
PID=$(pgrep -f "experimento_maker_h47.py --escalon B --n" | head -1)
[ -n "$PID" ] && kill -TERM "$PID" && for i in $(seq 1 60); do kill -0 "$PID" 2>/dev/null || break; sleep 1; done
kill -0 "$PID" 2>/dev/null && { echo "ABORTO: B no terminó"; exit 1; }
screen -S h47B -X quit 2>/dev/null

# 2) reseteo (suelo = saldo verificado)
cd $DEV && echo "REINICIAR SUELO 3d297F VEZ $N" | $PY experimento_maker_h47.py --escalon B --confirmo-dinero-real \
  --reiniciar-suelo "tanda $N de 5 USD agotada; siguiente ronda, OK Javi" --segundo-motivo "Javi pide encadenar la siguiente ronda de B (tope 500)" || { echo "ABORTO: reseteo rechazado"; exit 1; }

# 3) relanzar B
screen -dmS h47B bash -c "cd $DEV && nice -n 10 $PY experimento_maker_h47.py --escalon B --n 500 --confirmo-dinero-real >> $DL/h47_real_B_$(date -u +%Y%m%d_%H%M)_r$N.out 2>&1"
sleep 15; screen -ls | grep h47B && tail -2 $DL/experimento_h47_B_ledger.jsonl | cut -c1-200
