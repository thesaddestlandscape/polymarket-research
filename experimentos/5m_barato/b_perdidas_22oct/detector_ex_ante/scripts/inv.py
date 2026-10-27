import pandas as pd, numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
T=pd.read_pickle('T_det.pkl')
FWD=['pc','T','coin','hora','lado','vol30','bb','ba','bs','as_','spread','depth_ticks','b15','a15','lvl15','gap15','d15_30','dbb30','vol30ws','r60f','rpre_s','CON','imb','qage','q15age']
FULL=FWD+['gap_last','dp5','dp30','dp60','hi60','rng60','d_open','vol_all','flow60','fv_gap','z','sig_bps_s','b10']
days=sorted(T.dia.unique()); test=[d for d in days if '2026-10-12'<=d<='2026-10-20']
rows=[]
for feats,name in ((FWD,'M1'),(FULL,'M2')):
  for d in test:
    tr=T[T.dia<d]; te=T[T.dia==d]
    m=HistGradientBoostingClassifier(max_depth=3,max_iter=200,learning_rate=0.05,min_samples_leaf=300,l2_regularization=1.0,random_state=0).fit(tr[feats],tr.y)
    ev=m.predict_proba(te[feats])[:,1]/te.pc.values-1; evtr=m.predict_proba(tr[feats])[:,1]/tr.pc.values-1
    P=te.pnl.values;C=te.c.values
    for q in (0.9,0.75):
      top=ev>=np.quantile(evtr,q); f=C[top].sum()/C.sum()
      # beneficio de "concentrar" = EV del top - EV total; tambien dentro de estrato de precio (pc +-0,02)
      rows.append({'m':name,'dia':d,'q':q,'f':f,'EVtop':P[top].sum()/C[top].sum(),'EVall':P.sum()/C.sum(),'exc_top':P[top].sum()-f*P.sum(),
                   'pc_top':np.average(te.pc[top],weights=C[top]),'pc_all':np.average(te.pc,weights=C),'hit_pc_top':(te.y[top]-te.pc[top]).mean(),'hit_pc_rest':(te.y[~top]-te.pc[~top]).mean(),'coin_top_eth':(te.coin[top]==0).mean()})
R=pd.DataFrame(rows)
for (m,q),g in R.groupby(['m','q']):
    ex=g.exc_top.values; bs=[np.random.default_rng(i).choice(ex,len(ex)).mean() for i in range(2000)]
    print(m,q,'f=%.3f'%g.f.mean(),'EVtop %.4f EVall %.4f'%(np.average(g.EVtop,weights=g.f),g.EVall.mean()),'exc_tot %.1f IC90/dia (%.1f,%.1f) dias+ %d sin2 %.1f'%(ex.sum(),*np.percentile(bs,[5,95]),(ex>0).sum(),np.sort(ex)[:-2].sum()),
          'pc_top %.3f pc_all %.3f hit-pc top %.4f resto %.4f ETH_top %.2f'%(g.pc_top.mean(),g.pc_all.mean(),g.hit_pc_top.mean(),g.hit_pc_rest.mean(),g.coin_top_eth.mean()))
    print('   por dia exc_top', np.round(ex,1).tolist())
