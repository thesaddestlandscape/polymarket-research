import pandas as pd, numpy as np, glob, sys
S=sys.argv[1]; us='0x659a40ff9920febc5a66836213040924343d297f'
P=pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(S+'/pop_2026-*.pkl'))]); P=P[P.maker!=us]
U=P.groupby(['dia','maker','mkt','lado_c','act']).agg(c=('coste_m','sum'),p=('pnl_m','sum'),sh=('sh','sum'),n=('sh','size'),T0=('T','max'),T1=('T','min'),pc=('pc','mean')).reset_index()
def ev(df,cl='dia',n=2000):
    if len(df)==0: return 'n=0'
    g=df.groupby(cl)[['p','c']].sum(); a,b=g.p.values,g.c.values
    r=np.random.default_rng(1); i=r.integers(0,len(g),(n,len(g))); e=a[i].sum(1)/b[i].sum(1)
    return f"EV {a.sum()/b.sum():+.3f} ({np.quantile(e,.05):+.3f},{np.quantile(e,.95):+.3f}) uds={len(df)} €={b.sum():.0f} días+={int((g.p>0).sum())}/{len(g)}"
print('## EV por tamaño de la unidad maker (acciones acumuladas por maker-mercado-lado) — ojo: el tamaño FINAL condiciona (trampa 19-Oct), solo descriptivo')
for lo,hi in [(0,5.01),(5.01,50),(50,500),(500,1e9)]:
    for per,Q in [('09-19',U[U.dia<='2026-10-19']),('20-21',U[U.dia>='2026-10-20'])]:
        q=Q[(Q.sh>lo)&(Q.sh<=hi)]; print(f'  acc ({lo:.0f},{hi:.0f}] {per}',ev(q))
# selección de ganadoras por resultado 09-14, prueba 15-21 (y 20-21)
sel=U[U.dia<='2026-10-14'].groupby('maker').agg(p=('p','sum'),c=('c','sum'),d=('dia','nunique'))
sel=sel[(sel.d>=3)&(sel.c>=50)]; sel['ev']=sel.p/sel.c
top=set(sel[sel.ev>0].sort_values('p',ascending=False).head(30).index)
bot=set(sel[sel.ev<0].sort_values('p').head(30).index)
test=U[U.dia>='2026-10-15']
act=set(test.maker)&set(sel.index)
print(f'\n## persistencia makers de la celda (alts): seleccion 09-14 (>=3 dias, >=50 $), top-30 por PnL vs peores-30; prueba 15-21. Activos en ambos: {len(act)}')
print('  TOP30  ',ev(test[test.maker.isin(top)]))
print('  PEOR30 ',ev(test[test.maker.isin(bot)]))
print('  RESTO  ',ev(test[test.maker.isin(act-top-bot)]))
rng=np.random.default_rng(7); pl=[]
ac=sorted(act)
for k in range(300):
    g=set(rng.choice(ac,size=min(30,len(ac)),replace=False)); t=test[test.maker.isin(g)]; pl.append(t.p.sum()/t.c.sum())
pl=np.array(pl); tt=test[test.maker.isin(top)]; v=tt.p.sum()/tt.c.sum()
print(f'  placebo 300 grupos aleatorios de 30: mediana {np.median(pl):+.3f}, P(placebo>=top) = {(pl>=v).mean():.2f}')
print('  20-21 solo: TOP30',ev(U[(U.dia>='2026-10-20')&U.maker.isin(top)]),'| PEOR30',ev(U[(U.dia>='2026-10-20')&U.maker.isin(bot)]))
# perfil del top 10 por PnL total 09-21 en la celda alts y su contraste con nosotros
tot=U.groupby('maker').agg(p=('p','sum'),c=('c','sum'),d=('dia','nunique'),uds=('c','size'),acc_ud=('sh','median'),pc=('pc','median'),T0=('T0','median'),mon=('act',lambda s:s.value_counts(normalize=True).round(2).to_dict()))
tot['ev']=tot.p/tot.c
gd=U.groupby(['maker','dia']).p.sum().unstack()
tot['dias_pos']=(gd>0).sum(1).astype(str)+'/'+gd.notna().sum(1).astype(str)
pd.set_option('display.width',300); pd.set_option('display.max_colwidth',60)
print('\n## top-12 makers por PnL en la celda alts 09-21 (descriptivo, selección por resultado)')
print(tot.sort_values('p',ascending=False).head(12).round(3).to_string())
print('\n## makers con >=8 días y EV>0 en >=75 % de sus días (consistencia, no PnL):')
dd=(gd>0).sum(1); nn=gd.notna().sum(1)
cons=tot[(nn>=8)&(dd>=0.75*nn)&(tot.c>=200)]
print(cons.sort_values('p',ascending=False).head(12).round(3).to_string())
