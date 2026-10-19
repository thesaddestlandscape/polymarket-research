import pandas as pd,numpy as np,json,csv,gzip
SP='/tmp/claude-0/-root-polymarket-research/ce552a77-92f9-49c1-8c13-d01ef139d7f6/scratchpad/'
F=pd.read_pickle(SP+'F_all.pkl')
F=F[F.act=='BTC'].sort_values(['dia','mkt','lado_c','ts'],kind='stable')
def unidades(F,OFF=5000.0,K=50.0,TMAX=270.0):
    out={}
    for (dia,mkt,lado),x in F.groupby(['dia','mkt','lado_c'],sort=False):
        cum=0.0
        for ts,acc,coste,T,pnl in zip(x.ts.values,x.acc.values,x.coste.values,x['T'].values,x.pnl.values):
            cum0,cum=cum,cum+acc
            lo,hi=max(cum0-OFF,0),max(cum0+acc-OFF,0)
            tk=max(min(K,hi)-min(K,lo),0)
            if tk<=0 or not (60<T<=TMAX): continue
            f=tk/acc
            u=out.setdefault((dia,mkt,lado),{'dia':dia,'fin':round((ts+T)/300)*300,'c':0.0,'p':0.0,'acc':0.0})
            u['c']+=coste*f;u['p']+=pnl*f;u['acc']+=acc*f
    return pd.DataFrame(list(out.values()))
def reportar(U,nombre):
    c=U.c.sum();p=U.p.sum()
    print(nombre,'unidades',len(U),'días',U.dia.nunique(),'coste',round(c,1),'EV pond',round(p/c,4),'EV por unidad',round((U.p/U.c).mean(),4),'px medio',round(c/U.acc.sum(),3))
U=unidades(F)
print('REPRODUCCIÓN (mis fills on-chain, fuente distinta a pass1):')
for d,x in U.groupby('dia'): print(' ',d,len(x),round(x.c.sum(),1),round(x.p.sum()/x.c.sum(),3),'acierto unidades',round((x.p>0).mean(),3))
reportar(U[U.dia<='2026-10-16'],'IN-SAMPLE 09-16 (8 días; el descriptivo original era 06-16)')
reportar(U[U.dia>='2026-10-17'],'FORWARD 17-18')
U.to_pickle(SP+'R5K_U.pkl')
