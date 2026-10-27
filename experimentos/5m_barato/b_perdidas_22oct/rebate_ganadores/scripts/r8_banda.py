#!/usr/bin/env python3
"""r8: PnL(+reb) de los 3 ganadores por banda de precio (rellenos maker+tomador BTC 5m, 06..21-Oct) y reparto del beneficio; rebate/beneficio neto por wallet."""
import pandas as pd,numpy as np,json
R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'; DL='/root/polymarket-research-datalogs/mapa_escala/'
out=open(R+'rebate_ganadores/datos/r8_banda.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
des=json.load(open(DL+'des.json'))
X=pd.read_csv(R+'rebate_ganadores/datos/r4_fills.csv.gz',usecols=['dia','maker','rol','coin','mid','lc','pc','coste','acc','T','fee'],dtype={'mid':'category','maker':'category','rol':'category','coin':'category','lc':'category','dia':'category'})
X=X[(X.coin=='BTC')&(X.acc>0)&(X.coste>0)&(X.pc>=0.01)&(X.pc<0.99)&(X['T']>=-5)].copy()
for c in ('mid','maker','rol','lc'): X[c]=X[c].astype(str)
X['des']=X.mid.map(des); X=X[X.des.notna()]; X['pnl']=X.acc*(X.lc==X.des)-X.coste-np.where(X.rol=='T',X.fee.fillna(0),0)
X['reb']=np.where(X.rol=='M',0.014*(1-X.pc)*X.coste,0.0)
X['banda']=np.digitize(X.pc.values,[0.01,0.05,0.10,0.20,0.30,0.50,0.70,0.90,0.99])-1
B=['.01-.05','.05-.10','.10-.20','.20-.30','.30-.50','.50-.70','.70-.90','.90-.99']
GAN=('0x21f4c1a1','0xe29042f5','0x86b14772')
X['g']=np.where(X.maker.str[:10].isin(GAN),'GAN','CTRL')
P('banda | GAN coste/dia  EV(M+T,sin reb)  EV(+reb) pnl(+reb) | CTRL coste/dia EV sin reb  EV +reb')
for b in range(8):
    r=[]
    for g in ('GAN','CTRL'):
        s=X[(X.g==g)&(X.banda==b)]
        r.append((s.coste.sum()/16, s.pnl.sum()/s.coste.sum() if len(s) else np.nan, (s.pnl.sum()+s.reb.sum())/s.coste.sum() if len(s) else np.nan, s.pnl.sum()+s.reb.sum()))
    P(f"{B[b]:8s} | {r[0][0]:>9,.0f} {r[0][1]:+.4f} {r[0][2]:+.4f} {r[0][3]:>8,.0f} | {r[1][0]:>9,.0f} {r[1][1]:+.4f} {r[1][2]:+.4f}")
P('\nRebate / beneficio neto (M+T+reb) por wallet:')
for a,g in X.groupby('maker'):
    n=g.pnl.sum()+g.reb.sum(); P(f"{a[:10]} {'GAN ' if a[:10] in GAN else 'CTRL'} neto {n:>8,.0f} rebate inferido {g.reb.sum():>7,.0f} ({g.reb.sum()/n if n>0 else float('nan'):.0%} del neto) ; neto sin rebate {g.pnl.sum():>8,.0f}; coste total {g.coste.sum():,.0f}; EV neto +reb por EUR {n/g.coste.sum():+.4f}")
