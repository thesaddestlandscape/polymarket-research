#!/bin/bash
ulimit -v 3000000
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f3_carry
until grep -q '^FIN' datos/extrae.log; do sleep 20; done
for d in 2026-10-24 2026-10-23 2026-10-22 2026-10-21 2026-10-20 2026-10-19 2026-10-18 2026-10-17 2026-10-16 2026-10-15; do
 for m in 5min 15min; do
  h=$(date -u +%H); if [ "$h" -ge 6 ] && [ "$h" -lt 9 ]; then echo "PAUSA 06-09Z"; exit 0; fi
  [ -f /mnt/HC_Volume_106538179/agentes_datos/f3_carry/vpv_${m}_${d}.csv.gz ] || nice -n 19 ionice -c3 python3 -I scripts/f3_vpv.py --dia $d --marco $m
 done
done
echo FIN
