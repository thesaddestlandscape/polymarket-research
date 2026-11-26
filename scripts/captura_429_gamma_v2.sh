#!/bin/bash
# v2 (26-Nov, solo lectura): conexiones SOLO a gamma-api (IPs resueltas al vuelo, CloudFront) por proceso, cada 1 s, 15:44:30-15:48 (o la ventana en que se lance), + primer 429 visto.
LOG=/root/polymarket-research-datalogs/captura_429_gamma_v2_$(date -u +%Y%m%d_%H%M).log
IPS=$( (getent ahostsv4 gamma-api.polymarket.com; getent ahostsv6 gamma-api.polymarket.com) | awk '{print $1}' | sort -u | paste -sd'|')
echo "IPS $IPS" > $LOG
for i in $(seq 1 240); do
  T=$(date -u +%T)
  ss -tnpH 2>/dev/null | grep -E "$IPS" | grep -o 'users:(("[^"]*",pid=[0-9]*' | sort | uniq -c | sed "s/^/$T /" >> $LOG
  [ $((i % 20)) -eq 0 ] && IPS=$( (getent ahostsv4 gamma-api.polymarket.com; getent ahostsv6 gamma-api.polymarket.com) | awk '{print $1}' | sort -u | paste -sd'|')
  sleep 1
done
echo "## cmd de los pid vistos" >> $LOG
for p in $(grep -o 'pid=[0-9]*' $LOG | sort -u | cut -d= -f2); do echo "$p $(ps -o cmd= -p $p 2>/dev/null | cut -c1-200)" >> $LOG; done
grep -h "429" /root/polymarket-research/logs/h23_shadow.log | tail -400 | head -1 | cut -c1-40 >> $LOG
