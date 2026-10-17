import pandas as pd, numpy as np, json, pickle
V="/tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/vend"
des=json.load(open(V+"/../des_cache.json"))
days=[f"2026-10-{d:02d}" for d in range(5,17)]
wid={}; 
def codes(s):
    out=np.empty(len(s),dtype=np.int32)
    for i,w in enumerate(s):
        c=wid.get(w)
        if c is None: c=wid[w]=len(wid)
        out[i]=c
    return out
cols=["ts","mkt","act","lado_c","pc","acc","coste","T","maker","taker","tk_clase","tk_side","tk_lado","tk_acc","tk_px","inv_s","inv_ns","cash","nf_prev","first_ts","p_s_10","p_s_30","p_s_60","p_s_last","nmk"]
parts=[]
for d in days:
  for df in pd.read_csv(f"{V}/out/band_{d}.csv.gz",usecols=cols,dtype={"mkt":str,"maker":str,"taker":str,"act":str,"lado_c":str,"tk_clase":str,"tk_lado":str},chunksize=150000):
    o=pd.DataFrame({"ts":df.ts.astype("float64"),"mkt":df.mkt.astype("int32"),"act":df.act.astype(str),
        "lado":(df.lado_c=="YES").astype("int8"),"pc":df.pc.astype("float32"),"acc":df.acc.astype("float32"),"coste":df.coste.astype("float32"),
        "T":df["T"].astype("float32"),"mk":codes(df.maker),"tk":codes(df.taker),"cl":df.tk_clase.astype("str"),
        "tk_acc":df.tk_acc.astype("float32"),"tk_px":df.tk_px.astype("float32"),"inv_s":df.inv_s.astype("float32"),"inv_ns":df.inv_ns.astype("float32"),
        "cash":df.cash.astype("float32"),"nf_prev":df.nf_prev.astype("int32"),"first_ts":df.first_ts.astype("float64"),
        "p10":df.p_s_10.astype("float32"),"p30":df.p_s_30.astype("float32"),"p60":df.p_s_60.astype("float32"),"plast":df.p_s_last.astype("float32"),"nmk":df.nmk.astype("int16")})
    o["file"]=d
    parts.append(o)
  print(d,flush=True)
P=pd.concat(parts,ignore_index=True)
P["file"]=P.file.astype("category"); P["cl"]=P.cl.astype("category"); P["act"]=P.act.astype(str).astype("category")
P["des"]=P.mkt.astype(str).map(des).map({"YES":1,"NO":0}).astype("float32")
P["gana"]=(P.lado==P.des).astype("int8")
P["fin"]=(np.round((P.ts+P["T"])/300)*300)
P["dia"]=pd.to_datetime(P.fin,unit="s").dt.strftime("%Y-%m-%d").astype("category")
P=P.sort_values(["mkt","lado","ts"],kind="stable").reset_index(drop=True)
print(P.memory_usage(deep=True).sum()/1e6,"MB", len(P), P.des.isna().mean())
P.to_pickle("P.pkl")
pickle.dump(wid,open("wid.pkl","wb"))
