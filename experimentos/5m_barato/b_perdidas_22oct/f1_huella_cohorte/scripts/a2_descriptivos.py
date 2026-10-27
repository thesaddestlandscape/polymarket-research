#!/usr/bin/env python3
"""a2: descriptivos del PREREG (no contrastes): BTC vs alts, banda x tamano, estandarizacion por celda, huella de W/21f4/e290/86b1 y lookalikes."""
import sys; sys.path.insert(0,'.')
import lib
from lib import *
rng=np.random.default_rng(777)
out=open(D+'a2_resultados.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s,flush=True); out.write(s+'\n')
pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',200)
COLS=['maker','rolM','coin','dia','yes','coste','pcw','des_yes','acc','fee','n']
U=outcome(load(DESC+HOLD,cols=COLS)); U=U[U.rolM].copy()
U['pcm']=U.pcw/U.coste; EDG=[0,0.05,0.10,0.20,0.30,0.50,0.70,0.90,1.0]; U['banda']=np.clip(np.digitize(U.pcm.values,EDG)-1,0,7)
BN=['<.05','.05-.10','.10-.20','.20-.30','.30-.50','.50-.70','.70-.90','>=.90']
per={'DESC':U[U.dia.isin(DI)],'HOLD':U[U.dia.isin(HI)]}; Ufull=U
def ev2(g): return pd.Series(dict(coste=g.coste.sum(),EV=g.pnl.sum()/g.coste.sum(),EVreb=(g.pnl.sum()+g.reb.sum())/g.coste.sum(),n=len(g)))
# A. por moneda x periodo
P('=== A. EV maker por moneda y periodo (ponderado por €; reb separado)')
for pn,X in per.items():
    r=X.groupby('coin').apply(ev2); r.index=[COINS[i] for i in r.index]; P(pn); P(r.round(4).to_string())
# B. banda x moneda (BTC vs ALT)
P('=== B. EV por banda de precio (pc medio de la unidad), BTC vs ALT')
for pn,X in per.items():
    X=X.assign(g=np.where(X.coin==0,'BTC','ALT')); r=X.groupby(['g','banda']).apply(ev2); r.index=[(a,BN[b]) for a,b in r.index]; P(pn); P(r.round(4).to_string())
# C. tamaño del maker (coste del periodo, todas las monedas) x moneda
P('=== C. EV por tamano de maker (terciles de coste maker en el periodo + top50) x BTC/ALT; n makers; % makers con EV>0 (>=20 unidades)')
for pn,X in per.items():
    tot=X.groupby('maker').coste.sum(); q=tot.rank(pct=True); top50=tot.nlargest(50).index
    X=X.assign(tam=np.where(X.maker.isin(top50),'top50',np.where(X.maker.map(q)>2/3,'T3',np.where(X.maker.map(q)>1/3,'T2','T1'))))
    X['g']=np.where(X.coin==0,'BTC','ALT')
    r=X.groupby(['g','tam']).apply(ev2); P(pn); P(r.round(4).to_string())
    for g in ['BTC','ALT']:
        Y=X[X.g==g]; mm=Y.groupby('maker').agg(c=('coste','sum'),p=('pnl','sum'),n=('n','sum')); big=mm.nlargest(48,'c')
        P('  top48 por coste en',g,':',(big.p>0).sum(),'/48 positivos; EV ponderado %.4f; coste top48 %.0f de %.0f (%.1f%%)'%(big.p.sum()/big.c.sum(),big.c.sum(),mm.c.sum(),100*big.c.sum()/mm.c.sum()))
        rest=mm.drop(big.index); rest=rest[rest.c>=500]; P('  resto con coste>=500: %d makers, %.1f%% positivos, EV %.4f'%(len(rest),100*(rest.p>0).mean(),rest.p.sum()/rest.c.sum()))
# D. estandarizacion por celda (dia, moneda, banda, lado): top-50 (por coste del periodo) vs resto
P('=== D. ventaja de los 48-50 mayores vs resto DENTRO de celda (dia,moneda,banda,lado), ponderada por coste de los grandes')
for pn,X in per.items():
    tot=X.groupby('maker').coste.sum(); top=set(tot.nlargest(50).index); X=X.assign(big=X.maker.isin(top))
    X['g']=np.where(X.coin==0,'BTC','ALT')
    for g in ['BTC','ALT']:
        Y=X[X.g==g]; cell=Y.groupby(['dia','coin','banda','yes','big'])[['pnl','coste']].sum().unstack('big').fillna(0)
        cell=cell[(cell[('coste',True)]>10)&(cell[('coste',False)]>10)]
        evb=cell[('pnl',True)]/cell[('coste',True)]; evr=cell[('pnl',False)]/cell[('coste',False)]; w=cell[('coste',True)]
        d=((evb-evr)*w).sum()/w.sum(); evbig=Y[Y.big].pnl.sum()/Y[Y.big].coste.sum(); evrest=Y[~Y.big].pnl.sum()/Y[~Y.big].coste.sum()
        # bootstrap por dia
        days=cell.index.get_level_values(0).unique().values; bs=[]
        for _ in range(2000):
            dd=rng.choice(days,len(days)); parts=[((evb-evr)*w)[cell.index.get_level_values(0)==x] for x in dd]; ww=[w[cell.index.get_level_values(0)==x] for x in dd]
            bs.append(pd.concat(parts).sum()/pd.concat(ww).sum())
        P(pn,g,'EV grandes %.4f EV resto %.4f diff bruta %.4f | diff intra-celda %.4f IC90 por dias (%.4f,%.4f) celdas %d'%(evbig,evrest,evbig-evrest,d,*np.percentile(bs,[5,95]),len(cell)))
# E. huella de los 4 + lookalikes (rasgos DESC)
P('=== E. huella de los 4 ganadores ex-post (NO evidencia independiente) y lookalikes')
del U,per
U0=load(DESC+HOLD,cols=['maker','coste','rolM']); tot_=U0.groupby('maker').coste.sum(); keep=tot_.index[tot_>=200].values; del U0
UA=outcome(load(DESC+HOLD,keep=keep)); UD=UA[UA.dia.isin(DI)]; UH=UA[UA.dia.isin(HI)]
names=np.array(lib.NAMES); 
def find(pref): 
    ix=[i for i,n in enumerate(names) if n.startswith(pref)]; return ix
W4={p:find(p) for p in ['0xb0f85baa','0x21f4c1a1','0xe29042f5','0x86b14772']}
P('direcciones:',{k:[names[i] for i in v] for k,v in W4.items()})
TD=traits(UD,'ALL'); TH=traits(UH,'ALL'); TDb=traits(UD,'BTC'); 
el=TD.index[TD.cost>=500]
rk=TD.loc[el,TRAITS].rank(pct=True)
rows=[]
for k,v in W4.items():
    if not v or v[0] not in TD.index: P(k,'sin rasgos en DESC'); continue
    i=v[0]; rows.append(pd.Series(rk.loc[i] if i in rk.index else TD.loc[i,TRAITS].rank(pct=True),name=k))
    P(k,'rasgos DESC (valor) :',TD.loc[i,TRAITS].round(3).to_dict(), '| coste maker DESC %.0f'%TD.loc[i,'cost'])
if rows: P('percentil de cada rasgo entre elegibles (cost>=500, universo ALL, DESC)'); P(pd.DataFrame(rows).round(2).to_string())
def evm(X,mk,coin=None):
    Y=X[X.maker.isin(mk)]; 
    if coin=='BTC': Y=Y[Y.coin==0]
    if coin=='ALT': Y=Y[Y.coin>0]
    return Y.pnl.sum()/max(Y.coste.sum(),1e-9),Y.coste.sum()
for k,v in W4.items():
    P(k,'EV maker DESC %.4f (coste %.0f) HOLD %.4f (coste %.0f)'%(*evm(UD[UD.rolM],v),*evm(UH[UH.rolM],v)))
# lookalikes: distancia en rasgos (percentiles) al centroide de los 4 (o a cada uno), excluyendo los 4
W_all=[i for v in W4.values() for i in v]
Z=rk.drop(index=[i for i in W_all if i in rk.index]); wr=pd.DataFrame(rows)
cent=wr.mean()
PH=UH[UH.rolM].groupby('maker')[['pnl','coste','reb']].sum()
for K in (20,50):
    d=((Z-cent)**2).sum(1)**0.5; near=d.nsmallest(K).index
    cand=PH.reindex(near).dropna(); cand=cand[cand.coste>=200]
    base=PH.reindex(Z.index).dropna(); base=base[base.coste>=200]
    ev_n=cand.pnl.sum()/cand.coste.sum(); ev_b=base.pnl.sum()/base.coste.sum()
    nl=[]
    for _ in range(2000):
        s=base.sample(len(cand),random_state=int(rng.integers(1e9))); nl.append(s.pnl.sum()/s.coste.sum())
    P('LOOKALIKES K=%d (distancia en percentiles de 20 rasgos al centroide de los 4; evaluables HOLD n=%d): EV HOLD %.4f (con reb %.4f) vs elegibles %.4f; p placebo (muestra aleatoria igual tamano) %.3f; %% positivos %.0f%%; coste %.0f; wallet top %.0f%%'%(K,len(cand),ev_n,(cand.pnl.sum()+cand.reb.sum())/cand.coste.sum(),ev_b,(np.abs(np.array(nl)-ev_b)>=abs(ev_n-ev_b)).mean(),100*(cand.pnl>0).mean(),cand.coste.sum(),100*cand.coste.max()/cand.coste.sum()))
# rasgos que distinguen a cada uno de los 4 de los perdedores: en DESC, comparar con makers elegibles con EV_DESC<0
PD=UD[UD.rolM].groupby('maker')[['pnl','coste']].sum(); lose=PD.index[(PD.pnl<0)&(PD.coste>=2000)].intersection(el)
win_=PD.index[(PD.pnl>0)&(PD.coste>=2000)].intersection(el)
P('perdedores DESC (coste>=2000, EV<0): %d; ganadores DESC: %d'%(len(lose),len(win_)))
cmp=pd.DataFrame({'med_perd':TD.loc[lose,TRAITS].median(),'med_gan':TD.loc[win_,TRAITS].median()})
for k,v in W4.items():
    if v and v[0] in TD.index: cmp[k[:10]]=TD.loc[v[0],TRAITS]
P(cmp.round(3).to_string())
