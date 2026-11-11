BEGIN{FS=","}
($1=="q" || $1=="x") && $2>1e12 {
  rx=$8; if($1=="x") ex=$2; else ex=$2
  if(rx=="" || rx<1e12) next
  lag=rx-ex; if(lag<-100)lag=-100; if(lag>2000)lag=2000;
  h=int((ex%86400000)/3600000); b=lag+100;
  c[$1","h","b]++
}
END{ for(k in c) print k","c[k] }
