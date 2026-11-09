#!/usr/bin/env python3
"""s8: Q1 poblacional (clusters de tomadores en la banda de B) + Q2 miner automatizado (rasgos e interacciones) + residuos.
DISC 20-29 Oct (grupos y ajuste), HOLD 30 Oct-08 Nov (medida). Ambos periodos son EXPLORATORIOS (26-Oct..06-Nov quemados para Q11);
confirmacion solo en forward desde 10-Nov con prerregistro. Unidad = orden tomadora que rellena bids de banda (agrega makers); EV del lado
maker ponderado por EUR (sum pnl / sum coste), IC90 bootstrap por DIA y por CIERRE. Multiplicidad: BH-FDR sobre (rasgo x cluster)."""
import json, glob, numpy as np, pandas as pd
pd.set_option('future.infer_string', False)
from scipy.stats import mannwhitneyu
from sklearn.ensemble import HistGradientBoostingClassifier as HGB
from sklearn.metrics import roc_auc_score, log_loss
DD='/root/polymarket-research/experimentos/5m_barato/diseccion_bots_b_09nov/datos/'
rng=np.random.default_rng(11)
DROP=['tx','taker','mkt','L','tL','bloque','ts','tau_rel','tpc','tacc_u','tventa_u','nmk_u','acc_u','coin']
def rd(f):
    X=pd.read_parquet(f); X=X.drop(columns=[k for k in DROP if k in X.columns]); fl=X.select_dtypes('float64').columns.difference(['tau_rel','tau_abs','ts','pnl_mk','c','pc_u','y_loss','acc_u'])
    X[fl]=X[fl].astype(np.float32); return X
F=pd.concat([rd(f) for f in sorted(glob.glob(DD+'feat_2026-*.parquet'))],ignore_index=True)
meta=['tw','cierre','pc_u','c','esB','y_loss','pnl_mk','dia','tau_abs']
feats=[k for k in F.columns if k not in meta]
for k in feats: F[k]=F[k].astype(np.float32)
F=F[F.y_loss.notna()].reset_index(drop=True)
WC=json.load(open(DD+'wallet_cluster.json'))['wallet_cluster']
F['cl']=F.tw.map(WC).fillna('C_nuevo')
F['per']=np.where(F.dia<='2026-10-29','DISC','HOLD'); F['cierre_id']=F.cierre.astype(int)
F['exc']=F.y_loss-(1-F.pc_u)
print('unidades',len(F),'dias',F.dia.nunique(),'DISC',int((F.per=='DISC').sum()),'HOLD',int((F.per=='HOLD').sum()),'B',int(F.esB.sum()))
def ev(S): return S.pnl_mk.sum()/S.c.sum()
def ic(S,by,B=1000):
    g=S.groupby(by).agg(p=('pnl_mk','sum'),c=('c','sum')); p=g.p.values; c=g.c.values
    if len(g)<3: return (np.nan,np.nan)
    i=rng.integers(0,len(g),(B,len(g))); r=p[i].sum(1)/c[i].sum(1); return tuple(np.round(np.quantile(r,[.05,.95]),3))
def sin2(S):
    g=S.groupby('dia').agg(p=('pnl_mk','sum'),c=('c','sum')); g=g.sort_values('p'); g=g.iloc[:-2] if len(g)>2 else g; return g.p.sum()/g.c.sum()
# ---------------- A. tabla de clusters
rows=[]
for cl,S in F.groupby('cl'):
    r={'cluster':cl,'wallets':S.tw.nunique(),'n':len(S),'pct_eur':S.c.sum()/F.c.sum()}
    for per in ('DISC','HOLD'):
        X=S[S.per==per]
        if len(X)<30: r.update({f'EV_{per}':np.nan}); continue
        r[f'n_{per}']=len(X); r[f'EV_{per}']=round(ev(X),4); r[f'IC90dia_{per}']=ic(X,'dia'); r[f'IC90cierre_{per}']=ic(X,'cierre_id'); r[f'sin2_{per}']=round(sin2(X),4)
        r[f'exc_{per}']=round(X.exc.mean(),4)
        tw=X.groupby('tw').c.sum().sort_values(ascending=False); r[f'top1w_{per}']=round(tw.iloc[0]/tw.sum(),3)
    B=S[S.esB]; r['B_n']=len(B); r['B_perd']=int(B.y_loss.sum()); r['B_EV']=round(ev(B),3) if len(B) else np.nan
    rows.append(r)
TA=pd.DataFrame(rows).sort_values('pct_eur',ascending=False); TA.to_csv(DD+'s8_tabla_clusters.csv',index=False)
pd.set_option('display.width',250); print(TA.to_string(index=False))
print('EV total DISC',round(ev(F[F.per=='DISC']),4),ic(F[F.per=='DISC'],'dia'),'HOLD',round(ev(F[F.per=='HOLD']),4),ic(F[F.per=='HOLD'],'dia'))
# placebo de etiquetas de cluster (permuta wallets entre clusters, mismo tamano): dispersion de EV entre clusters en HOLD
def disp(lab,S):
    g=S.assign(l=lab).groupby('l').agg(p=('pnl_mk','sum'),c=('c','sum')); g=g[g.c>=50]; e=g.p/g.c; return float((e.max()-e.min()))
