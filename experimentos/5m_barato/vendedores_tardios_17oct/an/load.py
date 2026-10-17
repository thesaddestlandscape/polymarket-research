import pandas as pd, numpy as np, json, glob, sys, os
V="/tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/vend"
des=json.load(open(V+"/../des_cache.json"))
def load_day(d):
    df=pd.read_csv(f"{V}/out/band_{d}.csv.gz",dtype={"mkt":str,"maker":"category","taker":"category","act":"category","lado_c":"category","tk_clase":"category","tx":str})
    df["des"]=df.mkt.map(des)
    return df
if __name__=="__main__":
    for d in sys.argv[1:]:
        df=load_day(d)
        print(d,len(df),df.des.isna().mean(), df.mkt.nunique(), df.groupby('mkt').des.first().isna().mean())
