import pandas as pd, numpy as np, json
rng=np.random.default_rng(7)
J=pd.read_pickle('J.pkl'); B='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'
SV=set(open(B+'as_tomador/contrafactual/datos/set_V.txt').read().split()); SI=set(open(B+'as_tomador/contrafactual/datos/set_I.txt').read().split())
J['taker']=J.taker.str.lower(); SV={s.lower() for s in SV}; SI={s.lower() for s in SI}
A=pd.read_csv(B+'anatomia/pos_anotado2.csv')
acols=['cola_post','spread_post','bidsz_post','dist_ref_bps','vol60_bps','bn_pre30','btc_pre30','n_ordenes','tras_cancel','t_desde_open','fv_gap']
A=A.rename(columns={'slug':'mercado'})[['mercado','outcome']+acols]
for c in ['tras_cancel']: A[c]=A[c].astype(str).map({'True':1,'False':0})
J=J.merge(A,on=['mercado','outcome'],how='left')
J['hora']=pd.to_datetime(J.fecha_utc).dt.hour; J['parcial']=(J.acc_llena<J.acc-1e-9).astype(int)
J['fV']=J.taker.isin(SV); J['fI']=J.taker.isin(SI); J['fR0']=J.h_w1==1
TR=J.dia.isin(['2026-10-20','2026-10-21']); TE=~TR
def ev(d): return d.pnl.sum()/d.coste.sum()
def exc(d,f):
    k=d[~f]; return (ev(k)-ev(d)) if len(k) else np.nan
def placebo(d,f,n=5000):
    obs=exc(d,f); fv=f.values; days=d.dia.values; out=np.empty(n)
    idx=[np.where(days==x)[0] for x in np.unique(days)]
    for i in range(n):
        g=fv.copy()
        for ix in idx: g[ix]=rng.permutation(fv[ix])
        out[i]=exc(d,pd.Series(g,index=d.index))
    return obs,(out>=obs).mean(),out.std()
def boot(d,f,n=2000,a=0.05):
    cl=d.fin.unique(); g={c:np.where(d.fin.values==c)[0] for c in cl}; r=[]
    for i in range(n):
        s=np.concatenate([g[c] for c in rng.choice(cl,len(cl))]); dd=d.iloc[s]; ff=f.iloc[s]
        if (~ff).sum()==0 or ff.sum()==0: continue
        r.append(exc(dd.reset_index(drop=True),ff.reset_index(drop=True)))
    return np.nanquantile(r,[a,1-a])
def sin2(d,f):
    dp=d[f].groupby('dia').pnl.sum().reindex(d.dia.unique()).fillna(0)  # dPnL=-pnl flagged
    best=(-dp).sort_values().index[-2:]; k=~d.dia.isin(best); return exc(d[k],f[k])
def rep(name,d,f):
    o,p,se=placebo(d,f); 
    return dict(regla=name,n=len(d),n_flag=int(f.sum()),cier_flag=int(d[f].fin.nunique()),ret=round(1-d[f].coste.sum()/d.coste.sum(),3),
      EVf=round(ev(d[f]),3) if f.sum() else None,EVk=round(ev(d[~f]),3),EXC=round(o,4),dPnL=round(-d[f].pnl.sum(),2),p=round(p,4),se=round(se,4))
OUT={}
print('EV total',round(ev(J),4),'TRAIN',round(ev(J[TR]),4),'TEST',round(ev(J[TE]),4),'cierres',J.fin.nunique(),J[TR].fin.nunique(),J[TE].fin.nunique())
# Familia P: evaluada en TEST y en todo
P=[]
for nm,c in [('P1_SET_V','fV'),('P2_SET_I_contam','fI'),('P3_R0','fR0')]:
    for lab,m in [('TEST',TE),('TODO',J.index==J.index)]:
        d=J[m].reset_index(drop=True); f=d[c].astype(bool); r=rep(nm+'_'+lab,d,f)
        if lab=='TODO': r['sin2']=round(sin2(d,f),4)
        P.append(r)
print(pd.DataFrame(P).to_string())
# Familia L
base=['precio','T_s','edad','rpre_bps','abs_rpre','r900_bps','bn_edad_max_s','acc','hora','parcial','coste']
cat=['coin']; feats=base+acols+cat
L=[]
Jtr=J[TR].reset_index(drop=True); Jte=J[TE].reset_index(drop=True)
def cands(d,x):
    if x in cat: return [(x,'==',v) for v in d[x].dropna().unique()]
    q=d[x].dropna().quantile([1/3,2/3]).values; return [(x,'<=',q[0]),(x,'>',q[1])]
def flag(d,c):
    x,op,v=c; s=d[x]
    return (s==v) if op=='==' else ((s<=v) if op=='<=' else (s>v))
for x in feats:
    if Jtr[x].notna().sum()<30: continue
    best=None
    for c in cands(Jtr,x):
        f=flag(Jtr,c).fillna(False).astype(bool)
        if f.sum()==0 or Jtr[f].coste.sum()<0.15*Jtr.coste.sum(): continue
        e=ev(Jtr[f])
        if best is None or e<best[1]: best=(c,e)
    if best is None: continue
    dte=Jte[Jte[x].notna()].reset_index(drop=True) if x in acols else Jte
    f=flag(dte,best[0]).fillna(False).astype(bool)
    r=rep('L_'+x,dte,f); r['corte']=str(best[0][1])+str(round(best[0][2],3) if not isinstance(best[0][2],str) else best[0][2]); r['EVf_train']=round(best[1],3)
    L.append(r)
# arbol prof 2 sobre base
def bestsplit(d,fs):
    b=None
    for x in fs:
        for c in cands(d,x):
            f=flag(d,c).fillna(False).astype(bool)
            if f.sum()<15 or (~f).sum()<15: continue
            for side in [f,~f]:
                e=ev(d[side]); 
                if b is None or e<b[1]: b=((c,side is f),e)
    return b
b1=bestsplit(Jtr,base+cat); (c1,s1),e1=b1; f1=flag(Jtr,c1).fillna(False).astype(bool); f1=f1 if s1 else ~f1
b2=bestsplit(Jtr[f1].reset_index(drop=True),base+cat); (c2,s2),e2=b2
def tflag(d):
    a=flag(d,c1).fillna(False).astype(bool); a=a if s1 else ~a
    b=flag(d,c2).fillna(False).astype(bool); b=b if s2 else ~b
    return a&b
r=rep('L_arbol2',Jte,tflag(Jte)); r['corte']=f'{c1}{s1}&{c2}{s2}'; r['EVf_train']=round(ev(Jtr[tflag(Jtr)]),3); L.append(r)
Ld=pd.DataFrame(L); K=3+len(Ld); al=0.10/K
print('K_total',K,'alfa_Bonf',round(al,4)); print(Ld.to_string())
# BH sobre p de TEST (familia P TEST + L)
ps=pd.concat([pd.DataFrame(P)[lambda d:d.regla.str.endswith('TEST')][['regla','p']],Ld[['regla','p']]]).sort_values('p').reset_index(drop=True)
ps['bh']=[0.10*(i+1)/K for i in range(len(ps))]; ps['pasa_bh']=ps.p<=ps.bh
print(ps.head(8).to_string())
# candidatos con p<=0.10 en TEST: IC por cierre y sin2
for nm in ps[ps.p<=0.10].regla:
    print('detalle',nm)
J.to_pickle('J2.pkl'); Ld.to_csv('L.csv',index=False); pd.DataFrame(P).to_csv('P.csv',index=False)
