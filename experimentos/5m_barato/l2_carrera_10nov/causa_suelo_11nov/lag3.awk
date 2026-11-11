BEGIN{FS=","}
$1=="q" && $2>1e12 { rx=$8; if(rx==""||rx<1e12)next; lag=rx-$2; if(lag<-50)lag=-50; if(lag>300)lag=300;
  b=int(($2%86400000)/300000); c[b","lag+50]++ }
END{for(k in c)print k","c[k]}
