#!/bin/bash
# cola UNA a la vez: espera MemAvailable >= 3 GB y fuera de 06:00-09:00Z; nice 19, ionice c3, ulimit -v 3000000
cd /root/polymarket-research/experimentos/5m_barato/replay_brecha_B_16nov/ident_17nov
gate() { while true; do m=$(awk '/MemAvailable/{print $2}' /proc/meminfo); h=$(date -u +%H%M)
  if [ "$m" -ge 3000000 ] && { [ "$h" -lt 0600 ] || [ "$h" -ge 0900 ]; }; then break; fi; sleep 30; done
  echo "$(date -u +%FT%TZ) $1 MemAvail $m" >> run_ident.log; }
corre() { (ulimit -v 3000000; nice -n 19 ionice -c3 /usr/bin/time -f "%e s %U user %M KB rc=%x" timeout 1500 python3 -I "$@") >> run_ident.log 2>&1; }
DB=""; for d in 20 21 22 23 24 25 26 27 28 29 30 31; do DB="$DB 2026-10-$d"; done; for d in 01 02 03 04 05 06 07 08 09; do DB="$DB 2026-11-$d"; done
[ -f b1_ordenes.pkl ] || { gate b1; corre b1_tomadores_scan.py $DB; }
for d in 2026-10-20 2026-10-21 2026-10-22 2026-10-23 2026-10-24 2026-10-25 2026-10-26 2026-10-27 2026-10-28 2026-10-29 2026-10-30 2026-10-31 2026-11-03 2026-11-05 2026-11-06 2026-11-07 2026-11-08 2026-11-09; do
  [ -f A_ev_$d.pkl ] && continue; gate "a1 $d"; corre a1_virtual_b.py $d
done
gate a2; corre a2_agrega.py > /dev/null
gate b2; corre b2_perfil.py > /dev/null
echo "$(date -u +%FT%TZ) FIN" >> run_ident.log