H=F[F.per=='HOLD']; obs=disp(H.cl.values,H)
ws=H.tw.unique(); wl=pd.Series(H.groupby('tw').cl.first()); null=[]
for _ in range(300 if not __import__('os').environ.get('SKIP_A') else 0):
    perm=dict(zip(wl.index,rng.permutation(wl.values))); null.append(disp(H.tw.map(perm).values,H))
if null: print('placebo dispersion EV entre clusters HOLD: obs %.3f null p50 %.3f p95 %.3f p=%.3f'%(obs,np.median(null),np.quantile(null,.95),np.mean(np.array(null)>=obs)))
# persistencia DISC->HOLD del EV por cluster
m=TA.dropna(subset=['EV_DISC','EV_HOLD']); m=m[m.cluster!='C_nuevo']
print('signo EV cluster DISC vs HOLD coincide:',int((np.sign(m.EV_DISC)==np.sign(m.EV_HOLD)).sum()),'/',len(m))
# ---------------- B. ¿observables o identidad? (HGB DISC -> HOLD)
D_=F[F.per=='DISC'].sample(min(110000,int((F.per=='DISC').sum())),random_state=3); H_=F[F.per=='HOLD'].sample(min(100000,int((F.per=='HOLD').sum())),random_state=1)
CLS=sorted(F.cl.unique())
import gc; del F; gc.collect()
print('submuestras D_',len(D_),'H_',len(H_),flush=True)
Dtr=D_.sample(min(80000,len(D_)),random_state=0)
feats=[k for k in feats if Dtr[k].nunique()>2 and H_[k].nunique()>2]; print('rasgos usables',len(feats))
def fit(cols,X,y,depth=None,it=200,cat=None):
    m=HGB(max_iter=it,learning_rate=0.06,max_depth=depth,max_leaf_nodes=31 if depth is None else None,early_stopping=True,validation_fraction=0.15,random_state=0,categorical_features=cat)
    return m.fit(X[cols].values,y)
lg=lambda p: np.log(np.clip(p,1e-4,1-1e-4)/(1-np.clip(p,1e-4,1-1e-4)))
Dtr=Dtr.assign(lpc=lg(1-Dtr.pc_u)); H_=H_.assign(lpc=lg(1-H_.pc_u))
yD=Dtr.y_loss.values.astype(int); yH=H_.y_loss.values.astype(int)
res={}
m0=fit(['lpc'],Dtr,yD); p0=m0.predict_proba(H_[['lpc']].values)[:,1]
m1=fit(feats,Dtr,yD); p1=m1.predict_proba(H_[feats].values)[:,1]
ma=fit(feats,Dtr,yD,depth=1,it=500); pa=ma.predict_proba(H_[feats].values)[:,1]   # aditivo (sin interacciones)
cls=CLS; ci={c:i for i,c in enumerate(cls)}
Dtr=Dtr.assign(clc=Dtr.cl.map(ci).astype(float)); H_=H_.assign(clc=H_.cl.map(ci).astype(float))
m2=fit(feats+['clc'],Dtr,yD,cat=[False]*len(feats)+[True]); p2=m2.predict_proba(H_[feats+['clc']].values)[:,1]
m3=fit(['lpc','clc'],Dtr,yD,cat=[False,True]); p3=m3.predict_proba(H_[['lpc','clc']].values)[:,1]
def daybs(p,y,dias,B=500):
    u=np.unique(dias); idx={d:np.where(dias==d)[0] for d in u}; out=[]
    for _ in range(B):
        s=np.concatenate([idx[d] for d in rng.choice(u,len(u))]); out.append(roc_auc_score(y[s],p[s]))
    return tuple(np.round(np.quantile(out,[.05,.95]),3))
dH=H_.dia.values
for nm,p in (('M0 precio',p0),('M1 rasgos',p1),('M1a aditivo',pa),('M2 rasgos+cluster',p2),('M3 precio+cluster',p3)):
    print('%-18s HOLD AUC %.4f IC90dia %s logloss %.5f'%(nm,roc_auc_score(yH,p),daybs(p,yH,dH),log_loss(yH,np.clip(p,1e-4,1-1e-4))))
