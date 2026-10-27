"""R8 emparejado: ejecucion completa segun ../PREREG.md. Solo lectura. R8E_SYNTH=<dir> usa datos sinteticos (autotest)."""
import os, sys, json, time, numpy as np, pandas as pd
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from r8e_lib import *
SY=os.environ.get("R8E_SYNTH"); NP=int(os.environ.get("R8E_NPLACEBO","500")); NB=int(os.environ.get("R8E_NBOOT","2000"))
OUT=os.environ.get("R8E_OUT","/mnt/HC_Volume_106538179/agentes_datos/r8_emparejado"); os.makedirs(OUT,exist_ok=True)
F6="/mnt/HC_Volume_106538179/agentes_datos/f6"; NEW="/mnt/HC_Volume_106538179/agentes_datos/b_sin_flujo"
if SY:
    DES=json.load(open(SY+"/des.json"))
else:
    DES=json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json"))
    for f in ("/root/polymarket-research-datalogs/mapa_escala/des.json","/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/b_vs_poblacion/datos/des_gamma.json"):
        for k,v in json.load(open(f)).items(): DES.setdefault(k,v)
def log(*a): print(time.strftime("%H:%M:%S"),*a,flush=True)
def load(d):
    p=(SY+f"/T_{d}.parquet") if SY else (F6+f"/T_2026-10-{d:02d}.parquet" if d<24 else NEW+"/T_2026-10-24.parquet")
    x=pd.read_parquet(p,columns=["ts","w","act","buy","acc","usd","fee","mkt","lado","cierre","p"])
    x["w"]=x.w.astype(str); x["mkt"]=x.mkt.astype(str); x["lado"]=x.lado.astype(str); x["act"]=x.act.astype(str)
    o=x.mkt.map(DES).values; w=np.where(o=="YES",1.0,np.where(o=="NO",0.0,np.nan)); x["win"]=np.where(x.lado.values=="YES",w,1-w); return x
DAYS=range(12,25)
# ---- pase 1: agregados por dia-wallet (para rosters)
aggf=OUT+"/agg.pkl"
if os.path.exists(aggf) and not SY: agg=pd.read_pickle(aggf)
else:
    L=[]
    for d in range(5,25):
        x=load(d); ok=~np.isnan(x.win.values); w=np.nan_to_num(x.win.values)
        pnl=np.where(x.buy,x.acc*w-x.usd,x.usd-x.acc*w)-x.fee; var=x.acc**2*x.p*(1-x.p); cost=np.where(x.buy,x.usd,x.acc-x.usd)
        g=pd.DataFrame({"w":x.w,"pnl":np.where(ok,pnl,0),"var":np.where(ok,var,0),"c":np.where(ok,cost,0),"n":ok.astype(int)}).groupby("w").sum(); g["d"]=d; L.append(g.reset_index())
        log("agg dia",d,"cobertura desenlace (filas)",round(ok.mean(),4))
    agg=pd.concat(L); 
    if not SY: agg.to_pickle(aggf)
def sets(D):
    h=agg[(agg.d>=D-7)&(agg.d<=D-1)].groupby("w")[["pnl","var","c","n"]].sum(); z=h.pnl/np.sqrt(h["var"].clip(lower=1e-9)); el=(h.n>=30)&(h.c>=200)
    return set(h.index[el&(z<=-2)]),set(h.index[el&(z>=2)]),set(h.index[el&(z>-2)])
# ---- datos por dia
days={}; info={}
for D in DAYS:
    x=load(D); R,Wn,EL=sets(D); d=Day(x,None); sR=d.inS_from(R)
    cnt=np.bincount(d.wal,minlength=d.nw)
    # cobertura de desenlace en grupos con evento bruto vs sin (supervivencia)
    r=d.raw; U=np.flatnonzero(r["uni"]); inR=np.asarray(pd.Index(d.uw).isin(R))[r["wal"]]
    ev_g=np.unique(r["g"][U][inR[U]]); gev=np.zeros(r["g"].max()+1,bool); gev[ev_g]=True
    cE=r["cap"][U][gev[r["g"][U]]]; kE=r["known"][U][gev[r["g"][U]]]; cN=r["cap"][U][~gev[r["g"][U]]]; kN=r["known"][U][~gev[r["g"][U]]]
    info[D]=dict(roster=len(R),cov_ev_cap=float((cE*kE).sum()/max(cE.sum(),1e-9)),cov_noev_cap=float((cN*kN).sum()/max(cN.sum(),1e-9)),n_uni=int(d.n))
    d.raw=None; days[D]=dict(d=d,R=sR,W=d.inS_from(Wn),EL=d.inS_from(EL),cnt=cnt); info[D]['ts_max_utc']=time.strftime('%Y-%m-%d %H:%M',time.gmtime(float(x.ts.max())));info[D]['ts_min_utc']=time.strftime('%Y-%m-%d %H:%M',time.gmtime(float(x.ts.min())));log('dia',D,info[D])
