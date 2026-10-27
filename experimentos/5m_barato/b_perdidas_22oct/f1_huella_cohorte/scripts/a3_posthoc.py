#!/usr/bin/env python3
"""a3: POST-HOC (EXPLORATORY, declarado tras ver a1/a2): (1) rasgos binarios que a1 no pudo testear; (2) banda de precio de la unidad maker: EV por dia/moneda/cierre, calibracion, concentracion; (3) estratos volumen x precio; (4) estandarizacion por banda."""
import sys; sys.path.insert(0,'.')
import lib
from lib import *
rng=np.random.default_rng(4242)
out=open(D+'a3_resultados.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s,flush=True); out.write(s+'\n')
pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',200)
COLS=['maker','rolM','coin','dia','yes','coste','pcw','des_yes','acc','fee','n','fin']
U=outcome(load(DESC+HOLD,cols=COLS)); U=U[U.rolM].copy(); U['pcm']=U.pcw/U.coste
U['win']=((U.yes.values)==(U.des_yes.values==1)); U['accw']=U.acc*U.win
EDG=[0,0.05,0.10,0.20,0.30,0.50,0.70,0.90,1.0]; U['banda']=np.clip(np.digitize(U.pcm.values,EDG)-1,0,7)
BN=['<.05','.05-.10','.10-.20','.20-.30','.30-.50','.50-.70','.70-.90','>=.90']
# ---- (2) banda
P('=== (2) Banda de precio de la unidad maker (rol M), calibracion y robustez. EV=Σpnl/Σcoste; reb separado')
for nm,days in [('DESC',DI),('HOLD',HI)]:
    X=U[U.dia.isin(days)]
    for g,Y in [('BTC',X[X.coin==0]),('ALT',X[X.coin>0])]:
        r=Y.groupby('banda').apply(lambda z: pd.Series(dict(coste=z.coste.sum(),EV=z.pnl.sum()/z.coste.sum(),EVreb=(z.pnl.sum()+z.reb.sum())/z.coste.sum(),precio=z.pcw.sum()/z.coste.sum(),acierto_acc=z.accw.sum()/z.acc.sum(),n=len(z),makers=z.maker.nunique())))
        r.index=BN; P(nm,g); P(r.round(4).to_string())
# robustez bandas .50-.70, .70-.90, >=.90 : por dia, cierre, wallet
def robust(Y,tag):
    pd_=Y.groupby('dia').apply(lambda z: z.pnl.sum()/z.coste.sum()); cd=Y.groupby('dia').coste.sum()
    # bootstrap por cierre (fin)
    g=Y.groupby('fin')[['pnl','coste']].sum(); idx=np.arange(len(g)); pn=g.pnl.values; cn=g.coste.values
    bs=[ ]
    for _ in range(1000):
        s=rng.integers(0,len(g),len(g)); bs.append(pn[s].sum()/cn[s].sum())
    dd=Y.groupby('dia')[['pnl','coste']].sum(); bd=[]
    for _ in range(3000):
        s=rng.integers(0,len(dd),len(dd)); bd.append(dd.pnl.values[s].sum()/dd.coste.values[s].sum())
    best=dd.pnl.nlargest(2).index; z=dd.drop(best); mk=Y.groupby('maker')[['pnl','coste']].sum()
    top=mk.coste.max()/mk.coste.sum()
    capw=np.minimum(mk.coste,0.3*mk.coste.sum()); evcap=(mk.pnl/mk.coste*capw).sum()/capw.sum()
    P('  %s: EV %.4f | dias+ %d/%d | IC90 por dias (%.4f,%.4f) | IC90 por cierre (%.4f,%.4f) n_cierres %d | sin 2 mejores dias %.4f | wallet top %.1f%% | EV con peso wallet<=30%% %.4f | coste/dia %.0f'%(tag,Y.pnl.sum()/Y.coste.sum(),(pd_>0).sum(),len(pd_),*np.percentile(bd,[5,95]),*np.percentile(bs,[5,95]),len(g),z.pnl.sum()/z.coste.sum(),100*top,evcap,Y.coste.sum()/len(dd)))
    return pd_
P('--- robustez')
for g,sel in [('BTC',lambda X:X.coin==0),('ALT',lambda X:X.coin>0)]:
    for b in [5,6,7]:
        for nm,days in [('DESC',DI),('HOLD',HI)]:
            Y=U[U.dia.isin(days)&sel(U)&(U.banda==b)]; robust(Y,f'{g} {BN[b]} {nm}')
    for nm,days in [('DESC',DI),('HOLD',HI)]:
        Y=U[U.dia.isin(days)&sel(U)&(U.banda.isin([4]))]; robust(Y,f'{g} {BN[4]} {nm}')
        Y=U[U.dia.isin(days)&sel(U)&(U.banda.isin([1,2,3]))]; robust(Y,f'{g} .05-.30 {nm}')
P('--- por dia (BTC, banda .70-.90 / .50-.70 / >=.90 / .05-.30)')
dd=pd.DataFrame({BN[b]:U[(U.coin==0)&(U.banda==b)].groupby('dia').apply(lambda z: z.pnl.sum()/z.coste.sum()) for b in [2,3,4,5,6,7]}); P(dd.round(3).to_string())
dd=pd.DataFrame({BN[b]:U[(U.coin>0)&(U.banda==b)].groupby('dia').apply(lambda z: z.pnl.sum()/z.coste.sum()) for b in [2,3,4,5,6,7]}); P('ALT'); P(dd.round(3).to_string())
# por tamaño de maker en banda 0.7-0.9 BTC: terciles de coste en el periodo
P('--- BTC banda .70-.90 y .05-.30: EV por tamano de maker (terciles de coste maker total en el periodo) y top-50')
for nm,days in [('DESC',DI),('HOLD',HI)]:
    X=U[U.dia.isin(days)&(U.coin==0)]; tot=X.groupby('maker').coste.sum(); q=tot.rank(pct=True); top50=set(tot.nlargest(50).index)
    X=X.assign(tam=np.where(X.maker.isin(top50),'top50',np.where(X.maker.map(q)>2/3,'T3',np.where(X.maker.map(q)>1/3,'T2','T1'))))
    for bs_,lab in [([6],'.70-.90'),([5],'.50-.70'),([7],'>=.90'),([1,2,3],'.05-.30'),([4],'.30-.50')]:
        Y=X[X.banda.isin(bs_)]; r=Y.groupby('tam').apply(lambda z: pd.Series(dict(coste=z.coste.sum(),EV=z.pnl.sum()/z.coste.sum(),EVreb=(z.pnl.sum()+z.reb.sum())/z.coste.sum(),makers=z.maker.nunique())))
        P(nm,lab); P(r.round(4).to_string())
del U
# ---- (1) binarios y (3) estratos con rasgos
U0=load(DESC+HOLD,cols=['maker','coste','rolM']); tot_=U0.groupby('maker').coste.sum(); keep=tot_.index[tot_>=200].values; del U0
UA=outcome(load(DESC+HOLD,keep=keep)); UD=UA[UA.dia.isin(DI)]; UH=UA[UA.dia.isin(HI)]
def agg(Uper,coinsel):
    if coinsel=='BTC': Uper=Uper[Uper.coin==0]
    elif coinsel=='ALT': Uper=Uper[Uper.coin>0]
    M=Uper[Uper.rolM]; g=M.groupby('maker')[['pnl','coste','reb']].sum(); return g
P('=== (1) rasgos binarios (post-hoc): grupos fijados con DESC, EV maker HOLD ponderado por €; placebo por permutacion de makers (2000), p marginal')
BIN={'r12_vent_simult':('>1',lambda v:v>1.0),'r13_monedas':('>1',lambda v:v>1),'r14_cuota_btc':('<1 (no solo BTC)',lambda v:v<0.999),'r18_ventas':('>0 (vende algo)',lambda v:v>0),'r19_ambos_lados':('>0.5 (cubre ambos lados)',lambda v:v>0.5),'r20_taker':('>0.2 (taker relevante)',lambda v:v>0.2),'r17_ord_unidad':('>=5 ordenes/unidad',lambda v:v>=5)}
for nm,(Ta,Tb,per_o,per_t) in {'FWD':(UD,None,UH,'HOLD'),'REV':(UH,None,UD,'DESC')}.items():
    for cs in ['BTC','ALT','ALL']:
        T=traits(Ta,cs); o=agg(per_o,cs); el=T.index[T.cost>=500].intersection(o.index[o.coste>=200]); T=T.loc[el]; o=o.loc[el]
        for r,(lab,f) in BIN.items():
            m=f(T[r].values); 
            if m.sum()<10 or (~m).sum()<10: continue
            a=o.pnl.values[m].sum()/o.coste.values[m].sum(); b=o.pnl.values[~m].sum()/o.coste.values[~m].sum()
            nl=[]; p_=o.pnl.values; c_=o.coste.values
            for _ in range(2000):
                pr=rng.permutation(len(p_)); nl.append(p_[pr][m].sum()/c_[pr][m].sum()-p_[pr][~m].sum()/c_[pr][~m].sum())
            nl=np.array(nl); P(nm,cs,r,lab,'n_si %d n_no %d EV_si %.4f EV_no %.4f diff %.4f p_marg %.3f | coste_si %.0f wallet top_si %.1f%%'%(m.sum(),(~m).sum(),a,b,a-b,(np.abs(nl)>=abs(a-b)).mean(),c_[m].sum(),100*c_[m].max()/c_[m].sum()))
# ---- (3) estratos volumen x precio medio (rasgos DESC, EV HOLD) universo BTC y ALL
P('=== (3) estratos: tercil de volumen (r11) x tercil de precio medio (r05) -> EV maker HOLD (rasgos de DESC)')
for cs in ['BTC','ALL']:
    T=traits(UD,cs); o=agg(UH,cs); el=T.index[T.cost>=500].intersection(o.index[o.coste>=200]); T=T.loc[el]; o=o.loc[el]
    T['v3']=pd.qcut(T['r11_logdia'].rank(method='first'),3,labels=['V1','V2','V3']); T['p3']=pd.qcut(T['r05_pc_medio'].rank(method='first'),3,labels=['P1bajo','P2','P3alto'])
    T['c3']=pd.qcut(T['r17_ord_unidad'].rank(method='first'),3,labels=['O1','O2','O3'])
    J=T.join(o)
    for a,b in [('v3','p3'),('v3','c3'),('p3','c3')]:
        r=J.groupby([a,b],observed=True).apply(lambda z: pd.Series(dict(n=len(z),coste=z.coste.sum(),EV=z.pnl.sum()/z.coste.sum(),EVreb=(z.pnl.sum()+z.reb.sum())/z.coste.sum())))
        P(cs,a,'x',b); P(r.round(4).to_string())
    # mediana/ % positivos
    P(cs,'% makers con EV HOLD>0 por tercil volumen:',J.groupby('v3',observed=True).apply(lambda z:(z.pnl>0).mean()).round(3).to_dict())
