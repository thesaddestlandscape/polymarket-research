# s5_poblacion.py: PREREG paso 1. Poblacion de rellenos MAKER on-chain 60m/4h, unidad (mercado,lado,bucket 0,05) por dia de fichero, desenlace gamma. Independiente de F2.
import pandas as pd, numpy as np, json, glob, os
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/fav_60m_4h/datos/'; O='/mnt/HC_Volume_106538179/agentes_datos/fav60_onchain/'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
G=json.load(open(D+'tokmap_gamma.json')); TK=G['tokens']; MK=G['mercados']
rng=np.random.default_rng(20261025); LIM={'60min':3600,'240min':14400}
cols=['tipo','bloque','ts_est','tx','log_index','order_hash','maker','taker','side','token_id','maker_amt','taker_amt','fee']
parts=[]
for f in sorted(glob.glob(O+'oc_*.csv.gz')):
    d=f[-17:-7]
    x=pd.read_csv(f,names=cols,header=None,dtype={'token_id':str,'tx':str,'taker':str,'maker':str})
    x=x[(x.tipo=='F')&(x.taker.str.lower()!=EXCH)].drop_duplicates(['tx','log_index'])
    v=x.token_id.map(TK); x=x[v.notna()]; v=v[v.notna()]
    x['coin']=[a[0] for a in v]; x['marco']=[a[1] for a in v]; x['mid']=[a[2] for a in v]; x['fin']=[a[3] for a in v]; x['out']=[a[4] for a in v]
    venta=x.side.astype(int).values==1
    acc=np.where(venta,x.maker_amt,x.taker_amt).astype(float); usdc=np.where(venta,x.taker_amt,x.maker_amt).astype(float)
    x['lc']=np.where(venta,np.where(x.out=='Up','Down','Up'),x.out); x['venta']=venta
    with np.errstate(all='ignore'): x['pc']=np.where(venta,1-usdc/acc,usdc/acc); x['coste']=np.where(venta,acc-usdc,usdc)
    x['acc']=acc; x['T']=x.fin-x.ts_est.astype(float); x['dia']=d
    parts.append(x[['dia','coin','marco','mid','fin','lc','venta','pc','coste','acc','T','maker']])
X=pd.concat(parts,ignore_index=True)
X=X[(X.acc>0)&(X.coste>0)&(X.pc>=0.01)&(X.pc<0.99)&(X['T']>60)&(X['T']<=X.marco.map(LIM))].copy()
X['b']=np.floor(X.pc/0.05+1e-9).astype(int)
X['w']=X.mid.map(lambda m: MK[m]['win'] if m in MK else None)
cob=X.groupby('marco').apply(lambda g: g.loc[g.w.notna(),'coste'].sum()/g.coste.sum()); print('cobertura coste con desenlace',cob.to_dict())
X=X[X.w.notna()]; X['win']=(X.w==X.lc).astype(float)
def unid(X):
    U=X.groupby(['dia','marco','coin','mid','lc','b']).agg(coste=('coste','sum'),acc=('acc','sum'),win=('win','first'),fin=('fin','first')).reset_index()
    U['pnl']=U.acc*U.win-U.coste; U['reb']=0.014*(1-U.coste/U.acc)*U.coste; return U
def stat(U,key='dia'):
    Dd=U.groupby(key).agg(c=('coste','sum'),p=('pnl','sum'),r=('reb','sum'))
    if len(Dd)==0 or Dd.c.sum()<=0: return {}
    ev=Dd.p.sum()/Dd.c.sum(); i=rng.integers(0,len(Dd),(4000,len(Dd))); bs=Dd.p.values[i].sum(1)/Dd.c.values[i].sum(1)
    s2=Dd.sort_values('p',ascending=False).iloc[2:]; 
    return dict(n_unid=len(U),dias=len(Dd),dias_pos=int((Dd.p>0).sum()),cierres=U.fin.nunique(),coste=round(Dd.c.sum()),ev=round(ev,4),ic90=(round(np.percentile(bs,5),4),round(np.percentile(bs,95),4)),
                ev_sin2=round(s2.p.sum()/s2.c.sum(),4) if len(s2) else None,ev_reb=round((Dd.p.sum()+Dd.r.sum())/Dd.c.sum(),4),hit=round((U.win*U.coste).sum()/U.coste.sum(),4),pmed=round(U.coste.sum()/U.acc.sum(),4))
U=unid(X); res={}
def cel(nombre,m): r=stat(U[m]); res[nombre]=r; print(nombre,r)
f60=(U.marco=='60min')&U.coin.isin(['BTC','ETH','SOL'])&(U.b>=14)&(U.b<18)
cel('60m_BTCETHSOL_070_090_18a23',f60&(U.dia<='2026-10-23'))
cel('60m_BTCETHSOL_070_090_18a24',f60)
cel('60m_BTCETHSOL_070_090_solo24',f60&(U.dia=='2026-10-24'))
f4=(U.marco=='240min')&(U.b>=13)&(U.b<=19)
cel('4h_ALL_065_099_18a23',f4&(U.dia<='2026-10-23')); cel('4h_ALL_065_099_18a24',f4)
for c in ['BTC','ETH','SOL','XRP','DOGE','BNB']:
    cel(f'60m_{c}_070_090_18a24',(U.marco=='60min')&(U.coin==c)&(U.b>=14)&(U.b<18))
    cel(f'4h_{c}_065_099_18a24',(U.marco=='240min')&(U.coin==c)&(U.b>=13))
for b in range(10,20): cel(f'60m_BTCETHSOL_b{b*5:02d}',(U.marco=='60min')&U.coin.isin(['BTC','ETH','SOL'])&(U.b==b))
# solo compras (sin ventas convertidas)
Ub=unid(X[~X.venta]); m=(Ub.marco=='60min')&Ub.coin.isin(['BTC','ETH','SOL'])&(Ub.b>=14)&(Ub.b<18); r=stat(Ub[m]); res['60m_070_090_solo_compras_18a24']=r; print('solo compras',r)
# flujo maker/dia celda 60m
res['flujo_60m_070_090_eur_dia']=round(U[f60].coste.sum()/U[f60].dia.nunique()); res['flujo_4h_065_099_eur_dia']=round(U[f4].coste.sum()/max(1,U[f4].dia.nunique()))
json.dump(res,open(D+'poblacion.json','w'),indent=1,default=str)
