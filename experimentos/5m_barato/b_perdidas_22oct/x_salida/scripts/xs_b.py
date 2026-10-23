import pandas as pd, numpy as np, pickle, json, time, sys
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/x_salida/scripts')
from xs_sim import sim,REGLAS
from scipy import stats as st
O='/root/polymarket-research-datalogs/x_salida/'
S=pickle.load(open(O+'datasets.pkl','rb')); rng=np.random.default_rng(20261024)
DB,DP=S['DB'],S['DP']
def flow_from(df,tcol='fin',order='t'):
    f=[]
    for fin,g in df.groupby('fin',sort=True):
        g=g.sort_values(order) if order in g else g
        f.append((int(fin),int(fin//86400),tuple(g.coste.values),tuple(g.pnl.values)))
    return f
def permute_within_day(flow):
    out=[]; byd={}
    for i,(t,d,c,p) in enumerate(flow): byd.setdefault(d,[]).append(i)
    res=[None]*len(flow)
    for d,ix in byd.items():
        contents=[(flow[i][2],flow[i][3]) for i in ix]; perm=rng.permutation(len(ix))
        for k,i in enumerate(ix): res[i]=(flow[i][0],d,contents[perm[k]][0],contents[perm[k]][1])
    return res
def runall(flow,E_ini,H=12.0):
    return {k:sim(flow,r,E_ini,H=H) for k,r in REGLAS.items()}
def ev(m): return m['pnl']/m['cost'] if m['cost']>0 else np.nan
out={}; t0=time.time()
# ---------- E-B
fB=flow_from(DB.assign(fin=DB.fin))
res={}
for nm,Ei,Hh in (('S_real',19.59,12.0),('S_free',40.0,12.0),('S_H0_POSTHOC',19.59,0.0)):
    base=runall(fB,Ei,Hh); NP=2000
    perm=[runall(permute_within_day(fB),Ei,Hh) for _ in range(NP)]
    # bootstrap de bloques de cierres (6) para IC90 de delta
    nb=len(fB); boots=[]
    for _ in range(500):
        idx=[];
        while len(idx)<nb:
            s=rng.integers(0,nb); idx+=list(range(s,min(s+6,nb)))
        idx=idx[:nb]; fl=[(fB[i][0]+0*k,fB[i][1],fB[i][2],fB[i][3]) for k,i in enumerate(idx)]
        # reordenar tiempos para mantener monotonia: t sintetico = indice*300, dia = el original (transiciones de dia por cambio)
        fl=[(k*300,fl[k][1],fl[k][2],fl[k][3]) for k in range(nb)]
        boots.append(runall(fl,Ei,Hh))
    tab={}
    for k in REGLAS:
        d=base[k]['pnl']-base['R0']['pnl']; dp=np.array([p[k]['pnl']-p['R0']['pnl'] for p in perm]); db=np.array([b[k]['pnl']-b['R0']['pnl'] for b in boots])
        tab[k]=dict(pnl=base[k]['pnl'],takes=base[k]['takes'],cost=base[k]['cost'],EV=ev(base[k]),dd=base[k]['dd'],halted=base[k]['halted'],
          d_vs_R0=d,d_perm_mean=float(dp.mean()),d_est=float(d-dp.mean()),p_placebo=float((1+(dp>=d).sum())/(NP+1)),
          d_boot_ic90=[float(np.percentile(db,5)),float(np.percentile(db,95))],
          dEV=(ev(base[k])-ev(base['R0'])) if base[k]['cost']>0 and base['R0']['cost']>0 else None)
    res[nm]=tab; print('E-B',nm,'R0',tab['R0'],round(time.time()-t0),flush=True)
out['E-B']=res
# ---------- perfil horario de B y flujo pseudo-B
DBc=DB.groupby('fin').size().reset_index(); DBc['h']=(DBc.fin%86400)//3600
t_a,t_b=DB.t.min(),DB.t.max()
cov=np.zeros(24)
for tt in range(int(t_a//3600),int(t_b//3600)+1): cov[tt%24]+=1
nBh=np.bincount(DBc.h.astype(int),minlength=24)
DPc=DP.groupby('fin').size().reset_index(); DPc['h']=(DPc.fin%86400)//3600; DPc['dia']=DPc.fin//86400
dpavg=DPc.groupby('h').size()/DPc.dia.nunique()
ph=np.array([min(1.0,nBh[h]/(cov[h]*dpavg.get(h,np.nan))) if cov[h]>0 and dpavg.get(h,0)>0 else 0.0 for h in range(24)])
out['perfil_horario_p']=ph.round(3).tolist()
# estructura DP: dia -> hora -> lista de cierres (unidades)
DP['h']=(DP.fin%86400)//3600; DP['dday']=DP.fin//86400
pool={}
for (dd,fin),g in DP.groupby(['dday','fin']): pool.setdefault(dd,{}).setdefault(int((fin%86400)//3600),[]).append((int(fin%86400),tuple(g.coste.values),tuple(g.pnl.values)))
days_src=sorted(pool)
def pseudoB(srcday,ndays):
    f=[]
    for k in range(ndays):
        dd=srcday if srcday is not None else days_src[rng.integers(len(days_src))]
        for h in range(24):
            if h not in pool[dd] or ph[h]==0: continue
            for (sec,cs,ps) in pool[dd][h]:
                if rng.random()<ph[h]:
                    m=min(len(cs),1+rng.poisson(0.8)); ix=rng.choice(len(cs),m,replace=False)
                    f.append((k*86400+sec,k,tuple(cs[i] for i in ix),tuple(ps[i] for i in ix)))
    return f
resP={}
for nm,Ei,Hh,nd,ntr in (('S_free',60.0,12.0,30,300),('S_real',19.59,12.0,10,300),('S_H0_POSTHOC',19.59,0.0,10,300)):
    rows=[]
    for sd in days_src:
        for j in range(ntr):
            fl=pseudoB(sd,nd); fp=permute_within_day(fl)
            a=runall(fl,Ei,Hh); b=runall(fp,Ei,Hh)
            for k in REGLAS: rows.append((sd,j,k,a[k]['pnl'],a[k]['cost'],a[k]['dd'],int(a[k]['halted']),b[k]['pnl'],b[k]['cost'],a['R0']['pnl'],b['R0']['pnl'],a['R0']['cost']))
        print('E-P',nm,sd,round(time.time()-t0),flush=True)
    resP[nm]=pd.DataFrame(rows,columns=['src','j','regla','pnl','cost','dd','halt','pnl_perm','cost_perm','pnl_R0','pnl_perm_R0','cost_R0'])
    resP[nm].to_pickle(O+f'EP_{nm}.pkl')
tabP={}
for nm,df in resP.items():
    tab={}
    for k in REGLAS:
        x=df[df.regla==k]; d=x.pnl-x.pnl_R0; dpm=x.pnl_perm-x.pnl_perm_R0; est=d-dpm
        pd_=pd.DataFrame(dict(src=x.src,d=d,est=est,ev=x.pnl/x.cost.replace(0,np.nan),cost=x.cost,pnl=x.pnl,costR0=x.cost_R0,pnlR0=x.pnl_R0)).groupby('src')
        m=pd_.mean(numeric_only=True)
        def ic(v):
            mu=v.mean(); se=v.std(ddof=1)/np.sqrt(len(v)); t=st.t.ppf(.95,len(v)-1); return [float(mu-t*se),float(mu+t*se)]
        tt=st.ttest_1samp(m.est,0) if k!='R0' else None
        evk=(x.groupby('src').pnl.sum()/x.groupby('src').cost.sum()); ev0=(x.groupby('src').pnl_R0.sum()/x.groupby('src').cost_R0.sum())
        tab[k]=dict(pnl=float(x.pnl.mean()),cost=float(x.cost.mean()),EV=float(x.pnl.sum()/x.cost.sum()),dd=float(x.dd.mean()),halt=float(x.halt.mean()),
          d_mean=float(d.mean()),d_ic90_dias=ic(m.d),dias_pos=int((m.d>0).sum()),d_est=float(est.mean()),d_est_ic90_dias=ic(m.est),
          p_placebo_dias=float(tt.pvalue) if tt is not None else None,dEV=float((evk-ev0).mean()),d_se_traj=float(d.std(ddof=1)/np.sqrt(len(d))))
    tabP[nm]=tab
out['E-P']=tabP; print('E-P listo',round(time.time()-t0),flush=True)
# ---------- E-S sintetico (estructura = DB repetida 3 veces, resultados Bernoulli con copula)
from scipy.stats import norm
Bg=[(int(f),g) for f,g in DB.groupby('fin')]
cids=[]; 
def synth(e,rho=.333,reps=3):
    f=[]; 
    for r in range(reps):
        for fin,g in Bg:
            p=np.clip(g.precio_medio.values*(1+e),.01,.99); zc=rng.standard_normal(); z=np.sqrt(rho)*zc+np.sqrt(1-rho)*rng.standard_normal(len(g))
            w=(z<norm.ppf(p)); cs=g.coste.values; ps=np.where(w,g.acciones.values-cs,-cs)
            f.append((int(fin)-int(DB.fin.min())+r*4*86400,int((fin-int(DB.fin.min()))//86400)+r*4,tuple(cs),tuple(ps)))
    return f
resS={}
for e in (-0.10,-0.05,0.0,0.05,0.10):
    rows=[]
    for j in range(1500):
        a=runall(synth(e),40.0)
        for k in REGLAS: rows.append((k,a[k]['pnl'],a[k]['cost'],a[k]['dd'],a['R0']['pnl'],a['R0']['cost'],a[k]['takes']))
    df=pd.DataFrame(rows,columns=['regla','pnl','cost','dd','pnl_R0','cost_R0','takes']); tab={}
    for k in REGLAS:
        x=df[df.regla==k]; d=x.pnl-x.pnl_R0; dc=x.cost-x.cost_R0
        tab[k]=dict(pnl=float(x.pnl.mean()),d=float(d.mean()),d_se=float(d.std(ddof=1)/np.sqrt(len(d))),dcost=float(dc.mean()),wald_ratio=float(d.mean()/dc.mean()) if abs(dc.mean())>1e-6 else None,
                    dd=float(x.dd.mean()),EV=float(x.pnl.sum()/x.cost.sum()),pnlsd=float(x.pnl.std()))
    resS[str(e)]=tab; print('E-S',e,round(time.time()-t0),flush=True)
out['E-S']=resS
json.dump(out,open(O+'parteB.json','w'),indent=1,default=float); print('fin',round(time.time()-t0))
