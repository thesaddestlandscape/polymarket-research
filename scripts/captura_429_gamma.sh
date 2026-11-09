#!/bin/bash
# Captura de solo lectura (Javi 09-Nov): quien dispara la rafaga de 429 de gamma-api a las :46 cada 4 h (07/11/15/19/23Z).
# Muestrea cada 5 s durante 9 min: procesos con conexiones :443 (ss), procesos recien nacidos (etime<150 s) y top CPU.
LOG=/root/polymarket-research/logs/captura_429_gamma.log
echo "##### inicio $(date -u +%FT%TZ)" >> $LOG
for i in $(seq 1 108); do
  echo "=== $(date -u +%T)" >> $LOG
  echo "-- conexiones 443 por proceso:" >> $LOG
  ss -tnpH state established '( dport = :443 )' 2>/dev/null | grep -o 'users:(("[^"]*",pid=[0-9]*' | sort | uniq -c | sort -rn | head -8 >> $LOG
  echo "-- recien nacidos:" >> $LOG
  ps -eo etimes,pid,pcpu,cmd --sort=etimes | awk '$1<150' | grep -vE "ps -eo|awk|captura_429|sleep|ss -tn" | head -8 | cut -c1-200 >> $LOG
  sleep 5
done
echo "##### fin $(date -u +%FT%TZ)" >> $LOG
