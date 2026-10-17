import csv, gzip, json, pickle, numpy as np, pandas as pd
from array import array
V="/tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/vend"
des=json.load(open(V+"/../des_cache.json"))
days=[f"2026-10-{d:02d}" for d in range(5,17)]
wid={}
def w(x):
    c=wid.get(x)
    if c is None: c=wid[x]=len(wid)
    return c
actm={}; clm={}
def f(x):
    return float(x) if x!="" else float("nan")
spec=[("ts","d"),("mkt","i"),("act","b"),("lado","b"),("pc","f"),("acc","f"),("coste","f"),("T","f"),("mk","i"),("tk","i"),("cl","b"),("tk_acc","f"),("tk_px","f"),("inv_s","f"),("inv_ns","f"),("cash","f"),("nf_prev","i"),("first_ts","d"),("p10","f"),("p30","f"),("p60","f"),("plast","f"),("nmk","i"),("file","b")]
A={n:array(t) for n,t in spec}
for di,d in enumerate(days):
    with gzip.open(f"{V}/out/band_{d}.csv.gz","rt") as fh:
        rd=csv.reader(fh); h=next(rd); ix={k:i for i,k in enumerate(h)}
        for c in rd:
            A["ts"].append(float(c[0])); A["mkt"].append(int(c[3]))
            A["act"].append(actm.setdefault(c[4],len(actm))); A["lado"].append(1 if c[5]=="YES" else 0)
            A["pc"].append(float(c[6])); A["acc"].append(float(c[7])); A["coste"].append(float(c[8])); A["T"].append(float(c[9]))
            A["mk"].append(w(c[10])); A["tk"].append(w(c[11])); A["cl"].append(clm.setdefault(c[12],len(clm)))
            A["tk_acc"].append(f(c[15])); A["tk_px"].append(f(c[16])); A["inv_s"].append(float(c[17])); A["inv_ns"].append(float(c[18]))
            A["cash"].append(float(c[19])); A["nf_prev"].append(int(c[20])); A["first_ts"].append(f(c[21]))
            A["p10"].append(f(c[22])); A["p30"].append(f(c[23])); A["p60"].append(f(c[24])); A["plast"].append(f(c[25])); A["nmk"].append(int(c[26]))
            A["file"].append(di)
    print(d,len(A["ts"]),flush=True)
D={n:np.frombuffer(A[n],dtype=np.dtype({"d":"f8","i":"i4","b":"i1","f":"f4"}[t])) for n,t in spec}
P=pd.DataFrame(D)
inv_act={v:k for k,v in actm.items()}; inv_cl={v:k for k,v in clm.items()}
P["act"]=P.act.map(inv_act).astype("category"); P["cl"]=P.cl.map(inv_cl).astype("category")
P["file"]=P.file.map(dict(enumerate(days))).astype("category")
P["des"]=P.mkt.astype(str).map(des).map({"YES":1,"NO":0}).astype("float32")
P["gana"]=(P.lado==P.des).astype("int8")
P["fin"]=np.round((P.ts+P["T"])/300)*300
P["dia"]=pd.to_datetime(P.fin,unit="s").dt.strftime("%Y-%m-%d").astype("category")
P=P.sort_values(["mkt","lado","ts"],kind="stable").reset_index(drop=True)
print(P.memory_usage(deep=True).sum()/1e6,"MB",len(P),P.des.isna().mean(),P.cl.value_counts().to_dict())
P.to_pickle("P.pkl"); pickle.dump(wid,open("wid.pkl","wb"))
