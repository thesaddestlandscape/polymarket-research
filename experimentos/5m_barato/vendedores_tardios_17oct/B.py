import csv, gzip, glob, collections, pandas as pd
W=[l.strip() for l in open("w6.txt")]; Ws=set(W)
kt={}
with open("kall.csv") as fh:
    for c in csv.reader(fh): kt[c[0]]=(c[1],c[2])
rows=[]
for f in sorted(glob.glob("B/*.csv.gz")):
    name=f.split("/")[-1][:-7]; src,d=name.split("_")
    seen=set()
    with gzip.open(f,"rt") as fh:
        for c in csv.reader(fh):
            if len(c)<13 or c[0] not in ("F","M"): continue
            if c[0]!="F": continue
            mk,tk=c[6],c[7]
            w=mk if mk in Ws else (tk if tk in Ws else None)
            if w is None: continue
            key=(c[3],c[4])
            if key in seen: continue
            seen.add(key)
            side=int(c[8]); ma=float(c[10]); ta=float(c[11])
            usd=ma if side==0 else ta; acc=ta if side==0 else ma
            a,m=kt.get(c[9],("?","otro"))
            rows.append((src,d,w[:10],"maker" if mk in Ws else "taker",a,m,side,usd,acc,float(c[2])))
df=pd.DataFrame(rows,columns=["src","d","w","rol","act","marco","side","usd","acc","ts"])
df.to_pickle("B.pkl")
print(len(df))
# dedup fuentes: m5/m15 archivos vs all_ (mismo dia 05-08 solo m5/m15)
print(df.groupby(["src"]).size())
