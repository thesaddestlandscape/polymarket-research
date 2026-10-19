# MC2: (a) P(completar H47-B ~70 rellenos) según presupuesto disponible sobre el suelo; (b) P2 1.000 rellenos: tope catastrófico
# y regla secuencial por miradas (250/500/1000) con IC por días; vectorizado por bloques. Solo lectura.
import pandas as pd,glob,numpy as np
rng=np.random.default_rng(1910)
fs=sorted(glob.glob('/root/polymarket-research-datalogs/m5_maker_colocacion/base_*.csv.gz'))
D=pd.concat([pd.read_csv(f) for f in fs],ignore_index=True)
sel={'ETH':'DEEP_k2|C0|CONS|5','SOL':'DEEP_k1|C0|CONS|5','XRP':'DEEP_k1|C0|CONS|5'}
H=pd.concat([D[(D.act==a)&(D.motor==m)] for a,m in sel.items()])
f=H[H.lleno>0].copy();EV=f.pnl.sum()/f.coste.sum()
dias=sorted(f.dia.unique())
CL={d:[g[['pnl','coste']].values for _,g in f[f.dia==d].groupby('fin_s')] for d in dias}
def camino(N,fpd,ev):
    P=[];C=[];DI=[];n=0;k=0
    while n<N:
        d=dias[rng.integers(len(dias))];m=0
        while m<fpd and n<N:
            c=CL[d][rng.integers(len(CL[d]))]
            for p,co in c: P.append(p);C.append(co);DI.append(k);n+=1;m+=1
        k+=1
    P=np.array(P[:N]);C=np.array(C[:N]);DI=np.array(DI[:N])
    return P-(EV-ev)*C,C,DI
# (a) presupuesto disponible B = saldo - suelo - exposición viva (~3 órdenes*1,02)
print('(a) H47-B 70 rellenos, P(completar) por presupuesto efectivo B (autoredención al cierre)')
for ev in (EV,0.05,0.0,-0.10):
    row=[]
    for B in (4.5,7.6,12,20,30,40):
        ok=0
        for r in range(2000):
            P,C,_=camino(70,100,ev)
            if np.cumsum(P).min()>-B: ok+=1
        row.append((B,round(ok/2000,3)))
    print(' ev',round(ev,3),row)
# (b) P2: 1000 rellenos, 150/día; miradas a 250/500/1000 rellenos: parar si cota sup. IC90 (bootstrap por días de la rampa) del EV ponderado < 0
def ic_sup(P,C,DI,B=300):
    ud=np.unique(DI);pd_=np.array([P[DI==u].sum() for u in ud]);cd=np.array([C[DI==u].sum() for u in ud])
    idx=rng.integers(len(ud),size=(B,len(ud)));e=pd_[idx].sum(1)/cd[idx].sum(1)
    return np.percentile(e,95),np.percentile(e,5),pd_.sum()/cd.sum()
print('(b) P2 5 acc, 1000 rellenos (150/día ≈ 7 días)')
for ev in (EV,0.05,0.0,-0.05,-0.10):
    stop=0;dd=[];fin=[];lo_ok=0
    for r in range(800):
        P,C,DI=camino(1000,150,ev);cum=np.cumsum(P);dd.append(-min(0,cum.min()));fin.append(cum[-1])
        parado=False
        for L in (250,500,1000):
            s,l,e=ic_sup(P[:L],C[:L],DI[:L])
            if s<0: parado=True;break
        stop+=parado
        s,l,e=ic_sup(P,C,DI)
        lo_ok+= (l>0)
    dd=np.array(dd);fin=np.array(fin)
    print(' ev',round(ev,3),'P(parar por miradas)',round(stop/800,3),'P(IC90 inf>0 a 1000)',round(lo_ok/800,3),'E',round(fin.mean(),1),'sd',round(fin.std(),1),'P5',round(np.percentile(fin,5),1),'DD95',round(np.percentile(dd,95),1),'DD90',round(np.percentile(dd,90),1))
# rellenos necesarios para IC90 inf > 0 con prob 80% si EV real = +0,064 (OOS) : aprox con se por relleno
r=(f.pnl/f.coste);print('sd por € por relleno',round(r.std(),3))
