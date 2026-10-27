import sys; sys.argv=['x','none']; exec(open('B.py').read().split("da=daily(UA)")[0])
D0,D1='2026-10-05','2026-10-23'
# 1) interaccion a T=120
Y120=prep(view(X,120,250),W,des)
for lab,(d0,d1) in (('05-23',(D0,D1)),):
    ua=units(Y120[Y120.dia.between(d0,d1)],ALT); ub=units(Y120[Y120.dia.between(d0,d1)],BTC)
    exec(open('B.py').read().split("# Diferencia BTC vs alts pareada por cierre (mismo cierre en ambas monedas)")[1].split("for lab,(d0,d1)")[0])
    d,ic,p2,n=paired(ua,ub,'cierre',nb=1000); P(f'Interaccion BTC-alts T=120 {lab} por cierre: {d:+.3f} IC90 ({ic[0]:+.3f},{ic[1]:+.3f}) p2 {p2:.3f}')
    d,ic,p2,n=paired(ua,ub,'dia'); P(f'Interaccion BTC-alts T=120 {lab} por dia: {d:+.3f} IC90 ({ic[0]:+.3f},{ic[1]:+.3f}) p2 {p2:.3f}')
# 2) bootstrap por bloques de 3 dias (circular) - dependencia temporal
def blockboot(U,L=3,nb=4000,seed=3):
    V=U[U.cls.isin(['CON','CONTRA'])]; days=sorted(V.dia.unique()); nd=len(days)
    g=V.groupby(['dia','cls']).agg(p=('pnl','sum'),c=('cst','sum')).unstack('cls').fillna(0).reindex(days).fillna(0)
    a=g[[('p','CON'),('c','CON'),('p','CONTRA'),('c','CONTRA')]].values; rng=np.random.default_rng(seed); out=[]
    nblk=int(np.ceil(nd/L))
    for _ in range(nb):
        st=rng.integers(0,nd,nblk); idx=np.concatenate([(s+np.arange(L))%nd for s in st])[:nd]; s=a[idx].sum(0); out.append(s[0]/s[1]-s[2]/s[3])
    return np.percentile(out,[5,95]),np.mean(np.array(out)>=0)
for lab,U in (('ALTS 05-23',UA),('BTC 05-23',UB),('ALTS 05-21',UA[UA.dia<='2026-10-21']),('BTC 05-21',UB[UB.dia<='2026-10-21'])):
    for L in (2,3,5):
        ic,pp=blockboot(U,L); P(f'bloques circulares de {L} dias {lab}: Delta {delta(U):+.3f} IC90 ({ic[0]:+.3f},{ic[1]:+.3f}) P(Delta*>=0) {pp:.3f}')
# 3) por moneda
for c in ['ETH','SOL','XRP','BNB','DOGE','BTC']:
    for lab,(d0,d1) in (('05-21',('2026-10-05','2026-10-21')),('22-23',('2026-10-22','2026-10-23'))):
        h1(units(Y[Y.dia.between(d0,d1)],[c]),f'{c} {lab}',full=False)
# 4) dEV de R0 (EV retenido - EV total) con IC90 por dia y cierre para alts 05-23 y BTC
def dEV_boot(U,key,nb=4000,seed=9):
    a=U[U.cls=='CON']; keepm=U.cls!='CON'
    g=pd.DataFrame({'k':U[key],'p':U.pnl,'c':U.cst,'keep':keepm.astype(int)}); g['pk']=g.p*g.keep; g['ck']=g.c*g.keep
    s=g.groupby('k')[['p','c','pk','ck']].sum().values; n=len(s); rng=np.random.default_rng(seed); idx=rng.integers(0,n,(nb,n)); S=s[idx].sum(1); bs=S[:,2]/S[:,3]-S[:,0]/S[:,1]; t=s.sum(0)
    return t[2]/t[3]-t[0]/t[1],np.percentile(bs,[5,95])
for lab,U in (('ALTS 05-21',UA[UA.dia<='2026-10-21']),('ALTS 22-23',UA[UA.dia>='2026-10-22']),('ALTS 05-23',UA),('BTC 05-23',UB)):
    for key in ('cierre','dia'):
        d,ic=dEV_boot(U,key); P(f'dEV R0 (EV sin CON - EV todo) {lab} por {key}: {d:+.4f} IC90 ({ic[0]:+.4f},{ic[1]:+.4f})')
# 5) dEV por dia alts: sd, para potencia
dd=[]
for d,g in UA.groupby('dia'):
    k=g[g.cls!='CON']; dd.append(ev(k.pnl,k.cst)-ev(g.pnl,g.cst))
dd=np.array(dd); P(f'dEV R0 diario alts: media {dd.mean():+.4f} sd {dd.std(ddof=1):.4f}; dias>0 {(dd>0).sum()}/{len(dd)}')
open('out_C.txt','w').write('\n'.join(OUT))
