import sys,json,csv,gzip
sys.path.insert(0,sys.argv[1]); S=sys.argv[1]
from common import *
from npbt import *
import os,gc
import pandas as pd, numpy as np
from datetime import date,timedelta
EX='0xe111180000d2663c0091e4f400237545b87b996b'
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
CA='/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
def from_raw(path,gm):
    tok={}
    for slug,v in gm.items():
        st=int(slug.rsplit('-',1)[1]); coin=slug.split('-')[0].upper()
        for t,l in zip(v['toks'],('YES','NO')): tok[t]=(coin,v['id'],st+300,l,v['des'])
    cols=['tipo','bloque','ts','tx','li','oh','maker','taker','side','tok','maker_amt','taker_amt','fee']
    R=pd.read_csv(path,header=None,names=cols,dtype={'tok':str,'tx':str,'maker':str,'taker':str},usecols=['tipo','ts','tx','maker','taker','side','tok','maker_amt','taker_amt'])
    R=R[(R.tipo=='F')&(R.taker.str.lower()!=EX)&R.tok.isin(tok.keys())].copy()
    R['maker']=R.maker.str.lower(); R['taker']=R.taker.str.lower()
    R['act']=R.tok.map(lambda t:tok[t][0]); R['mkt']=R.tok.map(lambda t:tok[t][1]); R['fin']=R.tok.map(lambda t:tok[t][2])
    R['lado']=R.tok.map(lambda t:tok[t][3]); R['des']=R.tok.map(lambda t:tok[t][4])
    return R.drop(columns=['tipo','tok'])
out=[]
days=[(date(2026,10,9)+timedelta(i)).isoformat() for i in range(13)]
for d in days:
    if os.path.exists(S+f'/pop_{d}.pkl'): continue
    if d<='2026-10-18':
        F=pd.read_parquet(CA+f'fills_{d}.parquet',columns=['tx','is_tk','maker','taker','side','act','mkt','lado','fin','ts','maker_amt','taker_amt'])
        F=F[(F.is_tk==0)&F.act.isin(['ETH','SOL','XRP'])].copy(); F['des']=F.mkt.astype(str).map(DES); F['tx']=F.tx.astype(str)
    else:
        gm=json.load(open(S+('/gmap19.json' if d=='2026-10-19' else '/gmap.json')))
        F=from_raw(S+f'/alt_{d[8:]}.csv',gm)
        # 20-oct: el fichero alt_20 es m5_onchain_20; alt_21 es onchain_21
    if not len(F): continue
    v=F.side.values==1
    F['sh']=np.where(v,F.maker_amt,F.taker_amt); usd=np.where(v,F.taker_amt,F.maker_amt)
    F['lado_c']=np.where(v,np.where(F.lado=='YES','NO','YES'),F.lado)
    F['pc']=np.where(v,1-usd/F.sh,usd/F.sh); F['coste_m']=np.where(v,F.sh-usd,usd); F['T']=F.fin-F.ts
    X=F[(F.sh>0)&(F.coste_m>0)&(F.pc>0.10)&(F.pc<=0.30)&(F['T']>60)&(F['T']<=300)].copy()
    cob=X.des.notna().mean(); X=X[X.des.notna()]
    X['gana']=(X.lado_c==X.des); X['pnl_m']=np.where(X.gana,X.sh,0)-X.coste_m
    X['dia']=d
    dd=[d,(date.fromisoformat(d)+timedelta(1)).isoformat()]
    dd=[x for x in dd if x<='2026-10-21']
    bt=load_bt_np(dd)
    tm=X.ts.values-2.4; sg=np.where(X.lado_c=='YES',1,-1); A=X.act.values
    for nm,(a0,a1) in dict(pre10x=(-10,-1.5),pre5x=(-5,-1.5),pre20x=(-20,-1.5),pre30x=(-30,-1.5)).items():
        r=np.full(len(X),np.nan)
        for a in ('ETH','SOL','XRP'):
            m=A==a; r[m]=ret_np(bt[a],tm[m]+a0,tm[m]+a1)
        X['bn_'+nm]=sg*r
    X[['dia','act','mkt','fin','ts','tx','maker','taker','lado_c','pc','sh','coste_m','pnl_m','gana','T','bn_pre10x','bn_pre5x','bn_pre20x','bn_pre30x']].to_pickle(S+f'/pop_{d}.pkl'); del bt,F; gc.collect()
    print(d,len(X),'cob',round(cob,4),'EV',round(X.pnl_m.sum()/X.coste_m.sum(),4),flush=True)
print('ok')
