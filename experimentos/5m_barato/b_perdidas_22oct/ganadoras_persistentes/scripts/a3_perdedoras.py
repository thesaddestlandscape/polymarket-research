#!/usr/bin/env python3
"""ADENDA2: R6 perdedoras persistentes como filtro, R2-controles, perfil INV vs B, rango ballenas_timing_history 5m."""
import pandas as pd,numpy as np,sys,os
sys.path.insert(0,os.path.dirname(__file__)); import comun; from comun import *
BW='0x659a40ff9920febc5a66836213040924343d297f'
F,cob=carga_banda(); A2C=comun.WMAP; BC=A2C.get(BW,-1)
U=F.groupby(['w','dia','mid','lc','fin'],observed=True)[['pnl','coste']].sum().reset_index()
Gc=U.groupby(['w','dia','fin'])['pnl'].sum().reset_index(); Gc['q']=Gc.pnl**2
G=U.groupby(['w','dia']).agg(S=('pnl','sum'),C=('coste','sum'),N=('pnl','size')).reset_index().merge(Gc.groupby(['w','dia'])['q'].sum().reset_index(),on=['w','dia'])
del U,Gc
def elig(dias):
    g=G[G.dia.isin(dias)]
    a=g.groupby('w').agg(S=('S','sum'),C=('C','sum'),N=('N','sum'),Q=('q','sum'),nd=('dia','nunique'),pos=('S',lambda s:(s>0).sum())).reset_index()
    e=a[(a.N>=20)&(a.nd>=3)&(a.C>=100)].copy(); e['z']=e.S/np.sqrt(e.Q.clip(lower=1e-12)); e['ev']=e.S/e.C
    e['R']=(e.z>=2)&(e.ev>0)&(e.pos>=0.6*e.nd); e['INV']=(e.z<=-2)&(e.ev<0); return e
