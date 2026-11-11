#!/bin/bash
# wait_for.sh FICHERO PATRON SEGUNDOS : espera (<=SEGUNDOS) a que PATRON aparezca en FICHERO; imprime las ultimas 4 lineas.
f=$1; p=$2; t=$3; s=0
while [ $s -lt $t ]; do grep -q "$p" "$f" 2>/dev/null && break; sleep 20; s=$((s+20)); done
date -u; tail -4 "$f" 2>/dev/null | cut -c1-300