# EV del maker por decil de riesgo predicho (M1, exceso sobre precio) en HOLD
H_=H_.assign(sc=p1-p0); H_['dec']=pd.qcut(H_.sc.rank(method='first'),10,labels=False)
print('HOLD EV maker por decil de exceso predicho M1 (0=menos riesgo):')
print(H_.groupby('dec').apply(lambda S: pd.Series({'n':len(S),'EV':ev(S),'exc':S.exc.mean(),'B_n':int(S.esB.sum())}),include_groups=False).round(4).to_string())
# placebo del M1: etiquetas barajadas dentro de dia en DISC
yP=Dtr.groupby('dia').y_loss.transform(lambda s: s.sample(frac=1,random_state=1).values).values.astype(int)
mp=fit(feats,Dtr,yP); pp=mp.predict_proba(H_[feats].values)[:,1]; print('placebo M1 HOLD AUC %.4f'%roc_auc_score(yH,pp))
# importancias por permutacion en HOLD (submuestra)
from sklearn.inspection import permutation_importance
Hs=H_.sample(min(40000,len(H_)),random_state=0)
pi=permutation_importance(m1,Hs[feats].values,Hs.y_loss.values.astype(int),scoring='roc_auc',n_repeats=3,random_state=0)
imp=pd.Series(pi.importances_mean,index=feats).sort_values(ascending=False); imp.to_csv(DD+'s8_importancias_M1.csv'); print('top importancias M1 (HOLD, ΔAUC):'); print(imp.head(20).round(4).to_string())
# ---------------- C. disparadores por cluster: ¿que observables preceden la llegada de cada cluster? (univariante + BH-FDR + replica HOLD; HGB DISC->HOLD vs placebo)
top=[c for c in TA.cluster if c not in ('C_nuevo',)][:8]
U=[]
for cl in top:
    yd=(D_.cl==cl).values; yh=(H_.cl==cl).values
    for k in feats:
        a=D_[k].values; b=H_[k].values; ma_=~np.isnan(a); mb=~np.isnan(b)
        if yd[ma_].sum()<100 or (~yd[ma_]).sum()<100 or np.nanstd(a)==0: continue
        aucd=roc_auc_score(yd[ma_],a[ma_]); pd_=mannwhitneyu(a[ma_&yd],a[ma_&~yd]).pvalue
        auch=roc_auc_score(yh[mb],b[mb]) if yh[mb].sum()>=50 else np.nan
        U.append((cl,k,aucd,pd_,auch))
U=pd.DataFrame(U,columns=['cl','rasgo','AUC_DISC','p_DISC','AUC_HOLD'])
p=U.p_DISC.values; o=np.argsort(p); mtests=len(p); thr=np.zeros(mtests); thr[o]=(np.arange(1,mtests+1)/mtests)*0.05
U['BH']=p<=np.max(np.where(np.sort(p)<=(np.arange(1,mtests+1)/mtests)*0.05,np.sort(p),0))
U['replica']=U.BH&(np.sign(U.AUC_DISC-.5)==np.sign(U.AUC_HOLD-.5))&(abs(U.AUC_HOLD-.5)>=0.03)&(abs(U.AUC_DISC-.5)>=0.03)
U.to_csv(DD+'s8_disparadores_univ.csv',index=False)
print('tests',mtests,'BH',int(U.BH.sum()),'replican (|AUC-0,5|>=0,03 ambos, mismo signo)',int(U.replica.sum()))
for cl in top:
    S=U[(U.cl==cl)&U.replica].assign(ef=lambda d:abs(d.AUC_HOLD-.5)).sort_values('ef',ascending=False).head(6)
    print(cl,[(r.rasgo,round(r.AUC_DISC,3),round(r.AUC_HOLD,3)) for r in S.itertuples()])
print('HGB pertenencia a cluster DISC->HOLD (AUC, placebo barajando etiqueta dentro de dia):')
for cl in top:
    yd=(Dtr.cl==cl).values.astype(int); yh=(H_.cl==cl).values.astype(int)
    if yd.sum()<200 or yh.sum()<100: continue
    mc=fit(feats,Dtr,yd,it=200); pc_=mc.predict_proba(H_[feats].values)[:,1]
    ypl=pd.Series(yd).groupby(Dtr.dia.values).transform(lambda s: s.sample(frac=1,random_state=2).values).values
    mpl=fit(feats,Dtr,ypl,it=200); ppl=mpl.predict_proba(H_[feats].values)[:,1]
    # dentro del cluster: ¿los rasgos predicen su exceso de perdida mejor que el precio?
    Sd=Dtr[Dtr.cl==cl]; Sh=H_[H_.cl==cl]; extra=''
    if len(Sd)>=2000 and len(Sh)>=1000:
        mw=fit(feats,Sd,Sd.y_loss.values.astype(int),it=200); mw0=fit(['lpc'],Sd,Sd.y_loss.values.astype(int))
        extra=' | perdida dentro del cluster: AUC rasgos %.3f vs precio %.3f (HOLD n=%d)'%(roc_auc_score(Sh.y_loss,mw.predict_proba(Sh[feats].values)[:,1]),roc_auc_score(Sh.y_loss,mw0.predict_proba(Sh[['lpc']].values)[:,1]),len(Sh))
    print('  %-10s AUC %.3f placebo %.3f base %.3f%s'%(cl,roc_auc_score(yh,pc_),roc_auc_score(yh,ppl),yh.mean(),extra))

