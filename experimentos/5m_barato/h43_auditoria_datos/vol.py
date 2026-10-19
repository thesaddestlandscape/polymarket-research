import csv, math, datetime, sys
for d in sys.argv[1:]:
    last={}
    import os,gzip
    p=f"/root/polymarket-research/data/prices/chainlink_{d}.csv"
    fh=gzip.open(p+".gz","rt") if not os.path.exists(p) else open(p)
    with fh:
        rd=csv.reader(fh); next(rd)
        for c in rd:
            if c[1]!="BTC" or c[4]!="chainlink": continue
            t=datetime.datetime.fromisoformat(c[0]).timestamp(); b=int(t//300)
            last[b]=float(c[2])
    ks=sorted(last); r=[math.log(last[b]/last[a])*1e4 for a,b in zip(ks,ks[1:]) if b==a+1]
    sd=math.sqrt(sum(x*x for x in r)/len(r))
    big=sum(1 for x in r if abs(x)>=15)/len(r)
    print(d,"n5m",len(r),"sd5m_bps %.2f"%sd,"frac|mov5m|>=15bps %.3f"%big)
