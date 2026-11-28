import json,collections,sys
exec(open('val.py').read().split("R=collections.defaultdict")[0].replace("run,dfile,order=sys.argv[1],sys.argv[2],sys.argv[3]","run,dfile,order=sys.argv[1],sys.argv[2],'seq'"))
def q(x,p):
    x=sorted(x); return None if not x else round(x[min(len(x)-1,int(p*len(x)))],1)
G=collections.defaultdict(lambda:collections.defaultdict(list))
for oid,p in P.items():
    if oid not in C: continue
    c=I[oid]['coin']; tok=I[oid]['tok']; ts=C[oid]['t_send_ns']/1e6; ta=C[oid]['t_ack_ns']/1e6
    m=[e for e in ev[tok] if e[1]==-5 and ts-50<=e[0]<=ts+2000]
    st='uniq' if len(m)==1 and m[0][0]>=ts-5 else ('cero' if not m else 'multi')
    G[c][st].append(ta-ts); G[c]['all'].append(ta-ts)
    # among multi: is there any event in [ta-60, ta-15] (ack-bracket consistent)?
    if st=='multi':
        mm=[e for e in m if ta-60<=e[0]<=ta-15]
        G[c]['multi_bracket_hits'].append(len(mm))
for c,d in G.items():
    print(c,{k:(len(v),q(v,.5),q(v,.9)) for k,v in d.items() if k!='multi_bracket_hits'}, 'multi: n con exactamente 1 evento en [ack-60,ack-15]=',sum(1 for x in d['multi_bracket_hits'] if x==1),'/',len(d['multi_bracket_hits']))
