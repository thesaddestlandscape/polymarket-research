BEGIN{FS=","}
$1=="q" && $2>1e12 { s=($2%86400000)/1000; if(s<30600||s>=31320) next;
  rx=$8; if(rx==""||rx<1e12)next; lag=rx-$2; if(lag>100)lag=100; if(lag<0)lag=0;
  c[int(s/60)","lag]++ }
END{for(k in c)print k","c[k]}
