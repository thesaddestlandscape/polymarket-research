# f2_extrae.py DIA MARCO ... : rellenos MAKER on-chain -> unidades (mercado, lado comprado, bucket 0,05) con T en (60,L]. Solo lectura de fuentes; escribe en OUT.
import pandas as pd, numpy as np, json, glob, sys, os
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
V='/mnt/HC_Volume_106538179'; OUT=V+'/agentes_datos/f2_menos_as'; os.makedirs(OUT,exist_ok=True)
SRC={'5min':V+'/m5_onchain/m5_onchain_%s.csv.gz','15min':V+'/m15_onchain/m15_onchain_%s.csv.gz','60min':V+'/agentes_datos/mapa_infra/m60_onchain/m60_onchain_%s.csv.gz',
     '240min':V+'/agentes_datos/mapa_infra/m240_onchain/m240_onchain_%s.csv.gz','24h':V+'/agentes_datos/mapa_infra/m24h_onchain/m24h_onchain_%s.csv.gz'}
LIM={'5min':300,'15min':900,'60min':3600,'240min':14400,'24h':86400}
TK={}
TK.update(json.load(open('/root/polymarket-research-datalogs/mapa_escala/tokens.json')))
TK.update(json.load(open('/root/polymarket-research-datalogs/mapa_escala/tokens_extra.json')))
for f in glob.glob(V+'/agentes_datos/mapa_infra/tokmap/*.k.json'): TK.update(json.load(open(f)))
for f in glob.glob(V+'/agentes_datos/mapa_infra/tokmap/gamma_*.json'):
    g=json.load(open(f)); TK.update(g.get('tokens',{}))
EDG=np.round(np.arange(0.0,1.0001,0.05),2)
def run(d,marco):
    tk={t:v for t,v in TK.items() if v[1]==marco}; ids=set(tk); parts=[]; nrow=0
    cfg=dict(usecols=['tipo','ts_est','tx','log_index','maker','taker','side','token_id','maker_amt','taker_amt'],dtype={'token_id':str,'tx':str,'maker':str,'taker':str},chunksize=300000)
    for x in pd.read_csv(SRC[marco]%d,**cfg):
        x=x[(x.tipo=='F')&(x.taker!=EXCH)&x.token_id.isin(ids)]
        if len(x)==0: continue
        nrow+=len(x); tkv=x.token_id.values
        coin=np.array([tk[t][0] for t in tkv]); mid=np.array([tk[t][2] for t in tkv]); fin=np.array([tk[t][3] for t in tkv],float); lado=np.array([tk[t][4] for t in tkv])
        venta=x.side.values==1
        acc=np.where(venta,x.maker_amt.values,x.taker_amt.values).astype(float); usdc=np.where(venta,x.taker_amt.values,x.maker_amt.values).astype(float)
        lc=np.where(venta,np.where(lado=='YES','NO','YES'),lado)
        with np.errstate(all='ignore'):
            pc=np.where(venta,1-usdc/acc,usdc/acc); coste=np.where(venta,acc-usdc,usdc)
        ts=x.ts_est.astype(float).values
        parts.append(pd.DataFrame(dict(tx=x.tx.values,li=x.log_index.values.astype(np.int64),coin=coin,mid=mid,fin=fin,ts=ts,T=fin-ts,lc=lc,pc=pc,coste=coste,acc=acc,maker=x.maker.str.lower().values)))
    if not parts: return None,0,0
    X=pd.concat(parts,ignore_index=True); n0=len(X); X=X.drop_duplicates(['tx','li']); ndup=n0-len(X)
    X=X[(X.acc>0)&(X.coste>0)&(X.pc>=0.01)&(X.pc<0.99)&(X['T']>60)&(X['T']<=LIM[marco])].copy()
    X['b']=(np.floor(X.pc.values/0.05+1e-9)).astype(int)   # 0..19 -> [0.05*b, 0.05*(b+1))
    return X,nrow,ndup
def unidades(X,d,marco):
    X=X.sort_values(['mid','lc','b','ts','li']); g=X.groupby(['mid','lc','b'],sort=False)
    X['cacc']=g.acc.cumsum(); X['prev']=X.cacc-X.acc
    X['acc5']=np.clip(5-X.prev,0,X.acc); X['coste5']=X.coste*X.acc5/X.acc
    U=g.agg(coin=('coin','first'),fin=('fin','first'),coste=('coste','sum'),acc=('acc','sum'),nf=('coste','size'),coste5=('coste5','sum'),acc5=('acc5','sum'),ts0=('ts','min'),Tmed=('T','median'),nmak=('maker','nunique')).reset_index()
    U['dia']=d; U['marco']=marco
    M=X.groupby(['coin','b','maker']).coste.sum().reset_index(); M['dia']=d; M['marco']=marco
    return U,M
if __name__=='__main__':
    d=sys.argv[1]
    for marco in sys.argv[2:]:
        fu=f'{OUT}/u_{marco}_{d}.csv.gz'
        if os.path.exists(fu): continue
        if not os.path.exists(SRC[marco]%d): print(d,marco,'SIN FUENTE',flush=True); continue
        X,nrow,ndup=run(d,marco)
        if X is None: print(d,marco,'vacio',flush=True); continue
        U,M=unidades(X,d,marco); U.to_csv(fu+'.tmp',index=False,compression='gzip'); os.replace(fu+'.tmp',fu)
        M.to_csv(f'{OUT}/m_{marco}_{d}.csv.gz',index=False,compression='gzip')
        print(d,marco,'fills maker',nrow,'dup',ndup,'ventana',len(X),'unid',len(U),'coste',round(X.coste.sum()),flush=True)
