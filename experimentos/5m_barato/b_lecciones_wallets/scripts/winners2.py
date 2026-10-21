import pandas as pd, numpy as np, glob, sys, warnings; warnings.filterwarnings('ignore')
S=sys.argv[1]; us='0x659a40ff9920febc5a66836213040924343d297f'
P=pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(S+'/pop_2026-*.pkl'))])
U=P.groupby(['dia','maker','mkt','lado_c','act']).agg(c=('coste_m','sum'),p=('pnl_m','sum'),sh=('sh','sum'),T0=('T','max'),pc=('pc','mean')).reset_index()
def ev(df):
    g=df.groupby('dia')[['p','c']].sum(); a,b=g.p.values,g.c.values
    r=np.random.default_rng(1); i=r.integers(0,len(g),(2000,len(g))); e=a[i].sum(1)/b[i].sum(1)
    return f"EV {a.sum()/b.sum():+.3f} ({np.quantile(e,.05):+.3f},{np.quantile(e,.95):+.3f}) uds={len(df)} €={b.sum():.0f} días+={int((g.p>0).sum())}/{len(g)}"
for cut in ['2026-10-15','2026-10-17']:
    A=U[U.dia<=cut]; B=U[U.dia>cut]
    gd=A.groupby(['maker','dia']).p.sum().unstack(); nn=gd.notna().sum(axis=1); dp=(gd>0).sum(axis=1)
    cA=A.groupby('maker').c.sum()
    cons=set(gd.index[(nn>=4)&(dp>=0.75*nn)&(cA.reindex(gd.index)>=50)])
    act=sorted(set(B.maker)&set(gd.index[nn>=4]))
    t=B[B.maker.isin(cons)]; v=t.p.sum()/t.c.sum()
    rng=np.random.default_rng(3); pl=[]
    k=len(cons&set(act))
    for _ in range(300):
        g=set(rng.choice(act,size=k,replace=False)); q=B[B.maker.isin(g)]; pl.append(q.p.sum()/q.c.sum())
    print(f'selección por CONSISTENCIA (>=4 días, >=75 % días +, >=50 $) hasta {cut}: {len(cons)} wallets ({k} activas después); prueba > {cut}:',ev(t),f'| placebo mediana {np.median(pl):+.3f}, P(placebo>=sel)={(np.array(pl)>=v).mean():.2f}')
# perfil: % de unidades con primer relleno T>240, por grupo
gd=U.groupby(['maker','dia']).p.sum().unstack(); nn=gd.notna().sum(axis=1); dp=(gd>0).sum(axis=1)
cons=set(gd.index[(nn>=8)&(dp>=0.75*nn)])
for nm,q in [('consistentes 09-21 (in-sample)',U[U.maker.isin(cons)]),('resto makers',U[~U.maker.isin(cons)&(U.maker!=us)]),('NOSOTROS (B)',U[U.maker==us])]:
    print(f'{nm:32s} uds={len(q)} %T0>240={100*(q.T0>240).mean():.0f} %XRP={100*(q.act=="XRP").mean():.0f} acc/ud mediana={q.sh.median():.1f} pc mediana={q.pc.median():.3f}')
