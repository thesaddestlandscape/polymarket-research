#!/usr/bin/env python3
"""r5: diseccion de los 3 ganadores BTC 5m vs 3 perdedores de volumen parecido, desde el libro mayor on-chain (r4_fills).
Unidad mercado+lado, desenlace oficial (des.json), rebate = 0.014(1-pc)*coste solo en rellenos MAKER. Contrafactual 'celda': mismo dia, banda de precio, tb (tramo T) y lado
con el EV de TODOS los demas makers (leave-one-out) sobre cells_*.csv.gz -> parte del PnL explicada por la mezcla de celdas; residuo = seleccion dentro de la celda.
Salida datos/r5_diseccion.txt"""
import pandas as pd,numpy as np,json,glob,collections
R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'; DL='/root/polymarket-research-datalogs/mapa_escala/'
out=open(R+'rebate_ganadores/datos/r5_diseccion.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
des=json.load(open(DL+'des.json')); TOK=json.load(open(DL+'tokens.json'))
X=pd.read_csv(R+'rebate_ganadores/datos/r4_fills.csv.gz',usecols=['dia','maker','rol','coin','mid','lc','pc','coste','acc','T','fee'],dtype={'mid':'category','maker':'category','rol':'category','coin':'category','lc':'category','dia':'category'})
X['mid']=X.mid.astype(str)
X=X[(X.acc>0)&(X.coste>0)&(X.pc>=0.01)&(X.pc<0.99)&(X['T']>=-5)].copy()
X['des']=X.mid.map(des); P('cobertura desenlace oficial: %.4f de %d fills (coste)'%(X[X.des.notna()].coste.sum()/X.coste.sum(),len(X)))
X=X[X.des.notna()].copy(); X['gana']=(X.lc==X.des).astype(float); X['pnl']=X.acc*X.gana-X.coste-np.where(X.rol=='T',X.fee.fillna(0),0)
X['reb']=np.where(X.rol=='M',0.014*(1-X.pc)*X.coste,0.0)
EDG=np.array([0.01,0.05,0.10,0.20,0.30,0.50,0.70,0.90,0.99]); TEDG=np.array([-5,60,150,300,900,3600])
X['banda']=np.digitize(X.pc.values,EDG)-1; X['tb']=np.digitize(X['T'].values,TEDG)-1
name={}
for a in X.maker.astype(str).unique(): name[a]=a[:10]
# poblacion: cells BTC 5min por (dia,banda,tb,lc)
pop=[]; NM=set()
for f in sorted(glob.glob(DL+'cells_2026-10-*.csv.gz')):
    c=pd.read_csv(f,usecols=['dia','marco','coin','maker','mid','lc','banda','tb','coste','acc'],dtype={'mid':str,'maker':'category','marco':'category','coin':'category'})
    c=c[(c.marco=='5min')&(c.coin=='BTC')].copy(); c['des']=c.mid.map(des); c=c[c.des.notna()]
    c['pnl']=c.acc*(c.lc==c.des)-c.coste; pop.append(c.groupby(['dia','banda','tb','lc'])[['coste','pnl']].sum().reset_index()); NM.update(c.maker.unique())
pop=pd.concat(pop); P('poblacion BTC 5m: coste %.0f M, makers %d'%(pop.coste.sum()/1e6,len(NM)))
tot=pop.groupby(['dia','banda','tb','lc'])[['coste','pnl']].sum()
Xb=X[X.coin=='BTC'].copy()
X['maker']=X.maker.astype(str); X['rol']=X.rol.astype(str); X['lc']=X.lc.astype(str); X['dia']=X.dia.astype(str); X['coin']=X.coin.astype(str)
cls={a:('GAN' if a[:10] in ('0x21f4c1a1','0xe29042f5','0x86b14772') else 'PERD') for a in X.maker.unique()}
P('\n== 1. PnL por wallet (BTC 5m, 06..21-Oct, desenlace oficial) ==')
P('wallet  clase  coste_M  coste_T  pnl_M  pnl_T  reb_inf  EV_M(sin reb) EV_M(+reb)  dias  mercados  fills')
rows=[]
for a,g in Xb.groupby('maker'):
    M=g[g.rol=='M']; T=g[g.rol=='T']
    P(f"{a[:10]} {cls[a]:4s} {M.coste.sum():>10,.0f} {T.coste.sum():>9,.0f} {M.pnl.sum():>9,.0f} {T.pnl.sum():>8,.0f} {M.reb.sum():>7,.0f}  {M.pnl.sum()/M.coste.sum():+.4f} {(M.pnl.sum()+M.reb.sum())/M.coste.sum():+.4f}  {g.dia.nunique():3d} {g.mid.nunique():6d} {len(g):8d}")
P('\n== 2. PnL diario (M, sin y con rebate) y sin 2 mejores dias; IC90 por dias del EV ponderado ==')
rng=np.random.default_rng(3)
for a,g in Xb[Xb.rol=='M'].groupby('maker'):
    d=g.groupby('dia').agg(c=('coste','sum'),p=('pnl','sum'),r=('reb','sum'))
    ev=(d.p+d.r).sum()/d.c.sum(); s2=d.sort_values('p',ascending=False).iloc[2:]
    bs=[ (lambda i:(d.p.values[i]+d.r.values[i]).sum()/d.c.values[i].sum())(rng.integers(0,len(d),len(d))) for _ in range(2000)]
    P(f"{a[:10]} {cls[a]} dias+ {(d.p+d.r>0).sum()}/{len(d)} pnl_dia(+reb) med {np.median(d.p+d.r):,.0f} | EV+reb {ev:+.4f} IC90 dias ({np.percentile(bs,5):+.4f},{np.percentile(bs,95):+.4f}) | sin 2 mejores {(s2.p+s2.r).sum()/s2.c.sum():+.4f}")
P('\n== 3. Contrafactual de CELDA (dia,banda,tb,lado) con EV de los demas makers (leave-one-out) ==')
for a,g in Xb[Xb.rol=='M'].groupby('maker'):
    gg=g.groupby(['dia','banda','tb','lc']).agg(c=('coste','sum'),p=('pnl','sum')).reset_index()
    t=tot.reindex(pd.MultiIndex.from_frame(gg[['dia','banda','tb','lc']])).fillna(0)
    oc=t.coste.values-gg.c.values; op=t.pnl.values-gg.p.values
    ok=oc>50; ev=np.where(ok,op/np.maximum(oc,1),0.0)
    exp=(gg.c.values*ev)[ok].sum(); real=gg.p.values[ok].sum(); c=gg.c.values[ok].sum()
    P(f"{a[:10]} {cls[a]} cobertura celdas {c/gg.c.sum():.3f} | PnL real {real:,.0f} vs esperado por mezcla de celdas {exp:,.0f} -> explica {exp/real if real else float('nan'):.2f} ; residuo (seleccion dentro de celda) {real-exp:+,.0f} = {(real-exp)/c:+.4f} por EUR")
P('\n== 4. Perfil: banda, T, lado, tamaño ==')
for a,g in Xb[Xb.rol=='M'].groupby('maker'):
    bb=g.groupby('banda').coste.sum()/g.coste.sum(); tt=g.groupby('tb').coste.sum()/g.coste.sum()
    P(f"{a[:10]} {cls[a]} coste por banda[0.01-.05,.05-.1,.1-.2,.2-.3,.3-.5,.5-.7,.7-.9,.9-.99]: "+' '.join(f"{bb.get(i,0):.2f}" for i in range(8))+" | por T[<=60,60-150,150-300]: "+' '.join(f"{tt.get(i,0):.2f}" for i in range(3))+f" | acc/fill med {g.acc.median():.1f} p90 {g.acc.quantile(.9):.0f} | pc med {g.pc.median():.2f}")
P('\n== 5. Cobertura de mercados e inventario (unidad mercado) ==')
nm=collections.Counter(v[2] for v in TOK.values() if v[0]=='BTC' and v[1]=='5min' and v[4]=='YES' and v[2] in des)
P('mercados BTC 5m con desenlace en 06..21-Oct:',len(nm))
for a,g in Xb.groupby('maker'):
    gm=g.groupby(['mid','lc']).agg(acc=('acc','sum'),c=('coste','sum'),p=('pnl','sum'),r=('reb','sum')).reset_index()
    pv=gm.pivot(index='mid',columns='lc',values='acc').fillna(0)
    for k in ('YES','NO'):
        if k not in pv: pv[k]=0.0
    mn=np.minimum(pv.YES,pv.NO); tt=pv.YES+pv.NO
    cob=g.mid.nunique()/len(nm); hed=(mn/tt>0.2)
    pp=gm.groupby('mid').p.sum()
    mkt=g.groupby('mid').agg(c=('coste','sum'),p=('pnl','sum'),r=('reb','sum'))
    P(f"{a[:10]} {cls[a]} mercados {g.mid.nunique()} ({cob:.2f} de todos) | acc/mercado med {tt.median():.0f} | cobertura de pares: share acc emparejada {mn.sum()/tt.sum():.3f}; mercados cubiertos (>=20% lado corto) {hed.mean():.2f}; solo un lado {(mn==0).mean():.2f}"
      f" | pnl mercado hedged {mkt.reindex(pv.index[hed]).p.sum():,.0f} vs no {mkt.reindex(pv.index[~hed]).p.sum():,.0f}")
P('\n== 6. Rol tomador: parte del PnL (BTC) ==')
for a,g in Xb.groupby('maker'):
    T=g[g.rol=='T']
    if len(T): P(f"{a[:10]} {cls[a]} tomador coste {T.coste.sum():,.0f} ({T.coste.sum()/g.coste.sum():.2%} del total) pnl neto fee {T.pnl.sum():,.0f} EV {T.pnl.sum()/T.coste.sum():+.4f}")

