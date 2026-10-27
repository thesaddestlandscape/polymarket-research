#!/usr/bin/env python3
"""ADENDA1: S1-R / S1-T, test poblacional, S2 roles, S3 R1-R5 + skill, S4 ballenas no circular."""
import pandas as pd,numpy as np,sys,os,json,glob
from scipy.stats import norm
sys.path.insert(0,os.path.dirname(__file__)); import comun; from comun import *
F,cob=carga_banda(); INV=np.array(list(comun.WMAP.keys()),dtype=object); A2C=comun.WMAP
print('fills',len(F),'cob',cob,flush=True)
U=F.groupby(['w','dia','mid','lc','fin'],observed=True)[['pnl','coste']].sum().reset_index()
Gc=U.groupby(['w','dia','fin'])['pnl'].sum().reset_index(); Gc['q']=Gc.pnl**2
G=U.groupby(['w','dia']).agg(S=('pnl','sum'),C=('coste','sum'),N=('pnl','size')).reset_index().merge(Gc.groupby(['w','dia'])['q'].sum().reset_index(),on=['w','dia'])
del U,Gc
def elig(dias):
    g=G[G.dia.isin(dias)]
    a=g.groupby('w').agg(S=('S','sum'),C=('C','sum'),N=('N','sum'),Q=('q','sum'),nd=('dia','nunique'),pos=('S',lambda s:(s>0).sum())).reset_index()
    e=a[(a.N>=20)&(a.nd>=3)&(a.C>=100)].copy(); e['z']=e.S/np.sqrt(e.Q.clip(lower=1e-12)); e['ev']=e.S/e.C
    e['R']=(e.z>=2)&(e.ev>0)&(e.pos>=0.6*e.nd); e['INV']=(e.z<=-2)&(e.ev<0)
    k=max(5,int(round(0.01*len(e)))); e['T']=e.w.isin(e.nlargest(k,'z').w); return e
# ---- roles: features por (w,dia) desde R_D.pkl
def feats_dia(i):
    R=pd.read_pickle(O+f'R_{DIAS[i]}.pkl'); R['w']=R.w.astype(str).map(A2C); R=R[R.w.notna()]; R['w']=R.w.astype(np.int64)
    R['pr']=R.coste/R.acc
    t=R.groupby('w').coste.sum().rename('tot'); m=R[R.rol==0].groupby('w').coste.sum().rename('M'); v=R[R.v==1].groupby('w').coste.sum().rename('V')
    l=R[R.pr<0.30].groupby('w').coste.sum().rename('L')
    b=R[R.v==0].groupby(['w','mid','tok']).acc.sum().unstack('tok')
    b=b.dropna(); bal=(b.min(1)/b.max(1)).rename('bal')
    cm=R.groupby(['w','mid']).coste.sum().rename('cm')
    pm=cm.to_frame().join(bal,how='inner'); pm['cb']=pm.cm*pm.bal
    p=pm.groupby('w')[['cm','cb']].sum().rename(columns={'cm':'P','cb':'PB'})
    X=pd.concat([t,m,v,l,p],axis=1).fillna(0); X['dia']=i; return X.reset_index()
FE=pd.concat([feats_dia(i) for i in range(len(DIAS))],ignore_index=True); print('feats',len(FE),flush=True)
def rol(ws,dias):
    x=FE[FE.dia.isin(dias)&FE.w.isin(ws)].groupby('w')[['tot','M','V','L','P','PB']].sum()
    fM=x.M/x.tot; fV=x.V/x.tot; fP=x.P/x.tot; fL=x.L/x.tot; bal=x.PB/x.P.clip(lower=1e-9)
    r=pd.Series('maker_pasivo',index=x.index)
    r[(fM>=0.5)&(fP<0.5)&(fL>=0.5)]='holder_longshots'
    r[(fM>=0.5)&(fP>=0.5)]=np.where(bal[(fM>=0.5)&(fP>=0.5)]>=0.6,'acumulador_pares','maker_ambos_lados')
    r[fM<0.5]='tomador_sniper'; r[fV>=0.25]='gestor_salidas'
    return r
