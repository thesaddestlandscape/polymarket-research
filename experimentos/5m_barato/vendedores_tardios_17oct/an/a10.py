exec(open("common_s.py").read())
P=P[(P.act=="BTC")&(P.dia!="2026-10-05")&(P.dia!="2026-10-17")]
P=P.assign(v60=np.where(P["T"]>240,P.acc,0.0).astype("float32"),v120=np.where(P["T"]>180,P.acc,0.0).astype("float32"))
g=P.groupby(["mkt","lado"],sort=False)
U=g.agg(fin=("fin","first"),dia=("dia","first"),per=("per","first"),tot=("acc","sum"),v60=("v60","sum"),v120=("v120","sum"),ncl=("acc","size")).reset_index()
# tiempo en que cum cruza 2000
P2=P[P.cum0+P.acc>=2000].groupby(["mkt","lado"]).agg(T2000=("T","max")).reset_index()
U=U.merge(P2,on=["mkt","lado"],how="left")
U["h2000"]=(U.tot>=2000).astype(int); U["h500"]=(U.tot>=500).astype(int)
U["hora"]=pd.to_datetime(U.fin,unit="s").dt.hour
print("unidades BTC con alguna banda:",len(U),"alcanzan 500:",U.h500.sum(),"alcanzan 2000:",U.h2000.sum())
print("T restante (s) al cruzar 2000 acc: cuantiles",U.T2000.quantile([.1,.25,.5,.75,.9]).round(0).to_dict())
def auc(score,y):
    r=pd.Series(score).rank().values; n1=y.sum(); n0=len(y)-n1
    return (r[y==1].sum()-n1*(n1+1)/2)/(n1*n0)
for nm,x in [("SEL",U[U.per=="SEL"]),("MEAS",U[U.per=="MEAS"])]:
    print(nm,"unidades",len(x),"P(2000)=%.3f"%x.h2000.mean(),"AUC v60->h2000 %.3f"%auc(x.v60.values,x.h2000.values),"AUC v120->h2000 %.3f"%auc(x.v120.values,x.h2000.values),
       "AUC v60 solo entre las que tuvieron fills a T>240: %.3f"%(auc(x[x.v60>0].v60.values,x[x.v60>0].h2000.values)))
# persistencia entre mercados consecutivos (mismo lado)
U=U.sort_values(["lado","fin"]); U["prev"]=U.groupby("lado").h2000.shift(1); U["gap"]=U.groupby("lado").fin.diff()
V=U[(U.gap==300)&U.prev.notna()]
for nm,x in [("SEL",V[V.per=="SEL"]),("MEAS",V[V.per=="MEAS"])]:
    print(nm,"P(h2000|prev heavy)=%.3f  P(h2000|prev no)=%.3f  n %d"%(x[x.prev==1].h2000.mean(),x[x.prev==0].h2000.mean(),len(x)))
# hora del dia
print("P(h2000) por bloque de 4 h SEL / MEAS:")
U["hb"]=(U.hora//4)*4
print(U.groupby(["hb","per"],observed=True).h2000.mean().unstack().round(3).to_string())
# probabilidad de que el lado barato alcance 2000 condicionado a que ya alcanzo 500 y T restante
x=U[U.h500==1]; print("P(2000|500) %.3f"%x.h2000.mean())
# distribucion de T restante cuando se cruza 500 (llegada)
P3=P[P.cum0+P.acc>=500].groupby(["mkt","lado"]).agg(T500=("T","max")).reset_index()
print("T restante al cruzar 500:",P3.T500.quantile([.1,.25,.5,.75,.9]).round(0).to_dict())