F['cel']=(F.coin.astype(np.int32)*1000+(F.sec//60).astype(np.int32)*10+((F.pc-0.05)//0.05).clip(0,4).astype(np.int32))
def delta(rows,tag,q=(5,95)):
    df=pd.DataFrame(rows,columns=['d','S1','C1','S2','C2']); ok=(df.C1>0)&(df.C2>0); df=df[ok]
    ev1=df.S1.sum()/df.C1.sum(); ev2=df.S2.sum()/df.C2.sum(); rng=np.random.default_rng(3); n=len(df); bs=[]
    for _ in range(4000):
        i=rng.integers(0,n,n); bs.append(df.S1.values[i].sum()/df.C1.values[i].sum()-df.S2.values[i].sum()/df.C2.values[i].sum())
    dd=(df.S1/df.C1-df.S2/df.C2).values; o=np.argsort(-dd)[2:]
    print(f'{tag}: A {ev1:+.4f} (coste {df.C1.sum():.0f}) B {ev2:+.4f} (coste {df.C2.sum():.0f}) Δ {ev1-ev2:+.4f} IC90d ({np.percentile(bs,5):+.4f},{np.percentile(bs,95):+.4f}) IC98,75 ({np.percentile(bs,0.625):+.4f},{np.percentile(bs,99.375):+.4f}) sin2 {df.S1.values[o].sum()/df.C1.values[o].sum()-df.S2.values[o].sum()/df.C2.values[o].sum():+.4f} días Δ>0 {int((dd>0).sum())}/{n}',flush=True)
r6={k:[] for k in ['all','mk','tk','opp']}; rc={k:[] for k in ['R2','pop','evpos','inv']}; prof=[]; celdasR2={}
for d in range(7,16):
    W=list(range(d-7,d)); e=elig(W); R=set(e.w[e.R]); I=set(e.w[e.INV]); X=F[F.dia==d]; WF=F[F.dia.isin(W)]
    P=X[(X.rol==0)&~X.w.isin(R|I)][['mid','lc','ts','pnl','coste','cel']].copy()
    for k,sel in (('all',X.w.isin(I)),('mk',X.w.isin(I)&(X.rol==0)),('tk',X.w.isin(I)&(X.rol==1))):
        t0=X[sel].groupby(['mid','lc']).ts.min()
        f=(P.ts-5>=t0.reindex(pd.MultiIndex.from_arrays([P.mid,P.lc])).values)
        r6[k].append((d,P.pnl[~f].sum(),P.coste[~f].sum(),P.pnl.sum(),P.coste.sum()))
        if k=='all':
            fo=(P.ts-5>=t0.reindex(pd.MultiIndex.from_arrays([P.mid,1-P.lc])).values)
            r6['opp'].append((d,P.pnl[fo].sum(),P.coste[fo].sum(),P.pnl[~fo].sum(),P.coste[~fo].sum()))
            prof.append((d,f.mean(),P.coste[f].sum()/P.coste.sum()))
    Pall=X[(X.rol==0)&~X.w.isin(R)]
    def cells_cov(Wsub):
        c=Wsub.groupby('cel').coste.sum().sort_values(ascending=False); return set(c.index[(c.cumsum()/c.sum()).values<=0.5])|{c.index[0]}
    cR=cells_cov(WF[(WF.rol==0)&WF.w.isin(R)]); celdasR2[DIAS[d]]=sorted(cR)
    wm=WF[WF.rol==0]; ce=wm.groupby('cel').apply(lambda g:g.pnl.sum()/g.coste.sum()).sort_values(ascending=False)
    for k,cs in (('R2',cR),('pop',cells_cov(wm)),('evpos',set(ce.index[:len(cR)])),('inv',cells_cov(WF[(WF.rol==0)&WF.w.isin(I)]))):
        inn=Pall[Pall.cel.isin(cs)]; rc[k].append((d,inn.pnl.sum(),inn.coste.sum(),Pall.pnl.sum(),Pall.coste.sum()))
print('######## R6 perdedoras persistentes (INV) como filtro de B-maker (pobl. maker banda, sin INV/roster)')
print('fracción de fills/coste con INV previo mismo lado por día:',[(DIAS[d][5:],round(a,3),round(b,3)) for d,a,b in prof])
delta(r6['all'],'R6 mantener solo sin INV previo mismo lado (A) vs todo (B)')
delta(r6['mk'],'R6-mk (INV-makers) sin flag vs todo')
delta(r6['tk'],'R6-tk (INV-tomadoras, solapa contrapunto) sin flag vs todo')
delta(r6['opp'],'R6o INV previo lado OPUESTO (A) vs no (B)')
print('######## R2 controles (celdas; pobl. maker banda en celdas vs toda)')
for k in rc: delta(rc[k],f'celdas {k}')
print('celdas R2 (moneda*1000+min*10+bucket5c) ej. 2026-10-21:',celdasR2['2026-10-21'][:40])
# perfil INV vs roster vs B (ventana 14..20 => dia 15)
e=elig(list(range(8,15)))
for nm,ws in (('INV',e.w[e.INV]),('R',e.w[e.R]),('todos_elegibles',e.w)):
    Y=F[F.dia.isin(range(8,15))&F.w.isin(set(ws))]
    print(f'perfil {nm} (n={len(set(ws))}): coste {Y.coste.sum():.0f} fM {Y.coste[Y.rol==0].sum()/Y.coste.sum():.2f} pc_med {np.average(Y.pc,weights=Y.coste):.3f} sec_med {np.average(Y.sec,weights=Y.coste):.0f} frac<0,10 {Y.coste[Y.pc<0.10].sum()/Y.coste.sum():.2f} frac_sec>=240 {Y.coste[Y.sec>=240].sum()/Y.coste.sum():.2f} EV {Y.pnl.sum()/Y.coste.sum():+.4f}')
Bz=e[e.w==BC]; print('B en elegibles ventana 14-20:',Bz[['N','C','S','z','ev','INV']].to_dict('records') if len(Bz) else 'no elegible', '| B código', BC)
YB=F[F.w==BC]; 
if len(YB): print(f'perfil B on-chain banda: coste {YB.coste.sum():.0f} fM {YB.coste[YB.rol==0].sum()/YB.coste.sum():.2f} pc_med {np.average(YB.pc,weights=YB.coste):.3f} sec_med {np.average(YB.sec,weights=YB.coste):.0f} EV {YB.pnl.sum()/YB.coste.sum():+.4f} días {sorted(YB.dia.unique().tolist())}')
H=pd.read_csv('/root/polymarket-research/data/shadow/ballenas_timing_history.csv',usecols=['marco','ts_trade','precio'])
h=H[H.marco=='5m']; print('ballenas_timing_history 5m: filas',len(h),'rango',h.ts_trade.min(),h.ts_trade.max(),'banda',((h.precio>=0.05)&(h.precio<=0.30)).sum())