def resumen(tag,rows):
    df=pd.DataFrame(rows,columns=['d','S','C','n']);
    if df.C.sum()==0: print(tag,'sin datos'); return
    print(f'{tag}: EV€ {df.S.sum()/df.C.sum():+.4f} IC90d {boot_dias(df.S,df.C)} sin2 {sin_mejores(df.S,df.C):+.4f} días+ {(df.S>0).sum()}/{(df.C>0).sum()} n_unid {int(df.n.sum())} coste {df.C.sum():.0f} pnl {df.S.sum():+.0f}',flush=True)
rng=np.random.default_rng(11)
SETS={}
for nombre,pruebas,ventana in [('WF',range(7,16),lambda d:list(range(d-7,d))),('SPLIT',range(8,16),lambda d:list(range(0,8)))]:
    print(f'\n######## {nombre}')
    acc={k:[] for k in ['R','T','INV']}; pl=np.zeros((200,2)); roles={}; wc={}; pobl=[]
    for d in pruebas:
        e=elig(ventana(d)); el=e.w.values; gd=G[G.dia==d].set_index('w')
        pobl.append((DIAS[d],len(e),int((e.z>=2).sum()),int((e.z<=-2).sum()),round(0.0228*len(e),1)))
        for k in acc:
            ws=e.w[e[k]].values; x=gd.reindex(ws).dropna(); acc[k].append((d,x.S.sum(),x.C.sum(),x.N.sum()))
            if k=='R':
                for w,c in zip(x.index,x.C): wc[w]=wc.get(w,0)+c
        nR=int(e.R.sum())
        for r in range(200):
            x=gd.reindex(rng.choice(el,nR,replace=False)).dropna(); pl[r]+=[x.S.sum(),x.C.sum()]
        rr=rol(e.w[e.R].values,ventana(d)); 
        for w,ro in rr.items():
            x=gd.reindex([w]).dropna()
            roles.setdefault(ro,[]).append((d,x.S.sum(),x.C.sum(),x.N.sum()) if len(x) else (d,0,0,0))
        SETS[(nombre,d)]=(set(e.w[e.R]),rr)
    print('test poblacional (dia, elegibles, z>=2, z<=-2, esperado H0 por cola):',pobl)
    for k in acc: resumen(f'  roster {k}',acc[k])
    evR=sum(a[1] for a in acc['R'])/max(sum(a[2] for a in acc['R']),1e-9); plev=pl[:,0]/np.maximum(pl[:,1],1e-9)
    print(f'  placebo (mismo tamaño que R): media {plev.mean():+.4f} p95 {np.percentile(plev,95):+.4f} p(plac>=R) {(plev>=evR).mean():.3f}; top1 wallet R {max(wc.values())/sum(wc.values()):.3f} ({INV[max(wc,key=wc.get)][:10]})')
    for ro,rows in sorted(roles.items()):
        agg={}
        for d,S,C,n in rows: a=agg.setdefault(d,[d,0,0,0]); a[1]+=S;a[2]+=C;a[3]+=n
        resumen(f'  rol {ro:18s} (wallet-días {len(rows)})',list(agg.values()))
