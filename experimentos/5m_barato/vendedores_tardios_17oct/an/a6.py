exec(open("common.py").read())
rng=np.random.default_rng(11)
wid=pickle.load(open("wid.pkl","rb")); inv={v:k for k,v in wid.items()}
L=P[(P.acc_l>0)&(P.dia!="2026-10-05")&(P.dia!="2026-10-17")].copy()
# unidad: taker x mercado-lado  (para no contar fills)
U=L.groupby(["tk","mkt","lado","per"],observed=True).agg(c=("c_l","sum"),pn=("pnl_l","sum"),acc=("acc_l","sum"),dia=("dia","first")).reset_index()
print("unidades taker-mercado-lado",len(U))
S=U[U.per=="SEL"].groupby("tk").agg(c=("c","sum"),pn=("pn","sum"),n=("c","size"),dias=("dia","nunique"))
M=U[U.per=="MEAS"].groupby("tk").agg(c=("c","sum"),pn=("pn","sum"),n=("c","size"),dias=("dia","nunique"))
S["ev"]=S.pn/S.c; M["ev"]=M.pn/M.c
print("takers SEL",len(S),"MEAS",len(M),"ambos",len(S.index.intersection(M.index)))
# 1) persistencia de PRESENCIA (seleccion por volumen, no por resultado): >=4 dias de 4 (06-09) y >=20 unidades
Sd=U[U.per=="SEL"].groupby("tk").agg(dias=("dia","nunique"),n=("c","size"),c=("c","sum"))
core=Sd[(Sd.dias>=4)&(Sd.n>=40)].index
print("nucleo presencia SEL (>=4 dias de 4 con datos completos 06-09, >=40 unidades):",len(core))
Mx=U[U.per=="MEAS"]
for nm,idx in [("nucleo",core),("resto",Sd.index.difference(core)),("nuevos en MEAS (no vistos en SEL)",M.index.difference(Sd.index))]:
    y=Mx[Mx.tk.isin(idx)]
    print(f"  {nm:38} wallets {len(idx):6d} share coste MEAS {y.c.sum()/Mx.c.sum():.3f} EV maker {y.pn.sum()/y.c.sum():+.4f} dias+ {sum(1 for _,z in y.groupby('dia') if z.pn.sum()>0)}/7")
# 2) seleccion por resultado en SEL: top/bottom decil por EV maker (min 40 unidades), medir en MEAS
cand=S[(S.n>=40)&(S.c>2000)].copy()
cand=cand.join(M[["c","pn","n"]].rename(columns=lambda s:s+"_m"),how="left")
cand["q"]=pd.qcut(cand.ev.rank(method="first"),10,labels=False)
print("\ncandidatos (n>=40 unidades y coste>2000 en SEL):",len(cand))
for q in [9,8,5,1,0]:
    x=cand[cand.q==q]; print(f"  decil {q} (EV SEL {x.pn.sum()/x.c.sum():+.3f}): wallets {len(x)}  MEAS coste {x.c_m.sum():.0f} EV {x.pn_m.sum()/x.c_m.sum():+.4f} (con datos MEAS: {x.c_m.notna().sum()})")
print("  Spearman ev SEL vs ev MEAS (wallets con n>=20 en MEAS):",cand.assign(evm=cand.pn_m/cand.c_m)[cand.n_m>=20][["ev","evm"]].corr(method="spearman").iloc[0,1])
# placebo: 1000 conjuntos aleatorios del mismo tamaño que el decil superior
x=cand[cand.q==9]; k=len(x); vals=[]
pool=cand[cand.c_m.notna()]
for _ in range(1000):
    z=pool.sample(k,random_state=int(rng.integers(1e9))); vals.append(z.pn_m.sum()/z.c_m.sum())
print("  placebo (aleatorios de igual tamano, mismo universo): media %.4f  p5 %.4f p95 %.4f ; decil top real %.4f"%(np.mean(vals),np.percentile(vals,5),np.percentile(vals,95),x.pn_m.sum()/x.c_m.sum()))
# 3) top perdedores globales (11 dias): perfil
T=U.groupby("tk").agg(c=("c","sum"),pn=("pn","sum"),n=("c","size"),dias=("dia","nunique"),acc=("acc","sum")).sort_values("pn",ascending=False)
T["w"]=[inv[i][:10] for i in T.index]; T["ev"]=T.pn/T.c; T["acc_u"]=T.acc/T.n
print("\nTop 15 tomadores por PnL del maker (= perdida del tomador) 06-16 Oct, tardio")
print(T.head(15).round(2).to_string())
print("Top 8 por PnL negativo del maker (tomadores que ganan):"); print(T.tail(8).round(2).to_string())
print("suma pn top15 %.0f de total %.0f ; suma sin top15 %.0f ; c total %.0f"%(T.pn.head(15).sum(),T.pn.sum(),T.pn.sum()-T.pn.head(15).sum(),T.c.sum()))
