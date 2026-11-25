#!/bin/bash
# retraso entre una G de token (caida/traspaso/...) y el siguiente B del token (hasta ahi no hay continuidad). Solo lectura.
zcat "$1" 2>/dev/null | nice -n19 gawk -F, 'NR>1{ if($1=="G"){ if($3!="*" && $4!="baja"){ P[$3]=$7; M[$3]=$4 } else if($3=="*"){ gs++ } }
 else if($1=="B" && ($3 in P)){ dl=$7-P[$3]; delete P[$3]; n++; v[n]=dl; m[M[$3]]++ } }
END{ n2=asort(v); print "G(token, no baja)->siguiente B: n",n,"p50",v[int(n2*.5)],"p90",v[int(n2*.9)],"p99",v[int(n2*.99)],"max",v[n2], "G* totales",gs+0; for(k in m) print "  motivo",k,m[k]; for(t in P) pend++; print "  G sin B posterior (hasta fin fichero):",pend+0 }'
