import pandas as pd, numpy as np, glob, sys, json
S=sys.argv[1]; us='0x659a40ff9920febc5a66836213040924343d297f'
P=pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(S+'/pop_2026-*.pkl'))])
P=P[P.maker!=us]
P['small']=P.sh<=20
def ev_ic(df,clave='dia',n=3000):
    g=df.groupby(clave)[['pnl_m','coste_m']].sum()
    if len(g)<2: return round(df.pnl_m.sum()/df.coste_m.sum(),3),None,len(g)
    a,b=g.pnl_m.values,g.coste_m.values; r=np.random.default_rng(1); i=r.integers(0,len(g),(n,len(g)))
    e=a[i].sum(1)/b[i].sum(1); return round(a.sum()/b.sum(),3),tuple(np.quantile(e,[.05,.95]).round(3)),len(g)
def comp(df,mask,lab):
    a=df[mask]; b=df[~mask]
    da=a.groupby('dia')[['pnl_m','coste_m']].sum(); db=b.groupby('dia')[['pnl_m','coste_m']].sum()
    dd=(da.pnl_m/da.coste_m - db.pnl_m/db.coste_m).dropna()
    print(f'{lab:40s} SI: n={len(a)} €={a.coste_m.sum():.0f} EV={ev_ic(a)} hit={a.gana.mean():.3f} pc={a.coste_m.sum()/a.sh.sum():.3f} | NO: n={len(b)} EV={ev_ic(b)} | dif por día SI−NO: media {dd.mean():.3f}, días SI<NO {int((dd<0).sum())}/{len(dd)}')
for nm,P2 in [('TODOS makers 09-21 (sin nosotros)',P),('makers pequeños (≤20 acc/relleno)',P[P.small]),('09-19 Oct (antes de B)',P[P.dia<='2026-10-19']),('20-21 Oct (mismo periodo que B)',P[P.dia>='2026-10-20'])]:
    print('\n###',nm,'n',len(P2),'EV',ev_ic(P2))
    for f in ['bn_pre10x','bn_pre5x','bn_pre20x','bn_pre30x']:
        x=P2[f]; m=(x<=-2)&x.notna()
        comp(P2[x.notna()],m[x.notna()],f+' <= -2 bps (en contra)')
    x=P2.bn_pre10x; comp(P2[x.notna()],(x<=-5)[x.notna()],'bn_pre10x <= -5')
    comp(P2,P2['T']>240,'T>240 s')
    comp(P2,P2['T']<=120,'T<=120 s')
    comp(P2,P2.pc>0.25,'pc>0.25')
    comp(P2,P2.pc<=0.15,'pc<=0.15')
    for a in ['ETH','SOL','XRP']:
        comp(P2,P2.act==a,'moneda '+a)
