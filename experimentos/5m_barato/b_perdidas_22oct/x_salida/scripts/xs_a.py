# PARTE A: estructura de los incrementos por CIERRE. Permutacion intra-dia. semilla 20261023
import pandas as pd, numpy as np, pickle, json, sys, time
O='/root/polymarket-research-datalogs/x_salida/'
S=pickle.load(open(O+'datasets.pkl','rb'))
rng=np.random.default_rng(20261023)
def cierres(df,dia_fn):
    g=df.groupby('fin').agg(x=('pnl','sum'),c=('coste','sum'),n=('pnl','size')).reset_index().sort_values('fin')
    g['dia']=g.fin//86400; g['blk']=((g.fin%86400)//14400).astype(int)
    return g
def pad(g,cols):
    days=g.dia.values; u,inv=np.unique(days,return_inverse=True)
    cnt=np.bincount(inv); L=cnt.max(); D=len(u)
    pos=np.arange(len(g))-np.repeat(np.cumsum(cnt)-cnt,cnt)
    out={}
    for k in cols:
        a=np.zeros((D,L)); a[inv,pos]=g[k].values; out[k]=a
    V=np.zeros((D,L),bool); V[inv,pos]=True
    return out,V
def stats(X,C,B,V,sig):
    Xv=X[V]; m=Xv.mean(); Z=(X-m)*V; den=(Z**2).sum()
    r1=(Z[:,:-1]*Z[:,1:]).sum()/den
    r2=(Z[:,:-2]*Z[:,2:]).sum()/den if X.shape[1]>2 else 0
    r3=(Z[:,:-3]*Z[:,3:]).sum()/den if X.shape[1]>3 else 0
    Xm=X*V; Cm=np.cumsum(Xm,1); P=Cm-Xm
    Pv=P[V]; Pm=Pv.mean(); b=((Xv-m)*(Pv-Pm)).sum()/((Pv-Pm)**2).sum()
    hi=V&(P>=sig); lo=V&(P<=-sig)
    dif=(X[hi].mean() if hi.sum()>5 else np.nan)-(X[lo].mean() if lo.sum()>5 else np.nan)
    M=np.maximum.accumulate(Cm,1); cond=(Cm<=M-2*sig)&(M>=2*sig)&V
    nx=X[:,1:]; cm=cond[:,:-1]&V[:,1:]; rest=V[:,1:]&~cond[:,:-1]
    s3=(nx[cm].mean()-nx[rest].mean()) if cm.sum()>=5 else 0.0
    vr={}
    for h in (2,4,8,16):
        if X.shape[1]>h:
            W=Cm[:,h:]-Cm[:,:-h]; mk=V[:,h:]
            vr[h]=((W[mk]-h*m)**2).mean()/(h*(Z[V]**2).mean()) if mk.sum()>10 else np.nan
    # S5
    bl=B[V].astype(int); cb=np.bincount(bl,weights=C[V],minlength=6); xb=np.bincount(bl,weights=Xv,minlength=6)
    evg=Xv.sum()/C[V].sum(); evb=np.where(cb>0,xb/np.where(cb>0,cb,1),evg)
    s5=np.max(np.abs(evb-evg)*(cb>0))
    return dict(S1=r1,S2=b,S3=s3,S4=vr.get(8,np.nan),S5=s5,r2=r2,r3=r3,dif=dif,n_hi=int(hi.sum()),n_lo=int(lo.sum()),n_S3=int(cm.sum()),VR=vr,evb=evb,cb=cb)
def perm_arrays(X,C,V):
    k=rng.random(X.shape); k[~V]=np.inf; idx=np.argsort(k,axis=1)
    return np.take_along_axis(X,idx,1),np.take_along_axis(C,idx,1)
