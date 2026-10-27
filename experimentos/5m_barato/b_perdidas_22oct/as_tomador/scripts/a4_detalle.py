#!/usr/bin/env python3
"""a4: detalle descriptivo de R_W (ADENDA1) + bin tk_score<-0.02 + persistencia de ROI de tomador SEL->TEST en la celda (tab)."""
import json, numpy as np, pandas as pd
from scipy import stats
T0=pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl'); T0['taker']=T0.taker.str.lower()
T=T0[T0.dia>='2026-10-12'].reset_index(drop=True)
pnl=T.pnl.values; c=T.c.values; sc=T.tk_score.values
def ev(m): return float(pnl[m].sum()/c[m].sum()) if m.any() else None
fW=np.nan_to_num(sc,nan=-9)>=0.02
print('--- R_W por dia: EXCESO, EV_IN, EV_OUT, fracEUR')
rows=[]
for d,g in T.groupby('dia'):
    m=(T.dia==d).values; r=m&~fW
    rows.append((d,int(m.sum()),float(pnl[r].sum()/c[r].sum()-pnl[m].sum()/c[m].sum()),ev(m&fW),ev(m&~fW),float(c[m&fW].sum()/c[m].sum()),float(pnl[~fW&m].sum()-pnl[m].sum())))
D=pd.DataFrame(rows,columns=['dia','n','EXC','EV_IN','EV_OUT','fracEUR','dPnL']); print(D.round(4).to_string())
top2=D.sort_values('dPnL',ascending=False).index[:2]
r=~fW.copy(); keep=~T.dia.isin(D.dia[top2]).values
print('sin 2 mejores dias EXC', pnl[keep&~fW].sum()/c[keep&~fW].sum()-pnl[keep].sum()/c[keep].sum(), 'dias', list(D.dia[top2]), 'dias EXC>0:',int((D.EXC>0).sum()),'/',len(D))
for k in ('ETH','SOL','XRP'):
    m=(T.act==k).values; print(k,'n_IN',int((m&fW).sum()),'EV_IN',ev(m&fW),'EV_OUT',ev(m&~fW),'EXC',float(pnl[m&~fW].sum()/c[m&~fW].sum()-pnl[m].sum()/c[m].sum()))
print('--- bin tk_score<-0.02 (takers que pierden): concentracion y dias')
b=(sc<-0.02)
sh=pd.Series(c[b]).groupby(T.taker[b].values).sum().sort_values(ascending=False)
print('n takers',len(sh),'top1',sh.iloc[0]/sh.sum(),sh.index[0],'top5',sh.head(5).sum()/sh.sum())
print('EV por dia (bin) :',{d:(round(ev(b&(T.dia==d).values),3) if (b&(T.dia==d).values).any() else None) for d in sorted(T.dia.unique())})
print('EV por moneda (bin):',{k:round(ev(b&(T.act==k).values),3) for k in ('ETH','SOL','XRP')})
print('EV bin sin top1:',ev(b&(T.taker!=sh.index[0]).values))
print('--- persistencia ROI tomador SEL(09-11)->TEST(12-21) en la celda (unidades de tab; ROI_maker=-ROI_tomador aprox)')
A=T0[T0.dia<='2026-10-11']; B=T0[T0.dia>='2026-10-12']
ga=A.groupby('taker').agg(p=('pnl','sum'),c=('c','sum'),n=('pnl','size')); gb=B.groupby('taker').agg(p=('pnl','sum'),c=('c','sum'),n=('pnl','size'))
J=ga.join(gb,lsuffix='_a',rsuffix='_b',how='inner'); J=J[(J.c_a>=100)&(J.c_b>=100)]
J['ra']=-J.p_a/J.c_a; J['rb']=-J.p_b/J.c_b  # ROI del tomador en la celda (bruto), maker pnl = -tomador
print('takers con coste>=100 en ambos:',len(J),'Spearman',stats.spearmanr(J.ra,J.rb), 'Pearson',stats.pearsonr(J.ra,J.rb))
J['q']=pd.qcut(J.ra,5,labels=False,duplicates='drop')
gq=J.groupby('q').apply(lambda g: pd.Series({'n':len(g),'ROI_sel_pond':-g.p_a.sum()/g.c_a.sum(),'ROI_test_pond':-g.p_b.sum()/g.c_b.sum()}))
print(gq.round(4))
