import json,collections,sys
exec(open('val.py').read().split("R=collections.defaultdict")[0].replace("run,dfile,order=sys.argv[1],sys.argv[2],sys.argv[3]","run,dfile,order=sys.argv[1],sys.argv[2],'seq'"))
rows=[];allp=collections.defaultdict(list)
for oid,p in P.items():
    if oid not in C: continue
    c=I[oid]['coin']; tok=I[oid]['tok']; ts=C[oid]['t_send_ns']/1e6; ta=C[oid]['t_ack_ns']/1e6
    m=[e for e in ev[tok] if e[1]==-5 and ts-50<=e[0]<=ts+2000]
    allp[c].append(ta-ts-23)
    if len(m)==1 and m[0][0]>=ts-5 and ta-ts>100: rows.append((c,round(ta-ts),round(m[0][0]-ts),round(m[0][0]-ta)))
print('lentos unicos (coin,http,efecto-envio,efecto-ack):',rows)
def q(x,p):
    x=sorted(x); return round(x[min(len(x)-1,int(p*len(x)))])
print('proxy L=delete_http-23 todas las intenciones:',{c:(len(v),q(v,.5),q(v,.9)) for c,v in allp.items()})
