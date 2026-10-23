# s2: celdas (dia, marco, coin, maker, mid, lado_c, banda, tb) de rellenos MAKER on-chain + exposicion concurrente por nicho. Solo lectura de fuentes; escribe en datalogs/mapa_escala.
import pandas as pd, numpy as np, json, gzip, sys, os
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
DL='/root/polymarket-research-datalogs'; OUT=DL+'/mapa_escala'; V='/mnt/HC_Volume_106538179'
TOK=json.load(open(OUT+'/tokens.json'))
EDG=np.array([0.01,0.05,0.10,0.20,0.30,0.50,0.70,0.90,0.99]); TEDG=np.array([-5,60,150,300,900,3600])
LIM={'5min':300,'15min':900,'60min':3600}
T0=int(pd.Timestamp('2026-10-06',tz='UTC').timestamp()); NMIN=16*1440+1500
def run(d,marco,src):
    tk={t:v for t,v in TOK.items() if v[1]==marco}
    ids=set(tk); parts=[]; nrow=0
    cfg=dict(usecols=['tipo','ts_est','tx','log_index','maker','taker','side','token_id','maker_amt','taker_amt'],dtype={'token_id':str,'tx':str,'maker':str,'taker':str},chunksize=300000)
    for x in pd.read_csv(src,**cfg):
        x=x[(x.tipo=='F')&(x.taker!=EXCH)&x.token_id.isin(ids)]
        if len(x)==0: continue
        nrow+=len(x); tkv=x.token_id.values
        coin=np.array([tk[t][0] for t in tkv]); mid=np.array([tk[t][2] for t in tkv]); fin=np.array([tk[t][3] for t in tkv],float); lado=np.array([tk[t][4] for t in tkv])
        venta=x.side.values==1
        acc=np.where(venta,x.maker_amt.values,x.taker_amt.values).astype(float); usdc=np.where(venta,x.taker_amt.values,x.maker_amt.values).astype(float)
        lc=np.where(venta,np.where(lado=='YES','NO','YES'),lado)
        with np.errstate(all='ignore'):
            pc=np.where(venta,1-usdc/acc,usdc/acc); coste=np.where(venta,acc-usdc,usdc)
        ts=x.ts_est.astype(float).values; T=fin-ts
        parts.append(pd.DataFrame(dict(tx=x.tx.values,li=x.log_index.values,coin=coin,mid=mid,fin=fin,ts=ts,T=T,lc=lc,pc=pc,coste=coste,acc=acc,maker=x.maker.str.lower().values)))
    X=pd.concat(parts,ignore_index=True)
    n0=len(X); X=X.drop_duplicates(['tx','li']); ndup=n0-len(X)
    X=X[(X.acc>0)&(X.coste>0)&(X.pc>=0.01)&(X.pc<0.99)&(X['T']>=-5)].copy()
    X['banda']=np.digitize(X.pc.values,EDG)-1       # 0..7
    X['tb']=np.digitize(X['T'].values,TEDG)-1        # 0:<=60 1:(60,150] 2:(150,300] 3:(300,900] 4:(900,3600] 5:>3600 (digitize: -5..60 ->0)
    X['reb']=0.014*(1-X.pc)*X.coste
    X['dia']=d; X['marco']=marco
    # exposicion: solo T en (60,L]
    E=X[(X['T']>60)&(X['T']<=LIM[marco])]
    return X,E,nrow,ndup
def agg(X):
    g=X.groupby(['dia','marco','coin','maker','mid','lc','banda','tb'],sort=False).agg(coste=('coste','sum'),acc=('acc','sum'),reb=('reb','sum'),nf=('coste','size'),fin=('fin','first')).reset_index()
    return g
expo={}   # (marco,coin,banda) -> diff array
def add_expo(E,marco):
    for (coin,b),g in E.groupby(['coin','banda']):
        a=expo.setdefault((marco,coin,int(b)),np.zeros(NMIN+2))
        i0=np.clip(((g.ts.values-T0)//60).astype(int),0,NMIN); i1=np.clip(((g.fin.values-T0)//60).astype(int)+1,0,NMIN)
        np.add.at(a,i0,g.coste.values); np.add.at(a,i1,-g.coste.values)
dias=sys.argv[1:] or [f'2026-10-{i:02d}' for i in range(6,22)]
for d in dias:
    res=[]
    for marco,src in [('5min',f'{V}/m5_onchain/m5_onchain_{d}.csv.gz'),('15min',f'{V}/m15_onchain/m15_onchain_{d}.csv.gz')]+([('60min',f'{DL}/onchain_fills_{d}.csv.gz')] if d in ('2026-10-18','2026-10-19','2026-10-20','2026-10-21') else []):
        X,E,nrow,ndup=run(d,marco,src); add_expo(E,marco); res.append(agg(X))
        print(d,marco,'fills maker',nrow,'dup',ndup,'coste',round(X.coste.sum()),flush=True)
    pd.concat(res).to_csv(f'{OUT}/cells_{d}.csv.gz',index=False)
np.savez_compressed(OUT+'/expo.npz',**{f'{k[0]}|{k[1]}|{k[2]}':np.cumsum(v) for k,v in expo.items()})
