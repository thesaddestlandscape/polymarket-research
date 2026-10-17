import csv, gzip, sys
from collections import defaultdict
EXCH="0xe111180000d2663c0091e4f400237545b87b996b"
d=sys.argv[1]
tok={}
for c in csv.reader(open("kall.csv")):
    if c[2]=="5min": tok[c[0]]=(c[1],c[5])
agg=defaultdict(lambda:[0,0.0,0.0])
bins=[0.05,0.10,0.20,0.30,0.5,0.7,0.9,1.01]
def pb(p):
    for i,b in enumerate(bins):
        if p<b: return i
    return len(bins)-1
with gzip.open(f"/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz","rt") as fh:
    rd=csv.reader(fh); next(rd)
    for c in rd:
        if c[0]!="F" or c[7]==EXCH: continue
        t=tok.get(c[9])
        if t is None: continue
        side=int(c[8]); ma=float(c[10]); ta=float(c[11])
        usd,acc=(ma,ta) if side==0 else (ta,ma)
        if acc<=0: continue
        k=(c[6],t[0],side,pb(usd/acc))
        a=agg[k]; a[0]+=1; a[1]+=acc; a[2]+=usd
with open(f"p2/p2_{d}.csv","w") as fo:
    w=csv.writer(fo); w.writerow(["wallet","act","side","pb","n","acc","usd"])
    for k,a in agg.items(): w.writerow(list(k)+[a[0],round(a[1],2),round(a[2],2)])
