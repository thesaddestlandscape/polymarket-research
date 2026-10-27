import sys; sys.argv=['x','none']; exec(open('main.py').read().split("if __name__=='__main__':")[0])
from scipy import stats
D0,D1='2026-10-05','2026-10-23'
UA=units(Y[Y.dia.between(D0,D1)],ALT); UB=units(Y[Y.dia.between(D0,D1)],BTC)
def daily(U):
    r={}
    for d,g in U.groupby('dia'):
        a=g[g.cls=='CON']; b=g[g.cls=='CONTRA']
        r[d]=(len(a),len(b),delta(g) if len(a)>=3 and len(b)>=3 else np.nan)
    return pd.DataFrame(r,index=['nCON','nCTR','Delta']).T
da=daily(UA); db=daily(UB); t=da.join(db,lsuffix='_alts',rsuffix='_btc'); P('\n## Delta diario (unidad: cierre-lado, ask real, T180+250ms)'); P(t.round(3).to_string())
ok=t[['Delta_alts','Delta_btc']].dropna(); P(f'corr Pearson dia alts-BTC {ok.corr().iloc[0,1]:+.2f} (n {len(ok)}); Spearman {stats.spearmanr(ok.Delta_alts,ok.Delta_btc)[0]:+.2f} p {stats.spearmanr(ok.Delta_alts,ok.Delta_btc)[1]:.3f}')
for nm,x in (('alts',da.Delta.dropna()),('BTC',db.Delta.dropna())):
    for rng_,lab in ((slice('2026-10-05','2026-10-21'),'05-21'),(slice('2026-10-05','2026-10-23'),'05-23')):
        v=x.loc[rng_]; k=(v<0).sum(); n=len(v); P(f'  {nm} {lab}: dias {n}, Delta<0 en {k}; test de signos bilateral p {stats.binomtest(k,n,0.5).pvalue:.3f}; media diaria {v.mean():+.3f} sd {v.std():.3f}; t-test dias p(bilateral) {stats.ttest_1samp(v,0).pvalue:.3f}')
# Diferencia BTC vs alts pareada por cierre (mismo cierre en ambas monedas)
def paired(UA,UB,key='cierre',nb=4000,seed=5):
    V=pd.concat([UA.assign(g='A'),UB.assign(g='B')]); V=V[V.cls.isin(['CON','CONTRA'])]
    g=V.groupby([key,'g','cls']).agg(p=('pnl','sum'),c=('cst','sum')).unstack(['g','cls']).fillna(0)
    cols=[(v,gg,c) for gg in 'AB' for c in ('CON','CONTRA') for v in 'pc']
    for c in cols:
        if c not in g.columns: g[c]=0.0
    a=g[cols].values  # A: pCON cCON pCTR cCTR ; B: same
    def f(s): return (s[4]/s[5]-s[6]/s[7])-(s[0]/s[1]-s[2]/s[3])
    n=len(a); rng=np.random.default_rng(seed); idx=rng.integers(0,n,(nb,n)); S=a[idx].sum(1)
    bs=(S[:,4]/S[:,5]-S[:,6]/S[:,7])-(S[:,0]/S[:,1]-S[:,2]/S[:,3]); return f(a.sum(0)),np.percentile(bs,[5,95]),(bs<=0).mean()*2,n
for lab,(d0,d1) in (('05-21',('2026-10-05','2026-10-21')),('05-23',(D0,D1))):
    ua=UA[UA.dia.between(d0,d1)]; ub=UB[UB.dia.between(d0,d1)]
    for key in ('cierre','dia'):
        d,ic,p2,n=paired(ua,ub,key); P(f'Interaccion (Delta_BTC - Delta_alts) {lab} por {key}: {d:+.3f} IC90 ({ic[0]:+.3f},{ic[1]:+.3f}) p2(bootstrap) {p2:.3f} clusters {n}')
# sensibilidades BTC (y alts) por variante
P('\n## Sensibilidades (post-hoc, descriptivas). Delta [IC90 cierre] ; n CON/CONTRA')
def line(label,U):
    r=h1(U,label,full=False)
for lab,coins in (('BTC',BTC),('ALTS',ALT)):
    for T,lag in ((180,250),(180,0),(180,1000),(120,250),(120,0),(120,1000)):
        YY=prep(view(X,T,lag),W,des); line(f'{lab} T={T} lag={lag} ask 05-23',units(YY,coins))
    YY=Y
    line(f'{lab} bid 05-23',units(YY,coins,'bid')); line(f'{lab} print 05-23',units(YY,coins,'print'))
    line(f'{lab} asz>=5 acc 05-23',units(YY,coins,minsz=5)); line(f'{lab} asz>=20 acc 05-23',units(YY,coins,minsz=20))
    for lo,hi in ((0.10,0.15),(0.15,0.20),(0.20,0.25),(0.25,0.30)): line(f'{lab} ask[{lo:.2f},{hi:.2f}) 05-23',units(YY,coins,lo=lo,hi=hi))
    line(f'{lab} mitad A 05-13',units(YY[YY.dia<='2026-10-13'],coins)); line(f'{lab} mitad B 14-23',units(YY[YY.dia>='2026-10-14'],coins))
    for thr in (4.7,7.7,11,15,20):
        YT=prep(view(X),W,des,thr=thr); line(f'{lab} umbral CON/CONTRA {thr} bps',units(YT,coins))
# BTC por R
P('\n## Delta por regimen R (dentro de CON/CONTRA)')
for lab,U in (('BTC',UB),('ALTS',UA)):
    for R in ('TREND','MIXTO','REVERT'): h1(U[U.R==R],f'{lab} R={R}',full=False)
# por hora UTC bloque 6h BTC
UB2=UB.copy(); UB2['blk']=((UB2.cierre%86400)//21600)
for b in range(4): h1(UB2[UB2.blk==b],f'BTC bloque UTC {6*b:02d}-{6*b+6:02d}',full=False)
# leave-one-day-out
for lab,U in (('ALTS',UA),('BTC',UB)):
    v=[delta(U[U.dia!=d]) for d in sorted(U.dia.unique())]; P(f'leave-one-day-out {lab}: min {min(v):+.3f} max {max(v):+.3f}')
open('out_B.txt','w').write('\n'.join(OUT))
