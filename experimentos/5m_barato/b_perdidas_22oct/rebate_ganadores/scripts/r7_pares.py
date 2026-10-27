#!/usr/bin/env python3
"""r7: descomposicion por mercado BTC 5m (unidad mercado, rellenos M+T, desenlace oficial): PnL = bloqueado por pares + residuo direccional.
Por mercado: m=min(accYES,accNO); precio medio ponderado por lado; bloqueado = m*(1-pY-pN) (coste de las m acciones emparejadas a precio medio); residuo = pnl total - bloqueado - rebate.
Ademas: EV por orden de llegada del fill en el mercado (1er tercio / resto) y por tamano del fill."""
import pandas as pd,numpy as np,json
R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'; DL='/root/polymarket-research-datalogs/mapa_escala/'
out=open(R+'rebate_ganadores/datos/r7_pares.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
des=json.load(open(DL+'des.json'))
X=pd.read_csv(R+'rebate_ganadores/datos/r4_fills.csv.gz',usecols=['dia','maker','rol','coin','mid','lc','pc','coste','acc','T','fee','ts_est'],dtype={'mid':'category','maker':'category','rol':'category','coin':'category','lc':'category','dia':'category'})
X=X[(X.coin=='BTC')&(X.acc>0)&(X.coste>0)&(X.pc>=0.01)&(X.pc<0.99)&(X['T']>=-5)].copy()
for c in ('mid','maker','rol','lc','dia'): X[c]=X[c].astype(str)
X['des']=X.mid.map(des); X=X[X.des.notna()]; X['pnl']=X.acc*(X.lc==X.des)-X.coste-np.where(X.rol=='T',X.fee.fillna(0),0)
X['reb']=np.where(X.rol=='M',0.014*(1-X.pc)*X.coste,0.0)
GAN=('0x21f4c1a1','0xe29042f5','0x86b14772')
P('wallet clase | PnL total(+reb) | bloqueado por pares | residuo direccional | EV bloqueado/EUR | EV residuo/EUR | mercados con par | pnl/mercado dir (IC90 mercados)')
rng=np.random.default_rng(1)
for a,g in X.groupby('maker'):
    pv=g.pivot_table(index='mid',columns='lc',values=['acc','coste'],aggfunc='sum',fill_value=0)
    for k in ('YES','NO'):
        for v in ('acc','coste'):
            if (v,k) not in pv.columns: pv[(v,k)]=0.0
    aY,aN,cY,cN=pv[('acc','YES')],pv[('acc','NO')],pv[('coste','YES')],pv[('coste','NO')]
    m=np.minimum(aY,aN); pY=np.where(aY>0,cY/aY.replace(0,np.nan),0); pN=np.where(aN>0,cN/aN.replace(0,np.nan),0)
    lock=(m*(1-pY-pN)).fillna(0)
    tot=g.groupby('mid').agg(p=('pnl','sum'),r=('reb','sum'),c=('coste','sum')).reindex(pv.index)
    res=tot.p-lock
    haypar=m>0
    d=res[haypar]; bs=[d.values[rng.integers(0,len(d),len(d))].mean() for _ in range(1000)]
    P(f"{a[:10]} {'GAN ' if a[:10] in GAN else 'PERD'} | {(tot.p+tot.r).sum():>8,.0f} | {lock.sum():>8,.0f} | {res.sum():>8,.0f} | {lock.sum()/tot.c.sum():+.4f} | {res.sum()/tot.c.sum():+.4f} | {haypar.mean():.2f} | {d.mean():+.2f} ({np.percentile(bs,5):+.2f},{np.percentile(bs,95):+.2f}) ; pares: precio medio YES+NO emparejado {np.nanmean((pY+pN)[haypar.values]):.3f}")
P('\n== EV maker (sin rebate) por orden de llegada en el mercado y tamano de fill ==')
for a,g in X[X.rol=='M'].groupby('maker'):
    g=g.sort_values(['mid','ts_est']); g['rk']=g.groupby('mid').cumcount()/g.groupby('mid').acc.transform('size')
    f=lambda s:s.pnl.sum()/s.coste.sum()
    q=pd.qcut(g.acc,[0,.5,.9,1],duplicates='drop')
    P(f"{a[:10]} {'GAN ' if a[:10] in GAN else 'PERD'} llegada tercio1 {f(g[g.rk<1/3]):+.4f} tercio2 {f(g[(g.rk>=1/3)&(g.rk<2/3)]):+.4f} tercio3 {f(g[g.rk>=2/3]):+.4f} | tamano mediana-baja {f(g[g.acc<=g.acc.median()]):+.4f} p90+ {f(g[g.acc>=g.acc.quantile(.9)]):+.4f} | por T(<=60,60-150,150-300): "+' '.join(f"{f(g[(g['T']>lo)&(g['T']<=hi)]):+.4f}" for lo,hi in ((-5,60),(60,150),(150,300))))
