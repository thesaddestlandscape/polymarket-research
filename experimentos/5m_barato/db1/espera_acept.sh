#!/bin/bash
L=/root/polymarket-research/experimentos/5m_barato/db1/aceptacion.log
for i in $(seq 1 55); do grep -q "=== fin\|^FALLO" <(tail -n +1 $L | awk '/inicio/{n=NR} {a[NR]=$0} END{for(i=n;i<=NR;i++)print a[i]}') && break; sleep 10; done
