exec(open("common.py").read())
wid=pickle.load(open("wid.pkl","rb"))
W=[l.strip() for l in open("../w6.txt")]
ids={w:wid[w] for w in W if w in wid}
print(len(ids))
X=P[P.mk.isin(ids.values())]
print("filas banda de las 6:",len(X),"de",len(P))
inv={v:k[:10] for k,v in ids.items()}
X=X.assign(w=X.mk.map(inv))
t=X.groupby(["dia"],observed=True).agg(n=("acc","size"),acc=("acc","sum"),c=("coste","sum"),pnl=("pnl","sum"),mk=("mkt","nunique")).join(P.groupby("dia",observed=True).agg(N=("acc","size"),C=("coste","sum")))
t["ev"]=t.pnl/t.c; t["share_c"]=t.c/t.C
print(t.round(3).to_string())
print("\nT de sus rellenos / precio / lado")
print(X.groupby(pd.cut(X["T"],[60,120,180,240,300])).agg(n=("acc","size"),c=("coste","sum"),pc=("pc","mean"),ev=("pnl",lambda s: 0)).round(2).to_string())
print(X.groupby("act",observed=True).agg(n=("acc","size"),c=("coste","sum")).to_string())
print("cl:",X.groupby("cl",observed=True).acc.sum().to_dict())
for w,x in X.groupby("w"):
    print(w,"ev SEL %.3f MEAS %.3f"%(ev(x[x.per=="SEL"].pnl,x[x.per=="SEL"].coste),ev(x[x.per=="MEAS"].pnl,x[x.per=="MEAS"].coste)),"tardio share %.2f"%(x.acc_l.sum()/x.acc.sum()), "mkts/dia",round(x.groupby("dia",observed=True).mkt.nunique().mean()))
