import pandas as pd, numpy as np, pickle, json
from scipy import stats as st
O='/root/polymarket-research-datalogs/x_salida/'
S=pickle.load(open(O+'datasets.pkl','rb')); rng=np.random.default_rng(20261025)
DB,DP=S['DB'].copy(),S['DP'].copy(); DB['dia']=DB.fin//86400; DP['dia']=DP.fin//86400
out={}
def momentos(df,nombre):
    df=df.copy(); mu=df.pnl.sum()/df.coste.sum(); df['e']=df.pnl-mu*df.coste
    sig2=(df.e**2).sum()/(df.coste**2).sum()*(df.coste.mean())/(df.coste.mean())  # varianza de retorno por EUR ponderada por coste^2
    r=df.pnl/df.coste; sig2w=(df.coste*(r-mu)**2).sum()/df.coste.sum()
    cl=df.groupby('fin').e.agg(['sum',lambda x:(x**2).sum()]); deff=(cl['sum']**2).sum()/cl.iloc[:,1].sum()
    # bootstrap por cierre y por dia (EV)
    g=df.groupby('fin').agg(p=('pnl','sum'),c=('coste','sum'),d=('dia','first')); B=[]
    for _ in range(2000):
        ix=rng.integers(0,len(g),len(g)); B.append(g.p.values[ix].sum()/g.c.values[ix].sum())
    ic_cierre=[float(np.percentile(B,5)),float(np.percentile(B,95))]
    dd=df.groupby('dia').agg(p=('pnl','sum'),c=('coste','sum'),n=('pnl','size')); evd=dd.p/dd.c
    comp=dd[dd.n>=0.6*dd.n.median()]; evc=(comp.p/comp.c)
    t=st.t.ppf(.95,len(evc)-1) if len(evc)>1 else np.nan
    se=evc.std(ddof=1)/np.sqrt(len(evc)) if len(evc)>1 else np.nan
    ndias=len(comp); npd=comp.n.mean(); cd=comp.c.mean()
    neff=npd/deff
    res=dict(n=int(len(df)),cierres=int(len(g)),EV_pond=float(mu),EV_ic90_cierre=ic_cierre,EV_por_dia={str(k):float(v) for k,v in evd.items()},n_dias_completos=int(ndias),
      EV_ic90_dias=[float(evc.mean()-t*se),float(evc.mean()+t*se)] if ndias>1 else None,sigma2_por_eur=float(sig2w),DEFF=float(deff),pos_por_dia=float(npd),n_eff_dia=float(neff),
      nocional_dia=float(cd),f_kelly=float(max(mu,0)/(sig2w*deff)),g_dia_kelly=float(neff*max(mu,0)**2/(2*sig2w)))
    return res
out['B']=momentos(DB,'B'); out['DP']=momentos(DP,'DP')
# DP sin dia incompleto 22
print(json.dumps({k:{a:b for a,b in v.items() if a!='EV_por_dia'} for k,v in out.items()},indent=0,default=float)[:1800])
# --- tabla EV -> nocional/dia para 200k
tab=[]
for ev in (0.03,0.05,0.07,0.11,0.20,0.30):
    for dias in (365,260):
        N=200000/(ev*dias); tab.append(dict(EV=ev,dias=dias,nocional_dia=N,vs_B_real=N/out['B']['nocional_dia'],vs_R3_techo_K20=N/(130*2.44),vs_pool_DP=N/out['DP']['nocional_dia'],fills_dia_a_2_44=N/2.44))
out['tabla_200k']=tab
# --- reinversion por tramos
DP['r']=DP.pnl/DP.coste; DPs=DP.sort_values('fin'); ids=pd.factorize(DPs.fin)[0]; cnt=np.bincount(ids); stt=np.cumsum(cnt)-cnt; rr=DPs.r.values
NP_=300000; cc=rng.integers(0,len(cnt),NP_); mm=np.minimum(1+rng.poisson(.8,NP_),4); Sc=np.zeros(NP_)
for j_ in range(4):
    u=stt[cc]+(rng.random(NP_)*cnt[cc]).astype(int); Sc+=np.where(mm>j_,rr[u],0.0)
