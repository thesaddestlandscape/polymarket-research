#!/usr/bin/env python3
"""r13: compara sim v2 con real por dia (construccion o evaluacion). Uso: r13_v2_compara.py SALIDA DIA1,DIA2,.. [VARIANTE_unica]"""
import pandas as pd,numpy as np,sys,glob
RG='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/rebate_ganadores/datos/'
out=open(RG+sys.argv[1],'w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
dias=sys.argv[2].split(','); only=sys.argv[3] if len(sys.argv)>3 else None
S=pd.concat([pd.read_csv(RG+f'r12_sim_{d}.csv.gz',dtype={'mid':str}) for d in dias]); Rl=pd.concat([pd.read_csv(RG+f'r12_real_{d}.csv.gz',dtype={'mid':str}) for d in dias])
if only: S=S[S['var']==only]
Rl['w']=Rl.maker.str[:10]; ev=lambda g:(g.pnl.sum()+g.reb.sum())/g.coste.sum() if len(g) and g.coste.sum()>0 else np.nan
nm=S.groupby('dia').mid.nunique().to_dict(); P('dias',dias,'mercados validos con fill sim',nm, '| mercados reales por wallet:',Rl.groupby('w').mid.nunique().to_dict())
rr={w:{d:ev(x) for d,x in g.groupby('dia')} for w,g in Rl.groupby('w')}
for w,r in rr.items(): P('REAL',w,'EV(+reb)/dia',{d[-2:]:round(v,4) for d,v in r.items()},'total',round(ev(Rl[Rl.w==w]),4),'fills',int((Rl.w==w).sum()))
sv={}
for v,g in S.groupby('var'):
    sv[v]={d:ev(x) for d,x in g.groupby('dia')}; P('SIM',v,'EV(+reb)/dia',{d[-2:]:round(x,4) for d,x in sv[v].items()},'total',round(ev(g),4),'sin reb',round(g.pnl.sum()/g.coste.sum(),4),'fills',len(g),'acc/mercado-lado med',round(g.groupby(['mid','lc']).acc.sum().median(),0))
P('\nCRITERIO por variante x wallet: dias con |dEV|<=0.005 y mismo signo / dias; error medio (sim-real)')
allerr={}
for v,r in sv.items():
    for w,rw in rr.items():
        ok=[abs(r.get(d,np.nan)-rw[d])<=0.005 and np.sign(r.get(d,np.nan))==np.sign(rw[d]) for d in rw]; sg=[np.sign(r.get(d,np.nan))==np.sign(rw[d]) for d in rw]
        e=[r.get(d,np.nan)-rw[d] for d in rw]; allerr.setdefault(v,[]).extend(np.abs(e))
        P(f"{v} {w}: error<=0.5pp+signo {sum(ok)}/{len(ok)} ; solo signo {sum(sg)}/{len(sg)} ; error medio {np.nanmean(e):+.4f} ; |error| medio {np.nanmean(np.abs(e)):.4f}")
for v,e in allerr.items(): P('MEDIA |error| (3 wallets x dias)',v,round(float(np.nanmean(e)),4))
P('\nPATA SUELTA vs EMPAREJADA (real, por wallet): EV terminal(+reb)/EUR y markout30 s del bid (Δbid/EUR)')
Rl['mo']=(Rl.bid30-Rl.pc)*Rl.acc
for (w,rp),g in Rl.groupby(['w','rol_pata']):
    gg=g.dropna(subset=['bid30']); P(w,rp,'coste',round(g.coste.sum()),'EV terminal',round(ev(g),4),'markout30',round(gg.mo.sum()/gg.coste.sum(),4) if len(gg) else None,'n',len(g))
def lockres(df):
    o=[]
    for (k,mid),g in df.groupby([df['maker'] if 'maker' in df else df['var'],'mid']):
        a=g.groupby('lc').agg(acc=('acc','sum'),c=('coste','sum'),p=('pnl','sum'),r=('reb','sum')).reindex(['YES','NO']).fillna(0)
        m=min(a.acc.YES,a.acc.NO); pY=a.c.YES/a.acc.YES if a.acc.YES>0 else 0; pN=a.c.NO/a.acc.NO if a.acc.NO>0 else 0
        lock=m*(1-pY-pN) if m>0 else 0; o.append((k,lock,a.p.sum()-lock,a.c.sum(),a.r.sum()))
    return pd.DataFrame(o,columns=['k','lock','res','c','r'])
P('\nBLOQUEADO por pares vs RESIDUO (pata suelta), por EUR de coste')
L=lockres(Rl.assign(maker=Rl.w)); 
for k,g in L.groupby('k'): P('REAL',k,f"bloqueado {g.lock.sum()/g.c.sum():+.4f}/EUR residuo {g.res.sum()/g.c.sum():+.4f}/EUR rebate {g.r.sum()/g.c.sum():+.4f}")
L=lockres(S)
for k,g in L.groupby('k'): P('SIM',k,f"bloqueado {g.lock.sum()/g.c.sum():+.4f}/EUR residuo {g.res.sum()/g.c.sum():+.4f}/EUR rebate {g.r.sum()/g.c.sum():+.4f}")
P('\nNIVELES (sim): distribucion del coste por distancia al precio mas alto rellenado del mercado-lado no disponible; coste por banda sim:')
b=pd.cut(S.pc,[0.01,0.1,0.2,0.3,0.5,0.7,0.9,0.99],right=False)
for v,g in S.groupby('var'): P(v,{str(k):round(x.coste.sum()) for k,x in g.groupby(pd.cut(g.pc,[0.01,0.1,0.3,0.5,0.7,0.99],right=False),observed=True)})
b=pd.cut(Rl.pc,[0.01,0.1,0.3,0.5,0.7,0.99],right=False)
for w,g in Rl.groupby('w'): P('REAL',w,{str(k):round(x.coste.sum()) for k,x in g.groupby(pd.cut(g.pc,[0.01,0.1,0.3,0.5,0.7,0.99],right=False),observed=True)})
