#!/bin/bash
# Despliegue MINIMO e idempotente del paquete H23 en /root/polymarket-research-dev (ver DESPLIEGUE_DEV.md).
# Solo CREA ficheros nuevos; NO toca experimento_maker_h47.py, experimento_pares_cola_15m.py, pares_contabilidad.py ni procesos.
set -euo pipefail
SRC=/root/polymarket-research/experimentos/5m_barato/h23_maker
DEV=/root/polymarket-research-dev
DST=$DEV/experimentos/5m_barato/h23_maker
mkdir -p "$DST/paquete_real"
cp -p "$SRC/h23_regla.py" "$SRC/h23_shadow.py" "$DST/"
cp -p "$SRC/paquete_real/experimento_maker_h23.py" "$DEV/experimento_maker_h23.py"
cp -p "$SRC/paquete_real/test_experimento_maker_h23.py" "$SRC/paquete_real/sim_kill_v2.py" "$SRC/paquete_real/sim_kill_v3.py" "$DST/paquete_real/"
# verificacion: sha identicos origen/destino
for p in "$SRC/h23_regla.py:$DST/h23_regla.py" "$SRC/h23_shadow.py:$DST/h23_shadow.py" "$SRC/paquete_real/experimento_maker_h23.py:$DEV/experimento_maker_h23.py"; do
  a=${p%%:*}; b=${p##*:}
  sa=$(sha256sum "$a" | cut -c1-16); sb=$(sha256sum "$b" | cut -c1-16)
  [ "$sa" = "$sb" ] && echo "OK $a $sa" || { echo "DIFIERE $a $sa $sb"; exit 1; }
done
