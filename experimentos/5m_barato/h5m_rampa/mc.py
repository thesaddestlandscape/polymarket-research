# MC de la rampa H5M/H35 (solo lectura; base = dataset de colocación, política H35 ETH k2/SOL k1/XRP k1, CONS, 5 acc)
import pandas as pd,glob,numpy as np,sys,json
rng=np.random.default_rng(20261019)
fs=sorted(glob.glob('/root/polymarket-research-datalogs/m5_maker_colocacion/base_*.csv.gz'))
D=pd.concat([pd.read_csv(f) for f in fs],ignore_index=True)
sel={'ETH':'DEEP_k2|C0|CONS|5','SOL':'DEEP_k1|C0|CONS|5','XRP':'DEEP_k1|C0|CONS|5'}
H=pd.concat([D[(D.act==a)&(D.motor==m)] for a,m in sel.items()])
f=H[H.lleno>0].copy()
EV_EMP=f.pnl.sum()/f.coste.sum()
dias=sorted(f.dia.unique())
# clusters por cierre dentro de cada día
CL={d:[g[['pnl','coste']].values for _,g in f[f.dia==d].groupby('fin_s')] for d in dias}
W={d:len(CL[d]) for d in dias}
print('EV emp',round(EV_EMP,4),'fills',len(f),'dias',len(dias))
def camino(N,fpd,S,ev):
    """devuelve arrays pnl, coste de N rellenos; bloques de 'fpd' rellenos por día de la rampa, cada uno de un día fuente al azar"""
    P=[];C=[];n=0
    while n<N:
        d=dias[rng.integers(len(dias))]; m=0
        while m<fpd and n<N:
            c=CL[d][rng.integers(W[d])]
            for p,co in c:
                P.append(p);C.append(co);n+=1;m+=1
    P=np.array(P[:N])*S/5;C=np.array(C[:N])*S/5
    P=P-(EV_EMP-ev)*C
    return P,C
def sim(N,fpd,S,ev,R=4000,caps=(),naive=True):
    fin=np.empty(R);dd=np.empty(R);trig={c:0 for c in caps};nv=0;turn=np.empty(R)
    for r in range(R):
        P,C=camino(N,fpd,S,ev);cum=np.cumsum(P)
        fin[r]=cum[-1];dd[r]=-min(0,cum.min());turn[r]=C.sum()
        for c in caps:
            if cum.min()<=-c: trig[c]+=1
        if naive:
            # kill secuencial naif: tras cada relleno con n>=20, media acumulada por € <0
            cc=np.cumsum(C); k=np.arange(1,N+1)
            if np.any((k>=20)&(cum/cc<0)): nv+=1
    return dict(N=N,S=S,ev=ev,turn=round(turn.mean(),1),E=round(fin.mean(),2),sd=round(fin.std(),2),P_neg=round((fin<0).mean(),3),
                P5=round(np.percentile(fin,5),2),P50=round(np.percentile(fin,50),2),DD95=round(np.percentile(dd,95),2),DD50=round(np.percentile(dd,50),2),
                trig={c:round(v/R,3) for c,v in trig.items()},naive=round(nv/R,3))
def cap_q(N,fpd,S,ev=0.05,q=0.05,R=4000):
    dd=[]
    for r in range(R):
        P,C=camino(N,fpd,S,ev);cum=np.cumsum(P);dd.append(-min(0,cum.min()))
    return float(np.percentile(dd,100*(1-q)))
out=[]
PELD=[('R1 H47-B',70,100,5),('R2 5acc ext',300,150,5),('R3 10acc',300,150,10),('R4 25acc',300,150,25),('R5 50acc',300,150,50)]
for nom,N,fpd,S in PELD:
    c=cap_q(N,fpd,S)
    res=[]
    for ev in (EV_EMP,0.05,0.003,0.0,-0.05,-0.10):
        r=sim(N,fpd,S,ev,R=3000,caps=(round(c,1),),naive=True);res.append(r)
    out.append(dict(peldano=nom,cap_5pct_bajo_EV005=round(c,1),res=res))
    print(nom,'cap',round(c,1))
    for r in res: print('  ',r)
# suelo de saldo H47-B (dedicada 19,59, suelo 12): con autoredención inmediata -> parada si cum <= -6,5; sin redención -> rellenos hasta agotar
for ev in (EV_EMP,0.05,0.0,-0.10):
    st=0;nst=[]
    for r in range(3000):
        P,C=camino(70,100,5,ev);cum=np.cumsum(P);idx=np.where(cum<=-6.5)[0]
        if len(idx): st+=1;nst.append(idx[0]+1)
    print('suelo autoredencion ev',round(ev,3),'P(parada antes de 70 rellenos)',round(st/3000,3),'mediana relleno de parada',np.median(nst) if nst else None)
print('sin redencion: rellenos hasta suelo ~', round(7.59/f.coste.mean(),1))
json.dump(out,open('mc_out.json','w'),default=float,indent=1)
