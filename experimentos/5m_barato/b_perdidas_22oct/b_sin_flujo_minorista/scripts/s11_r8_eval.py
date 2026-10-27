import numpy as np, pandas as pd
NEW="/mnt/HC_Volume_106538179/agentes_datos/b_sin_flujo"; rng=np.random.default_rng(5)
R=pd.read_pickle(NEW+"/R8.pkl"); C=pd.read_pickle(NEW+"/R8_ctrl.pkl")
def ev(x,p,c): return x[p].sum()/x[c].sum()
def bootc(df,p,c,key,nb=3000):
    g=df.groupby(key)[[p,c]].sum().values; i=rng.integers(0,len(g),(nb,len(g))); s=g[i].sum(1); r=s[:,0]/s[:,1]; return np.percentile(r,5),np.percentile(r,95),len(g)
E_=R[R.cap_W>0]; K=R[R.cap_C>0]
print("EVENTO W[+5,+60]: eventos con flujo %d, cap %.0f $, EV %.4f IC90 cierre (%.3f,%.3f) n_cierres=%d"%(len(E_),E_.cap_W.sum(),ev(E_,"pnl_W","cap_W"),*bootc(E_,"pnl_W","cap_W","cierre")))
print("   IC90 por dia (%.3f,%.3f) dias=%d"%bootc(E_,"pnl_W","cap_W","D"))
print("MISMO MERCADO-LADO despues [+65,+120]: n %d cap %.0f EV %.4f IC90 cierre (%.3f,%.3f)"%(len(K),K.cap_C.sum(),ev(K,"pnl_C","cap_C"),*bootc(K,"pnl_C","cap_C","cierre")[:2]))
Cc=C[C.cap>0]; print("CONTROL mercado sin evento, mismos segundos desde apertura: n %d cap %.0f EV %.4f IC90 cierre (%.3f,%.3f)"%(len(Cc),Cc.cap.sum(),ev(Cc,"pnl","cap"),*bootc(Cc,"pnl","cap","cierre")[:2]))
# diferencia pareada W - despues, por cierre
P=R[(R.cap_W>0)&(R.cap_C>0)].copy(); 
g=P.groupby("cierre")[["pnl_W","cap_W","pnl_C","cap_C"]].sum().values; i=rng.integers(0,len(g),(3000,len(g))); s=g[i].sum(1); d=s[:,0]/s[:,1]-s[:,2]/s[:,3]
print("DIF pareada W - despues: %.4f IC90 cierre (%.3f,%.3f) n=%d cierres=%d"%(ev(P,"pnl_W","cap_W")-ev(P,"pnl_C","cap_C"),np.percentile(d,5),np.percentile(d,95),len(P),len(g)))
dd=P.groupby("D").apply(lambda x: ev(x,"pnl_W","cap_W")-ev(x,"pnl_C","cap_C")); print("   dif por dia",dd.round(3).to_dict(),"; dias>0: %d/%d"%((dd>0).sum(),len(dd)), "; sin 2 mejores dias: %.4f"%dd.drop(dd.nlargest(2).index).mean())
# W vs control sin evento: dif y permutacion de etiquetas
dife=ev(E_,"pnl_W","cap_W")-ev(Cc,"pnl","cap")
A=pd.concat([E_.rename(columns={"pnl_W":"pnl","cap_W":"cap"})[["D","cierre","pnl","cap"]].assign(l=1),Cc[["D","cierre","pnl","cap"]].assign(l=0)])
perm=[]
for _ in range(500):
    A["l2"]=A.groupby("D").l.transform(lambda v: rng.permutation(v.values)); a=A[A.l2==1]; b=A[A.l2==0]; perm.append(a.pnl.sum()/a.cap.sum()-b.pnl.sum()/b.cap.sum())
print("DIF evento - control sin evento: %.4f ; permutacion p(>=)=%.3f"%(dife,(1+(np.array(perm)>=dife).sum())/501))
ddd=pd.DataFrame({"E":E_.groupby("D").apply(lambda x:ev(x,"pnl_W","cap_W")),"C":Cc.groupby("D").apply(lambda x:ev(x,"pnl","cap"))}); ddd["dif"]=ddd.E-ddd.C; print(ddd.round(3).T.to_string()); print("dias dif>0: %d/%d ; sin 2 mejores dias dif %.4f ; mitades %.4f / %.4f"%((ddd.dif>0).sum(),len(ddd),ddd.dif.drop(ddd.dif.nlargest(2).index).mean(),ddd.dif.iloc[:6].mean(),ddd.dif.iloc[6:].mean()))
print("EV por tramo T0 (elapsed al evento):"); R["tb"]=pd.cut(R.T0,[0,60,120,180,240,300]); print(R[R.cap_W>0].groupby("tb",observed=True).apply(lambda x: pd.Series({"n":len(x),"cap":x.cap_W.sum(),"EV":ev(x,"pnl_W","cap_W")})).round(3).to_string())
