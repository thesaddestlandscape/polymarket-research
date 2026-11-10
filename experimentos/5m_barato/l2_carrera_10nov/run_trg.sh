#!/bin/bash
cd /root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov
ulimit -v 3000000
for d in 2026-11-03 2026-11-04 2026-11-05 2026-11-06 2026-11-07 2026-11-08 2026-11-09; do
  [ -f out/trg_$d.pkl ] && continue
  h=$(date -u +%H%M); if [ "$h" -ge 0600 ] && [ "$h" -lt 0915 ]; then echo "VENTANA 06-09:15Z, paro"; exit 3; fi
  nice -n 19 ionice -c3 python3 -I l2_triggers.py $d >> out/trg.log 2>&1
done
echo FIN >> out/trg.log
