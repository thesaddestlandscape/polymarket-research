import pandas as pd, numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
T=pd.read_pickle('T_det.pkl')
T['depth_ticks']=(T.bb-T.pc)/0.01; T['gap15']=T.b15-T.bb
M1F=['pc','T','coin','hora','lado','vol30','bb','ba','bs','spread','depth_ticks','b15','a15','lvl15','gap15','vol30ws','r60f','rpre_s','CON']
FWD=['pc','T','coin','hora','lado','vol30','bb','ba','bs','as_','spread','depth_ticks','b15','a15','lvl15','gap15','d15_30','dbb30','vol30ws','r60f','rpre_s','CON','imb','qage','q15age']
FULL=FWD+['gap_last','dp5','dp30','dp60','hi60','rng60','d_open','vol_all','flow60','fv_gap','z','sig_bps_s','b10']
print('corr z vs rpre_s', np.corrcoef(T.z.fillna(0),T.rpre_s.fillna(0))[0,1], ' z*sg vs rpre_s', np.corrcoef((T.z*T.sg).fillna(0),T.rpre_s.fillna(0))[0,1])
days=sorted(T.dia.unique()); test=[d for d in days if '2026-10-12'<=d<='2026-10-20']
H=lambda: HistGradientBoostingClassifier(max_depth=3,max_iter=200,learning_rate=0.05,min_samples_leaf=300,l2_regularization=1.0,random_state=0)
parts=[]
for d in test:
    tr=T[T.dia<d]; te=T[T.dia==d].copy()
    # R1 proxy: tercil bajo de sig_bps_s con cortes del TRAIN por moneda
    te['R1p']=False
    for c in (0,1,2):
        cut=np.nanquantile(tr.sig_bps_s[tr.coin==c],1/3); te.loc[te.coin==c,'R1p']=te.sig_bps_s[te.coin==c]<=cut
    for nm,f in (('M1F',M1F),('M2',FULL)):
        m=H().fit(tr[f],tr.y); ev=m.predict_proba(te[f])[:,1]/te.pc.values-1; evtr=m.predict_proba(tr[f])[:,1]/tr.pc.values-1
        o=np.argsort(evtr); cw=np.cumsum(tr.c.values[o])/tr.c.sum(); cut=evtr[o][np.searchsorted(cw,0.90)]
        te['top_'+nm]=ev>=cut
    parts.append(te)
X=pd.concat(parts)
zcol='z'  # z de build_units (ver nota de signo)
X['zs']=X[zcol]*X.sg if abs(np.corrcoef((T.z*T.sg).fillna(0),T.rpre_s.fillna(0))[0,1])>abs(np.corrcoef(T.z.fillna(0),T.rpre_s.fillna(0))[0,1]) else X[zcol]
X['ZS']=(X.zs>-1)&(X.zs<=0)
EV=lambda g: g.pnl.sum()/g.c.sum()
for nm in ('M1F','M2'):
    t=X['top_'+nm]; ex=[]
    for d,g in X.groupby('dia'):
        f=g.c[g['top_'+nm]].sum()/g.c.sum(); ex.append(g.pnl[g['top_'+nm]].sum()-f*g.pnl.sum())
    ex=np.array(ex); bs=[np.random.default_rng(i).choice(ex,len(ex)).mean() for i in range(2000)]
    print(nm,'f %.3f EVtop %.4f EVall %.4f exc %.0f IC90/dia (%.0f,%.0f) dias+ %d sin2 %.0f'%(X.c[t].sum()/X.c.sum(),EV(X[t]),EV(X),ex.sum(),*np.percentile(bs,[5,95]),(ex>0).sum(),np.sort(ex)[:-2].sum()))
    for k in ('R1p','ZS'):
        a=X[k]; 
        print('  %s: P(%s|top)=%.3f P(%s|resto)=%.3f | EV top&%s %.4f (n %d) top&no %.4f (n %d) | notop&%s %.4f notop&no %.4f'%(nm,k,a[t].mean(),k,a[~t].mean(),k,EV(X[t&a]),(t&a).sum(),EV(X[t&~a]),(t&~a).sum(),k,EV(X[~t&a]),EV(X[~t&~a])))
print('solapamiento M1F/M2 top (Jaccard)', ((X.top_M1F&X.top_M2).sum()/(X.top_M1F|X.top_M2).sum()))
X[['dia','mkt','maker','lado_c','top_M1F','top_M2','R1p','ZS','pnl','c']].to_csv('cruce_flags.csv.gz',index=False)