Mc=mm.astype(float); rmean=Sc.sum()/Mc.sum(); sig2p=float(((rr-rr.mean())**2).mean()); deffp=float(((Sc-rmean*Mc)**2).sum()/(sig2p*Mc.sum()))
out['pool_pseudoB']={'EV_pool_pseudoB(cierre-igual-peso)':float(rmean),'EV_DP_pond':out['DP']['EV_pond'],'sigma2':sig2p,'DEFF':deffp,'pos_por_cierre':float(Mc.mean())}
print(out['pool_pseudoB'])
sig2,deff=sig2p,deffp
CAP=2.44; DET=0.017
def mc(EV,W0,npos,guard,dias=730,N=2000):
    fK=EV/(sig2*deff); K=int(round(npos/Mc.mean()))
    W=np.full(N,W0); alive=np.ones(N,bool); cap_day=np.full(N,np.nan); ruin=np.zeros(N,bool); inc=np.zeros(N); shift=EV-rmean
    for d in range(dias):
        s=np.clip(0.5*fK*W,1.05,CAP)
        ok=alive&(W>=4.2)
        if guard: ok&=(s/W<=2*fK)
        ix=rng.integers(0,len(Sc),(N,K)); ret=(Sc[ix]+shift*Mc[ix]).sum(1); det=DET*(s/CAP)*Mc[ix].sum(1)
        pnl=np.where(ok,s*(ret-det),0.0); W=W+pnl
        hit=ok&(s>=CAP-1e-9)&np.isnan(cap_day); cap_day[hit]=d
        newr=(W<5.0)&alive; ruin|=newr; alive&=~newr
        if d>=dias-365: inc+=pnl
    q=lambda a,p: float(np.percentile(a,p))
    return dict(fKelly=fK,K_cierres=K,P_ruina=float(ruin.mean()),P_tope=float((~np.isnan(cap_day)).mean()),dia_tope_p50=float(np.nanmedian(cap_day)) if (~np.isnan(cap_day)).any() else None,
                W_final_p50=q(W,50),ingreso_ultimo_ano_p10=q(inc,10),ingreso_ultimo_ano_p50=q(inc,50),ingreso_ultimo_ano_p90=q(inc,90),W_tope_halfK=CAP/(0.5*fK),W_min_stake_Kelly=1.05/(0.5*fK),W_min_crec_pos=1.05/(2*fK))
rein=[]
for EV in (0.03,0.07,0.11,0.20):
    for W0 in (19.59,75.0,150.0,300.0):
        for npos in (73,130):
            for guard in (False,True):
                r=mc(EV,W0,npos,guard); r.update(EV=EV,W0=W0,npos=npos,guard=guard); r['ingreso_teorico_tope']=npos*CAP*(EV-DET)*365; rein.append(r)
out['reinversion']=rein
for r in rein: print(' '.join(f"{k}={round(v,3) if isinstance(v,float) else v}" for k,v in r.items() if k in ('EV','W0','npos','guard','P_ruina','P_tope','dia_tope_p50','ingreso_ultimo_ano_p50','ingreso_ultimo_ano_p10','ingreso_ultimo_ano_p90','W_min_crec_pos','ingreso_teorico_tope')))
# --- grande: stake 100/250/etc. si el libro absorbiera (SCENARIO, sin deterioro): ingreso = npos*stake*EV*365
out['hueco']={'VALIDATED':0.0,'B_hoy_EV':out['B']['EV_pond'],'techo_R3_K20_base_SCENARIO':[2400,6100],'techo_R3_optimista_SCENARIO':10800,'fuente':'plan_escalado/ADENDA_22OCT_B_R3.md §2'}
json.dump(out,open(O+'parteC.json','w'),indent=1,default=float)
