exec(open("common_s.py").read())
rng=np.random.default_rng(21)
P=P[(P.acc_l>0)&(P.dia!="2026-10-05")&(P.dia!="2026-10-17")][["tk","mkt","lado","act","cl","inv_s","inv_ns","tk_acc","c_l","pnl_l","acc_l","dia","per","nmk"]].copy()
import gc; gc.collect()
def ic(x):
    dd=x.groupby("dia",observed=True)[["pnl_l","c_l"]].sum()
    if len(dd)<3: return (np.nan,np.nan,0,len(dd))
    b=[ (lambda i: dd.pnl_l.values[i].sum()/dd.c_l.values[i].sum())(rng.integers(0,len(dd),len(dd))) for _ in range(2000)]
    return (*np.percentile(b,[5,95]),(dd.pnl_l>0).sum(),len(dd))
SELd=P[P.per=="SEL"]
perfil=SELd.groupby("tk").agg(dias=("dia","nunique"),n=("c_l","size"))
# unidades por taker en SEL
un=SELd.groupby(["tk"]).apply(lambda x: x.groupby(["mkt","lado"]).ngroups,include_groups=False)
core=un[(perfil.dias>=4)&(un>=40)].index
M=P[P.per=="MEAS"]
vistos=perfil.index
grp=np.where(M.tk.isin(core),"NUCLEO",np.where(M.tk.isin(vistos),"RESTO_SEL","NUEVO_MEAS"))
M=M.assign(g=grp)
print("GRUPOS de tomador (definidos con presencia en SEL, medidos en MEAS 10-16 Oct), volumen tardio")
rows=[]
for g_,x in M.groupby("g"):
    lo,hi,pos,nd=ic(x); rows.append((g_,x.tk.nunique(),len(x),x.c_l.sum()/M.c_l.sum(),x.acc_l.sum() and x.c_l.sum()/x.acc_l.sum(),ev(x.pnl_l,x.c_l),lo,hi,f"{pos}/{nd}"))
print(pd.DataFrame(rows,columns=["grupo","wallets","fills","share_coste","px","EV_maker","IC90lo","IC90hi","dias+"]).round(3).to_string(index=False))
# placebo del nucleo: 554 wallets al azar de SEL con volumen similar (mismo decil de coste SEL)
sc=SELd.groupby("tk").c_l.sum(); 
cand=sc.index.difference(core); ev_pl=[]
mm=M.groupby("tk")[["pnl_l","c_l"]].sum()
nuc_c=sc.loc[core]
for _ in range(500):
    pick=[]
    # emparejar por cuantil de coste
    qs=pd.qcut(sc,10,labels=False,duplicates="drop"); qn=qs.loc[core].value_counts()
    for q,k in qn.items():
        pool=qs[(qs==q)&(~qs.index.isin(core))].index
        pick+=list(rng.choice(pool,size=min(k,len(pool)),replace=False))
    z=mm.reindex(pick).dropna(); ev_pl.append(z.pnl_l.sum()/z.c_l.sum())
nuc=M[M.tk.isin(core)]
print("placebo NUCLEO (wallets SEL no-nucleo emparejadas por decil de coste): media %.3f p5 %.3f p95 %.3f ; NUCLEO real %.3f"%(np.mean(ev_pl),np.percentile(ev_pl,5),np.percentile(ev_pl,95),ev(nuc.pnl_l,nuc.c_l)))
# top-5 persistentes pesados (coste SEL) y su cuota MEAS
top=sc.sort_values(ascending=False).head(10).index
x=M[M.tk.isin(top)]
print("top10 tomadores por coste en SEL: cuota MEAS %.3f EV %.3f n wallets presentes %d"%(x.c_l.sum()/M.c_l.sum(),ev(x.pnl_l,x.c_l),x.tk.nunique()))
# estados
vend=(M.cl=="VENDE_s").values; a=(M.inv_s>0.5).values; b=(M.inv_ns>0.5).values
code=np.where(vend,np.where(a,np.where(b,0,1),np.where(b,2,3)),np.where(b,np.where(a,4,5),np.where(a,6,7)))
names=["VENDE_s|dueno_s+ns(deshace par)","VENDE_s|dueno_s(liquida)","VENDE_s|solo_ns","VENDE_s|sin_inv(mint/ext)","COMPRA_ns|dueno_s+ns(amplia par)","COMPRA_ns|dueno_ns(refuerza fav)","COMPRA_ns|dueno_s(cubre)","COMPRA_ns|sin_inv(nuevo)"]
M=M.assign(st=pd.Categorical.from_codes(code,names))
rows=[]
for s,x in M.groupby("st",observed=True):
    lo,hi,pos,nd=ic(x); rows.append((s,x.tk.nunique(),x.groupby(["mkt","lado"]).ngroups,x.c_l.sum()/M.c_l.sum(),ev(x.pnl_l,x.c_l),lo,hi,f"{pos}/{nd}"))
print("\nESTADO previo del tomador (MEAS)"); print(pd.DataFrame(rows,columns=["estado","wallets","unidades","share_coste","EV_maker","lo","hi","dias+"]).round(3).to_string(index=False))
# tamano del fill del tomador
M["tkb"]=pd.cut(M.tk_acc,[0,10,50,200,1e9]); rows=[]
for s,x in M.groupby("tkb",observed=True):
    lo,hi,pos,nd=ic(x); rows.append((str(s),x.tk.nunique(),x.c_l.sum()/M.c_l.sum(),ev(x.pnl_l,x.c_l),lo,hi,f"{pos}/{nd}"))
print("\nTAMANO fill del tomador (acc) MEAS"); print(pd.DataFrame(rows,columns=["tam","wallets","share_coste","EV_maker","lo","hi","dias+"]).round(3).to_string(index=False))
