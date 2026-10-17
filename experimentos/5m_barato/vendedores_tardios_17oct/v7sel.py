import csv, gzip, collections, pandas as pd, numpy as np
EXCH="0xe111180000d2663c0091e4f400237545b87b996b"
M="/root/polymarket-research-datalogs/m5barato_mision/"
ev=[]
for d in range(5,17):
    x=pd.read_csv(f"{M}disparo15m_2026-10-{d:02d}.csv.gz"); x["d"]=d; ev.append(x)
E=pd.concat(ev)
E=E[E.moneda=="BTC"]
print("eventos V7 BTC por dia (filas, mercados distintos, pnl, coste):")
print(E.groupby("d").agg(filas=("mercado","size"),mkts=("mercado","nunique"),pnl=("pnl","sum"),coste=("coste","sum")).round(2).T.to_string())
# token por (mercado,lado)
tk={}
for c in csv.reader(open("kall.csv")):
    if c[2]=="5min" and c[1]=="BTC": tk[(int(c[3]),c[5])]=c[0]
E["tok"]=[tk.get((int(m),"YES" if l=="Up" else "NO")) for m,l in zip(E.mercado,E.lado)]
print("sin token:",E.tok.isna().sum(),"de",len(E))
ent=collections.defaultdict(list)
for r in E.itertuples():
    if r.tok: ent[(r.tok)].append((r.t/1000.0,r.ask,r.d,r.mercado,r.lado))
res=[]
for d in range(6,17):
    f=f"/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_2026-10-{d:02d}.csv.gz"
    with gzip.open(f,"rt") as fh:
        rd=csv.reader(fh); next(rd)
        for c in rd:
            if c[0]!="F" or c[7]==EXCH: continue
            L=ent.get(c[9])
            if not L or c[8]!="1": continue
            ts=float(c[2]); ma=float(c[10]); ta=float(c[11]); acc=ma; usd=ta
            if acc<=0: continue
            p=usd/acc
            for (t,ask,dd,m,l) in L:
                if t-1<=ts<=t+8 and abs(p-ask)<=0.0151:
                    res.append((dd,m,l,t,ts-t,ask,p,acc,c[6]))
R=pd.DataFrame(res,columns=["d","mkt","lado","t","dt","ask","p","acc","maker"])
R.to_pickle("v7sel.pkl")
print(len(R))
W=[l.strip() for l in open("w6.txt")]
R["six"]=R.maker.isin(W)
g=R.groupby(["d"]).apply(lambda x: pd.Series({"n":len(x),"acc":x.acc.sum(),"share6_acc":x[x.six].acc.sum()/x.acc.sum(),"makers":x.maker.nunique(),"top1":x.groupby("maker").acc.sum().max()/x.acc.sum()}),include_groups=False)
print(g.round(3).T.to_string())
R["w"]=R.maker.str[:10]
print(R.groupby(["d","w"]).acc.sum().unstack(0).fillna(0).assign(t=lambda x:x.sum(axis=1)).sort_values("t",ascending=False).head(14).round(0).to_string())