def testear(g,nperm,B=True):
    a,V=pad(g,['x','c','blk']); X,C,Bk=a['x'],a['c'],a['blk']
    sig=X[V].std()
    obs=stats(X,C,Bk,V,sig)
    keys=['S1','S2','S3','S4','S5']; dist={k:[] for k in keys}; dd=[]
    for _ in range(nperm):
        Xp,Cp=perm_arrays(X,C,V); s=stats(Xp,Cp,Bk,V,sig)
        for k in keys: dist[k].append(s[k])
        dd.append(s['dif'])
    res={'n_cierres':int(V.sum()),'n_dias':int(V.shape[0]),'sigma_cierre':float(sig),'MDE_lag1':float(2.8/np.sqrt(V.sum())),
         'EV_pond':float(X[V].sum()/C[V].sum()),'obs':{k:float(obs[k]) for k in keys+['r2','r3','dif']},'n_hi_lo_S3':[obs['n_hi'],obs['n_lo'],obs['n_S3']],
         'VR':{str(k):float(v) for k,v in obs['VR'].items()},'evb':[float(v) for v in obs['evb']],'cb':[float(v) for v in obs['cb']],'p':{},'nperm':nperm}
    for k in keys:
        d=np.array(dist[k]); mu=d.mean()
        if k=='S5': p=(1+(d>=obs[k]).sum())/(nperm+1)
        else: p=(1+(np.abs(d-mu)>=abs(obs[k]-mu)).sum())/(nperm+1)
        res['p'][k]=float(p); res.setdefault('nullmean',{})[k]=float(mu); res.setdefault('nullsd',{})[k]=float(d.std())
    return res
def sinteticos(df,pcol,rho=0.333,e=0.0):
    # resultados Bernoulli con p=precio*(1+e), copula gaussiana intra-cierre; pnl = acc*win - coste
    from scipy.stats import norm
    d=df.copy(); p=np.clip(d[pcol].values*(1+e),0.01,0.99)
    cid=pd.factorize(d.fin)[0]; zc=rng.standard_normal(cid.max()+1)[cid]
    z=np.sqrt(rho)*zc+np.sqrt(1-rho)*rng.standard_normal(len(d))
    win=(z<norm.ppf(p)).astype(float); d['pnl']=d.acc*win-d.coste; return d
if __name__=='__main__':
    t0=time.time(); out={}
    DB=S['DB'].copy(); DP=S['DP'].copy(); DL=S['DL'].copy()
    for nm,df,npm in (('DB',DB,5000),('DP',DP,5000),('DL',DL,2000)):
        g=cierres(df,None); out[nm]=testear(g,npm); print(nm,out[nm]['n_cierres'],out[nm]['obs'],out[nm]['p'],round(time.time()-t0),flush=True)
    # S6 nivel diario (DL)
    g=cierres(DL,None); dd=g.groupby('dia').agg(x=('x','sum'),c=('c','sum'),n=('n','size')); dd=dd[dd.n>=40]; ev=(dd.x/dd.c).values
    r1=np.corrcoef(ev[:-1],ev[1:])[0,1]; vm=ev.var()
    nul=[];nulv=[]
    gx=g.x.values; gc=g.c.values; dayid=pd.factorize(g.dia)[0]
    for _ in range(1000):
        pm=rng.permutation(len(g)); xs=gx[pm]; cs=gc[pm]
        sx=np.bincount(dayid,weights=xs); sc=np.bincount(dayid,weights=cs); n=np.bincount(dayid); k=n>=40
        e=(sx[k]/sc[k]); nul.append(np.corrcoef(e[:-1],e[1:])[0,1]); nulv.append(e.var())
    nul=np.array(nul); nulv=np.array(nulv)
    out['S6']={'n_dias':int(len(ev)),'lag1_EVdia':float(r1),'p_lag1':float((1+(np.abs(nul-nul.mean())>=abs(r1-nul.mean())).sum())/1001),
               'razon_var':float(vm/nulv.mean()),'p_var':float((1+(nulv>=vm).sum())/1001),'EV_dia_sd':float(np.sqrt(vm)),'null_sd':float(np.sqrt(nulv.mean()))}
    print('S6',out['S6'],flush=True)
    # calibracion con desenlaces sinteticos (DB, DP) e=0
    cal={}
    for nm,df,pc,reps,npm in (('DB',DB.assign(acc=DB.acciones),'precio_medio',150,300),('DP',DP.assign(precio=DP.coste/DP.acc),'precio',150,300)):
        fp=np.zeros(5); keys=['S1','S2','S3','S4','S5']
        for r in range(reps):
            d=sinteticos(df,pc); res=testear(cierres(d,None),npm)
            fp+=np.array([res['p'][k]<0.05 for k in keys])
        cal[nm]={'reps':reps,'nperm':npm,'FP_5pct':dict(zip(keys,(fp/reps).round(3).tolist()))}; print('cal',nm,cal[nm],round(time.time()-t0),flush=True)
    out['calibracion_sintetica']=cal
    json.dump(out,open(O+'parteA.json','w'),indent=1); print('fin',round(time.time()-t0))