pd.to_pickle({k:(list(v[0]),v[1].to_dict()) for k,v in SETS.items()},O+'sets.pkl')
# ---- S3 sobre WF
print('\n######## S3 relaciones (roster R walk-forward, días 13-21)')
F['cel']=(F.coin.astype(np.int32)*1000+(F.sec//60).astype(np.int32)*10+((F.pc-0.05)//0.05).clip(0,4).astype(np.int32))
r2={0:[],1:[]}; sk={0:[],1:[]}; r4=[]; r1=[]
for d in range(7,16):
    R,rr=SETS[('WF',d)]; W=F[F.dia.isin(range(d-7,d))&F.w.isin(R)]; X=F[F.dia==d]
    for ro in (0,1):
        c=W[W.rol==ro].groupby('cel').coste.sum().sort_values(ascending=False)
        if c.sum()==0: continue
        cells=set(c.index[(c.cumsum()/c.sum()).values<=0.5])|{c.index[0]}
        P=X[(X.rol==ro)&~X.w.isin(R)]; inn=P[P.cel.isin(cells)]
        r2[ro].append((d,inn.pnl.sum(),inn.coste.sum(),P.pnl.sum(),P.coste.sum()))
        Rf=X[(X.rol==ro)&X.w.isin(R)]
        if len(Rf):
            evc=P.groupby('cel').apply(lambda g:g.pnl.sum()/g.coste.sum()); rc=Rf.groupby('cel')[['pnl','coste']].sum().join(evc.rename('evp'),how='inner')
            sk[ro].append((d,rc.pnl.sum(),rc.coste.sum(),(rc.coste*rc.evp).sum()))
    # R4/R5: población maker vs roster-maker previo en (m,s) / (m,1-s)
    RM=X[(X.rol==0)&X.w.isin(R)].groupby(['mid','lc']).ts.min()
    P=X[(X.rol==0)&~X.w.isin(R)][['mid','lc','ts','pnl','coste']].copy()
    P['t0']=RM.reindex(pd.MultiIndex.from_arrays([P.mid,P.lc])).values
    P['t1']=RM.reindex(pd.MultiIndex.from_arrays([P.mid,1-P.lc])).values
    P['f4']=(P.ts-5>=P.t0).fillna(False); P['f5']=(P.ts-5>=P.t1).fillna(False)
    r4.append((d,)+tuple(v for m in (P.f4,~P.f4,P.f5,~P.f5) for v in (P.pnl[m].sum(),P.coste[m].sum()))+(P.pnl.sum(),P.coste.sum()))
    # R1: copia de roster-tomador al print tomador siguiente >=2 s
    RT=X[(X.rol==1)&X.w.isin(R)].sort_values('ts').groupby(['mid','lc']).first().reset_index()[['mid','lc','ts','pnl','coste']]
    if len(RT):
        Q=X[(X.rol==1)].sort_values('ts')[['mid','lc','ts','pnl','coste','w']]
        RT['ts2']=RT.ts+2; RT=RT.sort_values('ts2')
        m=pd.merge_asof(RT,Q.rename(columns={'ts':'tq','pnl':'pq','coste':'cq'}),left_on='ts2',right_on='tq',by=['mid','lc'],direction='forward',tolerance=28)
        m=m[m.tq.notna()]; r1.append((d,m.pnl.sum(),m.coste.sum(),m.pq.sum(),m.cq.sum(),len(RT),len(m)))
def delta(rows,a,b,c,dd,tag):
    df=pd.DataFrame(rows); S1,C1,S2,C2=df[a],df[b],df[c],df[dd]
    ev1=S1.sum()/C1.sum(); ev2=S2.sum()/C2.sum(); rng=np.random.default_rng(3); n=len(df); bs=[]
    for _ in range(2000):
        i=rng.integers(0,n,n); bs.append(S1.values[i].sum()/C1.values[i].sum()-S2.values[i].sum()/C2.values[i].sum())
    o=np.argsort(-(S1/C1-S2/C2).values)[2:]
    print(f'{tag}: EV€ A {ev1:+.4f} (coste {C1.sum():.0f}) vs B {ev2:+.4f} (coste {C2.sum():.0f}) Δ {ev1-ev2:+.4f} IC90d ({np.percentile(bs,5):+.4f},{np.percentile(bs,95):+.4f}) Δ sin2 {S1.values[o].sum()/C1.values[o].sum()-S2.values[o].sum()/C2.values[o].sum():+.4f} días Δ>0 {int(((S1/C1-S2/C2)>0).sum())}/{n}')
for ro,nm in ((0,'R2 celdas maker (pobl. en celdas roster vs toda banda maker)'),(1,'R3 celdas tomador')):
    if r2[ro]: delta(r2[ro],1,2,3,4,nm)
for ro,nm in ((0,'skill maker roster vs pobl. mismas celdas'),(1,'skill tomador roster vs pobl. mismas celdas')):
    if sk[ro]:
        df=pd.DataFrame(sk[ro]); print(f'{nm}: EV roster {df[1].sum()/df[2].sum():+.4f} vs esperado celdas {df[3].sum()/df[2].sum():+.4f} (coste {df[2].sum():.0f}); por día {[round((a-c)/b,3) for _,a,b,c in sk[ro]]}')
delta(r4,1,2,3,4,'R4 maker pobl. con roster-maker previo mismo lado (A) vs sin (B)')
delta(r4,5,6,9,10,'R5 regla cancelar si roster-maker previo lado opuesto: mantener (A=sin opuesto) vs todo (B)')
delta(r4,5,6,7,8,'R5b con opuesto (A) vs sin opuesto (B)')
if r1:
    df=pd.DataFrame(r1); print(f'R1 copia tomador: unidades roster {df[5].sum()} con print siguiente {df[6].sum()} | EV roster (sus fills) {df[1].sum()/df[2].sum():+.4f} | EV copia print>=2s {df[3].sum()/df[4].sum():+.4f} IC90d {boot_dias(df[3],df[4])} coste copia {df[4].sum():.0f}')
# ---- S4 ballenas_timing_history, solo filas < 14-Oct
print('\n######## S4 ballenas_timing_history (ts<2026-10-14, 5m, precio 0,05-0,30)')
P=[]
for ch in pd.read_csv('/root/polymarket-research/data/shadow/ballenas_timing_history.csv',usecols=['marco','ts_trade','wallet','precio','acierto'],chunksize=1000000):
    ch=ch[(ch.marco=='5m')&(ch.precio>=0.05)&(ch.precio<=0.30)&(ch.ts_trade<'2026-10-14')]; P.append(ch)
H=pd.concat(P); print('filas',len(H),'rango',H.ts_trade.min(),H.ts_trade.max())
a=H.groupby('wallet').agg(n=('acierto','size'),hit=('acierto','mean'),pr=('precio','mean')); a=a[a.n>=20]
bp=[w for w in a.index[(a.hit-a.pr)>=0.05] if w in A2C]; base=[w for w in a.index if w in A2C]
bc=[A2C[w] for w in bp]; basec=[A2C[w] for w in base]
rows=[]
for d in range(8,16):
    gd=G[G.dia==d].set_index('w'); x=gd.reindex(bc).dropna(); rows.append((d,x.S.sum(),x.C.sum(),x.N.sum()))
print(f'BH_pre {len(bp)} wallets (de {len(a)} con n>=20; {len(base)} en on-chain)'); resumen('  BH_pre on-chain 14-21',rows)
pl=[]
for r in range(200):
    s=rng.choice(basec,len(bc),replace=False); S=C=0
    for d in range(8,16):
        x=G[(G.dia==d)&G.w.isin(s)]; S+=x.S.sum(); C+=x.C.sum()
    pl.append(S/max(C,1e-9))
ev=sum(r[1] for r in rows)/max(sum(r[2] for r in rows),1e-9); print(f'  placebo media {np.mean(pl):+.4f} p95 {np.percentile(pl,95):+.4f} p {(np.array(pl)>=ev).mean():.3f}')
# solape (circular) con wallet_edge_score_por_marco
we=json.load(open('/root/polymarket-research/data/shadow/wallet_edge_score_por_marco.json'))
w5={v['wallet'] for v in we.values() if isinstance(v,dict) and v.get('marco') in ('5m','5min')}
allR=set().union(*[SETS[('WF',d)][0] for d in range(7,16)]); allRa={INV[w] for w in allR}
print(f'solape roster WF ({len(allRa)} wallets únicas) con wallet_edge_score 5m ({len(w5)}): {len(allRa&w5)} [CIRCULAR, descriptivo]')
pd.Series(sorted(allRa)).to_csv(O+'roster_WF_wallets.csv',index=False)
