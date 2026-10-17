import csv, gzip, pickle, numpy as np, pandas as pd, sys
wid=pickle.load(open("an/wid.pkl","rb"))
tok={}
for c in csv.reader(open("kall.csv")):
    if c[2]=="15min" and c[1]=="BTC": tok[c[0]]=(int(c[3]),c[5])
ts=[];w=[];m=[];d=[];s=[]
for dd in range(5,17):
    f=f"/mnt/HC_Volume_106538179/m15_onchain/m15_onchain_2026-10-{dd:02d}.csv.gz"
    with gzip.open(f,"rt") as fh:
        rd=csv.reader(fh); next(rd)
        for c in rd:
            if c[0]!="F": continue
            t=tok.get(c[9])
            if t is None: continue
            k=wid.get(c[6])
            if k is None: continue
            side=int(c[8]); ma=float(c[10]); ta=float(c[11])
            acc=ta if side==0 else ma
            sg=(1 if side==0 else -1)*(1 if t[1]=="YES" else -1)
            ts.append(float(c[2])); w.append(k); m.append(t[0]); d.append(sg*acc)
    print(dd,len(ts),flush=True)
pd.DataFrame({"ts":ts,"w":np.array(w,dtype="int32"),"m15":np.array(m,dtype="int32"),"dup":np.array(d,dtype="float32")}).to_pickle("E15.pkl")
