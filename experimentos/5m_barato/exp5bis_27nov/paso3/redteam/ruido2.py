import sys,collections
rows=collections.defaultdict(list)
for l in open(sys.argv[1]):
    c,tipo,t,tok,side,p,sz,rx,seq=l.strip().split(',')
    if c!='BTC': continue
    rows[(p,tok)].append((int(seq),int(t),round(float(sz)*100)))
for P in ('0.01','0.02','0.03'):
    cnt=collections.Counter(); T=0; n=0; same=0
    for (p,tok),v in rows.items():
        if p!=P: continue
        v.sort(); T+=(v[-1][1]-v[0][1])/1000
        for a,b in zip(v,v[1:]):
            d=abs(b[2]-a[2])
            if d: cnt[d]+=1; n+=1
            same+= b[1]==a[1]
    rng=range(501,750)
    vals=sorted((cnt.get(a,0),a) for a in rng)
    q=[x for x,_ in vals]
    print(P,'n',n,'tok_s',round(T),'mismo_t_ms',same,'| tamanos 5.01-7.49: ceros',q.count(0),'p10',q[24],'p50',q[124],'p90',q[224],'| 20 mas silenciosos',[a/100 for _,a in vals[:20]],'| ruido/s/tok p50 %.4f'%(q[124]/T))
