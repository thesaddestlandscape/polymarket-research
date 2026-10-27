"""s8: Q1-Q4 (prereg b_sin_flujo_minorista). Solo lectura de agentes_datos/b_sin_flujo y ledger."""
import numpy as np, pandas as pd
NEW="/mnt/HC_Volume_106538179/agentes_datos/b_sin_flujo"; rng=np.random.default_rng(25)
U=pd.read_pickle(NEW+"/UB.pkl"); O=pd.read_pickle(NEW+"/ordenes_B.pkl"); MB=pd.read_pickle(NEW+"/match_B.pkl"); off=float(open(NEW+"/offset.txt").read())
U["band"]=np.floor(U.p/0.05).clip(1,5).astype(int); U["nyd"]=U.cl.isin(["DES","NUEVO"])
P=U[~U.isB]; Bd=U[U.isB]
def boot(v_num, v_den, groups, nb=3000):
    g=pd.DataFrame({"n":v_num,"d":v_den,"g":groups}).groupby("g").sum(); a=g.values; i=rng.integers(0,len(a),(nb,len(a))); s=a[i].sum(1)
    return g.n.sum()/g.d.sum(), np.percentile(s[:,0]/s[:,1],5), np.percentile(s[:,0]/s[:,1],95), len(a)
print("=== Q1a: B fill-level, cuota DES+NUEVO vs esperada (coin x dia x banda), por dia ===")
sh=P[P.cob].groupby(["act","dia","band"]).apply(lambda x: x.c[x.nyd].sum()/x.c.sum())
for dias in (["2026-10-20","2026-10-21","2026-10-22","2026-10-23"],):
    b=Bd[Bd.dia.isin(dias)&Bd.cob].copy(); b["e"]=sh.reindex(list(zip(b.act,b.dia,b.band))).values
    b["eC"]=b.e*b.c; b["oC"]=b.c*b.nyd
    d=(b.oC-b.eC)
    r=boot(d.values,b.c.values,b.cierre.values); print("todos 20-23: obs %.3f esp %.3f dif %.3f IC90 cierre (%.3f,%.3f) cierres=%d n=%d"%(b.oC.sum()/b.c.sum(),b.eC.sum()/b.c.sum(),r[0],r[1],r[2],r[3],len(b)))
    for dd,x in b.groupby("dia"): print("  ",dd,"n=%d obs %.3f esp %.3f"%(len(x),x.oC.sum()/x.c.sum(),x.eC.sum()/x.c.sum()))
    dd_=b.groupby("dia").apply(lambda x:(x.oC.sum()-x.eC.sum())/x.c.sum()); print("   dif por dia",dd_.round(3).to_dict(),"; sin mejor dia(menos negativo):",round(dd_.drop(dd_.idxmax()).mean(),3))
print("\n=== Q1b: flujo de OTROS al nivel exacto durante la vida de cada orden armada de B (ventana vida +-1.4 s) vs placebo (+60 s) ===")
Pn=P.copy(); Pn["s"]=Pn.ts-off; Pn["key"]=Pn.act+"|"+Pn.cierre.astype(int).astype(str)+"|"+Pn.lado+"|"+Pn.p.round(2).astype(str)
Pn=Pn.sort_values("s"); grp={k:(g.s.values,g.c.values,g.nyd.values,g.cl.values,g.acc.values) for k,g in Pn.groupby("key")}
O=O[O.dia.isin(["2026-10-20","2026-10-21","2026-10-22","2026-10-23"])].copy(); O["act"]=O.coin.str.upper(); O["band"]=np.floor(O.precio/0.05).clip(1,5).astype(int)
O["key"]=O.act+"|"+O.cierre.astype(str)+"|"+O.lado+"|"+O.precio.round(2).astype(str); O["vida"]=O.vida_s.fillna(O.vida_s.median())
TOL=1.4; EXT=12.0
def flow(row,a,b):
    g=grp.get(row.key); 
    if g is None: return (0.0,0.0,0.0)
    i0,i1=np.searchsorted(g[0],[a,b]); c=g[1][i0:i1]; y=g[2][i0:i1]; return (c.sum(), c[y].sum(), float(g[4][i0:i1].sum()))
rows=[]
for r in O.itertuples():
    ta=r.t_arm; tc=ta+r.vida
    life=flow(r,ta-TOL,tc+TOL); late=flow(r,tc+TOL,ta+EXT+TOL); plc=flow(r,ta+60-TOL,tc+60+TOL)
    rows.append((r.oid,r.dia,r.cierre,r.act,r.band,r.vida,)+life+late+plc)
F=pd.DataFrame(rows,columns=["oid","dia","cierre","act","band","vida","lc","ln","lk","ec","en","ek","pc","pn","pk"])
F["e"]=sh.reindex(list(zip(F.act,F.dia,F.band))).values
for nm,(c,n) in {"vida":("lc","ln"),"extension(vida,12s]":("ec","en"),"placebo +60 s":("pc","pn")}.items():
    x=F[F[c]>0]; r=boot((x[n]-x.e*x[c]).values,x[c].values,x.cierre.values)
    print("%-22s ordenes con flujo %5d de %d; € flujo %8.1f; cuota DES+NUEVO %.3f vs esperada %.3f; dif %.3f IC90 cierre (%.3f,%.3f); cierres=%d"%(nm,len(x),len(F),x[c].sum(),x[n].sum()/x[c].sum(),(x.e*x[c]).sum()/x[c].sum(),r[0],r[1],r[2],r[3]))