# ---- clusters
cl_list=[]; cl_day=[]
for D in DAYS:
    u=np.unique(days[D]["d"].cierre); days[D]["cl"]=np.searchsorted(u,days[D]["d"].cierre); days[D]["ncl"]=len(u); cl_list+=[(D,c) for c in u]; cl_day+= [D]*len(u)
NCL=len(cl_list); cl_day=np.array(cl_day); off={}; o=0
for D in DAYS: off[D]=o; o+=days[D]["ncl"]
rng=np.random.default_rng(20261026)
CNT=np.stack([np.bincount(rng.integers(0,NCL,NCL),minlength=NCL) for _ in range(NB)]).astype(np.float32)
dayidx=np.array([DAYS.index(x) for x in cl_day]); CD=np.stack([np.bincount(rng.integers(0,len(DAYS),len(DAYS)),minlength=len(DAYS)) for _ in range(NB)]).astype(np.float32)[:,dayidx]
log("clusters",NCL,"dias",len(DAYS),"bootstraps",NB)
def build(S_of,a,b,strict=False,cap5=False,use_reb=False):
    """devuelve por dia: X (4 x ncl x NCELL), elig, y estadisticos"""
    out={}
    for D in DAYS:
        d=days[D]["d"]; wt,ctrl,has=d.masks(S_of(D),a,b,strict,cap5); Tp,Tc,Cp,Cc,el=cellsums(d,wt,ctrl,use_reb=use_reb)
        pn=d.pnl+(d.reb if use_reb else 0); ncl=days[D]["ncl"]; idx=days[D]["cl"]*NCELL+d.cell
        X=np.stack([np.bincount(idx,v,ncl*NCELL).reshape(ncl,NCELL) for v in (wt*pn,wt*d.cap,ctrl*pn,ctrl*d.cap)])
        ev=np.isfinite(d.events(S_of(D))[0]); out[D]=dict(X=X,el=el,Tp=Tp,Tc=Tc,Cp=Cp,Cc=Cc,nev=int(ev.sum()),nevw=int(len(np.unique(d.g[wt>0]))),tot=(Tp.sum(),Tc.sum()))
    return out
