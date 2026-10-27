"""s9: politicas P1 hold X s / P3 top-1c / P2 late como COTA OPTIMISTA (replay FIFO bloqueado por validacion: ver s8). B asume ir primero en la cola, tamano 5.
Flujo = rellenos de OTROS al nivel exacto (on-chain, reloj corregido, tol 1.4 s). Placebo = ventanas desplazadas."""
import numpy as np, pandas as pd
NEW="/mnt/HC_Volume_106538179/agentes_datos/b_sin_flujo"; rng=np.random.default_rng(7)
U=pd.read_pickle(NEW+"/UB.pkl"); O=pd.read_pickle(NEW+"/ordenes_B.pkl"); off=float(open(NEW+"/offset.txt").read())
U["nyd"]=U.cl.isin(["DES","NUEVO"]); Pn=U[~U.isB&U.cob].copy(); Pn["s"]=Pn.ts-off; Pn["key"]=Pn.act+"|"+Pn.cierre.astype(int).astype(str)+"|"+Pn.lado+"|"+Pn.p.round(2).astype(str)
Pn["ppu"]=Pn.pnl/Pn.acc  # pnl por accion
Pn=Pn.sort_values("s"); grp={k:(g.s.values,g.acc.values,g.ppu.values,g.nyd.values) for k,g in Pn.groupby("key")}
O=O[O.dia.isin(["2026-10-20","2026-10-21","2026-10-22","2026-10-23"])].copy(); O["act"]=O.coin.str.upper(); O["vida"]=O.vida_s.fillna(O.vida_s.median()); O["tc"]=O.t_arm+O.vida
TOL=1.4; SZ=5.0
def take(key,a,b,p):
    g=grp.get(key)
    if g is None: return None
    i0,i1=np.searchsorted(g[0],[a,b]); 
    if i1<=i0: return None
    rem=SZ; sh=[];pn=[];ny=[]
    for j in range(i0,i1):
        t=min(rem,g[1][j]); sh.append(t); pn.append(t*g[2][j]); ny.append(g[3][j]); rem-=t
        if rem<=1e-9: break
    sh=np.array(sh); return sh.sum(), np.sum(pn), p*sh.sum(), float((sh*np.array(ny)).sum())
def run(win, level_off=0.0, shift=0.0):
    out=[]
    for r in O.itertuples():
        p=round(r.precio-level_off,2)
        if p<0.05: continue
        key=f"{r.act}|{r.cierre}|{r.lado}|{p}"
        a,b=win(r); res=take(key,a+shift,b+shift,p)
        if res: out.append((r.cierre,r.dia,)+res)
    return pd.DataFrame(out,columns=["cierre","dia","sh","pnl","c","nysh"])
def ev(d,base):  # base: DataFrame con cierre, dia, pnl, c
    x=pd.concat([base[["cierre","dia","pnl","c"]],d[["cierre","dia","pnl","c"]]]); return x
def boot(x,nb=2000):
    g=x.groupby("cierre")[["pnl","c"]].sum().values; i=rng.integers(0,len(g),(nb,len(g))); s=g[i].sum(1); return np.percentile(s[:,0]/s[:,1],5),np.percentile(s[:,0]/s[:,1],95)
Bf=U[U.isB&U.cob&U.dia.isin(["2026-10-20","2026-10-21","2026-10-22","2026-10-23"])][["cierre","dia","pnl","c"]].copy()
b_ev=Bf.pnl.sum()/Bf.c.sum(); lo,hi=boot(Bf); print("BASE B fills reales n=%d € %.1f EV %.4f IC90 cierre (%.3f,%.3f)"%(len(Bf),Bf.c.sum(),b_ev,lo,hi))
pol={}
for X in (3,6,12): pol[f"P1_hold_{X}s"]=(lambda r,X=X:(r.tc+TOL, r.t_arm+X+TOL),0.0)
pol["P3_top-1c_vida_real"]=(lambda r:(r.t_arm-TOL,r.tc+TOL),0.01)
pol["P3_top-1c_hold6"]=(lambda r:(r.t_arm-TOL,r.t_arm+6+TOL),0.01)
rows=[];pv=[]
for nm,(w,lo_) in pol.items():
    add=run(w,lo_); ev_add=add.pnl.sum()/add.c.sum() if len(add) else np.nan
    # placebo: desplazamientos
    pl=[]
    for s in np.arange(-240,241,16):
        if abs(s)<20: continue
        a=run(w,lo_,s); pl.append(a.pnl.sum()/a.c.sum() if len(a) and a.c.sum()>0 else np.nan)
    pl=np.array([v for v in pl if v==v]); p=(1+(pl>=ev_add).sum())/(1+len(pl))
    comb=ev(add,Bf); lo,hi=boot(comb); dlt=comb.pnl.sum()/comb.c.sum()-b_ev
    # delta bootstrap por cierre
    cl=sorted(set(comb.cierre)); G=comb.groupby("cierre")[["pnl","c"]].sum(); Gb=Bf.groupby("cierre")[["pnl","c"]].sum().reindex(G.index).fillna(0)
    i=rng.integers(0,len(G),(2000,len(G))); s1=G.values[i].sum(1); s0=Gb.values[i].sum(1); dd=s1[:,0]/s1[:,1]-s0[:,0]/s0[:,1]
    perd=comb.groupby("dia")[["pnl","c"]].sum(); perd0=Bf.groupby("dia")[["pnl","c"]].sum()
    dday=(perd.pnl/perd.c-perd0.pnl/perd0.c).round(3).to_dict()
    rows.append(dict(politica=nm,n_add=len(add),eur_add=round(add.c.sum(),1),EV_add=round(ev_add,3),nyd_share_add=round(add.nysh.sum()/add.sh.sum(),3) if len(add) else np.nan,
        EV_comb=round(comb.pnl.sum()/comb.c.sum(),4),delta=round(dlt,4),delta_IC90_cierre=(round(np.percentile(dd,5),3),round(np.percentile(dd,95),3)),placebo_p=round(p,3),placebo_med=round(np.median(pl),3),delta_por_dia=dday))
    pv.append(p)
R=pd.DataFrame(rows)
# BH-FDR sobre placebo p
o=np.argsort(pv); m=len(pv); q=np.empty(m); prev=1
for rank,i_ in list(enumerate(o,1))[::-1]: prev=min(prev,pv[i_]*m/rank); q[i_]=prev
R["bh_q"]=q.round(3); pd.set_option("display.width",250); pd.set_option("display.max_colwidth",120); print(R.to_string())
# P2 late sobre fills reales (descriptivo): T restante en armado <=150 s
M=pd.read_pickle(NEW+"/match_B.pkl"); M["Trem"]=300-M["T"]
for nm,m_ in (("armado T restante<=150 s",M.Trem<=150),("T restante>150 s",M.Trem>150)):
    x=M[m_]; print("P2",nm,"n=%d € %.1f EV %.3f NYD share € %.3f"%(len(x),x.c.sum(),x.pnl.sum()/x.c.sum(),x.c[x.cl.isin(['DES','NUEVO'])].sum()/x.c.sum()), "ordenes B armadas con T<=150:", int((O.T_post<=150).sum()),"de",len(O))
