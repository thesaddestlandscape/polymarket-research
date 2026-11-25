import json,numpy as np,pandas as pd
H='out/'; OLD='../recalc_13nov/out/'; days=[f'2026-11-{d:02d}' for d in range(2,13)]; V=('G0','T1','PLA_T1')
print('dia sinev% min_hueco n_huecos horas_malas -> estado (criterio fijado: sinev>10% O min_hueco>120)')
clean=[]
for d in days:
    m=json.load(open(H+f'hole60_dec2v3_meta_{d}.json')); M=json.load(open(H+f'meta2_{d}.json'))
    s=100*m['n_sinev']/m['n_ev']; mh=sum(b-a for a,b in M['holes'])/60000; ok=(s<=10 and mh<=120); 
    print(d,round(s,1),round(mh),len(M['holes']),len(M['bad_hours']),'LIMPIO' if ok else 'DEGRADADO'); 
    if ok: clean.append(d)
A=pd.read_pickle(H+'A_hole60.pkl'); 
def ic(x):
    x=np.asarray(x,float); n=len(x); t={9:1.833,8:1.860,7:1.895,6:1.943}.get(n-1,1.8); se=x.std(ddof=1)/np.sqrt(n); return round(x.mean(),1),round(x.mean()-t*se,1),round(x.mean()+t*se,1),int((x>0).sum()),n
def blk(sub,lab):
    dd=sub.groupby(['d','var']).pnl.sum().unstack().fillna(0); o={}
    for v in V: y=sub[sub['var']==v]; o[v]=(round(y.pnl.sum(),1),round(y.pnl.sum()/y.cost.sum(),3))
    print(lab,o,'| dT1G0 tot',round(o['T1'][0]-o['G0'][0],1),'dia',ic(dd['T1']-dd['G0']),'| T1-PLA',round(o['T1'][0]-o['PLA_T1'][0],1),'dia',ic(dd['T1']-dd['PLA_T1']))
for lab,ds in (('11 dias',days),('LIMPIOS',clean)):
    S=A[A.d.isin(ds)]; print('==',lab,len(ds),'dias'); blk(S,'hole60 todo'); blk(S[S.bad],'  recuperadas'); blk(S[~S.bad],'  ya incluidas')
O=pd.concat([pd.read_pickle(OLD+f'dec2v3_{d}.pkl').assign(d=d) for d in clean]); O=O[O['var'].isin(V)]; blk(O,'baseline HORA, dias limpios')
