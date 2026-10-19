#!/usr/bin/env python3
"""Cobertura on-chain por dia de m5_onchain (solo lectura, streaming): F/M, bloques distintos, huecos de bloque, horas, ts fuera de dia."""
import csv, gzip, sys
from collections import Counter
VOL="/mnt/HC_Volume_106538179/m5_onchain"
for d in sys.argv[1:]:
    nF=nM=0; blocks=set(); hrs=Counter(); tmin=1e18; tmax=0; tx=set(); dup=0; seen=set()
    with gzip.open(f"{VOL}/m5_onchain_{d}.csv.gz","rt") as fh:
        rd=csv.reader(fh); next(rd)
        for c in rd:
            if c[0]=="F":
                nF+=1; b=int(c[1]); blocks.add(b); ts=float(c[2]); tmin=min(tmin,ts); tmax=max(tmax,ts)
                hrs[int(ts//3600)%24]+=1
                k=(c[3],c[4])
                if k in seen: dup+=1
                else: seen.add(k)
            elif c[0]=="M": nM+=1
    bl=sorted(blocks); gaps=[(bl[i+1]-bl[i],bl[i]) for i in range(len(bl)-1) if bl[i+1]-bl[i]>15]
    gaps.sort(reverse=True)
    import datetime
    f=lambda t: datetime.datetime.fromtimestamp(t,datetime.timezone.utc).strftime("%m-%d %H:%M:%S")
    print(d,"F",nF,"M",nM,"blocks",len(bl),"rango",bl[0],bl[-1],"esperados",bl[-1]-bl[0]+1,"ts",f(tmin),f(tmax),"dupFlogidx",dup,"huecos>15bl",len(gaps),gaps[:4])
    print("   F/hora:",[hrs[h] for h in range(24)],flush=True)
