#!/bin/bash
# espera a que acabe la primera pasada (FIN en s2.log) y relanza una segunda pasada idempotente (rehace ficheros borrados)
D=/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/fav_60m_4h
until grep -q FIN $D/datos/s2.log; do sleep 15; done
nice -n 19 ionice -c3 $D/scripts/s2_extrae_ms.sh > $D/datos/s2b.log 2>&1
