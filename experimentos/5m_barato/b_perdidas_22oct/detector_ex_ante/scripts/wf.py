import pandas as pd, numpy as np, json, sys
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
rng=np.random.default_rng(7)
T=pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl').reset_index(drop=True)
T['y']=T.gana_f.astype(float); T['coin']=T.act.map({'ETH':0,'SOL':1,'XRP':2})
T['lado']=(T.lado_c=='YES').astype(int)
# --- rasgos ex-ante de identidad/flujo (solo rellenos de la propia tabla, banda 0,10-0,30: cobertura parcial declarada)
LAG=4.0; W=60.0
T=T.sort_values(['mkt','ts']).reset_index(drop=True)
npv=np.zeros(len(T)); inf_prev=np.full(len(T),np.nan); same_prev=np.zeros(len(T)); seen=np.zeros(len(T))
for m,ix in T.groupby('mkt').indices.items():
    ts=T.ts.values[ix]; sc=T.tk_score.values[ix]; ld=T.lado.values[ix]; tk=T.taker.values[ix]
    for k,i in enumerate(ix):
        a=np.searchsorted(ts,ts[k]-W,'left'); b=np.searchsorted(ts,ts[k]-LAG,'right')
        if b>a:
            npv[i]=b-a; s=sc[a:b]; s=s[np.isfinite(s)]
            if len(s): inf_prev[i]=s.max()
            same_prev[i]=(ld[a:b]==ld[k]).mean()
# cruzado entre monedas: rellenos de otras monedas mismo cierre en [ts-60,ts-4], fraccion mismo lado
xc_n=np.zeros(len(T)); xc_same=np.full(len(T),np.nan)
for c,ix in T.groupby('cierre').indices.items():
    o=ix[np.argsort(T.ts.values[ix])]; ts=T.ts.values[o]; co=T.coin.values[o]; ld=T.lado.values[o]
    for k,i in enumerate(o):
        a=np.searchsorted(ts,ts[k]-W,'left'); b=np.searchsorted(ts,ts[k]-LAG,'right')
        msk=co[a:b]!=co[k]
        if msk.any(): xc_n[i]=msk.sum(); xc_same[i]=(ld[a:b][msk]==ld[k]).mean()
T['n_prev60']=npv; T['inf_prev60']=inf_prev; T['same_prev60']=same_prev; T['xc_n60']=xc_n; T['xc_same60']=xc_same
FWD=['pc','T','coin','hora','lado','vol30','bb','ba','bs','as_','spread','depth_ticks','b15','a15','lvl15','gap15','d15_30','dbb30','vol30ws','r60f','rpre_s','CON','imb','qage','q15age']
FULL=FWD+['gap_last','dp5','dp30','dp60','hi60','rng60','d_open','vol_all','flow60','fv_gap','z','sig_bps_s','b10']
IDX=FULL+['n_prev60','inf_prev60','same_prev60','xc_n60','xc_same60']
ORA=IDX+['tk_score']   # identidad del tomador EN el relleno: no es ex-ante (diagnostico de techo)
MODELS={'M0_precio':None,'M1_FWD':FWD,'M2_FULL':FULL,'M3_FULL+flujoID':IDX,'M4_oraculoID':ORA,'M5_soloID':['pc','coin','tk_score']}
T.to_pickle('T_det.pkl')
days=sorted(T.dia.unique()); test_days=[d for d in days if '2026-10-12'<=d<='2026-10-20']
def sauc(y,s,strat):
    num=0;den=0
    df=pd.DataFrame({'y':y,'s':s,'g':strat})
    for g,d in df.groupby('g'):
        n1=d.y.sum(); n0=len(d)-n1
        if n1>0 and n0>0:
            num+=roc_auc_score(d.y,d.s)*n1*n0; den+=n1*n0
    return num/den
out=[]
for d in test_days:
    tr=T[T.dia<d]; te=T[T.dia==d].copy()
    strat=te.coin.astype(str)+'_'+(te.pc*100).round().astype(int).astype(str)
    for name,feats in MODELS.items():
        if feats is None:
            X=np.c_[np.log(tr.pc/(1-tr.pc)),np.eye(3)[tr.coin]]; Xt=np.c_[np.log(te.pc/(1-te.pc)),np.eye(3)[te.coin]]
            mdl=LogisticRegression(C=1.0,max_iter=500).fit(X,tr.y); q=mdl.predict_proba(Xt)[:,1]; qtr=mdl.predict_proba(X)[:,1]
        else:
            mdl=HistGradientBoostingClassifier(max_depth=3,max_iter=200,learning_rate=0.05,min_samples_leaf=300,l2_regularization=1.0,random_state=0)
            mdl.fit(tr[feats],tr.y); q=mdl.predict_proba(te[feats])[:,1]; qtr=mdl.predict_proba(tr[feats])[:,1]
        ev=q/te.pc.values-1; evtr=qtr/tr.pc.values-1
        ll=-np.mean(te.y*np.log(np.clip(q,1e-6,1))+(1-te.y)*np.log(np.clip(1-q,1e-6,1)))
        llp=-np.mean(te.y*np.log(te.pc)+(1-te.y)*np.log(1-te.pc))
        r={'dia':d,'m':name,'n':len(te),'auc_strat':sauc(te.y.values,q,strat.values),'dll_vs_pc':ll-llp}
        for phi in (0.10,0.25):
            # corte por cuantil de EUR en TRAIN (desplegable)
            o=np.argsort(evtr); cw=np.cumsum(tr.c.values[o])/tr.c.sum(); cut=evtr[o][np.searchsorted(cw,phi)]
            sk=ev<=cut; skI=ev>=np.quantile(evtr,1-phi)
            P=te.pnl.values; C=te.c.values
            f=C[sk].sum()/C.sum()
            r[f'f{phi}']=f; r[f'dP{phi}']=-P[sk].sum(); r[f'plac{phi}']=-f*P.sum(); r[f'dPinv{phi}']=-P[skI].sum()
            r[f'EVret{phi}']=P[~sk].sum()/C[~sk].sum(); r[f'EVall']=P.sum()/C.sum(); r[f'EVskip{phi}']=P[sk].sum()/max(C[sk].sum(),1e-9)
            # placebo permutacion (Bernoulli f) 500
            pl=np.array([-P[rng.random(len(P))<f].sum() for _ in range(500)])
            r[f'pperm{phi}']=float((pl>=r[f'dP{phi}']).mean())
        out.append(r); print(d,name,round(r['auc_strat'],4),round(r['dll_vs_pc'],5),round(r['dP0.25'],1),round(r['plac0.25'],1),flush=True)
R=pd.DataFrame(out); R.to_csv('wf_res.csv',index=False)
