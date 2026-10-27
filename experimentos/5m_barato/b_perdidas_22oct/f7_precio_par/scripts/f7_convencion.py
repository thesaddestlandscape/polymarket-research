#!/usr/bin/env python3
"""f7: la descomposicion 'margen bloqueado / pata suelta' depende de la convencion de emparejado. Se calcula en REAL (fills maker de los 3 ganadores en los mercados validos de la muestra libro5) y en SIM V2B, con tres convenciones:
AVG (r7: m*(1-pYmedio-pNmedio)), FIFO (por orden temporal), BEST (se emparejan las acciones mas baratas de cada lado = cota superior del margen). Total identico."""
import pandas as pd,numpy as np,glob,json,collections
RG='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/rebate_ganadores/datos/'
DAYS=['2026-10-18','2026-10-19','2026-10-20','2026-10-21','2026-10-22','2026-10-23']
def conv(g):  # g: filas de un (agente,mercado): lc,pc,acc,orden
    y=g[g.lc=='YES']; n=g[g.lc=='NO']; aY,aN=y.acc.sum(),n.acc.sum(); m=min(aY,aN)
    if m<=0: return 0.0,0.0,0.0
    avg=m*(1-(y.pc*y.acc).sum()/aY-(n.pc*n.acc).sum()/aN)
    def take(d,m,asc):
        d=d.sort_values('pc',ascending=asc); c=d.acc.cumsum(); t=np.minimum(d.acc,np.maximum(0,m-(c-d.acc))); return (t*d.pc).sum()
    best=m-take(y,m,True)-take(n,m,True)
    # fifo: emparejar en orden temporal
    qy=collections.deque(); qn=collections.deque(); lock=0.0
    for lc,pc,acc in zip(g.lc.values,g.pc.values,g.acc.values):
        q,o=(qy,qn) if lc=='YES' else (qn,qy); rem=acc
        while rem>1e-9 and o:
            a=o[0]; mm=min(rem,a[1]); lock+=mm*(1-a[0]-pc); rem-=mm; a[1]-=mm
            if a[1]<=1e-9: o.popleft()
        if rem>1e-9: q.append([pc,rem])
    return avg,lock,best
res=collections.defaultdict(lambda:np.zeros(6))
for d in DAYS:
    S=pd.read_csv(RG+f'r12_sim_{d}.csv.gz'); S=S[S['var']=='V2B'].sort_values('t'); S['agente']='SIM'
    Rr=pd.read_csv(RG+f'r12_real_{d}.csv.gz'); Rr=Rr.sort_values('ts_est'); Rr['agente']=Rr.maker.str[:10]
    for A in (S,Rr):
        for (ag,mid),g in A.groupby(['agente','mid']):
            a,f,b=conv(g); tot=g.pnl.sum(); 
            v=res[ag]; v+=[a,f,b,tot,g.coste.sum(),g.reb.sum()]
print('agente | coste | EV total sin reb | reb | lock AVG | lock FIFO | lock BEST (por EUR) | residuo AVG | FIFO | BEST')
for ag,v in res.items():
    a,f,b,t,c,r=v; print(f'{ag} | {c:,.0f} | {t/c:+.4f} | {r/c:+.4f} | {a/c:+.4f} | {f/c:+.4f} | {b/c:+.4f} | {(t-a)/c:+.4f} | {(t-f)/c:+.4f} | {(t-b)/c:+.4f}')
