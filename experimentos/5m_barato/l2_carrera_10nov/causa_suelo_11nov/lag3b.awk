BEGIN{FS=","}
$1=="x" && $2>1e12 { rx=$8; if(rx==""||rx<1e12)next; lag=rx-$2; if(lag<0)lag=0; if(lag>600)lag=600;
  b=int(($2%86400000)/300000); c[b","lag]++ }
END{for(k in c)print k","c[k]}
