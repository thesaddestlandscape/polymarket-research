import sys,collections
rows=collections.defaultdict(list)
for l in open(sys.argv[1]):
    c,tipo,t,tok,side,p,sz,rx,seq=l.strip().split(',')
    rows[(c,p,tok)].append((int(seq),int(t),round(float(sz)*100)))
st=collections.defaultdict(lambda: collections.Counter()); dur={}
for (c,p,tok),v in rows.items():
    v.sort(); 
    k=(c,p); dur[k]=dur.get(k,0)+(v[-1][1]-v[0][1])/1000
    for a,b in zip(v,v[1:]):
        d=b[2]-a[2]
        if d==0: continue
        s=st[k]; s['n']+=1; ad=abs(d)
        s['eq500']+= ad==500
        s['int']+= ad%100==0
        s['frac']+= ad%100!=0
        s['u_%d'%ad]+=1 if 501<=ad<=599 else 0
        s['fr_%d'%(ad%100)]+=1
for k in sorted(st):
    s=st[k]; n=s['n']; T=dur[k]
    if n<50: continue
    uniq=[s.get('u_%d'%a,0) for a in range(501,600)]
    fr=[s.get('fr_%d'%a,0) for a in range(1,100)]
    print(k, 'n',n,'seg_tok',round(T),'ev/s/tok',round(n/T,2),'|d|=5.00 %.1f%%'%(100*s['eq500']/n),'frac!=0 %.1f%%'%(100*s['frac']/n),
          '| |d|=5.kk: mediana',sorted(uniq)[49],'max',max(uniq),'ceros',uniq.count(0),'| frac=kk mediana',sorted(fr)[49],'min',min(fr),'max',max(fr))