def cellmask(kind,val):
    c=np.arange(NCELL); band_=c%7; minute_=(c//7)%5; coin_=(c//35)//2
    return {"coin":coin_,"band":band_,"minute":minute_}[kind]==val
def pooled(V,days_sel=None,sub=None):
    num=den=ab_n=ab_d=0.0
    for D in (days_sel or DAYS):
        v=V[D]; m=v["el"]&(sub if sub is not None else True); mu=np.where(v["Cc"]>0,v["Cp"]/np.maximum(v["Cc"],1e-12),0.)
        num+=((v["Tp"]-v["Tc"]*mu)*m).sum(); den+=(v["Tc"]*m).sum(); ab_n+=v["Tp"].sum(); ab_d+=v["Tc"].sum()
    return (num/den if den>0 else np.nan), den, (ab_n/ab_d if ab_d>0 else np.nan), ab_d
SCACHE={}
def getS(V,counts,D,cache):
    if cache and (D,id(counts)) in SCACHE: return SCACHE[(D,id(counts))]
    v=V[D]; k=counts[:,off[D]:off[D]+days[D]["ncl"]]; S=[(k@v["X"][i]).astype(np.float32) for i in range(4)]
    if cache: SCACHE[(D,id(counts))]=S
    return S
def boot(V,counts,sub=None,cache=False):
    num=np.zeros(NB); den=np.zeros(NB); an=np.zeros(NB); ad=np.zeros(NB)
    for D in DAYS:
        v=V[D]; S=getS(V,counts,D,cache); mu=np.where(S[3]>0,S[2]/np.maximum(S[3],1e-12),0.); m=v["el"]&(sub if sub is not None else True)
        num+=((S[0]-S[1]*mu)*m).sum(1); den+=(S[1]*m).sum(1); an+=S[0].sum(1); ad+=S[1].sum(1)
    with np.errstate(all="ignore"): return num/den, an/ad
def ci(x):
    x=x[np.isfinite(x)]
    if len(x)<10: return (float('nan'),float('nan'))
    return (float(np.percentile(x,5)),float(np.percentile(x,95)))
def pval(x):
    x=x[np.isfinite(x)]
    if len(x)<10: return float('nan')
    return float(min(1,2*min((x<=0).mean(),(x>=0).mean())+0))
R_of=lambda D: days[D]["R"]
RES={}
log("== variantes reales")
VAR={"primario":(5,60,{}),"pre":(-60,-5,{}),"post":(65,120,{}),"ini10":(10,60,{}),"ini15":(15,60,{}),"ini20":(20,60,{}),"estricto":(5,60,{"strict":True}),"cap5":(5,60,{"cap5":True}),"rebate":(5,60,{"use_reb":True}),"ganadoras_inv":(5,60,{})}
VV={}
for k,(a,b,kw) in VAR.items():
    S_of=(lambda D: days[D]["W"]) if k=="ganadoras_inv" else R_of
    VV[k]=build(S_of,a,b,**kw); ex,den,ab,abd=pooled(VV[k]); ca=(k=='primario'); be,ba=boot(VV[k],CNT,cache=ca); bed,bad=boot(VV[k],CD)
    RES[k]=dict(excess=ex,cap_matched=den,abs_ev=ab,cap_total=abd,cov=den/abd if abd else None,ic_cierre=ci(be),ic_dia=ci(bed),abs_ic_cierre=ci(ba),abs_ic_dia=ci(bad),
                eventos=sum(VV[k][D]["nev"] for D in DAYS),eventos_con_fill=sum(VV[k][D]["nevw"] for D in DAYS))
    if k!='primario':
        for D in DAYS: VV[k][D].pop('X')
    log(k,{q:(round(v,4) if isinstance(v,float) else v) for q,v in RES[k].items()})
# por dia, sin 2 mejores dias, mitades (primario)
V=VV["primario"]; exd={D:pooled(V,[D])[0] for D in DAYS}; absd={D:pooled(V,[D])[2] for D in DAYS}
best=sorted(exd,key=lambda q:-np.nan_to_num(exd[q],nan=-9))[:2]; rest=[D for D in DAYS if D not in best]
RES["dias"]=dict(exceso=exd,abs=absd,sin2mejores=pooled(V,rest)[0],mitad1=pooled(V,[D for D in DAYS if D<=17])[0],mitad2=pooled(V,[D for D in DAYS if D>=18])[0],mejores=best,dias_pos=int(sum(v>0 for v in exd.values())),
                abs_sin2=pooled(V,[D for D in DAYS if D not in sorted(absd,key=lambda q:-absd[q])[:2]])[2])
log("dias",RES["dias"])
RES["cobertura"]=info
# subgrupos (post-hoc)
SUB={}
for kind,vals in (("coin",range(5)),("band",range(7)),("minute",range(5))):
    for v in vals:
        m=cellmask(kind,v); ex,den,ab,_=pooled(V,sub=m); be,_=boot(V,CNT,sub=m,cache=True); SUB[f"{kind}={v}"]=dict(excess=ex,cap=den,ic=ci(be),p=pval(be))
for nm,ds in (("mitad=12-17",[D for D in DAYS if D<=17]),("mitad=18-24",[D for D in DAYS if D>=18])):
    ex,den,ab,_=pooled(V,ds); kk=np.zeros(NCL,bool); kk[[i for i,D in enumerate(cl_day) if D in ds]]=True
    be=np.full(NB,np.nan); 
    # bootstrap restringido a clusters de esas mitades
    bsub=[]; 
    for D in ds: pass
    num=np.zeros(NB); den_=np.zeros(NB)
    for D in ds:
        v=V[D]; S=getS(V,CNT,D,True); mu=np.where(S[3]>0,S[2]/np.maximum(S[3],1e-12),0.); num+=((S[0]-S[1]*mu)*v["el"]).sum(1); den_+=(S[1]*v["el"]).sum(1)
    be=num/den_; SUB[nm]=dict(excess=ex,cap=den,ic=ci(be),p=pval(be))
ps=np.array([v["p"] for v in SUB.values()]); o=np.argsort(ps); m=len(ps); q=np.empty(m); q[o]=np.minimum.accumulate((ps[o]*m/(np.arange(m)+1))[::-1])[::-1]
for (k,v),qq in zip(SUB.items(),q): v["q_BH"]=float(min(1,qq))
RES["subgrupos"]=SUB; log("subgrupos listos")
# ---- placebos
def draw_set(D,pool,rr):
    dd=days[D]; cnt=dd["cnt"]; Rm=dd["R"]; S=np.zeros(len(cnt),bool)
    rc=np.flatnonzero(Rm&(cnt>0)); bins=np.floor(np.log2(cnt)).astype(int); P=np.flatnonzero((pool&~Rm)&(cnt>0)); pb=bins[P]
    for b_,m in zip(*np.unique(bins[rc],return_counts=True)):
        c=P[pb==b_]
        if len(c)==0:
            if len(P)==0: continue
            c=P[np.abs(pb-b_)==np.abs(pb-b_).min()]
        S[rr.choice(c,m,replace=len(c)<m)]=True
    return S
def plac(pooltype,seed):
    rr=np.random.default_rng(seed); out=np.zeros(NP)
    for i in range(NP):
        num=den=0.0
        for D in DAYS:
            dd=days[D]; d=dd["d"]; pool=dd["EL"] if pooltype=="A" else np.ones(len(dd["cnt"]),bool)
            S=draw_set(D,pool,rr); wt,ctrl,_=d.masks(S,5,60); Tp,Tc,Cp,Cc,el=cellsums(d,wt,ctrl); mu=np.where(Cc>0,Cp/np.maximum(Cc,1e-12),0.); num+=((Tp-Tc*mu)*el).sum(); den+=(Tc*el).sum()
        out[i]=num/den if den>0 else np.nan
    return out
real=RES["primario"]["excess"]
for t,sd in (("A",11),("B",12)):
    pl=plac(t,sd); RES["placebo_"+t]=dict(media=float(np.nanmean(pl)),sd=float(np.nanstd(pl)),p95=float(np.nanpercentile(pl,95)),p=(float((1+(pl[np.isfinite(pl)]>=real).sum())/(np.isfinite(pl).sum()+1)) if np.isfinite(pl).sum()>=0.9*NP else float('nan')),n=int(np.isfinite(pl).sum())); log("placebo",t,RES["placebo_"+t])
# ---- gate
P=RES["primario"]; D_=RES["dias"]
G={"G0":bool(P["eventos"]>=40 and len(DAYS)>=10 and P["cov"] is not None and P["cov"]>=0.70),
   "G1":bool(P["excess"]>0 and P["ic_cierre"][0]>0 and P["ic_dia"][0]>0),
   "G2":bool(D_["sin2mejores"]>0 and D_["mitad1"]>0 and D_["mitad2"]>0),
   "G3":bool(RES["placebo_A"]["p"]<0.05 and RES["placebo_B"]["p"]<0.05),
   "G4":bool(RES["pre"]["excess"]<0.5*P["excess"]),
   "G5":bool(RES["ini10"]["excess"]>0 and RES["ini15"]["excess"]>0),
   "G6":bool(RES["estricto"]["excess"]>0),
   "G7":bool(P["abs_ic_cierre"][0]>0 and P["abs_ic_dia"][0]>0)}
if not G["G0"]: V_="DATA_BLOCKED"
elif all(G.values()): V_="PROMISING"
elif all(G[k] for k in ("G1","G2","G3","G4","G5","G6")) and not G["G7"]: V_="EXPLORATORY"
elif P["excess"]>0 and P["ic_cierre"][1]>=0.02: V_="EXPLORATORY"
else: V_="REJECTED"
RES["gate"]=G; RES["veredicto"]=V_; log("GATE",G,V_)
json.dump(RES,open(OUT+"/resultado.json","w"),default=lambda o:float(o) if isinstance(o,(np.floating,np.integer)) else str(o),indent=1)
