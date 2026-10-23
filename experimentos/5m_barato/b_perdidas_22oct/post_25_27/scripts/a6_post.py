# A6 (POST-HOC, no preregistrado en PREREG_POST2527 salvo lo indicado): ordenes por clase, EV poblacion por clase de regimen R, regla "no cotizar en REVERT". Familia total tras esto: 8 reglas, Bonferroni x8 (p<0,00625).
import pandas as pd, numpy as np, glob
D='/root/polymarket-research-datalogs'; O='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/post_25_27/datos'
S='/tmp/claude-0/-root-polymarket-research/3253f6f0-a68e-48c4-97db-8bfe225d6aca/scratchpad'
rng=np.random.default_rng(20261023)
E=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f'{D}/regimen_5m/etiquetas/regimen_*.csv.gz'))]+[pd.read_csv(f'{S}/reg/etiquetas/regimen_2026-10-23.csv.gz')]).drop_duplicates(['coin','tmin'],keep='last')[['coin','tmin','R']]
# ordenes
L=pd.concat([pd.read_csv(f'{D}/etiquetado_pasivo_B/etiquetado_B_{d}.csv.gz') for d in ['2026-10-20','2026-10-21','2026-10-22','2026-10-23']]); O_=L[L.unidad=='orden'].copy()
O_['tmin']=(O_.fin_s//60-5).astype(int); O_=O_.merge(E,on=['coin','tmin'],how='left'); O_['R']=O_.R.fillna('NA'); O_['llena']=(O_.acc_llena>0).astype(int)
O_['mk']=O_.mercado+'|'+O_.lado
print('ORDENES (puja_post) 20-23 Oct n',len(O_),'; con relleno',int(O_.llena.sum()))
for d,g in O_.groupby('dia'): print(d,'ordenes',len(g),'mercados-lado',g.mk.nunique(),'rellenos',int(g.llena.sum()),'tasa relleno por orden %.3f'%g.llena.mean(),'| por mercado-lado %.3f'%(g.groupby('mk').llena.max().mean()))
print('tasa de relleno por mercado-lado segun h_w1 / R (20-23, unidad = mercado-lado):')
u=O_.groupby('mk').agg(llena=('llena','max'),h=('h_w1','max'),R=('R','first'),dia=('dia','first'),clase=('clase_rpre','first')).reset_index()
print(u.groupby('h').llena.agg(['size','mean']).round(3).T.to_string()); print(u.groupby('R').llena.agg(['size','mean']).round(3).T.to_string()); print(u.groupby('clase').llena.agg(['size','mean']).round(3).T.to_string())
print('23-Oct solo:'); u3=u[u.dia=='2026-10-23']; print(u3.groupby('h').llena.agg(['size','sum','mean']).round(3).T.to_string())
# poblacion: EV por clase R
pob=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f'{D}/etiquetado_pasivo_B/poblacion/pob_*.csv.gz'))])
pob=pob[pob.gana_lado.notna()&pob.pnl.notna()&pob.coin.isin(['ETH','SOL','XRP'])&(pob.precio>=0.10)&(pob.precio<0.30)].copy()
pob['tmin']=(pob.fin_s//60-5).astype(int); pob=pob.merge(E,on=['coin','tmin'],how='left'); pob['R']=pob.R.fillna('NA')
def ev(g): return g.pnl.sum()/g.coste.sum()
def ci(g,nb=1500):
    uc=g.fin_s.values; ucs=np.unique(uc); ix={c:np.nonzero(uc==c)[0] for c in ucs}; pn=g.pnl.values; co=g.coste.values; s=[]
    cs=np.array([[pn[ix[c]].sum(),co[ix[c]].sum()] for c in ucs])
    for _ in range(nb): j=rng.integers(0,len(ucs),len(ucs)); s.append(cs[j,0].sum()/cs[j,1].sum())
    return np.percentile(s,5),np.percentile(s,95)
print('\nPOBLACION 17-22 (28.8k aprox, ya vista por R-TEND/W1; DESCRIPTIVO): EV por clase R'); 
for r,g in pob.groupby('R'):
    a=ci(g); print(f' R={r}: n {len(g)} coste {g.coste.sum():.0f} EV {ev(g):+.4f} IC90 cierre ({a[0]:+.3f},{a[1]:+.3f}) hit {g.gana_lado.mean():.3f}')
print(' por dia x R (EV):'); print(pob.groupby(['dia','R']).apply(ev).unstack().round(3).to_string())
print(' B 20-23 por dia x R (EV):'); P=pd.read_csv(f'{O}/pos_b.csv',keep_default_na=False,na_values=['']); P['R']=P.R.fillna('NA'); print(P.groupby(['dia','R']).apply(lambda g:g.pnl.sum()/g.coste.sum()).unstack().round(3).to_string())
# regla post-hoc: no cotizar en REVERT / no cotizar fuera de MIXTO, sobre B
def regla(Q,nm,s,nperm=20000):
    s=np.asarray(s,bool); pn=Q.pnl.values; k=int(s.sum()); dP=-pn[s].sum(); r=np.array([-pn[rng.choice(len(Q),k,replace=False)].sum() for _ in range(nperm)])
    cl=Q.cierre.values; uc=np.unique(cl); ix={c:np.nonzero(cl==c)[0] for c in uc}; ss=np.array([pn[ix[c]][s[ix[c]]].sum() for c in uc]); bs=np.array([-ss[rng.integers(0,len(uc),len(uc))].sum() for _ in range(3000)])
    print(f'{nm}: evaluadas {len(Q)} saltadas {k} coste {Q.coste[s].sum():.2f} pnl_saltadas {pn[s].sum():+.2f} dPnL {dP:+.2f} ganancias perdidas {pn[s][pn[s]>0].sum():.2f} p_perm {np.mean(r>=dP):.3f} IC90 cierre ({np.percentile(bs,5):+.2f},{np.percentile(bs,95):+.2f})')
Q=P[P.R!='NA']
print('\nREGLAS POST-HOC sobre posiciones de B (Bonferroni x8):')
for nm,Qs in [('23-Oct',Q[Q.dia=='2026-10-23']),('B 20-22 (visto)',Q[Q.dia<'2026-10-23']),('B total',Q)]:
    regla(Qs,f'[{nm}] RX1 no cotizar si R==REVERT',Qs.R=='REVERT'); regla(Qs,f'[{nm}] RX2 no cotizar si R!=MIXTO',Qs.R!='MIXTO')
# misma regla en la POBLACION como replica (PnL total, p por permutacion dentro de dia x moneda x cubo 0,05)
pob['cub']=(pob.precio*20).astype(int); pob=pob[pob.R!='NA']; st=(pob.dia.astype(str)+pob.coin+pob.cub.astype(str)).astype('category').cat.codes.values; s=(pob.R=='REVERT').values
idx=pd.Series(np.arange(len(pob))).groupby(st).apply(list); cnt=pd.Series(s).groupby(st).sum(); pn=pob.pnl.values; dP=-pn[s].sum(); pl=[]
for _ in range(500):
    t=0.0
    for g_,k in cnt.items():
        if k: t+=pn[rng.choice(idx[g_],int(k),replace=False)].sum()
    pl.append(-t)
print(f'POBLACION replica RX1 (descriptiva, mismo periodo que B 20-22): saltadas {int(s.sum())} de {len(pob)} coste {pob.coste[s].sum():.0f} dPnL {dP:+.1f} EUR ; placebo (dia x moneda x cubo) p {np.mean(np.array(pl)>=dP):.3f} ; EV retenido {pn[~s].sum()/pob.coste[~s].sum():+.4f} vs base {pn.sum()/pob.coste.sum():+.4f}')