# M1: extension vs vida (pareado por orden con flujo en ambas)
x=F[(F.lc>0)&(F.ec>0)]
d=(x.en/x.ec - x.ln/x.lc) if False else None
G=F.groupby("cierre")[["lc","ln","ec","en"]].sum(); G=G[(G.lc>0)&(G.ec>0)]
i=rng.integers(0,len(G),(3000,len(G))); a=G.values[i].sum(1); dm=a[:,3]/a[:,2]-a[:,1]/a[:,0]
print("M1: cuota NYD en extension %.3f vs vida %.3f ; dif %.3f IC90 cierre (%.3f,%.3f) cierres=%d"%(G.en.sum()/G.ec.sum(),G.ln.sum()/G.lc.sum(),G.en.sum()/G.ec.sum()-G.ln.sum()/G.lc.sum(),np.percentile(dm,5),np.percentile(dm,95),len(G)))
print("tasa de llegada de flujo € por segundo armado: vida %.3f ; extension %.3f €/s (ordenes con vida>0)"%(F.lc.sum()/F.vida.sum(), F.ec.sum()/np.maximum(EXT-F.vida,0.1).sum()))
F=F.merge(O[["oid","cola","filled","f","T_post","size"]],on="oid"); F.to_pickle(NEW+"/F_flujo_nivel.pkl")
print("M2 (cola): ordenes con flujo de otros en la vida: n=%d ; relleno de B en ellas %.3f ; sin flujo (n=%d) relleno %.3f"%((F.lk>0).sum(),F.filled[F.lk>0].mean(),(F.lk==0).sum(),F.filled[F.lk==0].mean()))
x=F[F.lk>0].copy(); x["cubre"]=x.lk>=x.cola
print(x.groupby("cubre").agg(n=("oid","size"),fill=("filled","mean"),flujo_acc=("lk","median"),cola=("cola","median")).round(3).to_string())

print("\n=== Q2/Q3: rellenos de B emparejados con el ledger (n=%d) ==="%len(MB))
mb=MB.copy(); mb["Trem"]=300-mb["T"]; mb["clase"]=mb.cl; mb["nyd"]=mb.cl.isin(["DES","NUEVO"])
print(mb.groupby("clase").agg(n=("c","size"),eur=("c","sum"),espera_med=("espera_s","median"),espera_p90=("espera_s",lambda x:x.quantile(.9)),vida_med=("vida_s","median"),cola_med=("cola","median"),T_med_elapsed=("T","median"),p_med=("p","median"),acc_med=("acc","median"),roi_prev=("tk_roi","median")).round(2).to_string())
mb["grp"]=np.where(mb.cl=="INF","INF",np.where(mb.nyd,"DES+NUEVO","MIX"))
mb["wb"]=pd.cut(mb.espera_s,[0,1,2,4,100]); print(mb.groupby("wb",observed=True).apply(lambda x: pd.Series({"n":len(x),"€":x.c.sum(),"INF":x.c[x.cl=="INF"].sum()/x.c.sum(),"NYD":x.c[x.nyd].sum()/x.c.sum(),"MIX":x.c[x.cl=="MIX"].sum()/x.c.sum(),"EV":x.pnl.sum()/x.c.sum()})).round(3).to_string())
mb["cb"]=pd.cut(mb.cola,[-1,20,60,150,1e5]); print(mb.groupby("cb",observed=True).apply(lambda x: pd.Series({"n":len(x),"€":x.c.sum(),"INF":x.c[x.cl=="INF"].sum()/x.c.sum(),"NYD":x.c[x.nyd].sum()/x.c.sum(),"MIX":x.c[x.cl=="MIX"].sum()/x.c.sum(),"EV":x.pnl.sum()/x.c.sum()})).round(3).to_string())
print("Poblacion (otros, ETH/SOL/XRP 20-24 Oct) por clase: T elapsed med, p med, acc med, tk_roi med")
print(P.groupby("cl").agg(n=("c","size"),eur=("c","sum"),T_med=("T","median"),p_med=("p","median"),acc_med=("acc","median"),acc_p90=("acc",lambda x:x.quantile(.9))).round(2).to_string())
# 24-Oct: poblacion por clase EV (persistencia del lado poblacion)
for dd,x in P[P.cob].groupby("dia"): print(dd,"pob n=%d € %.0f cuota NYD %.3f EV %.4f"%(len(x),x.c.sum(),x.c[x.nyd].sum()/x.c.sum(),x.pnl.sum()/x.c.sum()),{c:round(y.pnl.sum()/y.c.sum(),3) for c,y in x.groupby("cl")})
