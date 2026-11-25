#!/bin/bash
# u2_continuidad.sh FICHERO.csv.gz : marcas de continuidad (G, saltos de seq, hueco max por token) en libro5_ms. Solo lectura, streaming.
zcat "$1" | nice -n19 gawk -F, 'NR>1{ s=$8+0; if(NR>2 && s!=last+1){nj++; if(nj<=5) jmp=jmp " " last "->" s} last=s; n++
 if($1=="G"){ g[$4]++ ; if($3=="*") star[$4]++ }
 else { tk=$3; rx=$7+0; if(tk in L){ gp=rx-L[tk]; if(gp>MX[tk]) MX[tk]=gp; if(gp>1000) c1++; if(gp>5000) c5++; if(gp>30000) c30++; if(gp>60000) c60++; ng++ } L[tk]=rx; if($1=="T") nt++ } }
END{ print "filas",n,"saltos_seq",nj+0,"ej:" jmp; for(k in g) print "G_motivo",k,g[k], "(de ellas con token *:",star[k]+0 ")";
 print "gaps entre mensajes consecutivos del mismo token: n",ng,">1s",c1+0,">5s",c5+0,">30s",c30+0,">60s",c60+0;
 m=0; for(t in MX){ v[++m]=MX[t] } n2=asort(v); print "tokens",m,"maxgap_token p50",v[int(n2*0.5)],"p90",v[int(n2*0.9)],"p99",v[int(n2*0.99)],"max",v[n2] }'
