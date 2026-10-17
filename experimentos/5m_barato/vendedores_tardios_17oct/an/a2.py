exec(open("common.py").read())
wid=pickle.load(open("wid.pkl","rb")); inv={v:k for k,v in wid.items()}
L=P[P.acc_l>0]
print("filas tardio",len(L),"takers distintos",L.tk.nunique(),"makers distintos",L.mk.nunique())
for per in ["SEL","MEAS"]:
    x=L[L.per==per]
    t=x.groupby("tk").agg(acc=("acc_l","sum"),c=("c_l","sum"),pnl=("pnl_l","sum"),n=("acc","size"),mkts=("mkt","nunique"),dias=("dia","nunique")).sort_values("c",ascending=False)
    tot=t.c.sum()
    print(per,"takers",len(t),"coste tardio",round(tot),"top1 %.3f top3 %.3f top5 %.3f top10 %.3f top20 %.3f top50 %.3f"%tuple(t.c.head(k).sum()/tot for k in (1,3,5,10,20,50)))
    t["share"]=t.c/tot; t["ev_maker"]=t.pnl/t.c
    t["wallet"]=[inv[i][:10] for i in t.index]
    print(t.head(15).round(3).to_string())
# makers
for per in ["SEL","MEAS"]:
    x=L[L.per==per]
    t=x.groupby("mk").agg(c=("c_l","sum"),pnl=("pnl_l","sum")).sort_values("c",ascending=False)
    tot=t.c.sum(); print(per,"MAKERS",len(t),"top1 %.3f top5 %.3f top10 %.3f top20 %.3f"%tuple(t.c.head(k).sum()/tot for k in (1,5,10,20)))
